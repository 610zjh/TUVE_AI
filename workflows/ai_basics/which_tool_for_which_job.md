# 不同任务用哪个 AI 工具 / Which AI Tool for Which Job

> TUZHAN 内部支持的四个工具：Claude Code / Cursor / Codex / Trae。这份文件给一个粗略的"什么场景用哪个"经验。
> Four tools supported internally: Claude Code / Cursor / Codex / Trae. Rough heuristic for which to pick.

---

## 一句话 / One Line

**不用纠结。四个工具读的是同一份入口文件，都遵循同一套红线和工作流。**
**Don't agonize. All four tools read identical entry files and follow the same red lines and workflows.**

实际选哪个，看你**今天的任务**和**你的工作环境**。
Pick by **today's task** and **your environment**.

---

## 四工具速览 / Quick Glance

| 工具 / Tool | 强项 / Strength | 入口文件 / Entry file |
|---|---|---|
| **Claude Code** | 长文档审阅、多步任务、Skill 体系 | `CLAUDE.md` |
| **Cursor** | 代码内联编辑、IDE 级体验 | `.cursorrules` |
| **Codex** | 命令行批量任务、脚本化 | `AGENTS.md` |
| **Trae** | 中文体验、本地化插件 | `CODEX.md` |

---

## 按场景挑工具 / Pick by Scenario

### 场景：写一份新文档 / 改长文档 / 多步推理

**首选 Claude Code**

理由：
- 长文档读取 / 跨文件引用强 / Strong long-doc handling and cross-file referencing
- 多步任务的中途暂停 / 重组能力强 / Strong multi-step pause and recompose
- Skill 体系适合做反复性任务 / Skill system fits repeating tasks

例子：写 PRD、写客户简报、整理客户访谈、写月度复盘
Examples: writing PRDs, customer briefs, interview synthesis, monthly reviews

### 场景：在 IDE 里改代码、加新函数、refactor

**首选 Cursor**

理由：
- 内联编辑（Cmd+K）顺手 / Inline edit fluent
- 项目内 @-mention 文件 / 代码符号方便 / Easy in-project @-mention
- 与你的 Git / 终端集成最紧 / Tightest Git/terminal integration

例子：改一个函数、加一个 endpoint、refactor 一个模块
Examples: editing a function, adding an endpoint, refactoring a module

### 场景：批量任务 / 在 CI / 自动化脚本里

**首选 Codex**

理由：
- 命令行原生（`codex run -- <task>`）/ Native CLI
- 脚本化、可组合 / Scriptable, composable
- 在没有交互终端的场景（CI）也能跑 / Works in non-interactive contexts (CI)

例子：批量改 100 个文件的命名、CI 里自动审 PR、跨仓库扫红线
Examples: batch-renaming 100 files, auto-reviewing PRs in CI, scanning red lines cross-repo

### 场景：中文 IDE 体验 / 国内本地化插件优先

**首选 Trae**

理由：
- 中文 UI 完整，错误提示中文 / Full Chinese UI and error messages
- 国内本地化（火山引擎模型支持）/ China-localized (Volcano Engine model)
- 与 Codex 兼容，可以无缝切换 / Codex-compatible, swap freely

例子：中文为主的内容创作、国内合作伙伴对接、本地化 demo
Examples: Chinese-first content, China-partner integration, local demos

---

## 何时混用 / When to Mix

很多任务自然横跨多个工具：
Many tasks naturally span multiple tools:

```
任务：实现一个 PRD-XXXX
1. 在 Claude Code 里读完 PRD、起草实施计划（长文档 + 多步推理）
2. 切到 Cursor 在 IDE 里写代码、跑测试（IDE 体验）
3. 切到 Codex 在 CI 里批量跑回归（脚本化）
4. 回 Claude Code 写"实施记录"段补到 PRD 末尾（长文档）
```

四工具用的是同一个仓库 + 同一个红线 + 同一份入口文件。切换成本接近 0。
All four read the same repo + same red lines + same entry file. Near-zero switching cost.

