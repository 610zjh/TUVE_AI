---
name: PRD 与需求 / PRD and Requirements
description: PRD 怎么写、谁写、AI 能改哪些段、收尾五件套是什么 / How PRDs are written, by whom, what AI can edit, the five-part closeout
type: permanent
retention: permanent
retention_reason: 公司从需求到落地的纪律核心 / Core discipline from requirement to delivery
---

# PRD 与需求 / PRD and Requirements

## 红线 #5 重申 / Red Line #5 Restated

**任何代码改动必须对应一份 PRD 或一条 Bug 条目。**
**Every code change must map to a PRD or a Bug entry.**

**禁止**篡改 [`workspace_human/prd/`](../../workspace_human/prd/) 里人已经写好的 PRD 主体（背景 / 需求 / 验收段）。AI 只可在文件**末尾**追加被授权的"实施记录"段。
**Forbidden** to tamper with the body (context / requirements / acceptance criteria) of a human-written PRD. AI may only append an authorized "Implementation Log" at the **bottom**.

---

## 谁写 PRD / Who Writes PRDs

| 来源 / Source | 谁写 / Author |
|---|---|
| 产品需求 / Product feature | 产品 / 产品负责人 / Product / PM |
| 客户合作模式 / Customer engagement model | 销售 + 产品 / Sales + Product |
| 内部工具 / Internal tooling | 提需求方 + 产品 / Requestor + Product |
| 紧急修复 / 临时方案 / Hotfix or temporary | 紧急情况下，工程师可起草，但 24 小时内必须有人接手补正式 PRD / In urgencies, engineer drafts; within 24h someone must take over and complete a proper PRD |

AI 不写 PRD（人是 PRD 的责任人）。AI 可以**协助起草**，但最终保存进 [`workspace_human/prd/`](../../workspace_human/prd/) 的版本必须由人审过、人定稿。
AI does not write PRDs (humans own PRDs). AI may **help draft**, but the version saved into [`workspace_human/prd/`](../../workspace_human/prd/) must be human-reviewed and human-finalized.

---

## PRD 的标准结构 / Standard PRD Structure

模板在 [`templates/prd/`](../../templates/prd/)。骨架：
Template at [`templates/prd/`](../../templates/prd/). Skeleton:

```markdown
# PRD-XXXX: <一句话标题>

- 起草人 / Author: <Name>
- 起草日期 / Date: 2026-XX-XX
- 状态 / Status: 草稿 / 评审中 / 已批准 / 实施中 / 已上线 / 已废弃
- 关联客户 / 业务线 / Related customer / business line: ...

## 1. 背景与动机 / Context and Motivation
（为什么要做这件事；不做会怎样）

## 2. 目标与非目标 / Goals and Non-Goals
- ✅ 目标：...
- ❌ 非目标：...（明确写清楚不解决什么，避免范围漂移）

## 3. 用户故事 / User Stories
作为 <角色>，我希望 <能力>，以便 <价值>。

## 4. 需求详述 / Requirements
4.1 功能需求 ...
4.2 非功能需求（性能、合规、可观测性、回退）...

## 5. 验收标准 / Acceptance Criteria
（具体可验证的、不模糊的指标）

## 6. 主次审视 / Priority Audit （仅 paywall / feature gate / 分层 PRD 必填）
（按红线 #15，写"这件事是不是把产品价值和商业包装的主次搞反了"）

## 7. 时间表 / Timeline
（关键里程碑 + 复评点）

## 8. 风险与对策 / Risks and Mitigations
...

## 9. 决策记录 / Decisions
（PRD 进行中冒出的取舍点。同 ADR 格式，但内嵌）

## 10. 实施记录 / Implementation Log（AI 可在此追加）
- 2026-XX-XX：完成功能 A，链接到 commit XXXXXX
- ...

## 11. 完成快照 / Completion Snapshot
（按"五件套"逐项打勾的快照，对照原始需求一条条核）
```

---

## 五件套：开发后必做 / The Five-Part Closeout

红线 #10。任何 PRD 实施完，**必须**完成下面五件事，缺一项不许说"完工"：
Red Line #10. After finishing any PRD, **must** complete the following five; missing any → cannot say "done":

### 1. 补测试 / Add Tests

- 新功能至少有一个**冒烟测试**（最快路径上的端到端跑一遍能通）/ At least one **smoke test** for the happy path
- 修 Bug 必须有一个**回归测试**（重现这个 Bug 的输入 → 修复后输出对）/ Bugs require a **regression test** (input that reproduces the bug → output is now correct)
- 同步清掉**反向断言**测试（红线 #13）/ Clean up **reverse-assertion** tests (Red Line #13)

### 2. 登记版本 / Register Version

- 在 [`runbooks/`](../../runbooks/) 或 PRD 内的"实施记录"里写明：版本号 / 上线时间 / 主要改动 / Note version, deploy time, main changes in [`runbooks/`](../../runbooks/) or the PRD's Implementation Log
- 如果是面向客户的版本，**主要改动**段必须用客户面文案口径（见红线 #2）/ If customer-facing, the changes section uses customer-facing copy standards (Red Line #2)

### 3. PRD 完成快照 / PRD Completion Snapshot

- 回到原始 PRD 的"验收标准"段，逐条对照检查 / Walk through the PRD's Acceptance Criteria item-by-item
- 在"完成快照"段写：每条验收 ✅ 通过 / ⚠️ 部分 / ❌ 未做 / In Completion Snapshot, mark each ✅ pass / ⚠️ partial / ❌ not done
- 对 ⚠️ 和 ❌ 的，**必须**写入 [`issues/known.md`](../../issues/known.md) 留痕，不许默默不提 / For ⚠️ and ❌, **must** record into [`issues/known.md`](../../issues/known.md); silent omission is forbidden

