---
name: see2ai_text_to_image
description: >
  基于文本提示词生成高质量图像（文生图）的兼容适配 Skill。
  适合纯视觉画面生成，如短视频封面、商品展示图、种草配图、概念图、氛围图、插画图。
  默认 `backend=auto`，会在 `see2ai_image_generation_v1` 与 `see2ai_image_generation_alternative_v1` 之间按参数自动路由。
  如明确需要低延迟出图，可显式传 `backend=fast` 调用 `see2ai_image_generation_fast_v1`；auto 不会隐式切 fast。
  旧调用方式 `prompt + aspect_ratio + resolution + output_format` 仍然可用；其中旧的 `aspect_ratio + resolution` 现在优先走 `v1`，而 `size/quality/background/moderation/output_compression/n/user` 会走 `alternative_v1`。
  Do NOT use when the user has uploaded reference images; use `see2ai_image_to_image` instead.
  Do NOT use when the image is text-heavy, typography-first, multilingual, infographic-like, detail-page style, or PPT-like; use `see2ai_text_to_image_uniworld` instead.
  This Skill never uses `UniWorld`; `UniWorld` is only exposed by `see2ai_text_to_image_uniworld`.
version: 2.3.0
author: TUVE
update: 2026-04-29
action: see2ai_image_generation_v1
metadata:
  emoji: "🖼️"
  requires:
    - SEE2AI_BASE_URL
    - SEE2AI_API_KEY
dependency:
  python:
    - requests
---

## ⚠️ 调用前必查（红线）

1. **参考图检查**：如果用户上传了商品图、品牌图、人物图或任何参考图，禁止调用本 Skill，应改用 `see2ai_image_to_image`。
   - 如果用户原本明确要求图生图，但当前缺少可用参考图，也不能把失败场景自动降级到本 Skill；必须先补图或明确告知无法按图生图处理。
2. **排版需求检查**：如果用户要的是多文字、多语种、版式层级、结构化说明图、详情页视觉或 PPT 单页视觉，禁止调用本 Skill，应改用 `see2ai_text_to_image_uniworld`。
3. **UniWorld 边界检查**：本 Skill 绝对不允许以内嵌 backend、隐藏切换、兼容层复用或 fallback 的方式使用 `UniWorld`；如需 `UniWorld`，必须直接路由到 `see2ai_text_to_image_uniworld`。
4. **用户确认**：调用前必须先用用户能理解的话确认要生成什么、画面重点是什么、横竖版和清晰度大概是什么，等用户明确同意后再执行。
5. **不要把旧认知当规则**：`4K` 不再等于“必走 alternative”，`v1` 也不再是只支持 `1K/2K` 的旧 schema。

## 📋 能力声明 (Capability Declaration)

### `trigger_when`

- 用户要从纯文本生成图片，没有参考图输入。
- 用户要的是画面视觉、主体表现、风格氛围、场景感，而不是文字排版能力。
- 用户需要兼容旧式参数调用，或者希望直接传入 `alternative_v1` 原生参数。

### `do_NOT_trigger_when`

- 用户已经上传参考图，或明确说“基于这张图改图/扩图/换背景/换场景”。
- 用户要的是文字可读性优先、排版优先、结构化说明图、信息图、详情页视觉、海报文案图、PPT 单页视觉。
- 用户要的是局部编辑、修图、风格迁移、视频生成。

### `can_do`

- 支持兼容旧调用方式：`prompt + aspect_ratio + resolution + output_format`。
- 支持 `alternative_v1` 原生参数：`size`、`quality`、`background`、`moderation`、`output_format`、`output_compression`、`n`、`user`。
- 支持 `backend=auto / v1 / fast / alternative`，默认 `auto`。
- 支持显式 `backend=fast`：调用 `see2ai_image_generation_fast_v1`，适合更快获得 1K/2K 视觉草图或轻量素材。
- 在走 `alternative` 时，把旧的 `aspect_ratio + resolution` 自动转换成最新的 `size`。

