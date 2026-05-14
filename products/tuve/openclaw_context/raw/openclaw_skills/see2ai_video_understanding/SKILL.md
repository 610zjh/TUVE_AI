---
name: see2ai_video_understanding
description: >
  使用 SEE2AI 多模态大模型 API 对视频进行解析和理解。
  Use when the user needs to analyze, summarize, or extract information from video content.
  Supports video summarization, content analysis, key frame extraction via public URL.
  Do NOT use for local files without uploading first, or for image/document analysis.
version: 1.0.2
author: TUVE
update: 2026-05-13
action: see2ai_llm_doubao_v1
# PRD-0150 (2026-05-13): promoted into SEE2AI platform built-in
# `_video_understanding`. Legacy name `see2ai_video_understanding` is
# preserved via the platform skill's `aliases:` field. See
# src/apps/tuve/platform_skills/_image_understanding/SKILL.md frontmatter
# comments for the full rationale.
deprecated: true
replacement: src/apps/tuve/platform_skills/_video_understanding/SKILL.md
metadata:
  emoji: "🎥"
  requires:
    - SEE2AI_BASE_URL
    - SEE2AI_API_KEY
dependency:
  python:
    - requests
---

# 📋 能力声明 (Capability Declaration)

## trigger_when

- 用户需要总结、描述、分析已有视频内容或提取关键信息。
- `Context & Asset Agent` 已经盘点到视频素材，但素材选择、脚本规划或生成参数仍缺少视频语义、风格、动作或镜头事实。

## do_NOT_trigger_when

- 用户要生成视频，请用 `see2ai_video_generation`。
- 用户要拼接视频，请用 `see2ai_video_concat`。
- 用户只要视频封面图，请用 `see2ai_video_poster`。
- 用户给的是本地视频路径，请先调用 `see2ai_storage_upload`。
- 视频刚上传但当前任务不需要语义理解时，不要为了“上传后必须识视频”的旧流程调用本 Skill。
- 资产已有可信摘要、风格或镜头事实时，优先复用 `AssetBrief` / history files 中的已有事实，不要重复理解。

## can_do

- 调用 `see2ai_llm_doubao_v1` 的 `video_urls` 能力进行开放式视频理解。
- 支持摘要、详细描述、要点提取和场景分析。

## cannot_do

- 不生成、剪辑、拼接或抽帧视频。

## known_limitations

- 输入必须是公网 URL。
- 长视频可能产生较多 token 消耗，必要时先确认分析范围。

## fallback_candidates

- `see2ai_storage_upload`
- `see2ai_video_poster`

---

## 能力边界

- ✅ 支持功能：视频内容描述、摘要生成、关键信息提取、场景分析
- ✅ 适用场景：视频摘要、内容审核、教学视频分析、会议纪要提取
- ❌ 不支持：本地文件直接处理（需先上传获取 URL）
- ❌ 不支持：图片/文档内容分析（请使用对应专用工具）

## 使用方式

### ⚡ 推荐：JSON 配置模式

```bash
python skills/see2ai_video_understanding/scripts/vedio_understanding.py \
  --config '{"video_url": "https://example.com/video.mp4"}'

python skills/see2ai_video_understanding/scripts/vedio_understanding.py \
  --config '{"video_url": "https://example.com/video.mp4", "prompt": "总结这个视频的主要内容"}'
```

### 传统 CLI 模式（仍然支持）

```bash
python skills/see2ai_video_understanding/scripts/vedio_understanding.py <video_url>
python skills/see2ai_video_understanding/scripts/vedio_understanding.py <video_url> "总结这个视频的主要内容"
```

### JSON 配置参数说明

| JSON 字段 | 必填 | 说明 |
|-----------|------|------|
| `video_url` | ✅ | 视频的公网 URL 地址 |
| `prompt` | ❌ | 对视频的提问或提示词（默认："请详细描述这个视频的内容"） |

## 执行流程

1. **接收需求**：确认视频 URL 和分析要求
2. **验证 URL**：检查是否为有效的 http/https 公网 URL
3. **构建提示词**：根据用户需求优化 prompt
4. **执行脚本**：调用 CLI 工具进行视频理解
5. **返回结果**：展示解析内容和 Token 消耗，并把语义事实交给 `Context & Asset Agent` 写入当前任务的资产事实或 `AssetBrief`

### 提示词优化建议

| 用户意图 | 推荐 Prompt |
|----------|-------------|
| 视频摘要 | "请总结这个视频的主要内容" |
| 详细描述 | "详细描述视频中发生的所有事件" |
| 提取要点 | "提取视频中的关键信息和核心观点" |
| 场景分析 | "分析视频中的场景变化和氛围" |
| 教学分析 | "总结这个教学视频的知识要点" |

## 输出格式

### 标准输出

```
[视频解析内容]

==================================================
【思考过程】(如启用思考模式)
[思考内容]
```

## 示例

### 示例 1：视频摘要

```bash
python skills/see2ai_video_understanding/scripts/vedio_understanding.py \
  --config '{"video_url": "https://example.com/video.mp4", "prompt": "请总结这个视频的主要内容"}'
```

### 示例 2：会议视频提取

```bash
python skills/see2ai_video_understanding/scripts/vedio_understanding.py \
  --config '{"video_url": "https://example.com/meeting.mp4", "prompt": "提取会议中的决策事项和行动项"}'
```
