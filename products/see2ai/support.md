---
name: SEE2AI 支持与排查 / SEE2AI Support and Troubleshooting
description: 常见报错排查（401/429/5xx）、特殊场景排查、工单提交、API Key 安全提示
type: permanent
retention: permanent
retention_reason: 用户使用过程中遇到问题时的标准参考材料 / Standard reference for users encountering issues
---

# SEE2AI · 支持与排查 / Support and Troubleshooting

---

## 1. 常见报错排查 / Common error troubleshooting

平台为您提供清晰的 HTTP 状态码和详细的错误信息（`error.message`）。以下是最常见问题及解决步骤。
The platform provides clear HTTP status codes and detailed error messages. Below are the most common problems and resolutions.

### 1.1 HTTP 401 Unauthorized（身份验证失败 / 余额不足）/ Auth failure or insufficient balance

**可能原因 1：API Key 错误或未携带** / Possible cause 1: bad or missing API key:
- 检查请求 Header 是否包含 `Authorization: Bearer sk-...` / Check the header
- 检查 `sk-` 前缀是否完整复制，是否混入空格或换行符 / Check `sk-` prefix is complete, no whitespace contamination
- ⚠️ API Key 必须放在 Header 中，**不可作为 URL 参数传递** / Header only, **never as a URL param**

**可能原因 2：账户余额不足** / Possible cause 2: insufficient balance:
- 平台计费网关在每次请求前都会预扣费检查。可用 `cost_points` 耗尽 → 请求被拦截 / Pre-charge check on every request; depleted balance → blocked
- 解决：登录 `/tenant/dashboard` 查看余额；为 0 或负数 → 前往 `/tenant/recharge` 充值（具体金额范围以页面展示为准）/ Solution: check balance at `/tenant/dashboard`; recharge at `/tenant/recharge` (range as shown on the page)

**可能原因 3：Key 被封禁或重置** / Possible cause 3: key revoked or reset:
- 如果您在后台重置了 API Key，旧 Key 立即失效，请更新代码 / If you reset the key in the dashboard, the old one is invalidated immediately — update your code

### 1.2 HTTP 429 Too Many Requests（请求过于频繁）/ Rate limited

**可能原因 1：并发超限** / Concurrency limit exceeded:
- 平台对每个租户设置了基础并发限制（Rate Limit）/ Each tenant has a base rate limit
- 不同接口的并发可能不同 / Limits vary by endpoint
- 解决：在代码中加重试机制（Retry-After 头）或降低并发发包速度 / Solution: implement retry-with-backoff or slow down

**可能原因 2：恶意刷量防护触发** / Anti-abuse protection:
- 系统检测到短时间内大量异常请求 → 防火墙临时封禁 IP 或 Key / Rapid abnormal request bursts → temporary IP/key block
- 解决：暂停发送请求稍后再试 / Solution: pause and retry later

### 1.3 HTTP 5xx Server Error / 5xx errors

**可能原因 1：底层服务网络波动** / Underlying service fluctuation:
- 极少数情况下底层服务出现临时波动 → 可能返回 502 Bad Gateway / Rare underlying service fluctuation → 502 Bad Gateway
- ⚠️ **这类错误不会扣除您的任何费用** / **No charges are incurred**
- 解决：等待 1-2 分钟后重试 / Wait 1-2 min, retry

**可能原因 2：平台底座升级维护** / Platform maintenance:
- 503 Service Unavailable → 网关或动作服务正在热更新，通常几秒内恢复 / Hot update in progress, usually recovers in seconds

---

## 2. 特殊场景排查 / Special-scenario troubleshooting

### 2.1 流式输出突然中断或报 0 token / Streaming cuts off or reports 0 tokens

**现象**：调用 Chat Completions，开启 `stream: true`，最后一次返回的数据块报错，或后台日志显示消耗 0 token / Symptom: with `stream: true`, the final chunk errors or backend logs show 0 tokens

**解决**：在请求 JSON 中加上：
**Solution**: add to request JSON:

```json
"stream_options": {
  "include_usage": true
}
```

### 2.2 图像生成参数错误 / Image generation param errors

**现象**：调用 `see2ai_image_generation_v1` 返回参数错误 / Symptom: `see2ai_image_generation_v1` returns param errors

**解决**：
- 严格对照 `/actions` 详情页的参数说明 / Strictly match the `/actions` detail page
- `aspect_ratio` 支持值：1:1, 1:4, 1:8, 2:3, 3:2, 3:4, 4:1, 4:3, 4:5, 5:4, 8:1, 9:16, 16:9, 21:9
- `resolution` 支持值：1k, 2k, 4k

