#!/usr/bin/env python3
from __future__ import annotations

"""
排版文生图 CLI 工具
基于 see2ai_image_uniworld_v2 提交文字排版优先的文生图任务。

为什么保留 `uniworld` 作为脚本名：
- 与 skill 目录名和索引入口统一，避免文档、懒加载元数据和脚本调用残留旧 `typesetting` 命名。

用法:
    python text_to_image_uniworld.py <prompt> [--canvas_w <px>] [--canvas_h <px>]
    python text_to_image_uniworld.py "生成杂志封面版式" --canvas_w 2048 --canvas_h 3072
"""

import argparse
import json
import os
import sys
import time

import requests


ENDPOINT_PATH = "/api/v1/actions/see2ai_image_uniworld_v2"
STATUS_ENDPOINT_TEMPLATE = "/api/v1/actions/see2ai_image_uniworld_v2/status/{task_id}"
POLL_INTERVAL_SECONDS = 5
POLL_TIMEOUT_SECONDS = 300


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
        print(
            '正确格式示例: --config \'{"prompt": "生成科技风详情页头图", "canvas_w": 1660, "canvas_h": 2950}\'',
            file=sys.stderr,
        )
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


def build_headers(api_key: str) -> dict[str, str]:
    """统一构建请求头，避免提交与查状态时出现鉴权不一致。"""
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }


def extract_error_detail(response: requests.Response) -> str | None:
    """尽量从服务端响应体中提取可读错误，便于把失败原因直接反馈给上层 Agent。"""
    try:
        data = response.json()
    except ValueError:
        text = response.text.strip()
        return text or None

    if isinstance(data, dict):
        detail = data.get("detail")
        if detail:
            return str(detail)
        error = data.get("error")
        if isinstance(error, dict):
            message = error.get("message")
            if message:
                return str(message)
        message = data.get("message")
        if message:
            return str(message)

    return json.dumps(data, ensure_ascii=False)


def validate_canvas_value(value: object, field_name: str) -> int | None:
    """校验画布尺寸，避免把无效值直接传给接口。"""
    if value is None:
        return None
    if isinstance(value, bool):
        print(f"错误: {field_name} 不能是布尔值", file=sys.stderr)
        sys.exit(1)
    try:
        int_value = int(value)
    except (TypeError, ValueError):
        print(f"错误: {field_name} 必须是整数", file=sys.stderr)
        sys.exit(1)
    if int_value <= 0:
        print(f"错误: {field_name} 必须大于 0", file=sys.stderr)
        sys.exit(1)
    return int_value


def validate_optional_string(value: object, field_name: str) -> str | None:
    """校验可选字符串字段。"""
    if value is None:
        return None
    if not isinstance(value, str):
        print(f"错误: {field_name} 必须是字符串", file=sys.stderr)
        sys.exit(1)
    stripped = value.strip()
    if not stripped:
        return None
    return stripped


def parse_bool_value(value: object, field_name: str) -> bool:
    """统一解析布尔输入，避免 bool("false") 这类隐式真值坑到执行模式。"""
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in {"true", "1", "yes", "y"}:
            return True
        if normalized in {"false", "0", "no", "n"}:
            return False
    print(f"错误: {field_name} 只接受 true / false", file=sys.stderr)
    sys.exit(1)


def resolve_async_mode(config: dict | None, cli_async_mode: bool) -> bool:
    """兼容旧同步默认值，同时允许新调用方显式走 Action 原生异步契约。"""
    if cli_async_mode:
        return True
    if not config:
        return False

    has_async = "async" in config
    has_sync = "sync" in config
    if has_async and has_sync:
        async_mode = parse_bool_value(config["async"], "async")
        sync_mode = parse_bool_value(config["sync"], "sync")
        if async_mode == sync_mode:
            print("错误: async 与 sync 配置冲突，请只保留一个或确保它们语义互补", file=sys.stderr)
            sys.exit(1)
        return async_mode
    if has_async:
        return parse_bool_value(config["async"], "async")
    if has_sync:
        return not parse_bool_value(config["sync"], "sync")
    return False


def resolve_verbose_mode(config: dict | None, cli_verbose: bool) -> bool:
    if cli_verbose:
        return True
    if not config or "verbose" not in config:
        return False
    return parse_bool_value(config["verbose"], "verbose")


