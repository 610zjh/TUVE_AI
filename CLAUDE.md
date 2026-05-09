# CLAUDE.md · Claude Code 入口文件 / Claude Code Entry File

> 这份文件被 Claude Code 启动时自动加载。其他工具的入口文件（`AGENTS.md` / `.cursorrules` / `CODEX.md`）内容一致。
> Auto-loaded by Claude Code at startup. Companion entry files for other tools (`AGENTS.md` / `.cursorrules` / `CODEX.md`) carry identical content.

---

## 立即动作 / Immediate Actions

进入这个仓库后，按顺序完成：
On entering this repo, in order:

1. **读完 [`AI_MANUAL.md`](AI_MANUAL.md)** —— 项目总导航
   **Read [`AI_MANUAL.md`](AI_MANUAL.md) end-to-end** — project navigation
2. **读完 [`principles/000_CORE_RED_LINES.md`](principles/000_CORE_RED_LINES.md)** —— 红线宪法
   **Read [`principles/000_CORE_RED_LINES.md`](principles/000_CORE_RED_LINES.md)** — red-line constitution
3. **扫一眼 [`issues/known.md`](issues/known.md)** —— 当前未解决问题
   **Glance at [`issues/known.md`](issues/known.md)** — open issues
4. **扫一眼 [`workspace_human/prd/`](workspace_human/prd/)** —— 当前活跃需求
   **Glance at [`workspace_human/prd/`](workspace_human/prd/)** — active PRDs
5. **等用户告诉你今天的任务**。在第 5 步之前不要动任何文件。
   **Wait for the user's task.** Do not touch any file before step 5.

---

## 至高决策原则 / Supreme Decision Principle

> **长期主义 · 科学方法与业界标准 · 紧扣核心产品目标**
> **Long-term thinking · Scientific methods and industry standards · Locked on the core product objective**

任何具体红线没明说的情况，回到这一条。能自决的就自决；自决不了的，先写建议交人决策。
When red lines are silent, fall back here. Decide autonomously when you can; otherwise, write a recommendation and hand the call to a human.

---

## 红线速查（完整 15 条见 [`principles/000_CORE_RED_LINES.md`](principles/000_CORE_RED_LINES.md)） / Red Lines Quick Reference (full 15 in `principles/000_CORE_RED_LINES.md`)

1. 至高原则 / Supreme principle
2. 客户面文案严禁内部信息 / No internal info in customer-facing copy
3. 保密数据脱敏 / Confidential data redaction
4. Bug 单一登记本（known.md / fixed/YYYY-MM-DD.md）/ Issue SSOT
5. 改代码前先有 PRD / PRD before code
6. 决策落字成 ADR / Decisions get written as ADRs
7. 单文件 ≤ 800 行 / Single file ≤ 800 lines
8. 不可逆动作（外部消息 / 删数据 / 部署 / 退款）必须先确认 / Irreversible actions need human confirmation
9. 命名按"长期复用"，禁止 demo_/sample_/placeholder_ / Names are forever, no demo_/sample_/placeholder_
10. 收尾五件套（测试 / 版本 / PRD 快照 / 导航 / Bug 移位）/ Five-part closeout
11. 长 Markdown 必须声明 retention class / Long Markdown declares retention
12. `workspace_human/` 是 AI 只读 / `workspace_human/` is read-only
13. 修 Bug 同步清反向断言测试 / Fix bug → clean reverse-assertion tests
14. 线上故障第 1 动作 = 看日志 / Production incident → logs first
15. 主次不可颠倒：产品价值在前商业包装在后 / Product value before commercial packaging

---

## 不可逆动作清单 / Irreversible Actions Requiring Confirmation

执行前必问 / Ask before:
- 发外部消息（邮件 / 客户群 / 社交）/ Sending external messages
- 删任何文件 / 数据 / Deleting any file or data
- `git push --force` / 部署 / 关 PR / 删分支 / Force-push, deploy, close PR, delete branch
- 单次付费 API 超过 0.1 USD / Single paid-API call > 0.1 USD
- 退款 / 转账 / 修改合同 / Refunds, transfers, contract edits

