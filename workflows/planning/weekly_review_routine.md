---
name: 周复盘 / Weekly Review Routine
retention: permanent
retention_reason: 跨职能通用工作流，长期复用 / Universal cross-functional workflow, reused long-term
---

# 周复盘 / Weekly Review Routine

> 适用：每个人对自己的工作做周复盘；每个团队对团队工作做周复盘。
> For: every individual reviewing their own work; every team reviewing the team's.

---

## 一句话 / One Line

**周复盘不是"我做了什么"的流水账，是"哪些动作下周值得放大、哪些应该减少、哪些应该停止"的判断。**
**A weekly review is not a list of "what I did". It's a judgment on "amplify, reduce, stop" for next week.**

---

## 个人周复盘（30 分钟）/ Personal Weekly Review (30 min)

### 步 1：列本周做了什么（5 分钟）/ Step 1: List What Was Done (5 min)

```
本周的工作大致是 [概述]。具体每一项：
- 周一：...
- 周二：...
- 周三：...
- 周四：...
- 周五：...
```

如果记不全，去 [`issues/known.md`](../../issues/known.md)、[`issues/fixed/`](../../issues/fixed/)、[`workspace_human/meetings/`](../../workspace_human/meetings/)、git log、邮件 / Slack 记录捞。
If you can't recall, scan your trackers, git log, email, Slack history.

### 步 2：用 AI 帮你分类（5 分钟）/ Step 2: AI Classification (5 min)

```
请把上面这些工作按"距离我们公司核心目标的远近"分成三档：

🟢 紧扣核心目标（直接服务于 [核心目标]）
🟡 间接关联（支持核心目标的基础工作）
🔴 偏离核心目标（不知道为什么我做了这件事）

对每一档列出比例（紧扣 / 间接 / 偏离 = X% / Y% / Z%）。
```

如果偏离比例 > 30%，下周需要主动减少这类事。
If "偏离" > 30%, actively reduce this class next week.

### 步 3：识别本周的 3 个高价值动作和 3 个低价值动作 / Step 3: Top 3 + Bottom 3

```
请基于上面的工作，识别：
- Top 3 高价值动作：哪 3 件事产生了最大的产出？为什么？
- Bottom 3 低价值动作：哪 3 件事最浪费时间？为什么？
- 我下周应该如何减少 Bottom 3 的发生？
```

### 步 4：写一段"放大-减少-停止" / Step 4: Amplify–Reduce–Stop

```markdown
## 本周复盘 - YYYY-MM-DD

### 放大（下周做更多的）
- ...

### 减少（下周做少一点的）
- ...

### 停止（下周不做的）
- ...

### 下周必须完成
- [ ] ...
- [ ] ...
- [ ] ...
```

存到你自己的笔记 / 团队周报 / 公开看板里。
Save into your notes / team weekly / public board.

---

## 团队周复盘（45 分钟）/ Team Weekly Review (45 min)

