---
name: 保密 / Confidentiality
description: 公司机密的边界、什么进 AI、什么不进、违规后的紧急流程 / Confidentiality boundaries, what goes into AI, what doesn't, breach response
type: permanent
retention: permanent
retention_reason: 法律 + 客户信任的双重底线 / Both legal and customer-trust floor
---

# 保密 / Confidentiality

## 三档分类（重申自 [`data_and_privacy.md`](data_and_privacy.md)）/ Three Tiers (Restated)

| 档级 / Tier | 描述 | 进 AI 上下文 |
|---|---|---|
| 🟢 公开 / Public | 营销 / 产品介绍 / 公开新闻 | ✅ 自由 |
| 🟡 内部 / Internal | 内部流程 / 自家代码 / 自家 OKR | ⚠️ 公司付费 AI 可以；个人账号 / 公开 web 禁止 |
| 🔴 机密 / Confidential | 客户数据 / 合同 / 销售 / 财务 / PII | 🚫 必须脱敏后才能进 |

详细 SOP 在 [`data_and_privacy.md`](data_and_privacy.md)。本文件聚焦**保密本身**——什么算保密、为什么保密、违规后果、紧急响应。
Detailed SOP in [`data_and_privacy.md`](data_and_privacy.md). This file focuses on **confidentiality itself** — what counts, why, consequences, emergency response.

---

## 1. 什么算保密 / What Counts as Confidential

✅ 是保密 / IS confidential:
- **客户的所有数据**（包括客户的内容素材、客户的客户、客户的销售记录）/ All customer data (their content, their customers, their sales records)
- **合同条款原文**（金额、期限、独家条款、违约条款）/ Verbatim contract clauses (amounts, terms, exclusivity, penalties)
- **销售管线**（客户名 + 阶段 + 预期金额）/ Sales pipeline (customer + stage + expected amount)
- **薪酬信息**（具体数字、个人薪资、股权信息）/ Comp (specific numbers, individual salary, equity)
- **未发布的 product roadmap**（哪个功能何时发）/ Unreleased product roadmap (when which feature ships)
- **PII**：身份证、护照、银行卡、真实手机/邮箱、家庭地址 / PII
- **内部代号 / 项目代号**（违反红线 #2）/ Internal codenames (Red Line #2)
- **内部财务报表**（PnL、成本结构、毛利）/ Internal financials (PnL, costs, margins)
- **客户提供的认证 / 凭证**（客户给我们用来集成他们系统的 API key、SSO secret）/ Customer-provided credentials (API keys, SSO secrets they shared with us for integration)

⚠️ 模糊地带 / Gray zone:
- 自家产品的技术架构图——大致原理可以公开（营销价值），具体到模块名 / 内部 API 不行 / Our tech architecture — high-level OK (marketing value), module names / internal APIs not
- 客户**已经公开**承认是我们客户的，可以提到名字；没公开的不能 / Customers who have **publicly** disclosed they're our client → can name; otherwise can't
- 客户类型 / 行业 / 规模——量化脱敏后可以讨论 / Customer type / industry / size → OK after quantitative redaction

---

## 2. 为什么这条特别严 / Why Especially Strict

### 直接的法律风险 / Direct Legal Risk

- 国内《个人信息保护法》：违反可处营业额 5% 罚款 / PIPL: up to 5% of revenue penalty
- 欧盟 GDPR（如有欧洲客户）：违反可处全球营业额 4% 罚款 / GDPR: up to 4% of global revenue penalty
- 客户合同里的保密条款：违约通常意味着合同终止 + 违约金 / Confidentiality clauses in customer contracts: breach = termination + penalty
- 客户的客户的数据（B2B2C 场景）泄露：连锁责任 / Downstream customers' data leak: cascading liability

### 间接的信任风险 / Indirect Trust Risk

- 一次客户数据泄露 → 这个客户失去 → 客户的同行业网络扩散 → 这一行业的客户都流失 / One leak → that customer churns → spreads in their network → industry-wide loss
- 销售管线泄露 → 竞争对手知道你们在追哪些客户 → 抢先 / Sales pipeline leak → competitor knows your pursuits → preempts
- 内部代号 / roadmap 泄露 → 公关被动 / 客户期望管理失控 / Internal codenames / roadmap leak → PR setbacks, expectations chaos

---

## 3. 进入 AI 上下文的"心理门槛" / Mental Threshold for AI Context

每次准备粘贴东西给 AI 时，自问：
Each time before pasting into AI:

> **如果这段被截图发到外网，我能承受吗？我们公司能承受吗？**
> **If this got screenshotted and posted publicly, could I survive? Could the company survive?**

不能 → **不要粘**。
No → **don't paste**.

这个门槛比"AI 厂商承诺不用于训练"更高。理由：
This threshold is higher than "AI vendor promises not to use for training". Reasons:
- AI 厂商的承诺可能改变 / The vendor's promise may change
- 你的截图可能被你自己手贱发到 Slack 群 / You may accidentally post your own screenshot to a Slack channel
- 同事可能 over-shoulder 看到你屏幕上的对话 / Colleagues may look over your shoulder
- 系统更新可能改变默认数据流向 / System updates may change default data flow

把"会被截图发出去"当成默认假设。
Default assumption: "this will be screenshotted publicly."

---

## 4. 脱敏到什么程度算够 / How Much Redaction Is Enough

