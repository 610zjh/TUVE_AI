#!/usr/bin/env python3
"""
图片标准化 CLI 工具。

为什么新增：SEE2AI 最新 action 将图片预处理独立成 see2ai_image_normalize_v1。
Agent 在调用人脸检测、视频生成或图像生成前，可以先把不稳定的公网图片 URL
转换成更适合下游供应商读取的稳定 URL。
"""

import argparse
import json
import os
import sys
from typing import Any, Dict

import requests


ENDPOINT_PATH = "/api/v1/actions/see2ai_image_normalize_v1"
PROFILES = {
    "face_detection",
    "vlm",
    "video_reference",
    "storage_canonical",
    "video_seedance_reference",
    "video_kling_reference",
    "image_generation_reference",
}


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
    image_url = config.get("image_url")
    if not isinstance(image_url, str) or not image_url.strip():
        fail("image_url 必须是非空公网图片 URL")
    if not image_url.startswith(("http://", "https://")):
        fail("image_url 必须是 http/https URL；本地文件请先调用 see2ai_storage_upload")

    profile = config.get("profile", "face_detection")
    if not isinstance(profile, str) or profile not in PROFILES:
        fail(f"profile 不合法，可选: {sorted(PROFILES)}")

    return {"image_url": image_url.strip(), "profile": profile}


def call_action(payload: Dict[str, Any]) -> Dict[str, Any]:
    endpoint = f"{get_base_url()}{ENDPOINT_PATH}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {get_api_key()}",
    }
    try:
        response = requests.post(endpoint, json=payload, headers=headers, timeout=120)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as exc:
        status_code = exc.response.status_code if exc.response is not None else "unknown"
        body = exc.response.text if exc.response is not None else ""
        fail(f"HTTP 错误 {status_code}: {body or exc}")
    except requests.exceptions.RequestException as exc:
        fail(f"请求错误: {exc}")


def parse_inputs() -> Dict[str, Any]:
    parser = argparse.ArgumentParser(description="图片标准化 CLI 工具")
    parser.add_argument("image_url", nargs="?", default=None, help="公网图片 URL")
    parser.add_argument("--profile", default=None, help="下游用途 profile")
    parser.add_argument("--config", help="JSON 配置字符串或 JSON 文件路径")
    parser.add_argument("--verbose", "-v", action="store_true", help="输出完整响应到 stderr")
    args = parser.parse_args()

    if args.config:
        config = parse_config(args.config)
        config["verbose"] = bool(config.get("verbose", args.verbose))
        return config
    if not args.image_url:
        fail("请提供 image_url 或 --config")
    config = {"image_url": args.image_url, "verbose": args.verbose}
    if args.profile:
        config["profile"] = args.profile
    return config


def main() -> None:
    config = parse_inputs()
    payload = validate_config(config)
    result = call_action(payload)
    normalized_url = result.get("normalized_url")
    if not normalized_url:
        fail(f"响应中缺少 normalized_url: {json.dumps(result, ensure_ascii=False)}")
    print(normalized_url)
    if config.get("verbose"):
        print(json.dumps(result, ensure_ascii=False, indent=2), file=sys.stderr)


if __name__ == "__main__":
    main()
