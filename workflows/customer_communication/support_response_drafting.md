# 客户支持回复 / Support Response Drafting

> 适用：客服、客户成功、销售在回应客户工单 / 投诉 / 反馈时。
> For: customer service / CS / sales responding to tickets, complaints, feedback.

---

## 一句话 / One Line

**客户在投诉时不要的是"道歉模板"，要的是"我被听到 + 我能做什么"。**
**A complaining customer doesn't want an apology template; they want "I'm heard + here's what I can do".**

---

## 4 步法 / 4-Step Process

### 步 1：分类 / Step 1: Classify

```
请根据下面的客户工单内容，分类：

工单内容：[粘贴]

分类维度：
1. 紧急程度（P0 / P1 / P2 / P3）
2. 类型（Bug / 功能咨询 / 商务咨询 / 投诉 / 表扬 / 误解）
3. 客户情绪（愤怒 / 失望 / 困惑 / 中性 / 友好）
4. 是否涉及法律 / 合规
5. 我应该回复，还是升级给专门人处理

如果分类不确定（多种可能），列出来给我判断。
```

### 步 2：起多版本回应 / Step 2: Draft Multiple Versions

```
基于上面的分类，起 3 个回复候选：

版本 A：偏务实 + 给具体下一步
版本 B：偏共情 + 给情绪安抚 + 下一步
版本 C：偏正式（如果涉及法律 / 合规）

每个版本约束：
- 不出现 PRD 编号 / Bug 编号 / 内部代号 / 其他客户名（红线 #2）
- 不假承诺（"立刻给您解决"如果做不到不能说）
- 包含具体的下一步（不是"我们会跟进"）
- 长度 ≤ 200 字
```

### 步 3：自查 / Step 3: Self-Check

```
对你刚才的 3 个候选，自查：

1. 哪个最贴近客户当下的情绪？
2. 哪些含有"客户能立刻识别为模板的句式"？
3. 哪些下一步是"虚的"（"我们会评估""会优化"）？把它们改成具体动作。
4. 红线 #2 三道闸：禁词 / 品牌声音 / 法务可承诺
```

### 步 4：人审 + 发送 / Step 4: Human Review + Send

红线 #8：发送外部消息前必须人确认。
Red Line #8: human confirms before sending external messages.

特别是 / Especially:
- P0 / P1 工单 → 必须主管 / 客户成功负责人审
- 涉及法律 / 合规 → 必须法务审
- 客户情绪是"愤怒"的 → 至少另一双眼睛审（防止情绪化回应）

---

## 客户情绪 → 回应风格映射 / Emotion → Style Mapping

| 客户情绪 / Emotion | 回应风格 / Response style |
|---|---|
| 愤怒 / Angry | 先共情（"理解您的感受 / 这件事确实给您带来了不便"），再陈述事实和动作。**不要**急着辩护 |
| 失望 / Disappointed | 客观确认问题（"是的，X 确实发生了"），不淡化，给出补救动作 |
| 困惑 / Confused | 简洁澄清，不要堆术语，主动提供"如果您还不确定，可以 [X]" 的出口 |
| 中性 / Neutral | 直接给答案 + 下一步，不需要过多铺垫 |
| 友好 / Friendly | 同样友好，但仍然给具体下一步（不要被"客户友好"误导成可以含糊） |

---

## 法律 / 合规敏感场景 / Legal-Sensitive Scenarios

以下情况**必须**法务参与，不要自己回复：
The following **must** involve legal:

- 客户提到合同条款 / 索赔 / 违约金 / Contract terms, claims, penalties
- 客户提到数据泄露 / 隐私问题 / Data leak, privacy issues
- 客户提到上诉 / 法律行动 / Appeals, legal action
- 客户的反馈可能在公开渠道发酵（社交媒体、监管投诉）/ Could go public

回复模板（占位）/ Holding template:
> 您好，我们已经收到您反馈的问题。这件事我们需要认真核查相关条款 / 处理流程，我会在 24 小时内给您一个明确的回应。期间我们已将您的工单优先级标为最高。

这个回复**不**承诺解决方案，但**承诺**不沉默。买时间让法务介入。
This response **doesn't** commit a solution, but **commits** non-silence. Buys time for legal.

---

## "不能"的四种表达方式 / 4 Ways to Say "No"

客户要求做不到的事时，避免硬"不行"：
When you can't grant a customer's ask, avoid blunt "no":

### 1. "X，但 Y 可以"

> 我们暂时不能 [X]，但我们可以 [Y] 来达成您想要的核心目标。

### 2. "我能做的是 ..."

> 这个具体要求我们这边的标准流程不允许。我能做的是 [备选 1 / 备选 2]，您看哪个对您更合适？

### 3. 转介

> 这个问题超出我的处理范围。我已经把您的工单转给了 [负责人]，他会在 [时间] 前回您。

### 4. "需要更多信息"

> 为了给您准确的答复，我需要先确认 [X / Y / Z]。能否帮我提供一下？

**不要**说 / Don't say:
- "这是我们的政策" → 听起来在推卸 / Shifts responsibility
- "您可以试试 X" → 没具体到能行动 / Not specific
- "我们会努力" → 没承诺什么 / Commits nothing

---

## 复杂工单的"分批回复" / Batched Responses for Complex Tickets

工单涉及多个问题时：
When a ticket has multiple questions:

```
您好，谢谢您的反馈。我把您提的几个问题分开回应：

1. 关于 [A]：[具体回应 + 下一步]
2. 关于 [B]：[具体回应 + 下一步]
3. 关于 [C]：[需要更多信息：请提供 ...]

整体的下一步是 [汇总动作]。如有任何疑问，欢迎随时回复本工单。
```

不要把所有内容堆成一段话——客户会漏掉。
Don't dump everything in one paragraph — customer misses items.

---

## 反复客户的"上下文连续性" / Context Continuity for Recurring Customers

如果一位客户已经有多个历史工单：
For customers with prior ticket history:

```
请把这位客户的所有历史工单（粘贴）汇总：

1. 已解决的核心问题（按时间）
2. 反复出现的问题（如果同类问题第 3+ 次出现，标"系统性问题候选"）
3. 客户对我们的整体满意度走势（基于他的语气 / 主动反馈）
4. 我下次接触他时应该提前知道的 top-3 事
```

让客服不必每次都"从零开始"和这位客户互动。
So support doesn't restart from zero each time.

---

## 红线 / Red Lines

- 红线 #2：客户面回复不出现内部信息
- 红线 #3：内部记录可以提客户名 / 工单细节，但不出仓库
- 红线 #4：客户报告的 Bug → 立刻登记到 [`issues/known.md`](../../issues/known.md)
- 红线 #8：发送前必须人审
- 红线 #14：如果客户报"我的服务挂了"，第 1 个动作是看后台日志，不是先安抚再排查

---

## 速查 / Cheat Sheet

```
4 步：分类（紧急 / 类型 / 情绪 / 法律 / 升级）→ 多版本起草 → 自查 → 人审 + 发

情绪 → 风格：愤怒先共情 / 失望客观 / 困惑简洁 / 中性直接 / 友好同样直接

"不能"四式：X 但 Y / 我能做的是 / 转介 / 需更多信息

红线：客户面无内部信息 / Bug 立刻登记 / 发前必人审 / 法律敏感转法务
```
