# for_engineering · 开发 / Engineering

> 你今天打开仓库后的 5 分钟开局指引（后端 / 前端 / 客户端通用）。
> Your first 5 minutes as a backend / frontend / client developer.

---

## §1 你是谁 / 今天可能在做什么 / Who You Are & Today's Likely Work

你是 TUZHAN 短视频 AI Agent 团队的开发同事（不限端）。本周高频场景：

1. 实现 [`workspace_human/prd/`](../../workspace_human/prd/) 里的某份 PRD
2. 修 [`issues/known.md`](../../issues/known.md) 里的 Bug
3. 写 / 评审 PR
4. 上线前自查
5. 线上故障排查（红线 #14：第 1 个动作 = 拉真实日志）

---

## §2 第一次和 AI 的对话 / Your First AI Conversation

把下面整段复制给 AI（替换 `<...>` 处）：

```
请先读 AI_MANUAL.md 和 workflows/engineering/prd_to_implementation.md。我是 <后端 / 前端 / 客户端> 开发，今天要实现 PRD-<XXXX> 的 <第 N 部分>。先：1) 列你不确定的点（不许硬填），2) 给一份实施草图（含改动文件清单 + 测试策略）。等我确认后再写代码。最终代码自查红线 #5 / #7 / #13。

Read AI_MANUAL.md and workflows/engineering/prd_to_implementation.md first. I'm a <backend/frontend/client> dev, implementing part <N> of PRD-<XXXX>. First: 1) list unknowns (no guessing), 2) draft an implementation sketch (file list + test plan). Wait for my confirmation before coding. Self-check rules #5/#7/#13 at the end.
```

---

## §3 本周可以先用的 3 个工作流 / 3 Workflows to Start With

- [`workflows/engineering/prd_to_implementation.md`](../../workflows/engineering/prd_to_implementation.md) — PRD → 代码全生命周期
- [`workflows/engineering/debugging_workflow.md`](../../workflows/engineering/debugging_workflow.md) — 修 Bug；配合 [`templates/bug_report/`](../../templates/bug_report/) + [`issues/known.md`](../../issues/known.md)
- [`workflows/engineering/deployment_hygiene.md`](../../workflows/engineering/deployment_hygiene.md) — 上线前自查；配合 [`runbooks/`](../../runbooks/)

---

## §4 三个新手最常踩的坑 / 3 Common Pitfalls

1. **没 PRD 直接写代码**：越红线 #5。AI 建议跳过 PRD 时**严格拒绝**——先去 [`issues/known.md`](../../issues/known.md) 找对应 Bug，没有就起 PRD。
2. **漏清反向断言测试**：旧错误行为的单元测试是 Bug 的一部分（红线 #13），同 commit 翻转或删除。AI 默认不会主动找——你要让它列。
3. **故障没看日志就猜代码**：红线 #14——第 1 动作 = 拉真实日志。AI 想做 >3 轮静态猜测立刻打断，回 [`workflows/operations/incident_response_workflow.md`](../../workflows/operations/incident_response_workflow.md)。

---

## §5 下一步 / Next

- 卡住了 → [`common_obstacles.md`](common_obstacles.md)
- 学完想深入 → [`what_next.md`](what_next.md)（含 1 小时 / 1 天 / 1 周自学路径）
- AI 协作基础 → [`workflows/ai_basics/`](../../workflows/ai_basics/)
- 工程纪律完整版 → [`workflows/engineering/`](../../workflows/engineering/) 全组（6 份）
