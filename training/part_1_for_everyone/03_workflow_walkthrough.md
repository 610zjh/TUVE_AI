---
name: 03 - 工作流走查
retention: permanent
retention_reason: 培训中工作流演示段
---

# 第一部分 - 第 03 节：通用工作流走查（25 分钟）

> Part 1, Section 03: Universal Workflow Walkthrough (~25 min)

---

## 这一节要让听众离场时记住的

**给 AI 提示的 6 件事检查清单**和**8 种 AI 失败模式**——记不全没关系，知道仓库里在哪能找到。
**The 6-element prompt checklist** and **8 AI failure modes** — don't memorize; know where to find them.

---

## 讲稿（25 分钟）

### 给 AI 提示的 6 件事（10 分钟）

> 我现在做现场演示。我会用一个"销售开完客户电话要写跟进邮件"的真实例子。
>
> **反例提示（不要这样）：**
>
> > 帮我写一份客户跟进邮件。
>
> 让我们看 AI 会输出什么。（**演讲者切到 AI 工具，输入这个提示，等 AI 回复**）
>
> 看，AI 的输出基本不可用：
> - 不知道是哪个客户、什么背景、什么阶段
> - 给了一份"通用跟进邮件模板"——但客户不通用
> - 我要回去改 5 次才能用
>
> **正例提示（这样写）：**
>
> （切到第二个对话）
>
> > 帮我写一份给客户 A（教育-中型）的跟进邮件。
> >
> > 背景：上周二我们和"客户 A"开了第一次需求对齐会。客户对短视频 AI 自动化感兴趣，但担心数据合规。
> >
> > 目标：让对接人感觉"我们听到了你的需求"，并提议下周二上午做一次产品演示。
> >
> > 边界：
> > - 不要捏造没在会上发生的事
> > - 不要在邮件里出现 PRD 编号 / Bug 编号 / 内部代号（红线 #2）
> > - 不要点名其他客户
> >
> > 形式：
> > - 中文，约 200 字
> > - 三段式：感谢 / 回应担心 / 提议下一步
> >
> > 不确定就问：列出 top-3 你最不确定的点，我先回答你再开始。
>
> AI 输出后我们再看。
>
> （**讲者点击发送，让 AI 回复**）
>
> 差别一目了然。这次的输出几乎可以直接用——只需要润色 + 红线检查。
>
> 这背后就是"6 件事检查清单"：

```
1. 背景：你是谁、什么场景、为什么这件事冒出来
2. 目标：完成后应该长什么样、给谁看
3. 边界：不要做什么 / 必须保留什么
4. 材料：相关文件 / 链接 / 已有内容
5. 形式：长度 / 格式 / 语言
6. 不确定就问：让 AI 列 top-3 问题
```

> 这 6 件事在 [`workflows/ai_basics/how_to_give_clear_instructions.md`](../../workflows/ai_basics/how_to_give_clear_instructions.md) 有完整版。
>
> **第 6 件事最容易被忽略也最值钱**——多一句"不确定就问"，省下后面 5 次返工。

### AI 协作的 8 种失败模式（10 分钟）

> 我快速过一遍。详细在 [`workflows/ai_basics/common_failure_modes.md`](../../workflows/ai_basics/common_failure_modes.md)。
>
> **1. 编造引用 / Fabricated citations**
> AI 会编造看似权威的文献、API、文件路径。**永远要求 AI 标 [来源]，自己抽查 1-2 条**。
>
> **2. 过度自信 / Overconfidence**
> AI 用流畅语言陈述错误结论。**反向自查**：让 AI 回答"如果你错了最可能错在哪 3 处"。
>
> **3. 顺从用户的错误前提 / Sycophantic agreement**
> 你说"X 是对的吧" → AI 倾向同意。**把陈述句改成开放问句**："X 是对还是错？为什么？"
>
> **4. 任务漂移 / Task drift**
> AI 做你没要求的"额外好事"。**指令里写"只做 X，不要做 X 之外的事"**。
>
> **5. 提前完工 / Premature done**
> AI 说"完工了"但实际半成品。**让 AI 把红线 #10 五件套逐项核对**才能说完工。
>
> **6. 没看日志就猜代码 / Static guessing on bugs**
> 用户说"线上挂了" → AI 立刻 grep 代码猜原因。**红线 #14：先看日志**。
>
> **7. 跨会话假设记忆 / Cross-session memory loss**
> AI 上次说过 X，新对话里它不记得。**把跨会话有用的内容写进仓库文件**，不要靠它记。
>
> **8. 形式完整内容错 / Looks done not is done**
> AI 给的代码 / 文档结构上完整但内容有错。**抽样核对内容**，不要光看结构。

### 实战策略（5 分钟）

> 我说一个**反复出现的、最值钱**的策略：**让 AI 在动手前列 top-3 不确定**。
>
> 这一句话能让你的 AI 协作效率翻倍。它能：
> - 暴露你提示中没说清楚的部分
> - 让 AI 不在猜测下狂奔
> - 在你浪费 30 分钟等 AI 把错的方向跑完之前打断
>
> 例子：
>
> > 帮我写 X。在你开始之前，列出你最不确定的 top-3 点，我先回答你再开干。
>
> 这一句加在你**所有**复杂提示的末尾。一次澄清省下 5 次返工。

---

## 现场互动

> 现在我让大家做一个 1 分钟练习：
>
> 想一件你**这周必须做的工作**——可以是写邮件、整理客户笔记、做周报、写脚本。
>
> 用上面的"6 件事"框架在心里拟一份提示。
>
> 我会随机点 2 位起来分享他们想到的提示，我们一起看哪里可以改进。
>
> （**点 2 位现场分享**）

---

## 这一节用到的引用

- [`workflows/ai_basics/how_to_give_clear_instructions.md`](../../workflows/ai_basics/how_to_give_clear_instructions.md)
- [`workflows/ai_basics/prompt_pattern_library.md`](../../workflows/ai_basics/prompt_pattern_library.md)
- [`workflows/ai_basics/common_failure_modes.md`](../../workflows/ai_basics/common_failure_modes.md)
- [`workflows/ai_basics/trust_and_verify.md`](../../workflows/ai_basics/trust_and_verify.md)

---

## 节奏

- 6 件事：10 分钟
- 8 种失败：10 分钟
- 实战策略：5 分钟
- 总：25 分钟

→ 进入 [`04_hands_on_exercise.md`](04_hands_on_exercise.md)。
