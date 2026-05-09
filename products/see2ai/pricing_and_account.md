---
name: SEE2AI 计费与账户 / SEE2AI Pricing and Account
description: 平台词元（cost_points）的概念、按量计费机制、扣费时机、失败不扣费、充值与账单查询入口
type: permanent
retention: permanent
retention_reason: 用户使用 SEE2AI 时关于"钱怎么算、怎么充、怎么查"的标准参考 / Standard reference for "how it's billed, how to recharge, how to check"
---

# SEE2AI · 计费与账户 / Pricing and Account

> ⚠️ **本文件只描述计费机制与账户操作流程**。具体的价格、汇率、最低充值金额、可选档位、单次 Action 单价随业务调整随时变化——**所有具体数字以您登录后在平台 `/tenant/recharge` 与各 Action 详情页看到的实时信息为准**。
> ⚠️ **This file describes only the billing mechanism and account operation flow.** Specific prices, FX rates, minimum recharge amounts, available tiers, and per-Action unit prices change with business adjustments — **all concrete numbers are authoritative on the platform's `/tenant/recharge` and per-Action detail pages after login**.

---

## 1. 计费核心理念：按需付费 / Core idea: pay-as-you-go

平台所有服务（文本对话、图像生成、视频生成等）都采用**按量计费**模式。
All services (text chat, image generation, video generation) are billed on a **pay-as-you-go** basis.

您充值的金额完全掌握在自己手中——**只有在您成功调用了某个接口并获得结果时，系统才会从您的账户余额中扣除相应费用**。
Your prepaid balance is yours. **Charges only occur when you successfully invoke an interface and receive a result**.

---

## 2. 平台词元（`cost_points`）：全站统一计费单位 / Platform tokens (`cost_points`): unified unit

为了让您能够**用一个账户使用所有模型和能力**（无论文本对话、图像生成还是视频创作），平台引入了一个统一的内部货币单位：**`cost_points`（平台词元）**。
So you can **use one account across every model and capability** (text / image / video), the platform uses a unified internal unit: **`cost_points` (platform tokens)**.

您可以把 `cost_points` 理解为 SEE2AI 平台内部的"游戏币"或"点券"——所有跨模型、跨能力的消耗都换算成同一种单位，方便统一查询、统一对账。
Think of `cost_points` as platform-internal "tokens" or "credits" — every cross-model, cross-capability charge is converted to the same unit, making queries and reconciliation easy.

> 充值金额 → `cost_points` 的换算汇率，以及不同档位的入账数量，请以 `/tenant/recharge` 页面显示为准。
> The conversion rate from RMB to `cost_points`, and the amounts credited per tier, are as displayed on the `/tenant/recharge` page.

---

## 3. 两种计费模式 / Two billing modes

### 3.1 大模型文本对话（Token 计费）/ LLM text chat (per-token)

调用 LLM 文本接口时，平台按大模型返回的 `usage` 字段进行扣费：
For LLM text endpoints, charges follow the `usage` field returned by the model:

```
本次消耗 = 输入 token 数量 × 输入单价 + 输出 token 数量 × 输出单价
Charge = input_tokens × input_unit_price + output_tokens × output_unit_price
```

> 各模型的输入/输出单价以 SEE2AI 平台 `/actions` 详情页为准。
> Per-model input/output unit prices live on the `/actions` detail pages.

> ⚠️ **流式输出（Stream）必须加 `stream_options={"include_usage": true}`**，否则平台无法统计 token 消耗，可能导致调用异常。
> ⚠️ **Streaming requires `stream_options={"include_usage": true}`**, otherwise the platform can't track token usage and the call may fail.

### 3.2 多模态动作 API / Multimodal Actions

调用生图（如 `see2ai_image_generation_v1`）或生视频动作时，由于底层并非文本 token，平台采取**按次/按规格**计费：
For image (e.g. `see2ai_image_generation_v1`) or video Actions, billing isn't per-token — it's by call or by spec:

- 生图：通常按分辨率档位扣费 / Image: typically by resolution tier
- 生视频：通常按时长和模型扣费 / Video: typically by duration and model

> 具体的 Action 价格表，请在 SEE2AI 平台的 `/actions` 动作详情页查看（实时更新）。
> Per-Action pricing tables live at the `/actions` detail page in the SEE2AI platform (live-updated).

---

## 4. 计费保护机制与扣费时机 / Billing safeguards & timing

### 4.1 扣费链路 / Charging path

所有会产生费用的能力调用都会经过平台统一的计费保护链路。
Every billable call goes through the unified billing safeguard pipeline.

### 4.2 扣费时机 / When charges occur

**只有在调用成功且返回有效结果后，才会发生扣费**。
**Charges only occur after successful return of valid results**.

### 4.3 调用失败不扣费 / No charge on failure

如果由于平台网络波动或底层服务异常导致接口返回 HTTP 5xx 错误，**本次请求绝不扣费**。
If the call returns HTTP 5xx due to platform fluctuation or underlying service issues, **no charge is incurred**.

---

## 5. 余额不足与充值 / Insufficient balance & recharge

### 5.1 余额不足的表现 / Symptom

当您的可用 `cost_points` 余额耗尽，或不足以支付当前请求的预估最低费用时，网关会拒绝请求并返回：
When `cost_points` is depleted (or below the estimated minimum for the current request), the gateway rejects with:

