# 用 AI 做需求密听与会议准备 / Requirement Discovery & Meeting Prep with AI

> 适用：需求还不够清楚、需要先密听 / 开会 / 挖掘上下文，再决定是否进入 PRD 或执行的人。
> For: anyone whose requirement is still fuzzy and needs a meeting/discovery pass before a PRD or execution.

---

## 一句话 / One Line

**meeting 的第一产出是"把需求挖清楚"，第二产出才是"决议"。** 如果目标、边界、成功标准还模糊，就先做需求收敛，不要急着写 PRD 或直接开干。
**The first output of a meeting is requirement clarity; decisions come second.** If goals, boundaries, or success criteria are still fuzzy, do discovery first instead of rushing into a PRD or execution.

---

## 什么时候必须先开 meeting / When a Meeting Must Come First

只要出现任意一项，就不要直接写 PRD：

- 用户只给了一句方向，没有明确成功标准
- 你已经能预见 3 个以上关键澄清问题
- 任务涉及多角色、多系统或跨团队协作
- 任务和 TUVE 的 Agent / skill / config 上下文有关，但上下文还没对齐
- 你直觉上已经在"猜用户真正想要什么"

这时正确顺序是：`meeting / 密听 -> 需求挖掘 -> PRD -> 执行`。

---

## 会前 15 分钟的标准动作 / Standard 15-Minute Pre-Meeting

先分辨这次 meeting 属于哪一类：

- **需求挖掘型**：目标是把问题、边界、约束、成功标准讲清楚
- **方案决议型**：目标是在需求已经较清楚的前提下做取舍

如果是需求挖掘型，先跑下面这一步；不要急着列解决方案。

### 步 0：列出"还没搞清楚什么" / Step 0: List What Is Still Unclear

```
我要针对 [主题] 开一个 meeting。

现在我手里只有这些输入：
- 用户原话 / 背景：...
- 已知上下文：...
- 如果和 TUVE 运行时有关，补充 skill / config / Agent 上下文：...

请先不要写方案，先帮我列出：
- 已经明确的需求信号
- 还没明确的关键问题（按 H1 / H2 / H3 编号）
- 这次 meeting 最该问清楚的 top-5 问题
- 如果这些问题不问清，后面最容易返工的地方
```

### 步 1：明确这次会议的"决议候选" / Step 1: Frame Decision Candidates

如果这次 meeting 的目标其实还是需求挖掘，就把这里的"决议候选"改成"待确认问题"。
If the meeting is still for discovery, convert "decision candidates" into "questions to confirm".

不是"我们开个会聊聊 X"，而是：
- 需求挖掘型：`开会确认 A、B、C 三个关键问题`
- 方案决议型：`开会决定 A、B、C 三件事`

```
明天 10:00 我和 [谁] 开会，主题是 [X]。
请帮我列出：
- 这次会议必须决定的 3-5 件事（决议候选）
- 每件事的 2-3 个候选选项
- 每个选项的优劣

参考材料：
- 上次会议纪要（粘贴）
- 相关 PRD（路径或粘贴）
- 我自己的初步想法（粘贴）

约束：
- 选项要具体可执行，不要"再讨论""看情况"
- 优劣要中立，不要倾向我已有的想法
```

### 步 2：准备会议议程 / Step 2: Build the Agenda

```
基于上面的待确认问题 / 决议候选，请帮我起草一份会议议程，60 分钟内：
- 0-5 分钟：背景对齐（基于上次纪要 / 原始需求）
- 5-40 分钟：逐条挖清 top-3~5 个问题（每件 8-12 分钟）
- 40-50 分钟：确认哪些内容已经足够进入 PRD，哪些还不能
- 50-55 分钟：行动项确认（谁做什么 + 截止）
- 55-60 分钟：是否需要下一次 meeting / 是否进入 PRD

把议程发给我，我会调整后转发给参会者。
```