def build_payload(
    prompt: str,
    canvas_w: int | None = None,
    canvas_h: int | None = None,
    style: str | None = None,
    stylize: str | None = None,
) -> dict:
    """
    组装请求 payload。

    为什么这样做：
    - 当前排版文生图 Skill 只对用户暴露已明确理解的四项可配置字段；
    - `skip_diffusion` / `skip_harmonize` / `max_review_rounds` / `hierarchical`
      统一依赖接口默认值，避免在缺少产品解释时引入歧义。
    """
    payload = {"prompt": prompt}
    if canvas_w is not None:
        payload["canvas_w"] = canvas_w
    if canvas_h is not None:
        payload["canvas_h"] = canvas_h
    if style:
        payload["style"] = style
    if stylize:
        payload["stylize"] = stylize
    return payload


def submit_task(payload: dict) -> dict:
    """调用 SEE2AI API 提交排版文生图任务。"""
    api_key = get_api_key()
    endpoint = f"{get_base_url()}{ENDPOINT_PATH}"
    headers = build_headers(api_key)

    try:
        response = requests.post(endpoint, json=payload, headers=headers, timeout=300)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("错误: 请求超时（图像生成任务提交可能需要较长时间）", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        response = e.response
        print(f"HTTP 错误: {e}", file=sys.stderr)
        detail = extract_error_detail(response) if response is not None else None
        if response.status_code == 401:
            print("API Key 无效或余额不足", file=sys.stderr)
        elif response.status_code == 402:
            print("账号余额不足", file=sys.stderr)
        elif response.status_code == 404:
            print("接口或任务不存在，请稍后重试", file=sys.stderr)
        elif response.status_code == 422:
            print("请求参数校验失败，请检查 prompt 或画布参数", file=sys.stderr)
        elif response.status_code == 500:
            print("上游提交或托管失败，请稍后重试", file=sys.stderr)
        if detail:
            print(f"服务端详情: {detail}", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}", file=sys.stderr)
        sys.exit(1)


def parse_submit_result(result: dict) -> dict:
    """提取异步提交任务的关键信息。"""
    if not isinstance(result, dict):
        return {"error": "无效的响应格式"}

    summary = {
        "task_id": result.get("task_id", ""),
        "status": result.get("status", ""),
        "model": result.get("model", ""),
        "source": result.get("source", ""),
        "provider_config_id": result.get("provider_config_id"),
        "warnings": result.get("warnings") or [],
    }

    if not summary["task_id"] or not summary["status"]:
        summary["error"] = "响应缺少 task_id 或 status"

    return summary


def summarize_status_result(task_id: str, result: dict) -> dict:
    """把状态接口结果裁成稳定摘要，便于宿主统一处理 async_task。"""
    if not isinstance(result, dict):
        return {
            "task_id": task_id,
            "status": "unknown",
            "error_message": "无效的响应格式",
        }

    return {
        "task_id": result.get("task_id") or task_id,
        "status": result.get("status") or result.get("state") or "unknown",
        "image_url": result.get("image_url"),
        "error_message": result.get("error_message"),
        "warnings": result.get("warnings") or [],
        "progress": result.get("progress") or [],
        "result": result.get("result"),
        "model": result.get("model"),
        "source": result.get("source"),
    }


def query_task_status(task_id: str) -> dict:
    """查询任务当前状态。"""
    api_key = get_api_key()
    endpoint = f"{get_base_url()}{STATUS_ENDPOINT_TEMPLATE.format(task_id=task_id)}"
    headers = build_headers(api_key)

    try:
        response = requests.get(endpoint, headers=headers, timeout=60)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print("错误: 查询任务状态超时", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        response = e.response
        print(f"HTTP 错误: {e}", file=sys.stderr)
        detail = extract_error_detail(response) if response is not None else None
        if response.status_code == 401:
            print("API Key 无效或余额不足", file=sys.stderr)
        elif response.status_code == 404:
            print("任务不存在，可能是 task_id 无效或任务记录已失效", file=sys.stderr)
        elif response.status_code >= 500:
            print("查询任务状态失败，服务端暂时不可用", file=sys.stderr)
        if detail:
            print(f"服务端详情: {detail}", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}", file=sys.stderr)
        sys.exit(1)


def parse_final_result(result: dict) -> str:
    """从最终状态中提取图片链接。"""
    if not isinstance(result, dict):
        print("错误: 无效的响应格式", file=sys.stderr)
        sys.exit(1)

    image_url = result.get("image_url")
    if isinstance(image_url, str) and image_url.strip():
        return image_url.strip()

    nested_result = result.get("result")
    if isinstance(nested_result, dict):
        final_url = nested_result.get("final_url") or nested_result.get("provider_final_url")
        if isinstance(final_url, str) and final_url.strip():
            return final_url.strip()

    print("错误: 任务已完成，但未返回最终图片链接", file=sys.stderr)
    print(json.dumps(result, ensure_ascii=False), file=sys.stderr)
    sys.exit(1)


def build_failure_report(task_id: str, result: dict) -> dict:
    """统一构建失败报告，让上层能直接看到 task_id、状态和服务端错误。"""
    return {
        "task_id": task_id,
        "status": result.get("status") or result.get("state") or "unknown",
        "error_message": result.get("error_message") or result.get("error") or "任务执行失败",
        "warnings": result.get("warnings") or [],
    }


def wait_for_final_result(task_id: str, verbose: bool = False) -> dict:
    """
    轮询直到任务完成或超时。

    为什么固定轮询：
    - 当前 Skill 面向上层 Agent 时，更需要最终图片链接，而不是中间 task_id；
    - 固定 5 秒一次、最多 300 秒，可以兼顾稳定性与调用成本，避免每次都让 Agent 额外写一层状态查询。
    """
    start_time = time.monotonic()

    while True:
        elapsed_seconds = time.monotonic() - start_time
        if elapsed_seconds > POLL_TIMEOUT_SECONDS:
            print(
                f"错误: 任务轮询超时（{POLL_TIMEOUT_SECONDS} 秒），task_id: {task_id}",
                file=sys.stderr,
            )
            sys.exit(1)

        result = query_task_status(task_id)
        status = str(result.get("status") or result.get("state") or "").lower()

        if verbose:
            print(
                f"轮询状态: {status or 'unknown'} (task_id={task_id}, elapsed={int(elapsed_seconds)}s)",
                file=sys.stderr,
            )

        if status == "done":
            return result
        if status in {"error", "failed"}:
            report = build_failure_report(task_id, result)
            print(json.dumps(report, ensure_ascii=False), file=sys.stderr)
            sys.exit(1)

        time.sleep(POLL_INTERVAL_SECONDS)


def print_usage_info(result: dict) -> None:
    """打印 token 与最终结果信息。"""
    usage_info = [
        f"输入 Tokens: {result.get('input_tokens', 0)}",
        f"输出 Tokens: {result.get('output_tokens', 0)}",
        f"总 Tokens: {result.get('total_tokens', 0)}",
        f"任务 ID: {result.get('task_id', 'unknown')}",
        f"状态: {result.get('status', 'unknown')}",
    ]

    model = result.get("model", "unknown")
    source = result.get("source", "unknown")
    usage_info.append(f"模型: {model} (来源: {source})")

    warnings = result.get("warnings") or []
    if warnings:
        usage_info.append(f"警告: {'; '.join(warnings)}")

    image_url = result.get("image_url")
    if image_url:
        usage_info.append(f"结果链接: {image_url}")

    print("\n" + "-" * 50, file=sys.stderr)
    for info in usage_info:
        print(info, file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="排版文生图 CLI 工具 - 面向多文字与结构化排版图片",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 推荐：JSON 配置模式
  python text_to_image_uniworld.py --config '{"prompt": "生成科技风详情页头图，含标题和三条卖点", "canvas_w": 1660, "canvas_h": 2950, "style": "clean premium layout"}'
  python text_to_image_uniworld.py --config '{"prompt": "生成一张中英双语时间线说明图", "canvas_w": 2048, "canvas_h": 3072, "style": "educational infographic", "stylize": "medium"}'

  # 新编排推荐：异步提交 / 查询状态
  python text_to_image_uniworld.py --async --config '{"prompt": "生成招商会海报，含标题与时间地点", "canvas_w": 2048, "canvas_h": 3072}'
  python text_to_image_uniworld.py --status-task-id task_xxx

  # 传统 CLI 模式
  python text_to_image_uniworld.py "生成杂志封面版式，包含中英文标题" --canvas_w 2048 --canvas_h 3072 --style "editorial cover layout"

输出:
  默认同步模式：stdout 直接输出最终图片链接
  异步提交 / 查状态：stdout 输出 JSON 摘要
  失败时 stderr 输出错误报告并返回非 0 状态码
        """,
    )

    parser.add_argument(
        "prompt",
        nargs="?",
        default=None,
        help="描述想要生成的排版图片的文本提示词",
    )
    parser.add_argument(
        "--canvas_w",
        type=int,
        default=None,
        help="画布宽度（像素）",
    )
    parser.add_argument(
        "--canvas_h",
        type=int,
        default=None,
        help="画布高度（像素）",
    )
    parser.add_argument(
        "--style",
        default=None,
        help="整体视觉风格提示，例如 editorial layout / clean infographic",
    )
    parser.add_argument(
        "--stylize",
        default=None,
        help="风格化程度提示，仅在需要更强设计感时使用",
    )
    parser.add_argument(
        "--config",
        help="JSON 配置字符串或 JSON 文件路径，包含所有参数。优先级高于其他 CLI 参数",
    )
    parser.add_argument(
        "--async",
        dest="async_mode",
        action="store_true",
        help="仅提交任务并立即返回 task_id / status，不在本地轮询",
    )
    parser.add_argument(
        "--status-task-id",
        default=None,
        help="只查询已提交任务的状态，适合与 --async 配套使用",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="显示详细的 token 使用信息",
    )

    args = parser.parse_args()

    config = parse_config(args.config) if args.config else None

    status_task_id = validate_optional_string(
        args.status_task_id or ((config or {}).get("status_task_id")),
        "status_task_id",
    )
    if status_task_id:
        status_result = query_task_status(status_task_id)
        print(json.dumps(summarize_status_result(status_task_id, status_result), ensure_ascii=False))
        if args.verbose:
            print_usage_info(status_result)
        return

    async_mode = resolve_async_mode(config, args.async_mode)

    if config:
        prompt = validate_optional_string(config.get("prompt"), "prompt")
        if not prompt:
            print("错误: JSON 配置中缺少 prompt 字段", file=sys.stderr)
            sys.exit(1)
        canvas_w = validate_canvas_value(config.get("canvas_w"), "canvas_w")
        canvas_h = validate_canvas_value(config.get("canvas_h"), "canvas_h")
        style = validate_optional_string(config.get("style"), "style")
        stylize = validate_optional_string(config.get("stylize"), "stylize")
        verbose = resolve_verbose_mode(config, args.verbose)
    else:
        prompt = validate_optional_string(args.prompt, "prompt")
        if not prompt:
            print("错误: 请提供 prompt 参数或使用 --config", file=sys.stderr)
            sys.exit(1)
        canvas_w = validate_canvas_value(args.canvas_w, "canvas_w")
        canvas_h = validate_canvas_value(args.canvas_h, "canvas_h")
        style = validate_optional_string(args.style, "style")
        stylize = validate_optional_string(args.stylize, "stylize")
        verbose = args.verbose

    payload = build_payload(
        prompt=prompt,
        canvas_w=canvas_w,
        canvas_h=canvas_h,
        style=style,
        stylize=stylize,
    )
    submit_result = submit_task(payload)
    summary = parse_submit_result(submit_result)
    task_id = summary.get("task_id")
    if not task_id:
        print("错误: 提交成功但未返回 task_id", file=sys.stderr)
        print(json.dumps(submit_result, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)

    if async_mode:
        # Why: Action 已经以 task_id + status 作为正式异步契约；这里直接暴露，避免
        # Skill 再自创一套本地阻塞轮询协议，方便后续宿主统一编排。
        print(json.dumps(summary, ensure_ascii=False))
        return

    if verbose:
        print(
            f"任务已提交，开始每 {POLL_INTERVAL_SECONDS} 秒查询一次状态，最多等待 {POLL_TIMEOUT_SECONDS} 秒。",
            file=sys.stderr,
        )

    final_result = wait_for_final_result(task_id, verbose=verbose)
    final_url = parse_final_result(final_result)
    print(final_url)

    if verbose:
        print_usage_info(final_result)


if __name__ == "__main__":
    main()
