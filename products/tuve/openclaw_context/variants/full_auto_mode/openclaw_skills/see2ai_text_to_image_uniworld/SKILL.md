---
name: see2ai_text_to_image_uniworld
description: >
  排版与文字特化的文生图 Skill，专门处理文字可读性、多语种信息承载、版式层级与结构化布局优先的图片生成。
  凡生成图中需要出现文字、数字、标题、标签、多语种内容，或需要明确的信息层级、排版布局时，应优先使用本 Skill。
  纯氛围、纯艺术、纯插画、产品展示等“画面视觉优先且不需要文字/排版”的文生图需求，应使用 `see2ai_text_to_image`。
  已有参考图并要求基于图片改图、扩图、换背景或保留主体时，应使用 `see2ai_image_to_image`；不得把图生图失败自动 fallback 到本 Skill。
  Use for typography-first and layout-heavy text-to-image generation: web/mobile page visuals, posters, covers, infographics, presentation slides, social media cards, product detail pages, knowledge graphs, timeline charts, magazine layouts, e-commerce banners, event invitations, certificates, menus, and any image involving readable text, numbers, or structured composition.
  Supports text-to-image generation only (no reference image input).
  Do NOT use for image-to-image tasks or pure visual image generation without text/layout needs.
version: 2.1.0
author: TUVE
update: 2026-04-29
action: see2ai_image_uniworld_v2
metadata:
  emoji: "🧾"
  requires:
    - SEE2AI_BASE_URL
    - SEE2AI_API_KEY
dependency:
  python:
    - requests
---

# 📋 能力声明 (Capability Declaration)

## trigger_when

- 用户要生成含文字、数字、标题、标签、多语种内容或强版式结构的图片。
- 用户要详情页视觉、海报、封面、信息图、PPT 单页、社媒卡片、电商 banner、证书、菜单、功能介绍图等排版优先图片。
- 用户虽只说“做图”，但需求中明显包含信息组织、版式层级或可读文本。

## do_NOT_trigger_when

- 用户提供参考图并要求基于图片改图、扩图、换背景或换风格，应使用 `see2ai_image_to_image`。
- 用户明确只要纯氛围、纯艺术、纯插画且完全不需要任何文字/数字/排版元素，可评估 `see2ai_text_to_image`。
- 用户要视频生成、视频封面或图片理解。

## can_do

- 调用 `see2ai_image_uniworld_v2` 做文字与版式优先的文生图。
- 支持 `prompt`、`canvas_w`、`canvas_h`、`style`、`stylize`。
- 支持异步提交只取 `task_id` / `status`，以及按 `task_id` 查询任务状态。
- 可用于文字/排版优先的文生图；普通纯视觉文生图应优先交给 `see2ai_text_to_image`。

## cannot_do

- 不支持图生图或参考图输入。
- 不做局部编辑、修图、风格迁移或视频生成。
- 不替代普通图片理解/OCR 分析。

## known_limitations

- 这是异步图像生成 action；为兼容既有调用方，脚本默认仍会本地轮询到最终图片链接。
- 新编排若希望统一宿主管理异步状态，推荐显式使用 `--async` 或 JSON 中的 `async=true`，提交后再按 `task_id` 查询状态。
- 聊天中不要主动暴露 `skip_diffusion`、`skip_harmonize`、`max_review_rounds`、`hierarchical` 等底层字段，除非工程调用方明确需要。

## fallback_candidates

- 无自动 fallback。纯视觉文生图应重新路由到 `see2ai_text_to_image`；图生图必须先确认任务重定义后才能另起 `see2ai_image_to_image` 或其他任务。

---

## ⚠️ 调用前必查（红线）

**在调用本工具之前，必须完成以下检查：**

1. **路由边界检查**：本 Skill 是排版与文字特化的文生图入口，不是所有图片生成的兜底入口。为什么这样改：图片类 Skill 必须按用户意图稳定分流，避免把纯视觉图或图生图误路由到排版模型。
   - ✅ 适合本 Skill：图中涉及文字、数字、标题、标签、多语种内容、版式结构、信息层级、排版布局时——这是本模型的核心优势
   - ✅ 典型场景：详情页视觉、手机网页图、杂志/封面版式、信息说明图、时间线图、知识脉络图、PPT 单页视觉、多语种排版图、电商 banner、活动邀请函、证书、社媒卡片、产品功能介绍图、菜单、价目表
   - ❌ 不适合本 Skill：纯氛围、纯艺术、纯插画、产品展示等“画面视觉优先且不需要文字/数字/排版元素”的需求，应使用 `see2ai_text_to_image`
   - ❌ 如果用户上传了商品图/参考图并希望基于图片改图，应改用 `see2ai_image_to_image`
   - ⚠️ 重要：普通文生图（`see2ai_text_to_image`）和图生图（`see2ai_image_to_image`）不是排版模型。只要图中需要可读文字或强排版，必须优先评估本 Skill；但图生图任务不能自动改成文生图，必须先让用户确认任务重定义。
   - ⚠️ 唯一性约束：`UniWorld` 只允许由本 Skill 对外提供；`see2ai_text_to_image` 与 `see2ai_image_to_image` 不允许以内嵌 backend、隐藏切换、兼容层复用或 fallback 的方式使用 `UniWorld`。

