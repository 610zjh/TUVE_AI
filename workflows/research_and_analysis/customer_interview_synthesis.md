# 客户访谈总结 / Customer Interview Synthesis

> 适用：销售、产品、运营访谈完客户后，把内容整理成可决策的洞察。
> For: distilling actionable insight from customer interviews (sales / product / ops).

---

## 一句话 / One Line

**访谈纪要是事实记录；访谈洞察是判断和行动。** 别把两者混在一起。
**Interview minutes record facts; interview insights record judgment and action.** Don't conflate.

---

## 访谈前 / Before the Interview

### 准备 3 件事 / Prepare 3 Things

1. **判断题**：这次访谈完后，我希望能回答的具体问题是什么？/ What specific questions do I expect to answer?
2. **核心问题**：5-7 个开放式问题（不是是非题）/ 5-7 open-ended questions
3. **录音 + 同意**：明确征得客户同意录音 / 笔记是不是会内部分享 / Recording + consent

```
访谈前我希望明确：
- 判断题：[1-3 个]
- 核心问题清单：[5-7 个开放式]
- 同意条款：[录音 / 内部分享 / 客户匿名 / 客户实名]
```

---

## 访谈中 / During the Interview

### 三个原则 / Three Rules

1. **多听，少讲**：你的发言占比 ≤ 20% / Talk ≤ 20% of the time
2. **追"为什么"**：客户说"X 不好用"→ 追问"具体什么场景下 X 不好用？" / Drill into "why"
3. **不要替客户编故事**：客户没说的，不要假设 / Don't fill gaps for the customer

### AI 实时辅助的边界 / AI Real-Time Assistance Boundary

❌ AI 不要参与对话本身（除非全员同意）
❌ AI 不要替你判断客户情绪 / 真假
✅ AI 可以在另一屏帮你查事实（"客户提到的 X 法规是什么意思"）
✅ AI 可以帮你提示下一个追问问题

---

## 访谈后 24 小时 / Within 24 Hours After

### 步 1：写客观纪要（30 分钟）/ Step 1: Objective Minutes (30 min)

```markdown
# 客户访谈纪要 - YYYY-MM-DD

- 客户：[已脱敏，如 "客户 A，教育-中型"，按红线 #3]
- 对接人角色：[CTO / 运营负责人 / ...]
- 访谈人：[姓名]
- 访谈时长：N 分钟
- 录音是否存档：是 / 否
- 客户同意：内部分享 / 公开案例 / 完全匿名

## 客户原话（关键 quotes）
- "原话 1"
- "原话 2"
- ...

## 客户主动提到的关键事实
- ...

## 我的追问 + 客户回应
- 问：... / 答：...
```

存到 [`workspace_human/meetings/customer_interviews/`](../../workspace_human/meetings/) 下。
Save under `workspace_human/meetings/customer_interviews/`.

### 步 2：用 AI 帮你提取主题 / Step 2: AI-Assisted Theme Extraction

```
基于上面的纪要：
1. 提取 3-5 个反复出现的主题（不要无中生有）
2. 每个主题给 1-2 条客户原话作为依据
3. 标出每个主题在多少位客户身上看到（如果你有多份纪要可以一起送进来对比）
4. 列出客户**没说但我直觉感到**的潜在主题（标"假设"）
```

### 步 3：从主题到判断 / Step 3: Themes to Judgments

```
基于上面 3-5 个主题，回答：
- 我们的产品在哪个主题上做得最好？最差？
- 客户最痛的主题是什么？
- 这个主题的痛我们目前能做什么？
- 如果我们什么都不做，3 个月后客户的态度会怎样？
```

### 步 4：从判断到行动 / Step 4: Judgments to Actions

```
基于上面的判断，列出 top-3 行动项：
- 行动 1：负责人 / 截止 / 预期效果
- 行动 2 ...
- 行动 3 ...

注意：不是每个客户访谈都需要立即行动。如果当前结论是"再做 N 次访谈再判断"，
就明确写"暂不行动；下一步是访谈 [X 类客户] N 位"。
```

---

## 多次访谈的合并分析 / Cross-Interview Synthesis

访谈 ≥ 5 位客户后，做一次合并分析：
After ≥ 5 interviews, run a synthesis:

```
请把下面 N 份访谈纪要做合并分析：

1. 反复在 ≥ 60% 客户身上出现的主题（标"高共识"）
2. 在 30-60% 客户身上出现的（标"中共识"）
3. 仅在 < 30% 出现但很有价值的（标"少数但深刻"）
4. 互相矛盾的客户观点（标"分歧点"——通常代表不同客户细分）
5. 我们目前的 PRD / 产品方向 vs 上面 4 类的对照
   - 我们已经在做的
   - 我们没在做的（应不应该做？）
```

---

## 客户访谈的常见错误 / Common Errors

### 错误 1：访谈"老朋友"客户 / Interview Only Friends

❌ 只访谈关系好的客户 → 反馈偏正面
**Fix**：要访谈 (a) 续费的 (b) 流失的 (c) 没买的 三类，配比 1:1:1。

### 错误 2：客户说什么就信什么 / Take Customers at Face Value

❌ 客户说"如果有 X 功能我就买"——你做了 X，客户没买。
**Why**：客户在表达需求时往往会"理性化"——给一个听起来合理的理由，但这不是真实购买决策点。
**Fix**：观察客户**实际行为**（用什么工具 / 怎么花时间 / 怎么决策）比听他们**说**更可靠。

### 错误 3：让 AI"提炼洞察"太早 / AI Synthesizes Too Early

❌ 访谈 1 个客户就让 AI 总结成"行业洞察"
**Why**：N=1 不是洞察，是轶事。
**Fix**：≥ 5 位客户再让 AI 做合并分析。

### 错误 4：把客户原话当结论 / Quote ≠ Conclusion

❌ 客户说"我觉得这个功能没用"→ 团队读完后决定不做。
**Why**：单个客户的话可能反映他自己的场景，不代表所有客户。
**Fix**：单条 quote 是"假设"，需要在多位客户里验证。

---

## 数据脱敏纪律 / Redaction Discipline

红线 #3 在客户访谈里特别容易踩：
Red Line #3 is particularly easy to violate in interviews:

| 不要 / Don't | 要 / Do |
|---|---|
| 在 AI 提示里粘贴"晨星科技 CTO 张总说 X" | "客户 A（教育-中型）的 CTO 角色对接人说 X" |
| 把客户邮箱 / 电话写在纪要里 | 删掉或用占位符 |
| 写客户的具体合同金额 | 用量级（"五位数月费"）|
| 提及客户的客户的名字 | 行业 + 规模脱敏 |

详细 SOP 见 [`principles/subs/data_and_privacy.md`](../../principles/subs/data_and_privacy.md)。

---

## 速查 / Cheat Sheet

```
访谈前：判断题 + 5-7 开放问题 + 同意条款
访谈中：你 ≤ 20% / 追"为什么" / 不替客户编
访谈后 24h：客观纪要（脱敏） → AI 提主题 → 判断 → 行动

≥ 5 位客户后：合并分析（高共识 / 中共识 / 少数深刻 / 分歧点）

不要：只访"老朋友"；信"如果有 X 我就买"；N=1 就总结；单条 quote 当结论
```
