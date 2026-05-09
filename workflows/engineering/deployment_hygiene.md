---
name: 部署纪律 / Deployment Hygiene
retention: permanent
retention_reason: 工程上线前必读的 SOP，长期复用 / Pre-deploy SOP every engineer must read, reused long-term
---

# 部署纪律 / Deployment Hygiene

> 适用：所有要把代码 / 配置推到测试服 / 生产服的人。
> For: anyone pushing code or config to staging / production.

---

## 一句话 / One Line

**部署不是"代码合了 → 部署吧"。** 是一道独立的纪律，每次都过同一个清单。
**Deploy isn't "code merged → push it".** It's a discipline; the same checklist every time.

---

## 上线前自查表（每次必过）/ Pre-Deploy Checklist (Every Time)

### 代码层 / Code

- [ ] CI 全绿（含单元 / 集成 / lint / type check）/ CI green
- [ ] 至少一位同行评审 approve（重要改动 ≥ 2 位）/ ≥1 peer approve
- [ ] PR 描述对应一份 PRD 或 Bug 编号 / PR maps to PRD / Bug
- [ ] 反向断言测试已清理（红线 #13）/ Reverse-assertions cleaned
- [ ] 没有 commented-out old code / dead code / Dead code removed

### 测试层 / Tests

- [ ] 新功能至少冒烟测试 + 关键路径集成测试通过 / Smoke + integration pass
- [ ] 修 Bug 必有回归测试通过 / Regression test pass
- [ ] 测试服已上 ≥ 24 小时无新增 P0/P1 / On staging ≥ 24h, no new P0/P1
- [ ] 客户面文案过了红线 #2 三道闸（如有变化）/ Customer-facing copy passed gates

### 数据层 / Data

- [ ] 如有数据库迁移 → 在测试服跑过 / DB migration tested on staging
- [ ] 迁移有 **rollback SQL**（不只是"做"，还要能"撤"）/ Migration has rollback SQL
- [ ] 关键表有备份 / 快照 / Critical tables backed up / snapshotted
- [ ] 涉及客户数据的迁移 → 法务 / 合规已知 / Data migration → legal / compliance informed

### 监控层 / Monitoring

- [ ] 新代码的预期错误模式有对应监控 / New error patterns have monitoring
- [ ] 告警阈值合理（不是"每次错误告警"也不是"全无告警"）/ Alert thresholds tuned
- [ ] 告警接收人是真人 + 有 backup / Alerts go to humans + backup

### 沟通层 / Communication

- [ ] 销售 / 客户成功 / 客服 知道这次部署 / Sales / CS / support informed
- [ ] 影响客户的变化 → 客户提前告知（按红线 #2 客户面口径）/ Customer notified if impacted
- [ ] 部署完成后的第一通监控（5-15 分钟）由谁负责 / First monitoring window owner clear

### 时机层 / Timing

- [ ] 不在周五下班前 / Not pre-Friday-COB
- [ ] 不在节前一天 / Not pre-holiday
- [ ] 不在团队大部分人的非工时 / Not during off-hours for most of team

漏一项 → **不部署**，先补齐。
Missing any → **don't deploy**, fix first.

---

## Worktree 清洁 / Worktree Hygiene

部署脚本运行前：
Before deploy script:

- [ ] `git status` 输出干净（no uncommitted changes）
- [ ] 当前 commit 已推送到远程 / Current commit pushed
- [ ] 当前分支是约定的部署分支（main / release）/ On the agreed deploy branch

**看到脏 worktree 不要直接 `git reset --hard`**——先 `git stash`，看清楚里面是什么再决定。
**Don't `git reset --hard` on dirty worktree** — `git stash` first, inspect.

历史教训：一次 `git reset --hard` 抹掉了 7 份在改的源文件 + 3 份测试 + 1 份日志。后来从 stash / reflog 救回来，但当时心跳骤停。
Historical lesson: one `reset --hard` wiped 7 source files, 3 tests, 1 log. Recovered via stash / reflog, but with cardiac arrest.

---

## 部署节奏 / Deploy Cadence

| 类型 / Type | 节奏 / Cadence | 备注 / Notes |
|---|---|---|
| 常规小迭代 | 工作日 10:00-16:00，避开周五 | |
| 大版本 | 提前一周客户告知 + 团队就位 | |
| 紧急修复 | 任何时间，但要有监控 + rollback | |
| 客户面文案 | 与代码部署解耦时，可独立小批 | |

