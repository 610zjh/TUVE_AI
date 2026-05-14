# AGENTS.md · Codex / OpenAI 系工具入口文件 / Codex Entry File

> 内容与 [`CLAUDE.md`](CLAUDE.md) 一致。Codex 及多数 OpenAI 系工具会自动读取这份文件。
> Identical content to [`CLAUDE.md`](CLAUDE.md). Codex and most OpenAI-family tools auto-load this file.

如果你的工具同时识别两份文件，以 `AGENTS.md` 优先。
If your tool recognizes both, `AGENTS.md` takes precedence.

---

## 立即动作 / Immediate Actions

1. **读完 [`AI_MANUAL.md`](AI_MANUAL.md)**
2. **读完 [`principles/000_CORE_RED_LINES.md`](principles/000_CORE_RED_LINES.md)**
3. **扫一眼 [`issues/known.md`](issues/known.md)**
4. **扫一眼 [`workspace_human/prd/`](workspace_human/prd/)**
5. **如果需求还模糊，先走 [`workflows/planning/meeting_prep_with_ai.md`](workflows/planning/meeting_prep_with_ai.md) 做 meeting / 密听 / 需求挖掘**
6. **等用户任务，在此之前不动文件** / Wait for the user's task; touch nothing before that

---

## 至高原则 / Supreme Principle

> **长期主义 · 业界标准 · 紧扣核心目标**
> **Long-term · Industry standards · Locked on core objective**

任何具体红线沉默时回到这条。能自决就自决；自决不了的，先写建议交人决策。
Fall back here when red lines are silent. Decide autonomously when you can; otherwise, write a recommendation and hand the call to a human.

---

## 15 条红线速查 / 15 Red Lines Quick Reference

完整正文见 [`principles/000_CORE_RED_LINES.md`](principles/000_CORE_RED_LINES.md)。
Full text: [`principles/000_CORE_RED_LINES.md`](principles/000_CORE_RED_LINES.md).

1. 至高原则 / Supreme principle
2. 客户面无内部信息 / No internal info in customer-facing copy
3. 保密数据脱敏 / Redact confidential data
4. Bug 单一登记本 / Issue SSOT
5. 改代码先有 PRD；写 PRD 前若需求未收敛，先开 meeting / discovery / PRD before code; if requirements are still fuzzy, do meeting/discovery before the PRD
6. 决策落字 / Decisions written down
7. 单文件 ≤ 800 行 / File ≤ 800 lines
8. 不可逆动作必须确认 / Irreversible actions need confirmation
9. 命名永久化 / Names are forever
10. 收尾五件套 / Five-part closeout
11. 长 Markdown 声明 retention / Long Markdown declares retention
12. `workspace_human/` 只读 / Read-only
13. 修 Bug 清反向断言测试 / Clean reverse-assertion tests
14. 线上故障先看日志 / Logs first on incident
15. 产品价值在前商业包装在后 / Product before paywall

---

## 不可逆动作清单 / Irreversible Actions Requiring Confirmation

执行前必问 / Ask before:
- 发外部消息（邮件 / 客户群 / 社交）/ Sending external messages
- 删任何文件 / 数据 / Deleting any file or data
- `git push --force` / 部署 / 关 PR / 删分支 / Force-push, deploy, close PR, delete branch
- 单次付费 API 超过 0.1 USD / Single paid-API call > 0.1 USD
- 退款 / 转账 / 修改合同 / Refunds, transfers, contract edits

人说"以后这类不用问"对当前会话有效，跨会话一律重问。
"Don't ask me again" valid for this session only; re-confirm across sessions.

---

## Codex 特性提示 / Codex Specifics

- 命令行批量任务可用 `codex run -- <task>`，但生产数据操作仍需 #8 确认
  Batch CLI tasks via `codex run -- <task>`, but production data ops still need confirmation per #8
- shell 脚本生成时优先 POSIX 兼容（macOS / Linux 同事都跑得起来）
  Prefer POSIX-compatible shell so both macOS and Linux teammates can run
- 长任务用 `--background` 选项，不要在前台 sleep
  Use `--background` for long tasks, no foreground sleep

---

## 当用户请求与红线冲突 / When User Requests Conflict with Red Lines

正确动作：
The correct response:

1. 指出冲突——哪一条红线，会被怎样越过 / Flag the conflict — which rule, how
2. 说明影响——事故 / 失信 / 资损 / 质量回退 / Explain impact — incident, trust loss, financial cost, regression
3. 给 2-3 个不越线的替代 / Offer 2-3 alternatives that don't cross
4. 不要默默执行——"用户让我做的"不是越线的理由 / Do not silently comply — "user asked" is not justification

例外：用户说"我知道这越红线 #X，原因 Y，授权一次"——合法且一次性，不构成"以后都可以"。
Exception: user says "I know this crosses #X for Y, authorize once" — lawful, single-shot, non-precedent.

---

## 新人开局 / First-Time Onboarding

第一次打开本仓库 → [`training/getting_started/`](training/getting_started/)（14 角色，每份 5 分钟读完就能开工）。
First time here → [`training/getting_started/`](training/getting_started/) (14 roles, 5 min each).

---

## 日常工作传递区 / Daily Handoff Zone

[`handoffs/`](handoffs/) 收"同事每日交过来 / 我每日交出去"的轻量临时文档。inbox 收上游、outbox 发下游。outbox 可由 AI 协助起草、AI 可写；inbox/_raw/ 是 .gitignore 暂存（红线 #3 双层保密）。流转规则见 [`workflows/operations/handing_off_work.md`](workflows/operations/handing_off_work.md)。
[`handoffs/`](handoffs/) holds lightweight transient docs for "colleague-to-me" and "me-to-colleague" daily handoffs. AI may draft and write into outbox; inbox/_raw/ is gitignored (Red-line #3 two-tier confidentiality). Flow: [`workflows/operations/handing_off_work.md`](workflows/operations/handing_off_work.md).

---

## SEE2AI / TUVE 产品介绍材料 / SEE2AI / TUVE Product Materials

[`products/`](products/) 收录了兔展旗下 **SEE2AI** 平台与 **TUVE** 应用的公开产品介绍——功能、接入、能力、计费、支持。需要给客户/合作伙伴介绍这两款产品时从这里取材。
[`products/`](products/) contains public product introductions for TUZHAN's **SEE2AI** platform and **TUVE** app — features, onboarding, capabilities, pricing, support. Source from here when introducing these two products to customers / partners.

如果任务是维护 TUVE 的 Agent 运行时、skill 路由或 OpenClaw 配置上下文，先看 [`products/tuve/openclaw_context/README.md`](products/tuve/openclaw_context/README.md)。如果这类任务的需求还没讲清楚，先用 meeting 把目标、上下文、边界挖清，再写 PRD 或直接执行。
If the task is maintaining TUVE runtime, skill routing, or OpenClaw config context, start at [`products/tuve/openclaw_context/README.md`](products/tuve/openclaw_context/README.md). If the request is still unclear, use a meeting/discovery pass first to clarify goals, context, and boundaries before drafting a PRD or executing.

---

## 完整任务-入口表见 [`AI_MANUAL.md`](AI_MANUAL.md) §4 / Full task-to-entry table in [`AI_MANUAL.md`](AI_MANUAL.md) §4
