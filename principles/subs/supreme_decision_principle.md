---
name: 至高决策原则 / Supreme Decision Principle
description: TUZHAN 全员决策的最顶层依据，凌驾于具体红线之上 / Top-level decision basis above all specific red lines
type: permanent
retention: permanent
retention_reason: 决定其他所有规则在沉默时如何兜底 / Defines the fallback when every other rule is silent
---

# 至高决策原则 / Supreme Decision Principle

## 一句话 / One Line

> **长期主义 + 科学方法与业界标准 + 紧扣核心产品目标。**
> **Long-term thinking + scientific methods and industry standards + locked on the core product objective.**

AI 在这条原则下能自决就自决；不能时，先写建议交人决策。
Under this principle, AI decides autonomously when it can; when it cannot, it writes a recommendation and hands the call to a human.

---

## 三个要素拆开看 / The Three Elements Unpacked

### 1. 长期主义 / Long-Term Thinking

**问自己：6 个月后回看这个决定，我还会觉得它对吗？**
Ask yourself: looking back 6 months from now, would I still call this decision right?

具体反映在：
Practically:
- **不为了赶今天的进度而留下明天必修的债**。如果"现在快"和"以后稳"冲突，默认选"以后稳"。
  **Don't trade tomorrow's debt for today's speed.** When "fast now" conflicts with "stable later", default to "stable later".
- **命名按 6 个月后的人也能看懂的标准**。`tmp_v2_final.py` 是反例。
  **Name things so a future reader 6 months out can understand.** `tmp_v2_final.py` is the anti-pattern.
- **架构选择默认偏保守、可演进**。新潮的轮子 / 还没普及的协议先观望，让别的团队踩坑两年再考虑。
  **Architecture defaults to conservative and evolvable.** Trendy frameworks / nascent protocols → wait two years and let others step on the mines first.
- **文档不是给今天的自己写，而是给明年的新同事写**。
  **Docs aren't for today-you; they're for next-year's new colleague.**

### 2. 科学方法与业界标准 / Scientific Methods and Industry Standards

**问自己：这件事大公司 / 业界标杆是怎么做的？为什么我要做不一样的？**
Ask yourself: how do industry leaders do this? Why am I doing it differently?

具体反映在：
Practically:
- **优先复用已经在业界被验证的方案**（PRD 驱动、ADR、SSOT、回归测试、code review、A/B 测）。不要自创流派。
  **Reuse industry-validated patterns** (PRD-driven, ADR, SSOT, regression tests, code review, A/B testing). Don't invent your own school of thought.
- **决策时引用数据 / 案例 / 文献**，不引用"我感觉"。
  **Cite data, cases, sources** when deciding — not "I feel like".
- **不熟的领域先 Google + 看一两篇业界博客（10-30 分钟）再下结论**。
  **In unfamiliar territory, spend 10-30 min on Google + 1-2 industry blog posts before concluding.**
- **如果 AI 给你一个看似新颖的方案，问它"业界普遍是怎么做的？为什么不这么做？"**。AI 常常会编出听起来漂亮但实际上没人这么干的设计。
  **If AI hands you a novel design, ask "what's the industry default? Why not that?"** AI often invents pretty designs nobody actually uses.

### 3. 紧扣核心产品目标 / Locked on the Core Product Objective

**问自己：这件事和我们今年最重要的目标的距离有多远？**
Ask yourself: how far is this from our top objective for the year?

具体反映在：
Practically:
- **拒绝看起来酷但偏离主线的功能 / 重构 / 优化**。冷静评估 ROI。
  **Refuse cool-but-off-mainline features / refactors / optimizations.** Calmly assess ROI.
- **每周复盘时，列出本周做的事，按"距离核心目标多远"打分**。低分的事下周减少。
  **In weekly reviews, score each item by "distance from core objective". Reduce low-score items next week.**
- **AI 给你的方案如果跑偏了，立即拉回来**：「这件事虽然技术上很合理，但和我们今年要做的'X'没关系，先放一边」。
  **If AI drifts off-objective, pull back immediately**: "Technically reasonable, but unrelated to our 'X' goal — set aside."

---

## "AI 能自决就自决"的边界 / Where AI Can Decide Autonomously

**可以自决（不必每次问）：**
**OK to decide (no need to ask):**
- 命名一个新变量 / 函数 / 文件 / Naming a new variable, function, file
- 选用什么数据结构 / 什么算法 / Choosing data structures, algorithms
- 在已有风格下加注释或重构内部实现 / Adding comments or refactoring implementation within existing style
- 修单元测试以匹配修复后的行为 / Updating unit tests to match the fixed behavior
- 在工作流文档里加一段说明 / Adding a note to a workflow document
- 从模板里挑一个最贴合的填 / Picking the closest template

