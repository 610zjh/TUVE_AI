---
name: 日常工作传递（inbox / outbox）/ Daily Handoff Workflow
retention: permanent
retention_reason: 全公司日常岗位间轻量传递工作流，长期复用 / Universal company-wide daily-handoff workflow
---

# 日常工作传递 / Daily Handoff Workflow

> 适用：每天都在发生的"我做完一份小东西要给同事"或"同事临时给我一份资料"。
> 配套目录：[`handoffs/`](../../handoffs/)（[inbox](../../handoffs/inbox/) / [outbox](../../handoffs/outbox/)）。

---

## 决定要不要走 handoffs/

3 个判定问，全 yes 才走：

1. **轻量吗？** 这件事不需要开 PRD、不需要立项、不需要走签批
2. **临时吗？** 预期 30 天内会被消化掉（要么处理完归档，要么对方接手后这份就过时）
3. **岗位间吗？** 是同事 → 同事，不是岗位级离职交接、不是对客户的合同 / 报价 / 回执

任一 no → 走对应正规流程：

| 不是这种 → 去哪 |
|---|
| 不轻量（要立项）→ [`workspace_human/prd/`](../../workspace_human/prd/) 起 PRD |
| 不临时（要长期）→ [`runbooks/`](../../runbooks/) / [`templates/`](../../templates/) / [`case_studies/`](../../case_studies/) |
| 岗位级交接（人员变动）→ 专门的离职 / 调岗流程（未来 PRD） |
| 对客户合同 / 法务 → 签批流程（**不进 git**） |
| 客户电话纪要 → [`workspace_human/meetings/customer_followups/`](../../workspace_human/meetings/customer_followups/) |
| Bug / 问题 → [`issues/known.md`](../../issues/known.md)（红线 #4 SSOT）|

---

## inbox 接收流（同事给我了一份）

**收到**（含未脱敏字段）→ `_raw/` 暂存

```
ls handoffs/inbox/_raw/    # 应该看到你刚扔进来的文件
```

**提取 + 脱敏**：

```
我从客户群收到一段需求描述（在 handoffs/inbox/_raw/2026-05-10_xxx.txt）。
请基于内容生成一份 handoffs/inbox/2026-05-10_sales-to-ops_customer-needs.md，
要求：
- 客户名脱敏成"客户 A"
- 手机 / 邮箱 / 身份证全删除
- 不引入未在原文出现的事实
- 输出后告诉我你最不确定的 2 个点
```

**自查 5 条**（[../../handoffs/inbox/README.md](../../handoffs/inbox/README.md)）→ 全过 → `git add` 顶层文件 → `git commit`

**清理 `_raw/`**：本地删除或移到仓库外（红线 #3 + 反熵 第 3 条 AI 不自删，所以是你手动）

---

## outbox 发送流（我给同事一份）

**写成品**：

```
我要给视频组写一份本周拍摄要点，临时性、不开 PRD。
请生成一份 handoffs/outbox/2026-05-10_video-team_weekly-shoot-brief.md，
覆盖 [3-5 个要点]。
要求：
- 收件方是内部视频组（语气：协作平等，非对客户）
- 不含具体客户名 / 内部 PRD 编号 / 模型 ID / 未公开排期（红线 #2）
- 200-400 字
```

**自查**：脱敏 5 条 + 红线 #2 客户面口径（即使收件方是内部，按"假设这份会被外人看到"自查更稳）

**通知下游**：Slack / 邮件给视频组贴文件相对路径，让对方在 AI 协助下能直接读

---

## AI 协助起草 outbox 的 5 步

参考 [`workflows/planning/writing_a_prd.md`](../planning/writing_a_prd.md) 的 5 步法风格，本文件不复述：

1. **背景拼图**：说清楚收件方是谁、原始素材在哪
2. **目标 + 非目标**：写这份是为了让对方做什么、不是为了什么
3. **要点列出**：3-5 个核心信息
4. **用收件方语言改写**：销售给运营 ≠ 运营给视频，用对方能直接消化的语言
5. **自查脱敏 + 红线 #2**：必做，不省

---

## 5 个常见误用

| 误用 | 应去 |
|---|---|
| 把客户电话**纪要**写到 outbox/ | [`workspace_human/meetings/customer_followups/`](../../workspace_human/meetings/customer_followups/) |
| 把 Bug 报告写到 outbox/ | [`issues/known.md`](../../issues/known.md) |
| 把"未来要做的功能"想法写到 outbox/ | [`workspace_human/prd/`](../../workspace_human/prd/) 起 PRD |
| 把客户合同初稿丢进 inbox/_raw/ | 合同**不进 git**，走签批流程 |
| 6 个月还在 outbox/ 没动 | 周复盘时按 4 选 1 处理（[../../handoffs/README.md](../../handoffs/README.md)）|

---

## 周复盘时的 handoffs/ 扫描

每周 [`weekly_review_routine.md`](../planning/weekly_review_routine.md) 会让你扫一次 handoffs/ 30 天未动文件。判定 4 选 1：留 / 挪 / 删 / 归档。AI **不允许**自动执行清理，只能列候选。
