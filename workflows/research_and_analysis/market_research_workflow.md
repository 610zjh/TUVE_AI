# 市场调研 / Market Research Workflow

> 适用：销售、产品、运营在做新业务方向 / 新产品 / 新地域时。
> For: sales, product, ops investigating new business directions / products / geographies.

---

## 一句话 / One Line

**市场调研不是"看一堆资料"，是"回答 3-5 个具体的判断题"。** AI 帮你把判断题分解成可证伪的子问题。
**Market research isn't "reading a pile of stuff"; it's "answering 3-5 specific judgment questions".** AI breaks them into falsifiable sub-questions.

---

## 4 步法 / 4-Step Process

### 步 1：把"我想了解市场" 变成具体判断题 / Step 1: Convert "I want to understand X" into Decision Questions

错误起点：
Wrong starting point:
> "我想调研一下短视频 AI 工具市场。"

正确起点：
Right starting point:
> "我要回答的是：(a) 短视频 AI 工具市场目前的头部 3 家是谁、份额多大？(b) 我们的差异化能让我们抢到 X% 的份额吗？(c) 进入这个细分市场需要的最低成本是多少？"

让 AI 帮你做这一步：
Let AI help with this step:

```
我想调研 [领域]。请帮我把它分解成 3-5 个具体判断题，每个判断题：
- 用是 / 否 或具体数字回答
- 回答这个判断题需要哪些证据
- 如果这些证据找不到，说明判断题需要重写
```

### 步 2：列证据来源 / Step 2: List Evidence Sources

```
对上面每个判断题，列出：
- 必须看的 3-5 个数据源（行业报告 / 公开财报 / 政府数据 / 客户访谈）
- 每个数据源的可信度（高 / 中 / 低）
- 每个数据源的获取成本（公开免费 / 付费报告 / 需要访谈）
- 优先级（先看高可信度低成本的）
```

⚠️ AI 会编"看起来权威"的报告名 / 网址 / 作者。**每条都要自己核**。
**Caveat**: AI confabulates "authoritative-sounding" reports / URLs / authors. **Verify each yourself**.

### 步 3：调研执行 / Step 3: Execute Research

按优先级跑：
By priority:
1. 公开数据（行业报告、政府统计、公开财报）/ Public data
2. 半公开（行业大佬演讲、播客、公开访谈）/ Semi-public
3. 自己客户的访谈（已有客户的视角）/ Existing customer interviews
4. 潜在客户访谈（有偏，但不可缺）/ Prospect interviews
5. 内部数据（如果有）/ Internal data if any

**不要靠 AI 给你"行业现状总结"**。AI 给的是训练数据截止前的过时版本，且很可能加工过。
**Don't rely on AI for "industry overview".** AI's data is pre-cutoff and likely processed.

让 AI 帮你 / Use AI to:
- ✅ 整理你**自己拿到的**资料 / Organize material **you brought**
- ✅ 设计访谈问题 / Design interview questions
- ✅ 把多份资料的不同视角对照 / Cross-reference multiple sources
- ❌ 直接告诉你"现状是 X" / Tell you "the state is X" directly

### 步 4：判断 + 落字 / Step 4: Conclude + Write Down

```markdown
# 市场调研报告：<领域>

- 调研期：YYYY-MM-DD ~ YYYY-MM-DD
- 调研人：<name>
- 资料源数量：N（公开 X / 访谈 Y / 内部 Z）

## 判断题 1：[原始判断题]
- 答案：[是 / 否 / 具体数字]
- 证据：
  - [证据 1：来源 + 可信度]
  - [证据 2 ...]
- 反向证据（如果有）：...
- 不确定区间：[结论的置信度，不要装作 100% 确定]

## 判断题 2 ...

## 总结判断
基于以上 X 个判断题，对原始战略问题的回答是：[Y]

## 风险
- 如果我们的核心假设 Z 错了，结论会变成什么？
```

存到 [`meetings/research/`](../../meetings/) 下。
Save under `meetings/research/`.

---

## 反模式 / Anti-Patterns

### 反模式 1：让 AI "总结现状" / Anti-Pattern 1: AI "Summarize the State of X"

❌ "请总结一下中国短视频 AI 工具的市场现状。"

**问题**：AI 的训练数据截止 + 加工偏差，给的"现状"基本是 6-12 个月前的版本，且经常把不同细分市场混在一起。

**修正**：先问自己"我要回答什么具体问题"，再让 AI 帮你回答那个问题（用你提供的资料）。

### 反模式 2：把"找到一份报告"当成调研结束 / Anti-Pattern 2: One Report = Done

❌ 找到一份"行业白皮书"，把里面的数字直接搬到你的报告里。

**问题**：(1) 单一来源不能交叉验证 (2) 行业白皮书本身常常有商业目的（赞助商）

**修正**：每个关键数字至少有 2 个独立来源验证。

### 反模式 3：访谈样本太小 + 偏 / Anti-Pattern 3: Tiny, Biased Interview Sample

❌ 访谈了 3 位现有客户就总结"客户都觉得 X"。

**问题**：现有客户已经选了你，不能代表潜在客户。

**修正**：现有客户 + 流失客户 + 没买的潜在客户三类各 ≥ 3 人。

---

## AI 协助访谈的注意事项 / Notes on AI-Assisted Interviewing

可以让 AI 做 / Allowed:
- ✅ 准备访谈问题清单 / Draft question list
- ✅ 帮你练"如果对方说 X，怎么追问" / Practice probe responses
- ✅ 访谈后整理录音 / 笔记成纪要 / Post-interview note synthesis

不要让 AI 做 / Disallowed:
- ❌ 替你"主持"访谈（除非客户明确同意）/ Host the interview itself
- ❌ 在访谈纪要里"补全"客户没说过的话 / "Fill in" what the customer didn't say
- ❌ 把访谈数据未脱敏就送给 AI 处理 / Send unredacted interview data (Red Line #3)

---

## 速查 / Cheat Sheet

```
1. 把"想调研" → 3-5 个具体判断题（让 AI 帮分解）
2. 每个判断题列证据来源（自己核可信度）
3. 按优先级跑（公开 → 半公开 → 客户访谈 → 内部）
4. 落字成结构化报告（含反向证据 + 不确定区间）

不要：让 AI 凭训练数据告诉你"现状是 X"
要：让 AI 帮你处理你自己拿到的资料
```
