---
name: see2ai_image_understanding
description: >
  使用 SEE2AI 多模态大模型 API 对图片进行理解与问答分析。
  Use when the user needs to analyze, describe, or ask questions about image content.
  Supports photos, charts, diagrams, screenshots, and any visual content via public URL.
  Do NOT use for face detection, local files without uploading first, or document/video analysis.
version: 1.0.3
author: TUVE
update: 2026-05-13
action: see2ai_llm_doubao_v1
# PRD-0150 (2026-05-13): this skill has been promoted into the SEE2AI
# platform as an in-process built-in. The canonical name is
# `_image_understanding`; the legacy `see2ai_image_understanding` name is
# preserved via the platform skill's `aliases:` field, so existing tenant
# configs / openclaw AGENTS.md references continue to work. The platform
# version routes through `file_recognition_service` cache-aside (no
# redundant Doubao billing when tuve_file_recognitions already has a
# fresh-success row). Keep this SKILL.md here for `deploy.sh test/prod
# update` rsync compatibility, but the platform-side override is now
# load-bearing.
deprecated: true
replacement: src/apps/tuve/platform_skills/_image_understanding/SKILL.md
metadata:
  emoji: "👁️"
  requires:
    - SEE2AI_BASE_URL
    - SEE2AI_API_KEY
dependency:
  python:
    - requests
---

# 📋 能力声明 (Capability Declaration)

## trigger_when

- 用户需要描述图片、OCR、图表解读、商品外观分析或开放式视觉问答。
- `Context & Asset Agent` 已经盘点到图片素材，但素材选择、脚本规划或生成参数仍缺少语义描述。

## do_NOT_trigger_when

- 只需要判断有没有人脸或人脸数量，请用 `see2ai_face_detection`。
- 图片 URL 不稳定或格式可能不适合下游读取时，先考虑 `see2ai_image_normalize`。
- 用户给的是本地文件路径，请先调用 `see2ai_storage_upload`。
- 图片刚上传但当前任务不需要语义理解时，不要为了“上传后必须识图”的旧流程调用本 Skill。
- 资产已有可信描述、OCR 或商品事实时，优先复用 `AssetBrief` / history files 中的已有事实，不要重复理解。

## can_do

- 调用 `see2ai_llm_doubao_v1` 的 `image_urls` 能力进行开放式图片理解。
- 支持图片描述、OCR、图表解读、物体识别和场景分析。

## cannot_do

- 不做专用人脸检测，不返回 `has_face/face_count` 结构化字段。
- 不生成或修改图片。

## known_limitations

- 输入必须是公网 URL。
- 对极小文字、严重压缩图或访问不稳定 URL 的结果可能不稳定。

## fallback_candidates

- `see2ai_face_detection`
- `see2ai_image_normalize`
- `see2ai_storage_upload`

---

## 能力边界

- ✅ 支持类型：照片、图表、截图、海报、菜单、艺术作品等
- ✅ 支持任务：图像描述、内容分析、文字提取(OCR)、图表解读、物体识别
- ✅ 支持形式：对单张图片做开放式提问与视觉问答
- ❌ 不支持：本地文件直接处理（需先上传获取 URL）
- ❌ 不支持：专用人脸检测（请改用 `see2ai_face_detection`）
- ❌ 不支持：文档/视频内容分析（请使用对应专用工具）

## 使用方式

### ⚡ 推荐：JSON 配置模式

```bash
# 基本用法
python skills/see2ai_image_understanding/scripts/image_understanding.py \
  --config '{"image_url": "https://example.com/photo.jpg"}'

# 带自定义提示词
python skills/see2ai_image_understanding/scripts/image_understanding.py \
  --config '{"image_url": "https://example.com/chart.jpg", "prompt": "分析这张图表的数据趋势"}'
```

### 传统 CLI 模式（仍然支持）

```bash
python skills/see2ai_image_understanding/scripts/image_understanding.py <image_url>
python skills/see2ai_image_understanding/scripts/image_understanding.py <image_url> "分析这张图表的数据趋势"
```

### JSON 配置参数说明

| JSON 字段 | 必填 | 说明 |
|-----------|------|------|
| `image_url` | ✅ | 图片的公网 URL 地址 |
| `prompt` | ❌ | 对图片的提问或提示词（默认："请详细描述这张图片的内容"） |

## 执行流程

1. **接收需求**：确认图片 URL 和分析要求
2. **验证 URL**：检查是否为有效的 http/https 公网 URL
3. **构建提示词**：根据用户需求优化 prompt
4. **执行脚本**：调用 CLI 工具进行图像理解
5. **返回结果**：展示解析内容，并把语义事实交给 `Context & Asset Agent` 写入当前任务的资产事实或 `AssetBrief`

> 如果你的真实意图只是判断“这张图有没有人脸”，不要通过提示词绕道走图像理解，直接使用 `see2ai_face_detection`。
> 如果用户只是上传了图片但还没有提出需要图像语义的任务，不要主动调用本 Skill；先让 `Context & Asset Agent` 使用已有文件事实即可。

### 提示词优化建议

| 用户意图 | 推荐 Prompt |
|----------|-------------|
| 描述图片 | "请详细描述这张图片的内容" |
| 提取文字 | "提取图片中的所有文字内容" |
| 分析图表 | "分析这张图表的数据趋势和关键信息" |
| 识别物体 | "识别图片中的所有物体并列出" |
| 解读场景 | "描述这个场景的氛围和细节" |

## 输出格式

### 标准输出

```
[图像解析内容]

==================================================
【思考过程】(如启用思考模式)
[思考内容]
```

## 示例

### 示例 1：描述照片

```bash
python skills/see2ai_image_understanding/scripts/image_understanding.py \
  --config '{"image_url": "https://example.com/photo.jpg", "prompt": "请详细描述这张照片的内容"}'
```

### 示例 2：提取菜单文字

```bash
python skills/see2ai_image_understanding/scripts/image_understanding.py \
  --config '{"image_url": "https://example.com/menu.jpg", "prompt": "提取菜单上的所有菜品名称和价格"}'
```

### 示例 3：分析图表数据

```bash
python skills/see2ai_image_understanding/scripts/image_understanding.py \
  --config '{"image_url": "https://example.com/chart.png", "prompt": "分析这张销售图表的数据趋势和关键指标"}'
```

### 示例 4：识别商品卖点

```bash
python skills/see2ai_image_understanding/scripts/image_understanding.py \
  --config '{"image_url": "https://example.com/product.jpg", "prompt": "描述这张商品图的外观特征、材质和主要卖点"}'
```
