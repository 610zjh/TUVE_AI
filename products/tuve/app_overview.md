---
name: TUVE 应用定位与典型场景 / TUVE Positioning and Typical Scenarios
description: TUVE 是什么、为什么不同于普通剪辑工具、典型场景、与 SEE2AI 的关系——销售首次接触客户必备
type: permanent
retention: permanent
retention_reason: TUVE 对外定位的单点真相；销售/客服/PR 都从这里取材 / Single source of truth for TUVE positioning
---

# TUVE · 应用定位与典型场景 / Positioning and Typical Scenarios

## 1. 我们是什么 / What we are

**TUVE** 是基于 **SEE2AI** 平台能力构建的**对话式短视频创作 Agent**，由**兔展（深圳兔展智能科技有限公司）**提供。
**TUVE** is a **dialogue-driven short-video creation Agent** built on the **SEE2AI** platform, provided by **TUZHAN (Shenzhen Tuzhan Intelligent Technology Co., Ltd.)**.

颠覆传统视频剪辑的智能助理：您只需通过对话框输入需求，TUVE 就能自动帮您撰写脚本、生成分镜图片、合成视频片段，并最终拼接出一部完整的短视频。
A smart assistant that disrupts traditional video editing — describe what you want in chat, and TUVE auto-writes the script, generates storyboard images, synthesizes video clips, and stitches them into a finished short.

入口路径：`/apps/tuve`
Entry: `/apps/tuve`

---

## 2. 为什么需要 TUVE / Why TUVE exists

传统短视频生产链路通常是 / Traditional short-video production pipeline:
1. 找剪辑师写脚本 / Hire an editor to write the script
2. 找设计/拍摄团队产出素材 / Get a design / filming team for assets
3. 剪辑师在剪辑软件里拼接 / Editor stitches in editing software
4. 反复打回修改 / Endless revision rounds
5. 周期一次以"周"计 / Cycle measured in weeks

每一环都需要专业人员、对应工具、对应技能。
Each stage needs a specialist, a tool, and a skillset.

TUVE 把整条链路压缩成 / TUVE compresses the whole chain into:
1. 您在对话框说："给一款新出的咖啡机做个 30 秒推广短视频，强调便携和静音" / You type in chat: "30s promo for a portable, silent coffee machine"
2. TUVE 自动出脚本、出分镜、出片段、拼接成片 / TUVE generates script, storyboard, clips, stitches the final video
3. 您随时通过对话调整任意环节 / You adjust any step via chat
4. 周期以"分钟"计 / Cycle measured in minutes

---

## 3. 核心特性 / Core characteristics

### 3.1 对话即创作 / Chat is the creation tool

不需要学剪辑软件、不需要写指令、不需要懂分镜术语。
No editing-software learning curve, no command syntax, no storyboard jargon.

您说"我想要一支 30 秒的新品推广视频，节奏明快、用日系明亮风格"——TUVE 把它翻译成脚本、分镜、视觉风格指令、视频生成参数。
You say "I want a 30s product launch video, upbeat tempo, bright Japanese style" — TUVE translates that into scripts, storyboards, visual-style instructions, and video-gen parameters.

### 3.2 内置 Agent 运行时 / Built-in Agent runtime

TUVE 内置了 Agent 运行时，支持：
TUVE has a built-in Agent runtime supporting:

- **多步任务执行**：不是"一次问、一次答"，而是 TUVE 会自己拆任务 → 一步步执行 → 把进度汇报给您 / **Multi-step task execution**: not "one question, one answer", but TUVE breaks the task → executes step by step → reports progress
- **用户操作审批**：关键节点（生成视频前的脚本确认、最终拼接前的预览）会暂停等您确认 / **User approval gates**: critical nodes (script confirmation before video gen, preview before final stitching) pause for your sign-off
- **会话记忆管理**：本次对话的偏好、风格、人物设定会一直保留，不需要每条消息都重复 / **Session memory**: preferences / styles / character settings persist through the conversation; no need to repeat each message

---

## 4. 典型场景 / Typical scenarios

### 4.1 场景：自媒体作者每周一支短视频 / Scenario: weekly video for a solo creator

某自媒体每周需要做 1-2 支短视频。过去要自己写脚本、找素材、剪辑——单支耗时半天。
A creator does 1-2 videos a week. Previously: write script + source assets + edit — half a day per video.

用 TUVE：
With TUVE:
- 在对话框告诉 TUVE 本周选题方向（如"本周聊一聊远程办公的 5 个隐形成本"）/ Type the topic in chat
- TUVE 自动出脚本草稿 → 作者通过对话调整语气和侧重点 / TUVE drafts script → creator adjusts tone via chat
- TUVE 生成分镜图 → 作者勾选喜欢的、Prompt 调整不喜欢的 / TUVE generates storyboard → creator approves / adjusts
- TUVE 合成视频片段并拼接 → 作者下载成片 / TUVE synthesizes & stitches → creator downloads

单支耗时从半天降到 30 分钟以内。
Cycle drops from half a day to under 30 minutes.

### 4.2 场景：电商商详页批量短视频 / Scenario: batch product-detail videos

某电商每天上新 50 个 SKU，每个都需要 15 秒商详页短视频。过去外包剪辑团队，单价高、周期长。
An e-commerce daily ships 50 SKUs, each needing a 15s detail-page video. Previously: outsource — expensive and slow.

用 TUVE + TABLE 组合：
With TUVE + TABLE:
- 把 SKU 信息（图片、卖点、规格）整理到 **TABLE**（`/apps/table`）/ Put SKU info (image, selling points, specs) into **TABLE**
- 给 TABLE 的"视频"列绑定 TUVE 生成动作 / Bind a TUVE generation Action to a "video" column
- 一键批量执行 → 50 支短视频自动生成 / One-click batch → 50 videos auto-generated

成本透明、周期从天降到小时。
Cost is transparent; cycle drops from days to hours.

### 4.3 场景：知识付费课程的视频化 / Scenario: video-izing knowledge content

某知识付费团队有大量图文课件，想转换成短视频形式以适配短视频平台分发。
A paid-content team has lots of text-and-image courseware, wanting short-video versions for distribution.

用 TUVE：
With TUVE:
- 把图文章节直接粘贴进对话框 / Paste the chapter into chat
- 让 TUVE 把章节核心观点压缩成 60 秒短视频脚本 / Ask TUVE to compress the core points into a 60s script
- TUVE 配上风格统一的视觉素材和动效 / TUVE provides style-consistent visuals and motion
- 输出成片 → 直接发布到分发平台 / Output → publish

### 4.4 场景：品牌方持续内容生产 / Scenario: brand continuous content production

某中小品牌没有专职视频团队，但希望保持每周 3-5 支社交媒体短视频的节奏。
An SMB brand without a video team wants 3-5 social-media shorts per week.

用 TUVE：
With TUVE:
- 在对话框告诉 TUVE 品牌资产（logo、色彩体系、开场片尾、品牌 voice），TUVE 在创作上下文里长期保留 / Tell TUVE the brand assets (logo, color system, intro/outro, brand voice) in chat — TUVE persists them in the creation context
- 后续每次只需要告诉 TUVE 这一支视频的主题 / Subsequent videos just need the topic
- 品牌资产自动应用 → 视觉一致性自动保证 / Brand assets auto-apply → visual consistency guaranteed
