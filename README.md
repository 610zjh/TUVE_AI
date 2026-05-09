# TUZHAN_AI · 工作方法手册 / Work-with-AI Playbook

> 这不是某一个项目的代码仓库，而是 TUZHAN 全公司"如何与 AI 协作把工作做完"的工作底座。
> This is not a project codebase. It is TUZHAN's company-wide foundation for **getting work done with AI**.

> **本仓库同时承载了 2026 年内部培训《如何高效用 AI 完成工作》的全部教材**，详见 [`training/`](training/)。
> **This repository also contains the full training materials for the 2026 internal session "Effectively Using AI to Get Work Done"** — see [`training/`](training/).

---

## 这个文件夹是给谁用的 / Who this is for

| 角色 / Role | 你大概率会用到 / What you'll most likely use |
|---|---|
| 销售 Sales | [`workflows/customer_communication/`](workflows/customer_communication/) · [`workflows/research_and_analysis/`](workflows/research_and_analysis/) · [`templates/customer_brief/`](templates/customer_brief/) · [`templates/sales_call_summary/`](templates/sales_call_summary/) |
| 运营 Operations | [`workflows/operations/`](workflows/operations/) · [`workflows/planning/`](workflows/planning/) · [`runbooks/`](runbooks/) · [`templates/weekly_review/`](templates/weekly_review/) |
| 短视频制作 Video Production | [`workflows/content_creation/`](workflows/content_creation/) · [`templates/video_script/`](templates/video_script/) |
| 产品 Product | [`workflows/planning/`](workflows/planning/) · [`workflows/decision_records/`](workflows/decision_records/) · [`templates/prd/`](templates/prd/) · [`workspace_human/prd/`](workspace_human/prd/) |
| 开发 Engineering | [`workflows/engineering/`](workflows/engineering/) · [`projects/`](projects/) · [`issues/`](issues/) · [`runbooks/`](runbooks/) · [`principles/`](principles/) |
| 跨职能协作 Cross-functional | 必读 [`principles/000_CORE_RED_LINES.md`](principles/000_CORE_RED_LINES.md) · [`workflows/ai_basics/`](workflows/ai_basics/) · [`case_studies/`](case_studies/) |

无论什么角色，**第一次打开请先读完 [`workflows/ai_basics/`](workflows/ai_basics/) 这一组（约 30 分钟）**。它解决的是"我怎么和 AI 说话才能让它真的帮上忙"这个共性问题。
Regardless of role, **first-time readers should complete [`workflows/ai_basics/`](workflows/ai_basics/) (~30 min)** — it solves the universal "how do I talk to AI so it actually helps" problem.

---

## 5 分钟快速开始 / 5-minute Quickstart

### 第一步：让你的 AI 工具认识这个文件夹 / Step 1 — Let your AI tool recognize this folder

无论你用 Claude Code / Cursor / Codex / Trae，把整个 `TUZHAN_AI/` 文件夹拖进它的工作目录即可。
Whichever tool you use (Claude Code / Cursor / Codex / Trae), drop the whole `TUZHAN_AI/` folder into its working directory.

四个工具的入口文件已经预先写好：
The four agent entry files are pre-written:

- `CLAUDE.md` — Claude Code 启动时自动读取 / auto-loaded by Claude Code
- `AGENTS.md` — Codex / 多数 OpenAI 系工具读取 / auto-loaded by Codex and most OpenAI-flavored tools
- `.cursorrules` — Cursor 启动时自动读取 / auto-loaded by Cursor
- `CODEX.md` — Trae / 兼容 Codex 协议的工具读取 / for Trae and Codex-compatible tools

四个文件内容是一致的，只是文件名不同——这是为了让你不论用哪个工具，AI 都拿到同样的工作守则。
All four files share the same content, only filenames differ — so the AI gets the same operating rules regardless of tool.

### 第二步：告诉它"先读 AI_MANUAL.md" / Step 2 — Tell it "start by reading AI_MANUAL.md"

打开你的 AI 助手，发第一条消息：
Open your AI assistant and send the first message:

> 请先读 `AI_MANUAL.md` 了解项目导航，然后我会告诉你今天要做什么。
> Please read `AI_MANUAL.md` first to understand the project navigation. Then I'll tell you what we're doing today.

