# 写一份 PRD / Writing a PRD

> 适用：产品经理、项目负责人、提需求方。AI 可以协助起草，但**人是 PRD 的责任人**。
> For: product managers, project owners, requesters. AI can help draft, but **humans own PRDs**.

---

## 一句话 / One Line

**PRD 不是文档，是合同。** 它把"我们要做什么"用大家能复核的方式写下来，让今天的承诺 6 个月后还能被验证。
**A PRD is not a document; it's a contract.** It writes down "what we're going to build" in a verifiable form so today's commitment can be checked 6 months later.

---

## 一份好 PRD 的 8 个标准 / 8 Standards of a Good PRD

1. **背景**：6 个月后的人能从背景段读懂"为什么当时要做这件事" / Future readers can tell "why we did this" from the Context section alone
2. **目标**：每条目标可被测量（不是"提升用户满意度"，是"在 v1.2 上线后 30 天内，付费档客户主动续费率从 X% 升到 Y%"）/ Each goal is measurable
3. **非目标**：明确写"不做什么"，防止范围漂移 / Explicit non-goals, prevents scope drift
4. **用户故事**：3-5 个具体用户在具体场景下的具体需求 / 3-5 specific users in specific scenarios with specific needs
5. **验收标准**：每条标准是"可以勾选 ✅ / ❌"的，不是"系统应该好用" / Each criterion is checkbox-style, not "system should be good"
6. **主次审视**（仅 paywall / 分层 PRD 必填）：按红线 #15，过 [`principles/subs/business_priorities.md`](../../principles/subs/business_priorities.md) §"主次审视" 流程 / Required for paywall PRDs
7. **风险 + 对策**：列 top-3 风险 + 各自的对策 / Top-3 risks + mitigations
8. **时间表**：里程碑 + 复评点（不是"看情况"）/ Milestones + re-review points

模板见 [`templates/prd/`](../../templates/prd/)。
Template at [`templates/prd/`](../../templates/prd/).

---

## 用 AI 协助起草的 5 步 / 5 Steps with AI

### 步 1：背景拼图 / Step 1: Context Assembly

```
我要给"<功能名>"起草 PRD。背景信息散在以下几处：
- 客户访谈纪要（粘贴）
- 内部讨论记录（粘贴）
- 销售反馈（粘贴）

请把这些拼成一份 PRD 的"背景"段，约 200 字。
要求：
- 6 个月后的新同事读完能搞清楚"为什么要做这件事"
- 不要捏造没有出现在材料里的事实
- 输出后，列出你最不确定的 3 个点
```

### 步 2：目标和非目标 / Step 2: Goals and Non-Goals

```
基于上面的背景，请帮我列：
- 5 个候选目标，每个都要可测量
- 5 个候选非目标（明确不做什么）

我会从中挑、改、加。
```

PM 的责任是从候选里**挑和改**。AI 的责任是把所有可能性铺出来。
PM's job is to **pick and refine** from candidates. AI's job is to spread the candidate space.

### 步 3：用户故事 / Step 3: User Stories

```
列 5-8 个用户故事，按 "作为<角色>，我希望<能力>，以便<价值>" 格式。

约束：
- <角色> 必须是真实业务里存在的角色（销售 / 运营 / 制作 / 客户某具体角色）
- <能力> 必须具体（不是"看到数据"，是"在客户后台首页直接看到本周新增内容数量"）
- <价值> 必须是用户自己感受得到的（不是"提升体验"，是"省去每次去 5 个不同页面看数据的 5 分钟"）
```

### 步 4：验收标准 / Step 4: Acceptance Criteria

```
基于目标和用户故事，列 8-12 条验收标准。

约束：
- 每条以"用户能 X / 系统在 Y 时返回 Z" 的形式
- 不要"系统应该稳定"这种没法勾的
- 每条都得能在测试服里手动验证一遍
```

### 步 5：风险与对策 / Step 5: Risks and Mitigations

```
基于上面的内容，列 top-5 风险，每个对应：
1. 风险描述
2. 发生概率（高 / 中 / 低）
3. 影响（高 / 中 / 低）
4. 对策（具体动作）
5. 触发条件（什么发生了我们就执行对策）
```

---

## 红线提醒 / Red Line Reminders

写 PRD 时必须遵守：
While writing PRDs:

