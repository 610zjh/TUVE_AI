---
name: 数据与隐私 / Data and Privacy
description: 哪些数据能给 AI 看、哪些不能、给之前要做哪些处理 / What data AI can see, what it can't, and what to do before sharing
type: permanent
retention: permanent
retention_reason: 合规底线，违反将触发法律 + 客户信任双重风险 / Compliance floor; violations trigger both legal and trust risks
---

# 数据与隐私 / Data and Privacy

## 三类数据，三种姿态 / Three Data Classes, Three Postures

| 类别 / Class | 例子 / Examples | 能给 AI 看吗 / Allowed in AI context? |
|---|---|---|
| **公开 / Public** | 营销文案、产品介绍、公开新闻、公开数据集 / Marketing copy, product intro, public news, open datasets | ✅ 直接用 / Yes, directly |
| **内部 / Internal** | 内部流程、自家代码、自家产品文档、自家 OKR / Internal processes, our code, our product docs, our OKRs | ⚠️ 用公司付费的 AI 工具可以；个人账号 / 公开网页版禁止 / OK on company-paid AI; banned on personal accounts / public web UIs |
| **机密 / Confidential** | 客户数据、合同条款、销售管线、薪酬、个人身份信息（PII）/ Customer data, contract terms, sales pipeline, comp, PII | 🚫 必须脱敏后才能给 AI / Must be redacted before AI sees |

---

## 红线 #3 + #12 重申 / Red Lines #3 + #12 Restated

**红线 #3**：未脱敏的机密数据严禁进入 AI 上下文，包括"我只是给 AI 看一眼"的临时复制粘贴。
**Red Line #3**: unredacted confidential data never enters AI context, including "just letting AI take a quick look" copy-paste.

**红线 #12**：[`workspace_human/`](../../workspace_human/) 是 AI 只读区。AI 不许修改人写的 PRD、会议纪要、客户案例复盘。
**Red Line #12**: [`workspace_human/`](../../workspace_human/) is AI read-only. AI may not edit human-written PRDs, meeting notes, customer reviews.

---

## 机密数据脱敏 SOP / Confidential Data Redaction SOP

### 1. 客户数据 / Customer Data

需要脱敏的字段 / Fields to redact:
- 真实姓名 → `客户A` / `客户B` / Real names → `Customer A` / `Customer B`
- 公司名 → `行业-规模标签`（如"教育-中型"）/ Company name → `industry-size tag` (e.g., "Education-Medium")
- 真实手机 / 邮箱 / 微信 / Real phone / email / WeChat → `示例: 138****0000` / placeholder
- 真实订单金额 → 量级（"五万级"、"百万级"）/ Real order amount → magnitude ("5-figure RMB", "7-figure RMB")
- 合同条款原文 → 摘要（"包含为期一年的独家代理"）/ Contract clauses → summary

### 2. 销售管线 / Sales Pipeline

谈到具体客户 / 阶段 / 预测金额时：
When discussing specific customers / stages / forecasts:
- 用脱敏标签替代真实身份 / Use redacted labels instead of real identities
- 用"概率档位"代替具体百分比（"高/中/低意向"）/ Use probability buckets instead of specific percentages

### 3. 个人身份信息（PII）/ PII

绝对不能进 AI 的：
Absolute do-not-send:
- 身份证号 / 护照号 / 社保号 / ID, passport, social security
- 银行账号 / 信用卡号 / Bank, credit card
- 真实家庭住址 / Real home address
- 生物识别信息（指纹、面部识别原始数据）/ Biometric raw data

如果业务真的需要 AI 处理涉及 PII 的工作，**只有在公司专设的、合规审过的、签了 DPA 的 AI 服务**上才允许，且必须按 [`runbooks/`](../../runbooks/) 里的 PII 处理流程走。
If the business genuinely needs AI to process PII-adjacent work, it's **only allowed on a company-designated, compliance-reviewed, DPA-signed AI service**, and must follow the PII handling runbook in [`runbooks/`](../../runbooks/).

### 4. 内部财务 / 薪酬 / Internal Finances and Comp

- 公司财务报表、薪资结构、股权信息 → 严禁送 AI / Strictly off-AI
- 部门预算 / 项目成本预估 → 内部 AI 工具上 OK，个人账号禁止 / OK on internal AI, banned on personal accounts

---

## 脱敏前后对比 / Before vs After Redaction

❌ **脱敏前（不可发送给 AI）/ Before redaction (DO NOT send to AI):**
> 帮我整理今天和"晨星科技"李总的电话，他说他们公司有 200 个员工，月预算 5 万 RMB，对接邮箱 lizhongming@chenxing.com，电话 13800001234，他们有 3 个竞品在比，预计下周三下决定。

✅ **脱敏后（可以发送）/ After redaction (OK to send):**
> 帮我整理今天和"客户A"（教育-中型）对接人 X 的电话。预算量级：万级月预算。在比 2-3 家竞品。下决策时间：本周末前。

效果一样（AI 帮你整理对话内容），但即使这份提示词被泄露，也不会泄露客户身份。
Same effect (AI helps organize the call), but if the prompt leaks, no customer identity leaks.

---

## `workspace_human/` 是什么、为什么 AI 不能改 / What `workspace_human/` Is and Why AI Can't Edit

[`workspace_human/`](../../workspace_human/) 存的是**人独有的、不可被 AI 替代的判断与决策记录**：
[`workspace_human/`](../../workspace_human/) holds **human-exclusive judgments and decision records that AI cannot replace**:

