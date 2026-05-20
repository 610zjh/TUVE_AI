---
name: Bug 单一登记本（SSOT）/ Bug Single-Source-of-Truth
retention: permanent
retention_reason: 红线 #4 的实操指南，全员长期使用 / Operational guide for Red Line #4, used company-wide
---

# Bug 单一登记本（SSOT）/ Bug Single-Source-of-Truth

> 适用：所有人。Bug 不只是工程的事——销售、运营、客服都会发现 Bug 并要登记。
> For: everyone. Bugs aren't only engineering — sales / ops / support find bugs and need to register them.

---

## 一句话 / One Line

**全公司只有两个登记 Bug 的位置：[`issues/known.md`](../../issues/known.md)（未修）和 [`issues/fixed/YYYY-MM-DD.md`](../../issues/fixed/)（已修）。其他地方"也存一份" = 多份真相 = 失控。**
**Two locations company-wide: `issues/known.md` (open) and `issues/fixed/YYYY-MM-DD.md` (closed). "Also keep a copy" elsewhere = multi-truth = chaos.**

这是红线 #4。
This is Red Line #4.

---

## 谁登记 Bug / Who Files

任何人发现：**谁发现谁登记**。
Whoever finds it files it.

不要"我发现一个 Bug，让工程同事登记吧"——你登记。工程同事会接管修复，但**登记**是你的事。
Don't "I found a bug, let engineering file it" — you file it. Engineering takes over the fix, but **filing** is yours.

---

## 登记格式 / Filing Format

```markdown
## B-2026-MMDD-A: <一句话标题>

- 发现时间 / Discovered: 2026-MM-DD
- 发现人 / Reported by: <name + 角色>
- 影响范围 / Scope: <影响多少客户 / 多少功能 / 多大频率>
- 严重度 / Severity: P0 / P1 / P2 / P3
- 复现步骤 / Repro steps:
  1. ...
  2. ...
  3. ...
- 预期结果 vs 实际结果 / Expected vs Actual:
  预期：...
  实际：...
- 暂时绕行 / Temporary workaround: <如有>
- 拟修复 / Owner & ETA: <具体姓名> + <具体日期>
- 关联 / Related: <PRD-XXXX 或其他 Bug 编号>
```

---

## Bug 编号规则 / Bug Numbering

```
B-<年>-<月日>-<当日字母后缀>

例：
B-2026-0509-A   2026 年 5 月 9 日的第 1 个 Bug
B-2026-0509-B   同日第 2 个
B-2026-0509-C   同日第 3 个
B-2026-0510-A   次日第 1 个
```

全公司统一编号，不分部门。
Company-wide, not per-team.

---

## 严重度判断 / Severity Decisions

| 级别 / Level | 定义 / Definition | SLA |
|---|---|---|
| **P0** | 全产品停摆 / 数据丢失 / 安全事故 / 资损 | 立即响应（< 1 小时）|
| **P1** | 核心工作流阻断 / 重要客户被影响 | 24 小时内启动 |
| **P2** | 边角功能 / 小范围影响 / 有绕行 | 1 周内 |
| **P3** | 体验性问题 / 文档错别字 / 无真实影响 | 排进下个迭代 |

不确定时往**严重的方向**判（事后再降级比事后再升级好）。
When uncertain, lean **severe** (downgrading later beats upgrading later).

---

## P0 / P1 的特殊纪律 / P0 / P1 Special Discipline

P0 / P1 不是"登记完就行"——立刻通知：
P0 / P1 = not just "filed"; immediately notify:

- 工程负责人 / Engineering lead
- 受影响业务方（销售 / 客户成功 / 客服）/ Affected stakeholders
- 如客户已感知 → 客户告知（按红线 #2 客户面口径）/ If customer-impacting → customer notice

不要"先在 known.md 登记，明天再说"——失控的成本指数级增长。
Don't "file in known.md, tell people tomorrow" — chaos cost grows exponentially.

---

## "Bug" vs "需求" 的边界 / Bug vs Requirement Boundary

| 判断 / Question | 是 Bug 还是需求 / Bug or Requirement |
|---|---|
| 系统目前是 X，应该是 Y → Bug |
| 系统目前没有 Z，希望有 Z → 需求（进 PRD 候选）|
| 系统行为不一致（这次是 X，下次是 Y）→ Bug |
| 系统按设计这么做，但设计本身不合理 → 需求（产品决策） |

不确定时和产品 / 工程负责人聊 → 落到对应位置。
Uncertain → sync with PM / eng lead → file appropriately.

---

