---
name: SEE2AI 一页速览 / SEE2AI 1-page overview
description: SEE2AI 平台对外速览——是什么、给谁用、怎么开始、收费逻辑、详细材料入口
type: permanent
retention: permanent
retention_reason: 对外产品材料的入口；客户/合作伙伴/新人最先看到的页面 / Entry page for external product materials
---

# SEE2AI · 一页速览 / 1-page overview

> 看完这一页可以完成 / After this page you can:
> - 用 1 句话说清楚 SEE2AI 是什么 / Describe SEE2AI in one sentence
> - 知道 4 类典型用户场景 / Know the 4 typical user scenarios
> - 知道下一步去哪份详细材料 / Know which detail file to open next

---

## 一句话定位 / One-line positioning

**SEE2AI（See to AI）** 是面向 AI Agent 与企业客户的多模态能力平台，由**兔展（深圳兔展智能科技有限公司）**提供。
**SEE2AI (See to AI)** is a multimodal capability platform for AI Agents and enterprise customers, provided by **TUZHAN (Shenzhen Tuzhan Intelligent Technology Co., Ltd.)**.

核心理念：**Beyond Chat, Agents That Act（超越对话，让 Agent 真正干活）**。
Core idea: **Beyond Chat, Agents That Act**.

---

## 给谁用 / Who it's for

| 用户画像 / Persona | 用 SEE2AI 解决的问题 / What SEE2AI solves |
|---|---|
| AI 应用开发者 / AI app developer | 想给自己的 AI 应用接入"图像生成 / 视频生成 / 文档解析"等多模态能力，但不想为每个能力单独对接、单独鉴权、单独充值 / Wants to add image / video / doc capabilities to their AI app without integrating, authenticating, and recharging each one separately |
| Agent 框架使用者 / Agent framework user | 在主流 Agent 编排框架里给 Agent 注册"能干活的工具"——SEE2AI 的 Action 直接是 HTTP 接口，注册成 Tool 即可 / Wants Tools registered in mainstream Agent orchestration frameworks — SEE2AI Actions are straight HTTP endpoints, drop-in as Tools |
| 企业内部 AI 团队 / Enterprise AI team | 公司有内部 AI 应用，希望统一对接一个平台、统一计费、统一审计 / Company-internal AI apps need a single platform, unified billing, unified audit |
| 创意 / 内容团队 / Creative & content teams | 不写代码，直接用 SEE2AI 之上的 **TUVE / TABLE / UniWorld2.5** 应用完成短视频创作、批量出图、表格批量任务 / Doesn't code; uses TUVE / TABLE / UniWorld2.5 directly for video creation, batch image generation, table-driven batch tasks |

---

## 5 分钟内能跑起来 / 5 minutes to first call

1. 注册租户账号（手机号 + 密码）/ Sign up (phone + password)
2. 在租户后台拿到 `sk-` 开头的 API Key / Get an `sk-` API key from the tenant dashboard
3. 充值（具体金额范围以 `/tenant/recharge` 页面为准）/ Recharge (range as shown on `/tenant/recharge`)
4. 用通用对话 SDK 改一个 `base_url`，立刻发起首次调用 / Change one `base_url` in any chat SDK and make your first call

详细 SOP / Step-by-step: [`getting_started.md`](getting_started.md)

---

## 平台之上的应用生态 / Apps on top of the platform

如果不想自己写代码，**直接用现成应用**：
If you don't want to code, **use the apps directly**:

| 应用 / App | 一句话 / One-liner | 入口 / URL path |
|---|---|---|
| **TUVE** | 对话式短视频创作 Agent / Dialogue-driven short-video creation Agent | `/apps/tuve`（详见 [`../tuve/`](../tuve/)）|
| **TABLE** | 多维表格智能助手，可为列绑定 Action 进行批量自动执行 / Multi-dimensional spreadsheet that binds Actions to columns for batch automation | `/apps/table` |
| **UniWorld2.5** | 高质量图像创作能力，由 SEE2AI 以标准化 Action 方式承接 / High-quality image creation, exposed as standardized Actions on SEE2AI | 通过 SEE2AI Action 调用 / Via SEE2AI Action |

---

## 这一目录的详细材料 / Detail files in this folder

| 文件 / File | 内容 / Content |
|---|---|
| [`platform_overview.md`](platform_overview.md) | 平台定位与核心价值 / Platform positioning and core value |
| [`getting_started.md`](getting_started.md) | 5 分钟跑通首次调用 / First call in 5 minutes |
| [`capabilities.md`](capabilities.md) | 平台能力目录 / Capability catalog |
| [`pricing_and_account.md`](pricing_and_account.md) | 计费规则与账户操作 / Pricing rules and account operations |
| [`support.md`](support.md) | 故障排查、工单、安全提示 / Troubleshooting, tickets, security tips |
