---
name: see2ai_video_poster
description: >
  从公网视频 URL 中抽取首个非黑屏帧，返回 PNG 封面 URL。Use when a generated or
  uploaded video needs a preview poster/thumbnail for review, asset registry, or delivery.
  Do NOT use for video understanding, editing, concatenation, or generation.
version: 1.0.0
author: TUVE
update: 2026-04-29
action: see2ai_video_poster_v1
metadata:
  emoji: "🖼️"
  requires:
    - SEE2AI_BASE_URL
    - SEE2AI_API_KEY
dependency:
  python:
    - requests
---

# 📋 能力声明 (Capability Declaration)

## trigger_when

- 已有视频 URL，需要生成封面图、预览图、缩略图或资产库 poster。
- 分段视频或最终成片交付前，需要给用户展示视频的首个有效画面。
- 工作流需要为视频资产补充 `poster_url`。

## do_NOT_trigger_when

- 用户要生成新视频，请用 `see2ai_video_generation`。
- 用户要拼接视频，请用 `see2ai_video_concat`。
- 用户要理解视频内容、总结视频或提取语义，请用 `see2ai_video_understanding`。
- 用户提供的是本地视频文件；应先调用 `see2ai_storage_upload`。

## can_do

- 调用 `see2ai_video_poster_v1`，从视频中抽取首个非黑屏帧。
- 返回 `poster_url`，适合作为视频预览或资产登记字段。

## cannot_do

- 不会转码、剪辑、拼接或生成视频。
- 不会把 PNG 封面转存为其他格式；如需转存，交由上游工作流决定。
- 不支持本地路径或私有不可访问 URL。

## known_limitations

- 输入必须是公网 `http/https` 视频 URL。
- 如果上游视频不可读、全黑或供应商抽帧失败，Action 可能返回 4xx/5xx。

## fallback_candidates

- `see2ai_storage_upload`
- `see2ai_video_understanding`

---

# 使用方式

```bash
python skills/see2ai_video_poster/scripts/video_poster.py \
  --config '{"video_url": "https://example.com/video.mp4"}'
```

## JSON 配置参数说明

| JSON 字段 | 必填 | 说明 |
|---|---|---|
| `video_url` | ✅ | 要抽封面的公网视频 URL |
| `verbose` | ❌ | 是否在 stderr 输出完整结构化结果 |

## 输出格式

标准输出只打印 `poster_url`。