### 2.3 视频生成超时或失败 / Video generation timeout / failure

**解决**：
- HTTP 客户端超时设置 ≥ 300 秒 / HTTP timeout ≥ 300s
- 默认 `sync: true` → 接口阻塞等待生成完成 / `sync: true` default — blocks until done
- 持续失败 → 稍后重试或切换到另一个视频生成 Action / Persistent failures → retry later or switch Action

### 2.4 TUVE 应用连接中断 / TUVE connection drops

**解决**：
- 刷新页面重新连接，**历史对话和任务进度不丢失** / Refresh page; **history and task progress preserved**
- 反复断开 → 检查网络环境是否有代理或防火墙限制 WebSocket / Repeated drops → check for proxy/firewall blocking WebSocket
- 浏览器版本建议为最新版（推荐 Chrome / Edge）/ Use latest browser (Chrome / Edge recommended)

### 2.5 TABLE 应用 Action 执行失败 / TABLE Action execution fails

**解决**：
- 检查该行作为 Action 输入的列是否填写完整 / Verify input columns are filled
- 检查租户后台余额 / Check balance
- 如果是 Agent 列（多步任务），确认 prompt 模板中的变量名 `{{列ID}}` 与实际列 ID 匹配 / For Agent columns, ensure `{{column_id}}` matches actual column IDs

---

## 3. 仍然无法解决：提交工单 / Still stuck: file a ticket

请记录出错时的：
Record the following:
- **时间点**（精确到分钟）/ **Time** (to the minute)
- **请求的参数（Body）** / **Request body**
- **完整的报错信息** / **Full error message**

然后通过以下入口提交：
Then submit via:

| 入口 / Entry | 路径 / Path |
|---|---|
| Backlog 反馈页 / Backlog page | `/backlog` |
| 直接提交 / Direct submit | `/backlog/submit` |

### 3.1 工单类型 / Ticket types

- **Bug 报告** / Bug report：接口报错、功能异常、页面问题 / API errors, feature issues, page problems
- **功能建议** / Feature request：新功能需求或改进建议 / New features or improvements
- **一般反馈** / General feedback：使用体验、账单疑问、商务合作 / UX, billing, partnerships

### 3.2 服务承诺 / Service commitment

所有工单（特别是账单类申诉）**24 小时内人工答复**。
**All tickets (especially billing disputes) get a human reply within 24 hours**.

### 3.3 反馈奖励 / Feedback reward

- **每次有效反馈奖励**：1,000 平台词元 / Per valid feedback: 1,000 platform tokens
- **每日上限**：10 次（UTC 0 点重置）/ Daily cap: 10 (UTC midnight reset)

---

## 4. API Key 安全提示 / API Key security tips

API Key 是您账户内 `cost_points`（余额）的唯一提取凭证。
The API key is the sole credential for accessing your `cost_points` balance.

❌ **不要这么做 / Don't**:
- 把 API Key 以明文形式硬编码在前端代码（Vue/React）或客户端 App 中——前端被抓包反编译可能导致余额被盗刷 / Hardcode in front-end (Vue/React) or client apps — traffic intercept / decompile can drain balance
- 提交到公开代码仓库（GitHub）/ Commit to public repos (GitHub)
- 分享给非授权同事 / Share with unauthorized colleagues

✅ **这么做 / Do**:
- 始终在您的**后端服务器（Server-side）** 发起对 SEE2AI 的调用 / Always call SEE2AI from your **server-side**
- API Key 存放于环境变量或密钥管理服务中 / Store the key in env vars or a secrets manager
- 一旦怀疑泄露 → 立即在 `/tenant/dashboard` 重置 → 旧 Key 立即失效 / On suspected leak → reset at `/tenant/dashboard` → old key invalidated immediately

---

## 5. 速率限制 / Rate limiting

所有 API 接口都部署了基于 IP 和租户维度的速率限制。
All API endpoints have IP- and tenant-based rate limits.

如遇 429 → 实现重试机制或降低并发发包速度。
On 429 → implement retry-with-backoff or reduce concurrency.

---

## 6. 商务合作与企业级需求 / Business inquiries & enterprise needs

如果您：
If you:
- 有大规模调用需求 / Have large-scale calling needs
- 希望企业级合作（独立部署 / SLA / 合同）/ Want enterprise collaboration (private deploy / SLA / contracts)
- 有平台未覆盖的能力需求，希望共建 / Have capability needs not yet covered, want to co-build

请通过 `/backlog` 提交**商务合作工单**。
File a **business inquiry** at `/backlog`.