### 步 3：准备"如果对方提到 X 我怎么回应" / Step 3: Pre-Plan Reactions

```
基于上面的议程，列出对方最可能提的 5 个挑战 / 担心 / 反对，
每个我应该怎么回应（含数据 / 案例 / 退路）。
```

这一步在销售会议、客户对接会议、内部跨部门博弈会议特别有用。
Especially useful for sales / customer / cross-team negotiation meetings.

---

## 会中 / During the Meeting

### 主持人节奏 / Chair's Cadence

每议题开始时主持人念一句：
At each agenda item start, chair states:

> 我们下一项决议候选是 X。我先讲 30 秒背景，然后 [大家 / 你] 说意见，我会在 [X 分钟] 之内引导我们做出决定。

这个节奏让会议有"动力"，不会陷入"反复讨论无结论"。
This cadence keeps energy up, avoids "round-and-round no conclusion".

### 30 秒原则 / The 30-Second Rule

每位发言人**前 30 秒**必须直接给出立场（"我倾向 A，理由是 ..."），后面再展开。
First 30 seconds → must state position ("I lean A, because ..."), then expand.

不许 30 秒里还没说立场。强制聚焦。
30 seconds → must take a stance. Forces focus.

---

## 会后 24 小时 / Within 24 Hours After

### 步 1：用 AI 整理纪要 / Step 1: AI Drafts Minutes

```
我刚开完会。会议录音（如果允许）/ 我的笔记如下：[粘贴]

请帮我整理成会议纪要，按 [`templates/meeting_notes/`](../../templates/meeting_notes/) 的模板。
重点标出：
- 已确认的需求信号（哪些已经可以写进 PRD）
- 达成的决议（每条带"决议人 + 时间"）
- 待确认问题（按 H1 / H2 / H3 编号，标记谁来补）
- 行动项（每条带"谁做 + 什么 + 何时"）
- 未决但悬挂的（标记下次需要决议 / 或继续挖掘）

约束：
- 不要捏造没说过的话
- 不要修饰口语化表达使其"专业化"——保留原意
- 决议必须明确（如果是模糊的"再看看"，写成"未决，下周二再议"而不是"已达成共识"）
```

### 步 2：人审 / Step 2: Human Review

AI 给的纪要必须**人**审核：
AI's minutes must be **human-reviewed**:
- 关键决议是不是写对了？/ Decisions captured correctly?
- 行动项的"谁"是不是真同意了？（不是 AI 替别人答应的）/ "Who" actually agreed?
- 截止时间是不是真的能赶上？/ Deadlines realistic?

### 步 3：判断是否进入 PRD / Step 3: Decide Whether to Enter PRD

meeting 结束后先问 4 个问题：

- [ ] 目标是否已经能写成可验证的成功标准？
- [ ] 范围和非目标是否已经说清？
- [ ] 关键依赖、角色和约束是否不再靠猜？
- [ ] 仍未确认的问题是否已经少到不会让 PRD 失真？

四项都过，才进入 PRD。
否则，继续补信息或开下一轮 meeting。

### 步 4：发送 / Step 4: Distribute

24 小时内发到所有参会者。同步存到 [`workspace_human/meetings/YYYY-MM-DD_<topic>.md`](../../workspace_human/meetings/)。
Within 24h to all attendees. Save to `workspace_human/meetings/YYYY-MM-DD_<topic>.md`.

如果 meeting 已经把需求挖清，下一步才是去 [`writing_a_prd.md`](writing_a_prd.md)。
If the meeting has clarified the requirement enough, only then move to [`writing_a_prd.md`](writing_a_prd.md).

**纪要里的决议如果是非平凡决策**，同时起一份 ADR（[`workflows/decision_records/`](../decision_records/)）。
If meeting decisions are non-trivial, **also** spawn an ADR.

---

## 不要做的事 / What NOT to Do

### 1. 不要让 AI 替你"参加"会议

