---
name: see2ai_image_to_image
description: >
  基于参考图片生成新图像的兼容适配 Skill。
  适合商品图生成、模特换装、场景变换、风格转换、多图参考生成等图生图任务。
  默认 `backend=auto`，会在 `see2ai_image_generation_v1` 与 `see2ai_image_generation_alternative_v1` 之间按参数自动路由。
  如明确需要低延迟参考图生成，可显式传 `backend=fast` 调用 `see2ai_image_generation_fast_v1`；auto 不会隐式切 fast。
  旧调用方式 `image_url + prompt + aspect_ratio + resolution + output_format` 仍然可用；其中旧的 `image_url/image_urls + aspect_ratio + resolution` 现在优先走 `v1`，而 `size/quality/background/moderation/output_compression/n/user` 会走 `alternative_v1`。
  Do NOT use for text-only generation with no reference image.
  If the user explicitly asked for image-to-image but no usable reference image exists, you must ask the user to补充参考图 or clearly state that the task cannot be completed as image-to-image. Never auto-downgrade to any text-to-image Skill.
version: 2.3.0
author: TUVE
update: 2026-04-29
action: see2ai_image_generation_v1
metadata:
  emoji: "🧩"
  requires:
    - SEE2AI_BASE_URL
    - SEE2AI_API_KEY
dependency:
  python:
    - requests
---

## ⚠️ 调用前必查（红线）

1. **参考图必须存在**：没有参考图时禁止调用本 Skill。若用户明确要求图生图，必须先要求补充参考图；若用户无法提供，则应明确告知当前无法按图生图处理，绝不能自动改用任何文生图 Skill。
2. **先确认参考图来源**：必须使用可公网访问的 URL，不能把本地路径或临时不可访问链接直接传给 Skill。
3. **用户确认**：调用前必须确认参考哪张图、要改成什么样、重点保留哪些主体特征、横竖版与清晰度大概是什么，等用户明确同意后再执行。
4. **不要把旧认知当规则**：`4K` 不再等于“必走 alternative”，真正是否走 `alternative` 取决于参数组合是否兼容它的更窄 schema。

## 📋 能力声明 (Capability Declaration)

### `trigger_when`

- 用户已经提供参考图，希望基于该图改图、扩图、换背景、换场景、换展示方式、换风格。
- 用户要做商品图生成、模特换装、场景合成、多角度展示、参考图延展。
- 用户需要兼容旧式图生图参数调用，或希望直接传 `alternative_v1` 原生参数。

### `do_NOT_trigger_when`

- 用户没有参考图，只是纯文本描述想要什么画面。
- 用户虽然口头上提到“图生图/按这张图改”，但当前没有可用参考图；这种情况应先澄清补图或停止处理，不属于可自动改路由到文生图的触发条件。
- 用户重点要的是文字排版、多语种文本、结构化信息图，而不是基于参考图改图。
- 用户要的是视频生成或非图片任务。

### `can_do`

- 支持兼容旧调用方式：`image_url + prompt + aspect_ratio + resolution + output_format`。
- 支持 `image_url` 和 `image_urls`；如果两者同时存在，优先使用 `image_urls`。
- 支持 `alternative_v1` 原生参数：`size`、`quality`、`background`、`moderation`、`output_format`、`output_compression`、`n`、`user`。
- 在走 `v1` 时自动把图片字段切换为 `input_urls`；在走 `alternative` 时自动使用 `image_input`。
- 支持显式 `backend=fast`：调用 `see2ai_image_generation_fast_v1`，自动使用 `image_input`，适合快速参考图生成。

### `cannot_do`

- 不支持纯文生图；没有参考图时必须要求补图或明确告知当前无法按图生图处理，不能自动改走任何文生图 Skill。
- 不保证复杂排版、多文字信息图、详情页式文案图的文本渲染质量。
- 不支持以 fallback、隐藏 backend 或兼容层切换的方式使用 `UniWorld`；`UniWorld` 只允许由 `see2ai_text_to_image_uniworld` 对外提供。
- 不支持视频生成与非图片任务。

### `known_limitations`

- `backend=v1` 只接受 `prompt + input_urls + aspect_ratio + resolution` 这一套更窄 schema；若显式要求 `size`、`quality`、`background`、`moderation`、`output_format`、`output_compression`、`n`、`user`，应改走 `alternative`。
- `v1` 只支持 `aspect_ratio = auto / 1:1 / 9:16 / 16:9 / 4:3 / 3:4`，且 `resolution=4K` 不能搭配 `aspect_ratio=1:1` 或 `auto`。
- `v1` 最多支持 16 张参考图；`alternative` 与 `fast` 最多支持 14 张参考图。
- `backend=fast` 必须显式选择，只支持 `aspect_ratio = 1:1 / 1:4 / 1:8 / 2:3 / 3:2 / 3:4 / 4:1 / 4:3 / 4:5 / 5:4 / 8:1 / 9:16 / 16:9 / 21:9`，不支持 `auto`，只支持 `resolution=1K/2K`，且最多 14 张参考图。
- `backend=fast` 的 `output_format` 只支持 `jpg/jpeg/png`，不支持 `webp`。
- `background="transparent"` 会被最新 `alternative_v1` 校验拒绝。
- `alternative` 的 `size` 必须是合法的 `WIDTHxHEIGHT` 或 `auto`，宽高为 16 的倍数，最长边不超过 `3840`，总像素需落在 action 允许范围内。
- `alternative` 当前 `n` 只能为 `1`。

