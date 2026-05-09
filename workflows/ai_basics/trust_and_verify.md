# 什么时候相信 AI、什么时候必须自己验证 / Trust and Verify

> 这条工作流回答一个本质问题：**AI 给我的东西，我多大程度上能直接用？**
> This workflow answers the core question: **how much of AI's output can I use directly?**

---

## 一句话 / One Line

**AI 的自信度和正确率没有强相关。** 它最自信的回答有时正是它编造最严重的部分。
**AI's confidence and correctness are weakly correlated.** Its most confident answer is sometimes its worst hallucination.

---

## 三色分级 / Three-Color Tiers

### 🟢 绿灯：可以直接用 / Green: Use directly

AI 在这些事上基本可信：
AI is generally reliable on:

- **形式化任务**：翻译、改语法、改格式、统一标点 / Formal tasks: translation, grammar, formatting, punctuation
- **通用编程模板**：用 Python 写个 for 循环、用 SQL 写个 group by / Generic programming templates
- **结构化产出**：按你给的模板填空 / Structured output: filling templates you provide
- **总结你给的材料**：基于你提供的输入做提炼 / Summarizing material you provided

⚠️ 注意：即使绿灯，仍要扫一眼输出。AI 偶尔会"绿灯里翻车"。
Caveat: even green-lit, scan the output. AI occasionally "fails on greens."

### 🟡 黄灯：需要核对关键信息 / Yellow: Verify key facts

AI 在这些事上多半对，但要核对：
AI is mostly right, but verify:

- **你领域内的概念解释**：核对核心定义 / Concepts in your domain: check core definitions
- **行业一般做法**：核对"业界标准"和你公司的实际差异 / Industry general practices: cross-check with your company's actual practice
- **基础数据计算**：核对算式逻辑（不光看结果）/ Basic calculations: check the formula, not just the answer
- **多步推理结论**：核对推理链中是否每一步都成立 / Multi-step reasoning: verify each step

### 🔴 红灯：必须自己验证或不用 / Red: Verify yourself or don't use

AI 在这些事上经常错：
AI frequently errors on:

- **具体数字 / 日期 / 客户名** / Specific numbers, dates, customer names
- **法律条款 / 合规细节** / Legal terms, compliance specifics
- **金额 / 财务数据** / Money, financial data
- **客户的具体情况**（它没参加你的电话）/ Customer specifics (it wasn't on your call)
- **代码中具体的 API 名 / 库版本号** / Specific API names, library version numbers
- **引用文献 / URL / 文件路径**（AI 会编造看起来合理的）/ Citations, URLs, file paths (AI fabricates plausible-looking ones)
- **它"没读过的文件"的内容**（如果它声称读过却内容不对）/ Content of files it "didn't actually read"
- **任何"看起来太顺利了"的输出** / Any output that looks "suspiciously smooth"

红灯的事情，**必须自己核**。AI 给的只能当**初稿 + 提醒清单**。
Red-tier items: **verify yourself**. Treat AI output as **draft + checklist**, not final.

---

## 验证 4 招 / 4 Verification Tactics

### 招 1：让 AI 自己标依据 / Tactic 1: Make AI Cite

```
你刚才写的每一个事实声明后面，加一个 [来源: ...] 标记。
来源可以是：(a) 我提供给你的材料 §X, (b) 你从训练数据知道的（标"通识"），
(c) 你猜的（标"未验证"）。

如果某条没法标 (a) 或 (b)，请改写或删掉。
```

效果：AI 会自动暴露哪些内容是靠谱的、哪些是猜的。
Effect: AI auto-flags reliable vs guessed content.

### 招 2：双盲对照 / Tactic 2: Double-Blind Comparison

复杂事实题：开两个新对话，问一样的问题，对比答案。
Complex factual questions: open two fresh chats, ask the same question, compare.

不一致 = AI 在这个问题上不可靠。
Inconsistency = AI is unreliable on this question.

### 招 3：反向自查 / Tactic 3: Reverse Self-Check

```
你刚才的回答如果错了，最有可能错在哪 3 处？
列出 top-3 最容易被反驳的点。
```

AI 自己有时会指出它原始回答的薄弱点。
AI sometimes self-identifies weak spots in its original answer.

### 招 4：边界测试 / Tactic 4: Edge-Case Test

输入"它最不熟"的边界 case：
Feed it edge cases it's "least familiar" with:

- 极小输入 / 极大输入 / Very small / very large
- 反直觉前提 / Counter-intuitive premise
- 它不熟的具体术语 / Niche jargon
- 涉及最近发生的事 / Recent events

如果在边界 case 上崩了，说明它对这个领域的"地图"是粗的。中心区域可能仍然 OK。
If it breaks on edges, the territory map is coarse — center may still be OK.

---

## 不要做的 4 件事 / 4 Things NOT to Do

### 1. 不要因为"AI 说的"就跳过自己的判断

❌ "AI 觉得这个客户应该接，那就接吧"
**问题**：AI 不知道你客户的具体情况，它只是基于你给它的有限信息推断
**Fix**: 决策权在你，AI 给的是建议

### 2. 不要假设"AI 这次对，下次也对"

AI 的对错有概率分布。今天对的明天不一定对（特别是涉及具体数据时）。
AI's correctness is probabilistic. Right today doesn't mean right tomorrow (especially on specific data).

### 3. 不要把 AI 的"自信"当"对"

AI 用流畅语言陈述错误结论是常态。它不知道自己错。
AI confidently stating wrong conclusions is common. It doesn't know it's wrong.

### 4. 不要在你不熟的领域全靠 AI 验证

❌ "我让 AI 给我写一份法律文件，然后让 AI 自己核对一遍"
**问题**：AI 自查 AI = 同一个偏差源
**Fix**: 你不熟的领域，找真人专家或权威资料核

---

## 工具 / 模型差异 / Model Differences

不同模型在不同任务上的可信度不同。粗略经验：
Reliability varies across models. Rough heuristic:

| 任务 / Task | 倾向更可信 / Tend more reliable | 倾向更不可信 / Tend less reliable |
|---|---|---|
| 数学计算 / Math | 带工具调用的模型 / Tool-augmented models | 无工具的模型 |
| 实时事实 / Realtime facts | 带搜索的模型 / Search-augmented | 训练截止前的纯模型 |
| 代码 / Code | 在代码上 fine-tune 过的 / Code-FTed | 通用模型 |
| 中文文本质量 / CN text | 中文为主训练的 / CN-heavy training | 英文为主的 |

不要依赖单一模型。重要决策可以**用两种不同模型分别问**，不一致 = 警钟。
Don't rely on a single model. For important decisions, **ask two different models**; disagreement = warning bell.

---

## 速查卡 / Cheat Card

```
绿灯（直接用）：形式化任务 / 通用模板 / 总结你给的材料
黄灯（核对关键）：领域概念 / 业界做法 / 基础计算 / 多步推理
红灯（必须验证）：具体数字 / 法律 / 金额 / 客户具体情况 / API 名 / 引用

验证 4 招：让 AI 标依据 / 双盲对照 / 反向自查 / 边界 case 测试

不要：把 AI 自信当对 / 跨次假设依然对 / 在你不熟的领域全靠 AI 自查
```