❌ "AI 录音 + 自动总结，我不用听了" 是反模式。
**问题**：你失去了会议的现场感（语气、犹豫、暗示），这些是 AI 抓不到的。

✅ 你听 / 参与 + 简单笔记，AI 帮你**展开**笔记。
Right pattern: you attend + brief notes, AI **expands** the notes.

### 2. 不要把会议当成"决策工具"

❌ "我们开会决定一下 X" —— 如果不在会前给 AI 准备决议候选，开会的前 30 分钟会被浪费在"对齐认知"上。
**Problem**: without pre-meeting decision candidates, the first 30 min are wasted aligning understanding.

✅ 用 AI 在会前把决议候选 + 优劣对比都准备好，让会议直接进入"投票"模式。
Right: pre-prep candidates + tradeoffs; meeting jumps straight to "vote" mode.

### 2.5 不要把 meeting 跳过直接写 PRD

❌ 需求只有一句话，就直接让 AI 写 PRD。
**问题**：AI 会自动补全大量假设，最后写出来的是"看起来完整"，不一定是"真的对"。

✅ 先开 meeting，把目标、约束、边界、未决问题和成功标准挖出来，再写 PRD。

### 3. 不要在会议纪要里捏造"达成共识"

❌ AI 写"会上大家一致同意 X"——但实际上有人在沉默、有人犹豫，AI 把它当"同意"。
**Problem**: silence ≠ consent. Hesitation ≠ consent.

✅ 纪要必须如实写"X 提议，Y 同意，Z 沉默，W 表达保留"。歧义留给后续讨论，不要"一刀切"。
Right: minutes faithfully record stances; ambiguity stays open for follow-up.

---

## AI 在会议中"在场"的边界 / AI's In-Meeting Presence

如果你用 AI 工具实时辅助（开着 Claude Code / Cursor 在另一屏）：
If you use AI tools live (Claude Code / Cursor on another screen):

✅ 可以做：实时查事实、查数据、起草回应
**OK**: real-time fact lookup, data query, draft responses

❌ 不可以做：让 AI 实时听会议（除非全员同意 + 合规过审）/ AI 直接对会议讲话（替你说）
**NOT OK**: AI eavesdropping unauthorized; AI speaking on your behalf

涉及客户的会议，AI 实时辅助前**必须告知客户**（"我们正在用 AI 工具辅助记录，不会传到外部"）。
For customer meetings, **inform the customer first** ("we're using AI to help take notes; nothing goes externally").

---

## 跨语言会议 / Multi-Language Meetings

TUZHAN 是跨国企业，有些会议涉及中英文。
TUZHAN is multinational; some meetings span CN+EN.

- **会前**：议程双语 / Bilingual agenda
- **会中**：发言人想说哪种语言说哪种，主持人确保关键决议**两种语言都重述一遍**确保对齐 / Speakers use either language; chair restates key decisions in both
- **会后**：纪要双版本（中文 + 英文），不要靠 AI 直接翻译——AI 在会议口语上经常翻错 / Bilingual minutes, **not** purely AI-translated; AI fails on meeting jargon often

---

## 速查清单 / Quick Checklist

**会前 15 分钟**:
- [ ] 已列出"已确认需求信号"和"H1/H2/H3 待确认问题"
- [ ] 决议候选 3-5 件
- [ ] 每件有 2-3 个候选选项 + 优劣
- [ ] 议程时间盒
- [ ] 对方可能挑战的 5 个点

**会中**:
- [ ] 每议题主持人先念决议候选
- [ ] 每位发言人前 30 秒必须给立场
- [ ] 主持人对每议题计时

**会后 24 小时**:
- [ ] AI 起草纪要
- [ ] 人审纪要
- [ ] 发到所有参会者
- [ ] 存到 `workspace_human/meetings/`
- [ ] 判断是否已满足进入 PRD 的条件
- [ ] 非平凡决策 → 起 ADR