### `cannot_do`

- 不支持图生图；有参考图时必须走 `see2ai_image_to_image`。
- 不保证文字排版、多语种文本渲染、结构化信息布局。
- 不支持局部编辑、抠图式修补、精细修图工作流。
- 不支持 `UniWorld` 能力承载；不得以内嵌 backend、隐藏切换或 fallback 的方式调用 `UniWorld`。

### `known_limitations`

- `backend=v1` 只接受 `prompt + aspect_ratio + resolution` 这一套更窄 schema；若显式要求 `size`、`quality`、`background`、`moderation`、`output_format`、`output_compression`、`n`、`user`，应改走 `alternative`。
- `v1` 只支持 `aspect_ratio = auto / 1:1 / 9:16 / 16:9 / 4:3 / 3:4`，且 `resolution=4K` 不能搭配 `aspect_ratio=1:1` 或 `auto`。
- `backend=fast` 必须显式选择，只支持 `aspect_ratio = 1:1 / 1:4 / 1:8 / 2:3 / 3:2 / 3:4 / 4:1 / 4:3 / 4:5 / 5:4 / 8:1 / 9:16 / 16:9 / 21:9`，不支持 `auto`，且只支持 `resolution=1K/2K`。
- `backend=fast` 的 `output_format` 只支持 `jpg/jpeg/png`，不支持 `webp`。
- `background="transparent"` 会被最新 `alternative_v1` 校验拒绝。
- `alternative` 的 `size` 必须是合法的 `WIDTHxHEIGHT` 或 `auto`，宽高为 16 的倍数，最长边不超过 `3840`，总像素需落在 action 允许范围内。
- `alternative` 当前 `n` 只能为 `1`。
- 本 Skill 的 backend 仅限 `auto / v1 / fast / alternative`，不包含 `UniWorld`。

### `fallback_candidates`

- 排版、文字、多语种、结构化页面图：`see2ai_text_to_image_uniworld`
- 有参考图的图片生成：`see2ai_image_to_image`
- 如果用户原本明确要求图生图但当前缺少参考图：不得自动 fallback，必须先补图或停止处理。

## 能力边界

- ✅ 支持功能：纯文生图，兼容旧输入并适配最新 SEE2AI 图片 action 契约。
- ✅ 适用场景：短视频封面、商品展示图、种草配图、概念图、插画图、氛围图、视频素材配图。
- ✅ 默认路由：`backend=auto`。
- ✅ 旧调用兼容：外部仍可传 `aspect_ratio / resolution / output_format`。
- ✅ 新调用兼容：高级调用方可直接传 `size / quality / background / moderation / output_compression / n / user`，这些参数会路由到 `alternative`。
- ❌ 不适合：详情页视觉、文字海报、多语种排版图、信息图、PPT 单页视觉。
- ❌ 不支持：图生图、局部编辑、风格迁移、修图工作流、任何形式的 `UniWorld` 内嵌或隐藏调用。

## 路由规则

1. 默认 `backend=auto`。
2. 如果出现这些 `alternative` 原生参数中的任意一个：`size`、`quality`、`background`、`moderation`、`output_compression`、`n`、`user`，直接走 `alternative`。
3. 如果显式要求 `output_format` 且不是 `auto`，`auto` 会改走 `alternative`，因为最新 `v1` schema 不接受输出格式字段。
4. 如果仅使用旧式参数，且 `aspect_ratio` 属于 `auto / 1:1 / 9:16 / 16:9 / 4:3 / 3:4`，同时没有命中 `v1` 禁用组合，`auto` 会优先走 `v1`。
5. 如果旧式 `aspect_ratio` 超出 `v1` 支持范围，或命中 `resolution=4K + aspect_ratio=1:1/auto` 这类 `v1` 禁用组合，`auto` 会改走 `alternative` 并把旧参数换算成 `size`。
6. 其他情况默认走 `v1`。
7. 显式指定 `backend=fast` 时，只能传 `prompt + aspect_ratio + resolution + output_format`，其中 `aspect_ratio` 不能是 `auto`，`resolution` 只能是 `1K/2K`。
8. 显式指定 `backend=v1` 时，只能传 `v1` 支持的字段；显式指定 `backend=alternative` 时，可传 `alternative` 原生字段，也可继续让兼容层把旧参数换算成 `size`。