## 修复后的"移位"动作 / Move on Fix

红线 #4 的关键纪律：
Key Red Line #4 discipline:

修完 Bug → **当天**把条目从 [`issues/known.md`](../../issues/known.md) **整条搬**到 [`issues/fixed/YYYY-MM-DD.md`](../../issues/fixed/)。
On fix → **same day**, **move the whole entry** from `known.md` to `fixed/YYYY-MM-DD.md`.

格式：
Format:

```markdown
# Fixed Issues — 2026-05-09

## B-2026-0507-A: 上传超 5MB 视频时返回 500
（原始登记内容全部保留）

### 修复 / Fix
- 修复时间 / Fixed at: 2026-05-09 14:23
- 修复人 / Fixed by: 工程-Z
- 修复 commit / Fix commit: abc1234
- 关联 PRD: PRD-0083
- 根本原因 / Root cause: <一两句技术原因>
- 验证 / Verification: 已加回归测试 `tests/upload/test_large_file.py`
- 反向断言测试清理 / Reverse-assertions cleaned: ✅ 已删除 `tests/upload/test_5mb_returns_500`
```

不许 / Forbidden:
- 把条目从 known.md 删掉但**不**搬到 fixed.md（违反红线 #4 SSOT）
- 在 known.md 标"已修"但不搬走（同上）
- 修了一周才搬（细节会丢失）

---

## 不进 known.md 的 Bug-like 内容 / NOT in known.md

- 个人 todo（"我下周要 refactor 这块"）→ 个人笔记
- 改进想法（"如果有 X 功能就更好"）→ PRD 候选区
- 客户的产品反馈不是 Bug → CRM / 产品反馈渠道
- 配置 / 文档 typo（已自己改完了）→ 直接修不必登记

---

## 反复出现的 Bug → 系统性问题 / Recurring Bugs → Systemic Issue

如果一类 Bug 在 3 个月里出现 ≥ 3 次：
If a bug class appears ≥ 3 times in 3 months:

→ 它不是单 Bug，是**系统性问题**。
→ Not a single bug; a **systemic issue**.

→ 起一份 ADR / PRD 解决系统性根因（流程 / 工具 / 监控 / 文档）。
→ File ADR / PRD targeting the systemic root.

→ 在 [`issues/known.md`](../../issues/known.md) 登记一条"系统性问题"条目（不是单 Bug 的那种），关联到那份 ADR / PRD。
→ Log a "systemic" entry in `issues/known.md`, linked to the ADR / PRD.

---

## 季度 Bug 复盘 / Quarterly Bug Review

每季度一次，扫一遍当季 [`issues/fixed/`](../../issues/fixed/) 全部条目，回答：
Quarterly, scan all `issues/fixed/` entries:

1. **重复根因**：哪些 Bug 是"换了表象但根因相同"？/ Recurring root causes
2. **最长存活**：哪些 Bug 在 known.md 挂了 ≥ 30 天才修？为什么？/ Longest-living
3. **预警漏报**：哪些 Bug 是客户先发现的而不是监控？/ Detection gap
4. **新增模式**：是不是有新一类 Bug 反复出现？/ New patterns

复盘结论存到 [`meetings/`](../../meetings/) 当 ADR。
Conclusions → ADR in `meetings/`.

---

## AI 在 Bug 流程中的边界 / AI's Boundary in Bug Flow

AI 可以做 / AI may:
- ✅ 帮你写规范的 known.md 条目（按格式）
- ✅ 修 Bug（按 [`debugging_workflow.md`](debugging_workflow.md)）
- ✅ 修完后**整条搬运**到 fixed.md，并填好"修复"段
- ✅ 检查反向断言测试清理

AI 不能做 / AI may NOT:
- ❌ 删除 known.md 里的条目（必须搬，不能删）
- ❌ 把 P0/P1 的事降级而没人确认
- ❌ 把"已修但还没验证"的事直接搬到 fixed.md
- ❌ 修一个 Bug 时顺手"清理"掉别的 known.md 条目（没授权）

---

## 速查 / Cheat Sheet

```
SSOT 两处：
- 未修：issues/known.md
- 已修：issues/fixed/YYYY-MM-DD.md（按日归档，整条搬过去）

谁发现谁登记，不许"让别人登"

严重度：P0/P1/P2/P3 + 不确定往严重判
P0/P1 立刻通知（不只登记）

修完当天必移位（整条搬，不能只删）

反复出现 → 系统性问题 → 起 ADR / PRD

季度复盘：根因 / 最长存活 / 预警漏报 / 新模式
```
