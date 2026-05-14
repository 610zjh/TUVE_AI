#!/usr/bin/env python3
"""
文生图 CLI 工具

这次调整的重点是跟上 SEE2AI 最新 action 契约对调：
1. 继续兼容旧调用方传入的 aspect_ratio/resolution/output_format
2. 允许新调用方直接传 alternative_v1 原生参数
3. 根据新 schema 把旧参数优先路由到 v1，把高级参数路由到 alternative_v1
4. 显式支持 backend=fast，对接 see2ai_image_generation_fast_v1；auto 不会隐式切 fast
"""

import argparse
import json
import math
import os
import sys
from typing import Any, Dict, Optional, Set

import requests


V1_ENDPOINT_PATH = "/api/v1/actions/see2ai_image_generation_v1"
FAST_ENDPOINT_PATH = "/api/v1/actions/see2ai_image_generation_fast_v1"
ALTERNATIVE_ENDPOINT_PATH = "/api/v1/actions/see2ai_image_generation_alternative_v1"

LEGACY_ASPECT_RATIOS = [
    "1:1",
    "1:4",
    "1:8",
    "2:3",
    "3:2",
    "3:4",
    "4:1",
    "4:3",
    "4:5",
    "5:4",
    "8:1",
    "9:16",
    "16:9",
    "21:9",
    "auto",
]
V1_ASPECT_RATIOS = {"auto", "1:1", "9:16", "16:9", "4:3", "3:4"}
FAST_ASPECT_RATIOS = {
    "1:1",
    "1:4",
    "1:8",
    "2:3",
    "3:2",
    "3:4",
    "4:1",
    "4:3",
    "4:5",
    "5:4",
    "8:1",
    "9:16",
    "16:9",
    "21:9",
}
RESOLUTIONS = {"1K", "2K", "4K"}
FAST_RESOLUTIONS = {"1K", "2K"}
BACKENDS = {"auto", "v1", "fast", "alternative"}
ALTERNATIVE_QUALITY_VALUES = {"auto", "high", "medium", "low"}
ALTERNATIVE_BACKGROUND_VALUES = {"auto", "opaque", "transparent"}
ALTERNATIVE_MODERATION_VALUES = {"auto", "low"}
ALTERNATIVE_OUTPUT_FORMATS = {"auto", "png", "jpeg", "webp"}
FAST_OUTPUT_FORMATS = {"jpg", "jpeg", "png"}

TARGET_PIXELS_BY_RESOLUTION = {
    "1K": 1024 * 1024,
    "2K": 2048 * 2048,
    "4K": 3840 * 2160,
}
MAX_EDGE = 3840
MIN_EDGE = 256
MIN_PIXELS = 655_360
MAX_PIXELS = 3840 * 2160
MAX_ASPECT_RATIO = 3.0


def fail(message: str) -> None:
    print(f"错误: {message}", file=sys.stderr)
    sys.exit(1)


def parse_config(config_input: str) -> Dict[str, Any]:
    """解析 JSON 配置，支持 JSON 字符串或 JSON 文件路径。"""
    config_input = config_input.strip()

    if not config_input.startswith("{") and os.path.isfile(config_input):
        try:
            with open(config_input, encoding="utf-8") as file:
                config = json.load(file)
        except json.JSONDecodeError as exc:
            fail(f"JSON 文件解析失败: {exc}")
        except OSError as exc:
            fail(f"读取配置文件失败: {exc}")
        if not isinstance(config, dict):
            fail("JSON 文件内容必须是一个对象（字典）")
        return config

    try:
        config = json.loads(config_input)
    except json.JSONDecodeError as exc:
        fail(f"JSON 解析失败: {exc}")
    if not isinstance(config, dict):
        fail("JSON 内容必须是一个对象（字典）")
    return config


def get_base_url() -> str:
    """从环境变量获取 Base URL。"""
    base_url = os.environ.get("SEE2AI_BASE_URL")
    if not base_url:
        fail("未设置 SEE2AI_BASE_URL 环境变量")
    return base_url.rstrip("/")


def get_api_key() -> str:
    """从环境变量获取 API Key。"""
    api_key = os.environ.get("SEE2AI_API_KEY")
    if not api_key:
        fail("未设置 SEE2AI_API_KEY 环境变量")
    return api_key


