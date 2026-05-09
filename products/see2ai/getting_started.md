---
name: SEE2AI 新手接入指南 / SEE2AI Getting Started
description: 5 分钟跑通首次调用——注册、API Key、充值、首次调用四步走 SOP，配 Python/cURL 示例
type: permanent
retention: permanent
retention_reason: 客户首次接入 SOP；销售/客户成功最常分享的页面 / SOP for first integration; most-shared page
---

# SEE2AI · 新手接入指南 / Getting Started

> 这一份给"准备第一次接入 SEE2AI 的客户/合作伙伴"。语气鼓励、步骤具体，目标是 **5 分钟内完成首次调用**。
> For customers / partners doing their first SEE2AI integration. Tone: encouraging, concrete steps. Goal: **first call within 5 minutes**.

---

## 欢迎来到 SEE2AI / Welcome

无论您是资深开发者还是刚接触 API 的新人，通过我们标准化的"四步走"流程，您都能在 **5 分钟内** 完成首次调用。
Whether you're a seasoned developer or new to APIs, the standardized "four-step" flow gets you to a first call in **5 minutes**.

---

## 第一步：注册并登录租户后台 / Step 1 — Register and log in

所有操作都从一个有效的租户账号开始 / Everything starts with a tenant account.

1. 访问租户登录页：`/tenant/login`（请把 `/` 替换为您实际访问的平台域名前缀）/ Visit `/tenant/login` (prefix with your environment's domain)
2. 已有账号 → **手机号 + 密码**或手机号验证码登录 / Have an account → log in with phone + password (or SMS code)
3. 没有账号 → 访问 `/tenant/register` 注册；如果当前环境需要人工开通，请通过 `/backlog` 提交开通申请 / No account → `/tenant/register`; if invite-only, submit a request at `/backlog`
4. 登录成功后进入租户后台核心入口 `/tenant/dashboard` / On success, you'll land at `/tenant/dashboard`

### 邀请码相关 / Invitation codes

邀请码功能在 `/tenant/dashboard#invitations`：
At `/tenant/dashboard#invitations`:

- **手里有别人给的邀请码** → 在"填写邀请人的邀请码"输入 8 位邀请码（**区分大小写**）→ 点击"立即绑定" / Have a code → enter the 8-char code (**case-sensitive**) → bind
- **想申请自己的邀请码** → 点击"申请邀请资格" → 等管理员审核 → 通过后在"我的邀请码资格"复制邀请码发给被邀请人 / Want to invite others → "Apply for invite quota" → wait for admin review → copy your code from "My quota"

常见限制 / Common limits:
- 不能填写自己的邀请码 / Can't bind your own code
- 一个邀请码只能使用一次 / One code, one use
- 已使用 / 不存在的邀请码无法再次绑定 / Used / non-existent codes can't be re-bound

---

## 第二步：获取专属 API Key / Step 2 — Get your API key

API Key 是您调用平台能力的唯一身份凭证。
The API key is your sole credential for platform calls.

1. 在 `/tenant/dashboard` 找到 "API Key 管理" 区域 / Find "API Key Management" on the dashboard
2. 您会看到一串以 `sk-` 开头的长字符串 / You'll see a long `sk-` prefixed string
3. 点击"复制"按钮，保存到本地环境变量或安全的密码管理器 / Click "Copy" and store in env vars or a password manager

> ⚠️ **务必妥善保管**：API Key 等同于"数字身份证 + 银行卡密码"。**绝不要泄露给他人**，**绝不要硬编码在前端代码（Vue/React）**或客户端 App 中，**绝不要提交到公开代码仓库（如 GitHub）**。一旦泄露可能被盗刷余额，需立即在后台重置。
> ⚠️ **Guard it carefully**: think "ID card + bank password". **Never share**, **never hardcode in front-end code** (Vue/React) or client apps, **never commit to public repos** (GitHub). On leak, reset immediately in the dashboard.

---

## 第三步：完成首次充值 / Step 3 — Recharge

SEE2AI 采用"按需计费、先充后用"的模式。为避免首次调用因余额不足返回 401，请先完成首次充值。
SEE2AI uses pay-as-you-go with prepaid balance. To avoid 401 on your first call, complete an initial recharge.

1. 在 `/tenant/dashboard` 点击 "充值与套餐"（路径 `/tenant/recharge`）/ Click "Recharge & Plans" (`/tenant/recharge`)
2. 在该页面选择当前提供的充值金额或自定义金额（具体范围与最低门槛以页面实际展示为准）/ Choose from currently available recharge amounts or a custom value (the actual range and minimum are as shown on the page)
3. 选择当前可用的在线支付方式完成付款 / Pick an available online payment method
4. 支付成功后返回 `/tenant/dashboard`，可用余额会以平台词元 `cost_points` 形式实时显示 / After payment, your balance shows in `cost_points` on the dashboard

> 💡 如果您计划**连续生成图片、视频、TUVE 短视频或 UniWorld2.5 图像**，建议提前一次性准备较充足的余额，避免任务中途因余额不足被打断。具体合适的金额可结合 `/actions` 页面的单价、您的预期调用量自行评估，或参考 `/tenant/recharge` 页面当前展示的档位建议。
> 💡 If you plan **continuous image / video / TUVE / UniWorld2.5 generation**, recharge a generous balance up front. Estimate the right amount from per-call prices on `/actions` and your expected volume, or refer to the tier suggestions currently shown on `/tenant/recharge`.

详细计费机制见 [`pricing_and_account.md`](pricing_and_account.md)。
Full billing mechanism: [`pricing_and_account.md`](pricing_and_account.md).

---

## 第四步：发起首次 API 调用 / Step 4 — Make your first call

万事俱备 / Time to call.

### 4.1 核心配置参数 / Core config

- **Base URL**: 您所在环境的 SEE2AI 主域名 + `/api/v1` 后缀 / Your SEE2AI environment's main domain + `/api/v1` suffix
- **API Key**: 第二步获取的 `sk-` 开头密钥 / The `sk-` key from Step 2
- **Header**: `Authorization: Bearer sk-<您的密钥>` / `Authorization: Bearer sk-<your-key>`
- **接口地址 / Endpoint**: `POST /api/v1/chat/completions`（标准对话接口，与通用 SDK 兼容）/ Standard chat endpoint, compatible with common SDKs
- **Model 字段 / Model field**: 可在 `/actions` 页面查看当前可用全部模型清单 / See `/actions` for the live list

### 4.2 Python 示例 / Python example

```python
import os
import requests

api_key = os.environ["SEE2AI_API_KEY"]
base_url = os.environ.get("SEE2AI_BASE_URL", "https://see2ai.com/api/v1")

response = requests.post(
    f"{base_url}/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    },
    json={
        "model": "<请到 /actions 查询当前可用模型名 / pick from /actions>",
        "messages": [{"role": "user", "content": "你好，测试连接！"}],
    },
    timeout=60,
)

print(response.json())
```

### 4.3 cURL 示例（命令行直接测）/ cURL example (no code)

```bash
curl https://see2ai.com/api/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer 您的sk-密钥" \
  -d '{
    "model": "<请到 /actions 查询当前可用模型名>",
    "messages": [{"role": "user", "content": "你好，测试连接！"}]
  }'
```

### 4.4 流式输出（重要）/ Streaming (important)

如果您开启 `stream: true`，**务必加上** `stream_options={"include_usage": true}`，否则平台无法统计 token 消耗，可能导致调用异常。
If you enable `stream: true`, **always add** `stream_options={"include_usage": true}`. Otherwise the platform can't account for token usage, which may break the call.

```json
{
  "model": "<您选择的模型>",
  "messages": [{"role": "user", "content": "你好"}],
  "stream": true,
  "stream_options": {
    "include_usage": true
  }
}
```

---

## 进阶探索 / Going further

恭喜！跑通文本对话只是入门——SEE2AI 的精髓在于"让 Agent 真正干活"（生图、生视频、解析文档等）。
Congrats! Text chat is the warm-up — SEE2AI shines at "Agents That Act" (images, videos, doc parsing).

### 浏览全部能力 / Browse all capabilities
访问 `/actions` 页面，浏览平台提供的所有 Action（如 `see2ai_image_generation_v1`、`see2ai_storage_upload_v1` 等）。点击任意 Action 进入详情页，您会看到：
Visit `/actions` to browse all Actions (e.g. `see2ai_image_generation_v1`, `see2ai_storage_upload_v1`). Each detail page contains:
- 功能描述与适用场景 / Description & use cases
- 完整请求体（Body）结构与参数说明 / Full request body schema
- 可直接复制的 Python / cURL 示例代码 / Ready-to-copy Python / cURL examples
- 该接口具体的计费规则 / Per-Action billing rules

完整能力分类参见 [`capabilities.md`](capabilities.md)。
Full capability taxonomy: [`capabilities.md`](capabilities.md).

### 探索"无需写代码"的应用生态 / Explore the no-code apps

| 应用 / App | 入口 / Path | 适合 / For |
|---|---|---|
| **TUVE** | `/apps/tuve` | 通过对话完成短视频创作 / Dialogue-driven short-video creation |
| **TABLE** | `/apps/table` | 用表格批量组织和执行 AI 任务 / Spreadsheet-driven batch AI tasks |

TUVE 详细介绍见 [`../tuve/`](../tuve/)。
TUVE deep-dive: [`../tuve/`](../tuve/).

### 开发者实用 API / Useful developer APIs

- `GET /api/v1/me` — 查询当前租户信息和余额 / Current tenant info & balance
- `GET /api/v1/usage` — 按 Action 和时间范围查询用量统计 / Usage stats by Action and time range

---

## 平台功能地图：常用入口速查 / Platform map — common URL paths

| 我想做什么 / I want to | 去哪 / Go to |
|---|---|
| 登录 / 注册 / Log in / register | `/tenant/login` · `/tenant/register` |
| 看余额 / API Key / Balance & key | `/tenant/dashboard` |
| 看调用日志 / 账单 / Call logs & bills | `/tenant/dashboard#logs` · `/tenant/dashboard#bills` |
| 配置与可用能力 / Config & skills | `/tenant/dashboard#settings` · `/tenant/dashboard#skills` |
| 修改账户信息 / Edit account | `/tenant/dashboard#account`（敏感字段建议提交工单 / Sensitive fields → file ticket） |
| 邀请码 / Invitations | `/tenant/dashboard#invitations` |
| 充值与套餐 / Recharge & plans | `/tenant/recharge` |
| Action 能力列表 / Actions catalog | `/actions` |
| TUVE 短视频 | `/apps/tuve` |
| TABLE 批量任务 | `/apps/table` |
| 提交 Bug / 反馈 / 工单 / Bugs & tickets | `/backlog` |

---

## 接入过程中卡住了 / Stuck during onboarding?

- **遇到 401 / 429 / 5xx 报错** → 看 [`support.md`](support.md) §1 排查指南，或前往 SEE2AI 平台内 `/backlog` 提交工单 / Hit error codes → see support docs § 1 or file ticket
- **不确定该选哪个 Action / 哪个模型** → 参考 [`capabilities.md`](capabilities.md) 能力分类表，或前往 SEE2AI 平台 `/actions` 页面查看实时清单 / Not sure which Action / model → check the capability table or visit `/actions` for the live list
- **价格 / 充值 / 余额疑问** → [`pricing_and_account.md`](pricing_and_account.md) / Pricing questions → see pricing doc
- **想了解 SEE2AI 是什么、能干什么** → [`platform_overview.md`](platform_overview.md) / Want to know what SEE2AI is → see overview
