---
name: 与 AI 协作的基本姿态 / Basics of Working with AI
description: 全员通用的"怎么和 AI 说话、怎么验收 AI 的产出"原则 / Universal principles for talking to AI and reviewing its output
type: permanent
retention: permanent
retention_reason: 全员日常每次任务都用得上，最高频引用 / Every employee uses this in every task — highest frequency reference
---

# 与 AI 协作的基本姿态 / Basics of Working with AI

## 一句话 / One Line

**把 AI 当成一位刚入职的、聪明但缺背景的同事**——不是搜索引擎，不是替你做决定的老板，也不是会自动产出完美结果的咒语。
**Treat AI like a smart new hire who lacks context** — not a search engine, not a boss who decides for you, not an incantation that produces perfect output.

---

## 1. 永远先给"为什么" / Always Lead with "Why"

**反例 / Anti-pattern:**
> 帮我写个客户跟进邮件。

**正例 / Right pattern:**
> 帮我写个客户跟进邮件。背景：上周二我们和"晨星科技"开了第一次需求对齐会，他们对短视频 AI 自动化感兴趣但担心数据合规。客户对接人是李总。我希望这封邮件主要做三件事：
>
> 1. 感谢他参与上周的会
> 2. 回应他对数据合规的担心，附上我们的合规文档链接
> 3. 提议下周二上午做一次产品演示
>
> 邮件长度控制在 200 字以内，语气专业但不僵硬。

差别：
- 反例：AI 只能猜你要什么，猜得不对你来回改 5 次 / AI guesses, you iterate 5 times
- 正例：AI 一次产出 90% 可用，你只需要润色 / AI produces 90%-usable in one shot

**给"为什么"的检查清单 / "Why" checklist:**
- [ ] 这件事的**目标**是什么？/ The objective?
- [ ] 这件事的**背景**：它接在什么之后、为什么发生？/ The context: what came before, why now?
- [ ] **关键约束**：长度、语气、格式、不能做什么？/ Key constraints: length, tone, format, what NOT to do?
- [ ] **成功长什么样**：完成的产出是给谁看、要让对方做什么？/ What success looks like: audience, desired action?

---

## 2. 用 AI 做你的"扩音器"，不是"替身" / Use AI as Amplifier, Not Replacement

AI 强在：
AI is strong at:
- 把粗的想法快速展开成结构化文档 / Expanding rough ideas into structured documents
- 把长材料压缩成结论 / Compressing long material to conclusions
- 改稿、润色、翻译、查找格式问题 / Editing, polishing, translating, formatting
- 给出多个方向供你挑 / Generating multiple options to choose from

AI 弱在：
AI is weak at:
- 判断**你们公司**这件事的优先级（它不知道老板今天想什么）/ Judging *your company's* priorities (it doesn't know what the boss wants today)
- 判断**这位客户**的情绪（它没参加上次电话）/ Judging *this customer's* sentiment (it wasn't on the call)
- 判断**这个数字**对不对（它会编造看起来合理的数据）/ Judging whether *this number* is correct (it confabulates plausible-looking numbers)
- 替你担责（决定权和责任永远在你手上）/ Taking responsibility (decisions and accountability stay with you)

操作准则 / Operating rule:
- 让 AI 出 3-5 个版本 → 你挑 → 你定调
- AI drafts 3-5 versions → you pick → you set the tone

---

## 3. 不可逆动作必须先确认 / Irreversible Actions Need Confirmation

这是红线 #8。AI 在执行以下动作前**必须**先和人确认：
This is Red Line #8. AI **must** get human confirmation before:

| 类别 / Category | 例子 / Examples |
|---|---|
| 外部沟通 / External comms | 发邮件、发消息给客户 / 群发给客户群 / 发社交媒体 / Sending emails / messaging customers / posting socials |
| 数据 / Data | 删任何文件 / 数据库 row / 客户记录 / Deleting any file, DB row, customer record |
| 部署 / Deploy | 推到生产、`git push --force`、关 PR、删分支 / Deploy to prod, force-push, close PR, delete branch |
| 钱 / Money | 退款 / 转账 / 修改合同 / 调整定价 / Refund, transfer, contract edit, pricing change |
| 付费 API / Paid API | 单次调用 > 0.1 USD（避免账单意外）/ Single call > 0.1 USD (avoid bill surprises) |

