# for_content_moderation · 内容审核 / 合规

> 你今天打开仓库后的 5 分钟开局指引（UGC 平台必备）。
> Your first 5 minutes as a content moderation / compliance reviewer.

---

## §1 你是谁 / 今天可能在做什么 / Who You Are & Today's Likely Work

你是 TUZHAN 短视频 AI Agent 团队的内容审核 / 合规。本周高频场景：

1. 违规内容审核（人工 + 模型协作）
2. 申诉回复（被处理用户复议）
3. 审核规则迭代（新违规模式 → 规则手册更新）
4. 上报（重大违规 / 合规风险）
5. 培训新审核员

---

## §2 第一次和 AI 的对话 / Your First AI Conversation

把下面整段复制给 AI（替换 `<...>` 处）：

```
请先读 AI_MANUAL.md。我是内容审核，今天要起 <一个申诉类型> 的回复模板：3 段 + 援引规则编号（按法务给的对外编号，不是内部规则 ID）+ 复议路径。被处理账号信息我已脱敏。先列你不确定的点。注意：你给的是"判定依据 + 回复结构"，不是"是否违规判定"——判定由人按完整证据做（红线 #6）。

Read AI_MANUAL.md first. I'm in content moderation. Today: draft an appeal-response template for <appeal type> — 3 paragraphs + cited public rule IDs (not internal rule IDs) + appeal path. Subject account info redacted. List unknowns. Note: you provide "judgment basis + response structure", not "is-violation decisions" — decisions are mine on full evidence (rule #6).
```

---

## §3 本周可以先用的 3 个工作流 / 3 Workflows to Start With

- [`workflows/customer_communication/support_response_drafting.md`](../../workflows/customer_communication/support_response_drafting.md) — 申诉 / 客服回复
- [`workflows/operations/ops_runbook_authoring.md`](../../workflows/operations/ops_runbook_authoring.md) — 审核规则手册迭代
- [`workflows/decision_records/how_to_write_an_adr.md`](../../workflows/decision_records/how_to_write_an_adr.md) — 重要规则变更落字

---

## §4 三个新手最常踩的坑 / 3 Common Pitfalls

1. **申诉回复含内部规则编号 / 模型 ID / 内部审核员代号**：越红线 #2，被处理用户拿截图发社交平台 = 公司被反向曝光内部流程。**只**援引法务给的对外公开规则 ID。
2. **被处理用户的真实账号 / 真实手机号 / 真实违规截图贴 AI**：越红线 #3。脱敏 / 描述化处理后再用。
3. **让 AI 直接给"是否违规"的判定**：AI 给的是"判定依据 + 相似案例"，最终判定由人按完整证据 + 红线 #6 决策依据落字。AI 误判会让被冤枉的用户失去复议机会。

---

## §5 下一步 / Next

- 卡住了 → [`common_obstacles.md`](common_obstacles.md)
- 学完想深入 → [`what_next.md`](what_next.md)
- AI 协作基础 → [`workflows/ai_basics/`](../../workflows/ai_basics/)
- 客户 / 申诉沟通完整工作流 → [`workflows/customer_communication/`](../../workflows/customer_communication/)
