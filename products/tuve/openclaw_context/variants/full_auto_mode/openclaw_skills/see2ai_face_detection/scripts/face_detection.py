#!/usr/bin/env python3
"""
人脸检测 CLI 工具
使用 SEE2AI 专用人脸检测 Action 判断图片中是否包含可识别人脸。

用法:
    python face_detection.py <image_url>
    python face_detection.py https://example.com/image.jpg
"""

import argparse
import json
import os
import sys

import requests


ENDPOINT_PATH = "/api/v1/actions/see2ai_face_detection_v1"


def parse_config(config_input: str) -> dict:
    """解析 JSON 配置，支持 JSON 字符串或 JSON 文件路径。"""
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
    """从环境变量获取 Base URL。"""
    base_url = os.environ.get("SEE2AI_BASE_URL")
    if not base_url:
        print("错误: 未设置 SEE2AI_BASE_URL 环境变量", file=sys.stderr)
        print("请设置环境变量: export SEE2AI_BASE_URL='https://see2ai.com'", file=sys.stderr)
        sys.exit(1)
    return base_url.rstrip("/")


def get_api_key() -> str:
    """从环境变量获取 API Key。"""
    api_key = os.environ.get("SEE2AI_API_KEY")
    if not api_key:
        print("错误: 未设置 SEE2AI_API_KEY 环境变量", file=sys.stderr)
        print("请设置环境变量: export SEE2AI_API_KEY='sk-your-api-key'", file=sys.stderr)
        sys.exit(1)
    return api_key


def validate_url(url: str, url_type: str = "图片 URL") -> str:
    """验证公网 URL，避免把本地路径误传给 Action。"""
    if not url:
        raise argparse.ArgumentTypeError(
            f"{url_type} 不能为空\n"
            "正确用法示例:\n"
            "  python face_detection.py https://example.com/image.jpg"
        )

    if not url.startswith(("http://", "https://")):
        raise argparse.ArgumentTypeError(
            f"{url_type} 必须以 http:// 或 https:// 开头，收到: '{url}'\n"
            "正确用法示例:\n"
            "  python face_detection.py https://example.com/image.jpg"
        )

    return url


def detect_face(image_url: str) -> dict:
    """调用 SEE2AI 专用人脸检测 Action。"""
    api_key = get_api_key()
    endpoint = f"{get_base_url()}{ENDPOINT_PATH}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    payload = {
        "image_url": image_url,
    }

    try:
        response = requests.post(endpoint, json=payload, headers=headers, timeout=120)
        response.raise_for_status()
        result = response.json()
        if not isinstance(result, dict):
            print("错误: API 返回了非对象响应", file=sys.stderr)
            sys.exit(1)
        return result
    except requests.exceptions.Timeout:
        print("错误: 请求超时", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"HTTP 错误: {e}", file=sys.stderr)
        if response.status_code == 401:
            print("API Key 无效或余额不足", file=sys.stderr)
        elif response.status_code == 422:
            print("请求参数错误，请检查图片 URL 是否满足公网/格式/尺寸要求", file=sys.stderr)
        elif response.status_code == 429:
            print("请求频率超限，请稍后重试", file=sys.stderr)
        elif 500 <= response.status_code < 600:
            print("上游服务异常，请稍后重试", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError:
        print("错误: API 返回了无效 JSON", file=sys.stderr)
        sys.exit(1)


def normalize_result(result: dict) -> dict:
    """统一输出结构，方便上游 Agent 直接消费 has_face / face_count。"""
    return {
        "has_face": bool(result.get("has_face", False)),
        "face_count": int(result.get("face_count", 0)),
        "warnings": result.get("warnings"),
        "model": result.get("model", ""),
        "source": result.get("source", "see2ai"),
        "input_tokens": int(result.get("input_tokens", 0)),
        "output_tokens": int(result.get("output_tokens", 0)),
        "total_tokens": int(result.get("total_tokens", 0)),
        "cost_points": result.get("cost_points"),
    }


def print_usage_info(result: dict) -> None:
    """把计量信息打到 stderr，保持 stdout 纯 JSON。"""
    print("\n" + "-" * 50, file=sys.stderr)
    print(f"Has Face:      {result.get('has_face', False)}", file=sys.stderr)
    print(f"Face Count:    {result.get('face_count', 0)}", file=sys.stderr)
    print(f"Input Tokens:  {result.get('input_tokens', 0)}", file=sys.stderr)
    print(f"Output Tokens: {result.get('output_tokens', 0)}", file=sys.stderr)
    print(f"Total Tokens:  {result.get('total_tokens', 0)}", file=sys.stderr)
    print(f"Model:         {result.get('model', 'unknown')}", file=sys.stderr)
    print(f"Source:        {result.get('source', 'see2ai')}", file=sys.stderr)
    warnings = result.get("warnings") or []
    if warnings:
        print("Warnings:", file=sys.stderr)
        for warning in warnings:
            print(f"  - {warning}", file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="人脸检测 CLI 工具 - 使用 SEE2AI 专用 Action 检测图片是否含人脸",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 推荐：JSON 配置模式
  python face_detection.py --config '{"image_url": "https://example.com/photo.jpg"}'
  python face_detection.py --config '{"image_url": "https://example.com/photo.jpg", "verbose": true}'

  # 传统 CLI 模式
  python face_detection.py https://example.com/photo.jpg
        """,
    )

    parser.add_argument(
        "image_url",
        nargs="?",
        default=None,
        help="图片的公网 URL 地址（必须是可公开访问的 URL）",
    )
    parser.add_argument(
        "--config",
        help="JSON 配置字符串或 JSON 文件路径，包含所有参数。优先级高于其他 CLI 参数",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="显示详细的计量与 warning 信息",
    )

    args = parser.parse_args()

    if args.config:
        config = parse_config(args.config)
        image_url = config.get("image_url", "")
        if not image_url:
            print("错误: JSON 配置中缺少 image_url 字段", file=sys.stderr)
            sys.exit(1)
        validate_url(image_url)
        verbose = bool(config.get("verbose", args.verbose))
    else:
        if not args.image_url:
            parser.error("请提供图片 URL，或使用 --config 传入 image_url")
        image_url = validate_url(args.image_url)
        verbose = args.verbose

    result = normalize_result(detect_face(image_url))
    print(json.dumps(result, ensure_ascii=False))

    if verbose:
        print_usage_info(result)


if __name__ == "__main__":
    main()
