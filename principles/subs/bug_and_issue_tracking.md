---
name: Bug 与问题追踪 / Bug and Issue Tracking
description: 全公司只有两个登记位置——issues/known.md（未修）+ issues/fixed/YYYY-MM-DD.md（已修） / The whole company has only two issue locations
type: permanent
retention: permanent
retention_reason: 单一真相源是防"散落多处真相→失控"的关键 / SSOT is the key to prevent "truth scattered → out of control"
---

# Bug 与问题追踪 / Bug and Issue Tracking

## 红线 #4 重申 / Red Line #4 Restated

全公司有且只有**两个**登记 Bug / 问题的位置：
The whole company has **exactly two** locations for tracking bugs / issues:

- 未修 / Open: [`issues/known.md`](../../issues/known.md)
- 已修 / Closed: [`issues/fixed/YYYY-MM-DD.md`](../../issues/fixed/)（按日归档；同一天多条追加同一份）/ archived by day; multiple same-day entries appended to one file

修复后**整条**从 known 移到 fixed。
After a fix, move the **whole entry** from known to fixed.

不允许把 Bug "也存一份"在邮件、Slack、个人笔记、其他文档里。多份真相 = 失控的开始。
Forbidden to "also keep a copy" in emails, Slack, personal notes, other docs. Multi-source truth = the start of going out of control.

---

## "问题"包括什么 / What Counts as an "Issue"

不只是代码 Bug。下面这些**都**进 [`issues/known.md`](../../issues/known.md)：
Not only code bugs. All of these go into [`issues/known.md`](../../issues/known.md):

| 类型 / Type | 例子 / Example |
|---|---|
| 代码 Bug / Code bug | 客户上传超过 5MB 的视频会 500 |
| 流程 Bug / Process bug | 销售交接客户给客户成功的清单字段不全 |
| 文档 Bug / Doc bug | PRD-0042 §4.2 描述和实际行为不一致 |
| 客户面文案 Bug / Customer-facing copy bug | 错误提示里出现了内部 PRD 编号（违反红线 #2） |
| 数据问题 / Data issue | 周报某个指标的口径在两份报表里不一样 |
| 流程未达 SLA / Process SLA miss | 客户工单 24 小时未响应 |

不进 known.md 的 / Does NOT go into known.md:
- 不是问题，只是改进想法 → 进 [`workspace_human/prd/`](../../workspace_human/prd/) 当 PRD 候选 / Improvement ideas (not bugs) → PRD candidates in [`workspace_human/prd/`](../../workspace_human/prd/)
- 个人 todo → 个人笔记 / Personal todos → your own notes

---

## known.md 的格式 / Format of known.md

```markdown
# Known Issues / 未修问题

> 单一登记位置。修复后整条移到 issues/fixed/YYYY-MM-DD.md。
> Single tracking location. Move the whole entry to issues/fixed/YYYY-MM-DD.md upon fix.

---

## B-2026-0509-A: 上传超 5MB 视频时返回 500
- 发现时间 / Discovered: 2026-05-09
- 发现人 / Reported by: 客户成功-王
- 影响范围 / Scope: 影响所有上传 > 5MB 的视频，约占当日上传 8%
- 严重度 / Severity: P1（客户工作流被阻断）
- 复现步骤 / Repro steps:
  1. 登录任意租户
  2. 上传任意 ≥5MB 视频
  3. 等到上传进度条 100% 后约 3 秒，前端弹"上传失败"
- 暂时绕行 / Temporary workaround:
  - 客户分段上传（< 5MB）
- 拟修复 / Owner & ETA: 工程-张，2026-05-12 前
- 关联 / Related: PRD-0083 上传体验

---

## B-2026-0510-A: ...
```

字段说明 / Field notes:

- **B-2026-MMDD-A** 编号格式 = `B-<年>-<月日>-<当日字母后缀>`，全公司统一 / `B-<year>-<MMDD>-<letter>` format, company-wide
- **严重度** P0/P1/P2/P3：见 [`workflows/engineering/bug_tracking_ssot.md`](../../workflows/engineering/bug_tracking_ssot.md) / Severity P0/P1/P2/P3 — see workflow
- **拟修复** 必须有具体责任人和 ETA。"等等看"不是 ETA / Owner and ETA must be concrete. "Let's see" is not an ETA

---

## fixed/YYYY-MM-DD.md 的格式 / Format of fixed/YYYY-MM-DD.md

每天一份文件，当天有 Bug 修完就追加进同一份；当天没有就不创建。
One file per day; entries appended; days with no fixes have no file.

```markdown
# Fixed Issues — 2026-05-09

> 当天修复的全部 Bug。从 issues/known.md 整条搬来。
> All bugs fixed today. Moved as-is from issues/known.md.

---

## B-2026-0507-A: 上传超 5MB 视频时返回 500
（原始登记内容全部保留）

### 修复 / Fix
- 修复时间 / Fixed at: 2026-05-09 14:23
- 修复人 / Fixed by: 工程-张
- 修复 commit / Fix commit: abc1234
- 关联 PRD / Related PRD: PRD-0083
- 根本原因 / Root cause: <一两句话技术原因>
- 验证 / Verification: 已加回归测试 `tests/upload/test_large_file.py::test_5mb_video`
- 反向断言测试清理 / Reverse-assertion tests cleaned: ✅ 已删除 `tests/upload/test_5mb_returns_500`（这是当时记录错误行为的测试）
```