### 4. 更新导航 / Update Navigation

- 如果加了新工作流文件 → 更新 [`AI_MANUAL.md`](../../AI_MANUAL.md) §4 任务-入口表 / If new workflow files were added → update [`AI_MANUAL.md`](../../AI_MANUAL.md) §4 task-to-entry table
- 如果改了 [`runbooks/`](../../runbooks/) → 看是否需要顶部的目录索引同步 / If [`runbooks/`](../../runbooks/) changed → sync any top-level index

### 5. Bug 移位 / Bug Reclassification

- 这次 PRD 修掉的所有 Bug，从 [`issues/known.md`](../../issues/known.md) 移到 [`issues/fixed/YYYY-MM-DD.md`](../../issues/fixed/) / Move all bugs fixed in this PRD from `known.md` to `fixed/YYYY-MM-DD.md`
- 移位时**整条搬过去**，不只是写"修了 Bug-X"——历史信息全部保留 / Move the **whole entry**, not just "fixed Bug-X" — preserve full history

---

## "实施记录"段的写法 / How to Write the Implementation Log

[`workspace_human/prd/PRD-XXXX_*.md`](../../workspace_human/prd/) 文件**末尾**追加，AI 可写：
Append at the **end** of [`workspace_human/prd/PRD-XXXX_*.md`](../../workspace_human/prd/), AI may write:

```markdown
## 实施记录 / Implementation Log

### 2026-04-23（开工）/ Kickoff
- 已读：本 PRD §1-§5
- 起草实施路径：分 3 阶段 ...
- 不确定点（已问产品确认）：...

### 2026-04-25 第一次里程碑 / Milestone 1
- 完成功能 A，commit `abc1234`
- 验证：所有冒烟测试通过

### 2026-04-29 中途决策 / Mid-flight Decision
- 在实施过程中发现 §4.2.3 的指标"P95 < 500ms"在当前架构下做不到
- 与产品讨论后决定：放宽到 P95 < 800ms，作为 v1 验收标准；P95 < 500ms 进 v2 排期
- 已同步更新 §5 验收标准（产品改的，非 AI 改）

### 2026-05-02 完成 / Completed
（在 §11 完成快照里逐条核对）
```

要点：
- **每个里程碑都有时间戳** / Each milestone is timestamped
- **中途决策必须落字回 PRD**——不能只在脑子里 / Mid-flight decisions go back to the PRD, not just in your head
- **如果中途要改 PRD 主体段，由人改，AI 只在实施记录里反映"已被人更新"** / If the PRD body needs updating mid-flight, **a human** edits the body; AI only logs "body updated by X"

---

## "改 PRD 主体"的合法路径 / Legitimate Path to Update PRD Body

需求变化是常态。但是改 PRD 主体段（背景 / 需求 / 验收）必须满足：
Requirements drift is normal. But editing the PRD body (context / requirements / acceptance) requires:

1. **由 PRD 起草人或产品负责人改** / Edited by the PRD author or PM
2. **改动必须保留 git 历史**（不要"先删旧的再写新的"，要在原段下 strikethrough + 加新段）/ Changes preserve git history (don't "delete old, write new" — strikethrough old + add new)
3. **改完发到相关人对齐**（销售 / 工程 / 视频谁受影响通知谁）/ After editing, broadcast to affected parties (sales / eng / video as applicable)
4. **状态如果原本是"已批准"或"实施中"，要重新走一次评审**——你不能在落地一半时偷偷加一项需求 / If status was Approved or In Progress, re-review — you can't sneak in a new requirement mid-execution

AI 不参与上面任何一步。AI 在实施记录里**反映**主体被更新这件事即可。
AI doesn't participate in any of the above. AI just **logs** that the body was updated.

---

## 紧急 PRD（hotfix）/ Emergency PRD (Hotfix)

线上故障 / 客户急用 / 法务紧急要求等情况：
Production incidents / customer urgencies / legal demands:

1. 工程师**先按红线 #14 看日志，止损**（参考 [`subs/deployment_and_ops.md`](deployment_and_ops.md)）/ Engineer first **looks at logs and mitigates** per Red Line #14
2. 同时在 [`workspace_human/prd/`](../../workspace_human/prd/) **占一个 PRD-XXXX 编号 + 一句话占位**，标 `Status: Emergency` / Reserve a PRD-XXXX number with a one-liner placeholder, status `Emergency`
3. **24 小时内**由产品 / 受影响业务方接手补正式 PRD 主体 / Within 24h, product / affected stakeholder takes over and writes the proper PRD body
4. 完成后走五件套 / Five-part closeout follows

不允许：
Disallowed:
- ❌ 紧急 → 修完就完了，不补 PRD / Emergency → fix → done, no PRD ever
- ❌ 紧急 → 一直挂着 `Emergency` 状态超过 7 天 / Stays `Emergency` for > 7 days

---

## "完工"这个词 / The Word "Done"

**任何一项**五件套缺失，**禁止**用：
**If any of the five parts is missing, BANNED words include**:

- "完工 / Done"
- "全部搞定 / All set"
- "上线了 / Shipped"
- "已经发布 / Released"
- "圆满完成 / Successfully completed"

允许的措辞：
Allowed phrasings:
- "代码已合入主干，待补 X / Y" / "Merged to main, X / Y still pending"
- "功能可用，缺 X 的测试覆盖" / "Feature works; missing X test coverage"
- "已上线测试服，正式服待 X" / "Up on staging; prod gated on X"

诚实地说"剩 X 没做"比说"完工"再被人发现 X 没做强 100 倍。
"X is still pending" honestly is 100× better than saying "done" and being caught later.
