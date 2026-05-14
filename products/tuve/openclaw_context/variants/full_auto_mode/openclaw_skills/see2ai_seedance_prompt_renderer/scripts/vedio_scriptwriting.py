#!/usr/bin/env python3
"""
Seedance 2.0 Just-in-time Prompt Renderer

将单个 shot 的 Production Doc 数据渲染为符合 PRD 0023 / 0024 的
结构化 Seedance 2.0 专属 Prompt 包。
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any


NEGATIVE_CLAUSE = (
    "负向排除：画面模糊、人物变形、动作卡顿、场景跳变、光影错乱、色调异常、"
    "镜头抖动、细节丢失、穿帮画面"
)


def parse_config(config_input: str) -> dict[str, Any]:
    """解析 JSON 配置，支持 JSON 字符串或 JSON 文件路径。"""
    config_input = config_input.strip()

    if not config_input.startswith("{") and os.path.isfile(config_input):
        try:
            with open(config_input, encoding="utf-8") as f:
                config = json.load(f)
        except json.JSONDecodeError as e:
            print(json.dumps({"success": False, "error": f"JSON 文件解析失败: {e}"}, ensure_ascii=False))
            sys.exit(1)
        except OSError as e:
            print(json.dumps({"success": False, "error": f"读取配置文件失败: {e}"}, ensure_ascii=False))
            sys.exit(1)
    else:
        try:
            config = json.loads(config_input)
        except json.JSONDecodeError as e:
            print(json.dumps({"success": False, "error": f"JSON 解析失败: {e}"}, ensure_ascii=False))
            sys.exit(1)

    if not isinstance(config, dict):
        print(json.dumps({"success": False, "error": "配置必须是 JSON 对象"}, ensure_ascii=False))
        sys.exit(1)
    return config


def _filled_slots(slots: list[dict[str, Any]] | None) -> list[dict[str, Any]]:
    """仅保留已填充且带 URL 的槽位。"""
    return [
        slot for slot in (slots or [])
        if slot.get("status") == "filled" and slot.get("url")
    ]


def _ensure_material_limits(image_slots: list[dict[str, Any]],
                            video_slots: list[dict[str, Any]],
                            audio_slots: list[dict[str, Any]]) -> None:
    """执行 PRD 0023 中的硬性素材上限。"""
    total = len(image_slots) + len(video_slots) + len(audio_slots)
    if len(image_slots) > 9:
        raise ValueError("图片素材超限：单片段最多 9 张图片。")
    if len(video_slots) > 3:
        raise ValueError("视频素材超限：单片段最多 3 个视频。")
    if len(audio_slots) > 3:
        raise ValueError("音频素材超限：单片段最多 3 个音频。")
    if total > 12:
        raise ValueError("素材总数超限：单片段最多 12 个素材。")


def _localize_slots(slots: list[dict[str, Any]],
                    global_assets: dict[str, Any],
                    prefix: str) -> list[dict[str, Any]]:
    """
    将当前 shot 的素材重新编号为本片段内局部编号。
    prefix: 图 / 视频 / 音频
    """
    localized = []
    for idx, slot in enumerate(slots, start=1):
        global_asset_id = slot.get("global_asset_id")
        global_name = (
            global_assets.get(global_asset_id, {}).get("global_name")
            if global_asset_id else None
        ) or slot.get("purpose") or f"{prefix}素材{idx}"
        localized.append({
            **slot,
            "local_ref": f"@{prefix}{idx}",
            "global_name": global_name,
        })
    return localized


def _determine_best_entry(shot: dict[str, Any],
                          video_slots: list[dict[str, Any]],
                          audio_slots: list[dict[str, Any]]) -> str:
    """根据 shot 结构决定推荐入口。"""
    if shot.get("entry_type") == "first_last_frame":
        return "首尾帧"
    if video_slots or audio_slots:
        return "全能参考"
    return "全能参考"


def _build_material_lines(image_slots: list[dict[str, Any]],
                          video_slots: list[dict[str, Any]],
                          audio_slots: list[dict[str, Any]]) -> list[str]:
    """渲染【本片段素材清单】。"""
    lines: list[str] = []

    def line_level(slot: dict[str, Any]) -> str:
        role = slot.get("usage_role")
        if role in {"first_frame", "last_frame"}:
            return "核心必传"
        return "可选优化"

    for slot in image_slots:
        lines.append(
            f"- {line_level(slot)}：{slot['local_ref']} -> [全局：{slot['global_name']}]："
            f"{slot.get('purpose', '图片参考')}，用途={slot.get('usage_role', 'image_ref')}，"
            "支持 jpeg/png/webp/bmp/tiff/gif，单张<30MB"
        )
    for slot in video_slots:
        lines.append(
            f"- 可选优化：{slot['local_ref']} -> [全局：{slot['global_name']}]："
            f"{slot.get('purpose', '视频参考')}，用途={slot.get('usage_role', 'video_ref')}，"
            "时长 2-15s，480p-720p，单文件<50MB"
        )
    for slot in audio_slots:
        lines.append(
            f"- 可选优化：{slot['local_ref']} -> [全局：{slot['global_name']}]："
            f"{slot.get('purpose', '音频参考')}，用途={slot.get('usage_role', 'audio_ref')}，"
            "支持 mp3/wav，总时长≤15s，单文件<15MB"
        )

    return lines or ["- 无外部素材，本片段采用纯文本生成。"]


def _build_material_usage(image_slots: list[dict[str, Any]],
                          video_slots: list[dict[str, Any]],
                          audio_slots: list[dict[str, Any]]) -> str:
    """把素材用途压缩成 Prompt 内可直接引用的句子。"""
    parts = []
    for slot in image_slots:
        parts.append(f"{slot['local_ref']}用于{slot.get('purpose', '画面参考')}")
    for slot in video_slots:
        parts.append(f"{slot['local_ref']}用于{slot.get('purpose', '运镜/动作参考')}")
    for slot in audio_slots:
        parts.append(f"{slot['local_ref']}用于{slot.get('purpose', '音频节奏参考')}")
    return "；".join(parts)


def _build_timeline(shot: dict[str, Any]) -> str:
    """根据镜头时长生成紧凑时间轴。"""
    duration = int(shot.get("duration") or 5)
    title = shot.get("title") or "当前镜头"
    intent = shot.get("narrative_intent") or "完成镜头核心表达"
    composition = shot.get("composition_notes") or "镜头稳定、主体清晰"
    voiceover = shot.get("voiceover_line")
    music = shot.get("music_direction")

    seg1 = max(1, duration // 3)
    seg2 = max(seg1 + 1, duration - max(1, duration // 4))

    timeline_parts = [
        f"0-{seg1}秒：建立{title}的主画面，重点表达{intent}，{composition}",
        f"{seg1}-{seg2}秒：强化主体动作、镜头推进和细节层次，保持叙事连贯",
        f"{seg2}-{duration}秒：完成情绪收束与结果落点，镜头节奏自然闭合",
    ]

    if voiceover:
        timeline_parts.append(f"旁白内容围绕“{voiceover}”展开，语气与画面节奏一致")
    if music:
        timeline_parts.append(f"整体声音与节奏方向：{music}")

    return "；".join(timeline_parts)


def _build_director_tips(shot: dict[str, Any],
                         image_slots: list[dict[str, Any]],
                         video_slots: list[dict[str, Any]]) -> list[str]:
    """输出可落地的调优建议。"""
    tips = []
    if video_slots:
        tips.append("动作与运镜控制：如果运镜偏差，优先补充更明确的视频参考素材。")
    else:
        tips.append("动作与运镜控制：若运动感不足，可补充运镜参考视频或在提示词中强化推拉摇移说明。")

    if any(slot.get("usage_role") in {"character_ref", "product_ref", "style_ref"} for slot in image_slots):
        tips.append("一致性与效果优化：若一致性不稳，请补充多角度参考图并保持同一主体在各镜头重复引用。")
    else:
        tips.append("一致性与效果优化：若风格漂移，请补充 style_ref / product_ref 图片作为稳定锚点。")

    if shot.get("voiceover_line"):
        tips.append("音画同步：若口型或节奏不准，请缩短台词长度并明确时间轴中的说话时段。")

    return tips


def render_seedance_package(
    shot: dict[str, Any],
    global_context: dict[str, Any] | None = None,
    global_assets: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """
    渲染单个 shot 为 Seedance 2.0 专属 Prompt 包。
    返回结构化 JSON，供 video_generation 内部直接消费。
    """
    global_context = global_context or {}
    global_assets = global_assets or {}

    image_slots = _filled_slots(shot.get("image_slots"))
    video_slots = _filled_slots(shot.get("video_slots"))
    audio_slots = _filled_slots(shot.get("audio_slots"))

    _ensure_material_limits(image_slots, video_slots, audio_slots)

    localized_images = _localize_slots(image_slots, global_assets, "图")
    localized_videos = _localize_slots(video_slots, global_assets, "视频")
    localized_audios = _localize_slots(audio_slots, global_assets, "音频")

    best_entry = _determine_best_entry(shot, localized_videos, localized_audios)
    duration = int(shot.get("duration") or global_context.get("duration_target") or 5)
    visual_style = global_context.get("visual_style") or "风格统一、细节真实、光影自然"
    aspect_ratio = global_context.get("aspect_ratio") or "9:16"
    composition_notes = shot.get("composition_notes") or "主体清晰、构图稳定"
    shot_function = shot.get("shot_function") or "reveal"
    intent = shot.get("narrative_intent") or shot.get("title") or "完成当前镜头叙事"
    material_usage = _build_material_usage(localized_images, localized_videos, localized_audios)
    timeline = _build_timeline(shot)

    prompt_parts = [
        f"画面整体为{visual_style}，画幅{aspect_ratio}，镜头功能为{shot_function}，核心叙事目标是{intent}。",
        f"构图与摄影要求：{composition_notes}。",
    ]
    if material_usage:
        prompt_parts.append(f"素材引用与用途：{material_usage}。")
    prompt_parts.append(f"时间轴：{timeline}。")
    prompt_parts.append("全片保持物理规律真实、动作流畅、主体一致、风格统一。")
    prompt_parts.append(NEGATIVE_CLAUSE)

    prompt = "".join(prompt_parts)
    if len(prompt) > 800:
        prompt = prompt[:780].rstrip("，。； ") + "。" + NEGATIVE_CLAUSE
        prompt = prompt[:800]

    material_lines = _build_material_lines(localized_images, localized_videos, localized_audios)
    director_tips = _build_director_tips(shot, localized_images, localized_videos)

    markdown_lines = [
        f"### 🎥 片段 {shot.get('shot_id', 1)}：{shot.get('title', '未命名片段')}",
        "",
        "**【⚙️ 核心参数设置】**",
        f"- 最佳入口：{best_entry}",
        f"- 生成时长：{duration}秒",
        "",
        "**【📂 本片段素材清单】**",
        *material_lines,
        "",
        "---",
        "",
        "**【🪄 Seedance 2.0 专属 Prompt】**",
        f"> {prompt}",
        "",
        "---",
        "",
        "**【💡 导演调优指南】**",
        *[f"- {tip}" for tip in director_tips],
    ]

    return {
        "success": True,
        "best_entry": best_entry,
        "duration": duration,
        "aspect_ratio": aspect_ratio,
        "prompt": prompt,
        "materials": {
            "image_slots": localized_images,
            "video_slots": localized_videos,
            "audio_slots": localized_audios,
            "lines": material_lines,
        },
        "director_tips": director_tips,
        "markdown": "\n".join(markdown_lines),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Seedance 2.0 JIT Prompt Renderer")
    parser.add_argument("--config", required=True, help="JSON 配置字符串或 JSON 文件路径")
    args = parser.parse_args()

    config = parse_config(args.config)
    shot = config.get("shot") or config.get("shot_data")
    global_context = config.get("global_context", {})
    global_assets = config.get("global_assets", {})
    output_format = config.get("output_format", "json")

    if not isinstance(shot, dict):
        print(json.dumps({"success": False, "error": "缺少 shot / shot_data 对象"}, ensure_ascii=False))
        sys.exit(1)

    try:
        result = render_seedance_package(shot, global_context, global_assets)
    except Exception as e:
        print(json.dumps({"success": False, "error": str(e)}, ensure_ascii=False))
        sys.exit(1)

    if output_format == "markdown":
        print(result["markdown"])
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
