---
name: 主动反熵 / Anti-Entropy Discipline
description: retention class、800 行双向闸、COMPACT 提案、AI 永不自删 / Retention class, bidirectional 800-line cap, COMPACT proposal flow, AI never self-deletes
type: permanent
retention: permanent
retention_reason: 长期主义在仓库结构上的具体落地 / Operationalizes long-term thinking at repo level
---

# 主动反熵 / Anti-Entropy Discipline

## 一句话 / One Line

**长期主义要求项目可被长期导航。** 文件有归宿、有寿命、有缩页机制。
**Long-term thinking requires the project to remain navigable long-term.** Files have homes, lifespans, and rollup paths.

---

## 1. Retention Class / 保留分类

任何 ≥ 200 行的 Markdown，或 dated/sequential archive 目录下的文件，**必须**在 YAML frontmatter 声明：
Any Markdown ≥ 200 lines, or files under dated/sequential archive directories, **must** declare in YAML frontmatter:

```yaml
---
name: <文件标题 / title>
description: <一句话描述 / one-line description>
type: <类型 / type>
retention: permanent | rollup | ephemeral
retention_reason: <为什么是这一类 / why this class>
---
```

### 三类含义 / Three Classes

| 类别 / Class | 含义 / Meaning | 例子 / Examples |
|---|---|---|
| **permanent** | 长期保留，公司宪法级 / Long-term, constitution-level | 红线、ADR、PRD（已落地的）、客户案例复盘 / Red lines, ADRs, landed PRDs, customer reviews |
| **rollup** | 周期性归档汇总 / Periodically rolled up | 周报、月报、daily 日志（按周 / 月归档为单份汇总）/ Weekly / monthly reports, daily logs |
| **ephemeral** | 一次性、用完可作废 / One-shot, throwaway after use | 单次任务的临时笔记、调试快照 / Temp notes, debug snapshots |

### 判断标准 / Decision Rule

> **如果文件消失，AI 能否仅凭代码 + 数据 + git log 重建？**
> **If this file vanished, could AI reconstruct it from code + data + git log alone?**
>
> 能 → 可以是 rollup 或 ephemeral / Yes → can be rollup or ephemeral
> 不能 → 必须 permanent / No → must be permanent

人独有的判断、对真实事件的回溯、决策的取舍记录——都不能从代码重建，是 permanent。
Human-exclusive judgments, retrospectives, decision tradeoff records — irreproducible from code, must be permanent.

---

## 2. 双向 800 行（红线 #7 + #11）/ Bidirectional 800-Line Cap

### 上限 / Upper bound

任何文件 ≤ 800 行。超过 → 拆分。
Any file ≤ 800 lines. Over → split.

### 下限对 AI-loaded canonical manuals / Lower-cap exception

下面这些"AI 每次自动读"的核心入口文件适用 800 行硬上限：
The following "AI auto-loaded" canonical manuals apply the 800-line hard cap:

- `AI_MANUAL.md`
- `CLAUDE.md` / `AGENTS.md` / `CODEX.md` / `.cursorrules`
- `principles/000_CORE_RED_LINES.md`
- `principles/subs/*.md`
- `README.md`

超过 → 提 `COMPACT-NNNN` 拆分提案（见下）。
Over → file `COMPACT-NNNN` rollup proposal (see below).

### 例外目录 / Exempt Directories

- 纯数据文件（CSV, JSON, 模型参数）/ Pure data files
- vendored 第三方代码 / Vendored 3rd-party code
- 自动生成的 schema / 迁移 / Auto-generated schema / migrations

例外文件需在仓库根 `.codeowners` 或 [`000_CORE_RED_LINES.md`](../000_CORE_RED_LINES.md) 显式登记。
Exempt files must be explicitly listed in `.codeowners` or `000_CORE_RED_LINES.md`.

---

## 3. COMPACT-NNNN：压缩即 PRD / Compaction Is a PRD

任何**rollup / 归档 / 拆分**动作，必须先在 [`workspace_human/prd/compaction/COMPACT-NNNN_*.md`](../../workspace_human/prd/) 写提案，等人授权再执行。
Any **rollup / archive / split** action: first propose in `workspace_human/prd/compaction/COMPACT-NNNN_*.md`, then await human authorization.

提案模板 / Proposal template:

```markdown
# COMPACT-NNNN: <一句话标题>

- 起草人 / Author: <name>
- 时间 / Date: 2026-XX-XX

## 触发原因 / Trigger
<某文件超 800 行 / 某目录文件累积过多 / 某 dated archive 占空间过大 ...>

## 当前状态 / Current State
- 文件路径 / Path: ...
- 当前行数 / 文件数 / Current size
- 进入哪个 retention class / Current retention class

## 拟拆分 / 归档方案 / Proposed Split / Rollup
- 把 §X-Y 单独拆成 file_a.md
- 把 §Z-W 拆成 file_b.md
- file_a.md 更新到 [`AI_MANUAL.md`](../AI_MANUAL.md) §X 导航

## 链接更新清单 / Link Update Checklist
- [ ] 仓库内所有引用本文件的地方
- [ ] [`AI_MANUAL.md`](../../AI_MANUAL.md) §4 任务-入口表
- [ ] 上层目录的 README

## 不拆分会怎样 / If We Don't Split
（说明继续放任会带来的成本——比如 AI 一次读不完、新人查找慢）

## 备份方案 / Backup
- 拆分前的完整版本保存到 git tag `pre-compact-NNNN`
- AI 不直接 rm 任何文件——只 mv 到 archive/ 子目录
```

