# for_qa · 测试 / QA

> 你今天打开仓库后的 5 分钟开局指引（手工 / 自动化 / 回归 / 上线前）。
> Your first 5 minutes as QA / test engineer.

---

## §1 你是谁 / 今天可能在做什么 / Who You Are & Today's Likely Work

你是 TUZHAN 短视频 AI Agent 团队的 QA。本周高频场景：

1. 新功能测试用例设计
2. 回归测试（金线 / 边角）
3. Bug 复现 + 录入 [`issues/known.md`](../../issues/known.md)
4. 上线前自查（[`workflows/engineering/deployment_hygiene.md`](../../workflows/engineering/deployment_hygiene.md)）
5. 自动化脚本维护

---

## §2 第一次和 AI 的对话 / Your First AI Conversation

把下面整段复制给 AI（替换 `<...>` 处）：

```
请先读 AI_MANUAL.md 和 workflows/engineering/testing_discipline.md。我是 QA，今天要为 PRD-<XXXX> 列测试用例：金线 + 边角 + 回归。先：1) 列你不确定的点（特别是 PRD §5 验收标准里没说清的），2) 按 templates/bug_report/bug-template.md 准备一份 Bug 模板供我复现时填。线上日志 / 用户复现数据贴你之前会先脱敏（红线 #3）。

Read AI_MANUAL.md and workflows/engineering/testing_discipline.md first. I'm QA. Today: list test cases for PRD-<XXXX> — happy path + edge + regression. First: 1) list unknowns (esp. unclear AC items in PRD §5), 2) prep a bug template per templates/bug_report/bug-template.md. Production logs / repro data will be redacted before I paste (rule #3).
```

---

## §3 本周可以先用的 3 个工作流 / 3 Workflows to Start With

- [`workflows/engineering/testing_discipline.md`](../../workflows/engineering/testing_discipline.md) — 测试纪律全套
- [`workflows/engineering/bug_tracking_ssot.md`](../../workflows/engineering/bug_tracking_ssot.md) — Bug 单一登记本
- [`workflows/engineering/deployment_hygiene.md`](../../workflows/engineering/deployment_hygiene.md) — 上线前 / 后自查

---

## §4 三个新手最常踩的坑 / 3 Common Pitfalls

1. **发现 Bug 不录 [`issues/known.md`](../../issues/known.md) 而是私存 / Slack / 邮件**：越红线 #4 单一登记本——会造成多份真相。**整条**录入 [`issues/known.md`](../../issues/known.md)，修完整条搬到 [`issues/fixed/`](../../issues/fixed/)。
2. **修 Bug 时漏清反向断言测试**：旧错误行为如果有单元测试当时绿了 CI，那些测试是 Bug 的一部分（红线 #13），同 commit 翻转或删除。
3. **P0 / P1 没立刻通知**：登记完不算完——P0 / P1 立刻通知工程负责人 + 业务方 + 客户面口径（红线 #2）。流程见 [`issues/known.md`](../../issues/known.md) "P0 / P1 的特殊纪律"。

---

## §5 下一步 / Next

- 卡住了 → [`common_obstacles.md`](common_obstacles.md)
- 学完想深入 → [`what_next.md`](what_next.md)
- AI 协作基础 → [`workflows/ai_basics/`](../../workflows/ai_basics/)
- 工程纪律完整版 → [`workflows/engineering/`](../../workflows/engineering/)
