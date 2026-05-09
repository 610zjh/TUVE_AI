---
name: SEE2AI 平台定位与核心价值 / SEE2AI Platform Positioning and Core Value
description: SEE2AI 是什么、为什么不是普通的 LLM API、与兔展/TUVE/UniWorld2.5/TABLE 的关系——销售首次接触客户必备
type: permanent
retention: permanent
retention_reason: 公司对外定位的单点真相；销售/客服/合作 PR 都从这里取材 / Single source of truth for external positioning
---

# SEE2AI · 平台定位与核心价值 / Platform Positioning and Core Value

## 1. 我们是谁 / Who we are

**SEE2AI（See to AI）** 是一个专为赋能 AI Agent 与企业客户而设计的 **B2B（企业级）多模态能力平台**，由**兔展（深圳兔展智能科技有限公司）**提供。
**SEE2AI (See to AI)** is a **B2B multimodal capability platform** designed to empower AI Agents and enterprise customers, provided by **TUZHAN (Shenzhen Tuzhan Intelligent Technology Co., Ltd.)**.

---

## 2. 为什么需要 SEE2AI / Why SEE2AI exists

市面上有很多大模型平台，大多数只提供"聊天"功能（Chat）——您问一句，模型答一句。然而在真实业务场景中，仅仅聊天远远不够：
Most platforms today only provide chat — you ask, the model answers. In real business, that's not enough:

- 您希望 Agent 能**生成视频**，而不是只描述视频该长什么样 / You want the Agent to **generate the video**, not just describe what it would look like
- 您希望 Agent 能**做出图像**，而不是只解释图像该怎么做 / You want the Agent to **produce the image**, not just explain how
- 您希望 Agent 能**解析复杂文档**，而不是只告诉您"PDF 里大概有哪些章节" / You want the Agent to **parse complex documents**, not just summarize "what sections likely exist"

因此，SEE2AI 提出了一个核心理念：**Beyond Chat, Agents That Act（超越对话，让 Agent 真正干活）**。
Hence the core idea: **Beyond Chat, Agents That Act**.

---

## 3. 我们怎么做到 / How we do it

我们把各种复杂的业务能力封装成**标准化、开箱即用的"原子 API"（Actions）**。
We encapsulate complex business capabilities into **standardized, out-of-the-box atomic APIs (Actions)**.

无论您的系统使用什么语言开发，都可以通过 HTTP 调用以下能力：
Whatever language you use, you can call these capabilities via HTTP:

- **大语言模型与深度思考** / Large language models & deep reasoning
- **多模态图像生成与处理** / Multimodal image generation & processing
- **视频创作与处理** / Video creation & processing
- **专业文档解析** / Professional document parsing
- **云存储与文件处理** / Cloud storage & file handling
- **场景化能力封装**（爆款脚本撰写、视频拼接等）/ Scenario-specific capability packaging (script writing, video stitching, etc.)

详细能力清单见 [`capabilities.md`](capabilities.md)。
Full capability list: [`capabilities.md`](capabilities.md).

---

## 4. 三大核心价值 / Three core value props

### 4.1 极简接入，一步到位 / Frictionless onboarding

我们将繁杂的参数配置、异步轮询、环境依赖等全部抹平。比如生成一个视频，您只需调用一个标准化 Action 接口，后续的进度轮询与状态回调均由平台底座为您处理。
We flatten complex parameter setup, async polling, environment dependencies. To generate a video: call one standardized Action. The platform handles polling and callback state for you.

### 4.2 标准接口，无缝迁移 / Standard interface, seamless migration

我们提供标准化的 `/api/v1/chat/completions` 接口。如果您原本使用通用对话 SDK，**只需要将 `base_url` 改为我们的地址、`api_key` 换成我们的租户 Key，就能立刻享用我们平台的能力**。
We provide a standard `/api/v1/chat/completions` interface. If you already use a common chat SDK, **just change `base_url` to ours and swap `api_key` for your tenant key — you're in**.

### 4.3 统一计费与精细化管理 / Unified billing & fine-grained ops

无论是哪个模型、是生图还是生视频，所有消费都在一个统一的租户账户内进行扣费与管理（基于平台词元 `cost_points`）。您可以在 `/tenant/dashboard` 清晰地查看每一笔调用日志与消耗，彻底告别"多个平台来回充值对账"的痛苦。
Every model, every image, every video — all billed in one tenant account using platform tokens (`cost_points`). View per-call logs and consumption at `/tenant/dashboard`, no more cross-platform reconciliation pain.

---

## 5. 兔展 · SEE2AI · TUVE · UniWorld2.5 · TABLE 的关系 / How TUZHAN, SEE2AI, TUVE, UniWorld2.5, and TABLE relate

| 名称 / Name | 角色 / Role |
|---|---|
| **兔展（深圳兔展智能科技有限公司）** | 产品与服务的提供方 / Provider |
| **SEE2AI** | 面向 AI Agent 与企业客户的统一多模态能力平台，负责账号、API、计费、Action、资产托管和调用闭环 / Platform layer (accounts, API, billing, Actions, asset hosting, end-to-end loop) |
| **TUVE** | 基于 SEE2AI 能力构建的对话式短视频创作 Agent / Dialogue-driven short-video creation Agent built on SEE2AI |
| **UniWorld2.5** | 兔展旗下的高质量图像创作能力，由 SEE2AI 以标准化 Action 形式承接给用户使用 / TUZHAN's high-quality image capability, exposed via SEE2AI Actions |
| **TABLE** | 基于 SEE2AI 的多维表格智能助手 / Multi-dimensional intelligent spreadsheet on SEE2AI |

---

## 6. 典型客户场景 / Typical customer scenarios

### 6.1 场景：给现有 AI 应用接入"能干活"的能力 / Scenario: add "do-things" power to an existing AI app

某客户原本基于通用对话 SDK 做了一个文案助手，希望升级成"既能写又能配图的 Agent"。
A customer built a copywriting assistant on a common chat SDK and wants to upgrade to "writes and illustrates".

接入 SEE2AI 后：
After SEE2AI:
- 文案部分 `base_url` 改一行 / 升级 `model` 字段，无需重写业务代码 / One-line `base_url` change for copy
- 配图能力通过 `/api/v1/actions/see2ai_image_generation_v1` 调用，作为 Tool 注册给 Agent / Image gen via Action endpoint, registered as a Tool
- 计费统一在 SEE2AI 租户账户，财务一份发票 / Unified billing in the SEE2AI tenant, one invoice

### 6.2 场景：内容团队批量生产素材 / Scenario: batch content production

某客户每天需要为电商商详页生成 50 张高清主图 + 10 个短视频。
A customer needs 50 high-res hero images + 10 short videos daily for product pages.

无需写代码：直接登录 SEE2AI 之上的 **TUVE** 创作短视频，**TABLE** 批量出图，单条素材成本透明可查。
No code: use **TUVE** for video, **TABLE** for image batches. Per-asset cost is fully transparent.

### 6.3 场景：企业内部 Agent 平台 / Scenario: enterprise internal Agent platform

某客户内部多个团队各自开发 AI 应用，希望统一调用底座 + 统一审计 + 单点付费。
Multiple internal teams building AI apps, wanting unified backbone + audit + single billing.

接入 SEE2AI：每个团队拿一个子租户 Key，所有调用日志和消耗都在统一管理台 / 单据，IT 审计无盲区。
SEE2AI: each team gets a sub-tenant key, all calls and consumption land in a unified dashboard, full IT audit visibility.
