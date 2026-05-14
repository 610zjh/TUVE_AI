#!/usr/bin/env python3
"""
视频拼接 CLI 工具
通过 API 调用实现视频自动拼接，合并多个视频片段

用法:
    python video_concat.py <video_url1> <video_url2> [video_url3 ...]
    python video_concat.py https://example.com/video1.mp4 https://example.com/video2.mp4
"""

import argparse
import json
import os
import sys

import requests


# API 配置
ENDPOINT_PATH = "/api/v1/actions/see2ai_video_concat_v1"


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
        print('正确格式示例: --config \'{"video_urls": ["https://example.com/v1.mp4", "https://example.com/v2.mp4"]}\'', file=sys.stderr)
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


def validate_video_urls(urls: list[str]) -> list[str]:
    """验证视频 URL 列表"""
    if len(urls) < 2:
        raise argparse.ArgumentTypeError(
            f"至少需要提供两个视频 URL 进行拼接，当前只提供了 {len(urls)} 个\n"
            f"正确用法示例:\n"
            f"  python video_concat.py https://example.com/video1.mp4 https://example.com/video2.mp4"
        )

    for i, url in enumerate(urls):
        if not url:
            raise argparse.ArgumentTypeError(
                f"第 {i+1} 个视频 URL 不能为空\n"
                f"正确用法示例:\n"
                f"  python video_concat.py https://example.com/video1.mp4 https://example.com/video2.mp4"
            )
        if not url.startswith(("http://", "https://")):
            raise argparse.ArgumentTypeError(
                f"第 {i+1} 个视频 URL 必须以 http:// 或 https:// 开头，收到: '{url}'\n"
                f"正确用法示例:\n"
                f"  python video_concat.py https://example.com/video1.mp4 https://example.com/video2.mp4"
            )

    return urls


def concat_videos(media_urls: list[str]) -> dict:
    """
    调用 SEE2AI API 拼接视频

    Args:
        media_urls: 需要拼接的视频 URL 列表

    Returns:
        API 返回的完整结果字典
    """
    api_key = get_api_key()
    endpoint = f"{get_base_url()}{ENDPOINT_PATH}"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    payload = {
        "media_urls": media_urls,
    }

    try:
        response = requests.post(endpoint, json=payload, headers=headers, timeout=300)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("错误: 请求超时（视频拼接可能需要较长时间）", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"HTTP 错误: {e}", file=sys.stderr)
        if response.status_code == 401:
            print("API Key 无效或余额不足", file=sys.stderr)
        elif response.status_code == 422:
            print("请求参数错误，请检查视频 URL 列表是否有效", file=sys.stderr)
        elif response.status_code == 429:
            print("请求频率超限，请稍后重试", file=sys.stderr)
        elif response.status_code == 500:
            print("视频拼接服务异常，请稍后重试", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}", file=sys.stderr)
        sys.exit(1)


def parse_result(result: dict) -> str:
    """
    从 API 返回结果中提取拼接后的视频 URL

    Args:
        result: API 返回的字典

    Returns:
        拼接后的视频 URL
    """
    if not isinstance(result, dict):
        print("错误: 无效的响应格式", file=sys.stderr)
        sys.exit(1)

    video_url = result.get("video_url", "")
    if video_url:
        return video_url

    # 200 响应但缺少 video_url 不能视为成功，否则上层 Agent 会把失败当作可交付结果。
    print("错误: 未获取到拼接后的视频 URL", file=sys.stderr)
    sys.exit(1)


def print_usage_info(result: dict) -> None:
    """打印 token 使用信息"""
    usage_info = [
        f"输入 Tokens: {result.get('input_tokens', 0)}",
        f"输出 Tokens: {result.get('output_tokens', 0)}",
        f"总 Tokens: {result.get('total_tokens', 0)}",
    ]

    model = result.get("model", "unknown")
    source = result.get("source", "unknown")
    usage_info.append(f"模型: {model} (来源: {source})")

    print("\n" + "-" * 50, file=sys.stderr)
    for info in usage_info:
        print(info, file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="视频拼接 CLI 工具 - 合并多个视频片段",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # ⚡ 推荐：使用 JSON 配置模式
  python video_concat.py --config '{"video_urls": ["https://example.com/video1.mp4", "https://example.com/video2.mp4"]}'
  python video_concat.py --config '{"video_urls": ["https://example.com/clip1.mp4", "https://example.com/clip2.mp4", "https://example.com/clip3.mp4"], "verbose": true}'

  # 传统 CLI 模式（仍然支持）
  python video_concat.py https://example.com/video1.mp4 https://example.com/video2.mp4
  python video_concat.py https://example.com/clip1.mp4 https://example.com/clip2.mp4 https://example.com/clip3.mp4 -v
        """,
    )

    parser.add_argument(
        "video_urls",
        nargs="*",
        type=str,
        help="需要拼接的视频 URL 列表（至少两个）",
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
        video_urls = config.get("video_urls", [])
        if not isinstance(video_urls, list) or len(video_urls) < 2:
            print("错误: JSON 配置中 video_urls 必须是包含至少 2 个 URL 的数组", file=sys.stderr)
            sys.exit(1)
        validate_video_urls(video_urls)
        verbose = config.get("verbose", args.verbose)
    else:
        video_urls = args.video_urls
        if not video_urls or len(video_urls) < 2:
            print("错误: 请提供至少 2 个视频 URL 或使用 --config", file=sys.stderr)
            sys.exit(1)
        validate_video_urls(video_urls)
        verbose = args.verbose

    # 调用 API
    result = concat_videos(media_urls=video_urls)

    # 输出拼接后的视频 URL
    video_url = parse_result(result)
    print(video_url)

    # 如果需要，输出使用信息
    if verbose:
        print_usage_info(result)


if __name__ == "__main__":
    main()
