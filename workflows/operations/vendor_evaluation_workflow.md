# 供应商评估 / Vendor Evaluation Workflow

> 适用：运营、IT、采购、产品在评估第三方工具 / 服务 / 供应商时。
> For: ops / IT / procurement / product evaluating 3rd-party tools / services / vendors.

---

## 一句话 / One Line

**供应商评估不是"找便宜的"，是"找 5 年后还能合作的"。** 长期主义在这里特别重要。
**Vendor evaluation isn't "find the cheapest"; it's "find one we can still work with in 5 years".** Long-term thinking matters here.

---

## 标准评估 5 维度 / Standard 5-Dimension Evaluation

```
1. 功能契合 / Feature Fit
   - 当前需求覆盖度
   - 6 个月后预期需求覆盖度
   - 缺失功能：能否定制 / 走 API / 等更新

2. 商业可持续 / Business Sustainability
   - 公司规模 / 融资轮次 / 客户数量
   - 业务收入是否健康（不是亏钱烧钱模式）
   - 5 年内倒闭概率（粗略估）

3. 数据安全与合规 / Security & Compliance
   - 是否签 DPA
   - 数据存储位置（中国境内 / 境外）
   - 是否符合个保法 / GDPR / 行业监管
   - 是否有 SOC 2 / ISO 27001 等认证

4. 技术成熟度 / Technical Maturity
   - API 文档完整度
   - 历史 SLA / 故障率
   - 集成难度（自评 1-5）

5. 合作 + 退出 / Partnership & Exit
   - 合同条款是否合理
   - 数据导出是否容易（避免锁定）
   - 切换到其他供应商的成本
```

每个维度打 1-5 分，加权求总分。
Score 1-5 each, weighted sum.

---

## 用 AI 协助的 4 步 / 4 Steps with AI

### 步 1：列候选 / Step 1: List Candidates

```
我们要找一个 [类型] 的供应商。需求是 [一句话]。预算 [量级]。

请帮我列：
- 5 个国内供应商候选
- 5 个国际供应商候选（如果适用）
- 3 个开源 / 自建的替代选项

每个标注：
- 知名度（高 / 中 / 低）
- 我们这种规模 / 行业的客户多不多
- 你训练数据的截止时间（提醒：我得自己核对最新状态）
```

⚠️ AI 给的候选列表可能过时（训练数据截止）+ 编造（一些"听起来对"的厂商不存在）。**必须自己核对每个候选是否真实存在 + 当前是否还活着**。
**Caveat**: AI's candidate list may be outdated + fabricated. **Verify each candidate exists and is alive**.

### 步 2：5 维度对照表 / Step 2: 5-Dimension Comparison

```
对上面的候选（[列出 3-5 个]），帮我做 5 维度对照表。

对每个供应商：
- 功能契合：基于他们公开的产品页 / 文档（粘贴）
- 商业可持续：基于公开融资信息 / 客户案例
- 数据安全合规：基于他们的安全声明 / 合规认证页
- 技术成熟度：基于他们的 API 文档 / 公开 SLA
- 合作 + 退出：基于他们的合同模板（如有）/ 数据导出说明

我**自己**会去验证每个数据点，但你先帮我组装可读的对照表。

约束：
- 标"不确定"的格子比"瞎猜"好
- 不要捏造融资金额 / 客户数量这种具体数字
```

### 步 3：访谈 + 试用 / Step 3: Interview + Trial

AI 给的资料是公开的，但**真实判断需要访谈和试用**：
AI's input is public; **real judgment requires interview + trial**:

- **访谈他们的现有客户**（最好同行业 / 同规模）/ Talk to their existing customers
- **30 天试用**（如果有）/ 30-day trial
- **小规模 POC**（在你公司低风险场景跑一段时间）/ POC in low-risk context
- **看他们的客服响应**（提一个棘手问题，看回应速度和质量）/ Test their support

### 步 4：决策 + 落字成 ADR / Step 4: Decision + ADR

任何**非平凡**的供应商决策（年度合同、关键基础设施、影响多个团队的工具）落字成 ADR。
Non-trivial vendor decisions → ADR.

模板见 [`templates/decision_record/`](../../templates/decision_record/) 和 [`workflows/decision_records/`](../decision_records/)。

---

## 红线 / Red Lines

### 红线 #3：数据安全是底线

任何供应商如果：
Any vendor that:
- 不签 DPA / Won't sign DPA
- 不能告知数据存储位置 / Can't disclose data location
- 没有合规认证（且业务上需要）/ Lacks compliance certification (when needed)

→ **直接淘汰**，不进 5 维度评分。
→ **Disqualified**, doesn't enter scoring.

### 红线 #6：决策落字成 ADR

供应商决策影响远超表面（数据迁移、合作锁定、长期支出）。
Vendor decisions ripple far (data migration, lock-in, long-term spend).

5 年后回看：当时为什么选这家？没有 ADR 就没人知道。
5 years later: why this vendor? No ADR = no one knows.

### 红线 #15：长期主义

3 年内可能倒闭的小厂商，节省 30% 成本不值。
A vendor likely to fold in 3 years isn't worth 30% savings.

切换供应商的成本 + 风险 + 客户体验中断 → 远超那 30%。
Switch cost + risk + customer disruption → far exceeds the 30%.

---

## 供应商评估的常见错误 / Common Mistakes

### 错误 1：只比较功能 / Feature-Only Comparison

❌ 只看"谁家功能多"
**问题**：忽略了商业可持续 / 数据安全 / 退出成本
**修正**：5 维度全过

### 错误 2：被销售 demo 带偏 / Misled by Sales Demo

❌ 销售给你的 demo 只展示成功路径
**问题**：边界 case / 失败处理 / 真实负载下的表现 你都没看到
**修正**：30 天真实试用，不仅仅看 demo

### 错误 3：忽略"现有客户的真实声音" / Ignore Existing Customer Voice

❌ 看官网客户 logo 就当好评
**问题**：客户 logo 不代表客户满意；满意客户和不满意客户都可能是 logo 客户
**修正**：拿到 2-3 位现有客户做反向访谈（特别是同行业）

### 错误 4：低估"切换成本" / Underestimate Switch Cost

❌ "如果不行我们再换一家"
**问题**：切换成本含数据迁移、团队学习、流程重建、客户感知 —— 通常远超签约成本
**修正**：在签约前评估退出成本；签约时争取数据导出条款

### 错误 5：合规仅靠"我们看了对方说他们合规" / "Vendor Says So"

❌ 信对方营销页的"通过 SOC 2 认证"
**问题**：你需要看实际证书 + 范围 + 有效期
**修正**：要求看实际证书 + 法务过审

---

## 评估周期建议 / Cadence Recommendation

| 决策类型 / Decision Type | 评估期 / Eval period |
|---|---|
| 关键基础设施 / Critical infra | 4-8 周（含 POC）|
| 团队工具 / Team tool | 2-4 周（含试用）|
| 单点功能补充 / Single-feature add | 1-2 周 |
| 紧急救火（如果原有方案断了）| 视情况，但仍要落 ADR |

不要把"我们要快"当作跳过 5 维度的理由。
"We need it fast" is not a reason to skip the 5 dimensions.

---

## 速查 / Cheat Sheet

```
5 维度：功能 / 可持续 / 安全合规 / 技术成熟 / 合作退出

4 步法：列候选（自己核！）→ 对照表（标"不确定"）→ 访谈 + 试用 → ADR

红线：不签 DPA 直接淘汰 / 决策落 ADR / 长期主义优先

陷阱：只比功能 / 被 demo 带偏 / 信 logo / 低估切换成本 / 信"我们合规"
```