够 / Sufficient:
- 把所有可识别身份的字段替换成占位符 / Replace all identifiable fields with placeholders
- **再加一道 reverse-engineering 检查**：把脱敏后的内容假装是给一个"知道我们公司行业"的同行看，他能拼出原始客户是谁吗？/ **Run a reverse-engineering check**: assume readers know your industry — can they identify the original customer?
  - 例：脱敏掉了客户名，但留下了"教育行业""华东""学生数 5000-10000""使用 Gemini 不用 OpenAI"——这些组合可能拼回去 / E.g., removed name but left "education / East China / 5K-10K students / uses Gemini not OpenAI" → may be reverse-identifiable
- 经过 reverse-engineering 检查后还过得去，才算脱敏完成 / Only after passing reverse-engineering is redaction complete

不够 / Insufficient:
- 只删了名字，留下了一切其他可识别字段 / Removing only the name, leaving all other identifiers
- 用首字母代替（"Z 公司"——同业一查就知道是谁）/ Initial substitution ("Company Z" — recognizable in-industry)
- 在脱敏后的版本里"附录原始版本以防万一"——一份脱敏版 + 一份原版 = 没脱敏 / Attaching the original "in case" — defeats the redaction

---

## 5. AI 工具的保密分级 / AI Tool Confidentiality Tiers

按公司给每种工具的部署 / 账号情况分级：
Tiered by deployment / account type:

| 工具配置 / Tool config | 处理范围 / Allowed data |
|---|---|
| **公司账号 + 训练 opt-out + 私有部署** / Company account + training opt-out + private deploy | 🟢 + 🟡 + 部分脱敏后 🔴 |
| **公司账号 + 训练 opt-out（无私有部署）** / Company account + opt-out, hosted | 🟢 + 🟡 + 脱敏后 🔴 |
| **公司账号但默认配置** / Company account, default config | 🟢 + 🟡（注意：可能用于训练）|
| **个人账号 / 免费版** / Personal / free tier | 🟢 only |
| **公开 web 界面（claude.ai / chatgpt.com 网页版）** / Public web UI | 🟢 only |

不确定当前用的是哪一档时，**默认按最严格档**对待。
When unclear which tier, **default to strictest**.

---

## 6. 保密承诺给客户的口径 / Confidentiality Posture to Customers

客户问"你们用 AI 处理我们的数据吗"，统一回答：
When customer asks "do you use AI on our data", unified answer:

> 您的数据按机密档处理。任何使用 AI 加速的环节，我们会先脱敏。脱敏标准包括：去除身份信息、合同金额、个人联系方式等。我们使用的 AI 服务是企业账号，关闭训练数据贡献。如果您希望禁用 AI 加速，可以联系销售对接。

> Your data is handled at confidential tier. Where AI accelerates work, we redact first. Redaction includes: removing identifying info, contract amounts, personal contact info. We use enterprise AI accounts with training opt-out. If you'd like to disable AI acceleration, please contact sales.

不要说 / Don't say:
- ❌ "我们绝对不用 AI 处理您的数据"——兑现不了 / "We never use AI on your data" — can't deliver
- ❌ "我们的 AI 100% 私有部署"——除非这真的是事实 / "Our AI is 100% private" — unless actually true
- ❌ "AI 不会出错"——一定会 / "AI doesn't make mistakes" — it does

---

## 7. 紧急响应：发现机密已泄露给 AI / Emergency: Confidential Data Leaked to AI

执行顺序（不要乱顺序）/ Order (don't reorder):

1. **立即结束当前会话**——不要"试着删一下"，每次操作可能在服务端日志再次记录 / **End the session immediately** — don't "try to delete", each action may relog
2. **截屏证据**——什么工具、什么时间、什么内容（占位描述，不要复制原文再次粘贴）/ Screenshot for record — tool, time, content placeholder (don't repaste the original)
3. **30 分钟内通报合规 / 法务 / 数据保护负责人** / Notify compliance / legal / DPO within 30 min
4. **根据工具厂商提交"删除我的数据"流程**——多数有 30-90 天保留窗口 / File vendor's "delete my data" flow — most have 30-90-day retention
5. **判断是否要通知客户**：
   - 涉及 PII / 合同条款 → **必须**通知客户 / Involves PII / contract terms → **must** notify customer
   - 仅涉及业务数据但脱敏不充分 → 由合规和法务决定 / Business data with insufficient redaction → compliance and legal decide
6. **写事故报告到 [`meetings/`](../../meetings/)**——影响范围、根因、行动项 / File incident report — impact, root cause, action items

**禁止**：
**Forbidden**:
- 隐瞒不报 / Concealment
- 自行决定"应该没事吧"不通知客户 / Unilaterally deciding "probably fine, no notify"
- 等到下班后再说 / Deferring until after-hours

---

## 8. 保密文化的日常 / Day-to-Day Confidentiality Culture

不是"出事了才保密"，而是**默认状态就是保密**：
Not "confidentiality kicks in when something happens", but **confidentiality is the default state**:

- 屏幕共享前先扫一遍当前打开的标签页和窗口 / Scan tabs and windows before screen-sharing
- 在公共场合（咖啡馆、机场）不和同事讨论客户名 / 合同金额 / In public (cafés, airports), don't discuss customer names / amounts with colleagues
- 离开座位锁屏 / Lock screen when leaving desk
- 不在不应该的场合（非工作 IM、个人邮箱）转发工作内容 / Don't forward work content via personal IM / email
- 离职时按交接清单**清晰**移交，不带走任何客户数据 / On departure, hand over clearly per checklist; don't take any customer data

这些看似琐碎的小事，是保密文化的真实样子。
These mundane habits are what real confidentiality culture looks like.
