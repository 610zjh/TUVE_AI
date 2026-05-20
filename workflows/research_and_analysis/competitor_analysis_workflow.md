# 竞品分析 / Competitor Analysis Workflow

> 适用：销售、产品、运营要回答"我们和 [对手] 比怎么样"。
> For: when you need to answer "how do we compare to [competitor]".

---

## 一句话 / One Line

**竞品分析不是"列对手特性表"，是"回答我们应该如何在 3 个月内胜过他们的关键指标"。**
**Competitor analysis isn't "feature matrix dumps"; it's "how we beat them on key metrics in 3 months".**

---

## 5 维度框架 / 5-Dimension Framework

任何一份有用的竞品分析回答这 5 个问题：
A useful competitor analysis answers these 5:

| 维度 / Dimension | 问题 / Question |
|---|---|
| 1. 价值主张 / Value Prop | 对手对客户**承诺**什么？我们承诺什么？差异在哪？|
| 2. 实际兑现 / Actual Delivery | 对手实际**做到**什么程度？（看客户真实评价、流失率、投诉率）|
| 3. 价格 + 商业模式 / Pricing + Model | 对手怎么收费？我们怎么收费？同等价值下谁更便宜？|
| 4. 客户群 / Customer Base | 对手的客户长什么样（行业 / 规模 / 地域）？我们的呢？重叠区在哪？|
| 5. 不可被复制的优势 / Defensible Edge | 对手有哪些我们抄不来的（数据、网络效应、品牌、专利）？我们有哪些他们抄不来？|

---

## 用 AI 协助的 4 步 / 4 Steps with AI

### 步 1：列出对手清单 / Step 1: Identify Competitors

不只是"业内龙头"。还要：
Not just "industry leaders". Also:
- **直接对手**：解决同样问题的同类产品 / Direct: same product, same problem
- **间接对手**：用不同方式解决同样问题 / Indirect: same problem, different way
- **替代品**：客户没买你和对手时怎么办（Excel？人工？）/ Substitutes: what customers do without you or competitor

```
我们公司是 [公司+产品+目标客户]。请帮我列：
- 5 个直接对手
- 5 个间接对手
- 3 个客户最常见的"替代方案"

每个标出：知名度（高/中/低）、和我们的客户重叠程度（高/中/低）。
```

### 步 2：收集对手公开信息 / Step 2: Gather Public Info

公开信息源：
Public sources:
- 官网（产品页、定价页、客户案例）/ Website
- 应用商店评价 / App store reviews
- 行业报告（带具体数字的，不是营销稿）/ Industry reports with real numbers
- 客户主动反馈（Reddit / 知乎 / 小红书 / 行业群）/ Customer-generated content
- 财报（如果是上市公司）/ Filings if public

**不**要做的：
**DO NOT**:
- 在不脱敏的情况下让 AI"调用对手的产品"——可能违反对手 ToS
- 让员工以假名注册对手账号刺探——商业道德 + 合规风险
- 直接挖对手的人然后问内部信息——同样

### 步 3：让 AI 帮你做对照表 / Step 3: AI-Drafted Comparison Table

```
基于上面收集的信息，做一份对照表：

行 = 5 维度框架的 5 个问题
列 = 对手 1, 对手 2, 对手 3, 我们

每个单元格 ≤ 30 字。如果某格填不出来，标 [需要更多研究]。
不要为了"看起来完整"而捏造内容。
```

### 步 4：写出"我们的 3 个月行动" / Step 4: Translate to 3-Month Action

```
基于上面的对照表，回答：

1. 我们当前在哪 3 个维度上明显输给对手？
2. 这 3 个维度里，3 个月内能改变多少的是哪一个？
3. 改变这一个，需要哪些具体动作（含负责人和 ETA）？

列出 top-3 行动项。
```

---

## 红线提醒 / Red Line Reminders

- **不要在客户面文案里点名对手**（红线 #2 + 法律风险）/ Don't name competitors in customer-facing copy
- **不要用对手名字作为内部代号**（容易在客户面字里漏出来）/ Don't use competitor names as internal codes
- **客户告知里要说"行业其他玩家"**而不是具体名字 / Use "other players in the industry", not specific names

---

## 谁来做 / Who Does It

| 频率 / Cadence | 谁 / Who | 输出 / Output |
|---|---|---|
| 每周 / Weekly | 销售+运营各一位"竞品观察员" | 5 维度的小变化日志 |
| 每月 / Monthly | 产品 + 销售联合 | 月度竞品快照（更新对照表） |
| 每季度 / Quarterly | 产品负责人主导 | 完整竞品报告（5 维度深挖 + 3 个月行动） |
| 重大事件 / Major events | 即时（如对手大型产品发布、融资）| 应急响应（24 小时内出对策） |

存到 [`meetings/competitor/`](../../meetings/) 下。
Save under `meetings/competitor/`.

retention class = `permanent`（公司战略素材）/ permanent (company strategy material).

---

## 反模式 / Anti-Patterns

### 反模式 1：列特性表 = 完了 / List = Done

❌ 一张大特性表（"对手有 X 我们没"），就当作分析。

**问题**：特性表只回答了维度 1（价值主张）的一半。维度 2-5 都没碰。

**修正**：5 维度都过一遍。

### 反模式 2：被对手节奏带走 / Reactive to Competitor

❌ 对手发了一个新功能，我们立刻动员全部资源做同样的功能。

**问题**：对手做某个功能可能因为他们的客户结构和你不一样。盲目对标 = 失去自己的方向。

**修正**：对手发新功能时，先问"我们的客户**也**需要这个吗？"，不是"对手有，我们就要有"。

### 反模式 3：贬低对手 / Trash Talk

❌ "对手的 X 烂得很，我们随便都能赢。"

**问题**：(1) 客户不一定这么觉得 (2) 让团队失去警觉 (3) 在客户面前说出来违反红线 #2 / 法律风险

**修正**：客观陈述对手的优劣，让数据说话。

---

## 速查 / Cheat Sheet

```
5 维度：价值主张 / 实际兑现 / 价格 / 客户群 / 不可复制的优势

每个对手填 5 维度，用 AI 帮做对照表。
然后回答"我们 3 个月内能改变的 1 个维度是哪个"。

不要：列完特性表就当完成；被对手带节奏；贬低对手。
要：客观对比；找到自己的差异化；落实到具体行动。
```
