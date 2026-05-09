---
name: TUVE 支持与排查 / TUVE Support and Troubleshooting
description: TUVE 工作台打不开、连接断开、生成失败、生成质量等常见问题与排查、工单提交
type: permanent
retention: permanent
retention_reason: 用户使用 TUVE 时遇到问题的标准参考材料 / Standard reference for users encountering TUVE issues
---

# TUVE · 支持与排查 / Support and Troubleshooting

---

## 1. 常见问题排查 / Common issue troubleshooting

### 1.1 TUVE 工作台打不开 / Workbench won't load

**可能原因 / Possible causes**:
- 浏览器版本过旧 / Browser too old
- 未登录 SEE2AI 账号 / Not logged in to SEE2AI
- 网络环境屏蔽 WebSocket / Network blocking WebSocket

**解决 / Solution**:
- 使用最新版 Chrome 或 Edge / Use latest Chrome or Edge
- 先去 `/tenant/login` 完成登录 / Log in at `/tenant/login` first
- 检查公司/学校网络是否屏蔽 WebSocket（部分严格防火墙会拦）/ Check if your network blocks WebSocket (some strict firewalls do)

### 1.2 对话过程中连接断开 / Connection drops mid-chat

**原因 / Cause**: TUVE 使用 WebSocket 进行实时通信，可能因网络波动断开 / TUVE uses WebSocket; network fluctuation can drop it.

**解决 / Solution**:
- 刷新页面即可重新连接 / Refresh to reconnect
- ✅ **历史对话和已完成步骤不会丢失** / **History and completed steps are preserved**
- 如反复断开 → 检查网络环境是否有代理或防火墙限制 WebSocket / If recurrent → check for WebSocket-blocking proxy or firewall

### 1.3 视频生成等了很久 / Video generation taking a long time

**原因 / Cause**: 视频生成是计算密集型任务，单段 4-15 秒视频通常需要数十秒到数分钟 / Compute-heavy; a single 4-15s clip typically takes tens of seconds to minutes.

**解决 / Solution**:
- ✅ **不要刷新页面** —— 切换到其他浏览器 Tab 等待，任务面板会持续显示进度 / ✅ **Don't refresh** — switch to another tab; task rail keeps showing progress
- 如果超过 10 分钟仍无进展 → 提交工单（`/backlog`），附 TUVE 工作台显示的任务 ID / If still nothing after 10 min → file ticket at `/backlog` with the task ID shown in TUVE

### 1.4 视频生成失败 / Video generation failed

**可能原因 / Possible causes**:
- 底层服务临时波动 / Underlying service temporary fluctuation
- 余额不足 / Insufficient balance
- Prompt 触发了内容安全规则 / Prompt triggered content safety rules

**解决 / Solution**:
- ⚠️ **这类失败不会扣除您的费用**——可以放心重试 / **No charge incurred on failure** — retry safely
- 检查 `/tenant/dashboard` 余额 → 不足请充值 / Check balance at `/tenant/dashboard`; recharge if low
- 如果是内容安全拒绝（提示明确）→ 调整 prompt 后重试 / If safety refusal (clear message) → adjust prompt and retry
- 如反复失败 → 提交工单附任务 ID 与具体 prompt / If recurrent → file ticket with task ID and the prompt

### 1.5 生成的视频质量不满意 / Output quality not satisfying

**通常不是"失败"，而是"prompt 信息不够或不够具体"。**
**Usually not a "failure" — usually "prompt is too vague or thin".**

**调整方向 / What to try**:
- 把风格描述得更具体（不只说"日系明亮"，加"参考无印良品的视觉，柔和漫反射光、低饱和、暖色调"）/ Be more concrete about style
- 上传参考素材作为视觉锚点 / Upload reference assets as visual anchors
- 让 TUVE 先出 3 个候选风格，您选最接近的，再让它在那个基础上细化 / Iterate: ask TUVE for 3 candidates, pick closest, then refine
- 把"必须保留的元素"明确写出来（哪几句话必须出现、哪个产品/logo 必须入镜）/ Spell out "must-keep elements" (which lines, which product/logo)

详细 prompt 写法见 [`getting_started.md`](getting_started.md) §3.2。
Full prompt-writing guide: [`getting_started.md`](getting_started.md) §3.2.

