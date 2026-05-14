---
name: see2ai_image_normalize
description: >
  将公网图片 URL 标准化为 SEE2AI 托管的稳定压缩图片 URL，供人脸检测、视觉理解、
  视频参考图或图像生成参考图继续使用。Use when a downstream SEE2AI action rejects,
  times out, or may be sensitive to the original image size/format/host. Do NOT use for
  creative image generation or image understanding.
version: 1.0.0
author: TUVE
update: 2026-04-29
action: see2ai_image_normalize_v1
metadata:
  emoji: "🧼"
  requires:
    - SEE2AI_BASE_URL
    - SEE2AI_API_KEY
dependency:
  python:
    - requests
---

# 📋 能力声明 (Capability Declaration)

## trigger_when

- 下游 Action 需要公网图片 URL，但原图可能过大、格式不稳、宿主不稳定或不适合供应商直接读取。
- 需要为 `see2ai_face_detection`、`see2ai_image_understanding`、`see2ai_video_generation`、`see2ai_image_to_image` 准备更稳定的图片输入。
- 用户提供的是已经可公网访问的图片 URL，且目标是“标准化/压缩/转存”，不是重新生成图片。

## do_NOT_trigger_when

- 用户给的是本地图片路径；应先调用 `see2ai_storage_upload` 上传。
- 用户想改图、生成图、描述图片或做人脸检测；本 Skill 只做标准化，不做内容理解或创作。
- 原 URL 已经稳定可用，且下游 Action 没有尺寸、格式或访问风险。

## can_do

- 调用 `see2ai_image_normalize_v1`，返回 `normalized_url`。
- 支持 profile：`face_detection`、`vlm`、`video_reference`、`storage_canonical`、`video_seedance_reference`、`video_kling_reference`、`image_generation_reference`。
- 保留原始 URL 与标准化后图片的尺寸、字节数、处理方法和 warnings，便于上游 Agent 记录。

## cannot_do

- 不能处理本地路径、私有内网 URL 或非图片资源。
- 不能改变图片内容语义、主体、构图或风格。
- 不能替代上传、图像理解、人脸检测或图片生成 Skill。

## known_limitations

- 输入必须是公网 `http/https` 图片 URL。
- 标准化会生成新的独立图片 URL，不会覆盖原始文件。

## fallback_candidates

- `see2ai_storage_upload`
- `see2ai_face_detection`
- `see2ai_image_understanding`

---

# 使用方式

```bash
python skills/see2ai_image_normalize/scripts/image_normalize.py \
  --config '{"image_url": "https://example.com/photo.jpg", "profile": "video_seedance_reference"}'
```

## JSON 配置参数说明

| JSON 字段 | 必填 | 说明 |
|---|---|---|
| `image_url` | ✅ | 要标准化的公网图片 URL |
| `profile` | ❌ | 下游用途，默认 `face_detection` |
| `verbose` | ❌ | 是否在 stderr 输出完整结构化结果 |

## 输出格式

标准输出只打印 `normalized_url`，方便被其他 Skill 串联消费。开启 `verbose` 时，完整响应写入 stderr。