---

## 何时不要混用 / When NOT to Mix

- **同一个任务的同一阶段**：选一个干完，不要切来切去 / Same task same stage: pick one, finish; don't toggle
- **测试服 / 生产部署**：定一个工具作为"那台机器跑得最稳的"，其他工具用来辅助 / Staging/prod deploy: pick the most-stable tool as the deployer; others assist

---

## 不要做的 3 件事 / 3 Things NOT to Do

### 1. 不要换工具来"试运气" / Don't switch to "try a different luck"

如果 Cursor 给你的代码是错的，**不是**"换 Claude Code 试试"。
If Cursor gave wrong code, the answer is **not** "let me try Claude Code instead".

正确动作：分析为什么错（是指令不清楚？还是该任务模型本身能力不足？），按 [`common_failure_modes.md`](common_failure_modes.md) 修复。
Right action: analyze why (unclear instruction? model unfit?), fix per `common_failure_modes.md`.

### 2. 不要在四个工具的入口文件里加冲突的内容 / Don't put conflicting content in the four entry files

四个入口文件（`CLAUDE.md` / `AGENTS.md` / `CODEX.md` / `.cursorrules`）应该**保持一致**。它们是同一份内容的四个副本（适配各自工具的元信息略有差异，但红线、流程、动作清单都相同）。
The four entry files should **stay consistent**. Same content, four copies (with minor tool-specific metadata differences but identical red lines / processes / action lists).

如果加新规矩，**四份一起加**。
Add new rules to all four together.

### 3. 不要让某个工具读不到关键文件 / Don't let a tool miss key files

每个工具都应该能读：
Each tool should be able to read:
- `AI_MANUAL.md`
- `principles/000_CORE_RED_LINES.md`
- 自己的入口文件 / Its own entry file
- `issues/known.md` / `workspace_human/prd/`

测试方法：开新对话，问"现在 known.md 里有几条 P1 的 Bug？"如果它说"我读不到这个文件"，说明工作目录配置有问题。
Test: in a fresh chat, ask "how many P1 bugs in known.md?" — if it says "can't read this file", working-directory config is wrong.

---

## 工具的"模型"在哪 / Where Is the Model?

注意：这四个工具背后用的**底层模型**也可能不同（Claude / GPT / Gemini / 国内模型）。
Note: the **underlying model** behind each tool may differ (Claude / GPT / Gemini / domestic).

| 工具 / Tool | 默认模型 / Default model | 可换模型 / Switchable |
|---|---|---|
| Claude Code | Claude (Anthropic) | 不支持换 / Fixed |
| Cursor | 用户可选（Claude / GPT / Gemini）/ User-selectable | 是 / Yes |
| Codex | OpenAI GPT 系 / OpenAI GPT family | 限定 OpenAI / OpenAI only |
| Trae | 火山引擎模型 / Volcano Engine | 限定 / Limited |

如果某个工具表现差，**先换它的模型**而不是换工具。
If a tool underperforms, **switch its model first**, not the tool itself.

---

## 速查表 / Cheat Table

| 你想做 / You want to | 用 / Use |
|---|---|
| 写 PRD / 改长文档 | Claude Code |
| 在 IDE 改代码 | Cursor |
| 批量任务 / CI | Codex |
| 中文为主 / 国内插件 | Trae |
| 不知道选哪个 | Claude Code（默认安全选择）|

---

## 工具会变，红线不变 / Tools Change, Red Lines Don't

明年可能有新的 AI 工具出现。这份文件会更新。
New AI tools may emerge next year. This file gets updated.

但**红线**（在 [`principles/000_CORE_RED_LINES.md`](../../principles/000_CORE_RED_LINES.md)）跨工具有效。换工具不换规矩。
But **red lines** (in `principles/000_CORE_RED_LINES.md`) hold across tools. Switching tools doesn't switch rules.
