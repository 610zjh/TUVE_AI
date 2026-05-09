# for_product · 产品经理

> 你今天打开仓库后的 5 分钟开局指引（PRD / ADR / 跨职能对齐）。
> Your first 5 minutes as a product manager.

---

## §1 你是谁 / 今天可能在做什么 / Who You Are & Today's Likely Work

你是 TUZHAN 短视频 AI Agent 团队的产品经理。本周高频场景：

1. 写新 PRD（[`workspace_human/prd/`](../../workspace_human/prd/)）
2. 跨职能对齐（产品 / 设计 / 开发 / 数据）
3. 决策落字成 ADR（红线 #6）
4. 需求验收（拿成果对照 PRD §5 验收标准）
5. 周复盘（路线图调整）

---

## §2 第一次和 AI 的对话 / Your First AI Conversation

把下面整段复制给 AI（替换 `<...>` 处）：

```
请先读 AI_MANUAL.md 和 workflows/planning/writing_a_prd.md。我是产品经理，今天要起 PRD-<XXXX> 草稿：<一句话需求>。先：1) 列你不确定的点（不许硬填业务背景），2) 按 templates/prd/PRD-template.md 给一份骨架。等我给你真实业务背景再填内容。注意：你不许直接修改 workspace_human/prd/ 下的文件——红线 #12。

Read AI_MANUAL.md and workflows/planning/writing_a_prd.md first. I'm PM. Today: draft PRD-<XXXX> for <one-line requirement>. First: 1) list unknowns (no guessing business context), 2) skeleton per templates/prd/PRD-template.md. Wait for my real context before filling. Note: don't modify workspace_human/prd/ files — rule #12.
```

---

## §3 本周可以先用的 3 个工作流 / 3 Workflows to Start With

- [`workflows/planning/writing_a_prd.md`](../../workflows/planning/writing_a_prd.md) — 写 PRD；模板 [`templates/prd/`](../../templates/prd/)
- [`workflows/decision_records/how_to_write_an_adr.md`](../../workflows/decision_records/how_to_write_an_adr.md) — 决策落字；模板 [`templates/decision_record/`](../../templates/decision_record/)
- [`workflows/planning/breaking_down_a_project.md`](../../workflows/planning/breaking_down_a_project.md) — 大项目拆里程碑

---

## §4 三个新手最常踩的坑 / 3 Common Pitfalls

1. **让 AI 直接改 [`workspace_human/prd/`](../../workspace_human/prd/) 下的文件**：越红线 #12。AI 只能在 §10 实施记录追加。改 §1-§9 由人完成。
2. **PRD 含真实客户名 / 合同金额 / 模型 endpoint**：越红线 #3。客户面摘要 / 演示文档外发前再过一遍红线 #2。
3. **ADR 写"我做了什么决策"而不是"我为什么这么决策"**：决策依据缺失 = 6 个月后没人能追溯（红线 #6）。AI 帮你写时让它**逐条**列"选项 / 选择 / 理由"。

---

## §5 下一步 / Next

- 卡住了 → [`common_obstacles.md`](common_obstacles.md)
- 学完想深入 → [`what_next.md`](what_next.md)
- AI 协作基础 → [`workflows/ai_basics/`](../../workflows/ai_basics/)
- 规划与决策完整工作流 → [`workflows/planning/`](../../workflows/planning/) + [`workflows/decision_records/`](../../workflows/decision_records/)
