# 运营周复盘 / Weekly Ops Review

> 适用：运营、客户成功、IT、内部工具团队的周复盘。
> For: ops / CS / IT / internal tools weekly reviews.

---

## 一句话 / One Line

**周复盘不是回头看，是为下周做选择。** "上周 X 出了 → 下周我们怎么避免" 才是复盘的产出。
**Weekly review isn't backward-looking; it's forward-choosing.** "X happened last week → how we avoid it next week" is the output.

---

## 标准 5 段结构 / Standard 5-Section Structure

```markdown
# 运营周复盘 - YYYY 年 第 N 周（YYYY-MM-DD ~ YYYY-MM-DD）

## 1. 本周指标快照
（5 个核心指标 + 周环比 + 月环比）

## 2. 本周大事记
（≤ 5 件改变了团队工作流的事件）

## 3. 异常 + 根因
（异常指标 / 客户反馈 / 内部信号 + 每个的最可能 3 个原因）

## 4. 下周必做的 3 件事
（不是"加强 X"，是具体动作 + 负责人 + 截止）

## 5. 一句话感受
（团队当周最大的体感，1 句话）
```

存到 [`meetings/weekly_ops/`](../../meetings/) 下。
Save under `meetings/weekly_ops/`.

retention class = `rollup`（每月底归月度汇总）/ rollup (monthly aggregate at end of month)。

---

## 用 AI 协助的 4 步 / 4 Steps with AI

### 步 1：拼齐数据 / Step 1: Gather Data

每周一固定时段（如周一 9:30），把 5 个核心指标的当周值 / 周环比 / 月环比 拼成表。
Each Monday at a fixed time (e.g., 9:30 AM), assemble the 5 metrics into a table.

```
本周（YYYY-MM-DD ~ YYYY-MM-DD）的运营数据：

[5 个核心指标的当周值 / 上周值 / 上月均值]

请帮我：
1. 标出 top-3 异常（偏离过去 4 周均值 ≥ 20%）
2. 对每个异常，列 3 个最可能的原因（不要给"市场原因"这种空泛）
3. 每个原因对应的"如果是这个，下周应该看到 [Y] 现象" 可证伪假设
```

### 步 2：本周大事记 / Step 2: Weekly Highlights

```
本周影响团队工作流的事件（粘贴你的笔记 / Slack 消息 / 工单）：

请整理成 ≤ 5 件大事记，每件 1-2 句：
- 事件描述
- 对团队的影响
- 是否已经处理 / 还在进行 / 待处理

不要堆砌不影响工作流的事（比如个人请假、不痛不痒的客户问询）。
```

### 步 3：上周决议复盘 / Step 3: Last Week's Decisions

```
上周的"下周必做 3 件事"是 [粘贴上周复盘的第 4 段]。

逐项核：做到了 / 没做到 / 部分。
没做到的：原因 + 是否进入下周 / 是否取消 / 是否调整。
```

### 步 4：下周 3 件事 / Step 4: Next Week's 3

```
基于上面的指标 / 异常 / 大事记 / 上周未完成项，列出下周必做的 3 件事：

每件：
- 具体动作（不是"加强 X"，是"把 X 流程的 Y 步改成 Z"）
- 负责人（具体姓名）
- 截止（具体日期）
- 完成的验证方式

≤ 3 件。如果列出来超过 3 件，按"距离核心目标的远近"砍。
```

---

## 5 个核心指标的选择 / Choosing 5 Core Metrics

每个团队的核心指标不同。挑选标准：
Each team's metrics differ. Selection criteria:

1. **直接反映客户价值**——不是"我们的活动数"，是"客户从我们这里得到的内容产出量" / Reflects customer value directly
2. **有趋势性**——能看周环比、月环比，不是单点 / Trendable (WoW, MoM)
3. **可影响**——这个团队的动作能在 1-4 周内影响这个指标 / Affectable (this team's actions move it within 1-4 weeks)
4. **有口径**——"客户活跃数" 比"客户数" 更有口径 / Defined precisely
5. **互相不冗余**——5 个指标不要全是同一类的变体 / Not redundant

举例（运营团队）/ Example (ops team):
- 本周客户活跃数（DAU / WAU）
- 本周内容产出量
- 客户主动反馈（赞 / 投诉比）
- 工单平均响应时长
- 客户主动续费 / 流失数

---

## "异常 + 根因" 段的关键 / Key to "Anomaly + Root Cause"

不是"X 增加 / 减少了 N%" → "可能是 Y 引起"。
Not "X moved by N%" → "maybe caused by Y".

是：
But:
- 异常具体是什么（哪个指标 / 多少 / 同比）/ The anomaly itself
- 最可能的 3 个原因（不是 1 个，1 个 = 没做选项分析）/ Top 3 candidates
- 每个原因对应"如果是这个，下周应该看到 X" 的可证伪假设 / Falsifiable hypotheses
- 下周哪个动作可以验证哪个假设 / Which action validates which

不要"我们已经评估了原因"这种废话——把具体假设写出来。
Not "we evaluated the causes" — list specific hypotheses.

---

## 周复盘的反模式 / Anti-Patterns

### 反模式 1：流水账 / Activity Log

❌ "周一开会 ... 周二写文档 ... 周三 ..."
**修复**：换成"本周做了的事的价值分类"——紧扣核心目标 / 间接关联 / 偏离

### 反模式 2：自我表扬 / Self-Praise

❌ 全是亮点，没有"做错了 / 没做到"的段。
**修复**：必含"未完成 / 做错 / 走偏的"段。诚实复盘比好看复盘有价值。

### 反模式 3：泛化原因 / Vague Causation

❌ "本周指标下降是因为市场原因 / 客户认知问题"
**修复**：具体可证伪的假设 + 下周验证动作。

### 反模式 4：下周计划 = 上周计划复制 / Copy-Paste Next Week

❌ 上周计划"完成 X" 没做完 → 下周还是"完成 X"，不解释为什么没做完。
**修复**：没完成的事必须分析"为什么没完成"，再决定是否进入下周。

### 反模式 5：5 个指标变 50 个 / Metric Sprawl

❌ "本周 50 个指标的报告" → 没有重点 → 没人读。
**修复**：5 个核心，最多再加 5 个支撑。50 个指标存到看板里随时看，不进周复盘。

---

## 跨团队周复盘的协调 / Cross-Team Weekly Coordination

每个团队有自己的周复盘 → 周一 11:00 跨团队 30 分钟同步。
Each team has their own weekly → Monday 11:00 cross-team 30-min sync.

跨团队同步只解决：
Cross-team sync only solves:
- 跨团队依赖的本周状态 / Cross-team dependency status
- 跨团队冲突 / 资源协调 / Conflicts and resource coordination
- 上周遗留 + 下周需要其他团队配合的事 / Carry-over + needed help

不重复每个团队内部的复盘内容。
Don't repeat each team's internal review.

---

## 速查 / Cheat Sheet

```
5 段结构：指标 / 大事 / 异常 + 根因 / 下周 3 件 / 一句感受

4 步法：拼数据 → 大事记 → 上周决议 → 下周 3 件

5 个指标选择：直接反映客户价值 / 有趋势 / 可影响 / 有口径 / 不冗余

异常段不是"评估了原因"，是 3 个可证伪假设 + 下周验证动作

下周 3 件事 ≤ 3 件，每件含具体动作 / 负责人 / 截止 / 验证

陷阱：流水账 / 自我表扬 / 泛化原因 / 复制上周 / 50 个指标
```
