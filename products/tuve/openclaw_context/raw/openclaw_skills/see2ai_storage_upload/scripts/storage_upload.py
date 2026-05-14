#!/usr/bin/env python3
"""
文件上传 CLI 工具
上传图片、视频、文档等文件到 SEE2AI 云存储，返回带有 CDN 加速的永久 URL

用法:
    python storage_upload.py <file_path>
    python storage_upload.py /path/to/image.jpg
"""

import argparse
import json
import os
import sys
from pathlib import Path

import requests


# API 配置
ENDPOINT_PATH = "/api/v1/actions/see2ai_storage_upload_v1"
MAX_UPLOAD_SIZE_MB = 50
MAX_UPLOAD_SIZE_BYTES = MAX_UPLOAD_SIZE_MB * 1024 * 1024
UNSUPPORTED_SUFFIXES = {".webp"}


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
        print('正确格式示例: --config \'{"file_path": "/path/to/file.jpg"}\'', file=sys.stderr)
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


def validate_file_path(file_path: str) -> str:
    """验证文件路径"""
    if not file_path:
        raise argparse.ArgumentTypeError(
            f"文件路径不能为空\n"
            f"正确用法示例:\n"
            f"  python storage_upload.py /path/to/file.jpg"
        )

    path = Path(file_path)

    if not path.exists():
        raise argparse.ArgumentTypeError(
            f"文件不存在: {file_path}\n"
            f"请检查文件路径是否正确\n"
            f"正确用法示例:\n"
            f"  python storage_upload.py /path/to/file.jpg"
        )

    if not path.is_file():
        raise argparse.ArgumentTypeError(
            f"路径不是文件: {file_path}\n"
            f"请提供文件路径而非目录路径\n"
            f"正确用法示例:\n"
            f"  python storage_upload.py /path/to/file.jpg"
        )

    # 与 SEE2AI 服务端硬限制保持一致，避免 Agent 先选中服务端必拒的文件。
    file_size = path.stat().st_size
    if file_size > MAX_UPLOAD_SIZE_BYTES:
        raise argparse.ArgumentTypeError(
            f"文件大小超过限制: {file_size / (1024*1024):.2f}MB\n"
            f"最大允许大小: {MAX_UPLOAD_SIZE_MB}MB\n"
            f"请压缩文件后重试"
        )

    if file_size == 0:
        raise argparse.ArgumentTypeError(
            f"文件为空: {file_path}\n"
            f"请检查文件内容"
        )

    # SEE2AI 存储上传接口显式拒绝 WebP，提前阻断并提示转换格式。
    if path.suffix.lower() in UNSUPPORTED_SUFFIXES:
        raise argparse.ArgumentTypeError(
            f"不支持直接上传 WebP 文件: {file_path}\n"
            f"请先转换为 JPG 或 PNG 后再上传"
        )

    return file_path


def require_valid_file_path(file_path: str) -> str:
    """以 CLI 友好的方式输出本地校验错误，避免 argparse 异常堆栈暴露给 Agent。"""
    try:
        return validate_file_path(file_path)
    except argparse.ArgumentTypeError as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)


def upload_file(file_path: str) -> dict:
    """
    调用 SEE2AI API 上传文件

    Args:
        file_path: 本地文件路径（已通过 validate_file_path 校验）

    Returns:
        API 返回的完整结果字典
    """
    api_key = get_api_key()
    path = Path(file_path)

    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    # 准备文件上传
    try:
        with open(file_path, "rb") as f:
            files = {"file": (path.name, f)}
            endpoint = f"{get_base_url()}{ENDPOINT_PATH}"
            response = requests.post(
                endpoint,
                headers=headers,
                files=files,
                timeout=300,
            )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("错误: 请求超时（文件上传可能需要较长时间）", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"HTTP 错误: {e}", file=sys.stderr)
        if response.status_code == 401:
            print("API Key 无效或余额不足", file=sys.stderr)
        elif response.status_code == 413:
            print(f"文件超过服务端大小限制，请压缩到 {MAX_UPLOAD_SIZE_MB}MB 以内", file=sys.stderr)
        elif response.status_code == 422:
            print("请求参数错误，请检查文件格式是否支持；WebP 请先转换为 JPG 或 PNG", file=sys.stderr)
        elif response.status_code == 429:
            print("请求频率超限，请稍后重试", file=sys.stderr)
        elif response.status_code == 500:
            print("上传服务异常，请稍后重试", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}", file=sys.stderr)
        sys.exit(1)


def parse_result(result: dict) -> str:
    """
    从 API 返回结果中提取上传后的 URL

    Args:
        result: API 返回的字典

    Returns:
        上传文件的 URL
    """
    if not isinstance(result, dict):
        return "错误: 无效的响应格式"

    status = result.get("status", "")
    if status != "success":
        return f"上传失败，状态: {status}"

    url = result.get("url", "")
    if url:
        return url

    return "未获取到上传后的文件 URL"


def print_upload_info(result: dict, file_path: str) -> None:
    """打印上传详情"""
    path = Path(file_path)

    print("\n" + "-" * 50, file=sys.stderr)
    print(f"文件名: {result.get('filename', path.name)}", file=sys.stderr)
    print(f"文件大小: {result.get('size', path.stat().st_size)} 字节", file=sys.stderr)
    print(f"状态: {result.get('status', 'unknown')}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="文件上传 CLI 工具 - 上传文件到 SEE2AI 云存储",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # ⚡ 推荐：使用 JSON 配置模式
  python storage_upload.py --config '{"file_path": "/path/to/image.jpg"}'
  python storage_upload.py --config '{"file_path": "/path/to/video.mp4", "verbose": true}'

  # 传统 CLI 模式（仍然支持）
  python storage_upload.py /path/to/image.jpg
  python storage_upload.py /path/to/video.mp4 -v

支持的文件类型:
  - 图片: jpg, jpeg, png, gif 等（WebP 需先转换为 JPG/PNG）
  - 视频: mp4, mov, avi 等
  - 文档: pdf, doc, docx 等
  - 大小: 单文件最大 50MB
        """,
    )

    parser.add_argument(
        "file_path",
        nargs="?",
        default=None,
        help="要上传的本地文件路径",
    )

    parser.add_argument(
        "--config",
        help="JSON 配置字符串或 JSON 文件路径，包含所有参数。优先级高于其他 CLI 参数",
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="显示详细的上传信息",
    )

    args = parser.parse_args()

    # 解析参数：--config 优先
    if args.config:
        config = parse_config(args.config)
        file_path = config.get("file_path", "")
        if not file_path:
            print("错误: JSON 配置中缺少 file_path 字段", file=sys.stderr)
            sys.exit(1)
        file_path = require_valid_file_path(file_path)
        verbose = config.get("verbose", args.verbose)
    else:
        file_path = args.file_path
        if not file_path:
            print("错误: 请提供 file_path 参数或使用 --config", file=sys.stderr)
            sys.exit(1)
        file_path = require_valid_file_path(file_path)
        verbose = args.verbose

    # 调用 API
    result = upload_file(file_path=file_path)

    # 输出上传后的 URL
    url = parse_result(result)
    print(url)

    # 如果需要，输出详细信息
    if verbose:
        print_upload_info(result, file_path)


if __name__ == "__main__":
    main()