- 红线 #5：改代码前必须有 PRD（**反过来不必**——不是每份 PRD 都有代码改动，行政 / 流程 PRD 也合法）/ Code requires PRD; not every PRD requires code
- 红线 #12：[`workspace_human/`](../../workspace_human/) 是 AI 只读。新 PRD 起草完成后**由人**保存到 `workspace_human/prd/PRD-XXXX_*.md`，不让 AI 自己写到那 / `workspace_human/` is AI read-only; **a human** saves the new PRD into `workspace_human/prd/`
- 红线 #15：paywall / 分层 PRD 必含"主次审视" / Paywall PRDs require "Priority Audit"
- 红线 #6：PRD 进行中冒出的取舍点要落字成 ADR 或写入 PRD 的"决策"段 / Mid-flight tradeoffs go into ADRs or the PRD's Decisions section

---

## PRD 编号规则 / PRD Numbering

- 全公司统一编号：`PRD-NNNN`（NNNN 4 位数字，从 0001 开始）/ Company-wide `PRD-NNNN`, 4 digits from 0001
- 编号一旦分配不复用 / Numbers don't recycle
- 文件名：`PRD-XXXX_短标题.md` / File name `PRD-XXXX_short_title.md`
- 由产品负责人维护下一个可用编号清单 / Product lead maintains the next-available list

---

## PRD 状态生命周期 / Status Lifecycle

```
草稿 ──> 评审中 ──> 已批准 ──> 实施中 ──> 已上线 ──> 已废弃 / 已被替代
Draft → In Review → Approved → In Progress → Shipped → Deprecated / Superseded
```

每次状态变化在 PRD 顶部加一行：
Each status change adds a line at the top:

```
- 2026-04-23 状态从「草稿」变更为「评审中」，由 [产品-Z] 推动
```

---

## 谁审阅 PRD / Who Reviews

| 影响范围 / Scope | 评审人 / Reviewers |
|---|---|
| 单部门内 / Single function | 部门主管 + 至少一位关联职能 |
| 跨部门 / Cross-functional | 各相关职能负责人 |
| 涉及客户 / 公开 / Customer-facing or public | + 法务 + 销售 |
| 涉及钱 / Money-touching | + 财务 |
| 涉及合规 / Compliance | + 合规 / 法务 |

评审时间：草稿提交后 5 个工作日内必出评审意见，不许"先压着"。
Review SLA: ≤ 5 working days after draft submitted; "let it sit" is not allowed.

---

## PRD 写得好不好的 5 个测试 / 5 Tests for "Is This PRD Good"

1. **6 个月测试**：6 个月后一位完全不熟这件事的新同事读完，能搞清楚我们当时为什么这么做、要做什么、做到什么程度算完吗？
   **6-month test**: a future colleague unfamiliar with this can understand from this PRD alone — why, what, and what done means.
2. **冷读测试**：把 PRD 给一位不在这个项目里的同事读，他能找出含糊处吗？
   **Cold-read test**: a non-project colleague spots ambiguities.
3. **5W1H 测试**：5W1H 全有吗？/ All 5W1H present?
4. **可证伪测试**：每条目标 / 验收能客观验证 ✅ 或 ❌ 吗？/ Falsifiable: each goal / acceptance verifiable as ✅ or ❌?
5. **风险显式测试**：风险段不是"风险可控"，而是具体说出 top-3 风险？/ Risks listed concretely, not "risks are manageable"?

5 个都过 → 可以提交评审。
All 5 → submit for review.

---

## 写 PRD 的常见错误 / Common PRD Mistakes

| 错误 / Mistake | 表现 / Symptom | 修复 / Fix |
|---|---|---|
| **空泛的目标** Vague goals | "提升用户体验" | 改成"在 v1.2 上线 30 天内，X 行为数从 Y 提升到 Z" |
| **缺非目标** Missing non-goals | 只写了"做什么"，没写"不做什么" | 加非目标段；防止开发顺手"扩展" |
| **验收标准不可勾** Unprovable criteria | "系统应该稳定" | 改成"P95 响应时间 < 800ms" |
| **风险都说"可控"** Hand-waved risks | "我们已经评估了风险" | 把 top-3 具体风险列出来；每个有对策 |
| **里程碑全是"X 月底"** Vague milestones | "5 月底完成" | 加"5 月底前完成 X / Y 两个 acceptance criteria 并在测试服验证通过" |
| **改了不改状态** Status not updated | 已经做了一半 PRD 状态还是"草稿" | 状态生命周期纪律 |
