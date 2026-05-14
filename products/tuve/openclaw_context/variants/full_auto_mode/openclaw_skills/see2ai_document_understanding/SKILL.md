---
name: see2ai_document_understanding
description: >
  使用 SEE2AI 多模态大模型 API 对单个文档（PDF、TXT格式文档）进行解析和理解。
  Use when the user needs to analyze, summarize, extract information from a document, or ask questions about document content.
  Supports PDF and TXT formats via public URL.
  Do NOT use for local files without uploading first, or for image/video analysis (use image_understanding or video_understanding instead).
version: 1.0.3
author: TUVE
update: 2026-05-13
action: see2ai_llm_gemini_pro_v1
# PRD-0150 (2026-05-13): promoted into SEE2AI platform built-in
# `_document_understanding`. Legacy name `see2ai_document_understanding`
# is preserved via the platform skill's `aliases:` field. See
# src/apps/tuve/platform_skills/_image_understanding/SKILL.md frontmatter
# comments for the full rationale.
deprecated: true
replacement: src/apps/tuve/platform_skills/_document_understanding/SKILL.md
metadata:
  emoji: "📄"
  requires:
    - SEE2AI_BASE_URL
    - SEE2AI_API_KEY
dependency:
  python:
    - requests
---

# 📋 能力声明 (Capability Declaration)

## trigger_when

- 用户需要总结、分析、翻译或问答单个 PDF/TXT 公网文档。
- `Context & Asset Agent` 已经盘点到文档素材，但需求对齐、脚本规划或品牌/产品事实抽取仍缺少文档语义。

## do_NOT_trigger_when

- 文档是本地文件路径，请先调用 `see2ai_storage_upload` 上传。
- 用户要分析图片或视频，请改用对应视觉理解 Skill。
- 用户要处理 docx/xlsx/pptx 等 Office 文件时，应先转换为 PDF 或确认 SEE2AI 当前是否支持。
- 文档刚上传但当前任务不需要语义抽取时，不要为了“上传后必须识文档”的旧流程调用本 Skill。
- 资产已有可信摘要、卖点或品牌事实时，优先复用 `AssetBrief` / history files 中的已有事实，不要重复理解。

## can_do

- 调用 `see2ai_llm_gemini_pro_v1` 的 `document_urls` 能力分析 PDF/TXT。
- 支持总结、信息提取、问答分析、内容翻译。

## cannot_do

- 不能直接读取本地文件。
- 不能替代图片理解、视频理解或文件上传。

## known_limitations

- 输入必须是公网 URL。
- 长文档可能消耗较多 token，必要时先让用户确认范围。

## fallback_candidates

- `see2ai_storage_upload`
- `see2ai_image_understanding`

---

## 能力边界

- ✅ 支持格式：PDF、TXT格式文档
- ✅ 支持任务：文档总结、信息提取、问答分析、内容翻译
- ❌ 不支持：本地文件直接处理（需先上传获取 URL）
- ❌ 不支持：图片/视频内容分析（请使用对应专用工具）

## 使用方式

### ⚡ 推荐：JSON 配置模式

```bash
# 基本用法
python skills/see2ai_document_understanding/scripts/document_understanding.py \
  --config '{"document_url": "https://example.com/document.pdf"}'

# 带自定义提示词
python skills/see2ai_document_understanding/scripts/document_understanding.py \
  --config '{"document_url": "https://example.com/report.pdf", "prompt": "提取文档中的关键数据"}'

# 当前仅支持 Gemini 模型
python skills/see2ai_document_understanding/scripts/document_understanding.py \
  --config '{"document_url": "https://example.com/paper.pdf", "prompt": "总结这份报告"}'
```

### 传统 CLI 模式

```bash
python skills/see2ai_document_understanding/scripts/document_understanding.py <document_url>
python skills/see2ai_document_understanding/scripts/document_understanding.py <document_url> "提取文档中的关键数据"
python skills/see2ai_document_understanding/scripts/document_understanding.py <document_url> "总结这份报告"
```

### JSON 配置参数说明

| JSON 字段 | 必填 | 说明 |
|-----------|------|------|
| `document_url` | ✅ | 文档的公网 URL 地址 |
| `prompt` | ❌ | 对文档的提问或提示词（默认："请详细总结这份文档的主要内容"） |

## 执行流程

### 标准流程

1. **接收用户需求**：确认文档 URL 和分析要求
2. **验证 URL 格式**：检查是否为有效的 http/https 公网 URL
3. **构建提示词**：根据用户需求优化 prompt
4. **执行脚本**：调用 CLI 工具进行文档理解
5. **返回结果**：向用户展示解析内容，并把抽取到的品牌、产品、脚本或约束事实交给 `Context & Asset Agent` 写入当前任务的资产事实或 `AssetBrief`

##### 提示词优化建议

| 用户意图 | 推荐 Prompt |
|----------|-------------|
| 总结文档 | "请详细总结这份文档的主要内容" |
| 提取要点 | "提取文档中的核心观点和关键信息" |
| 问答分析 | "根据文档内容回答：[具体问题]" |
| 数据提取 | "提取文档中的所有表格数据和数字信息" |
| 翻译内容 | "将文档内容翻译成中文并总结" |

## 输出格式

### 标准输出

```
[文档解析内容]

==================================================
【思考过程】(如启用思考模式)
[思考内容]
```

## 示例

### 示例 1：总结 PDF 报告

```bash
python skills/see2ai_document_understanding/scripts/document_understanding.py \
  --config '{"document_url": "https://example.com/annual-report.pdf", "prompt": "请详细总结这份报告的主要内容"}'
```

### 示例 2：提取特定信息

```bash
python skills/see2ai_document_understanding/scripts/document_understanding.py \
  --config '{"document_url": "https://example.com/paper.pdf", "prompt": "提取论文中的研究方法部分，详细说明实验设计和数据分析方法"}'
```

### 示例 3：合同条款分析

```bash
python skills/see2ai_document_understanding/scripts/document_understanding.py \
  --config '{"document_url": "https://example.com/contract.pdf", "prompt": "分析合同中的关键条款，包括付款条件、违约责任和保密条款"}'
```
