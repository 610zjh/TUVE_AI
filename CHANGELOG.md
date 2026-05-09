# CHANGELOG

This repository's release history.

Versioning follows date-based tags (`vYYYY.MM.DD`) since the cadence is event-driven (annual training + ad-hoc updates), not semantic. Dates are when the snapshot was frozen, not when work began.

Root PRD: [`workspace_human/prd/PRD-0001_conference_playbook_for_using_ai_at_work.md`](workspace_human/prd/PRD-0001_conference_playbook_for_using_ai_at_work.md).

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
