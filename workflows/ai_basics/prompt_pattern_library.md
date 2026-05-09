---
name: 提示词模式库 / Prompt Pattern Library
retention: permanent
retention_reason: 全员通用基础工作流，长期复用 / Universal AI-basics workflow, reused long-term
---

# 提示词模式库 / Prompt Pattern Library

> 已经反复证明好用的提示词结构。直接复用，不必每次重发明。
> Patterns proven to work. Reuse directly; no need to reinvent each time.

---

## 1. 总结模式 / Summarize Pattern

```
请把下面这份 [文档 / 邮件 / 会议纪要] 总结给 [目标读者]。

输出形式：
- [N] 段 / [N] 行
- 每段开头一句结论，结论后是支撑事实
- 不要"综上所述""值得注意的是"这种 AI 套话

[材料]
```

---

## 2. 起草并自查模式 / Draft-and-Self-Check Pattern

```
请帮我起草 [产出]。

[6 件事填好]

起草完成后，自己过一遍：
- [ ] 红线 #2：客户面文案没有 PRD 编号 / Bug 编号 / 内部代号
- [ ] 数字都来自我给你的材料，没有编造
- [ ] 没有"AI 套话"（详见 `principles/subs/content_quality.md`）

自查通过后再交给我。
```

---

## 3. 多版本对比模式 / Multiple-Version Pattern

```
请按下面的指令各起 3 个版本：
1. 风格 A：[偏正式]
2. 风格 B：[偏轻松]
3. 风格 C：[偏数据驱动]

每个版本不要超过 [N] 字。
我会从 3 个里挑一个再让你深化。
```

适合：第一次写新内容、不确定基调时。
Best for: first drafts of new content, uncertain about tone.

---

## 4. 反向自检模式 / Self-Critique Pattern

```
你刚才写的内容请自己反驳一遍：
- 哪些地方最容易被读者质疑？
- 哪些事实没有出处？
- 哪些段落如果删了不影响核心？

把上面三个回答完了之后，按你自己的反驳改一版。
```

适合：终稿前一道关。
Best for: final-draft pass.

---

## 5. 边界 case 提问模式 / Edge-Case Test Pattern

```
你刚才写的 [代码 / 流程 / 文档] 在以下情况会怎样：
1. 输入是空的？
2. 输入是异常大的？
3. 上下游突然不响应？
4. 用户中途取消？
5. [一个你想到的具体边界 case]

给每个 case 回答：(a) 现在会发生什么 (b) 应不应该改 (c) 怎么改
```

适合：写完代码 / 流程 / runbook 之后的健壮性自查。
Best for: post-write robustness check on code / processes / runbooks.

---

## 6. 改稿模式（不要从头写）/ Edit-Don't-Rewrite Pattern

当 AI 的稿基本对，只需要小修时：
When AI's draft is mostly right, just small edits:

```
基本可以。改这几处：

第 2 段第 1 行："X" → "Y"，理由：[简单理由]
第 4 段整段删除，理由：[简单理由]
末尾加一段 30 字以内的"接下来"

其他保持不动。
```

**不要**：
- ❌ "重写一下"——AI 可能从头改，把已经对的也改坏
- ❌ "再改改"——它不知道改哪里

---

## 7. 不确定时让 AI 问回模式 / "Ask Me Back" Pattern

```
[6 件事填好]

注意：在你开始干之前，列出你最不确定的 top-3 个点。
我先回答你的问题，你再开干。
不要凭猜测就开始写——猜错了我们要全部重来。
```

**这是最值钱的一招**。一次澄清能省下后面 5 次返工。
**This is the highest-leverage trick.** One clarification saves 5 future iterations.

---

## 8. 反复性任务的标准提示 / Repeating-Task Standard Prompt

某种任务你每周都做（如：周复盘、客户邮件、视频脚本）：
For tasks you do weekly (e.g., weekly review, customer email, video script):

1. 第一次：用 6 件事框架写一遍详尽提示
2. AI 给的版本你打磨好
3. 把这次的提示 + 最终产出 → 存到 [`templates/`](../../templates/) 下相应模板里
4. 下一次：直接 `@templates/<name>` 引用模板，AI 自己组合上下文

模板见 [`templates/`](../../templates/)。
Templates at [`templates/`](../../templates/).

---

## 9. 角色扮演模式（慎用）/ Role-Play Pattern (Use Cautiously)

```
请扮演 [角色] 来评审 [产出]：
- 角色：5 年经验的 SaaS 产品经理
- 评审目标：找出 [产出] 在 [维度] 上的问题
- 输出：列出 top-5 问题，每个 1-2 句说明

注意：你只是模拟这个角色的视角，不是真的扮演具体人。
不要冒充真实公司 / 真实人士的判断。
```

适合：拿不到真专家时，让 AI 模拟一个角色视角做评审。
Best for: when you can't get a real expert, simulating a role's perspective for review.

注意：AI 模拟的"专家"经常错。**不要**把 AI 模拟的判断当成真实专家的判断引用。
Caveat: simulated "experts" are often wrong. **Don't** cite AI-simulated judgments as real expert opinion.

---

## 10. "我读完，你执行"模式 / "I-Read-You-Execute" Pattern

适合：你不熟的领域，但需要 AI 帮你做事。
Best for: domains you're unfamiliar with but need AI to act in.

```
我对 [领域] 不熟。请：
1. 用 3 段话给我讲清楚我接下来要做的事的核心概念
2. 在我读完确认理解后，再开始执行
3. 执行过程中如果有任何"假设我懂某个前置概念"的步骤，停下来告诉我
```

防止 AI 跑得太远，把你抛在后面。
Prevents AI running ahead and leaving you behind.

---

## 11. "防止跑偏"的硬约束 / Hard-Constraint Pattern Against Drift

```
[6 件事]

硬约束（你必须遵守，不许"为了帮我而忽略"）:
- 不超过 [N] 字
- 不出现 [禁词清单]
- 必须包含 [必含清单]
- 不许做 [禁止动作]：包括 [具体禁动作 1, 2, 3]

如果 [硬约束] 和我其他指令冲突，按硬约束。
```

适合：需要严格符合规范的场景（合规 / 法务 / 客户面文案）。
Best for: scenarios requiring strict spec compliance (compliance / legal / customer-facing copy).

---

## 12. 把这套库本身扩展 / Extending This Library

发现某个新的提示词结构对你工作很好用 → 把它**加进这个文件**。
When you discover a new prompt pattern that works well → **add it to this file**.

加的时候按上面格式写：模式名、模板、适合场景。
Add it in the format above: pattern name, template, when to use.

让这份库随业务进化。
Let this library evolve with the business.
