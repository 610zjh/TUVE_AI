---
name: 决策与记录 / Decisions and Records
description: 什么样的决定必须落字成 ADR、ADR 怎么写、什么时候补、什么时候推翻 / What must be written as an ADR, how to write one, how to revise
type: permanent
retention: permanent
retention_reason: 防止"这个决定是谁拍的，为什么这么拍"成为半年后的悬案 / Prevents "who decided X, why?" from becoming an unsolvable mystery 6 months later
---

# 决策与记录 / Decisions and Records

## 一句话 / One Line

**口头共识不算数，落字才算数。**
**Verbal consensus doesn't count. Written record does.**

不是官僚主义。是为了让你 6 个月后回来还能搞清楚自己当时为什么这么做。
Not bureaucracy. So future-you, 6 months later, can still tell why this call was made.

---

## 什么算"非平凡决策" / What Counts as a Non-Trivial Decision

满足下面任意一条，就要落字成 ADR：
If any of the below applies, write an ADR:

1. **影响其他人**——结果会被销售 / 运营 / 视频 / 开发 / 产品里 ≥ 1 个其他职能用到
   **Affects others** — outcome touches ≥ 1 other function (sales / ops / video / dev / product)
2. **涉及取舍**——选了 A 就放弃了 B 的某些好处
   **Involves a tradeoff** — picking A means giving up B's benefits
3. **难以撤销**——做了再改要付额外成本（不止改一次代码、不止重发一封邮件）
   **Hard to undo** — reverting incurs more than a single code change or re-send
4. **后续可能被追问"为什么"**——半年后有人会问"当初为什么这么定？"
   **May be challenged later** — somebody will ask "why this way?" 6 months out

如果都不满足，是日常微决策，不必落字。
If none applies, it's a routine micro-decision; no record needed.

---

## ADR（Architecture Decision Record）格式 / ADR Format

```markdown
# ADR-NNNN: <一句话标题，含动词>

- 时间 / Date: 2026-XX-XX
- 决策人 / Decided by: <姓名 / Name>
- 状态 / Status: 提出 / 采纳 / 已推翻 / 已废弃 (Proposed / Accepted / Superseded / Deprecated)

## 背景 / Context
触发这个决策的事是什么？目前的状态是什么？为什么要决策？
What triggered this decision? Current state? Why decide now?

## 选项 / Options
- 选项 A：... 优点 ... 缺点 ...
- 选项 B：... 优点 ... 缺点 ...
- 选项 C（可选）：...

## 决策 / Decision
我们选 <X>，因为 <理由 1, 2, 3>。
We chose <X> because <reason 1, 2, 3>.

## 后果 / Consequences
- 选了 X 之后会发生 ... / What happens after X
- 我们放弃的 ... / What we gave up
- 未来需要复评的触发条件 / When to re-review

## 关联 / Related
- 关联 PRD：[PRD-XXXX](path)
- 关联 Bug：...
- 推翻了 / 被推翻：ADR-NNNN
```

模板见 [`templates/decision_record/`](../../templates/decision_record/)。
Template at [`templates/decision_record/`](../../templates/decision_record/).

---

## ADR 编号规则 / ADR Numbering

- 全公司**统一连续编号**，不分部门 / Company-wide single sequence, no per-team numbering
- 编号一旦分配不复用，即使 ADR 被废弃 / Numbers never reused, even if ADR is deprecated
- 文件名格式：`ADR-NNNN_短标题.md`，存在 [`workspace_human/meetings/`](../../workspace_human/meetings/) 下 / File name `ADR-NNNN_short_title.md` under [`workspace_human/meetings/`](../../workspace_human/meetings/)

---

## 状态生命周期 / Status Lifecycle

```
Proposed ──> Accepted ──> Superseded by ADR-XXXX
                  │
                  └─> Deprecated（不再推翻，只是过时了）
```

- **Proposed**：写好了在征求意见 / Drafted, in review
- **Accepted**：决定落地，按这个执行 / Adopted, follow this
- **Superseded**：被一份**新的 ADR** 改写。**旧 ADR 不删，标 superseded by ADR-XXXX** / Replaced by a **new ADR**. **Don't delete the old one; mark "superseded by ADR-XXXX"**
- **Deprecated**：背景已经不存在了，没人推翻它，自然过时 / Context no longer exists; obsoleted without explicit replacement

为什么旧 ADR 不删：6 个月后有新人看历史，需要看到"我们曾经有过这个共识，是怎么演化到今天的"。
Why old ADRs aren't deleted: future readers need the **lineage**, not just the latest snapshot.

---

## 写 ADR 的常见错误 / Common Mistakes Writing ADRs

### 错误 1：把"决策"写成了"记录" / Mistake 1 — Writing a record, not a decision

❌ "今天的会上我们讨论了 X，最终大家都觉得 Y 不错。"
**问题**：没有"为什么 Y 不另外两个候选"的对比，没有"放弃了什么"的清单，没有"未来什么情况要复评"的触发条件。
**Issue**: no comparison vs alternatives, no listing of what was given up, no re-review trigger.

✅ 正确：明确写选项 A/B/C 的优缺点，写"为什么选 Y 不选 X 和 Z"，写"什么时候我们应该回来重新看这个决定"。
**Right**: explicit A/B/C comparison, explicit reasoning, explicit re-review trigger.

