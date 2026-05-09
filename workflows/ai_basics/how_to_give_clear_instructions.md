# 怎么给 AI 清晰的指令 / How to Give AI Clear Instructions

> **适用对象**：所有人（销售 / 运营 / 视频 / 产品 / 开发）
> **Audience**: everyone

---

## 一句话 / One Line

把 AI 当成一位刚入职 3 天的、聪明的、缺背景的同事。你给同事的任务怎么交代清楚，给 AI 就怎么交代清楚。
Treat AI like a smart colleague who started 3 days ago and lacks context. Brief AI exactly like you'd brief that colleague.

---

## 6 件事的检查清单 / The 6-Element Checklist

每次给 AI 任务前，自检：
Before each AI task, self-check:

| # | 元素 / Element | 检查问题 / Check |
|---|---|---|
| 1 | **背景 / Context** | 我是谁？这件事是接在什么之后的？为什么现在做？|
| 2 | **目标 / Goal** | 完成后应该长什么样？谁是最终读者？我希望读者读完做什么？|
| 3 | **边界 / Boundaries** | 不要做什么？必须保留什么？哪些是红线（参考 [`000_CORE_RED_LINES.md`](../../principles/000_CORE_RED_LINES.md)）？|
| 4 | **材料 / Materials** | AI 需要哪些文件 / 链接 / 已有内容？我把它们指给它了吗？|
| 5 | **形式 / Format** | 长度？markdown / 纯文本？中文 / 英文 / 双语？|
| 6 | **不确定就问 / If unsure, ask** | "你看完后列出 top-3 不确定的点，问我，我先回答再开始干。" |

第 6 项是**最被忽略也最值钱**的一项。
Item 6 is the **most-skipped and highest-value** of the six.

---

## 反例 vs 正例 / Anti-Pattern vs Pattern

### 任务：写一份给客户的项目简报 / Task: Customer brief

**反例**:
> 帮我写一份客户简报。

**会发生什么**：
- AI 不知道是哪个客户、哪个项目、哪个阶段
- AI 编一份"看起来很专业"但和实际客户无关的简报
- 你来回改 5 次

**正例**:
```
背景：我们昨天和「客户 A」（教育-中型）开了第二次需求对齐会。客户对我们的短视频 AI 产品感兴趣，
但担心数据合规和实施复杂度。
目标：给客户的项目简报，让他能在公司内部转发给老板看，明确「我们要一起做什么、什么时候、怎么验收」。
边界：
  - 数字 / 客户名 / 内部 PRD 编号一律不能出现在客户面文案里（红线 #2）
  - 不要捏造预期效果数据，只说真实可承诺的
材料：上次会议纪要在下面（粘贴）。客户简报模板见 `templates/customer_brief/`。
形式：markdown，约 800 字，中文。结构：背景 / 我们一起要做什么 / 时间表 / 接下来的事。
不确定：你读完后列 top-3 问题问我，我先回答你再开始写。
```

**会发生什么**：
- AI 一次给出 80% 可用的稿
- 你只需要润色
- 总时长 = 反例的 1/5

---

## 6 个常见的"指令缺陷" / 6 Common Instruction Gaps

| 缺陷 / Gap | 症状 / Symptom | 修复 / Fix |
|---|---|---|
| 缺背景 / Missing context | AI 给的内容感觉"飘""不接地气" | 加 1-3 句"我们公司是 X / 现在是 Y / 这件事接在 Z 之后" |
| 缺目标 / Missing goal | AI 给的内容偏向，但偏的不是你想要的 | 写"完成后这份内容是给 [谁] 看的，我希望他读完之后 [做什么]" |
| 缺边界 / Missing boundaries | AI 顺手做了你没要求的"额外好事" | 写"不要做 X / 不要假设 Y / 必须保留 Z" |
| 缺材料 / Missing materials | AI 编造数据 / 引用 / 文件路径 | 把所有相关材料粘贴或指出路径 |
| 缺形式 / Missing format | AI 给得太长 / 太短 / 格式不对 | 写"约 N 字 / markdown / 三段式" |
| 缺"问我" / Missing "ask me back" | AI 不问问题就开干，开错了 | 加一句"不确定的列 top-3 问题问我" |

---

## "5W1H" 备用框架 / 5W1H Fallback

记不住 6 件事时，至少回答 5W1H：
If you can't remember the 6 elements, at least answer 5W1H:

- **Who**: 给谁看？
- **What**: 要什么产出？
- **When**: 什么时候要？
- **Where**: 在什么场合用？
- **Why**: 为什么要这件事？
- **How**: 怎么样的形式？多长？什么风格？

---

## 长任务的分阶段提示 / Stage-by-Stage Prompting for Long Tasks

≥ 30 分钟的任务，分阶段：
≥ 30 min tasks, stage them:

```
[阶段 1：理解]
"先把背景和材料读一遍。读完告诉我：
1) 你理解的目标是什么
2) 你看到的最关键的 3 个事实
3) 你最不确定的 3 个点"

[等 AI 回应，你确认 / 修正]

[阶段 2：起草]
"按上面的理解起草第一版。"

[阶段 3：自查]
"自查：(a) 红线 #2 客户面文案规则有没有违反 (b) 数字是不是都来自我给你的材料"

[阶段 4：润色]
"按 [指出的反馈] 润色。"
```

---

## 速查卡片 / Cheat Card

```
背景：[你是谁、在什么场景]
目标：[完成后应该长什么样、给谁看]
边界：[不要做什么 / 必须保留什么]
材料：[文件路径 / 链接 / 粘贴内容]
形式：[长度 / 格式 / 语言]
不确定：[让 AI 列 top-3 问题]
```

每次开新对话，照填一遍。多花 30 秒，节省 5 次返工。
Each new conversation, fill this in. Adds 30s, saves 5 iterations.
