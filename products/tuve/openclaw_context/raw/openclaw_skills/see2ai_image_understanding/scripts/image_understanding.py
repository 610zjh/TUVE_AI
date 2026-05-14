#!/usr/bin/env python3
"""
图像理解 CLI 工具
使用 SEE2AI 多模态大模型 API 对图片进行解析和理解

用法:
    python image_understanding.py <image_url> [prompt]
    python image_understanding.py https://example.com/image.jpg "描述这张图片"
"""

import argparse
import json
import os
import sys

import requests


# API 配置
MODEL_ENDPOINT_PATH = "/api/v1/actions/see2ai_llm_doubao_v1"
DEFAULT_PROMPT = "请详细描述这张图片的内容"


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
        print('正确格式示例: --config \'{"image_url": "https://example.com/image.jpg"}\'', file=sys.stderr)
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
    if not url:
        raise argparse.ArgumentTypeError(
            f"{url_type} 不能为空\n"
            f"正确用法示例:\n"
            f"  python image_understanding.py https://example.com/image.jpg"
        )

    if not url.startswith(("http://", "https://")):
        raise argparse.ArgumentTypeError(
            f"{url_type} 必须以 http:// 或 https:// 开头，收到: '{url}'\n"
            f"正确用法示例:\n"
            f"  python image_understanding.py https://example.com/image.jpg"
        )

    return url


def require_valid_url(url: str, url_type: str = "URL") -> str:
    """把 URL 校验错误转成清晰的 CLI 退出信息，避免问题延迟到服务端才暴露。"""
    try:
        return validate_url(url, url_type)
    except argparse.ArgumentTypeError as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)


def understand_image(
    image_url: str,
    prompt: str = DEFAULT_PROMPT,
) -> dict:
    """
    调用 SEE2AI API 对图片进行理解

    Args:
        image_url: 图片的公网 URL
        prompt: 对图片的提问或提示词
    Returns:
        API 返回的完整结果字典
    """
    api_key = get_api_key()
    # 该 Skill 已固定为 Doubao，避免继续暴露已下线的多模型分支。
    endpoint = f"{get_base_url()}{MODEL_ENDPOINT_PATH}"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    payload = {
        "query": prompt,
        "image_urls": [image_url],
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
            print("请求参数错误，请检查图片 URL 是否有效", file=sys.stderr)
        elif response.status_code == 429:
            print("请求频率超限，请稍后重试", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}", file=sys.stderr)
        sys.exit(1)


def parse_result(result: dict) -> str:
    """
    从 API 返回结果中提取图片解析内容

    Args:
        result: API 返回的字典

    Returns:
        图片解析文本内容
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
        description="图像理解 CLI 工具 - 使用 AI 解析图片内容",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # ⚡ 推荐：使用 JSON 配置模式
  python image_understanding.py --config '{"image_url": "https://example.com/photo.jpg"}'
  python image_understanding.py --config '{"image_url": "https://example.com/chart.jpg", "prompt": "分析这张图表的数据"}'

  # 传统 CLI 模式（仍然支持）
  python image_understanding.py https://example.com/photo.jpg
  python image_understanding.py https://example.com/chart.jpg "分析这张图表的数据"
        """,
    )

    parser.add_argument(
        "image_url",
        nargs="?",
        default=None,
        help="图片的公网 URL 地址（必须是可公开访问的 URL）",
    )

    parser.add_argument(
        "prompt",
        nargs="?",
        default=DEFAULT_PROMPT,
        help=f"对图片的提问或提示词（默认: '{DEFAULT_PROMPT}'）",
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
        image_url = config.get("image_url", "")
        if not image_url:
            print("错误: JSON 配置中缺少 image_url 字段", file=sys.stderr)
            sys.exit(1)
        image_url = require_valid_url(image_url, "图片 URL")
        prompt = config.get("prompt", DEFAULT_PROMPT)
        verbose = config.get("verbose", args.verbose)
    else:
        image_url = require_valid_url(args.image_url, "图片 URL")
        prompt = args.prompt
        verbose = args.verbose

    # 调用 API
    result = understand_image(
        image_url=image_url,
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
