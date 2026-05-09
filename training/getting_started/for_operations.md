# for_operations · 运营 / 产品运营 / 活动运营

> 你今天打开仓库后的 5 分钟开局指引。
> Your first 5 minutes as an operations / product-ops / campaign-ops person.

---

## §1 你是谁 / 今天可能在做什么 / Who You Are & Today's Likely Work

你是 TUZHAN 短视频 AI Agent 团队的运营。本周高频场景：

1. 活动策划（节点 / 日常 / 裂变）
2. 用户运营（社群 / 用户分层 / 召回）
3. SOP 维护（[`runbooks/`](../../runbooks/)）
4. 周报（指标 + 主要动作 + 下周计划）
5. 跨部门协调会准备

---

## §2 第一次和 AI 的对话 / Your First AI Conversation

把下面整段复制给 AI（替换 `<...>` 处）：

```
请先读 AI_MANUAL.md。我是运营，今天要起 <一个活动> 方案：1 页背景 + 玩法 + 数据指标 + 风险预案。所有用户名单 / 真实指标已脱敏。先列你不确定的点。涉及对外活动文案的部分按红线 #2 自查（不出现内部代号 / PRD 编号）。

Read AI_MANUAL.md first. I'm in ops. Today: draft a plan for <campaign> — 1 page background + mechanics + metrics + risk plan. User lists / real metrics redacted. List unknowns. Self-check rule #2 for all customer-facing copy (no internal codenames / PRD IDs).
```

---

## §3 本周可以先用的 3 个工作流 / 3 Workflows to Start With

- [`workflows/operations/weekly_ops_review.md`](../../workflows/operations/weekly_ops_review.md) — 周报；模板 [`templates/weekly_review/`](../../templates/weekly_review/)
- [`workflows/operations/ops_runbook_authoring.md`](../../workflows/operations/ops_runbook_authoring.md) — 写 / 改 SOP
- [`workflows/planning/meeting_prep_with_ai.md`](../../workflows/planning/meeting_prep_with_ai.md) — 跨部门会前准备

---

## §4 三个新手最常踩的坑 / 3 Common Pitfalls

1. **活动文案 / 推送文案出现内部代号 / 真实模型名**：越红线 #2，特别是裂变海报 / 弹窗 / push 推送这类高曝光位。
2. **用户名单 / 用户行为数据未脱敏喂 AI**：越红线 #3，社群运营经常踩这个。导出 CSV 前先看是否含手机号 / 真实姓名。
3. **直接用 AI 改 [`workflows/`](../../workflows/) / [`runbooks/`](../../runbooks/)**：越红线 #5——任何流程类改动先起 PRD 再改文件。**禁止**让 AI 在没有 PRD 时直接改 SOP。

---

## §5 下一步 / Next

- 卡住了 → [`common_obstacles.md`](common_obstacles.md)
- 学完想深入 → [`what_next.md`](what_next.md)
- AI 协作基础 → [`workflows/ai_basics/`](../../workflows/ai_basics/)
- 运营完整工作流 → [`workflows/operations/`](../../workflows/operations/)
