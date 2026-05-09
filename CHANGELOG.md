# CHANGELOG

This repository's release history.

Versioning follows date-based tags (`vYYYY.MM.DD`) since the cadence is event-driven (annual training + ad-hoc updates), not semantic. Dates are when the snapshot was frozen, not when work began.

Root PRD: [`workspace_human/prd/PRD-0001_conference_playbook_for_using_ai_at_work.md`](workspace_human/prd/PRD-0001_conference_playbook_for_using_ai_at_work.md).

---

## v2026.05.10 — 2026-05-10 (PRD-0002)

按 [PRD-0002](workspace_human/prd/PRD-0002_role_based_getting_started.md) 加按角色分组的新人开局引导 `training/getting_started/`。

### What ships

- **`training/getting_started/`** — 18 份 Markdown：4 公共（README / 00_first_5_minutes / common_obstacles / what_next）+ 14 角色专属开局文档（销售 / 市场增长 / 客户成功 / 创作者运营 / 产品 / 设计 / 开发 / AI 算法 / QA / 运营 / 数据分析 / 短视频内容 / 内容审核 / 跨职能兜底）。每份 ≤ 150 行 / 5 段固定结构（身份场景 → 第一句脚本 → 本周三个工作流 → 三个常见坑 → 下一步）/ 中英双语段标 / 含 ≥ 1 条 80-200 字逐字脚本。
- **6 入口文件指向更新** — `README.md`（"## 这个文件夹是给谁用的"上方加新人入口段）/ `AI_MANUAL.md` §4（"不知道从哪开始"行链接由 `workflows/ai_basics/` 改为 `training/getting_started/`）/ `CLAUDE.md` 任务接入路径表 / `AGENTS.md` / `.cursorrules` / `CODEX.md`（4 入口文件加"新人开局"段）。

### Red-line audit

- ✅ AC-1..AC-9 全部通过（详见 PRD-0002 §11 完成快照）
- ✅ 18 份文件每份 ≤ 150 行（最长 70 行 README）
- ✅ AC-7 红线条目原文指纹 grep 返回空——只链不抄
- ✅ AC-9 命名永久化 grep 返回空（教学反例改成不触发匹配的拼字母版）
- ✅ 18 份文件无真实客户名 / 模型 ID / 内部代号 / 真实合同金额

### Deferred

- **风险 #1 spot-check**：14 份角色文档至少 5 份需找对应岗位代表读一遍，是 v1.1 前的用户侧任务，不阻塞本次上线。
- **v1.1 反馈窗口**：按 PRD-0002 §7 复评点，上线 1 个月后（约 2026-06-10）按真实使用反馈决定是否需要 v1.1。

---

## v1.0 — 2026-05-10

First public release.

Prepared for the 2026 internal session **"Effectively Using AI to Get Work Done"** (~50 attendees: TUZHAN staff + partners). Released under [CC BY 4.0](LICENSE) so partners and any reader can clone, adapt, and reuse — only attribution is required.

### What ships in v1.0

- **`principles/`** — 15 red lines + 12 sub-principle files. Constitutional layer; every other file in the repo is downstream of these.
- **`workflows/`** — 41 "how-to" guides across 8 work categories (ai_basics, planning, research_and_analysis, content_creation, customer_communication, operations, engineering, decision_records).
- **`templates/`** — 8 reusable templates (PRD, ADR, customer brief, sales-call summary, video script, weekly review, bug report, meeting notes).
- **`case_studies/`** — 3 fully fictional cross-functional case studies (product / operations / sales).
- **`projects/customer_brief_generator/`** — runnable Python sample project; works offline (template-fill mode) without an `ANTHROPIC_API_KEY`, switches to Claude API when a key is provided. `pytest tests/` passes 20/20.
- **`training/`** — complete materials for the two-part conference session (Part 1 general ~90 min, Part 2 developer ~90 min), plus live-demo walkthrough, speaker notes, and a one-page conference run-sheet.
- **`runbooks/`** — 3 operational runbooks (deployment rollback, partner onboarding, sales-lead handoff).
- **4 AI-tool entry files** — `CLAUDE.md` / `AGENTS.md` / `.cursorrules` / `CODEX.md`. Same operating contract regardless of which AI tool a reader uses.
- **`setup.sh`** / **`setup.ps1`** — one-shot init for macOS/Linux + Windows (Python check, git init, sample tests, integrity verification).

### Red-line audit (release blockers, all green)

- ✅ Single file ≤ 800 lines (longest is the root PRD at 365 lines)
- ✅ All Markdown ≥ 200 lines declares `retention:` in frontmatter
- ✅ No customer data, real PRD/Bug IDs, real customer/employee names, model endpoints, or contract values in any file
- ✅ Sample project tests pass with and without API key
- ✅ Four AI-tool entry files share the same red-line and immediate-action contract

### Pre-publish redaction

- One internal-looking SSH/docker reference in [training/part_2_for_developers/04_deployment_and_red_lines.md](training/part_2_for_developers/04_deployment_and_red_lines.md) was rewritten to use unmistakable `<your-prod-host>` / `<your-app-container>` placeholders, preserving the teaching shape of the command while ensuring no internal infrastructure name leaks. Recorded here for auditability.

### Known gaps (intentional, deferred)

- **Pre-commit secret-scanning hook** — would have caught the redaction above before commit. Deferred to a future PRD; manual grep is the current control.
- **Public issue / PR templates** — internal single source of truth remains [issues/known.md](issues/known.md). Public-facing templates can be added when partner-side reuse generates inbound issues.

---

## How to read this file

Each release section answers: **what shipped**, **what was verified**, **what was deliberately deferred**. New releases append to the top.