- `prd/` —— 产品经理写的需求文档，是项目的"原始意图" / PM-written PRDs, the "original intent" of a project
- `meetings/` —— 会议纪要、ADR、客户案例复盘 / Meeting notes, ADRs, customer case reviews
- 偶尔还有：手写笔记的扫描、白板照片、关键对话录音的转写 / Occasionally: handwritten notes, whiteboard photos, transcripts of key conversations

为什么 AI 不能改 / Why AI cannot edit:
1. **PRD 是合同**。一旦人写好，AI 不许擅自改需求段——否则原始意图丢失。
   PRD is a contract. Once written, AI doesn't get to alter requirements unilaterally — original intent must be preserved.
2. **会议纪要是史料**。AI 改动会模糊"谁在什么时候说了什么"的可追溯性。
   Meeting notes are historical records. AI edits blur "who said what when" traceability.
3. **客户案例复盘涉及对真实客户的判断**。判断要留人。
   Customer case reviews involve judgment about real customers — judgment stays with humans.

允许的 AI 动作 / What AI may do:
- ✅ 读 / Read
- ✅ 引用（在其他地方）/ Reference (elsewhere)
- ✅ 在 PRD 末尾追加"实施记录" / Append "implementation log" at the bottom of a PRD
- ✅ 用模板帮人**新建** PRD / 会议纪要——人确认后由人保存进 `workspace_human/` / Help **draft new** PRDs / meeting notes from templates — human confirms and saves into `workspace_human/`

不允许的 AI 动作 / What AI may NOT do:
- ❌ 修改已有 PRD 的需求段 / 验收标准段 / Edit requirements or acceptance-criteria sections of existing PRDs
- ❌ 修改会议纪要里的发言记录 / Edit speech records in meeting notes
- ❌ "更新"客户案例复盘的判断段 / "Update" judgment sections of customer reviews
- ❌ 删除 `workspace_human/` 下任何文件 / Delete anything under `workspace_human/`

例外只有一种：人**明确说**"在 PRD-XXXX 末尾追加一段实施记录"——这种**指明具体动作和位置**的授权才算授权。
Only exception: human says **specifically** "append an implementation log to PRD-XXXX" — only such **explicit-action-and-location** authorization counts.

---

## 跨系统数据流 / Cross-System Data Flow

公司内常见的数据流向：
Common data flows inside the company:

```
CRM / 客户系统          ──┐
合同管理系统          ──┼──> 提取片段 ──> 脱敏 ──> AI 处理 ──> 人审核 ──> 落回 CRM / 文档
ERP / 财务系统          ──┘
                                                                  ↓
                                                       禁止把 AI 原始输出
                                                       直接回写到 CRM /
                                                       发送给客户
```

关键节点：
Key checkpoints:
- **提取片段时**：只取最小必要的部分，不要"全表导出给 AI 看一眼" / Pull minimum necessary; never "export the whole table for AI to glance at"
- **脱敏后送 AI**：用上节的 SOP / Apply the SOP above
- **AI 输出后审核**：参考 [`subs/working_with_ai.md`](working_with_ai.md) §4 的两道关 / Use the two gates in `working_with_ai.md` §4
- **回写时实名替换**：脱敏标签换回真实身份的最后一步**由人**做，不让 AI 替代 / Re-mapping placeholders to real identities is **the human's** final step, not AI

---

## 紧急情况：发现数据已经送给了不该送的地方 / Emergency: Data Already Leaked to Wrong AI Service

执行顺序：
Order of operations:

1. **立即停**——别让对话继续，别再追加更多 / Stop the chat; don't add more
2. **截屏存证**——保留是哪个工具、什么时间、什么内容 / Screenshot for record
3. **30 分钟内通报合规 / 法务 / 数据保护负责人** / Notify compliance / legal / DPO within 30 min
4. **按对应工具的"删除我的数据"流程提交申请**（多数主流 AI 厂商都有 30-90 天数据保留窗口）/ File the "delete my data" request via the tool's vendor flow (most have 30-90-day retention windows)
5. **写一份事故纪要**到 [`workspace_human/meetings/`](../../workspace_human/meetings/)，登记影响范围、客户是否需要通知、未来防范措施 / File an incident note in [`workspace_human/meetings/`](../../workspace_human/meetings/): scope, customer notification needed?, prevention

不要藏。藏了 6 个月之后被审计抓出来比当下报告严重 100 倍。
Don't hide. Discovery 6 months later by audit is 100× worse than reporting now.

---

## 实战检查清单 / Practical Checklist

每次准备发送给 AI 的 prompt，过一遍：
Before sending each prompt to AI, run through:

- [ ] 这段里有没有真实人名？/ Real person names?
- [ ] 这段里有没有真实公司名（除了我们自己 TUZHAN）？/ Real company names (other than TUZHAN itself)?
- [ ] 这段里有没有具体金额？/ Specific monetary amounts?
- [ ] 这段里有没有手机 / 邮箱 / 身份证 / 银行账号？/ Phones / emails / IDs / bank accounts?
- [ ] 这段里有没有合同条款原文？/ Verbatim contract clauses?
- [ ] 这段里有没有未公开的产品 roadmap？/ Unpublished product roadmap?

任何一项命中 → 脱敏后再发，或者改用公司专设的合规 AI 服务。
Any hit → redact first, or use the company's compliance-approved AI service.