def build_prompt_from_shot_context(config: Dict[str, Any]) -> str:
    """将 PRD 0024 的 shot_context 结构转成可直接生图的 prompt。"""
    shot_context = config.get("shot_context", {}) or {}
    asset_slot = config.get("asset_slot", {}) or {}
    global_style = config.get("global_style", {}) or {}

    narrative_intent = shot_context.get("narrative_intent", "完成当前镜头的叙事目标")
    shot_function = shot_context.get("shot_function", "reveal")
    prev_narrative = shot_context.get("previous_shot_narrative")
    next_narrative = shot_context.get("next_shot_narrative")
    composition_notes = shot_context.get("composition_notes", "主体清晰，构图稳定")
    purpose = asset_slot.get("purpose", "生成当前镜头所需关键帧")
    usage_role = asset_slot.get("usage_role", "image_ref")
    style_consistency_ref = asset_slot.get("style_consistency_ref")
    visual_style = global_style.get("visual_style", "风格统一、细节真实")
    aspect_ratio = global_style.get("aspect_ratio", "9:16")

    parts = [
        f"为短视频镜头生成一张关键帧图片，画幅 {aspect_ratio}，整体视觉风格为{visual_style}。",
        f"该镜头的叙事意图是：{narrative_intent}；镜头功能是：{shot_function}。",
        f"这张图的用途是：{purpose}；在后续视频生成中承担 {usage_role} 的作用。",
        f"构图要求：{composition_notes}。",
    ]
    if prev_narrative:
        parts.append(f"上一镜头承接信息：{prev_narrative}。")
    if next_narrative:
        parts.append(f"下一镜头衔接信息：{next_narrative}。")
    if style_consistency_ref:
        parts.append(f"需与一致性参考资产 {style_consistency_ref} 保持同一风格、光影与色调。")
    parts.append("要求画面具体、可拍、服务叙事，避免空泛抽象视觉。")
    return "".join(parts)


