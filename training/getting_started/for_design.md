# for_design · 设计 / UI · UX

> 你今天打开仓库后的 5 分钟开局指引（UI / UX 设计师）。
> Your first 5 minutes as a UI/UX designer.

---

## §1 你是谁 / 今天可能在做什么 / Who You Are & Today's Likely Work

你是 TUZHAN 短视频 AI Agent 团队的设计师。本周高频场景：

1. UI 草稿 / 高保真稿
2. 用户体验流程梳理（含错误状态 / 空状态）
3. 组件库 / 设计 token 维护
4. 设计评审（自审 + 跨职能评审）
5. 用户研究素材整理（访谈 / 可用性测试）

---

## §2 第一次和 AI 的对话 / Your First AI Conversation

把下面整段复制给 AI（替换 `<...>` 处）：

```
请先读 AI_MANUAL.md。我是设计师，今天要为 <一个功能> 列 3 个 UI 方向 + 每个方向的验收清单（含空状态 / 错误态 / 加载态）。已脱敏的截图 / 真实用户数据不要回放给我。先列你不确定的点。所有 UI 字符串自查红线 #2（不出现内部代号 / PRD 编号）。

Read AI_MANUAL.md first. I'm a designer. Today: draft 3 UI directions for <feature> + acceptance checklists each (incl. empty / error / loading states). Don't echo back redacted screenshots / real user data. List unknowns. Self-check all UI strings against rule #2 (no internal codenames / PRD IDs).
```

---

## §3 本周可以先用的 3 个工作流 / 3 Workflows to Start With

- [`workflows/content_creation/slide_outline_workflow.md`](../../workflows/content_creation/slide_outline_workflow.md) — 设计评审 / 提案 PPT 骨架
- [`workflows/research_and_analysis/customer_interview_synthesis.md`](../../workflows/research_and_analysis/customer_interview_synthesis.md) — 用户访谈合成
- [`workflows/planning/breaking_down_a_project.md`](../../workflows/planning/breaking_down_a_project.md) — 大设计任务拆里程碑

---

## §4 三个新手最常踩的坑 / 3 Common Pitfalls

1. **截图带内部测试数据 / 真实用户名贴 AI**：越红线 #3。截图先打码再喂。
2. **UI 字符串含内部产品代号 / 模型 ID**：越红线 #2，特别是 placeholder / error message / debug-like 副本。
3. **设计稿命名一次性 / 拼字母**（如 `xglb-v3.fig`、堆 `-final-final-v2` 后缀）：越红线 #9——按"长期复用"命名，例如 `feature-onboarding-flow.fig`。

---

## §5 下一步 / Next

- 卡住了 → [`common_obstacles.md`](common_obstacles.md)
- 学完想深入 → [`what_next.md`](what_next.md)
- AI 协作基础 → [`workflows/ai_basics/`](../../workflows/ai_basics/)
- 内容 / 设计相关工作流 → [`workflows/content_creation/`](../../workflows/content_creation/)