AI 会自己把入口文件、红线、导航地图都串起来。之后你就可以直接说"帮我写一份 X"或者"修一下 Y"。
The AI will chain the entry files, red lines, and navigation map on its own. From there you can say "draft an X" or "fix Y" naturally.

### 第三步：用模板开工 / Step 3 — Start work from a template

不要让 AI 凭空发挥。从 [`templates/`](templates/) 里挑最贴近你今天工作的模板，让 AI 帮你填。
Don't let AI improvise from scratch. Pick the template closest to today's work from [`templates/`](templates/) and have AI fill it in.

例如 / For example:
- 写一份给客户的项目简报 → 用 [`templates/customer_brief/`](templates/customer_brief/)
- 把今天的客户电话整理成跟进材料 → 用 [`templates/sales_call_summary/`](templates/sales_call_summary/)
- 给一支 30 秒短视频写脚本 → 用 [`templates/video_script/`](templates/video_script/)
- 写一份产品需求文档 → 用 [`templates/prd/`](templates/prd/)

---

## 整体目录地图 / Repository Map

```
TUZHAN_AI/
├── AI_MANUAL.md              ← 项目总导航（AI 第一个读的文件）
│                                Project navigation (the first file AI reads)
├── principles/               ← 全员通用的红线和准则
│                                Company-wide red lines and principles
├── workflows/                ← 按工作类型组织的"怎么做"指南
│                                "How to" guides organized by work type
├── templates/                ← 可直接复制使用的工作模板
│                                Reusable work templates (PRD, brief, script, etc.)
├── case_studies/             ← 跨职能真实工作案例（替换为你团队的真实案例）
│                                Cross-functional worked examples (replace with your team's)
├── workspace_human/          ← 人写的 PRD / 会议纪要（AI 只读）
│                                Human-authored PRDs and meeting notes (AI read-only)
├── issues/                   ← 全公司 Bug / 工艺问题登记本（SSOT）
│                                Company-wide issue tracker (single source of truth)
├── runbooks/                 ← 操作手册（部署 / 接客 / 上下游交接）
│                                Operational runbooks (deploys, onboarding, handoffs)
├── projects/                 ← 你的实际项目（包含一个完整可跑的样例项目）
│                                Your actual projects (includes one complete working sample)
├── training/                 ← 内部培训《如何高效用 AI 完成工作》全部材料
│                                Full materials for the internal "Use AI Effectively" training
├── CLAUDE.md / AGENTS.md /   ← 给四种主流 AI 工具的入口文件
│   .cursorrules / CODEX.md     Entry files for the four mainstream AI tools
├── setup.sh / setup.ps1      ← 一键完成 git / 钩子 / 目录初始化
│                                One-shot init for git / hooks / directories
└── README.md                 ← 你正在看的这份
```

---

## 这个仓库背后的几条核心信念 / The Beliefs Behind This Repo

1. **AI 是有能力的同事，不是搜索引擎。** 你怎么对待一位刚入职但很聪明的同事——给他背景、给他目标、让他读相关材料、有疑问就问——AI 也一样。
   **AI is a capable colleague, not a search engine.** Treat it like a smart new hire: give context, give goals, point at relevant material, expect it to ask back when unsure.

2. **流程比聪明更重要。** 一个普通方案 + 严密流程 > 一个绝妙点子 + 凭直觉操作。这个仓库里的红线、模板、工作流就是把"严密流程"做成了肌肉记忆。
   **Process beats brilliance.** A solid solution executed against a tight process > a brilliant idea executed by intuition. The red lines, templates, and workflows here turn the tight process into muscle memory.

3. **写下来的事才算数。** PRD、Bug、决策记录、会议结论——口头上的不算。这不是官僚主义，是为了让你 6 个月后回来还能搞清楚自己当时为什么这么做。
   **If it's not written, it didn't happen.** PRDs, bugs, decision records, meeting outcomes — verbal doesn't count. This is not bureaucracy; it's so future-you (6 months later) can still tell why you made this call.