def normalize_lower_choice(value: Any, field_name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(f"{field_name} 必须是非空字符串")
    return value.strip().lower()


def normalize_resolution(value: Any) -> str:
    if not isinstance(value, str) or not value.strip():
        fail("resolution 必须是非空字符串")
    normalized = value.strip().upper()
    if normalized not in RESOLUTIONS:
        fail(f"不支持的 resolution '{value}'，可选: {sorted(RESOLUTIONS)}")
    return normalized


def normalize_output_format(value: Any) -> Optional[str]:
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        fail("output_format 必须是非空字符串")
    normalized = value.strip().lower()
    if normalized == "jpg":
        normalized = "jpeg"
    if normalized not in ALTERNATIVE_OUTPUT_FORMATS:
        fail(
            f"不支持的 output_format '{value}'，可选: {sorted(ALTERNATIVE_OUTPUT_FORMATS | {'jpg'})}"
        )
    return normalized


def parse_int_value(value: Any, field_name: str) -> int:
    if isinstance(value, bool):
        fail(f"{field_name} 不能是布尔值")
    try:
        return int(value)
    except (TypeError, ValueError):
        fail(f"{field_name} 必须是整数")


def parse_ratio_value(aspect_ratio: str) -> float:
    if aspect_ratio == "auto":
        return 1.0
    left, right = aspect_ratio.split(":", 1)
    return float(left) / float(right)


def round_to_multiple_of_16(value: float) -> int:
    rounded = int(round(value / 16.0) * 16)
    return max(16, rounded)


def build_size_from_legacy(aspect_ratio: str, resolution: str) -> str:
    ratio = parse_ratio_value(aspect_ratio)
    target_pixels = TARGET_PIXELS_BY_RESOLUTION[resolution]

    width = math.sqrt(target_pixels * ratio)
    height = math.sqrt(target_pixels / ratio)

    scale = min(1.0, MAX_EDGE / max(width, height))
    width *= scale
    height *= scale

    width = max(MIN_EDGE, round_to_multiple_of_16(width))
    height = max(MIN_EDGE, round_to_multiple_of_16(height))

    while width * height > MAX_PIXELS:
        width = max(16, width - 16)
        height = max(16, height - 16)

    return f"{width}x{height}"


def validate_size(size: str) -> None:
    if size.strip().lower() == "auto":
        return
    if "x" not in size:
        fail("size 必须使用 WIDTHxHEIGHT 格式，例如 1536x1024")
    width_text, height_text = size.lower().split("x", 1)
    if not width_text.isdigit() or not height_text.isdigit():
        fail("size 必须使用 WIDTHxHEIGHT 格式，例如 1536x1024")
    width = int(width_text)
    height = int(height_text)
    if width <= 0 or height <= 0:
        fail("size 的宽高必须大于 0")
    if width % 16 != 0 or height % 16 != 0:
        fail("size 的宽高必须都是 16 的倍数")
    if max(width, height) > MAX_EDGE:
        fail("size 的最长边不能超过 3840")
    ratio = max(width, height) / min(width, height)
    if ratio > MAX_ASPECT_RATIO:
        fail("size 的宽高比不能超过 3:1")
    pixels = width * height
    if pixels < MIN_PIXELS or pixels > MAX_PIXELS:
        fail(f"size 的总像素必须在 {MIN_PIXELS}..{MAX_PIXELS} 之间")


def validate_common_inputs(plan_input: Dict[str, Any], explicit_fields: Set[str]) -> None:
    if plan_input["backend"] not in BACKENDS:
        fail(f"不支持的 backend '{plan_input['backend']}'，可选: {sorted(BACKENDS)}")
    if plan_input["aspect_ratio"] not in LEGACY_ASPECT_RATIOS:
        fail(f"不支持的 aspect_ratio '{plan_input['aspect_ratio']}'，可选: {LEGACY_ASPECT_RATIOS}")
    if plan_input["quality"] not in ALTERNATIVE_QUALITY_VALUES:
        fail(f"不支持的 quality '{plan_input['quality']}'，可选: {sorted(ALTERNATIVE_QUALITY_VALUES)}")
    if plan_input["background"] == "transparent":
        fail("background='transparent' 已被 SEE2AI 最新 alternative_v1 校验拒绝，请改用 auto 或 opaque")
    if plan_input["background"] not in ALTERNATIVE_BACKGROUND_VALUES:
        fail(
            f"不支持的 background '{plan_input['background']}'，可选: {sorted(ALTERNATIVE_BACKGROUND_VALUES)}"
        )
    if plan_input["moderation"] not in ALTERNATIVE_MODERATION_VALUES:
        fail(
            f"不支持的 moderation '{plan_input['moderation']}'，可选: {sorted(ALTERNATIVE_MODERATION_VALUES)}"
        )
    if plan_input["output_compression"] is not None:
        if not 0 <= plan_input["output_compression"] <= 100:
            fail("output_compression 必须在 0..100 之间")
    if plan_input["n"] is not None:
        if not 1 <= plan_input["n"] <= 1:
            fail("根据 SEE2AI 最新 alternative_v1 校验，n 当前只能为 1")
    if plan_input["size"] is not None:
        validate_size(plan_input["size"])

    if "resolution" in explicit_fields and plan_input["resolution"] not in RESOLUTIONS:
        fail(f"不支持的 resolution '{plan_input['resolution']}'，可选: {sorted(RESOLUTIONS)}")


def validate_no_reference_inputs(config: Dict[str, Any]) -> None:
    # 这里显式拦截参考图字段，是为了防止图生图缺图时被错误降级到文生图脚本执行。
    for field_name in ("image_url", "image_urls", "image_input"):
        if field_name not in config:
            continue
        value = config.get(field_name)
        if value in (None, "", []):
            continue
        fail(
            "see2ai_text_to_image 是纯文生图 Skill，不接受 image_url/image_urls/image_input。"
            "如果用户明确要图生图，请改用 see2ai_image_to_image；若当前缺少参考图，应先补图或明确告知无法按图生图处理。"
        )


def choose_backend(plan_input: Dict[str, Any], explicit_fields: Set[str]) -> str:
    backend = plan_input["backend"]
    if backend != "auto":
        return backend

    alternative_native_fields = {
        "size",
        "quality",
        "background",
        "moderation",
        "output_compression",
        "n",
        "user",
    }
    if explicit_fields & alternative_native_fields:
        return "alternative"

    if "output_format" in explicit_fields and plan_input["output_format"] not in {None, "auto"}:
        return "alternative"

    if plan_input["aspect_ratio"] not in V1_ASPECT_RATIOS:
        return "alternative"

    if plan_input["resolution"] == "4K" and plan_input["aspect_ratio"] in {"1:1", "auto"}:
        # 这里优先切 alternative，是为了兼容 v1 最新显式禁用的 4K+方图/auto 组合。
        return "alternative"

    return "v1"


def build_request_plan(config: Dict[str, Any], explicit_fields: Set[str]) -> Dict[str, Any]:
    validate_no_reference_inputs(config)
    prompt = config.get("prompt")
    if not isinstance(prompt, str) or not prompt.strip():
        fail("缺少 prompt 字段，且未提供可转换的 shot_context")

    plan_input = {
        "prompt": prompt.strip(),
        "backend": normalize_lower_choice(config.get("backend", "auto"), "backend"),
        "aspect_ratio": config.get("aspect_ratio", "auto"),
        "resolution": normalize_resolution(config.get("resolution", "2K")),
        "size": config.get("size"),
        "quality": normalize_lower_choice(config.get("quality", "auto"), "quality"),
        "background": normalize_lower_choice(config.get("background", "auto"), "background"),
        "moderation": normalize_lower_choice(config.get("moderation", "auto"), "moderation"),
        "output_format": normalize_output_format(config.get("output_format")),
        "output_compression": (
            parse_int_value(config.get("output_compression"), "output_compression")
            if "output_compression" in explicit_fields
            else None
        ),
        "n": parse_int_value(config.get("n"), "n") if "n" in explicit_fields else None,
        "user": config.get("user"),
    }

    if not isinstance(plan_input["aspect_ratio"], str) or plan_input["aspect_ratio"] not in LEGACY_ASPECT_RATIOS:
        fail(f"不支持的 aspect_ratio '{plan_input['aspect_ratio']}'，可选: {LEGACY_ASPECT_RATIOS}")
    if plan_input["size"] is not None and (not isinstance(plan_input["size"], str) or not plan_input["size"].strip()):
        fail("size 必须是非空字符串，例如 1536x1024")

    validate_common_inputs(plan_input, explicit_fields)
    resolved_backend = choose_backend(plan_input, explicit_fields)

    if resolved_backend == "v1":
        if plan_input["size"] is not None:
            fail("backend=v1 不接受 size；如需自定义尺寸请改走 alternative")
        if "quality" in explicit_fields:
            fail("backend=v1 不接受 quality")
        if "background" in explicit_fields:
            fail("backend=v1 不接受 background")
        if "moderation" in explicit_fields:
            fail("backend=v1 不接受 moderation")
        if "output_compression" in explicit_fields:
            fail("backend=v1 不接受 output_compression")
        if "user" in explicit_fields:
            fail("backend=v1 不接受 user")
        if "n" in explicit_fields:
            fail("backend=v1 不接受 n")
        if "output_format" in explicit_fields and plan_input["output_format"] not in {None, "auto"}:
            fail("backend=v1 不接受显式 output_format；如需指定格式请改走 alternative")
        if plan_input["aspect_ratio"] not in V1_ASPECT_RATIOS:
            fail("backend=v1 只支持 aspect_ratio: auto / 1:1 / 9:16 / 16:9 / 4:3 / 3:4")
        if plan_input["resolution"] == "4K" and plan_input["aspect_ratio"] in {"1:1", "auto"}:
            fail("backend=v1 不支持 resolution=4K 搭配 aspect_ratio=1:1 或 auto")

        payload = {
            "prompt": plan_input["prompt"],
            "aspect_ratio": plan_input["aspect_ratio"],
            "resolution": plan_input["resolution"],
        }
        return {
            "backend": resolved_backend,
            "endpoint_path": V1_ENDPOINT_PATH,
            "payload": payload,
        }

    if resolved_backend == "fast":
        if plan_input["size"] is not None:
            fail("backend=fast 不接受 size；fast 只接受 aspect_ratio + 1K/2K")
        for field_name in ("quality", "background", "moderation", "output_compression", "n", "user"):
            if field_name in explicit_fields:
                fail(f"backend=fast 不接受 {field_name}")
        if plan_input["aspect_ratio"] == "auto":
            fail("backend=fast 要求显式 aspect_ratio，不能使用 auto")
        if plan_input["aspect_ratio"] not in FAST_ASPECT_RATIOS:
            fail(f"backend=fast 只支持 aspect_ratio: {sorted(FAST_ASPECT_RATIOS)}")
        if plan_input["resolution"] not in FAST_RESOLUTIONS:
            fail("backend=fast 只支持 resolution=1K 或 2K，不支持 4K")
        output_format = plan_input["output_format"] or "jpg"
        if output_format == "auto":
            output_format = "jpg"
        if output_format not in FAST_OUTPUT_FORMATS:
            fail("backend=fast 的 output_format 只支持 jpg/jpeg/png")
        payload = {
            "prompt": plan_input["prompt"],
            # fast action schema 要求 image_input 字段；纯文生图显式传空数组，避免服务端误判。
            "image_input": [],
            "aspect_ratio": plan_input["aspect_ratio"],
            "resolution": plan_input["resolution"],
            "output_format": output_format,
        }
        return {
            "backend": resolved_backend,
            "endpoint_path": FAST_ENDPOINT_PATH,
            "payload": payload,
        }

    # 这里把旧的 aspect_ratio/resolution 转成 size，是为了兼容旧调用方，同时对齐 alternative_v1 新 schema。
    resolved_size = plan_input["size"] or build_size_from_legacy(
        plan_input["aspect_ratio"],
        plan_input["resolution"],
    )
    validate_size(resolved_size)
    payload = {
        "prompt": plan_input["prompt"],
        "image_input": [],
        "size": resolved_size,
        "quality": plan_input["quality"],
        "background": plan_input["background"],
        "moderation": plan_input["moderation"],
        "output_format": plan_input["output_format"] or "auto",
        "output_compression": plan_input["output_compression"] if plan_input["output_compression"] is not None else 100,
        "n": plan_input["n"] if plan_input["n"] is not None else 1,
    }
    if plan_input["user"] is not None:
        payload["user"] = plan_input["user"]
    return {
        "backend": resolved_backend,
        "endpoint_path": ALTERNATIVE_ENDPOINT_PATH,
        "payload": payload,
    }


def generate_image(plan: Dict[str, Any]) -> Dict[str, Any]:
    endpoint = f"{get_base_url()}{plan['endpoint_path']}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {get_api_key()}",
    }

    try:
        response = requests.post(endpoint, json=plan["payload"], headers=headers, timeout=300)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        fail("请求超时（图像生成可能需要较长时间）")
    except requests.exceptions.HTTPError as exc:
        status_code = exc.response.status_code if exc.response is not None else "unknown"
        body = exc.response.text if exc.response is not None else ""
        fail(f"HTTP 错误 {status_code}: {body or exc}")
    except requests.exceptions.RequestException as exc:
        fail(f"请求错误: {exc}")


