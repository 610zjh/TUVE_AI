---
name: TUVE 能力详解 / TUVE Capabilities Detail
description: TUVE 提供的对话式短视频创作能力——Agent 运行时、创作上下文、媒体引用、典型工作流场景
type: permanent
retention: permanent
retention_reason: 客户/技术评估在评估"TUVE 能不能覆盖业务需求"时的对照表 / Capability coverage reference for TUVE evaluations
---

# TUVE · 能力详解 / Capabilities Detail

> 这一份给"已经初步上手 TUVE，想了解能力边界、典型工作流场景、与 SEE2AI 其他能力如何组合"的用户。
> For users past the basics, wanting to understand the capability surface, typical workflow scenarios, and how to combine with other SEE2AI capabilities.

---

## 1. 使用方式：对话驱动 / Usage: dialogue-driven

TUVE 的使用方式是**自然语言对话**——用日常中文/英文描述需求，无需学指令语法、剪辑术语、参数模板。
TUVE is used via **natural-language dialogue** — describe in everyday CN/EN, no commands, jargon, or templates to learn.

入口：`/apps/tuve`
Entry: `/apps/tuve`

---

## 2. 内置 Agent 运行时 / Built-in Agent runtime

不是"一次问、一次答"，而是 TUVE 自己拆任务、按步骤执行、汇报进度：
Not "one question, one answer" — TUVE breaks the task, executes step by step, reports progress:

- **多步任务编排**：脚本 → 分镜 → 视频片段 → 拼接 → 调整，一条对话内完成 / **Multi-step orchestration**: script → storyboard → clips → stitch → adjust, all in one conversation
- **用户操作审批**：关键节点（脚本确认、最终拼接前预览）自动暂停等您确认 / **User approval gates**: critical nodes auto-pause for your sign-off
- **会话记忆**：偏好、风格、人物设定、品牌资产在对话内长期保留 / **Session memory**: preferences, styles, character settings, brand assets persist throughout the session

---

## 3. 创作上下文（Creation Context）/ Creation Context

TUVE 维护一个"本次创作上下文"，包括：
TUVE maintains a "current creation context" including:
- 您之前给的脚本指令、风格偏好 / Your prior script directives and style preferences
- 已生成的素材（脚本、分镜、片段、成片）/ Generated assets (scripts, storyboards, clips, finished videos)
- 您手动上传的参考素材 / Reference assets you've manually uploaded

这意味着您不需要每条消息都重复"我要日系明亮风格"——TUVE 一直记得。
This means you don't need to repeat "I want bright Japanese style" each message — TUVE remembers.

---

## 4. 媒体引用区（Reference Tray）/ Reference Tray

工作台右侧的媒体引用区显示当前对话中所有相关素材：
The reference tray (right side of workbench) shows every asset relevant to the current conversation:
- 您上传的参考图 / 参考视频 / Your uploaded references
- TUVE 生成的中间产物（脚本、分镜图、视频片段）/ TUVE's intermediate products
- 最终成片 / Finished videos

每个素材都可以单独下载、单独编辑、单独引用到下一轮对话。
Each asset can be downloaded, edited, or referenced into the next round individually.

---

## 5. 任务面板（Task Rail）/ Task Rail

工作台右侧的任务面板实时显示当前执行的任务进度：
The task rail (right side) shows live progress of currently executing tasks:
- 哪一步在跑 / Which step is running
- 预计剩余时间 / ETA
- 已完成 / 待执行的子任务列表 / Completed / pending subtasks

任务过程中可以切换到其他对话，回来时进度自动同步。
You can switch to other conversations during execution; progress syncs back automatically.

---

## 6. 输出能力清单 / Output capabilities

| 输出类型 / Output | 说明 / Notes |
|---|---|
| **视频脚本** / Video script | 含分段、镜头描述、配音文案、节奏建议 / Includes segments, shot descriptions, VO copy, pacing suggestions |
| **分镜图** / Storyboard images | 单张高清图，可指定比例（含 16:9 / 9:16 / 1:1 等 14 种）和分辨率（1K/2K/4K）/ Single hi-res images, 14 aspect ratios + 1K/2K/4K resolutions |
| **视频片段** / Video clips | 单段 4-15 秒、720p/480p、可指定首帧/尾帧 / Single clip 4-15s, 720p/480p, first/last frame controllable |
| **完整成片** / Finished video | 多段拼接而成、可加配音 / Stitched multi-clip, optional VO |
| **可下载格式** / Downloadable formats | 标准 MP4，可在主流播放器和分发平台直接使用 / Standard MP4, ready for all major players and distribution platforms |

---

## 7. 典型创作场景 / Typical creation scenarios

