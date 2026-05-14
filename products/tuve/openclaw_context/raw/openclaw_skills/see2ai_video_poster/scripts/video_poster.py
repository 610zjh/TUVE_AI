#!/usr/bin/env python3
"""
视频封面抽帧 CLI 工具。

为什么新增：SEE2AI 最新 action 已把“首个非黑屏帧封面”封装成
see2ai_video_poster_v1，Agent 不应再自行下载视频或用本地 ffmpeg 抽帧。
"""

import argparse
import json
import os
import sys
from typing import Any, Dict

import requests


ENDPOINT_PATH = "/api/v1/actions/see2ai_video_poster_v1"


def fail(message: str) -> None:
    print(f"错误: {message}", file=sys.stderr)
    sys.exit(1)


def parse_config(config_input: str) -> Dict[str, Any]:
    config_input = config_input.strip()
    if not config_input.startswith("{") and os.path.isfile(config_input):
        with open(config_input, encoding="utf-8") as file:
            data = json.load(file)
    else:
        data = json.loads(config_input)
    if not isinstance(data, dict):
        fail("JSON 配置必须是对象")
    return data


def get_base_url() -> str:
    base_url = os.environ.get("SEE2AI_BASE_URL")
    if not base_url:
        fail("未设置 SEE2AI_BASE_URL 环境变量")
    return base_url.rstrip("/")


def get_api_key() -> str:
    api_key = os.environ.get("SEE2AI_API_KEY")
    if not api_key:
        fail("未设置 SEE2AI_API_KEY 环境变量")
    return api_key


def validate_config(config: Dict[str, Any]) -> Dict[str, Any]:
    video_url = config.get("video_url")
    if not isinstance(video_url, str) or not video_url.strip():
        fail("video_url 必须是非空公网视频 URL")
    if not video_url.startswith(("http://", "https://")):
        fail("video_url 必须是 http/https URL；本地文件请先调用 see2ai_storage_upload")
    return {"video_url": video_url.strip()}


def call_action(payload: Dict[str, Any]) -> Dict[str, Any]:
    endpoint = f"{get_base_url()}{ENDPOINT_PATH}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {get_api_key()}",
    }
    try:
        response = requests.post(endpoint, json=payload, headers=headers, timeout=180)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as exc:
        status_code = exc.response.status_code if exc.response is not None else "unknown"
        body = exc.response.text if exc.response is not None else ""
        fail(f"HTTP 错误 {status_code}: {body or exc}")
    except requests.exceptions.RequestException as exc:
        fail(f"请求错误: {exc}")


def parse_inputs() -> Dict[str, Any]:
    parser = argparse.ArgumentParser(description="视频封面抽帧 CLI 工具")
    parser.add_argument("video_url", nargs="?", default=None, help="公网视频 URL")
    parser.add_argument("--config", help="JSON 配置字符串或 JSON 文件路径")
    parser.add_argument("--verbose", "-v", action="store_true", help="输出完整响应到 stderr")
    args = parser.parse_args()

    if args.config:
        config = parse_config(args.config)
        config["verbose"] = bool(config.get("verbose", args.verbose))
        return config
    if not args.video_url:
        fail("请提供 video_url 或 --config")
    return {"video_url": args.video_url, "verbose": args.verbose}


def main() -> None:
    config = parse_inputs()
    payload = validate_config(config)
    result = call_action(payload)
    poster_url = result.get("poster_url")
    if not poster_url:
        fail(f"响应中缺少 poster_url: {json.dumps(result, ensure_ascii=False)}")
    print(poster_url)
    if config.get("verbose"):
        print(json.dumps(result, ensure_ascii=False, indent=2), file=sys.stderr)


if __name__ == "__main__":
    main()
