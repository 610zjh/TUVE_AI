# 数据汇总分析 / Data Summarization Workflow

> 适用：把一份数据（CSV / Excel / 数据库导出 / 监控指标）变成可决策的判断。
> For: turning data (CSV / Excel / DB export / metrics) into decision-ready judgments.

---

## 一句话 / One Line

**数据汇总不是"算几个指标"，是"回答一个具体问题 + 给出行动建议"。**
**Data summarization isn't "compute some metrics"; it's "answer a specific question + recommend action".**

---

## 4 步法 / 4-Step Process

### 步 1：明确问题 / Step 1: Clarify the Question

不是"我看一下这份数据"，而是：
Not "let me take a look at this data", but:

> "本月客户流失率从 3% 升到 5%。我要知道流失客户和留存客户在 [X、Y、Z] 维度上有没有显著差异。"

```
我有一份 [数据描述]。我要回答的问题是：

[具体问题]

请帮我：
1. 列出回答这个问题需要看的 3-5 个核心指标
2. 每个指标的计算口径（具体到列名 / 公式）
3. 应该按哪些维度切分（行业 / 月份 / 客户规模 / 价格档位 ...）
4. 我应该警惕哪些数据陷阱（比如季节性、新客 vs 老客口径混淆）
```

### 步 2：脱敏后送 AI / Step 2: Redact, Then Send to AI

数据**必须**先脱敏（红线 #3）。详细脱敏方法见 [`principles/subs/data_and_privacy.md`](../../principles/subs/data_and_privacy.md)。
Redact (Red Line #3). Methods in `principles/subs/data_and_privacy.md`.

最常见的脱敏：
Most common redactions:
- 客户名 → "客户 A / B / C"
- 真实金额 → 量级或排序档位
- 个人信息 → 删除
- 内部代号 → 用功能名替代

### 步 3：让 AI 帮你做汇总 / Step 3: AI-Assisted Aggregation

```
[脱敏后的数据]

请：
1. 计算上面提到的 3-5 个核心指标
2. 按维度切分（行业 / 规模 / 月份 ...）
3. 标出 top-3 异常点（偏离均值 ≥ 20% 或趋势反转的）
4. 不要捏造数据点；如果某个切分下样本太少（< 5），明确说"样本太小不可靠"
```

### 步 4：从数据到判断 / Step 4: Data to Judgment

```
基于上面的汇总，回答：

1. 原始问题的答案是什么？（一句话）
2. 数据支撑这个答案的强度（高 / 中 / 低）？
3. 数据背后最可能的 3 个解释是什么？
4. 每个解释对应一个"如果 X 是原因，下个月应该看到 Y" 的可证伪假设
5. Top-3 行动建议（每个含负责人 / 截止 / 预期效果）
```

---

## AI 处理数据的 4 个常见错误 / 4 Common AI Data Errors

### 错误 1：编造数据 / Fabricated Data

AI 经常会"算出来"几个看起来合理但实际上不在原始数据里的数字。
AI often "computes" plausible numbers that don't actually exist in source.

**防御**：
- 让 AI 给的每个数字标"出处"（哪一行 / 哪一列）
- 关键数字自己用 Excel 或脚本核一遍

### 错误 2：忽略空值 / Null Handling

数据里的 null / 空值 AI 经常静默处理（当 0、当忽略、当均值）。
AI silently handles nulls (as 0, ignore, mean).

**防御**：
- 明确问"空值你怎么处理的？"
- 让 AI 报告每列的空值比例

### 错误 3：抽样 vs 全量混淆 / Sample vs Full

AI 给"客户平均消费 X"——基于的是抽样还是全量？
AI says "average customer spend is X" — based on sample or full?

**防御**：
- 明确口径："你算的是全量 N 个客户的均值，还是其中 M 个的子集？"

### 错误 4：相关 vs 因果 / Correlation vs Causation

AI 看到 X 和 Y 同向变化 → 经常说"X 导致了 Y"。
AI sees X and Y move together → often says "X caused Y".

**防御**：
- 强制 AI 用"X 和 Y 同向变化（相关性 0.X）"，不许"X 导致 Y"
- 任何因果声明要求 AI 给出反向证据测试方案

---

## 适合 AI 做的 vs 不适合 / What AI Is Good / Bad At

| 适合 / Good for AI | 不适合 / Bad for AI |
|---|---|
| 把 CSV / Excel 的列做基础聚合（sum / avg / count） | 涉及大数据量（>10 万行）的精确计算 |
| 找数据里的明显模式 / 异常 | 复杂统计推断（回归、显著性检验） |
| 把数据描述成可读的语言 | 涉及具体业务决策的判断 |
| 起草数据可视化（Markdown 表 / 简单 ASCII 图）| 复杂图表（用 Excel / Python 自己做） |

不适合的部分，让 AI **生成代码**让你自己跑，而不是让 AI 直接给数字。
For "bad for AI" items, have AI **generate the code** you run yourself, instead of giving numbers directly.

---

## 输出标准 / Output Standard

任何数据汇总的最终输出包含：
Every data summary's final output includes:

```markdown
# 数据汇总：[问题]

- 数据范围：YYYY-MM-DD ~ YYYY-MM-DD
- 数据规模：N 行
- 脱敏程度：[详细 / 中等 / 仅个人信息]
- 分析人：[name]
- 分析日期：YYYY-MM-DD

## 原始问题
...

## 关键发现（≤ 5 条）
- 发现 1：[一句话] | 数据支撑：[行号 / 切片] | 强度：[高/中/低]
- 发现 2：...

## 反向证据
（找过哪些反向证据？找到了吗？）

## 不确定区间
（结论的置信度，不要装作 100% 确定）

## Top-3 行动建议
...

## 附：方法论说明
（用了哪些数据、怎么聚合、空值怎么处理、抽样还是全量）
```

存到 [`meetings/analysis/`](../../meetings/) 下。
Save under `meetings/analysis/`.

retention class：如果是月度 / 周度的汇总，用 `rollup`；如果是一次性深度分析，用 `permanent`。
retention: `rollup` for periodic summaries, `permanent` for deep one-off analyses.

---

## 速查 / Cheat Sheet

```
1. 明确问题（不是"看一下数据"，是回答具体判断题）
2. 数据脱敏（红线 #3）
3. AI 协助聚合（强制让它标出处 + 报空值比例 + 区分相关 vs 因果）
4. 从数据到判断到行动（Top-3 行动 + 每个含负责人/截止/预期）

不要：让 AI 在没看到具体数据时给"行业平均值"
不要：把"相关"读成"因果"
要：给每个数字标出处；自己抽查关键数字
```
