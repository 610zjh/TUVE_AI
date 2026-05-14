#!/usr/bin/env python3
"""
文档理解 CLI 工具
使用 SEE2AI 多模态大模型 API 对文档（PDF等）进行解析和理解

用法:
    python document_understanding.py <document_url> [prompt]
    python document_understanding.py https://example.com/document.pdf "总结这份文档"
"""

import argparse
import json
import os
import sys

import requests


# API 配置
# 只保留 Gemini 作为唯一后端，避免调用已下线的旧文档识别能力。
MODEL_ENDPOINT_PATH = "/api/v1/actions/see2ai_llm_gemini_pro_v1"
DEFAULT_MODEL = "gemini"
DEFAULT_PROMPT = "请详细总结这份文档的主要内容"
_WRAPPER_QUOTES = ("`", '"', "'")
DOCUMENT_MISSING_PATTERNS = (
    "忘记在提问中附上或粘贴文档的具体内容",
    "请您将需要解析的文档文本直接发送给我",
    "未收到文档内容",
    "没有收到文档内容",
    "请直接发送文档文本",
)


def normalize_input(value: str | None) -> str:
    """清洗输入文本，去掉常见的成对包裹引号/反引号"""
    if value is None:
        return ""

    normalized = str(value).strip()
    # 修改原因：上游可能从 Markdown 或日志中提取 URL，常会夹带反引号，需先清洗再校验。
    while len(normalized) >= 2 and normalized[0] == normalized[-1] and normalized[0] in _WRAPPER_QUOTES:
        normalized = normalized[1:-1].strip()
    return normalized


def parse_config(config_input: str) -> dict:
    """解析 JSON 配置，支持 JSON 字符串或 JSON 文件路径"""
    config_input = config_input.strip()

    # 尝试作为文件路径读取
    if not config_input.startswith("{") and os.path.isfile(config_input):
        try:
            with open(config_input, encoding="utf-8") as f:
                config = json.load(f)
            if not isinstance(config, dict):
                print("错误: JSON 文件内容必须是一个对象（字典）", file=sys.stderr)
                sys.exit(1)
            return config
        except json.JSONDecodeError as e:
            print(f"错误: JSON 文件解析失败: {e}", file=sys.stderr)
            sys.exit(1)
        except OSError as e:
            print(f"错误: 读取配置文件失败: {e}", file=sys.stderr)
            sys.exit(1)

    # 尝试作为 JSON 字符串解析
    try:
        config = json.loads(config_input)
        if not isinstance(config, dict):
            print("错误: JSON 内容必须是一个对象（字典）", file=sys.stderr)
            sys.exit(1)
        return config
    except json.JSONDecodeError as e:
        print(f"错误: JSON 解析失败: {e}", file=sys.stderr)
        print('正确格式示例: --config \'{"document_url": "https://example.com/doc.pdf"}\'', file=sys.stderr)
        sys.exit(1)


def get_base_url() -> str:
    """从环境变量获取 Base URL"""
    base_url = os.environ.get("SEE2AI_BASE_URL")
    if not base_url:
        print("错误: 未设置 SEE2AI_BASE_URL 环境变量", file=sys.stderr)
        print("请设置环境变量: export SEE2AI_BASE_URL='https://see2ai.com'", file=sys.stderr)
        sys.exit(1)
    return base_url.rstrip('/')


def get_api_key() -> str:
    """从环境变量获取 API Key"""
    api_key = os.environ.get("SEE2AI_API_KEY")
    if not api_key:
        print("错误: 未设置 SEE2AI_API_KEY 环境变量", file=sys.stderr)
        print("请设置环境变量: export SEE2AI_API_KEY='sk-your-api-key'", file=sys.stderr)
        sys.exit(1)
    return api_key


def validate_url(url: str, url_type: str = "URL") -> str:
    """验证 URL 格式"""
    url = normalize_input(url)

    if not url:
        raise argparse.ArgumentTypeError(
            f"{url_type} 不能为空\n"
            f"正确用法示例:\n"
            f"  python document_understanding.py https://example.com/document.pdf"
        )

    if not url.startswith(("http://", "https://")):
        raise argparse.ArgumentTypeError(
            f"{url_type} 必须以 http:// 或 https:// 开头，收到: '{url}'\n"
            f"正确用法示例:\n"
            f"  python document_understanding.py https://example.com/document.pdf"
        )

    return url