def parse_result(result: Dict[str, Any]) -> str:
    if not isinstance(result, dict):
        return "错误: 无效的响应格式"

    state = (result.get("status") or result.get("state") or "").upper()
    if state != "SUCCESS":
        error_msg = result.get("error_message") or result.get("message") or result.get("detail")
        if error_msg:
            return f"图像生成失败，状态: {state or 'UNKNOWN'}，错误: {error_msg}"
        return f"图像生成失败，状态: {state or 'UNKNOWN'}"

    result_urls = result.get("result_urls", [])
    if result_urls:
        return "\n".join(result_urls)
    return "未获取到生成的图片 URL"


def print_usage_info(result: Dict[str, Any], plan: Dict[str, Any]) -> None:
    print("\n" + "-" * 50, file=sys.stderr)
    print(f"后端: {plan['backend']}", file=sys.stderr)
    print(f"Action: {plan['endpoint_path']}", file=sys.stderr)
    for field, label in [
        ("task_id", "任务 ID"),
        ("status", "状态"),
        ("state", "State"),
        ("model", "模型"),
        ("source", "来源"),
        ("cost_time", "生成耗时"),
        ("input_tokens", "输入 Tokens"),
        ("output_tokens", "输出 Tokens"),
        ("total_tokens", "总 Tokens"),
        ("cost_points", "Cost Points"),
        ("warnings", "Warnings"),
        ("client_notes", "Client Notes"),
    ]:
        value = result.get(field)
        if value is None:
            continue
        if isinstance(value, (dict, list)):
            value = json.dumps(value, ensure_ascii=False)
        suffix = "ms" if field == "cost_time" else ""
        print(f"{label}: {value}{suffix}", file=sys.stderr)


