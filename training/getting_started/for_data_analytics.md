# for_data_analytics · 数据分析

> 你今天打开仓库后的 5 分钟开局指引（增长 / 行为 / A/B / 留存）。
> Your first 5 minutes as a data analyst.

---

## §1 你是谁 / 今天可能在做什么 / Who You Are & Today's Likely Work

你是 TUZHAN 短视频 AI Agent 团队的数据分析师。本周高频场景：

1. A/B 实验报告（含显著性 + 业务解释）
2. 漏斗诊断 / 留存分析
3. 行为聚类 / 用户画像
4. 数据周报（指标 + 异动 + 归因）
5. 配合产品 / 增长出实验设计

---

## §2 第一次和 AI 的对话 / Your First AI Conversation

把下面整段复制给 AI（替换 `<...>` 处）：

```
请先读 AI_MANUAL.md。我是数据分析师，今天要为 <一个 A/B 实验> 起报告框架：实验设计 + 主指标 + 守护指标 + 解读模板。所有原始数据 / 真实指标已脱敏，我不会把用户行为日志贴给你。先列你不确定的点。注意：你给我的是"分析框架 + 验数据合理性建议"，不是"业务决策"——决策由人来做（红线 #6 决策依据 ≠ 决策）。

Read AI_MANUAL.md first. I'm a data analyst. Today: draft an analytics framework for <A/B test> — design + primary metrics + guardrails + readout template. Raw data / real numbers redacted; I won't paste user behavior logs. List unknowns. Note: you give me "analysis framework + sanity-check suggestions", not "business decisions" — decisions are mine (rule #6: rationale ≠ decision).
```

---

## §3 本周可以先用的 3 个工作流 / 3 Workflows to Start With

- [`workflows/research_and_analysis/data_summarization_workflow.md`](../../workflows/research_and_analysis/data_summarization_workflow.md) — 数据汇总 / 周报
- [`workflows/planning/weekly_review_routine.md`](../../workflows/planning/weekly_review_routine.md) — 周复盘
- [`workflows/decision_records/how_to_write_an_adr.md`](../../workflows/decision_records/how_to_write_an_adr.md) — 实验结论落字成 ADR

---

## §4 三个新手最常踩的坑 / 3 Common Pitfalls

1. **原始用户行为数据 / 用户 ID / 设备号贴 AI**：越红线 #3。BI 工具默认导出格式经常含 PII——脱敏 / 抽样 / 聚合后再用，规则见 [`principles/subs/confidentiality.md`](../../principles/subs/confidentiality.md)。
2. **BI 截图含内部表名 / 字段名 / 内部数据源名进客户面 / 演示文档**：越红线 #2。打码后再外发。
3. **让 AI 直接给"是否上线 / 是否扩量"的判定**：AI 给的是分析依据，不是决策（红线 #6）。把 AI 输出当"决策依据"，决策由人按业务上下文做。

---

## §5 下一步 / Next

- 卡住了 → [`common_obstacles.md`](common_obstacles.md)
- 学完想深入 → [`what_next.md`](what_next.md)
- AI 协作基础 → [`workflows/ai_basics/`](../../workflows/ai_basics/)
- 数据 / 研究完整工作流 → [`workflows/research_and_analysis/`](../../workflows/research_and_analysis/)