人说"以后这类不用问"对当前会话有效，跨会话一律重问。
"Don't ask me again" valid for this session only.

---

## 任务接入路径 / Task Entry Paths

按用户当前任务找入口 / Find entry by user's current task:

| 任务类型 / Task type | 起步文件 / Start here |
|---|---|
| 写 PRD / Draft PRD | [`workflows/planning/writing_a_prd.md`](workflows/planning/writing_a_prd.md) |
| 实现 PRD / Implement PRD | [`workflows/engineering/prd_to_implementation.md`](workflows/engineering/prd_to_implementation.md) → [`AI_MANUAL.md`](AI_MANUAL.md) §5 全生命周期清单 |
| 修 Bug / Fix bug | [`workflows/engineering/debugging_workflow.md`](workflows/engineering/debugging_workflow.md) |
| 客户电话整理 / Process call | [`workflows/customer_communication/sales_call_followup.md`](workflows/customer_communication/sales_call_followup.md) |
| 写视频脚本 / Video script | [`workflows/content_creation/video_script_drafting.md`](workflows/content_creation/video_script_drafting.md) |
| 写客户简报 / Customer brief | [`workflows/customer_communication/customer_brief_generation.md`](workflows/customer_communication/customer_brief_generation.md) |
| 周复盘 / Weekly review | [`workflows/planning/weekly_review_routine.md`](workflows/planning/weekly_review_routine.md) |
| 上线自查 / Pre-deploy check | [`workflows/engineering/deployment_hygiene.md`](workflows/engineering/deployment_hygiene.md) |
| 出故障 / Production incident | [`workflows/operations/incident_response_workflow.md`](workflows/operations/incident_response_workflow.md) |
| 给客户介绍 SEE2AI / TUVE / Introduce SEE2AI / TUVE to a customer | [`products/see2ai/platform_overview.md`](products/see2ai/platform_overview.md) · [`products/tuve/app_overview.md`](products/tuve/app_overview.md) |
| 不知道从哪开始 / Don't know | [`training/getting_started/`](training/getting_started/)（14 角色开局引导）/ [`workflows/ai_basics/`](workflows/ai_basics/)（基础课） |

完整任务-入口表见 [`AI_MANUAL.md`](AI_MANUAL.md) §4。
Full task-to-entry table: [`AI_MANUAL.md`](AI_MANUAL.md) §4.

---

## Claude Code 特性提示 / Claude Code Specifics

- 使用 Skill 系统时，优先调用 [`workflows/`](workflows/) 下与任务最贴近的工作流文件作为上下文
  When using Skills, pull the most-relevant workflow file under [`workflows/`](workflows/) as context first
- 使用 TodoWrite 跟踪多步任务，每步完成立即标 completed（不要批量标）
  Use TodoWrite for multi-step tasks; mark complete immediately, never batch
- 长操作（部署 / 测试套件）使用 `run_in_background`，不要 sleep 轮询
  Use `run_in_background` for long ops; never sleep-poll
- 不确定的具体业务术语 / 客户名 / 内部流程，**主动问人**而不是猜
  Unfamiliar business terms / customer names / internal processes — **ask**, don't guess

---

## 当你和用户的请求与红线冲突时 / When User Requests Conflict with Red Lines

正确动作：
The correct response:

1. **指出冲突** —— 哪一条红线，会被怎样越过 / **Flag the conflict** — which rule, how it would be crossed
2. **说明影响** —— 越过会带来什么后果（事故 / 失信 / 资损 / 质量回退）/ **Explain impact** — incident risk, trust loss, financial cost, quality regression
3. **请用户改请求** —— 给出 2-3 个不越线的替代方案 / **Ask the user to revise** — offer 2-3 alternatives that don't cross
4. **不要默默执行** —— "用户让我做的"不是越线的理由 / **Do not silently comply** — "user asked" is not a justification

例外只有一种：用户说"我知道这越过了红线 #X，原因是 Y，我授权一次"——这才算合法越线，且一次性，不构成"以后都可以"。
The only exception: user says "I know this crosses red line #X for reason Y, I authorize this once" — that's lawful, single-shot, non-precedent-setting.
