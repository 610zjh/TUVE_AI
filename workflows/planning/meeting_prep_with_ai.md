# 用 AI 准备会议 / Meeting Prep with AI

> 适用：所有要主持会议或被邀去重要会议的人。
> For: anyone hosting or attending an important meeting.

---

## 一句话 / One Line

**会议的产出是"决议"，不是"过程"。** AI 帮你在会前把决议候选准备好，让会议从 60 分钟降到 30 分钟。
**A meeting's output is "decisions", not "process".** AI prepares decision candidates before the meeting, cutting 60 min to 30.

---

## 会前 15 分钟的标准动作 / Standard 15-Minute Pre-Meeting

### 步 1：明确这次会议的"决议候选" / Step 1: Frame Decision Candidates

不是"我们开个会聊聊 X"，是"开会决定 A、B、C 三件事"。
Not "let's chat about X", but "the meeting decides A, B, C".

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
基于上面的决议候选，请帮我起草一份会议议程，60 分钟内：
- 0-5 分钟：背景对齐（基于上次纪要）
- 5-50 分钟：3-5 件决议（每件 10-15 分钟）
- 50-55 分钟：行动项确认（谁做什么 + 截止）
- 55-60 分钟：下次会议时间

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
- 达成的决议（每条带"决议人 + 时间"）
- 行动项（每条带"谁做 + 什么 + 何时"）
- 未决但悬挂的（标记下次需要决议）

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

### 步 3：发送 / Step 3: Distribute

24 小时内发到所有参会者。同步存到 [`workspace_human/meetings/YYYY-MM-DD_<topic>.md`](../../workspace_human/meetings/)。
Within 24h to all attendees. Save to `workspace_human/meetings/YYYY-MM-DD_<topic>.md`.

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
- [ ] 非平凡决策 → 起 ADR
