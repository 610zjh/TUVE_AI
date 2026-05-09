---
name: 05 - 工程场 Q&A 和总结
retention: permanent
retention_reason: 培训第二部分收尾段
---

# 第二部分 - 第 05 节：Q&A 和"下周作业"（10 分钟）

> Part 2, Section 05: Q&A and "Next Week's Homework" (~10 min)

---

## 这一节要让听众离场时记住的

**仓库的 [`workflows/engineering/`](../../workflows/engineering/) 是工程师的本地参考。 [`projects/customer_brief_generator/`](../../projects/customer_brief_generator/) 是工程师的入门样例。**
**[`workflows/engineering/`](../../workflows/engineering/) is your local reference; [`projects/customer_brief_generator/`](../../projects/customer_brief_generator/) is your starter sample.**

---

## 讲稿（10 分钟）

### 第二部分总结（3 分钟）

> 90 分钟讲了什么：
>
> 1. **工程师特殊性**：代码会被反复跑、和外部系统交互、6 个月后被接手、错误更难发现 → 纪律比销售更严
> 2. **PRD-到-代码 现场演示**：5 阶段（理解 / 草图 / 实施 / 验证 / 收尾五件套）
> 3. **Bug-到-修复 现场演示**：6 步（复现 / 登记 / 定位 / 选策略 / 修+测 / 移位）
> 4. **部署纪律**：8 件事自查表 + worktree 清洁 + 红线 #14（先看日志）

### 下周作业（5 分钟）

> 工程同事的下周作业：
>
> **作业 1（必做）：** 给你正在做的某个项目加一份 [`workspace_human/prd/`](../../workspace_human/prd/) 下的 PRD。哪怕这件事已经做了一半 —— 把"已经做了的"逆向写成 PRD（追溯型 PRD）+ 把"还没做的"前向写成需求。
>
> **作业 2（推荐）：** 在你下周的某个 Bug 修复 PR 里，**严格走完** 6 步（复现 / 登记 / 定位 / 选策略 / 修+测 / 移位），最后在团队群里分享你的体感。
>
> **作业 3（推荐）：** 给我一个反馈：你过去 3 个月 AI 协作中**最浪费时间的一个失败模式**是哪一种？我们整理后回到 [`workflows/ai_basics/common_failure_modes.md`](../../workflows/ai_basics/common_failure_modes.md) 补充新的失败模式 + 防御。
>
> 一周后我们做一次 60 分钟的工程师专场答疑。

### Q&A（2 分钟）

> 现在 5 分钟自由 Q&A。
>
> 没回答完的问题会收集起来放进 [`training/post_conference/`](../post_conference/) 里。

---

## 收尾

> 各位辛苦了。今天讲的内容很多，**不要试图全记住**。
>
> 仓库就在那里，[`AI_MANUAL.md`](../../AI_MANUAL.md) 永远是入口，[`workflows/engineering/`](../../workflows/engineering/) 是工程师专属参考。
>
> 一周后见。

---

## 工程师常见问题（提前准备答案）/ Anticipated Questions

### Q: 我们现在都在用 Cursor，不是 Claude Code。这套方法论一样适用吗？

A: 是。四个工具（Claude Code / Cursor / Codex / Trae）共享同一份入口文件（CLAUDE.md / AGENTS.md / .cursorrules / CODEX.md，内容一致）。换工具不换规矩。

### Q: 我们项目已经有 800+ 行的文件，怎么办？

A: 不必现在就拆。但是：(1) 不要新加超过 800 行的；(2) 当那个文件被改时，顺手考虑拆分（提一份 COMPACT-NNNN 提案）；(3) 把"为什么这个例外"在 .codeowners 或 000_CORE_RED_LINES.md 显式登记。

### Q: 我们的客户面文案跑红线 #2 grep 在 CI 里吗？

A: 推荐加。先做 advisory（不阻断），半个月后看大家是不是适应，再升级到 blocking。Issue 模板见 [`projects/customer_brief_generator/customer_brief_generator.py`](../../projects/customer_brief_generator/customer_brief_generator.py) 的 INTERNAL_TOKEN_PATTERNS。

### Q: 我用 AI 修 Bug 时，AI 经常给"看似合理但实际不对"的修复。怎么办？

A: 三招：
1. 红线 #14：先看真实日志，再让 AI 提建议（不是让 AI 凭代码猜）
2. 让 AI 在动手前列 top-3 候选根因 + 每个的可证伪假设
3. 让 AI **写完后跑测试** + 跑你给它的边界 case，再说"完工"

### Q: 我们有些代码是 vendored 第三方库，超 800 行。

A: vendored 代码是 #7 的例外。但要在 .codeowners 显式登记 + 不修改它（修改它就失去 vendored 意义；如果非改不可，做一个 wrapper 层）。

---

## 这一节用到的引用

- [`AI_MANUAL.md`](../../AI_MANUAL.md)
- [`workflows/engineering/`](../../workflows/engineering/) 全 6 文件
- [`training/post_conference/`](../post_conference/)

---

## 节奏

- 总结：3 分钟
- 下周作业：5 分钟
- Q&A：2 分钟（实际可拉到 5-10 分钟）
- 总：10 分钟（弹性 + 5）
