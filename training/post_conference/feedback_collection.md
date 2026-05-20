---
name: 反馈收集
retention: permanent
retention_reason: 让培训持续进化
---

# 反馈收集 / Feedback Collection

> 让培训随真实使用 + 真实反馈进化。
> Let training evolve with real use and real feedback.

---

## 4 类反馈 / 4 Types of Feedback

### 1. 现场没回答完的问题 / Unanswered On-Site Questions

培训现场记下的、当时没答完的问题。

**收集方式**：演讲者或助手在演示时记笔记 + 培训后整理。

**回应方式**：
- 24 小时内整理成 FAQ
- 发回参与者邮件 / 群组
- 加到 [`speaker_notes/anticipated_questions.md`](../speaker_notes/anticipated_questions.md) 的 Q&A 中以备下次

### 2. "我从今天带走的 1 件事是 ___" 反馈 / Takeaway Feedback

培训结束前每位参与者一句话留言。

**收集方式**：
- 物理：现场放一张大白板，每人贴便签
- 数字：培训后 2 小时内发邮件邀请填一份 1 题问卷

**回应方式**：
- 整理出 top 5 共性主题
- 贴到 [`meetings/`](../../meetings/) 当成"培训复盘"
- 用来调整下次培训的重点

### 3. 自学过程中的反馈 / Self-Study Feedback

不参加培训直接看仓库的同事 / 培训后真实使用的同事。

**收集方式**：
- 在 [`AI_MANUAL.md`](../../AI_MANUAL.md) 末尾留一个"反馈给我们"的指引
- 邀请同事在 [`meetings/`](../../meetings/) 起反馈纪要

### 4. "我用了之后发现 X 段不对 / 不清楚" 反馈 / "I Used It and Found X Wrong/Unclear" Feedback

最值钱的反馈——真实使用后发现的问题。

**回应方式**：
- 立刻起一份 PRD 修订对应工作流
- 致谢反馈人（在更新版的 changelog 提名）

---

## 培训复盘模板 / Training Retrospective Template

培训结束后 1 周内，演讲者写一份复盘到 [`meetings/training_retro_YYYY-MM-DD.md`](../../meetings/):

```markdown
# 培训复盘：YYYY-MM-DD《如何高效用 AI 完成工作》

- 参与人数：N
- 演讲者：[name]

## 现场观察
- 哪些段反响最好（眼神、互动、提问数）？
- 哪些段反响最差？
- 哪些段时间不够 / 太多？

## 收到的反馈

### top 3 高质量提问
- ...

### top 3 "带走的 1 件事"
- ...

### top 3 不满 / 困惑点
- ...

## 演讲者自评
- 我做对的：...
- 我做错的：...
- 下次怎么改：...

## 行动项

下次培训前要改的：
- [ ] 把"运维同步回填" 这一段案例换成更新的真实案例
- [ ] 把第 02 节加快 5 分钟（这次过头了）
- [ ] 第 04 节的动手练习再加一个备选案例
- ...

仓库内容要改的：
- [ ] 某 workflow 文件 §X 描述不准确 → 修订
- [ ] 某 case study 漏写了一个关键教训 → 补充
- [ ] AI_MANUAL.md §4 任务表少了一项 → 加上
```

---

## 收集机制设置 / Setting Up Collection Channels

### 选项 A：邮件

培训结束后立刻发：

```
主题：感谢参与今天的培训 + 1 分钟反馈

各位：

感谢今天参与《如何高效用 AI 完成工作》培训。

为了让这套方法论持续进化，请用 1 分钟回复这封邮件，回答以下任一问题：

1. 您今天带走的最重要的 1 件事是什么？
2. 哪一段对您最有用？
3. 哪一段您觉得不够清楚 / 想多听一些？
4. 您下周打算用这套方法论解决的 1 件事是什么？

任意 1 题即可。我会汇总后用于下次培训迭代。

谢谢，
[培训发起人]
```

### 选项 B：协作文档

在仓库的 [`meetings/training_feedback/`](../../meetings/) 下开一份共享文档，邀请参与者填。

### 选项 C：物理白板

会议室留一面白板：

```
我从今天的培训带走的 1 件事是 ___

[每人一张便签]
```

---

## 把反馈用起来 / Acting on Feedback

收集完不等于结束。每月一次：

1. 查看 [`meetings/training_feedback/`](../../meetings/) 下的反馈
2. 分类：(a) 培训内容改进 (b) 仓库内容改进 (c) 全新缺口
3. 起对应 PRD / ADR
4. 实施
5. 在下一次培训中**显式提到**："上次培训反馈的 X，我们已经在 [`workflows/...`](../../workflows/) 加了 Y"

让参与者看到他们的反馈被认真对待——这是激励持续反馈的最好方式。

---

## 仓库随培训进化 / Repo Evolves with Training

每次培训后**至少改 1 处**仓库：
- 新增的 FAQ → [`speaker_notes/anticipated_questions.md`](../speaker_notes/anticipated_questions.md)
- 新发现的失败模式 → [`workflows/ai_basics/common_failure_modes.md`](../../workflows/ai_basics/common_failure_modes.md)
- 反复出现的工作流缺口 → 新建 workflow 文件
- 旧 workflow 描述过时 → 更新

不要让仓库**冻结**——它要和真实使用一起呼吸。
