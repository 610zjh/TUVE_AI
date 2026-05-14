---
name: see2ai_seedance_prompt_renderer
description: >
  ⚠️ workflow-only 内部工具，禁止主模型直接调用，也不得作为默认可选 Skill 暴露。
  这不是脚本撰写技能。
  Just-in-time SEE2AI 视频生成提示词渲染器。
  接收 Production Doc 的 shot 叙事字段 + 已填充资产 URL，输出符合 PRD 0023 规范的 SEE2AI 视频生成专属 Prompt。
  当前已提供真实脚本 `scripts/vedio_scriptwriting.py`，默认输出结构化 JSON，也支持输出 Markdown。
  当前仓库中该能力作为保留的内部渲染工具存在，需要由工程侧或上游工作流显式传入 `shot` / `shot_data` 调用。
  运行时注册必须把本 Skill 从主模型默认技能列表移除，只允许 workflow 显式调用。
  Do NOT call directly from the main model — this is an internal rendering utility and not a user-facing skill.
version: 2.0.0
author: TUVE
update: 2026-04-29
action: see2ai_scriptwriting_v1
metadata:
  emoji: "🎛️"
  visibility: internal
  invocation_policy: workflow_only
  user_facing: false
  requires: []
dependency:
  python: []
---

# 📋 能力声明（Capability Declaration）

```yaml
trigger_when: >
  调用方已经准备好 Production Doc 的单个 shot 完整数据（`shot` / `shot_data`），
  需要渲染出符合 Seedance 2.0 规范的专属 Prompt。

do_NOT_trigger_when: >
  - 用户提出"帮我写脚本"、"生成脚本"、"脚本撰写"等需求（脚本职责由主模型承担，参见 PRD 0024 决策一）
  - 主模型直接调用（禁止，主模型只负责叙事层内容，不调用此技能）
  - 用户要求"帮我写视频提示词"（应引导进入完整工作流，不单独调用此技能）
  - 图片槽位未全部 filled 时（缺少输入，无法渲染）

can_do:
  - 读取 shot 的叙事字段（narrative_intent、shot_function、composition_notes 等）
  - 读取已填充的 image_slots、video_slots、audio_slots 及其 URL
  - 按 PRD 0023 Seedance 2.0 提示词规范生成专属 Prompt（纯中文，≤ 800 字）
  - 输出结构化 JSON：`prompt`、`best_entry`、`materials`、`director_tips`、`markdown`
  - 生成配套的素材清单（@图X → [全局：素材名]）
  - 生成核心参数设置（入口选择、生成时长）
  - 检查并强制执行素材编号重置（每个镜头从 @图1 重新开始）
  - 检查素材数量是否超过 Seedance 2.0 单镜头上限（图≤9、视频≤3、音频≤3、总≤12）
  - 输出导演调优指南

cannot_do:
  - 创意策略讨论或脚本内容决策（这是主模型的工作）
  - 独立面向用户提供服务
  - 生成视频
  - 生成图片

known_limitations:
  - 当 shot 缺少关键叙事字段时（如 narrative_intent 为空），渲染质量下降
  - 不能自动检测图片中是否有人脸（如调用方需要，需在渲染前使用 `see2ai_face_detection` 完成检测与参数决策）

fallback_candidates:
  - 若渲染失败，应由调用方回退为人工编写 Prompt，或改为直接使用文字简述
```

---

# see2ai-seedance-prompt-renderer · Just-in-time Seedance 2.0 提示词渲染器

> **定位变更说明（PRD 0024 P3-1）**：本 Skill 已从"brief → Seedance 格式翻译器"重定位为
> "Production Doc shot 字段 → Seedance 2.0 专属 Prompt 渲染器"。
> 原创意策略和脚本内容职责已移交主模型，本 Skill 只做格式渲染。

---

## 输入规范

本 Skill 接受 Production Doc 中单个 shot 的完整数据（由调用方显式组装后传入）：

