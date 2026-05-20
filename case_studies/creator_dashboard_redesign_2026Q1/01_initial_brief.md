---
name: 01 - 最初的客户反馈
retention: permanent
retention_reason: 案例的"原始触发"段，反映真实需求是怎么来的
---

# 01. 最初的客户反馈

> 这是 PRD-0042 的种子。下面是 2025-Q4 客户访谈中反复出现的反馈。
> Seed of PRD-0042. Below are recurring 2025-Q4 customer-interview feedback patterns.

---

## 触发原因 / Trigger

2025 Q4 客户访谈中（10 位客户，[`workflows/research_and_analysis/customer_interview_synthesis.md`](../../workflows/research_and_analysis/customer_interview_synthesis.md) 流程）汇总出 3 类反复反馈。

In Q4-2025 customer interviews (10 customers), 3 recurring feedback themes surfaced.

---

## 客户原话（脱敏）/ Customer Quotes (Redacted)

### 主题 1：要看 5 个不同页面才能知道"本周做得怎么样"

- "客户 A（教育-中型，运营负责人）"：
  > 我每周一上班第一件事是打开你们后台。但要先去 [模块 A] 看产量，再去 [模块 B] 看播放量，再去 [模块 C] 看互动数据，再去 [模块 D] 看客户反馈，再去 [模块 E] 看排期。一个早上 1 小时就这样过去了。

- "客户 B（电商-小型，主理人）"：
  > 我希望能像看股票 K 线一样一屏知道这周状况。

- "客户 C（教育-大型，运营总监）"：
  > 现在的后台对老员工 OK，新员工要培训 2 周才会用。

### 主题 2：核心数据看完就够了，深度数据看板分开

- 4 位客户主动提到"绝大多数时候我只看 5-10 个核心数字，深度分析一周才看一次"

### 主题 3：移动端体验不行（但不是首要痛点）

- 7 位客户提了，但都说"我们都在 PC 上做事，移动端可有可无"

---

## 客户没主动提但我们假设的需求

> 红线纪律：客户**没明说**的需求要标"假设"，让客户校准。

- **假设 1**：客户希望"自定义首页能看到哪些数据"——但 10 位客户里只有 1 位主动提，可能是低优先级
- **假设 2**：客户希望"和团队成员一起看同一个首页"——0 位主动提，可能不是真需求

---

## 我们用的工作流 / Workflow Used

1. [`customer_interview_synthesis.md`](../../workflows/research_and_analysis/customer_interview_synthesis.md) — 多份访谈合并分析
2. 提炼出 3 个高共识主题 + 2 个假设 → 进入 PRD 起草
3. 在 [`meetings/customer_interviews/`](../../meetings/) 存了完整的 10 份访谈纪要（脱敏）

---

## 教学点 / Teaching Points

- **N=1 不是洞察，是轶事**：单个客户说"X" 不能立 PRD，要看是不是反复出现
- **"客户没说的"要标"假设"**：让客户有机会校准
- **用脱敏标签**而不是真实公司名 → 红线 #3
- **多份访谈合并后才提炼共识**：不要 N=1 就开 PRD
