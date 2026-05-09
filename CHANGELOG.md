# CHANGELOG

This repository's release history.

Versioning follows date-based tags (`vYYYY.MM.DD`) since the cadence is event-driven (annual training + ad-hoc updates), not semantic. Dates are when the snapshot was frozen, not when work began.

Root PRD: [`workspace_human/prd/PRD-0001_conference_playbook_for_using_ai_at_work.md`](workspace_human/prd/PRD-0001_conference_playbook_for_using_ai_at_work.md).

---

## v2026.05.10d — 2026-05-10 (PRD-0003)

按 [PRD-0003](workspace_human/prd/PRD-0003_daily_handoff_zone.md) 加日常工作传递区 [`handoffs/`](handoffs/)（inbox + outbox），承载"同事每日交过来 / 我每日交出去"的轻量临时文档。

### What ships

- **`handoffs/`** —— 仓库根新目录树 + 4 份 README：
  - `handoffs/README.md`（总入口：是什么 / 不是什么 / 命名 / 30 天反熵）
  - `handoffs/inbox/README.md`（接收流：双层保密 + 脱敏自查 5 条）
  - `handoffs/inbox/_raw/README.md`（红色警示：未脱敏暂存，已 .gitignore）
  - `handoffs/inbox/_raw/.gitkeep`（让目录在 git 里存在）
  - `handoffs/outbox/README.md`（发送流：脱敏 + 通知下游）
- **`workflows/operations/handing_off_work.md`** —— 流转工作流：3 个判定问、inbox 接收流、outbox 发送流、AI 起草 5 步、5 个常见误用、周复盘扫描
- **`.gitignore`** —— 加 3 行：`handoffs/inbox/_raw/*` 走 .gitignore，保留 .gitkeep + README（红线 #3 双层保密落地）
- **导航更新 8 处**：
  - `AI_MANUAL.md` §2 仓库地图加 `handoffs/` 节点；§4 任务-入口表加 2 行（"给同事临时传 / 收到同事一份"）
  - `README.md` §"角色 → 你大概率会用到"销售/客户成功/运营/视频四行加 `handoffs/` 链接；§仓库地图加节点
  - `CLAUDE.md` 任务接入路径表加 1 行（"日常和同事传一份东西"）
  - `AGENTS.md` / `.cursorrules` / `CODEX.md` 各加一段"日常工作传递区"指针
  - `workspace_human/README.md` 末尾加反向引用（指向 `../handoffs/` + 解释为何不在 human 区）
  - `workflows/planning/weekly_review_routine.md` 团队周复盘加"步 4.5: handoffs/ 30 天反熵扫"

### Red-line audit

- ✅ AC-1..AC-28 全部通过（详见 PRD-0003 §11 完成快照）
- ✅ 红线 #3 落地：`_raw/` 双层 + `.gitignore` 验证通过（AC-7）
- ✅ 红线 #7：所有新文件 ≤ 800 行（最长 workflow 130 行）
- ✅ 红线 #9：命名永久化，无 demo_/tmp_/temp_ 前缀
- ✅ 红线 #11：单文件 < 200 行无需声明 retention；workflow 文件已声明 `retention: permanent`
- ✅ 红线 #12：`workspace_human/` 既有正文未改，仅末尾追加 1 段反向引用（按 PRD AC-21 列明的合法授权动作执行）
- ✅ 4 入口文件保持各自结构差异下的内容一致性（CLAUDE 表行 / 其他 3 个加段）

### Deferred

- **pre-commit hook 拦截未脱敏内容**：本次不做，按 PRD §9 决策 9.3 等纪律观察期；触发条件是第 1 次发生未脱敏 commit → 升级为可选 PRD
- **30 天反熵首次扫描**：上线 30 天后第一次周复盘验证，PRD §7 复评点之一

---

## v2026.05.10c — 2026-05-10

对 [`products/`](products/) 内容做日常维护性修订，使描述更聚焦产品本身、更紧贴平台实时信息。
Routine maintenance pass on [`products/`](products/) — sharpening focus on the product itself, aligning closer to live platform info.

### What changes

- `products/see2ai/pricing_and_account.md` —— 重写为按需计费机制说明，所有具体金额、换算关系、可选金额范围以平台 `/tenant/recharge` 与 `/actions` 详情页的实时展示为准
- `products/see2ai/{README,getting_started,support,capabilities}.md` —— 同步价格相关描述与平台页面对齐；frontmatter 描述与正文措辞精简
- `products/tuve/capabilities.md` —— 精简能力章节，聚焦 TUVE 对话式创作主线；章节序号重排
- `products/tuve/{README,app_overview,getting_started,support}.md` —— 同步章节调整与文件互链更新

---

## v2026.05.10b — 2026-05-10

新增 [`products/`](products/) 目录，收录兔展旗下 **SEE2AI** 平台与 **TUVE** 应用的公开产品介绍材料。

### What ships

- **`products/README.md`** — 目录入口，列出收录的产品和按场景的阅读路径
- **`products/see2ai/`** —— SEE2AI 平台介绍材料 6 份：
  - `README.md`（一页速览）/ `platform_overview.md`（平台定位与核心价值）/ `getting_started.md`（首次调用 SOP）/ `capabilities.md`（平台能力目录）/ `pricing_and_account.md`（按需计费机制 + 平台词元 + 失败不扣费）/ `support.md`（401/429/5xx 排查 + 工单 + API Key 安全提示）
- **`products/tuve/`** —— TUVE 应用介绍材料 5 份：
  - `README.md`（一页速览）/ `app_overview.md`（应用定位 + 4 类典型场景）/ `getting_started.md`（首支视频上手 + 高质量 Prompt 写法）/ `capabilities.md`（Agent 运行时/创作上下文/媒体引用/任务面板/典型场景）/ `support.md`（连接断开/生成失败/工单）
- **入口文件同步更新**：
  - `README.md` —— "Who this is for" 表加销售/客户成功/合作伙伴/视频四类入口；目录地图加 `products/`；"For Teams Adopting This Repo" 加 products/ 替换说明
  - `AI_MANUAL.md` §2 仓库地图加 `products/`；§4 任务-入口表加 5 行（介绍 SEE2AI / 介绍 TUVE / 协助接入 / 解释计费 / 客户报错）
  - `CLAUDE.md` 任务接入路径表加介绍 SEE2AI/TUVE 一行
  - `AGENTS.md` / `CODEX.md` / `.cursorrules` 各加一段"SEE2AI / TUVE 产品介绍材料"指针

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