### `fallback_candidates`

- 无自动 fallback；图生图条件不满足时，必须先澄清补图或明确停止处理。
- 如果用户明确放弃图生图，并重新定义为“文字与排版优先的全新文生图任务”，可在重新确认任务类型后单独改评估 `see2ai_text_to_image_uniworld`。

## 能力边界

- ✅ 支持功能：基于参考图生成新图像，兼容旧输入并适配最新 SEE2AI 图片 action 契约。
- ✅ 适用场景：商品主图、场景展示、模特换装、多角度图、参考图延展、风格转换。
- ✅ 默认路由：`backend=auto`。
- ✅ 旧调用兼容：外部仍可传 `image_url / aspect_ratio / resolution / output_format`。
- ✅ 新调用兼容：高级调用方可直接传 `image_urls / size / quality / background / moderation / output_compression / n / user`，这些高级参数会路由到 `alternative`。
- ❌ 不支持：纯文生图、视频生成、复杂排版制图、任何形式的 `UniWorld` 内嵌或隐藏调用。

## 路由规则

1. 默认 `backend=auto`。
2. 如果出现这些 `alternative` 原生参数中的任意一个：`size`、`quality`、`background`、`moderation`、`output_compression`、`n`、`user`，直接走 `alternative`。
3. 如果显式要求 `output_format` 且不是 `auto`，`auto` 会改走 `alternative`，因为最新 `v1` schema 不接受输出格式字段。
4. 如果仅使用旧式参数，且 `aspect_ratio` 属于 `auto / 1:1 / 9:16 / 16:9 / 4:3 / 3:4`，同时没有命中 `v1` 禁用组合，`auto` 会优先走 `v1`，并把图片字段发为 `input_urls`。
5. 如果旧式 `aspect_ratio` 超出 `v1` 支持范围，或命中 `resolution=4K + aspect_ratio=1:1/auto` 这类 `v1` 禁用组合，`auto` 会改走 `alternative`，并把旧参数换算成 `size`，把图片字段发为 `image_input`。
6. 显式指定 `backend=fast` 时，只能传 `image_url(s) + prompt + aspect_ratio + resolution + output_format`，其中 `aspect_ratio` 不能是 `auto`，`resolution` 只能是 `1K/2K`。
7. 显式指定 `backend=v1` 时，只能传 `v1` 支持的字段；显式指定 `backend=alternative` 时，可传 `alternative` 原生字段，也可继续让兼容层把旧参数换算成 `size`。

## 参数表

| 字段 | 必填 | 说明 |
|---|---|---|
| `image_url` | 条件必填 | 单张参考图 URL |
| `image_urls` | 条件必填 | 多张参考图 URL；若存在则优先使用 |
| `prompt` | 是 | 图像编辑/改图提示词 |
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
python skills/see2ai_image_to_image/scripts/image_to_image.py \
  --config '{"image_url": "https://example.com/product.jpg", "prompt": "参考图里的商品，生成电商主图"}'

python skills/see2ai_image_to_image/scripts/image_to_image.py \
  --config '{"image_url": "https://example.com/product.jpg", "prompt": "生成 4K 场景图", "aspect_ratio": "16:9", "resolution": "4K"}'

python skills/see2ai_image_to_image/scripts/image_to_image.py \
  --config '{"image_urls": ["https://example.com/a.jpg", "https://example.com/b.jpg"], "prompt": "融合两张参考图做品牌视觉", "size": "2048x1152", "quality": "high"}'

python skills/see2ai_image_to_image/scripts/image_to_image.py \
  --config '{"image_url": "https://example.com/photo.jpg", "prompt": "快速生成商品场景图", "backend": "fast", "aspect_ratio": "4:5", "resolution": "1K"}'
```

### 传统 CLI 模式（仍然支持）

```bash
python skills/see2ai_image_to_image/scripts/image_to_image.py \
  https://example.com/product.jpg "参考图里的商品，生成电商主图"

python skills/see2ai_image_to_image/scripts/image_to_image.py \
  https://example.com/product.jpg "生成品牌场景图" --aspect_ratio 16:9 --resolution 2K
```

## Guardrails

- 走 `v1` 时，不要传 `size`、`quality`、`background`、`moderation`、`output_format`、`output_compression`、`n`、`user`。
- 走 `v1` 时，参考图字段会自动切到 `input_urls`，不要再把旧的 `image_input` 当成主字段发给后端。
- 走 `v1` 时，只支持 `aspect_ratio = auto / 1:1 / 9:16 / 16:9 / 4:3 / 3:4`，且 `resolution=4K` 不能搭配 `aspect_ratio=1:1` 或 `auto`。
- 走 `fast` 时，参考图字段会自动切到 `image_input`；不要传 `size`、`quality`、`background`、`moderation`、`output_compression`、`n`、`user`；最多 14 张参考图。
- 走 `alternative` 时，参考图字段会自动切到 `image_input`，并且旧的 `aspect_ratio + resolution` 会被换算成 `size`。
- 走 `alternative` 时，最多只支持 14 张参考图；`background="transparent"` 必须直接拒绝，`n` 当前只能为 `1`。

## 输出

标准输出为生成后的图片 URL，每行一个：

```text
https://cdn.see2ai.com/generated/image1.jpg
https://cdn.see2ai.com/generated/image2.jpg
```