```yaml
# 叙事字段（由主模型在 scriptwriting 阶段写入）
shot:
  shot_id: 1
  title: "开场：高原水源揭幕"
  duration: 6
  entry_type: "full_reference"           # full_reference | first_last_frame
  narrative_intent: "情绪建立——纯净感和高端调性"
  shot_function: "establishing"
  previous_shot_ref: null
  next_shot_ref: 2
  composition_notes: "大全景，水平线居中，冷色调"
  voiceover_line: "来自4000米高原的馈赠"
  music_direction: "空旷弦乐，情绪平静中带期待"

  # 已填充的资产槽位（由生图技能在 image_generation 阶段填充）
  image_slots:
    - slot_ref: "@图1"
      global_asset_id: "asset_002"
      url: "https://cdn.see2ai.com/yyy.jpg"
      usage_role: "first_frame"
      purpose: "首帧：高原水源全景"
      status: "filled"

  video_slots:
    - slot_ref: "@视频1"
      global_asset_id: "asset_004"
      url: "https://cdn.see2ai.com/ref.mp4"
      usage_role: "motion_ref"
      purpose: "参考慢动作水流运镜节奏"
      status: "filled"

  audio_slots: []

# 全局信息（来自 requirements 和 consistency_anchors）
global_context:
  visual_style: "清冷高级感，蓝白色系"
  aspect_ratio: "9:16"
  duration_target: 30
  consistency_anchors:
    character: null
    product: "asset_001"

# 全局资产注册表（用于 @X → [全局素材名] 映射）
global_assets:
  asset_001:
    global_name: "产品瓶身正面图"
  asset_002:
    global_name: "高原水源航拍图"
  asset_004:
    global_name: "竞品运镜参考视频"
```

---

## 输出规范（严格遵循 PRD 0023 模板）

输出必须包含以下三个部分：

### 1. 核心参数设置

```
【⚙️ 核心参数设置】
- 最佳入口：首尾帧 / 全能参考
  （判断规则：仅有 first_frame + last_frame 图片 → 首尾帧；含视频/音频 → 全能参考）
- 生成时长：X 秒
```

### 2. 本片段素材清单

```
【📂 本片段素材清单】
- 核心必传：@图1 -> [全局：高原水源航拍图]：首帧，全景高原湖泊，jpeg，<30MB
- 可选优化：@视频1 -> [全局：竞品运镜参考视频]：运镜节奏参考，时长 ≤15s，<50MB，480p-720p
```

**重要规则**：
- 每个 shot 的素材编号**从 @图1 重新开始**，绝不跨镜累加
- 全局素材名只在此处出现，Prompt 正文只用 @图1 等编号
- 检查总素材数 ≤ 12，否则输出错误并阻断

### 3. Seedance 2.0 专属 Prompt

```
【🪄 Seedance 2.0 专属 Prompt】
> [纯中文，≤ 800 字，包含：
>  1. 整体视觉风格与光影（来自 visual_style + composition_notes）
>  2. @素材精准引用与用途（仅用 @图X 格式，说明用途）
>  3. 时间轴秒数控制（来自 duration）
>  4. 专业运镜术语（来自 composition_notes）
>  5. 台词与音效（来自 voiceover_line + music_direction）
>  6. 负向排除词（固定结尾：负向排除：画面模糊、人物变形、动作卡顿、场景跳变、光影错乱）
> ]
```

---

## 使用方式

```bash
# 由调用方显式传入 shot / shot_data，默认输出 JSON
python skills/see2ai_seedance_prompt_renderer/scripts/vedio_scriptwriting.py \
  --config '{"shot_data": {...}, "global_context": {...}, "global_assets": {...}}'

# 如需直接查看 Markdown 包，可显式指定 output_format
python skills/see2ai_seedance_prompt_renderer/scripts/vedio_scriptwriting.py \
  --config '{"shot_data": {...}, "global_context": {...}, "global_assets": {...}, "output_format": "markdown"}'
```

> **注意**：当前真实实现只支持 `shot` / `shot_data` 工作流输入，
> 不再支持旧的 `brief -> Prompt` 生产链路。

---

## Seedance 2.0 核心约束（来自 PRD 0023，渲染时必须遵守）

| 约束 | 规则 |
|---|---|
| 素材编号 | 每个镜头从 @图1 重新计算，禁止跨镜累加 |
| 提示词字数 | ≤ 800 字，禁止废话 |
| 图片上限 | ≤ 9 张，单张 < 30MB |
| 视频上限 | ≤ 3 个，2-15s，< 50MB |
| 音频上限 | ≤ 3 个，总时长 ≤ 15s，< 15MB |
| 总素材上限 | ≤ 12 个 |
| 语言 | 纯中文（保留外文专有名词） |
| 台词格式 | `角色开口说话："台词原文"` |
| 负向排除 | 每个 Prompt 末尾必须附加 |
| 入口选择 | 首尾帧：仅 first_frame+last_frame；全能参考：含视频/音频时 |

---

## 错误处理

| 错误情况 | 处理方式 |
|---|---|
| image_slots 中有 `status: "pending"` | 阻断，返回错误：哪个槽位未填充 |
| 素材总数 > 12 | 阻断，返回错误：建议主模型拆分镜头 |
| `narrative_intent` 为空 | 警告并降级：使用 `title` 和 `shot_function` 推断 |
| 未设置 SEE2AI_API_KEY | 提示设置环境变量 |