def parse_streaming_response(response: requests.Response) -> dict:
    """聚合 SSE 响应，兼容底层流式 action 接口"""
    accumulated = []
    thinking_parts = []
    last_usage = {}
    last_source = ""
    last_model = ""
    saw_sse_event = False

    for raw_line in response.iter_lines(decode_unicode=True):
        if not raw_line:
            continue

        line = str(raw_line).strip()
        if not line.startswith("data:"):
            continue

        saw_sse_event = True
        data_str = line[len("data:"):].strip()
        if data_str == "[DONE]":
            break

        try:
            event = json.loads(data_str)
        except json.JSONDecodeError:
            continue

        piece = event.get("response")
        if piece:
            accumulated.append(piece)

        thinking = event.get("thinking_content")
        if thinking:
            thinking_parts.append(thinking)

        if event.get("usage"):
            last_usage = event["usage"]
        if event.get("source"):
            last_source = event["source"]
        if event.get("model"):
            last_model = event["model"]

    # 修改原因：兼容服务端偶发直接返回 JSON 的情况，避免只支持 SSE 导致空结果。
    if not saw_sse_event:
        return response.json()

    return {
        "response": "".join(accumulated),
        "thinking_content": "".join(thinking_parts) or None,
        "usage": last_usage,
        "source": last_source,
        "model": last_model or last_source,
    }


def detect_document_missing(result: dict) -> str | None:
    """识别模型未真正收到文档时的通用兜底话术"""
    response_text = str(result.get("response", "") or "")
    lowered = response_text.lower()
    for pattern in DOCUMENT_MISSING_PATTERNS:
        if pattern in response_text or pattern.lower() in lowered:
            return response_text
    return None


def ensure_document_received(result: dict, document_url: str, model: str) -> None:
    """将“模型未收到文档”从软失败升级成显式错误，便于上游定位问题"""
    missing_message = detect_document_missing(result)
    if not missing_message:
        return

    usage = result.get("usage") or {}
    print("错误: 文档理解接口返回了“未收到文档内容”的兜底回复", file=sys.stderr)
    print("这通常表示服务端没有正确消费 document_urls，虽然 HTTP 调用本身成功。", file=sys.stderr)
    print(f"模型: {result.get('model') or model}", file=sys.stderr)
    print(f"来源: {result.get('source') or 'unknown'}", file=sys.stderr)
    print(f"文档 URL: {document_url}", file=sys.stderr)
    if usage:
        print(
            "Token 使用: "
            f"input={usage.get('input_tokens', 0)}, "
            f"output={usage.get('output_tokens', 0)}, "
            f"total={usage.get('total_tokens', 0)}",
            file=sys.stderr,
        )
    print("模型原始回复预览:", file=sys.stderr)
    print(missing_message[:1000], file=sys.stderr)
    sys.exit(2)


def understand_document(
    document_url: str,
    prompt: str = DEFAULT_PROMPT,
    model: str = DEFAULT_MODEL,
) -> dict:
    """
    调用 SEE2AI API 对文档进行理解

    Args:
        document_url: 文档的公网 URL
        prompt: 对文档的提问或提示词
        model: 模型名称（当前仅支持 gemini）

    Returns:
        API 返回的完整结果字典
    """
    api_key = get_api_key()
    endpoint = f"{get_base_url()}{MODEL_ENDPOINT_PATH}"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    # Gemini 是当前唯一支持的文档理解模型，统一使用相同请求体。
    payload = {
        "query": prompt,
        "document_urls": [document_url],
        # 修改原因：旧版 SEE2AI LLM 封装长期走流式，多模态附件在流式路径上更稳定。
        "stream": True,
    }

    try:
        response = requests.post(endpoint, json=payload, headers=headers, timeout=120, stream=True)
        response.raise_for_status()
        result = parse_streaming_response(response)
        ensure_document_received(result, document_url=document_url, model=model)
        return result
    except requests.exceptions.Timeout:
        print("错误: 请求超时", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"HTTP 错误: {e}", file=sys.stderr)
        if response.status_code == 401:
            print("API Key 无效或余额不足", file=sys.stderr)
        elif response.status_code == 422:
            print("请求参数错误，请检查文档 URL 是否有效", file=sys.stderr)
        elif response.status_code == 429:
            print("请求频率超限，请稍后重试", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}", file=sys.stderr)
        sys.exit(1)


