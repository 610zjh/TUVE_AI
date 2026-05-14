#!/usr/bin/env python3
"""
视频生成 CLI 工具 — see2ai_video_generation_v1 客户端（PRD-0103 guided repair 客户端）

设计纲领（2026-04-26 起）：
    1. **Action 是唯一校验权威**：本脚本不再做任何业务校验（duration / 字段冲突 / 数量
       上限 / 模式冲突 等），所有校验下沉到 Action 端的 `validate_video_generation_input`。
       脚本本地只做最小的 env / JSON 形态校验。Why: PRD-0103 引入 guided repair 后，
       Action 一旦拒收会返回完整的「修复指引」结构化 body；本地若先行短路报错就会
       让上游 Agent 与终端用户都看不到这份指引，反而越修越乱。
    2. **不兼容旧字段**：`face_image_url` / `non_face_image_url(s)` 已在 Action 端硬拒，
       本脚本同样不再接受这些字段。Why: 加葱 2026-04-26 「不留技术债」明示。
    3. **needs_repair 双轨呈现**：当 Action 返回 `state="needs_repair"`（HTTP 422）时，
       本脚本会把 RepairGuidance 拆成两个面向：
           ① 给真人用户看的：清晰的客服式中文，标题 + 一两句话 + 候选改法。
           ② 给上游 Agent 看的：机器友好的指令块、问题码、payload_patch_plan、
              minimal_runnable_payload。
       让"用户随时知道下一步是什么、Agent 随时知道下一步是什么"。
    4. **退出码语义**：
         0  = 正常成功；
         2  = needs_repair（请求不可执行，但已附带完整修复指引）；
         3  = 等待用户授权 (awaiting_user_approval)；
         1  = 其他错误（网络 / 鉴权 / 上游 5xx 等）。

CLI / JSON 字段一览（与 Action `VideoGenerationInput` 1:1 对齐）：
    prompt
    model_name                                       (see2ai-video-v2 / -fast)
    first_frame_url, last_frame_url
    reference_image_url, reference_image_urls
    first_frame_contains_real_face,
    last_frame_contains_real_face,
    reference_image_contains_real_face               (Optional[bool] hint, None=自动识别)
    video_url, video_urls                            (≤3 段)
    audio_url, audio_urls                            (≤3 段，且不可孤悬)
    duration, resolution, aspect_ratio
    watermark, generate_audio, enable_web_search, force_asset_upload, sync
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any

import requests


ENDPOINT_PATH = "/api/v1/actions/see2ai_video_generation_v1"

# 仅保留为 CLI choices 提示用；不在脚本端硬拒——拒绝由 Action 端 guided repair 给完整指引。
MODEL_NAMES = [
    "see2ai-video-v2",
    "see2ai-video-v2-fast",
    "doubao-seedance-2-0-260128",
    "doubao-seedance-2-0-fast-260128",
]
RESOLUTIONS = ["480p", "720p", "1080p"]
ASPECT_RATIOS = ["adaptive", "16:9", "9:16", "1:1", "21:9", "4:3", "3:4"]


# ---------------------------------------------------------------------------
# 退出码（脚本契约的一部分；Agent 据此判断下一步动作）
# ---------------------------------------------------------------------------

EXIT_OK = 0
EXIT_GENERIC_ERROR = 1
EXIT_NEEDS_REPAIR = 2
EXIT_AWAITING_APPROVAL = 3


# ---------------------------------------------------------------------------
# env / 输入解析（极小集合，不做业务校验）
# ---------------------------------------------------------------------------


def get_base_url() -> str:
    base_url = os.environ.get("SEE2AI_BASE_URL")
    if not base_url:
        print("错误: 未设置 SEE2AI_BASE_URL 环境变量", file=sys.stderr)
        print("请设置: export SEE2AI_BASE_URL='https://see2ai.com'", file=sys.stderr)
        sys.exit(EXIT_GENERIC_ERROR)
    return base_url.rstrip("/")


def get_api_key() -> str:
    api_key = os.environ.get("SEE2AI_API_KEY")
    if not api_key:
        print("错误: 未设置 SEE2AI_API_KEY 环境变量", file=sys.stderr)
        print("请设置: export SEE2AI_API_KEY='sk-your-api-key'", file=sys.stderr)
        sys.exit(EXIT_GENERIC_ERROR)
    return api_key


def parse_optional_bool(value: str) -> bool:
    """CLI 中显式解析 true/false，避免 bool('false') 被误判为 True。"""
    normalized = value.strip().lower()
    if normalized in {"true", "1", "yes", "y"}:
        return True
    if normalized in {"false", "0", "no", "n"}:
        return False
    raise argparse.ArgumentTypeError("布尔参数只接受 true / false。")


def parse_hint_value(value: Any) -> Any:
    """JSON 配置里 true / false / null 的归一化。"""
    if value is None or isinstance(value, bool):
        return value
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in {"null", "none", ""}:
            return None
        if normalized in {"true", "1", "yes", "y"}:
            return True
        if normalized in {"false", "0", "no", "n"}:
            return False
    raise ValueError(f"hint 字段只接受 true / false / null，收到: {value!r}")


def parse_config(config_input: str) -> dict:
    """支持 JSON 字符串或 JSON 文件路径。"""
    config_input = config_input.strip()

    if not config_input.startswith("{") and os.path.isfile(config_input):
        try:
            with open(config_input, encoding="utf-8") as f:
                config = json.load(f)
            if not isinstance(config, dict):
                print("错误: JSON 文件内容必须是一个对象（字典）", file=sys.stderr)
                sys.exit(EXIT_GENERIC_ERROR)
            return config
        except json.JSONDecodeError as e:
            print(f"错误: JSON 文件解析失败: {e}", file=sys.stderr)
            sys.exit(EXIT_GENERIC_ERROR)
        except OSError as e:
            print(f"错误: 读取配置文件失败: {e}", file=sys.stderr)
            sys.exit(EXIT_GENERIC_ERROR)

    try:
        config = json.loads(config_input)
        if not isinstance(config, dict):
            print("错误: JSON 内容必须是一个对象（字典）", file=sys.stderr)
            sys.exit(EXIT_GENERIC_ERROR)
        return config
    except json.JSONDecodeError as e:
        print(f"错误: JSON 解析失败: {e}", file=sys.stderr)
        print("正确格式示例: --config '{\"prompt\": \"一只猫咪在草地上玩耍\"}'", file=sys.stderr)
        sys.exit(EXIT_GENERIC_ERROR)


# ---------------------------------------------------------------------------
# Payload 组装（与 Action schema 1:1 透传，不做改写）
# ---------------------------------------------------------------------------


# 完整字段白名单——只允许这些字段透传给 Action。Why: 一旦默写错的字段名混进去，
# Action 那边会在 alias 层悄悄归一或报警；本脚本作为「客户端」应该让请求干净进入。
_ACCEPTED_FIELDS = (
    "prompt",
    "model_name",
    "first_frame_url",
    "last_frame_url",
    "reference_image_url",
    "reference_image_urls",
    "first_frame_contains_real_face",
    "last_frame_contains_real_face",
    "reference_image_contains_real_face",
    "video_url",
    "video_urls",
    "audio_url",
    "audio_urls",
    "duration",
    "resolution",
    "aspect_ratio",
    "watermark",
    "generate_audio",
    "enable_web_search",
    "force_asset_upload",
    "sync",
)

# 已下线字段——脚本端硬拒，给清晰指引指向新字段。Why: PRD-0103 一切以现在为准；
# 这里和 Action `_LEGACY_IMAGE_FIELDS` 形成双层守卫。
_RETIRED_FIELDS = {
    "face_image_url": "请改用 reference_image_url + reference_image_contains_real_face=true",
    "face": "请改用 reference_image_url + reference_image_contains_real_face=true",
    "face_image": "请改用 reference_image_url + reference_image_contains_real_face=true",
    "face_url": "请改用 reference_image_url + reference_image_contains_real_face=true",
    "non_face_image_url": "请改用 reference_image_url",
    "non_face_image_urls": "请改用 reference_image_urls",
    "portrait": "请改用 reference_image_url + reference_image_contains_real_face=true",
    "portrait_url": "请改用 reference_image_url + reference_image_contains_real_face=true",
}


def reject_retired_fields(config: dict) -> None:
    """硬拒已下线字段——立即停手，让用户/Agent 看到该往哪里改。"""
    bad = [name for name in _RETIRED_FIELDS if name in config]
    if not bad:
        return
    print("错误: 检测到已下线字段，本脚本不再兼容旧入口。", file=sys.stderr)
    for name in sorted(bad):
        print(f"  · {name}: {_RETIRED_FIELDS[name]}", file=sys.stderr)
    print(
        "Why: 2026-04-26 起 reference_image_url(s) + 可选 *_contains_real_face hint 已是唯一入口。",
        file=sys.stderr,
    )
    sys.exit(EXIT_GENERIC_ERROR)


def build_payload_from_config(config: dict) -> dict:
    """从 JSON / CLI 收上来的 dict 中筛出合法字段，原样透传给 Action。"""
    payload: dict = {}
    for key in _ACCEPTED_FIELDS:
        if key not in config:
            continue
        value = config[key]
        if value is None:
            # None 透传无意义；让 Action 走默认值更干净
            continue
        if key.endswith("_contains_real_face"):
            payload[key] = parse_hint_value(value)
        else:
            payload[key] = value
    return payload


# ---------------------------------------------------------------------------
# needs_repair 双轨呈现（PRD-0103 §5.2 R3 / §5.4 R8）
# ---------------------------------------------------------------------------


def render_needs_repair(guidance: dict) -> None:
    """把 Action 返回的 RepairGuidance 拆给真人用户和上游 Agent 同时消费。

    输出按下列顺序，确保用户先看到「该怎么办」，Agent 再看到「机器指令」。
    所有内容都打到 stderr，stdout 保持干净（仅最终 fallback 留 minimal payload，
    便于 Agent 用 `< video_generation.py ... 2> /dev/null` 取最小可运行配置）。
    """
    issues = guidance.get("issues", []) or []
    options = guidance.get("repair_options", []) or []
    patch = guidance.get("payload_patch_plan", {}) or {}
    minimal = guidance.get("minimal_runnable_payload", {}) or {}
    warnings = guidance.get("warnings", []) or []
    hints = guidance.get("hints", []) or []

    # ── ① 给真人用户看的 ──────────────────────────────────────────
    sep = "─" * 60
    print(f"\n{sep}", file=sys.stderr)
    print("⚠️  请求暂时无法执行（needs_repair）", file=sys.stderr)
    print(sep, file=sys.stderr)

    summary = guidance.get("repair_summary", "") or ""
    if summary:
        print(f"概要: {summary}", file=sys.stderr)

    print("\n[👤 给用户的话]", file=sys.stderr)
    user_msg = guidance.get("user_facing_message", "") or "（无）"
    print(user_msg, file=sys.stderr)

    if options:
        print("\n[🔀 候选改法（请选一种再重试）]", file=sys.stderr)
        for i, opt in enumerate(options, 1):
            label = chr(ord("A") + i - 1)
            print(f"  方案 {label}: {opt.get('title','(无标题)')}", file=sys.stderr)
            desc = opt.get("description", "")
            if desc:
                print(f"    · {desc}", file=sys.stderr)
            if opt.get("keep_fields"):
                print(f"    · 保留字段: {', '.join(opt['keep_fields'])}", file=sys.stderr)
            if opt.get("remove_fields"):
                print(f"    · 删除字段: {', '.join(opt['remove_fields'])}", file=sys.stderr)
            if opt.get("change_fields"):
                print(f"    · 改值字段: {opt['change_fields']}", file=sys.stderr)

    # ── ② 给上游 Agent 看的（机器友好块） ─────────────────────────
    print(f"\n{sep}", file=sys.stderr)
    print("[🤖 给 Agent 的机器指令]", file=sys.stderr)
    print(sep, file=sys.stderr)

    print(f"error_code:      {guidance.get('error_code','')}", file=sys.stderr)
    print(f"repair_category: {guidance.get('repair_category','')}", file=sys.stderr)
    agent_inst = guidance.get("agent_facing_instruction", "") or ""
    if agent_inst:
        print(f"agent_instruction: {agent_inst}", file=sys.stderr)

    if issues:
        print(f"\nissues ({len(issues)}):", file=sys.stderr)
        for i, d in enumerate(issues, 1):
            print(
                f"  {i}. [{d.get('code','')}] field={d.get('field','')}; "
                f"got={d.get('got','')}; severity={d.get('severity','')}",
                file=sys.stderr,
            )
            print(f"     rule: {d.get('rule','')}", file=sys.stderr)
            fix = d.get("fix", "")
            for line in (fix or "").splitlines():
                print(f"     fix:  {line}", file=sys.stderr)
            print(f"     example: {d.get('example','')}", file=sys.stderr)

    if patch:
        print("\npayload_patch_plan:", file=sys.stderr)
        print(json.dumps(patch, ensure_ascii=False, indent=2), file=sys.stderr)
        print(
            "  ⚠️ Agent 切勿在未取得用户认可前自动套用 patch。"
            "应先把改法报给用户，等用户点头再发起新请求。",
            file=sys.stderr,
        )

    if minimal:
        print("\nminimal_runnable_payload (从零开始能跑的最小示例):", file=sys.stderr)
        print(json.dumps(minimal, ensure_ascii=False, indent=2), file=sys.stderr)

    if warnings:
        print("\nnon-blocking warnings (合法但非最优):", file=sys.stderr)
        for w in warnings:
            for line in (w or "").splitlines():
                print(f"  · {line}", file=sys.stderr)

    if hints:
        print("\nlocal-uncheckable hints (上传后才能验证的硬约束):", file=sys.stderr)
        for h in hints:
            print(f"  · {h}", file=sys.stderr)

    print(sep, file=sys.stderr)
    print(
        "下一步: 把上面方案给用户选；用户选定后，把对应字段改完再次调用本脚本。\n"
        "脚本退出码: 2 (EXIT_NEEDS_REPAIR)；Agent 应据此停手等用户。",
        file=sys.stderr,
    )


# ---------------------------------------------------------------------------
# 调用主逻辑
# ---------------------------------------------------------------------------


def call_action(payload: dict) -> tuple[int, dict]:
    """同步调用 Action，返回 (http_status, body)。

    不做任何重试——重试策略由 Agent / 用户 决定，本脚本只是个透明客户端。
    """
    api_key = get_api_key()
    endpoint = f"{get_base_url()}{ENDPOINT_PATH}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    try:
        response = requests.post(endpoint, json=payload, headers=headers, timeout=600)
    except requests.exceptions.Timeout:
        print("错误: 请求超时（视频生成可能需要较长时间）。", file=sys.stderr)
        sys.exit(EXIT_GENERIC_ERROR)
    except requests.exceptions.RequestException as e:
        print(f"网络错误: {e}", file=sys.stderr)
        sys.exit(EXIT_GENERIC_ERROR)

    try:
        body = response.json()
    except ValueError:
        body = {"_raw_text": response.text}
    return response.status_code, body if isinstance(body, dict) else {"_raw_body": body}


def looks_like_repair_guidance(body: dict) -> bool:
    """判断 422 body 是否符合 PRD-0103 RepairGuidance 形态。"""
    return (
        body.get("state") == "needs_repair"
        and body.get("error_code") == "video_request_invalid"
    )


def parse_success_result(body: dict) -> str:
    """从 200 成功响应中提取要给用户看的视频 URL（或 awaiting / running 文案）。"""
    raw_state = body.get("status") or body.get("state", "")
    state = str(raw_state).lower()

    if state == "awaiting_user_approval":
        approval_urls = body.get("approval_urls", {}) or {}
        approve_url = approval_urls.get("approve", "")
        expires_in = body.get("expires_in_s", 300)
        approval_id = body.get("approval_id", "")
        lines = [f"⏳ 等待用户授权（{expires_in}秒内有效）"]
        if approval_id:
            lines.append(f"授权 ID: {approval_id}")
        if approve_url:
            lines.append(f"👉 请点击授权: {approve_url}")
        return "\n".join(lines)

    if state == "running":
        task_id = body.get("task_id", "unknown")
        return f"🚀 任务已提交（异步模式）。task_id={task_id}"

    if state in {"success", "succeeded"}:
        urls = body.get("result_urls", []) or []
        if urls:
            return "\n".join(urls)
        return "成功但未返回视频 URL（请联系平台）。"

    err = body.get("error_message") or body.get("message") or ""
    if err:
        return f"视频生成失败，状态: {raw_state}，错误: {err}"
    return f"视频生成失败，状态: {raw_state}"


def print_usage_info(body: dict) -> None:
    info = [
        f"输入 Tokens: {body.get('input_tokens', 0)}",
        f"输出 Tokens: {body.get('output_tokens', 0)}",
        f"任务 ID:    {body.get('task_id', 'unknown')}",
        f"状态:       {body.get('status') or body.get('state', 'unknown')}",
    ]
    cost_time = body.get("cost_time")
    if cost_time:
        info.append(f"生成耗时:   {cost_time}ms")
    model = body.get("model", "unknown")
    source = body.get("source", "unknown")
    info.append(f"模型:       {model} (来源: {source})")
    sep = "-" * 50
    print(f"\n{sep}", file=sys.stderr)
    for line in info:
        print(line, file=sys.stderr)


# ---------------------------------------------------------------------------
# CLI 入口
# ---------------------------------------------------------------------------


def collect_runtime_config_from_args(args: argparse.Namespace) -> dict:
    """从 argparse Namespace 抽出非 None 字段，组成 dict。"""
    cfg: dict = {}
    for key in _ACCEPTED_FIELDS:
        if not hasattr(args, key):
            continue
        value = getattr(args, key)
        if value is None:
            continue
        cfg[key] = value
    # bool flags 已经是 True/False；store_true 默认 False，None-value 已被剔除。
    # generate_audio 默认 True；--no_audio 反转。
    cfg["generate_audio"] = bool(getattr(args, "generate_audio", True))
    cfg["sync"] = not bool(getattr(args, "async_mode", False))
    return cfg


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "视频生成 CLI 工具 — see2ai_video_generation_v1 客户端\n"
            "Action 端 (PRD-0103) 已升级为 guided repair 契约：\n"
            "请求不可执行时返回 422 + 完整结构化指引；本脚本会双轨呈现给用户与上游 Agent。"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python video_generation.py --config '{"prompt": "一只猫咪在草地上玩耍"}'
  python video_generation.py --config '{"first_frame_url": "https://example.com/portrait.jpg", "first_frame_contains_real_face": true, "prompt": "女孩看向镜头", "duration": 8, "aspect_ratio": "9:16"}'
  python video_generation.py --reference_image_url "https://example.com/product.jpg" --prompt "让产品自然转动"

退出码:
  0 = 成功 / running / awaiting_approval（成功提交）
  2 = needs_repair（已附带完整修复指引，用户需选择改法）
  3 = awaiting_user_approval（已等用户授权链接）
  1 = 其他错误（网络 / 鉴权 / 上游 5xx）
        """,
    )

    parser.add_argument("--config", help="JSON 配置字符串或 JSON 文件路径，优先级最高")

    parser.add_argument("--prompt", help="文本提示词")
    parser.add_argument("--model_name", choices=MODEL_NAMES, default=None, help="模型版本（默认 see2ai-video-v2）")

    parser.add_argument("--first_frame_url", help="首帧图片 URL")
    parser.add_argument("--last_frame_url", help="尾帧图片 URL")
    parser.add_argument("--reference_image_url", help="参考图片 URL（单图）")
    parser.add_argument("--reference_image_urls", nargs="+", help="参考图片 URL 列表（最多 9 张）")

    parser.add_argument("--first_frame_contains_real_face", type=parse_optional_bool,
                        help="首帧是否含真人脸（true/false；不传 = 服务端自动识别）")
    parser.add_argument("--last_frame_contains_real_face", type=parse_optional_bool,
                        help="尾帧是否含真人脸（true/false；不传 = 服务端自动识别）")
    parser.add_argument("--reference_image_contains_real_face", type=parse_optional_bool,
                        help="参考图是否含真人脸（true/false；对单图与多图共用同一布尔）")

    parser.add_argument("--video_url", help="参考视频 URL（单段）")
    parser.add_argument("--video_urls", nargs="+", help="参考视频 URL 列表（最多 3 段）")
    parser.add_argument("--audio_url", help="参考音频 URL（单段）")
    parser.add_argument("--audio_urls", nargs="+", help="参考音频 URL 列表（最多 3 段）")

    parser.add_argument("--duration", type=int, default=None,
                        help="时长秒数（4–15 或 -1 自动）；本脚本不做范围校验，下沉到 Action")
    parser.add_argument("--resolution", choices=RESOLUTIONS, default=None, help="分辨率")
    parser.add_argument("--aspect_ratio", choices=ASPECT_RATIOS, default=None, help="宽高比")

    parser.add_argument("--watermark", action="store_true", default=None, help="添加水印")
    parser.add_argument("--no_audio", dest="generate_audio", action="store_false", default=True,
                        help="不生成同步音频（默认会自动生成）")
    parser.add_argument("--enable_web_search", action="store_true", default=None, help="开启联网搜索增强")
    parser.add_argument("--force_asset_upload", action="store_true", default=None,
                        help="强制全部素材走素材库（显著拉长耗时）")
    parser.add_argument("--async", dest="async_mode", action="store_true", help="异步提交，立即返回 task_id")
    parser.add_argument("--verbose", "-v", action="store_true", help="打印 token / 任务元信息")

    args = parser.parse_args()

    # 1. 配置来源：--config 优先；否则从命令行 args 拼
    if args.config:
        config = parse_config(args.config)
    else:
        config = collect_runtime_config_from_args(args)

    # 2. 硬拒已下线字段（脚本端清晰指引）
    reject_retired_fields(config)

    # 3. 透传给 Action（不做业务校验）
    payload = build_payload_from_config(config)

    if not payload:
        print("错误: 没有任何有效字段。请至少提供 --prompt 或一个素材字段，或用 --config 传完整 JSON。",
              file=sys.stderr)
        return EXIT_GENERIC_ERROR

    # 4. 调用 Action 并双轨呈现结果
    status, body = call_action(payload)

    # 4.a needs_repair (HTTP 422 + RepairGuidance body)
    if status == 422 and looks_like_repair_guidance(body):
        render_needs_repair(body)
        return EXIT_NEEDS_REPAIR

    # 4.b 其他 4xx / 5xx — 把 body 作为机器友好诊断块打印出来，让 Agent 看到原始上游回执
    if status >= 400:
        print(f"\n请求失败 (HTTP {status})", file=sys.stderr)
        print(json.dumps(body, ensure_ascii=False, indent=2), file=sys.stderr)
        if status == 401:
            print("提示: API Key 无效或已过期。", file=sys.stderr)
        elif status == 402:
            print("提示: 账号余额不足。", file=sys.stderr)
        elif status == 429:
            print("提示: 请求频率超限，请稍后重试。", file=sys.stderr)
        elif 500 <= status < 600:
            print("提示: 上游或网关异常，可稍后重试。", file=sys.stderr)
        return EXIT_GENERIC_ERROR

    # 4.c 200 success / running / awaiting_approval
    raw_state = str(body.get("status") or body.get("state", "")).lower()
    summary = parse_success_result(body)
    print(summary)

    if args.verbose:
        print_usage_info(body)

    if raw_state == "awaiting_user_approval":
        return EXIT_AWAITING_APPROVAL
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