频率：每周一次，最好周五下午（让周末缓冲下周方案）/ 周一上午（让上周记忆鲜活）。
Cadence: weekly, ideally Friday PM (let the weekend cushion next-week's plan) or Monday AM (when last week is fresh).

### 步 1：本周指标 / Step 1: Weekly Metrics (10 min)

每个团队的核心指标各不相同。预先定好一份"本周必看 5 个指标"。
Each team has its own metrics. Define a "weekly top-5 metrics" upfront.

举例 / Examples:
| 团队 / Team | Top-5 metrics |
|---|---|
| 销售 / Sales | 本周入线、Demo 数、成单数、单均、流失数 |
| 运营 / Ops | 内容产出、完播率、客户主动反馈、客户工单 |
| 短视频 / Video | 本周产量、A/B 测胜率、爆款数 |
| 产品 / Product | 上线功能、留存指标、客户主动反馈 |
| 开发 / Engineering | 上线 PR、known.md 增减、P0/P1 数、生产事故 |

每周开会前，AI 把这 5 个指标的本周值 / 周环比 / 月环比 整成一张表。
Pre-meeting: AI compiles the values + WoW + MoM into a table.

### 步 2：异常解读（10 分钟）/ Step 2: Anomaly Reading (10 min)

```
本周指标是 [上面的表]。请：
1. 列出 top-3 异常（数字偏离过去 4 周均值 ≥ 20% 的指标）
2. 对每个异常，列 3 个最可能的原因（不要给"市场原因"这种空泛解释）
3. 列每个原因的"如果是这个原因，下周应该看到 [Y] 现象 / 数据"
```

异常解读不是猜原因，是**列出可证伪的假设**。
Anomaly reading isn't guessing; it's **listing falsifiable hypotheses**.

### 步 3：上周决议复盘（10 分钟）/ Step 3: Last Week's Decisions (10 min)

回到上周复盘里写的"放大 / 减少 / 停止"和"必须完成"清单。
Go back to last week's amplify/reduce/stop and must-complete list.

逐项核：做到了 / 没做到 / 做了一半。没做到的进入下周必做 + 写明原因。
Item-by-item: done / not done / partial. Not-done → next week's must-do + reason.

### 步 4：下周计划（10 分钟）/ Step 4: Next Week's Plan (10 min)

每个 owner 列下周自己最重要的 3 件事 + 需要其他职能配合的事。
Each owner lists their top-3 + needed cross-function help.

需要配合的事**当场拍板谁配合**，不要"会后再对"。
Cross-function dependencies decided **on the spot**, not "let's chat after".

### 步 4.5：handoffs/ 30 天反熵扫（3 分钟）/ Step 4.5: handoffs/ 30-Day Sweep (3 min)

扫一次 [`../../handoffs/inbox/`](../../handoffs/inbox/) 与 [`../../handoffs/outbox/`](../../handoffs/outbox/) 顶层文件 mtime ≥ 30 天的，逐个 4 选 1：留 / 挪（→ runbooks / templates / case_studies / workspace_human/meetings）/ 删（git rm）/ 归档（archive/，开 COMPACT 提案）。

AI 不允许自动执行清理，只列候选。详见 [`../../handoffs/README.md`](../../handoffs/README.md)。

Sweep top-level files in [`handoffs/inbox/`](../../handoffs/inbox/) and [`handoffs/outbox/`](../../handoffs/outbox/) with mtime ≥ 30 days, decide one of four: keep / relocate / delete / archive. AI may only list candidates, never execute cleanup.

---

### 步 5：本周一句话（5 分钟）/ Step 5: One-Line Wrap (5 min)

每位参会者用一句话说本周最大的体感。
Each attendee one sentence on biggest takeaway from the week.

不接续讨论。这一步是给团队"留一个记忆锚点"。
No follow-up discussion. This is a memory anchor for the team.

---

## 月度复盘（90 分钟）/ Monthly Review (90 min)

每月最后一周，把 4 次周复盘汇总。
Last week of each month, aggregate 4 weekly reviews.

```
请把过去 4 周的周复盘（粘贴）汇总成月度复盘：

1. 本月指标趋势（不是单周值，是 4 周走势）
2. 反复出现的"放大""减少""停止"主题——哪些已经形成模式
3. 上月底设定的月度目标完成情况（逐条 ✅ / ⚠️ / ❌）
4. 下月 3 个最重要的事
5. 反复出现的根因 —— 是不是有"流程性问题"已经能识别？

约束：
- 不要重复同一份信息——同一件事如果在多周都出现，归一次
- 不要"整体表现良好"这种废话
- 数字 / 客户名 / 内部代号按红线 #2 处理
```

月度复盘存到 [`workspace_human/meetings/monthly/`](../../workspace_human/meetings/) 下，按月归档。
Save under `workspace_human/meetings/monthly/`, archived monthly.

retention class = `rollup`（每年底归一份年度汇总）。
retention class = `rollup` (annual rollup at year-end).

---

## 季度 / 半年 / 年度复盘 / Quarterly / Semi / Annual Reviews

频率越低，复盘越深。年度复盘建议 1-2 天的封闭式会议。
Lower frequency → deeper review. Annual review: 1-2 days off-site.

详见 [`templates/weekly_review/`](../../templates/weekly_review/) 里的"季度复盘 / 年度复盘"模板。
See "quarterly / annual review" templates in `templates/weekly_review/`.

---

## 复盘的反模式 / Anti-Patterns

| 反模式 / Anti-pattern | 表现 / Symptom | 修正 / Fix |
|---|---|---|
| **流水账** Activity log | "周一开会 ... 周二写文档 ... 周三 ..." | 加分类 + 价值判断 |
| **自我表扬** Self-praise | "本周亮点：X、Y、Z" 但没说 W、Q 没做到 | 必含"未做到 / 做错了"段 |
| **泛化原因** Vague causation | "市场原因 / 客户认知问题" | 列具体可证伪的假设 |
| **无具体行动** No specific action | "下周要加强 X" | 改成"下周一上午之前完成 X 的具体动作 1, 2" |
| **同一件事说五遍** Repeated point | 每周都说"X 重要" | 写到团队章程里，从此不在每周复盘里重复 |

---

## 周复盘是协作记忆 / Weekly Review Is Collaborative Memory

个人周复盘存自己看；团队周复盘存全队看；月度复盘存所有相关方看。
Personal review for yourself; team review for the team; monthly for all stakeholders.

为什么写下来很重要：**人的记忆有偏，写下来的版本是真相**。
Why writing matters: **human memory is biased; written records are truth**.

3 个月后回看本季度的周复盘，你会发现："原来这个问题在 8 周前就出现过苗头"——而当时你没察觉。
3 months later, scanning quarterly weekly reviews → "this issue showed up 8 weeks ago" — that you missed at the time.

这就是复盘最大的价值：**让模式可见**。
That's the value: **making patterns visible**.