> **HTTP 401 Unauthorized**
> 提示："余额不足，请充值"
> Message: "Insufficient balance, please recharge"

### 5.2 充值流程 / Recharge flow

1. 登录 `/tenant/dashboard` / Log in to `/tenant/dashboard`
2. 点击左侧菜单 "充值与套餐"，路径 `/tenant/recharge` / Click "Recharge & Plans" → `/tenant/recharge`
3. 在该页面选择当前可用的充值金额或自定义金额（具体范围与档位以页面实际展示为准）/ Choose from currently available recharge amounts or a custom value (the actual range and tiers are as shown on the page)
4. 选择当前页面提供的在线支付方式完成付款 / Use one of the online payment channels currently offered on the page
5. 支付成功后返回或刷新页面，`cost_points` 余额自动到账 / After payment, refresh — your balance updates automatically

> 💡 如果您准备**连续生成图片、视频、TUVE 短视频或 UniWorld2.5 图像**，建议提前一次性准备较充足的余额，避免任务中途因余额不足被打断。具体合适的金额请结合 `/actions` 页面的单价、您的预期调用量自行评估，或在 `/tenant/recharge` 页面参考当前提供的档位建议。
> 💡 If you'll be doing **continuous image / video / TUVE / UniWorld2.5 generation**, recharge a generous balance up front to avoid mid-task interruptions. Estimate the right amount based on per-call prices on `/actions` and your expected call volume, or refer to the tier suggestions currently shown on `/tenant/recharge`.

---

## 6. 常见计费疑问 / Common billing questions

### Q1: 为什么我充值后余额显示为一大串数字而不是人民币？/ Why does my balance show as a large number instead of RMB?

**A**: 这是正常的。您看到的数字就是您的 `cost_points`（平台词元）——平台所有能力的统一计费单位。
**A**: That's normal. What you see is `cost_points` (platform tokens) — the unified billing unit across all platform capabilities.

这种设计有助于在微小的 token 消耗中进行高精度扣费，避免产生小数点后的精度丢失。
This design enables high-precision billing on tiny token consumptions, avoiding rounding errors.

> 充值金额与 `cost_points` 的换算关系以 `/tenant/recharge` 页面显示为准。
> The conversion between recharge amount and `cost_points` is as displayed on `/tenant/recharge`.

### Q2: 怎么查我的钱都花在哪里了？/ How do I see where my money went?

**A**: 平台提供高度透明的账单系统：
**A**: The platform provides a fully transparent billing system:

1. 进入 `/tenant/dashboard` / Visit `/tenant/dashboard`
2. 点击 "调用日志" 或 "账单明细"（路径：`/tenant/dashboard#logs` / `/tenant/dashboard#bills`）/ Click "Call logs" or "Bills"
3. 每一笔 API 调用都有精确记录：时间、调用的模型名称、请求消耗的 tokens 数量、最终扣除的 `cost_points` / Each call shows: time, model name, tokens consumed, `cost_points` deducted

也可以通过开发者 API 查询：
You can also query via developer API:

```bash
GET /api/v1/usage    # 按 Action 和时间范围查询用量统计
                     # Usage stats by Action and time range
```

### Q3: 如果我觉得某次扣费不合理怎么办？/ What if a charge looks wrong?

**A**: 请不要着急。
**A**: Don't worry — here's the path:

1. 在 `/tenant/dashboard#logs` 中找到该次调用日志，复制 **Request ID** / Find the call in `/tenant/dashboard#logs`, copy the **Request ID**
2. 通过工单系统（`/backlog`）提交申诉，附上 Request ID 和具体疑问 / File a ticket at `/backlog` with the Request ID and details
3. 人工客服核实后，会立刻为您办理退款（返还 `cost_points`）/ On verification, refund (`cost_points` returned) is issued

我们承诺**所有账单类申诉在 24 小时内给出人工答复**。
We commit to **all billing disputes get a human reply within 24 hours**.

---

## 7. 账户操作 / Account operations

| 操作 / Operation | 入口 / Where |
|---|---|
| 看余额 + API Key / Balance + key | `/tenant/dashboard` |
| 看调用日志 / Call logs | `/tenant/dashboard#logs` |
| 看账单明细 / Bill details | `/tenant/dashboard#bills` |
| 配置 / 可用能力 / Config & skills | `/tenant/dashboard#settings` · `/tenant/dashboard#skills` |
| 修改账户基本信息 / Edit account basics | `/tenant/dashboard#account` |
| 修改手机号等敏感字段 / Sensitive field changes (phone, etc.) | 提交工单 `/backlog` / File ticket at `/backlog` |
| 邀请码 / Invitation codes | `/tenant/dashboard#invitations` |
| 重置 API Key（如怀疑泄露）/ Reset API key (on suspected leak) | `/tenant/dashboard` API Key 管理区域 / API Key Management section |

---

## 8. 反馈奖励机制 / Feedback rewards

平台为有效反馈提供 `cost_points` 奖励——具体奖励数量、每日上限以平台公告与工单页面实时展示为准。
The platform rewards valid feedback with `cost_points` — actual reward amounts and daily caps are as currently shown in platform announcements and the ticket page.

详细工单流程见 [`support.md`](support.md)。
Full ticket flow: [`support.md`](support.md).