def parse_result(result: dict) -> str:
    """
    从 API 返回结果中提取文档解析内容

    Args:
        result: API 返回的字典

    Returns:
        文档解析文本内容
    """
    if not isinstance(result, dict):
        return "错误: 无效的响应格式"

    # 提取主要响应内容
    response_text = result.get("response", "")

    # 如果有思考内容，也一并返回
    thinking_content = result.get("thinking_content")

    output = []
    if response_text:
        output.append(response_text)

    if thinking_content:
        output.append("\n" + "=" * 50)
        output.append("【思考过程】")
        output.append(thinking_content)

    return "\n".join(output) if output else "未获取到解析结果"


def print_usage_info(result: dict) -> None:
    """打印 token 使用信息"""
    usage = result.get("usage", {})
    if usage:
        print("\n" + "-" * 50, file=sys.stderr)
        print(f"输入 Tokens: {usage.get('input_tokens', 0)}", file=sys.stderr)
        print(f"输出 Tokens: {usage.get('output_tokens', 0)}", file=sys.stderr)
        print(f"总 Tokens: {usage.get('total_tokens', 0)}", file=sys.stderr)

    model = result.get("model", "unknown")
    source = result.get("source", "unknown")
    print(f"模型: {model} (来源: {source})", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="文档理解 CLI 工具 - 使用 AI 解析文档内容（PDF等）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # ⚡ 推荐：使用 JSON 配置模式
  python document_understanding.py --config '{"document_url": "https://example.com/document.pdf"}'
  python document_understanding.py --config '{"document_url": "https://example.com/report.pdf", "prompt": "总结这份报告的核心观点"}'
  python document_understanding.py --config '{"document_url": "https://example.com/paper.pdf", "prompt": "提取论文中的研究方法", "model": "gemini"}'

  # 传统 CLI 模式（仍然支持）
  python document_understanding.py https://example.com/document.pdf
  python document_understanding.py https://example.com/report.pdf "总结这份报告的核心观点"
        """,
    )

    parser.add_argument(
        "document_url",
        nargs="?",
        default=None,
        help="文档的公网 URL 地址（必须是可公开访问的 URL，支持 PDF 等格式）",
    )

    parser.add_argument(
        "prompt",
        nargs="?",
        default=DEFAULT_PROMPT,
        help=f"对文档的提问或提示词（默认: '{DEFAULT_PROMPT}'）",
    )

    parser.add_argument(
        "--model",
        choices=[DEFAULT_MODEL],
        default=DEFAULT_MODEL,
        help="使用的模型（当前仅支持: gemini）",
    )

    parser.add_argument(
        "--config",
        help="JSON 配置字符串或 JSON 文件路径，包含所有参数。优先级高于其他 CLI 参数",
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="显示详细的 token 使用信息",
    )

    args = parser.parse_args()

    # 解析参数：--config 优先
    if args.config:
        config = parse_config(args.config)
        document_url = normalize_input(config.get("document_url", ""))
        if not document_url:
            print("错误: JSON 配置中缺少 document_url 字段", file=sys.stderr)
            sys.exit(1)
        document_url = validate_url(document_url, "文档 URL")
        prompt = config.get("prompt", DEFAULT_PROMPT)
        # 保留 model 字段兼容旧调用，但只允许 gemini，避免静默走错误后端。
        model = config.get("model", DEFAULT_MODEL)
        verbose = config.get("verbose", args.verbose)
        if model != DEFAULT_MODEL:
            print(f"错误: 不支持的模型 '{model}'，当前仅支持: {DEFAULT_MODEL}", file=sys.stderr)
            sys.exit(1)
    else:
        document_url = validate_url(args.document_url, "文档 URL")
        prompt = args.prompt
        model = args.model
        verbose = args.verbose

    # 调用 API
    result = understand_document(
        document_url=document_url,
        prompt=prompt,
        model=model,
    )

    # 输出解析结果
    parsed_content = parse_result(result)
    print(parsed_content)

    # 如果需要，输出使用信息
    if verbose:
        print_usage_info(result)


if __name__ == "__main__":
    main()
