---
name: TUVE 一页速览 / TUVE 1-page overview
description: TUVE 应用对外速览——是什么、给谁用、5 分钟入门路径、详细材料入口
type: permanent
retention: permanent
retention_reason: TUVE 对外材料的入口；销售/客服/合作伙伴/新人最先看到的页面 / Entry page for TUVE external materials
---

# TUVE · 一页速览 / 1-page overview

> 看完这一页可以完成 / After this page you can:
> - 用 1 句话说清楚 TUVE 是什么 / Describe TUVE in one sentence
> - 知道 4 类典型用户场景 / Know the 4 typical user scenarios
> - 知道下一步去哪份详细材料 / Know which detail file to open next

---

## 一句话定位 / One-line positioning

**TUVE** 是基于 **SEE2AI** 平台能力构建的**对话式短视频创作 Agent**——通过对话让脚本、分镜、素材、成片整条链路自动跑通。由**兔展（深圳兔展智能科技有限公司）**提供。
**TUVE** is a **dialogue-driven short-video creation Agent** built on the **SEE2AI** platform — chat your way through script, storyboard, assets, and final video. Provided by **TUZHAN (Shenzhen Tuzhan Intelligent Technology Co., Ltd.)**.

颠覆传统视频剪辑的智能助理：您只需在对话框输入需求，TUVE 就能自动撰写脚本、生成分镜图片、合成视频片段，并最终拼接出一部完整的短视频。
A smart assistant that disrupts traditional video editing — describe what you want, and TUVE writes the script, generates storyboard images, synthesizes clips, and stitches them into a finished short.

---

## 给谁用 / Who it's for

| 用户画像 / Persona | 用 TUVE 解决的问题 / What TUVE solves |
|---|---|
| 内容创作者 / 自媒体 / Content creators / individual media | 想做短视频但不会剪辑、没素材库、不会写脚本 / Want to make videos but don't know editing, lack assets, can't write scripts |
| 电商商详 / 营销团队 / E-commerce / marketing teams | 每天需要为新品、活动、商详页批量产出短视频 / Daily batch production of product / event / detail-page videos |
| 教育 / 知识付费 / Education / paid content | 把图文知识转换成短视频形式 / Convert text-and-image knowledge into short-video form |
| 中小企业品牌方 / SMB brands | 没有专职视频团队，但需要持续输出品牌内容 / No dedicated video team, but needs continuous brand content |

---

## 5 分钟内能做什么 / What 5 minutes gets you

1. 打开 `/apps/tuve` 进入工作台 / Open `/apps/tuve` to enter the workbench
2. 在对话框输入您想要的视频主题（例如"给一款新出的咖啡机做个 30 秒推广短视频，强调便携和静音"）/ Type your video topic in chat (e.g. "30s promo for a new portable, silent coffee machine")
3. TUVE 自动撰写脚本 → 生成分镜图 → 合成视频片段 → 拼接成片 / TUVE auto-writes script → generates storyboard → synthesizes clips → stitches the final video
4. 您可以在过程中随时**通过对话调整**（"第二个镜头改成俯拍"、"配音换成女声"）/ Adjust **via chat** at any step ("change shot 2 to top-down", "switch VO to female")

详细 SOP / Step-by-step: [`getting_started.md`](getting_started.md)

---

## 与 SEE2AI 的关系 / Relationship with SEE2AI

- **SEE2AI** 是底层多模态能力平台（账号、API、计费、Action、资产托管）/ SEE2AI is the underlying capability platform (accounts, API, billing, Actions, asset hosting)
- **TUVE** 是 SEE2AI 之上的应用层产品，把多个 Action（脚本撰写、文生图、视频生成、视频拼接）**串成完整的"对话 → 成片"工作流** / TUVE is the app-layer product on SEE2AI, chaining multiple Actions (script, text-to-image, video gen, stitching) into a **"chat → finished video" workflow**
- TUVE 的所有调用都通过您的 SEE2AI 租户账户**统一计费**——一份充值，对话生图、生视频、拼接全部覆盖 / All TUVE calls are **unified billing** under your SEE2AI tenant — one recharge covers all interactions

如果您想自己用 SEE2AI Action 搭建类似工作流：见 [`../see2ai/capabilities.md`](../see2ai/capabilities.md) §7「多 Action 编排」。
If you want to build a similar workflow yourself with SEE2AI Actions: see [`../see2ai/capabilities.md`](../see2ai/capabilities.md) §7 "Multi-Action orchestration".

---

## 这一目录的详细材料 / Detail files in this folder

| 文件 / File | 内容 / Content |
|---|---|
| [`app_overview.md`](app_overview.md) | 应用定位、典型场景 / App positioning, typical scenarios |
| [`getting_started.md`](getting_started.md) | 5 分钟做出第一支视频 / Make your first video in 5 minutes |
| [`capabilities.md`](capabilities.md) | Agent 运行时 / 创作上下文 / 媒体引用 / 任务面板 / 典型创作场景 / Agent runtime, Creation Context, Reference Tray, Task Rail, typical scenarios |
| [`support.md`](support.md) | 故障排查、工单 / Troubleshooting, tickets |
| [`openclaw_context/`](openclaw_context/) | 面向内部维护与 AI 协作的 TUVE 运行时上下文包：skill 路由、Agent 契约、配置模板 / Internal runtime context pack for maintenance and AI collaboration |
