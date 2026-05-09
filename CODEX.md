# CODEX.md · Trae / Codex 兼容工具入口文件 / Trae and Codex-Compatible Tools Entry File

> 内容与 [`CLAUDE.md`](CLAUDE.md) / [`AGENTS.md`](AGENTS.md) 一致。Trae 等兼容 Codex 协议的工具会读取这份文件。
> Identical content to [`CLAUDE.md`](CLAUDE.md) / [`AGENTS.md`](AGENTS.md). Trae and other Codex-protocol-compatible tools auto-load this file.

---

## 立即动作 / Immediate Actions

1. 读完 [`AI_MANUAL.md`](AI_MANUAL.md)
2. 读完 [`principles/000_CORE_RED_LINES.md`](principles/000_CORE_RED_LINES.md)
3. 扫一眼 [`issues/known.md`](issues/known.md)
4. 扫一眼 [`workspace_human/prd/`](workspace_human/prd/)
5. 等用户任务，在此之前不动文件 / Wait for the user's task; touch nothing before that

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
2. 客户面文案严禁内部信息 / No internal info in customer-facing copy
3. 保密数据脱敏 / Redact confidential data
4. Bug 单一登记本（known.md → fixed/YYYY-MM-DD.md）/ Issue SSOT
5. 改代码先有 PRD / PRD before code
6. 决策落字成 ADR / Decisions written as ADRs
7. 单文件 ≤ 800 行 / Single file ≤ 800 lines
8. 不可逆动作必须先确认 / Irreversible actions need confirmation
9. 命名按"长期复用"，禁止 demo_/sample_/placeholder_ / Names are forever
10. 收尾五件套 / Five-part closeout
11. 长 Markdown 声明 retention class / Long Markdown declares retention
12. `workspace_human/` 是 AI 只读 / `workspace_human/` is read-only
13. 修 Bug 同步清反向断言测试 / Clean reverse-assertion tests
14. 线上故障第 1 动作看日志 / Logs first on incident
15. 主次不可颠倒：产品价值在前商业包装在后 / Product before paywall

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

## Trae 特性提示 / Trae Specifics

- 中文 IDE 体验最完整，复杂任务前先用中文把目标说清楚
  Strongest CN IDE experience; for complex tasks, state goals in Chinese first
- 与 Codex CLI 互通，本地开发与远程批量可同一份指令套用
  Interoperable with Codex CLI; local-dev and remote-batch reuse the same instructions
- 涉及代码改动一律走 [`workflows/engineering/prd_to_implementation.md`](workflows/engineering/prd_to_implementation.md) 的流程
  Any code change goes through [`workflows/engineering/prd_to_implementation.md`](workflows/engineering/prd_to_implementation.md)

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

## SEE2AI / TUVE 产品介绍材料 / SEE2AI / TUVE Product Materials

[`products/`](products/) 收录了兔展旗下 **SEE2AI** 平台与 **TUVE** 应用的公开产品介绍——功能、接入、能力、计费、支持。需要给客户/合作伙伴介绍这两款产品时从这里取材。
[`products/`](products/) contains public product introductions for TUZHAN's **SEE2AI** platform and **TUVE** app — features, onboarding, capabilities, pricing, support. Source from here when introducing these two products to customers / partners.

---

## 完整任务-入口表见 [`AI_MANUAL.md`](AI_MANUAL.md) §4 / Full task-to-entry table in [`AI_MANUAL.md`](AI_MANUAL.md) §4