2. **参数补全检查**：在执行前必须把以下信息补齐到足够可执行：
   - 这张图的用途是什么
   - 需要多少文字、是否多语种、文字层级如何划分
   - 画布方向或尺寸需求（优先补到 `canvas_w` / `canvas_h`，默认推荐 2K 等效尺寸，即短边约 2048px）
   - 整体视觉风格
   - 如用户特别追求更强设计感，再补问 `stylize`

3. **用户确认**：在调用前**必须**用列表或表格向用户说明：
   - 准备生成什么类型的图
   - 文字内容将如何组织
   - 画布尺寸或横竖版说明
   - 风格描述如何理解
   - 等用户明确说“可以”“开始”“好的”等确认后才能执行；**全自动省心模式**除外：若上游 `AGENTS.md` 已明确进入 Mode 2，则可跳过这轮文字确认，直接执行，并在生成后立即贴出 CDN 链接
   - **严禁甩 JSON/代码给用户看**

**这是一条硬性规则，绝不能拿到一句模糊需求就直接调用！**

## 能力边界

- ✅ 支持功能：文字/排版/结构化信息优先的文生图
- ✅ 核心优势：文字可读性极高、排版精准、版式层级清晰、多语种信息承载可靠、结构化布局准确——远超普通文生图模型
- ✅ 唯一归属：本 Skill 是仓库内 `UniWorld` 能力的唯一合法承载入口
- ✅ 适用场景：所有含文字/数字/排版/布局需求的图片（如详情页、海报、封面、信息图、PPT、社媒卡片、电商 banner、证书、菜单、功能介绍图等）
- ✅ 支持参数：`prompt`、`canvas_w`、`canvas_h`、`style`、`stylize`
- ❌ 不支持：图生图（请使用 `see2ai_image_to_image`）
- ❌ 不支持：局部编辑、风格迁移、图片修改
- ⚠️ 注意：普通文生图（`see2ai_text_to_image`）对文字和排版极不准确，图中只要涉及任何文字/数字/排版元素，必须使用本 Skill

## 对话引导（强制）

在聊天中，主模型必须主动把需求补全到可执行，而不是直接把技术参数甩给用户。

### 基础必问项

1. **用途**：这张图用在什么场景？是详情页、封面、海报、信息图、PPT、社媒卡片、电商 banner，还是纯氛围图？
2. **文字与结构**：图中是否需要文字、数字、标签、标题？需要哪些文字模块？是否有标题、副标题、正文、分栏、多语种内容？如果完全不需要任何文字，是否确认用普通文生图？
3. **尺寸方向**：横版、竖版、方图，或明确到像素尺寸。默认优先推荐 2K 等效尺寸（短边约 2048px），如方图 2048×2048、竖版 1660×2950、横版 3640×2048。
4. **整体风格**：例如杂志感、科技感、极简感、品牌海报感、插画风、写实风。

### 进阶可选项

1. **`stylize`**：只有当用户明确想要更强设计感、更艺术化或更风格化表达时，再补问。

### 固定默认值

以下接口字段虽然存在于权威文档，但当前不在聊天中主动追问，也不在脚本中作为显式入参暴露：

- `skip_diffusion`
- `skip_harmonize`
- `max_review_rounds`
- `hierarchical`

这些字段统一保持接口默认值，避免在缺乏明确产品解释时制造歧义。

## 使用方式

### ⚡ 推荐：JSON 配置模式

```bash
python skills/see2ai_text_to_image_uniworld/scripts/text_to_image_uniworld.py \
  --config '{"prompt": "为护肤品牌生成手机端详情页头图，含中文标题、副标题和三条卖点，版式清晰，杂志感", "canvas_w": 1660, "canvas_h": 2950, "style": "editorial magazine layout"}'

python skills/see2ai_text_to_image_uniworld/scripts/text_to_image_uniworld.py \
  --config '{"prompt": "生成一张介绍人类进化历程的结构化说明图，包含时间线节点和中英文标签", "canvas_w": 2048, "canvas_h": 3072, "style": "clean infographic", "stylize": "medium"}'

# 新编排推荐：异步提交，只拿 task_id / status
python skills/see2ai_text_to_image_uniworld/scripts/text_to_image_uniworld.py \
  --async \
  --config '{"prompt": "生成活动海报，含标题、时间地点和报名二维码占位", "canvas_w": 2048, "canvas_h": 3072, "style": "event poster layout"}'

# 按 task_id 查询状态
python skills/see2ai_text_to_image_uniworld/scripts/text_to_image_uniworld.py \
  --status-task-id "task_xxx"
```