def parse_inputs() -> Dict[str, Any]:
    parser = argparse.ArgumentParser(
        description="文生图 CLI 工具 - 兼容旧参数并适配 SEE2AI 最新 image actions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 旧调用方式仍可继续使用
  python text_to_image.py "一只可爱的猫咪" --aspect_ratio 16:9 --resolution 2K
  python text_to_image.py --config '{"prompt": "未来城市夜景", "aspect_ratio": "16:9", "resolution": "4K"}'

  # 新的 alternative_v1 原生参数
  python text_to_image.py --config '{"prompt": "未来城市夜景", "size": "2048x1152", "quality": "high"}'
  python text_to_image.py "一只可爱的猫咪" --size 1536x1024 --format png --backend alternative

  # 新的 fast_v1 快速通道（必须显式选择，不会由 auto 隐式切换）
  python text_to_image.py --config '{"prompt": "清爽的商品视觉", "backend": "fast", "aspect_ratio": "4:5", "resolution": "1K"}'
        """,
    )
    parser.add_argument("prompt", nargs="?", default=None, help="描述想要生成的图片的文本提示词")
    parser.add_argument("--aspect_ratio", choices=LEGACY_ASPECT_RATIOS, default=None, help="旧兼容宽高比")
    parser.add_argument("--resolution", choices=sorted(RESOLUTIONS), default=None, help="旧兼容分辨率")
    parser.add_argument("--format", dest="output_format", default=None, help="输出格式：auto/png/jpeg/webp/jpg")
    parser.add_argument("--backend", choices=sorted(BACKENDS), default=None, help="路由后端：auto/v1/alternative")
    parser.add_argument("--size", default=None, help="alternative 原生 size，例如 1536x1024")
    parser.add_argument("--quality", default=None, help="alternative 原生 quality：auto/high/medium/low")
    parser.add_argument("--background", default=None, help="alternative 原生 background：auto/opaque")
    parser.add_argument("--moderation", default=None, help="alternative 原生 moderation：auto/low")
    parser.add_argument("--output_compression", type=int, default=None, help="alternative 原生 output_compression：0-100")
    parser.add_argument("--n", type=int, default=None, help="alternative 原生生成数量：当前仅支持 1")
    parser.add_argument("--user", default=None, help="alternative 原生 user 字段")
    parser.add_argument("--config", help="JSON 配置字符串或 JSON 文件路径，优先级高于其他 CLI 参数")
    parser.add_argument("--verbose", "-v", action="store_true", help="显示详细的任务与消耗信息")
    args = parser.parse_args()

    if args.config:
        config = parse_config(args.config)
        prompt = config.get("prompt")
        if not prompt and config.get("shot_context"):
            config["prompt"] = build_prompt_from_shot_context(config)
        config["verbose"] = bool(config.get("verbose", args.verbose))
        return config

    if not args.prompt:
        fail("请提供 prompt 参数或使用 --config")

    raw_config = {
        key: value
        for key, value in vars(args).items()
        if value is not None and key not in {"config", "verbose"}
    }
    raw_config["verbose"] = args.verbose
    return raw_config


def main() -> None:
    config = parse_inputs()
    explicit_fields = {key for key, value in config.items() if value is not None and key != "verbose"}
    plan = build_request_plan(config, explicit_fields)
    result = generate_image(plan)
    print(parse_result(result))
    if config.get("verbose"):
        print_usage_info(result, plan)


if __name__ == "__main__":
    main()