### 1.6 余额不够中途被打断 / Ran out mid-task

**原因 / Cause**: TUVE 视频生成会按时长和模型扣费，多支视频或反复迭代会加速消耗 / TUVE video gen charges by duration and model; multi-video iteration accelerates burn.

**解决 / Solution**:
- 充值后回到 TUVE 工作台 → 之前的对话和已生成素材不会丢失，可以继续 / Recharge → return to workbench; prior chat & assets preserved, continue
- 计划连续多轮迭代时建议提前准备较充足的余额，具体金额结合 `/actions` 页面的单价与您的预期调用量评估 / If you plan sustained iteration, recharge a generous balance up front; estimate the right amount from per-call prices on `/actions`
- 详细计费 → [`../see2ai/pricing_and_account.md`](../see2ai/pricing_and_account.md) / Full pricing → [`../see2ai/pricing_and_account.md`](../see2ai/pricing_and_account.md)

### 1.7 TUVE 拒绝执行某些指令 / TUVE refuses certain requests

TUVE 是面向商业级短视频创作的工具，遵守平台内容规范——以下场景会拒绝：
TUVE is built for commercial short-video creation and follows platform content rules. It will refuse:
- 涉及未成年人不当内容 / Inappropriate content involving minors
- 暴力、血腥、明确违法内容 / Violent / gory / explicitly illegal content
- 仿冒已知品牌或公众人物 / Impersonating known brands or public figures
- 政治敏感、宗教煽动、歧视性内容 / Political / religious incitement / discriminatory content

如果您的合理使用场景被误判拒绝 → 通过 `/backlog` 提交工单说明使用场景。
If a legitimate scenario is misjudged → file a ticket at `/backlog` describing the use case.

---

## 2. 提交工单 / Filing a ticket

### 2.1 入口 / Entry points

| 入口 / Entry | 路径 / Path |
|---|---|
| TUVE 工作台内反馈按钮 / TUVE workbench feedback button | TUVE 内 / Within TUVE |
| Backlog 反馈页 / Backlog page | `/backlog` |
| 直接提交 / Direct submit | `/backlog/submit` |

### 2.2 工单类型 / Ticket types

- **Bug 报告** / Bug report：TUVE 报错、连接异常、生成失败 / TUVE errors, connection issues, generation failure
- **功能建议** / Feature request：希望 TUVE 支持的新能力 / Capabilities you'd like TUVE to support
- **一般反馈** / General feedback：使用体验、账单疑问、商务合作 / UX, billing, partnerships

### 2.3 服务承诺 / Service commitment

所有工单（特别是账单类申诉）**24 小时内人工答复**。
**All tickets (especially billing) get human reply within 24 hours**.

平台对有效反馈提供 `cost_points` 奖励——具体奖励数量与每日上限以平台公告与工单页面实时展示为准。
The platform rewards valid feedback with `cost_points` — actual amounts and daily caps are as currently shown in platform announcements and the ticket page.

---

## 3. 商务合作与企业级需求 / Business inquiries & enterprise needs

如果您：
If you:
- 有大规模视频生产需求 / Large-scale video production needs
- 希望企业级合作（独立部署 / SLA / 合同 / 定制化能力）/ Enterprise collaboration (private deploy / SLA / contracts / customization)
- 想接入自己的视觉素材库 / Want to integrate your own asset library
- 有 TUVE 未覆盖的工作流需求，希望共建 / Have workflow needs not yet covered, want to co-build

请通过 `/backlog` 提交**商务合作工单**。
File a **business inquiry** at `/backlog`.

---

## 4. 还想了解什么 / What else

| 想知道 / Want to know | 去哪 / Go to |
|---|---|
| TUVE 是什么、典型场景 / What TUVE is, typical scenarios | [`app_overview.md`](app_overview.md) |
| 怎么做第一支视频 / Make my first video | [`getting_started.md`](getting_started.md) |
| TUVE 全部能力、典型创作场景 / All capabilities, typical scenarios | [`capabilities.md`](capabilities.md) |
| 计费 / 充值 / 账单 / Billing | [`../see2ai/pricing_and_account.md`](../see2ai/pricing_and_account.md) |
| SEE2AI 平台报错排查（401/429/5xx）/ Platform error troubleshooting | [`../see2ai/support.md`](../see2ai/support.md) |
