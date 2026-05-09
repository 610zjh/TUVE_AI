---
name: 04 - 部署纪律 + 工程红线深讲
retention: permanent
retention_reason: 培训第二部分技术纪律段
---

# 第二部分 - 第 04 节：部署纪律 + 工程红线深讲（15 分钟）

> Part 2, Section 04: Deployment Discipline + Engineering Red Lines Deep Dive (~15 min)

---

## 这一节要让听众离场时记住的

**部署不是"代码合了就推"，是一道独立的纪律。每次都过同一个清单。** 没看日志前不超过 3 轮静态猜测。
**Deploy isn't "code merged → push it"; it's a discipline. Same checklist every time.** ≤ 3 rounds of guessing before logs.

---

## 讲稿（15 分钟）

### 上线前自查表（5 分钟）

> 每次部署到生产前必过 8 件事（[`workflows/engineering/deployment_hygiene.md`](../../workflows/engineering/deployment_hygiene.md) 详细）：
>
> 1. CI 全绿 + 至少 1 位评审 approve
> 2. PR 描述对应一份 PRD 或 Bug 编号
> 3. 反向断言测试已清理（红线 #13）
> 4. 测试服已上 ≥ 24 小时无新增 P0/P1
> 5. Rollback 方案清楚（一句话能说出"如果 X 出问题就 Y"）
> 6. 销售 / 客户成功 / 客服已通知
> 7. 监控会捕获新代码的预期错误模式
> 8. 客户面文案过红线 #2 三道闸（如有变化）
>
> 漏一项 → **不部署**，先补。
>
> **禁止**的时机：周五下班前 / 周末非紧急 / 节前一天。
>
> 真实事故：去年某周五 17:00 部了一个"小修复" → 18:00 出问题 → 周末群里热闹，最终周日凌晨才修复。
> 立规：周五 16:00 后**不部署**（紧急除外）。

### Worktree 清洁（3 分钟）

> 部署脚本运行前：
> - `git status` 必须干净（no uncommitted changes）
> - 当前 commit 已推送到远程
> - 在约定的部署分支
>
> **看到脏 worktree 不要直接 `git reset --hard`**——先 `git stash`，看清楚里面是什么。
>
> 真实教训：一次直接 reset 抹掉了 7 份在改的源文件 + 3 份测试 + 1 份日志。后来从 stash / reflog 救回来，但当时心跳骤停。

### 红线 #14：线上故障第 1 个动作 = 看日志（5 分钟）

> 这条特别重要。
>
> 用户报"线上挂了 / 测试服 / 500 / 报错" 时，AI 的第 1 个动作**必须**是**SSH 拉真实日志拿真实 traceback**。
>
> **禁止**在没看日志前做超过 3 轮"我猜原因可能是 X"的静态分析。
>
> 真实事故：一条日志能定位的 500 错误，曾经在源码里瞎猜了 10+ 轮，浪费 1 小时多。
>
> 我现场演示。假设有人报"客户后台又 500 了"：
>
> **错的反应（不要这样）：**
>
> > 我看一下代码 ... grep ... 我猜可能是 X 引起 ... 让我再看 ... 可能是 Y ...
>
> （AI 在 grep，但完全没看真实日志，纯猜）
>
> **对的反应：**
>
> ```bash
> # 30 秒内启动这个命令（把 <...> 换成你自己的生产机和容器名）
> ssh root@<your-prod-host> 'docker logs <your-app-container> 2>&1 | grep -E "Traceback|500" | tail -50'
> ```
>
> 拿到真实 traceback → 看真实代码层 → 修。
>
> 这条规矩在 [`workflows/engineering/debugging_workflow.md`](../../workflows/engineering/debugging_workflow.md) 和 [`workflows/operations/incident_response_workflow.md`](../../workflows/operations/incident_response_workflow.md) 都有。
>
> 把"看日志"做成肌肉记忆。

### 短串其他工程红线（2 分钟）

> 我快速过一遍其他工程红线（详细在 [`principles/subs/code_quality.md`](../../principles/subs/code_quality.md) 和 [`principles/subs/deployment_and_ops.md`](../../principles/subs/deployment_and_ops.md)）：
>
> - **#9 命名永久化**：禁止 demo_/sample_/placeholder_/tmp_/final_。每个名字假设它会活 5 年。
> - **#7 单文件 ≤ 800 行**：超过 → 提 COMPACT-NNNN 拆分提案。
> - **#10 收尾五件套**：测试 / 版本 / PRD 快照 / 导航 / Bug 移位——任一缺失禁止说"完工"。
> - **#13 修 Bug 同步清反向断言测试**：在同一 commit 里翻转或删除断言旧错误行为的测试。

---

## 现场互动

> 让大家举手回答（不必出声，举手就行）：
>
> Q1: 你过去 3 个月**违反过几次**红线 #14（看日志）？（应有不少举手）
> Q2: 你过去 3 个月**部署前漏过几次**自查表？（应有不少）
> Q3: 你过去 3 个月有过"周五下班前部署"吗？（最好少）
>
> 不举手就是"违反 0 次" —— 我希望未来 3 个月这是大多数。

---

## 这一节用到的引用

- [`workflows/engineering/deployment_hygiene.md`](../../workflows/engineering/deployment_hygiene.md)
- [`workflows/engineering/debugging_workflow.md`](../../workflows/engineering/debugging_workflow.md)
- [`workflows/operations/incident_response_workflow.md`](../../workflows/operations/incident_response_workflow.md)
- [`principles/subs/deployment_and_ops.md`](../../principles/subs/deployment_and_ops.md)
- [`runbooks/engineering_emergency_rollback.md`](../../runbooks/engineering_emergency_rollback.md)

---

## 节奏

- 上线前清单：5 分钟
- Worktree：3 分钟
- 红线 #14：5 分钟
- 其他红线：2 分钟
- 总：15 分钟

→ 进入 [`05_qa_and_wrap.md`](05_qa_and_wrap.md)。