要点 / Key points:
- 原始登记内容**全部保留**（背景 / 复现 / 严重度 / 影响范围）/ Preserve **all** original content
- 加 `## 修复` 段记录修复细节 / Add `## Fix` section
- **反向断言测试清理**字段是必填——红线 #13 / Reverse-assertion-cleanup field is **mandatory** — Red Line #13

---

## 移位时机 / When to Move

**修完 + 验证通过 + 反向断言测试清理后**，立即移。
**After fix verified + reverse-assertion tests cleaned**, move immediately.

不要等到周末批量移。批量移 = 几条会被忘记 = 真相再次散落。
Don't batch on weekends. Batching = some get forgotten = truth scatters again.

---

## 严重度分级 / Severity Levels

| 级别 / Level | 定义 / Definition | 响应时间 / Response |
|---|---|---|
| **P0** | 全产品停摆 / 数据丢失 / 安全事故 / 资损 | 立即（< 1 小时）/ Immediately |
| **P1** | 核心工作流阻断 / 重要客户被影响 | 24 小时内 |
| **P2** | 边角功能 / 小范围客户影响 / 有绕行方案 | 1 周内 |
| **P3** | 体验性问题 / 文档错别字 / 没有真实影响 | 排进下个迭代 |

P0 / P1 必须立刻通知相关业务方（不止登记，还要主动 push 通知）。
P0 / P1 must immediately notify affected stakeholders (logging is not enough; actively notify).

---

## "已修但没移到 fixed" 的反模式 / Anti-Pattern: "Fixed but Not Moved"

最常见的违规 / Most common violation:

> "我已经在代码里改完了，PR 也合了，但 known.md 里还挂着。下周一起整理。"

后果 / Consequences:
1. 下周整理时发现忘了一些细节，移过去的版本不完整
   By Monday, details forgotten; the moved entry is incomplete
2. 同事以为这个 Bug 还没修，又花时间看一遍
   Colleagues think the bug is open, waste time investigating again
3. 客户 / 销售去 known.md 自查时看到这条还挂着，以为公司在拖延
   Customers / sales checking `known.md` see it open, think the company is stalling

正确：合 PR 当天就移 known → fixed。
Right: move the same day the PR merges.

---

## 不要用 known.md 当 wishlist / Don't Use known.md as a Wishlist

known.md 是**问题登记本**，不是**愿望清单**。
known.md is an **issue ledger**, not a **wishlist**.

❌ "希望加一个一键导出 PPT 的功能" → 这是需求，进 [`workspace_human/prd/`](../../workspace_human/prd/) 候选区
**Wrong**: feature wishes → PRD candidates

✅ "导出 Excel 时数字列被识别成文本" → Bug，进 known.md
**Right**: real bugs → known.md

边界判断：
Boundary: 
- "目前是 X，应当是 Y" → Bug / "It does X, should do Y" → Bug
- "目前没有 Z，希望有 Z" → 需求 / "It doesn't have Z; we wish it did" → Requirement

---

## AI 参与 Bug 处理时 / When AI Helps with Bug Handling

AI 可以做的 / AI may do:
- ✅ 帮你写一份格式规范的 known.md 条目 / Help draft a properly-formatted known.md entry
- ✅ 修 Bug（按 [`workflows/engineering/debugging_workflow.md`](../../workflows/engineering/debugging_workflow.md)）/ Fix the bug per workflow
- ✅ 修完后**整条搬运**到 fixed/YYYY-MM-DD.md，并填好"修复"段 / Move the **whole entry** to fixed and fill the Fix section
- ✅ 检查反向断言测试清理 / Check for reverse-assertion test cleanup

AI 不能做的 / AI may NOT do:
- ❌ 删除 known.md 里的条目而不归档（必须搬运，不能删）/ Delete entries from known.md without archiving — always move, never delete
- ❌ 把 P0/P1 的事降级，没人确认 / Downgrade P0/P1 severity without human confirm
- ❌ 把"已修但还没验证"的事直接搬到 fixed.md / Move "fixed but not verified" entries to fixed.md
- ❌ 修一个 Bug 时顺手"清理"掉别的 known.md 条目（没授权的）/ "Clean up" unrelated known.md entries while fixing one (without authorization)

---

## 季度复盘 / Quarterly Bug Review

每季度一次，把当季 [`issues/fixed/`](../../issues/fixed/) 全扫一遍，回答：
Once per quarter, walk through all of [`issues/fixed/`](../../issues/fixed/) for the quarter and answer:

1. **重复出现的根因**：哪些 Bug 是"换了表象但根因相同"？/ Recurring root causes — which bugs share an underlying cause?
2. **最长存活时间**：哪些 Bug 在 known.md 挂了超过 30 天才修？为什么？/ Longest-living — which bugs sat > 30 days? Why?
3. **预警漏报**：哪些 Bug 是客户先发现的而不是我们自己 / 监控发现的？/ Detection gap — which bugs surfaced via customer first, not internally?
4. **新增模式**：是不是有新的一类 Bug 反复出现，需要从根子上立一条新的红线 / 流程？/ New patterns — is a new bug class recurring, suggesting a new red line / process?

复盘结论写进 [`meetings/`](../../meetings/) 当 ADR。
Review conclusions go into [`meetings/`](../../meetings/) as ADRs.