4. **保密线就是底线。** 客户数据、内部代号、模型 ID、合同金额——出 TUZHAN 一步都不能跟随到 AI 的上下文里。具体规定见 [`principles/subs/confidentiality.md`](principles/subs/confidentiality.md)。
   **Confidentiality is the floor.** Customer data, internal codenames, model IDs, contract values — none of these step out of TUZHAN into an AI context. See [`principles/subs/confidentiality.md`](principles/subs/confidentiality.md).

5. **长期主义、业界标准、紧扣核心目标。** 任何决策当红线没明说时，就回到这一条。详见 [`principles/subs/supreme_decision_principle.md`](principles/subs/supreme_decision_principle.md)。
   **Long-term thinking, industry-standard methods, locked on core objectives.** When a specific red line is silent, fall back here. See [`principles/subs/supreme_decision_principle.md`](principles/subs/supreme_decision_principle.md).

---

## 给培训参与者 / For Training Attendees

如果你是从培训现场拷贝/下载到这份资料的——欢迎。
If you got this from the training session — welcome.

- 第一部分（全员场，约 90 分钟）的所有材料在 [`training/part_1_for_everyone/`](training/part_1_for_everyone/)
  All Part 1 (everyone, ~90 min) materials are in [`training/part_1_for_everyone/`](training/part_1_for_everyone/)
- 第二部分（开发场，约 90 分钟）的所有材料在 [`training/part_2_for_developers/`](training/part_2_for_developers/)
  All Part 2 (developers, ~90 min) materials are in [`training/part_2_for_developers/`](training/part_2_for_developers/)
- 现场演示的逐步脚本在 [`training/live_demo_walkthrough/`](training/live_demo_walkthrough/)
  The step-by-step live-demo script is in [`training/live_demo_walkthrough/`](training/live_demo_walkthrough/)

培训之后，[`training/post_conference/self_study_path_for_attendees.md`](training/post_conference/self_study_path_for_attendees.md) 给出了一条 "1 小时 / 1 天 / 1 周" 的自学路径。
After the session, [`training/post_conference/self_study_path_for_attendees.md`](training/post_conference/self_study_path_for_attendees.md) gives a "1-hour / 1-day / 1-week" self-study path.

---

## 给二次复用这份仓库的人 / For Teams Adopting This Repo

如果你是 TUZHAN 之外的合作伙伴，把这个文件夹拿去搭你自己团队的 AI 工作底座，这是被鼓励的。
If you're a partner outside TUZHAN adopting this folder for your own team's AI baseline — encouraged.

替换清单 / Replacement checklist:
- 全文搜索 `TUZHAN` 改成你的公司名 / Search-and-replace `TUZHAN` with your company name
- [`case_studies/`](case_studies/) 里的三个跨职能案例换成你团队的真实案例
  Replace the three cross-functional case studies in [`case_studies/`](case_studies/) with your team's
- [`projects/`](projects/) 里的样例项目可以直接删掉，换上你自己的项目
  Delete the sample project in [`projects/`](projects/) and put yours in
- [`workspace_human/prd/`](workspace_human/prd/) 留着空目录，从你下一个真实需求开始往里写
  Leave [`workspace_human/prd/`](workspace_human/prd/) empty; populate it with your next real requirement
- 培训材料 [`training/`](training/) 可以保留作为新员工 onboarding 资料，也可以替换成你公司的培训内容
  Keep [`training/`](training/) for new-hire onboarding, or replace with your own training content

红线、工作流、模板的内容是公司中性的——基本可以原样使用。
The red lines, workflows, and templates are company-neutral — usable as-is.

---

## 版本与变更 / Versions and Changes

每次发版的内容、验证结果、刻意延后项见 [CHANGELOG.md](CHANGELOG.md)。
Per-release contents, verification results, and deferred items: [CHANGELOG.md](CHANGELOG.md).

当前版本：**v1.0**（2026-05-10，首次公开发布）。
Current version: **v1.0** (2026-05-10, first public release).

---

## License

本仓库内容采用 CC BY 4.0 协议（见 [LICENSE](LICENSE)）。意味着你可以自由复用、修改、商用，只需要标注来源（"基于 TUZHAN_AI 工作方法手册"）。
Released under CC BY 4.0 (see [LICENSE](LICENSE)). You may reuse, modify, and use commercially with attribution ("based on TUZHAN_AI Work-with-AI Playbook").