## 参数表

| 字段 | 必填 | 说明 |
|---|---|---|
| `prompt` | 是 | 图像生成提示词 |
| `backend` | 否 | `auto / v1 / fast / alternative`，默认 `auto` |
| `aspect_ratio` | 否 | 旧兼容宽高比参数 |
| `resolution` | 否 | 旧兼容分辨率：`1K / 2K / 4K` |
| `size` | 否 | `alternative` 原生尺寸，如 `1536x1024` |
| `quality` | 否 | `alternative` 原生质量：`auto / high / medium / low` |
| `background` | 否 | `alternative` 原生背景：`auto / opaque` |
| `moderation` | 否 | `alternative` 原生审核强度：`auto / low` |
| `output_format` | 否 | `auto / png / jpeg / webp`，CLI 仍可传 `jpg` 并自动归一化为 `jpeg` |
| `output_compression` | 否 | `0-100`，仅 `alternative` 支持 |
| `n` | 否 | 当前仅支持 `1`，仅 `alternative` 支持 |
| `user` | 否 | `alternative` 原生用户字段 |

## 使用方式

### ⚡ 推荐：JSON 配置模式

```bash
python skills/see2ai_text_to_image/scripts/text_to_image.py \
  --config '{"prompt": "未来城市夜景，霓虹灯闪烁"}'

python skills/see2ai_text_to_image/scripts/text_to_image.py \
  --config '{"prompt": "赛博朋克街景", "aspect_ratio": "16:9", "resolution": "4K"}'

python skills/see2ai_text_to_image/scripts/text_to_image.py \
  --config '{"prompt": "高端产品海报级视觉", "size": "2048x1152", "quality": "high", "output_format": "png"}'

python skills/see2ai_text_to_image/scripts/text_to_image.py \
  --config '{"prompt": "快速生成一张商品场景草图", "backend": "fast", "aspect_ratio": "4:5", "resolution": "1K"}'
```

### 传统 CLI 模式（仍然支持）

```bash
python skills/see2ai_text_to_image/scripts/text_to_image.py "一只可爱的猫咪"
python skills/see2ai_text_to_image/scripts/text_to_image.py "未来城市夜景" --aspect_ratio 16:9 --resolution 2K
python skills/see2ai_text_to_image/scripts/text_to_image.py "品牌视觉海报" --backend alternative --size 1536x1024 --quality high
python skills/see2ai_text_to_image/scripts/text_to_image.py "快速商品场景草图" --backend fast --aspect_ratio 4:5 --resolution 1K
```

## Guardrails

- 走 `v1` 时，不要传 `size`、`quality`、`background`、`moderation`、`output_format`、`output_compression`、`n`、`user`。
- 走 `v1` 时，只支持 `aspect_ratio = auto / 1:1 / 9:16 / 16:9 / 4:3 / 3:4`。
- 走 `v1` 时，`resolution=4K` 不能搭配 `aspect_ratio=1:1` 或 `auto`。
- 走 `fast` 时，不要传 `size`、`quality`、`background`、`moderation`、`output_compression`、`n`、`user`；`aspect_ratio` 必须显式填写且不能为 `auto`；`resolution` 只能是 `1K/2K`。
- 走 `alternative` 时，会把旧的 `aspect_ratio + resolution` 换算成 `size`；如显式传 `size`，需满足最新 action 的尺寸校验范围。
- 走 `alternative` 时，`background="transparent"` 必须直接拒绝，`n` 当前只能为 `1`。

## 输出

标准输出为生成后的图片 URL，每行一个：

```text
https://cdn.see2ai.com/generated/image1.jpg
https://cdn.see2ai.com/generated/image2.jpg
```
