# common_obstacles · 我卡住了 / I'm Stuck

> 8 类最常见的"和 AI 说不上话"的障碍 + 怎么办。
> 8 most-common "AI is not understanding me" obstacles + what to do.

---

## 1. AI 没读 AI_MANUAL.md 就开干 / AI Started Without Reading AI_MANUAL

**症状**：建议明显违反某条红线，或链了不存在的文件。
**怎么办**：直接说"请先 100% 完成 AI_MANUAL.md 和 principles/000_CORE_RED_LINES.md，再回我"。

## 2. AI 把内部代号 / 真实客户名 / 模型 ID 写进了客户面文案 / AI Leaked Internal Info into Customer-facing Copy

**症状**：邮件草稿里出现内部 PRD 编号 / 内部模型 endpoint / 真实客户公司全名 / 内部岗位代号。
**怎么办**：援引红线 #2 让它重写；同时检查你的 prompt 里是否泄露了不该给的上下文（红线 #3）。三道闸验证见 [`principles/subs/content_quality.md`](../../principles/subs/content_quality.md)。

## 3. AI 不肯说"不知道" / AI Won't Say "Don't Know"

**症状**：编造文件路径 / API 端点 / 流程节点。
**怎么办**：在 prompt 里加一句"不确定时**必须**说不确定，不许猜"——参考 [`workflows/ai_basics/trust_and_verify.md`](../../workflows/ai_basics/trust_and_verify.md)。

## 4. AI 输出比预期短 / 浅 / AI Output Too Short or Shallow

**症状**：寥寥几行，没有逐条对应你的需求。
**怎么办**：用 [`workflows/ai_basics/how_to_give_clear_instructions.md`](../../workflows/ai_basics/how_to_give_clear_instructions.md) 的 6 件事检查清单（背景 / 目标 / 边界 / 材料 / 形式 / 不确定），补齐你没给到的那一两件。

## 5. AI 偏离话题越走越远 / AI Keeps Drifting

**症状**：3 轮后已经在讨论你完全不关心的事。
**怎么办**：开新会话 + 用更窄的 prompt 重启。把目标和边界写得更明确。

## 6. AI 推荐了不存在的工作流 / AI References Workflows That Don't Exist

**症状**：让你"参考 `workflows/xxx/yyy.md`"但路径不在仓库里。
**怎么办**：去 [`AI_MANUAL.md`](../../AI_MANUAL.md) §4 真实工作流表对照；如果**应该有但漏了**，按红线 #5 起一份 PRD 提议加新工作流。

## 7. AI 建议跳过 PRD 直接改代码 / AI Suggests Skipping PRD

**症状**："小改不需要走 PRD 吧" / "demo 一下就行"。
**怎么办**：援引红线 #5——任何代码改动必须对应 [`workspace_human/prd/`](../../workspace_human/prd/) 的 PRD 或 [`issues/known.md`](../../issues/known.md) 的一条 Bug 条目。**严格拒绝**绕过。

## 8. 我自己也不知道我要做什么 / I Don't Know What I Want To Do

**症状**：前 30 秒就放弃了，关掉 AI。
**怎么办**：去 [`for_cross_functional.md`](for_cross_functional.md)——专为这个状态设计。

---

## 还是卡？/ Still Stuck?

→ 找你的团队 lead 或仓库主理人；或在 [`meetings/`](../../meetings/) 起一份"自学反馈"，让仓库随真实使用进化。
→ Find your team lead or repo owner; or open a "self-study feedback" note in [`meetings/`](../../meetings/) so the repo evolves with real usage.