**必须先写建议交人决策（不要自决）：**
**Write a recommendation, don't decide:**
- 引入新依赖 / 新框架 / 新外部服务 / Adding a new dependency, framework, external service
- 修改红线本身 / 修改 `principles/` 下任何文件 / Editing the red lines themselves or any file under `principles/`
- 改变数据库 schema / API 契约 / Changing DB schema or API contract
- 删除任何已有的功能（哪怕你觉得它没用）/ Deleting any existing feature (even if you think it's unused)
- 涉及钱、客户数据、合同、上下游协议 / Anything involving money, customer data, contracts, upstream/downstream agreements
- 影响超过 3 个职能（销售/运营/产品/开发/视频）的事 / Anything touching > 3 functions

判断不准时：**默认问人**。问的代价远低于猜错的代价。
When uncertain: **default to ask**. The cost of asking is far below the cost of guessing wrong.

---

## "写建议交人决策"是什么样子 / What "Write a Recommendation" Looks Like

**反例（不要这样问）/ Anti-pattern (do not ask like this):**
> 我应该用 React 还是 Vue？

**正例（这样问）/ Right pattern:**
> 关于前端框架选型，我倾向 **React**，理由：
> 1. 团队 3 位开发里 2 位用过 React，1 位用过 Vue —— 上手成本 React 更低。
> 2. 行业招聘里 React 候选人池大约是 Vue 的 4 倍 —— 两年后扩团队更容易。
> 3. 我们的目标是在 2026 Q3 前把客户后台做出来，主要是表格 + 表单 + 仪表盘 —— 两个框架都能做，差异不大。
>
> 但 Vue 在国内中小厂普及度更高，如果之后要找外包补人手，Vue 池子更近 —— 这个**只有你（人）知道我们未来是不是会走外包路线**，所以最终请你拍板。

差别：
The difference:
- 反例把决策权完全甩回去 / The anti-pattern dumps the decision back wholesale
- 正例已经做了 80% 的功课，留 20%（人独有的信息）让人来定 / The right pattern does 80% of the homework, leaves the 20% only the human can supply

---

## 当原则和某条具体红线冲突时 / When This Principle Conflicts with a Specific Red Line

**具体红线优先**。
**The specific red line wins.**

理由：每条具体红线都是从过去的真实失败里换来的；至高原则是"红线没明说时怎么办"的兜底，不是凌驾红线的特权。
Reason: each specific red line was paid for with a real past failure; the supreme principle is the **fallback** when red lines are silent, not a license to override them.

如果你（人）觉得某条具体红线和长期主义反了——按红线 #2（红线如何演进）的流程**改那条红线**，不要在某次任务里偷偷绕过去。
If you (the human) feel a specific red line contradicts long-term thinking — go through the **red-line-evolution flow** (see `000_CORE_RED_LINES.md` Chapter 2). Don't quietly bypass it in one task.

---

## 实战例子 / Worked Examples

### 例子 1：客户要"今天就上线一个功能" / Example 1 — Customer wants a feature live today

应用至高原则：
- 长期：今天硬上的功能，明天可能要回滚，伤客户更深 → 反对硬上
- 业界标准：紧急需求走 hotfix 流程，要有最小测试 + rollback 计划 → 提议走 hotfix
- 核心目标：这个功能和我们 Q3 主线目标的关系？如果无关，能不能下周再做？

回给客户的话：
> 我们理解紧急性。今天上线的代价是【列出真实代价】。建议方案：(a) 今晚 22:00 上 hotfix（含最小测试 + rollback），(b) 明天上午先用人工兜底服务这个客户。

### 例子 2：AI 给你一个"全新设计模式" / Example 2 — AI proposes a "novel design pattern"

应用至高原则：
- 业界标准：业界普遍是怎么做的？AI 的方案为什么不一样？
- 让 AI 回答："业界默认方案是 X，我提议 Y 是因为 Z。"
- 如果 Z 站不住脚（"我觉得更优雅"），回到业界默认 X。

### 例子 3：内部讨论"要不要引入 SPEC 框架" / Example 3 — Internal debate "should we adopt SPEC framework"

应用至高原则：
- 长期：未普及的工具引进来要承担锁定成本，6 个月后还活着的概率？
- 业界标准：业界标杆里有几家在用？头部公司用什么？
- 核心目标：用了它能解决我们今年要解决的问题吗？还是只是显得"先进"？

得出结论的形式：写一份 ADR 落字到 [`meetings/`](../../meetings/)。哪怕结论是"暂不引入"，也写下来——这样下次有人重提，就不必从零讨论。
Output an ADR into [`meetings/`](../../meetings/). Even if the conclusion is "defer", write it — so next time someone re-raises, you point at the ADR instead of re-debating from scratch.

---

## 这条原则不是用来背的 / This Principle Is Not for Memorization

它是用来**遇到模糊地带时回头默念一遍**的。
It's for **silently reciting** when you hit ambiguity.

工作中 95% 的事不需要回到这条原则——按红线和工作流就够了。剩下 5% 当工作流没覆盖时，问自己这三个问题：
95% of work doesn't need this principle — red lines and workflows suffice. The remaining 5% (when workflows don't cover it), ask the three questions:

1. 6 个月后回看这个决定，我还会觉得它对吗？
2. 业界标杆是怎么做的？我做不一样的理由是不是站得住？
3. 这件事和我们今年最重要的目标的距离有多远？

三个问题都答得了，就动手。答不了，就问人。
If you can answer all three → act. If not → ask a human.
