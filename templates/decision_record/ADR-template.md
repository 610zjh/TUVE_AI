# ADR-NNNN: <一句话标题，含动词 / one-line title with verb>

> 复制这份模板，存到 `workspace_human/meetings/adr/ADR-NNNN_短标题.md`。
> Copy this template, save to `workspace_human/meetings/adr/ADR-NNNN_short_title.md`.

- **时间 / Date**: 2026-XX-XX
- **决策人 / Decided by**: <具体姓名，不许写"我们"/"团队">
- **状态 / Status**: Proposed | Accepted | Superseded by ADR-MMMM | Deprecated

---

## 1. 背景 / Context

<触发这个决策的事是什么？目前的状态？为什么现在决策？>
<2-3 段话，让 6 个月后的人能复原情境>

---

## 2. 选项 / Options Considered

### 选项 A: <一句话描述>
- 优点 / Pros:
  - ...
  - ...
- 缺点 / Cons:
  - ...
  - ...
- 实施成本估算：<人天 / 成本量级 / 时间>

### 选项 B: <一句话描述>
- 优点 / Pros: ...
- 缺点 / Cons: ...
- 实施成本估算：...

### 选项 C（可选）: ...

---

## 3. 决策 / Decision

我们选 **<X>**。

### 理由 / Reasoning

1. **长期主义角度**: <为什么选 X 在 6 个月 / 1 年 / 5 年后看仍然合理>
2. **业界标准角度**: <X 是不是业界普遍做法？我们偏离的代价是什么？>
3. **核心目标角度**: <X 怎么直接服务我们当前的核心产品目标>

（至少援引 3 个支柱中的 1 个，最好 2 个以上 —— 见 [`principles/subs/supreme_decision_principle.md`](../../principles/subs/supreme_decision_principle.md)）

---

## 4. 后果 / Consequences

### 正面 / Positive
- ...

### 负面（被取舍掉的部分）/ Tradeoffs
- 选了 X 意味着我们放弃 ...
- 短期 / 长期分别失去 ...

### 复评触发条件 / When to Re-review

- [ ] 当 [具体可观测的事] 发生时，回头评估这个决策是否还成立
- [ ] 默认每年 1 月例行复评

---

## 5. 关联 / Related

- 关联 PRD：[PRD-XXXX](../../prd/) （如适用）
- 关联 Bug：B-XXXX-XX（如适用）
- 推翻了 / Supersedes：ADR-MMMM（如有）
- 被推翻 / Superseded by：ADR-LLLL（如有）

---

## 状态变更日志 / Status History

- 2026-XX-XX 由 [name] 起草，状态 Proposed
- 2026-XX-XX 状态变为 Accepted

---

## 注：追溯型 ADR 的特殊段（如适用）/ Retroactive ADR Note (if applicable)

> 如果这是为已经发生但当时没落字的决策**追溯补写**的：
> If this was retroactively written for a past decision:

```markdown
## 注：此 ADR 为追溯补写
- 实际决策时间：约 2026-XX-XX (estimated)
- 追溯补写时间：2026-MM-DD by [name]
- 原因：当时未落字。现在补写以保留决策历史。
- 部分细节可能已记不准。我已尽力诚实重建。
```