### 错误 2：写得太抽象 / Mistake 2 — Too abstract

❌ "为了提升效率，我们决定优化流程。"
**问题**：6 个月后没人能从这句话里复原当时的具体讨论。
**Issue**: nobody can reconstruct the original context from this sentence.

✅ 正确：具体到"原本走人工审核每周耗 4 小时；改后走半自动 + 人工抽查每周耗 1 小时；放弃了对 A 类边角案例的全覆盖"。
**Right**: concrete metrics, concrete tradeoff, concrete scope.

### 错误 3：决策人写"我们" / Mistake 3 — "We" as decider

❌ "Decided by: 我们"
**问题**：没有责任人；半年后出问题没人能负责。
**Issue**: no accountable party; nobody to answer if it backfires.

✅ 正确：写一个具体的人名（即使决策是集体讨论后形成的，也由一个人代表落字）。
**Right**: write an actual name (even if collectively discussed, one person owns the writing).

### 错误 4：缺"放弃了什么" / Mistake 4 — Missing "what we gave up"

❌ 只写了"我们选 A，理由 1/2/3"。
**问题**：取舍是 ADR 的核心。如果没"放弃了什么"，这不是决策，是单选题。
**Issue**: tradeoff is the core of an ADR. Without "what we gave up", it's not a decision, it's a single-choice question.

✅ 正确：明写"选 A 意味着我们短期内不能做 B 的某些功能；如果未来 B 的需求增长到 X，需要回来重评"。
**Right**: explicitly state what you sacrificed and the threshold to revisit.

---

## 决策落字 vs 不落字的临界判断 / Tipping Point: Write or Skip?

| 情境 / Situation | 落字 / Write? |
|---|---|
| 决定下周一全员去客户现场而不是远程开 / Decide to go on-site Monday instead of remote | ❌ 不必（执行性安排）/ No (logistics) |
| 决定不接一个客户 / Decide to walk away from a customer | ✅ 落 ADR / Yes |
| 决定下一支视频用 60 秒而不是 90 秒 / Decide next video is 60s not 90s | ❌ 不必（创作选择）/ No (creative choice) |
| 决定**所有**视频统一改成 60 秒上限 / Decide **all** videos shall be ≤60s going forward | ✅ 落 ADR / Yes |
| 决定 Bug 这周不修，先排到下周 / Decide a bug doesn't get fixed this week | ❌ 不必（[`issues/known.md`](../../issues/known.md) 里登记就够）/ No (issues/known.md suffices) |
| 决定不修这一类 Bug（永久作为 wontfix 处理）/ Decide a class of bugs is permanently won't-fix | ✅ 落 ADR / Yes |
| 决定面试时多加一个轮次 / Decide to add an interview round | ⚠️ 看影响范围 / Depends on scope |
| 决定改公司 OKR 的某条 / Decide to amend a company OKR | ✅ 落 ADR / Yes |

口诀：**会变成"一类事的处理范式"的，落字；只解决"这一次"的，不必。**
Heuristic: **if it becomes a pattern for handling a class of cases, write it. If it solves "this one time", skip.**

---

## ADR 与 PRD 的边界 / ADR vs PRD Boundary

- **PRD** 描述**要做什么**——产品需求 / What we're going to build
- **ADR** 描述**为什么这么做**——决策与取舍 / Why we chose this path

二者**互相引用**，不互相替代。
They cross-reference, not replace each other.

一个 PRD 可能催生 0 到多个 ADR——做这个 PRD 期间冒出的取舍点都可以是 ADR 候选。
A PRD spawns 0+ ADRs — every tradeoff during execution is an ADR candidate.

---

## 已经做了的事但当时没写 ADR 怎么办 / Retroactive ADRs

发现某个决定在两个月前定了但没落字 → 现在补一份"追溯型 ADR"。
If you find a decision was made 2 months ago without an ADR → write a "retroactive ADR" now.

格式上加一段：
Add a section:

```markdown
## 注：此 ADR 为追溯补写 / Note: Retroactive ADR
- 实际决策时间：2026-XX-XX（约）/ Actual decision date: ~2026-XX-XX
- 补写时间：2026-MM-DD / Retroactively written: 2026-MM-DD
- 原因：当时未落字。当前补写以保留决策历史。/ Reason: not recorded at the time. Recorded now to preserve decision history.
```

不要假装它是当时写的。诚实标注追溯。
Don't pretend it was written at the time. Honestly mark it retroactive.

---

## ADR 是不是越多越好 / More ADRs = Better?

不是。
No.

ADR 的价值在于"被读到 + 救了一次"。如果你写了 50 份 ADR 但没人读，等于你**写了一份索引混乱的目录**。
The value of ADRs is "got read and saved someone once". 50 ADRs nobody reads is **a chaotic index of nothing**.

每写一份，问自己：
For each one ask:
- 这份决策值不值得 6 个月后的人翻出来？/ Worth being unearthed 6 months later?
- 它有没有具体到"放弃了什么、复评条件是什么"？/ Concrete enough on tradeoffs and re-review?
- 它编号清楚、文件名清楚、能被搜到吗？/ Numbered, named, searchable?

三个都"是"，写。三个里有"否"，先把它修到三个都"是"。
Three yeses → write. Any no → fix it first.
