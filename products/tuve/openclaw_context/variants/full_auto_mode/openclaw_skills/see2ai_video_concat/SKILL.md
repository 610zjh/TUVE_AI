---
name: see2ai_video_concat
description: >
  将多个视频片段拼接合并为一个完整视频。
  Use when the user needs to merge multiple video clips into a single video.
  Supports concatenating 2 or more video segments in sequence.
  Do NOT use for video generation or video editing with effects.
version: 1.0.1
author: TUVE
update: 2026-04-29
action: see2ai_video_concat_v1
metadata:
  emoji: "🎞️"
  requires:
    - SEE2AI_BASE_URL
    - SEE2AI_API_KEY
dependency:
  python:
    - requests
---

# 📋 能力声明 (Capability Declaration)

## trigger_when

- 用户已有两个或更多视频 URL，希望按顺序拼接成一个完整视频。
- 多镜头生成完成后，`Creative Planner Agent` 已经确认需要合成为最终成片。

## do_NOT_trigger_when

- 用户要生成新视频，请用 `see2ai_video_generation`。
- 用户要抽封面，请用 `see2ai_video_poster`。
- 用户要理解视频内容，请用 `see2ai_video_understanding`。
- 视频片段顺序、数量或来源尚未被 `Context & Asset Agent` / `Creative Planner Agent` 确认时，先补齐计划，不要直接拼接。

## can_do

- 调用 `see2ai_video_concat_v1`，对外兼容 `video_urls`，后端实际发送 `media_urls`。
- 返回拼接后的视频 URL。

## cannot_do

- 不做转场、字幕、配乐混音或复杂剪辑。
- 不处理本地视频路径，需先上传。

## known_limitations

- 至少需要 2 个公网视频 URL。

## fallback_candidates

- `see2ai_storage_upload`
- `see2ai_video_poster`

---

## 能力边界

- ✅ 支持功能：视频片段顺序拼接
- ✅ 输入要求：至少 2 个视频 URL
- ✅ 输出：拼接后的完整视频 URL
- ❌ 不支持：视频生成（请使用 video_generation）
- ❌ 不支持：视频特效、转场效果、音频混合

## 使用方式

### ⚡ 推荐：JSON 配置模式

```bash
# 拼接两个视频
python skills/see2ai_video_concat/scripts/video_concat.py \
  --config '{"video_urls": ["https://example.com/video1.mp4", "https://example.com/video2.mp4"]}'

# 拼接多个视频（显示详细信息）
python skills/see2ai_video_concat/scripts/video_concat.py \
  --config '{"video_urls": ["https://example.com/clip1.mp4", "https://example.com/clip2.mp4", "https://example.com/clip3.mp4"]}'
```

### 传统 CLI 模式（仍然支持）

```bash
python skills/see2ai_video_concat/scripts/video_concat.py \
  https://example.com/video1.mp4 https://example.com/video2.mp4
```

### JSON 配置参数说明

| JSON 字段 | 必填 | 说明 |
|-----------|------|------|
| `video_urls` | ✅ | 需要拼接的视频 URL 列表（数组，至少两个） |

## 执行流程

1. **接收需求**：确认需要拼接的视频列表
2. **验证 URL**：检查是否至少提供 2 个有效的 http/https URL
3. **执行拼接**：调用 CLI 工具进行视频拼接
4. **返回结果**：展示拼接后的视频 URL，并把最终成片 URL 交给当前任务状态层记录为交付资产

## 输出格式

### 标准输出

```
https://cdn.see2ai.com/concatenated/video.mp4
```

## 示例

### 示例 1：拼接两个视频片段

```bash
python skills/see2ai_video_concat/scripts/video_concat.py \
  --config '{"video_urls": ["https://cdn.see2ai.com/clip1.mp4", "https://cdn.see2ai.com/clip2.mp4"]}'
```

### 示例 2：拼接多个视频片段

```bash
python skills/see2ai_video_concat/scripts/video_concat.py \
  --config '{"video_urls": ["https://cdn.see2ai.com/intro.mp4", "https://cdn.see2ai.com/content.mp4", "https://cdn.see2ai.com/outro.mp4"]}'
```