### 7.1 自媒体周更 / Solo creator weekly update

> 「主题输入 → TUVE 出脚本草稿 → 您审定 → TUVE 生成分镜 → TUVE 合成视频片段 → TUVE 拼接成片 → 您下载」
> Topic → TUVE drafts script → you approve → TUVE generates storyboard → TUVE synthesizes clips → TUVE stitches → you download.

### 7.2 电商商详视频 / E-commerce detail video

> 「SKU 信息（图+卖点+规格）→ TUVE 强化产品视觉 → 出 15 秒脚本（突出 3 个卖点）→ 视频生成（带 logo 文字）→ 输出 MP4」
> SKU info (image + selling points + specs) → TUVE enhances product visual → 15s script (3 selling points) → video gen (with logo text) → MP4.

### 7.3 知识付费课程视频化 / Knowledge content video-ization

> 「图文章节粘贴 → TUVE 压缩成 60 秒脚本（保留 3 个核心观点）→ 配套视觉 → 视频生成 → 拼接成片」
> Paste chapter → TUVE compresses to 60s script (3 core points) → matching visuals → video gen → stitch.

### 7.4 品牌方持续内容 / Brand continuous content

> 「品牌资产（logo + 色彩 + 字体）+ 本次主题 → TUVE 应用品牌 voice 出脚本 → 强制品牌色出图 → 视频生成 → 拼上品牌片头/片尾」
> Brand assets (logo + palette + font) + topic → TUVE applies brand voice → enforces brand color → video gen → stitches with brand intro/outro.

### 7.5 多语言版本一次产出 / Multi-language one-shot

> 「中文脚本 → TUVE 翻译节点（中→英→日→西）→ 同一画面 + 不同字幕和配音 → 并行输出多个版本」
> Chinese script → TUVE translates (CN→EN→JA→ES) → same visuals + different subs/VO → multiple versions in parallel.

---

## 8. 与 SEE2AI 其他能力的组合 / Combining with other SEE2AI capabilities

TUVE 之外，SEE2AI 还有 TABLE、UniWorld2.5 等。常见组合：
Beyond TUVE, SEE2AI also has TABLE, UniWorld2.5, etc. Common combinations:

### 8.1 TUVE + TABLE：批量生产 / Batch production

- TABLE 里准备一个表，每行是一个待生成视频的素材（标题、主题、标签）/ Prepare a table where each row is a video to generate (title, topic, tags)
- 给"视频"列绑定 TUVE 生成动作 / Bind a TUVE Action to a "video" column
- 一键批量执行 / One-click batch
- 适合每天 50+ SKU 短视频、批量节日营销视频等场景 / For 50+ daily SKUs, holiday batch marketing, etc.

### 8.2 TUVE + UniWorld2.5：高质量分镜 / Premium storyboards

- TUVE 默认的分镜图已经能覆盖大部分场景 / TUVE's default storyboard handles most scenarios
- 如果您的场景需要**更高质量、更复杂构图**的分镜 → 在 TUVE 对话里说"分镜请用 UniWorld2.5 生成" / If you need **higher quality, more complex composition** storyboards → say "use UniWorld2.5 for storyboards" in TUVE chat
- TUVE 自动调用 UniWorld2.5 的 SEE2AI Action 出图 / TUVE auto-invokes the UniWorld2.5 SEE2AI Action

---

## 9. 数据与隐私 / Data and privacy

- 您在 TUVE 内的素材、对话、生成产物，**仅在您的租户账号下可见** / Your assets / chats / outputs are **visible only under your tenant**
- 上传的参考素材会在 SEE2AI 云存储以您账号下私有路径保存，外部无法访问 / Uploaded references are stored in SEE2AI cloud under your tenant's private path; not externally accessible
- 生成的成片可以下载到本地后从 TUVE 删除，平台不会无故保留 / Finished videos can be downloaded then deleted from TUVE; the platform doesn't retain unnecessarily

更详细的数据安全说明请通过 `/backlog` 提交"商务合作"工单咨询。
For more detailed data security inquiries, file a "business inquiry" ticket at `/backlog`.

---

## 10. 还想了解什么 / What else

| 想知道 / Want to know | 去哪 / Go to |
|---|---|
| 怎么开始做第一支视频 / How to make my first video | [`getting_started.md`](getting_started.md) |
| 出问题 / 工单 / Issues / tickets | [`support.md`](support.md) |
| TUVE 是什么、典型场景 / What TUVE is, typical scenarios | [`app_overview.md`](app_overview.md) |
| 计费 / 充值 / 账单 / Billing | [`../see2ai/pricing_and_account.md`](../see2ai/pricing_and_account.md) |
