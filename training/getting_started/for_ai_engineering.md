# for_ai_engineering · AI 算法 / 模型工程师

> 你今天打开仓库后的 5 分钟开局指引（短视频 AI 团队特有，与通用开发分开）。
> Your first 5 minutes as an AI/model engineer (specific to the short-video AI team).

---

## §1 你是谁 / 今天可能在做什么 / Who You Are & Today's Likely Work

你是 TUZHAN 短视频 AI Agent 团队的算法 / 模型工程师。和通用后端 / 前端开发的差异：你的"实现"包含模型迭代 + 离线评估 + 上线灰度。本周高频场景：

1. 模型迭代实验设计
2. 离线评估指标 + 人评样本
3. 上线灰度策略 + 监控
4. 效果归因 / 回归分析
5. 数据 pipeline 维护（训练 / 离线 / 在线）

---

## §2 第一次和 AI 的对话 / Your First AI Conversation

把下面整段复制给 AI（替换 `<...>` 处）：

```
请先读 AI_MANUAL.md 和 workflows/engineering/prd_to_implementation.md。我是 AI 算法工程师，今天要为 <一个模型迭代方向> 写实验设计：离线指标 + 人评样本设计 + 上线灰度方案。先：1) 列你不确定的点（特别是业务指标真值），2) 按红线 #5 自查"这次迭代有没有对应 PRD"。所有训练数据示例都已脱敏，不要让我把原始用户行为数据贴给你。

Read AI_MANUAL.md and workflows/engineering/prd_to_implementation.md first. I'm an AI/ML engineer. Today: design experiments for <model iteration direction> — offline metrics + human-eval samples + rollout plan. First: 1) list unknowns (esp. business-metric ground truth), 2) self-check rule #5 (does this iteration map to a PRD). Training samples are redacted; don't ask me to paste raw user behavior.
```

---

## §3 本周可以先用的 3 个工作流 / 3 Workflows to Start With

- [`workflows/engineering/prd_to_implementation.md`](../../workflows/engineering/prd_to_implementation.md) — 模型迭代也走 PRD
- [`workflows/engineering/testing_discipline.md`](../../workflows/engineering/testing_discipline.md) — 离线评估 = 你的"测试"
- [`workflows/engineering/deployment_hygiene.md`](../../workflows/engineering/deployment_hygiene.md) — 上线灰度自查

---

## §4 三个新手最常踩的坑 / 3 Common Pitfalls

1. **训练数据 / 用户行为日志未脱敏喂大模型 / 第三方 API**：越红线 #3，**且**很可能违反隐私合规。脱敏后再用，必要时走法务。
2. **模型 endpoint / 内部模型名 / 实验代号进客户面**：越红线 #2，错误日志 / 监控告警 / 客服回复都是常见泄漏点。
3. **上线灰度跳过 PRD**："只是改了下推荐权重"也要走 PRD（红线 #5）。任何线上行为变化对用户 = 一次新发布。

---

## §5 下一步 / Next

- 卡住了 → [`common_obstacles.md`](common_obstacles.md)
- 学完想深入 → [`what_next.md`](what_next.md)
- AI 协作基础 → [`workflows/ai_basics/`](../../workflows/ai_basics/)
- 工程纪律完整版 → [`workflows/engineering/`](../../workflows/engineering/)