**人说一次"以后这类不用问"对当前会话有效**，跨会话**一律重新确认**。理由：会话之间状态可能变（客户关系变了、上下游约定变了、人变了）。
**A "don't ask me again" is valid for the current session only**; across sessions, **re-confirm**. Reason: state may have changed (customer relationship, upstream/downstream agreement, personnel).

---

## 4. AI 给的内容**必须**人验收 / Always Review AI Output

每一份 AI 产出都要过两道关：
Every AI output passes two gates:

**关 1：事实验收 / Gate 1 — Fact-check**
- 数字对不对？/ Numbers correct?
- 客户名 / 产品名 / 日期对不对？/ Customer / product / date names correct?
- 引用的链接 / 文档存在吗？/ Cited links / docs actually exist?
- 行业知识有没有"听起来合理但其实是编的"？/ Industry claims that "sound right but are confabulated"?

**关 2：判断验收 / Gate 2 — Judgment review**
- 语气合适吗？（这个客户能不能接受这种语气？）/ Tone fit for *this* audience?
- 主次对吗？（重点是不是被淹在细节里？）/ Priorities right? (Is the main point buried?)
- 缺了什么？（有没有应该提但漏了的事？）/ Anything missing?
- 多了什么？（有没有不必要的、可以删掉的？）/ Anything redundant?

**没经过这两道关，不要发出去**。客户、伙伴、上司收到的每一份内容，最终责任人是你（人）不是 AI。
**Without both gates, do not send.** The accountable party for everything that reaches a customer, partner, or boss is you (the human), not AI.

---

## 5. AI 卡住时怎么办 / What to Do When AI Stalls

如果 AI 反复给你不对的答案，不要继续往同一个方向加压。换姿势：
If AI keeps giving wrong answers, don't push harder in the same direction. Pivot:

| 症状 / Symptom | 应对 / Response |
|---|---|
| AI 在同一个错误里打转 / AI loops on the same mistake | 开新对话，从零讲背景 / Start a fresh chat, give the context from zero |
| AI 给的代码 / 文档每次都不一样 / AI's code/doc changes every iteration | 把"刚才哪一版的哪一段对"明确告诉它 / Tell it explicitly "version N, paragraph M was correct" |
| AI 在编数据 / 编 API / 编文件路径 / AI confabulates data / API / file paths | 让它**只用你提供的输入**重写，不许引用外部 / Have it rewrite using *only your input*, no external citation |
| AI 一直不肯动手 / AI keeps stalling on confirmation | 检查你是不是给了一个跨红线 #8 的请求 / Check if your request crosses Red Line #8 |

---

## 6. 多工具协作 / Working with Multiple AI Tools

公司支持四种工具（Claude Code / Cursor / Codex / Trae），不需要纠结挑哪个。粗略经验：
Company supports four tools — don't agonize over selection. Rough heuristic:

| 场景 / Scenario | 推荐 / Recommended |
|---|---|
| 长文档审阅 / 多步推理 / Long-doc review, multi-step reasoning | Claude Code |
| 写代码（IDE 内联）/ Coding (inline IDE) | Cursor |
| 命令行批量任务 / Batch CLI tasks | Codex |
| 中文本地化体验 / Chinese-localized UX | Trae |

详细对比见 [`workflows/ai_basics/which_tool_for_which_job.md`](../../workflows/ai_basics/which_tool_for_which_job.md)。

**重要：四个工具读的是同一份入口文件（CLAUDE.md / AGENTS.md / .cursorrules / CODEX.md，内容一致）**，所以红线、流程、工作风格都是一致的。换工具不换规矩。
**Important: all four tools read identical entry files**, so red lines, processes, working style are consistent. Switching tools doesn't switch rules.

---

## 7. 不要把 AI 当作"决策权外包" / Don't Outsource Decisions to AI

最后一句也是最重要的一句：
Final and most important:

**AI 可以帮你想得更全、写得更快、改得更细——但决定权和责任永远在你手上。**
**AI helps you think more thoroughly, write faster, edit finer — but the decision and the accountability stay with you.**

如果有一天你发现自己说"AI 让我这么干的"，那一定是你这条流程出了问题，不是 AI 的问题。
The day you find yourself saying "AI told me to do it" — your process broke, not AI.
