#!/usr/bin/env python3
"""
视频理解 CLI 工具
使用 SEE2AI 多模态大模型 API 对视频进行解析和理解

用法:
    python vedio_understanding.py <video_url> [prompt]
    python vedio_understanding.py https://example.com/video.mp4 "描述这个视频的内容"
"""

import argparse
import json
import os
import sys

import requests


# API 配置
# 修改原因：视频理解当前仅保留已实测可用的单模型链路，避免保留未验证分支。
MODEL_ENDPOINT_PATH = "/api/v1/actions/see2ai_llm_doubao_v1"
DEFAULT_PROMPT = "请详细描述这个视频的内容"
_WRAPPER_QUOTES = ("`", '"', "'")


def normalize_input(value: str | None) -> str:
    """清洗输入文本，去掉常见的成对包裹引号/反引号"""
    if value is None:
        return ""

    normalized = str(value).strip()
    # 修改原因：复用 image_understanding 的输入容错，兼容从 Markdown/日志复制出的带包裹符 URL。
    while len(normalized) >= 2 and normalized[0] == normalized[-1] and normalized[0] in _WRAPPER_QUOTES:
        normalized = normalized[1:-1].strip()
    return normalized


def parse_config(config_input: str) -> dict:
    """解析 JSON 配置，支持 JSON 字符串或 JSON 文件路径"""
    config_input = config_input.strip()

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

    try:
        config = json.loads(config_input)
        if not isinstance(config, dict):
            print("错误: JSON 内容必须是一个对象（字典）", file=sys.stderr)
            sys.exit(1)
        return config
    except json.JSONDecodeError as e:
        print(f"错误: JSON 解析失败: {e}", file=sys.stderr)
        print('正确格式示例: --config \'{"video_url": "https://example.com/video.mp4"}\'', file=sys.stderr)
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
            f"  python vedio_understanding.py https://example.com/video.mp4"
        )

    if not url.startswith(("http://", "https://")):
        raise argparse.ArgumentTypeError(
            f"{url_type} 必须以 http:// 或 https:// 开头，收到: '{url}'\n"
            f"正确用法示例:\n"
            f"  python vedio_understanding.py https://example.com/video.mp4"
        )

    return url


def understand_video(
    video_url: str,
    prompt: str = DEFAULT_PROMPT,
) -> dict:
    """
    调用 SEE2AI API 对视频进行理解

    Args:
        video_url: 视频的公网 URL
        prompt: 对视频的提问或提示词

    Returns:
        API 返回的完整结果字典
    """
    api_key = get_api_key()
    endpoint = f"{get_base_url()}{MODEL_ENDPOINT_PATH}"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    # 修改原因：视频理解当前仅走 Doubao，可直接固定请求体，避免保留无效多模型分支。
    payload = {
        "query": prompt,
        "video_urls": [video_url],
        "stream": False,
        "enable_thinking": False,
    }

    try:
        response = requests.post(endpoint, json=payload, headers=headers, timeout=120)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("错误: 请求超时", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"HTTP 错误: {e}", file=sys.stderr)
        if response.status_code == 401:
            print("API Key 无效或余额不足", file=sys.stderr)
        elif response.status_code == 422:
            print("请求参数错误，请检查视频 URL 是否有效", file=sys.stderr)
        elif response.status_code == 429:
            print("请求频率超限，请稍后重试", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}", file=sys.stderr)
        sys.exit(1)


def parse_result(result: dict) -> str:
    """
    从 API 返回结果中提取视频解析内容

    Args:
        result: API 返回的字典

    Returns:
        视频解析文本内容
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
        description="视频理解 CLI 工具 - 使用 AI 解析视频内容",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # ⚡ 推荐：使用 JSON 配置模式
  python vedio_understanding.py --config '{"video_url": "https://example.com/video.mp4"}'
  python vedio_understanding.py --config '{"video_url": "https://example.com/video.mp4", "prompt": "总结这个视频的主要内容"}'
  python vedio_understanding.py --config '{"video_url": "https://example.com/video.mp4", "prompt": "提取视频中的关键信息"}'

  # 传统 CLI 模式（仍然支持）
  python vedio_understanding.py https://example.com/video.mp4
  python vedio_understanding.py https://example.com/video.mp4 "总结这个视频的主要内容"
        """,
    )

    parser.add_argument(
        "video_url",
        nargs="?",
        default=None,
        help="视频的公网 URL 地址（必须是可公开访问的 URL）",
    )

    parser.add_argument(
        "prompt",
        nargs="?",
        default=DEFAULT_PROMPT,
        help=f"对视频的提问或提示词（默认: '{DEFAULT_PROMPT}'）",
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
        video_url = config.get("video_url", "")
        if not video_url:
            print("错误: JSON 配置中缺少 video_url 字段", file=sys.stderr)
            sys.exit(1)
        video_url = validate_url(video_url, "视频 URL")
        prompt = config.get("prompt", DEFAULT_PROMPT)
        verbose = config.get("verbose", args.verbose)
        model = normalize_input(config.get("model"))
        if model and model != "doubao":
            print("错误: 当前视频理解 skill 仅支持 doubao，请删除 model 字段或将其设为 doubao", file=sys.stderr)
            sys.exit(1)
    else:
        video_url = validate_url(args.video_url, "视频 URL")
        prompt = args.prompt
        verbose = args.verbose

    # 调用 API
    result = understand_video(
        video_url=video_url,
        prompt=prompt,
    )

    # 输出解析结果
    parsed_content = parse_result(result)
    print(parsed_content)

    # 如果需要，输出使用信息
    if verbose:
        print_usage_info(result)


if __name__ == "__main__":
    main()