### 传统 CLI 模式（仍然支持）

```bash
python skills/see2ai_text_to_image_uniworld/scripts/text_to_image_uniworld.py \
  "生成杂志风封面版式，包含中英文标题和日期信息" \
  --canvas_w 2048 \
  --canvas_h 3072 \
  --style "editorial cover layout"
```

### 执行行为

- 默认模式会先提交任务，再自动查询状态接口
- 默认固定每 `5` 秒轮询一次，最多等待 `300` 秒
- 默认同步模式成功时标准输出直接返回最终图片链接
- 显式异步模式（`--async` 或 `async=true`）会直接返回 `task_id` / `status` JSON，不在本地轮询
- 状态查询模式（`--status-task-id`）会返回当前任务状态摘要 JSON
- 失败或超时时标准错误输出错误报告，并以非 `0` 状态码退出

### JSON 配置参数说明

| JSON 字段 | 必填 | 说明 |
|-----------|------|------|
| `prompt` | ✅ | 图片生成描述，需包含排版图的内容目标与文字结构要求 |
| `canvas_w` | ❌ | 画布宽度（像素） |
| `canvas_h` | ❌ | 画布高度（像素） |
| `style` | ❌ | 整体视觉方向，如杂志感、科技感、极简感 |
| `stylize` | ❌ | 风格化程度提示，仅在需要更强设计感时使用 |

### 默认保持接口默认值的字段

以下字段不作为当前 Skill 的显式参数暴露：

- `skip_diffusion`
- `skip_harmonize`
- `max_review_rounds`
- `hierarchical`

## 执行流程

1. **判断路由**：确认这是文生图需求（非图生图）。只要图中涉及文字/数字/排版/布局，必须使用本 Skill；仅纯氛围/纯艺术且零文字需求时才降级到普通文生图
2. **补全需求**：补齐用途、文字结构、尺寸方向、整体风格
3. **整理确认单**：用用户能看懂的方式总结将要生成的图
4. **执行生成**：调用 `text_to_image_uniworld.py` 提交任务
5. **选择执行模式**：已有同步调用方可继续走默认轮询；新宿主编排优先使用 `--async`
6. **自动轮询或异步回收**：默认模式每 `5` 秒查询一次任务状态，最多等待 `300` 秒；异步模式由宿主后续按 `task_id` 查询
7. **返回结果**：同步成功时返回最终图片链接；异步时返回任务摘要 JSON；失败时返回错误报告

## 输出格式

### 标准输出

```text
https://cdn1.see2ai.com/path/to/final-image.png
```

### 异步提交输出

```json
{"task_id":"task_xxx","status":"running","model":"system/image_uniworld","source":"uniworld","warnings":[]}
```

### 状态查询输出

```json
{"task_id":"task_xxx","status":"running","image_url":null,"error_message":null,"warnings":[],"progress":[{"step":"layout","message":"processing","percent":35}],"result":null,"model":"system/image_uniworld","source":"uniworld"}
```

### 失败示例

```json
{"task_id":"task_xxx","status":"error","error_message":"上游生成失败","warnings":[]}
```

## 示例

### 示例 1：详情页视觉

```bash
python skills/see2ai_text_to_image_uniworld/scripts/text_to_image_uniworld.py \
  --config '{"prompt": "生成护肤品手机端详情页首屏视觉，包含产品名、核心卖点和成分标签，中文排版清晰", "canvas_w": 1660, "canvas_h": 2950, "style": "clean premium brand layout"}'
```

### 示例 2：结构介绍图

```bash
python skills/see2ai_text_to_image_uniworld/scripts/text_to_image_uniworld.py \
  --config '{"prompt": "生成一张介绍人类进化历程的结构化说明图，包含时间线、阶段名称和简短说明，中英双语", "canvas_w": 2048, "canvas_h": 3072, "style": "educational infographic", "stylize": "medium"}'
```

### 示例 3：PPT 单页视觉

```bash
python skills/see2ai_text_to_image_uniworld/scripts/text_to_image_uniworld.py \
  --config '{"prompt": "生成一页可用于商业汇报 PPT 的封面图，包含主标题、副标题和三段关键词模块，蓝白科技风", "canvas_w": 3640, "canvas_h": 2048, "style": "corporate presentation layout"}'
```
