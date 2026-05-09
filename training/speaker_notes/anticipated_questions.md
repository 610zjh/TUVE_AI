---
name: 提前准备的 Q&A
retention: permanent
retention_reason: 演讲者必备 FAQ
---

# 提前准备的 Q&A / Anticipated Questions

> Top 15 提前准备好的答案，避免临场无准备。
> Top 15 anticipated questions with prepared answers, to avoid being caught off-guard.

---

## 通用类

### Q1: 这套方法论是不是太重了？我们公司就 50 人，需要这么多规矩吗？

**A**: 规矩多看起来重，但每一条都是从过去的真实事故换来的。50 人公司也会有客户面文案泄露内部信息、Bug 散落多处真相、决策口头共识 3 个月后翻案这些问题——只是规模小一点。这套方法论的好处：**新员工能直接学到"成熟做法"**，不必自己踩 3 年坑。
另外：你不必一次全用。先用 5 条最贴近你当前痛点的红线 + 2-3 个工作流，半年后再扩。

### Q2: 我用 AI 用得很顺手，需要这套方法论吗？

**A**: 你"用得顺手"很可能因为你**自己心里有一套**——这套方法论就是把这个"心里的"显式化，让你的同事也能复用。一个人顺手 ≠ 团队顺手。

### Q3: AI 工具更新很快（去年用 GPT-4，今年用 Claude，明年可能换别的）。这套方法论会不会很快过时？

**A**: 工具会变，方法论不会。这套方法论的核心是"6 件事检查清单 / 红线 / 工作流" —— 这些跟具体 AI 厂商无关。换工具时入口文件（CLAUDE.md / .cursorrules 等）需要调整，但内容是一致的。

### Q4: 红线和创新会不会冲突？

**A**: 红线是"防重复犯老错误"的护栏，不是"禁止创新"的牢笼。
- 老错误：泄露内部代号 / 客户数据 → 红线挡住
- 新错误：可以发生，因为我们还没遇过 → 红线没覆盖
- 创新：发生在红线之外的空间

如果某条红线在某次创新中"碍事"——按"红线如何演进"流程提议改它，不要静默绕过。

---

## 销售 / 运营类

### Q5: 我每次都按 6 件事写提示太麻烦了，能不能简化？

**A**: 你**不需要每次都写 6 件事完整版**——你需要**心里有这 6 件**，但根据任务大小调整：
- 简单任务（3 分钟以内 AI 能完成）：1-2 件就够（"目标 + 边界"）
- 复杂任务（≥ 30 分钟 AI 需要）：6 件事完整版
- 反复性任务：写一份"我的标准提示模板"存到 [`templates/`](../../templates/)，每次复用

### Q6: 客户的真实数据（电话、邮件）在我手里。我**必须**给 AI 看才能让 AI 帮我整理。怎么办？

**A**: 看你需要 AI 做什么：
- 整理电话内容（结构化、提取要点）→ 在送 AI **前先脱敏**（手机变占位符、客户名变标签），脱敏后送 AI 完全可行
- 让 AI 直接发邮件给客户 → **不行**，红线 #8 不可逆动作必须人确认
- 让 AI 帮你查客户的合同条款 → 用公司的合规版 AI 工具（已签 DPA），不用个人账号 / 公开网页版

详细 SOP 见 [`principles/subs/data_and_privacy.md`](../../principles/subs/data_and_privacy.md)。

### Q7: 客户简报每次都要走"三道闸"太花时间。

**A**: "三道闸"中的关键词 grep 闸**应该自动化**——把它做成 PR 的 CI 检查（参考 [`projects/customer_brief_generator/customer_brief_generator.py`](../../projects/customer_brief_generator/customer_brief_generator.py) 的 `scan_for_internal_tokens` 实现）。
品牌声音闸 + 法务闸需要人，但只要内容质量稳了之后，第二闸 / 第三闸常常就 30 秒过完。
不要因为"麻烦"就跳过——一次违规事故的代价远超三道闸的累计时间。