**禁止**：周五下班前部署 / 周末非紧急部署 / 节前一天部署。
**Forbidden**: pre-Friday-COB / non-emergency weekend / pre-holiday.

---

## 部署后 30 分钟 / 30 Minutes After Deploy

不要"部署完就关电脑"。前 30 分钟是**最危险**的窗口：
Don't "deploy and walk away". The first 30 min is the **most dangerous** window:

- [ ] 监控指标对比上线前 / Compare metrics vs pre-deploy
- [ ] 客户报错（客服 / 工单系统）/ Customer errors (support tickets)
- [ ] 错误日志增长率 / Error log growth rate
- [ ] 关键业务路径手测一遍 / Manually walk through critical paths

发现异常 → 不要"再观察一会儿"，立刻判断要不要 rollback。
Anomaly → don't "watch a bit more"; decide rollback now.

---

## Rollback 决策 / Rollback Decision

**优先 rollback 的情境**：
**Rollback first** when:
- 监控指标突然恶化（错误率 / 延迟 / 业务量）/ Metrics suddenly worse
- 客户开始报告问题 / Customer reports starting
- 自己手测时发现关键路径断了 / Critical path broken on manual check
- 不能确定是不是这次部署引起 → 先 rollback 让症状消失，再排查 / Unsure if this deploy caused it → rollback first, investigate later

**优先 forward fix 的情境**：
**Forward fix first** when:
- 已经确认根因，且修复 PR 5 分钟内能完成 / Root cause known + fix < 5 min
- Rollback 涉及数据迁移回退（成本太高）/ Rollback requires data migration unwind (too costly)

不确定 → 默认 rollback（保守）。
Uncertain → default rollback.

---

## 客户告知 / Customer Notification

| 影响等级 / Impact | 提前告知 / Lead time |
|---|---|
| 停机 ≥ 5 分钟 | 至少 24 小时前 |
| 行为变化 | 至少 7 天前 |
| 性能下降可见 | 至少 24 小时前 + 持续监控 7 天 |
| 数据迁移（即使无停机）| 至少 7 天前 + 备份 + 回滚验证 |

告知模板见 [`runbooks/`](../../runbooks/)。
Templates in [`runbooks/`](../../runbooks/).

---

## 部署中的常见错误 / Common Deploy Errors

### 错误 1：周五下班前部署 / Friday-Evening Deploy

❌ "周五修完一个小问题，部一下就走"
**问题**：周末出问题没人在
**修复**：周五 16:00 后**不部署**（紧急除外）

### 错误 2：测试服跳过 / Skip Staging

❌ "改动很小，直接上生产吧"
**问题**：再小的改动也可能在生产数据下表现不同
**修复**：所有改动**必走测试服**

### 错误 3：监控不关心 / Don't Watch Monitoring

❌ 部署完关闭终端
**问题**：前 30 分钟最危险
**修复**：部署人**留在岗位** 30 分钟监控

### 错误 4：rollback 没演练 / Untested Rollback

❌ "我们有 rollback 计划"——但从来没真的演练过
**问题**：真要 rollback 时发现脚本有 bug / 数据格式不兼容
**修复**：每个发布周期演练一次 rollback

### 错误 5：客户没告知 / Customer Not Notified

❌ 客户面行为变化，但客户没收到通知
**问题**：客户发现自己的工作流断了，对你失去信任
**修复**：影响客户的变化按上面的 lead time 告知

---

## "客户告知"语言禁忌 / Banned Words When Notifying Customers

红线 #2 的延伸：
Extension of Red Line #2:

| 禁止 / Banned | 改用 / Replace |
|---|---|
| "运维同步回填" | "正在为您准备数据" |
| "下个迭代上线" | "近期将开放" |
| "Bug-2026-XXXX 已修复" | "这个问题已修复" |
| "下个 deploy 会修" | "我们已识别该问题，正在修复" |
| 模型 endpoint / 内部服务名 | 不出现 |

---

## 速查 / Cheat Sheet

```
上线前清单 6 层：代码 / 测试 / 数据 / 监控 / 沟通 / 时机

Worktree 清洁：git status 干净 + 已 push + 在部署分支
脏 worktree 不要 git reset --hard，先 git stash 看清楚

部署后 30 分钟：监控 + 客服 + 错误日志 + 手测关键路径

Rollback 优先：突然恶化 / 客户报 / 手测断 / 不确定原因
Forward fix 优先：根因明确且 < 5 分钟修

禁止：周五下班前 / 周末非紧急 / 节前一天 / 跳过测试服
```
