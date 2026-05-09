---
name: 04 - 动手练习
retention: permanent
retention_reason: 培训中实操段
---

# 第一部分 - 第 04 节：动手练习（25 分钟）

> Part 1, Section 04: Hands-On Exercise (~25 min)

---

## 这一节要让听众离场时记住的

**这套方法论不是抽象的——你今天用一次，明天就能省时间。**
**This methodology isn't abstract — try it once today, save time tomorrow.**

---

## 讲稿（25 分钟）

### 准备（5 分钟）

> 现在所有人打开自己的电脑，跟着我做。
>
> 步骤 1：从 [仓库链接 / 共享盘 / U 盘] 把 `TUZHAN_AI` 仓库下载到本地
> 步骤 2：用 Cursor / Claude Code / Trae / Codex 打开这个仓库
> 步骤 3：发第一条消息给 AI：
>
> > 请先读 AI_MANUAL.md 了解项目导航，然后我会告诉你今天要做什么。
>
> AI 会自动读完入口文件 + 红线 + 导航地图，准备好接收你的任务。
>
> （**确认全场都到这一步了**）

### 练习 1：让 AI 起一份客户简报（10 分钟）

> 我们会用 [`projects/customer_brief_generator/examples/sample_input.txt`](../../projects/customer_brief_generator/examples/sample_input.txt) 这份样例输入。
>
> 这是一份"销售开完电话后的原始笔记"——已经脱敏。
>
> **任务**：让 AI 把它转成一份给客户看的简报草稿。
>
> 给你们的提示模板：
>
> ```
> 我有一份销售电话的原始笔记（在 projects/customer_brief_generator/examples/sample_input.txt）。
>
> 请帮我把它转成一份给客户看的项目简报，按 templates/customer_brief/customer-brief-template.md 的结构。
>
> 约束：
> - 不出现 PRD 编号 / Bug 编号 / 内部代号 / 其他客户名（红线 #2）
> - 数字 / 时间 / 承诺必须基于笔记
> - 客户能看到字面所有内容
>
> 起草前：列 top-3 你最不确定的点。
> ```
>
> 把这个提示发给 AI，等它回。
>
> （**给 5 分钟让大家发提示 + 等 AI 回复**）
>
> 现在大家手里都有一份草稿。让我点 2 位分享他们 AI 给的输出，我们一起评估：
>
> （**点 2 位分享**）
>
> 看你们的输出：
> - 有 PRD 编号 / 内部代号没？
> - 数字是不是来自原笔记？
> - 语气是"我们听到了"还是"营销腔"？

### 练习 2：让 AI 自查红线（5 分钟）

> 现在让 AI **自己审核**它刚才输出的内容：
>
> ```
> 你刚才写的内容请自查：
>
> 闸 1（关键词 grep）：扫一遍是否含有 PRD-XXXX、Bug-XXXX、模型 endpoint、内部岗位代号、其他客户名
> 闸 2（品牌声音）：是不是 TUZHAN 的语气（不堆形容词、不 AI 套话）
> 闸 3（法务可承诺）：所有承诺都能兑现吗？
>
> 列出违规处 + 修改建议。
> ```
>
> 看 AI 怎么自查。这就是 [`workflows/content_creation/marketing_copy_workflow.md`](../../workflows/content_creation/marketing_copy_workflow.md) 里的"三道闸"流程。

### 反思（5 分钟）

> 整个练习用了多久？大概 5-10 分钟得到一份不算太差的客户简报草稿。
>
> 没有这套方法时你会怎么写：
> 1. 看一遍笔记（5 分钟）
> 2. 自己拟结构（10 分钟）
> 3. 写第一稿（15 分钟）
> 4. 检查内部信息泄露（5 分钟）
> 5. 润色（10 分钟）
>
> = 45 分钟。
>
> 用 AI + 这套方法：
> 1. 提示 + 等 AI 回复（5 分钟）
> 2. 让 AI 自查（2 分钟）
> 3. 你润色 + 终审（5 分钟）
>
> = 12 分钟。
>
> 节省的 30 分钟 × 一周 5 通客户电话 × 50 工作周 = **每年节省 125 小时**。**全公司每位销售。**
>
> 这就是为什么我们花一天讲这套方法。

---

## 现场互动

> 让 3 位同事举手分享：
>
> - 一位说"我刚才的提示哪里写得不够好" / 应该怎么改
> - 一位说"AI 给我的输出哪里让我意外" / 好的或不好的
> - 一位说"如果我以后要用这套，我下一周准备先用在哪件事上"

---

## 这一节用到的引用

- [`projects/customer_brief_generator/`](../../projects/customer_brief_generator/) （样例项目）
- [`templates/customer_brief/`](../../templates/customer_brief/)
- [`workflows/content_creation/marketing_copy_workflow.md`](../../workflows/content_creation/marketing_copy_workflow.md)
- [`workflows/ai_basics/how_to_give_clear_instructions.md`](../../workflows/ai_basics/how_to_give_clear_instructions.md)

---

## 节奏

- 准备：5 分钟
- 练习 1：10 分钟
- 练习 2：5 分钟
- 反思：5 分钟
- 总：25 分钟

→ 进入 [`05_qa_and_wrap.md`](05_qa_and_wrap.md)。