---

## 工程师类

### Q8: 我们项目已经有 800+ 行的文件，怎么处理？

**A**: 不必现在拆。但是：
1. **不新加**超过 800 行的文件
2. 当那个文件被改时，**顺手**考虑拆分（提一份 COMPACT-NNNN 提案）
3. 把"为什么这个例外"在 `.codeowners` 或 `principles/000_CORE_RED_LINES.md` 显式登记

### Q9: 如果 PRD 很简单（比如改个 typo），还要走 5 阶段吗？

**A**: 不必。改 typo / 改一行配置这种"完全可逆 + 不影响他人"的：直接改、commit message 写清楚、不必 PRD。
判断标准：有没有触发红线 #6（非平凡决策）？是不是 ≥ 1 个其他职能受影响？是不是难以撤销？任一是 → 走完整流程。

### Q10: 我修一个 Bug，发现旁边代码也有问题。能不能顺手修？

**A**: 不要顺手。原因：
1. 评审范围扩大，PR 难看
2. 如果旁边修复有问题，rollback Bug 修复连带回滚到旧形态
3. 旁边修复没在任何 PRD 里登记

正确做法：把"旁边的问题"立刻登记到 [`issues/known.md`](../../issues/known.md)，下次单独修。

### Q11: 我们用 Cursor 不是 Claude Code。这套方法论适用吗？

**A**: 完全适用。四个工具（Claude Code / Cursor / Codex / Trae）共享同一份入口文件——不同的文件名（CLAUDE.md / AGENTS.md / .cursorrules / CODEX.md）但内容一致。换工具不换规矩。

### Q12: AI 给的代码经常有微妙的错误（边界 case 没考虑）。怎么防御？

**A**: 三招：
1. 写完代码后让 AI **列出 top-5 边界 case**，逐个测试
2. 关键代码用**反向自查**：让 AI 回答"如果我错了最可能错在哪 3 处"
3. 写**回归测试**断言修复后正确行为，不只是"happy path"

详见 [`workflows/ai_basics/common_failure_modes.md`](../../workflows/ai_basics/common_failure_modes.md)。

---

## 产品类

### Q13: PRD 的"主次审视"段什么时候必须有？

**A**: 仅 paywall / feature gate / 分层 PRD 必须有。其他 PRD 可不必（但**主动**做也欢迎）。
"主次审视"段的核心问题：**这个 PRD 是不是把"产品价值"和"商业包装"主次搞反了**？详见 [`principles/subs/business_priorities.md`](../../principles/subs/business_priorities.md)。

### Q14: 客户访谈纪要存哪？

**A**: [`workspace_human/meetings/customer_interviews/YYYY-MM-DD_<customer_label>.md`](../../workspace_human/meetings/)，客户名按红线 #3 脱敏。

---

## 综合类

### Q15: 我看完培训后想让我们团队也用这套方法。从哪开始？

**A**: 推荐路径：
1. 第一周：让团队读完 [`workflows/ai_basics/`](../../workflows/ai_basics/) 5 个文件（约 30 分钟）
2. 第二周：选**一个**最贴你当前痛点的红线，团队开始用（比如：客户面文案 grep 闸）
3. 第一个月：把"客户简报""周报""跟进邮件"中的一种用 [`templates/`](../../templates/) 模板化
4. 第二个月：开始写第一份 [`workspace_human/prd/`](../../workspace_human/prd/)
5. 第三个月：开始写第一份 ADR，开始用 [`issues/known.md`](../../issues/known.md) 单一登记

不要一次全上。**先用，后扩**。

---

## 没在这份清单里的问题

如果有人问的问题不在这 15 个里：
1. 诚实答："这个问题我没现场准备好答案"
2. 把问题记下来
3. 在 [`training/post_conference/feedback_collection.md`](../post_conference/feedback_collection.md) 整理后回复

不要假装知道一个你不知道的问题。