---

## 4. AI 永不自删 / AI Never Self-Deletes

哪怕 retention=ephemeral，AI 也只允许：
Even retention=ephemeral, AI may only:

- ✅ 把文件**挪到 git-only 路径**（例如 `archive/2026/Q2/` 子目录）/ Move file to a git-only path
- ✅ 在 `.gitignore` 把某路径标为不入库 / Mark paths in `.gitignore` to exclude from repo

AI **不允许**：
AI may **NOT**:
- ❌ `rm`、`git rm`、`del` 任何已被人放进仓库的文件
- ❌ 把文件清空成 0 字节再说"我没删"

理由：人放进来的东西可能比 AI 以为的更重要。挪比删可逆。
Reason: things humans put in may be more important than AI assumes. Moves are reversible; deletes aren't.

---

## 5. 双重保护目录 / Double-Protected Directories

[`principles/`](..) 和 [`workspace_human/`](../../workspace_human/) 不在自动压缩 / 反熵动作的范围。
[`principles/`](..) and [`workspace_human/`](../../workspace_human/) are out-of-scope for automatic rollup / anti-entropy actions.

任何对这两个目录的结构性改动（拆分 / 合并 / 重命名）都需要**人逐次授权**，AI 不在没有具体授权的情况下提议针对这两个目录的批量处理。
Any structural change to these directories (split / merge / rename) requires **per-action human authorization**. AI doesn't propose bulk processing for them without specific authorization.

---

## 6. 默认 retention 表 / Default Retention Table by Directory

按目录默认 retention class（可被文件 frontmatter 显式覆盖）：
Default by directory (overridable by file frontmatter):

| 目录 / Directory | 默认 retention / Default | 备注 / Notes |
|---|---|---|
| `principles/` | permanent | 公司宪法 |
| `workspace_human/prd/` | permanent | 已落地的 PRD |
| `workspace_human/prd/compaction/` | permanent | COMPACT 提案的历史 |
| `workspace_human/meetings/` | permanent | ADR、复盘 |
| `workspace_human/meetings/weekly/` | rollup | 每月底归一份月度汇总 |
| `issues/known.md` | permanent | 文件本身永久；条目移走 |
| `issues/fixed/` | rollup | 每年底归一份年度汇总，原始日文件保留索引 |
| `runbooks/` | permanent | 操作手册 |
| `case_studies/` | permanent | 教学价值长期 |
| `workflows/` | permanent | 工作流方法论 |
| `templates/` | permanent | 模板 |
| `projects/<P>/` | 跟随项目自身 / per project | |
| `training/` | permanent | 培训教材一直能复用 |

---

## 7. 反熵的频率 / Cadence

| 周期 / Cadence | 动作 / Action |
|---|---|
| 每次新建文件 / On creation | 决定 retention class（≥ 200 行的必须声明 frontmatter） |
| 每周五下午 / Friday afternoon | 扫一遍本周新增 ephemeral 文件，看哪些可以归档 |
| 每月月底 / End of month | rollup 类目录做月度归档（如果到达归档点） |
| 每季度 / Quarterly | permanent 文件审查：还是 permanent 吗？有没有过时？ |
| 每年年底 / Year-end | 年度归档：fixed/ 按年汇总、weekly meeting notes 按年汇总 |

每次执行的反熵动作都要走 COMPACT-NNNN 提案。
Each execution goes through a COMPACT-NNNN proposal.

---

## 8. 反熵不是为了"看起来整洁" / Anti-Entropy ≠ Tidiness Theater

警惕"为了整洁而整洁"的反熵：
Watch out for tidiness-for-tidiness anti-entropy:

❌ "我觉得文件太多了，归档一下" → 没有具体的导航痛点
**问题**：归档动作本身是有成本的（搬迁、链接断裂、读者迷路）。没痛点就不要动。
**Issue**: archiving has costs (relocation, broken links, reader confusion). No pain → no move.

✅ "AI 一次读 800 行后内存不够，需要拆分" → 有具体的可量化痛点
**Right**: concrete, quantifiable pain.

每个 COMPACT 提案的"触发原因"段必须写**具体的、可量化的痛点**，不是"我感觉应该整理"。
Every COMPACT proposal's "Trigger" section must state **concrete quantifiable pain**, not "I feel we should clean up."

---

## 9. 当反熵和"用户当前急要"冲突 / When Anti-Entropy Conflicts with User's Immediate Need

用户："这个文件 1200 行了，但你现在帮我加一段"——这时不要因为超 800 行就拒绝。
User: "this file is 1200 lines, but please add a section right now" — don't refuse just because of the cap.

正确动作：
Right action:
1. 帮用户加 / Help the user add the section
2. 加完后**主动**说："这个文件现在 1230 行，超过 800 行硬上限。是否需要我起草一份 COMPACT-NNNN 提案？" / After finishing, **proactively** say "this file is now 1230 lines, over the 800-line cap. Should I draft a COMPACT-NNNN proposal?"
3. 等用户决定 / Wait for the user's call

不要因为反熵规矩**当下就**拒绝完成任务。反熵是长期纪律，单次任务里它的优先级低于"先把今天的活干完"。
Don't refuse the immediate task **right now** for the anti-entropy rule. Anti-entropy is long-term discipline; in a single task it's lower priority than "get today's work done."
