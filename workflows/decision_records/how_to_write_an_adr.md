# 怎么写一份 ADR / How to Write an ADR

> 适用：所有人。任何"非平凡决策"都要落字成 ADR。
> For: everyone. Any non-trivial decision must be written as an ADR.

---

## 一句话 / One Line

**ADR 不是为了"记账"，是为了让 6 个月后的人能搞清楚"当初为什么这么决定"。**
**ADRs aren't bookkeeping; they're so future-readers can tell "why we decided this".**

---

## 标准 ADR 模板 / Standard ADR Template

```markdown
# ADR-NNNN: <一句话标题，含动词>

- 时间 / Date: 2026-XX-XX
- 决策人 / Decided by: <具体姓名，不许写"我们" / "团队">
- 状态 / Status: Proposed | Accepted | Superseded by ADR-MMMM | Deprecated

## 背景 / Context
<触发这个决策的事是什么？目前状态？为什么现在决定？>
<2-3 段话，让 6 个月后的人能复原当时情境>

## 选项 / Options
- 选项 A: <描述>
  - 优点 / Pros: ...
  - 缺点 / Cons: ...
- 选项 B: <描述>
  - 优点 / Pros: ...
  - 缺点 / Cons: ...
- 选项 C（可选）: ...

## 决策 / Decision
我们选 <X>。

理由：
1. <理由 1，对应至高原则的哪个支柱：长期主义 / 业界标准 / 核心目标>
2. <理由 2>
3. <理由 3>

## 后果 / Consequences
- 选了 X 之后会发生 ...
- 我们放弃的（被取舍掉的）...
- 未来需要复评的触发条件 / When to re-review:
  - 当 [X] 发生时，应回头看这个决策是否还成立
  - 默认每年初例行复评

## 关联 / Related
- 关联 PRD: [PRD-XXXX](path)（如有）
- 关联 Bug: [B-XXXX](path)（如有）
- 推翻了 / Supersedes: ADR-MMMM（如有）
- 被推翻 / Superseded by: ADR-LLLL（如有）
```

---

## 写好 ADR 的 5 个标准 / 5 Standards for a Good ADR

### 1. 决策人是具体姓名 / Decider Is a Specific Name

❌ "Decided by: 我们"
**问题**：6 个月后没人能负责
**修复**：写一个具体名字（即使是集体讨论也由一个人代表落字）

### 2. 选项至少 2-3 个真实候选 / At Least 2-3 Real Candidates

❌ 列了 1 个真选项 + 2 个明显不行的"陪跑"
**问题**：未来读者会看出这是"假选项分析"
**修复**：列**真的考虑过**的 2-3 个，每个都有具体优缺点

### 3. "放弃了什么"必须明写 / "What We Gave Up" Explicit

❌ 只写"我们选 A，理由 1/2/3"
**问题**：取舍是 ADR 的核心；没有"放弃了什么" = 不是决策，是单选题
**修复**：明写"选 A 意味着我们短期不能做 B，如果 B 的需求增长到 X 要回看"

### 4. 复评触发条件 / Re-Review Triggers

❌ "之后看情况"
**问题**：等于没有复评——没人会主动想起来
**修复**：写具体的触发条件
- "当客户量超过 1000 时回头看"
- "下次合同续签（2027-Q1）"
- "如果新技术 X 成熟到 Y 程度"

### 5. 援引至高原则 / Cite Supreme Principle

理由段落里至少一条对应：
At least one reason cites:
- 长期主义 / Long-term thinking
- 业界标准 / Industry standard
- 核心目标 / Core objective

详见 [`principles/subs/supreme_decision_principle.md`](../../principles/subs/supreme_decision_principle.md)。

---

## 用 AI 协助起 ADR / AI-Assisted ADR Drafting

### 步 1：背景 + 选项 / Step 1: Context + Options

```
我要决策：[一句话]。

背景：
- 当前状态：...
- 触发原因：...
- 影响范围：...

请帮我：
1. 把背景写成 2-3 段话（让 6 个月后的人能复原情境）
2. 列出 3 个真实候选选项（不要稻草人对照）
3. 每个选项的具体优劣（不是"看情况""可能"的模糊词）

约束：
- 选项的优劣要平衡，不要倾向我已有的偏好
- 优劣要量化（"快 30%""贵 2 倍"），别用"显著""明显"
```

### 步 2：自己拍板 / Step 2: You Decide

AI 不能替你决策。AI 给你 3 个选项的对比 → **你**选 → **你**写理由。
AI doesn't decide. AI gives 3-option comparison → **you** pick → **you** write reasons.

### 步 3：让 AI 帮你写"放弃了什么"+ 复评触发 / Step 3: AI Drafts Tradeoffs + Triggers

```
我决定选选项 A，理由 1/2/3 是 [...]。

请帮我写：
1. "放弃了什么" 段——选 A 意味着我们短期 / 长期失去什么
2. "复评触发条件"段——什么具体情况下我应该回头看这个决策

约束：
- 触发条件要具体可观测（"客户量过 1000"，不是"业务增长后"）
- 如果触发条件多年不可能发生，加一条"默认每年初例行复评"
```

---

## ADR 的状态生命周期 / Status Lifecycle

```
Proposed   ──→  Accepted   ──→  Superseded by ADR-XXXX
                    │
                    └─→  Deprecated（不再推翻，只是过时了）
```

- **Proposed**：起好草稿在征求意见 / Drafted, in review
- **Accepted**：已经按这个执行 / Adopted, follow this
- **Superseded**：被一份**新的** ADR 改写。**旧 ADR 不删**，标 superseded by ADR-XXXX
- **Deprecated**：背景已不存在了，自然过时

为什么旧 ADR 不删：6 个月后新人需要看到"我们曾经的共识，是怎么演化到今天的"。
Why old ADRs aren't deleted: future readers need the **lineage**.

---

## ADR 编号 + 存放 / Numbering and Location

- 全公司**统一连续编号**（不分部门）
- 编号一旦分配不复用
- 文件名：`ADR-NNNN_短标题.md`
- 存放：[`workspace_human/meetings/adr/`](../../workspace_human/meetings/) 下
- 由产品负责人 / 公司主理人维护下一个可用编号清单

---

## 速查 / Cheat Sheet

```
模板：背景 → 选项 → 决策（理由援引至高原则）→ 后果 + 复评触发 → 关联

5 标准：决策人具体名 / 至少 2-3 真选项 / 放弃了什么明写 / 复评条件具体 / 援引至高原则

AI 协助：背景 + 选项让 AI 起 → 你决定 → 让 AI 帮写放弃了什么 + 触发条件

状态：Proposed → Accepted → Superseded（旧的不删）

存：workspace_human/meetings/adr/ADR-NNNN_*.md
```
