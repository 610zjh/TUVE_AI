---
name: 部署与运维 / Deployment and Ops
description: 上线前自查、出故障第 1 个动作看日志、运维交接的纪律 / Pre-deploy checklist, "logs first" on incidents, ops handoff discipline
type: permanent
retention: permanent
retention_reason: 一次错误的部署 / 误判故障原因可以让客户当场感受到，代价极高 / A bad deploy or misdiagnosed incident is felt instantly by customers
---

# 部署与运维 / Deployment and Ops

## 红线 #14 重申 / Red Line #14 Restated

**线上故障的第 1 个动作 = 看日志。**
**Action #1 on a production incident = look at logs.**

用户以"线上 / 测试服 / XX 挂了 / 500 / 报错"姿态来时，AI 的第 1 个动作必须是拉真实日志，拿到真实 traceback。
When the user reports "production / test server / X is down / 500 / error", AI's first action must be pulling real logs and getting the real traceback.

**禁止**在没拿到日志前做 3 轮以上本地静态分析 / 猜代码 / grep。
**Forbidden** to do > 3 rounds of local static analysis / code guessing / grep before logs.

历史教训：一条日志就能定位的故障曾经被瞎猜了十几轮。
Historical lesson: an incident resolvable by one log line has wasted 10+ rounds of guessing.

---

## 线上故障响应阶梯 / Incident Response Ladder

```
听到"线上挂了" / "Production is down"
    │
    ▼
1. 拉日志（30 秒内启动） / Pull logs (start within 30 seconds)
    │
    ▼
2. 找 traceback / 异常堆栈 / Find traceback / exception stack
    │
    ▼
3. 看时间线（什么时候开始的、影响多少请求）/ Read timeline (since when, request count affected)
    │
    ▼
4. 看是否在最近 deploy 之后（90% 故障是上一次 deploy 的副作用）
    Check if right after the last deploy (90% of incidents are deploy side-effects)
    │
    ├── 是 → rollback 或 forward fix（看变化大小） / Yes → rollback or forward fix
    └── 否 → 看 traceback 定位代码 / 数据 / 第三方原因 / No → use traceback to triage
```

**前 3 步不许跳**。从来没有"我看一眼代码就知道是什么问题"的真实捷径——你"看一眼"想到的可能是错的、看似合理的猜测。
**Steps 1-3 are non-skippable.** "I'll just glance at the code" is never a real shortcut — what you "glance and think" is plausible-but-wrong.

---

## 上线前自查表 / Pre-Deploy Checklist

每次部署到生产前，必过：
Before every prod deploy:

- [ ] **PRD 完成快照**已写完（红线 #10 五件套之一）/ PRD Completion Snapshot is filled
- [ ] **回归测试**全过（含本次修复的 Bug 的回归测试）/ Regression tests all pass (including bug-fix regression)
- [ ] **反向断言测试**已清理（红线 #13）/ Reverse-assertion tests cleaned (Red Line #13)
- [ ] **测试服**已先于生产上 ≥ 24 小时，无新增 P0/P1 / Staging deployed ≥ 24h with no new P0/P1
- [ ] **Rollback 方案**清楚（一句话能说出"如果 X 出问题就 Y"）/ Rollback plan clear (one-sentence "if X then Y")
- [ ] **影响范围告知**已发出（销售 / 运营 / 客服 / 客户）/ Impact-scope notification sent (sales / ops / support / customers)
- [ ] **监控**已确认会捕获新代码的预期错误模式 / Monitoring confirmed to catch the new code's expected failure modes
- [ ] **数据库迁移**（如有）已在测试服跑过、有回滚 SQL / DB migration (if any) tested on staging with rollback SQL
- [ ] **客户面文案**已通过红线 #2 三道闸 / Customer-facing copy passed Red Line #2's three gates

漏一项 → 不发布 / 推迟。
Missing any → don't deploy / postpone.

---

## 部署节奏 / Deployment Cadence

| 类型 / Type | 节奏 / Cadence | 备注 / Notes |
|---|---|---|
| **常规小迭代** Routine small | 工作日 10:00-16:00，避开周五 / Weekdays 10:00-16:00, avoid Fridays | 周五出问题没人在，周末烧 |
| **大版本** Major | 提前一周公告 + 客户告知 / 1 week advance announcement + customer notice | 含数据迁移 / 行为变化的 |
| **紧急修复** Hotfix | 任何时间，但要监控+回退方案 / Any time, with monitoring + rollback | P0/P1 的 Bug |
| **客户面文案变更** Customer-facing copy | 与代码部署解耦时，可独立小批 / If decoupled from code, batch independently | 文案变更也是变更 |

**禁止**：周五下班前部署；周末非紧急部署；节前一天部署。
**Forbidden**: deploys after Friday COB; non-emergency weekend deploys; pre-holiday deploys.

理由：出问题没人在班上，损失放大。
Reason: failures during off-hours blow up unattended.

---

## 监控与告警 / Monitoring and Alerts

每个新功能上线时必备：
Each new feature on launch:

1. **业务指标监控** / Business metric monitoring
   - 关键漏斗（从入口到核心动作的转化率）/ Key funnel (entry → core action conversion)
   - 错误率（按错误类型分类）/ Error rate (by category)
   - 延迟（P50 / P95 / P99）/ Latency (P50 / P95 / P99)

2. **告警阈值** / Alert thresholds
   - 不要"每次错误都告警"——会被忽略 / Not "every error" — alerts get ignored
   - 阈值 = 业务能接受的最低质量 / Threshold = lowest acceptable quality
   - 阈值要可调 / Thresholds must be tunable

3. **告警接收人** / Alert receivers
   - **真人**而不是邮件归档 / **Real humans**, not just an email archive
   - 轮值（不要永远是同一个倒霉蛋）/ Rotation (not always the same poor soul)
   - 工时外有 backup / On-call backup outside work hours

---

## 测试服 vs 生产服 / Staging vs Production

测试服的角色：
Staging's role:
- 上线前做最终验证 / Final pre-prod verification
- 客户演示用（如果客户参与试用）/ Customer demos (if involved in trial)
- AI 自由调试 / 测试边界用例 / AI free debugging / boundary case testing

生产服的角色：
Prod's role:
- 真客户在用 / Real customers
- 改动必须经过测试服 / Changes must pass staging
- 出问题第一反应：止损 → 看日志 → 修复 / 回退 / On incident: mitigate → logs → fix or rollback

测试服的特殊纪律 / Special disciplines for staging:
- 测试服自己复现 Bug 产生的成本（如 AI 调试烧 token）**不退**——这是测试服的用途 / Costs from AI debugging on staging itself are **not refundable** — that's what staging is for
- 测试服**也是真实环境**，不要"反正是测试服我乱来"——bug 也会被记录 / Staging is still real environment — "it's just staging" is not license to thrash; bugs are still tracked

---

## 部署前 worktree 清洁 / Worktree Hygiene Before Deploy

部署脚本运行前 / Before running deploy script:

- `git status` 必须干净（no uncommitted changes）/ `git status` clean (no uncommitted changes)
- 当前 commit 必须**已推送**到远程 / Current commit **pushed** to remote
- **看到脏 worktree 不要直接 `git reset --hard`**——先 `git stash`，看清楚里面是什么 / **Dirty worktree → don't `git reset --hard`** first; `git stash` and inspect

历史教训：一次直接 reset 抹掉了 7 份在改的源文件 + 3 份测试 + 1 份日志。后来全部从 stash / git reflog 救回来，但当时心跳骤停。
Historical lesson: one `git reset --hard` wiped 7 in-progress source files, 3 tests, 1 log. Recovered via stash / reflog, but with cardiac arrest.

---

## 客户告知的纪律 / Customer Notification Discipline

部署有客户感知（停机 / 行为变化 / 性能变化）时：
When deploys are customer-visible (downtime / behavior / perf changes):

| 影响等级 / Impact | 提前告知时间 / Lead time |
|---|---|
| 停机 ≥ 5 分钟 / Downtime ≥ 5 min | 至少 24 小时前 / ≥ 24h ahead |
| 行为变化（同一动作结果不同）/ Behavior change | 至少 7 天前 / ≥ 7 days ahead |
| 性能下降可见 / Visible perf degradation | 至少 24 小时前 + 监控持续 7 天 / ≥ 24h ahead + 7-day monitoring |
| 数据迁移（即使无停机） / Data migration (even zero-downtime) | 至少 7 天前 + 备份 + 回滚验证 / ≥ 7 days ahead + backup + rollback drill |

告知模板见 [`runbooks/`](../../runbooks/)。
Notification templates in [`runbooks/`](../../runbooks/).

---

## "运维语言" 的客户面禁忌 / Banned Phrases When Talking to Customers

这是红线 #2 的延伸。出于运维场景特别再列一遍：
Extension of Red Line #2, repeated for ops contexts:

| 禁止 / Banned | 改用 / Replace with |
|---|---|
| "运维同步回填" | "正在为您准备数据" |
| "下个迭代上线" | "近期将开放" |
| "服务器挂了" | "暂时无法处理，请稍后重试" |
| "数据库锁了" | "暂时无法处理" |
| "下个 deploy 修复" | "我们已经识别该问题，正在修复中" |
| "Bug-2026-XXXX 已记录" | "这个问题我们已记录" |

---

## AI 在故障响应中的边界 / AI's Boundary in Incident Response

AI 可以做的 / AI may do:
- ✅ 看日志、grep、组合查询 / Read logs, grep, compose queries
- ✅ 写一份"我目前看到的"小结给人类决策 / Write "what I see so far" summary for human triage
- ✅ 起草 rollback 命令（人审核后执行）/ Draft rollback commands (human approves before exec)
- ✅ 起草客户告知邮件 / 公告（人审核后发）/ Draft customer notice (human approves before sending)
- ✅ 在 [`issues/known.md`](../../issues/known.md) 起草 Bug 条目 / Draft issue entry in `issues/known.md`

AI 不能做的 / AI may NOT do:
- ❌ 自主执行 rollback / 部署 / Execute rollback / deploy autonomously
- ❌ 自主重启服务 / 删数据 / 改数据库 / Restart services / delete data / modify DB autonomously
- ❌ 自主对外发故障通告 / Send external incident communications autonomously
- ❌ 在没有日志的情况下"凭借经验"给修复建议 / Suggest fixes "from experience" without logs

---

## 复盘（Post-Mortem）/ Post-Mortem

任何 P0 / P1 故障**24 小时内**起草复盘。模板：
Any P0 / P1 incident → draft post-mortem **within 24 hours**. Template:

```markdown
# Incident Post-Mortem: <一句话故障描述>

- 发生时间 / Started: 2026-XX-XX HH:MM
- 检测到时间 / Detected: ... （什么方式检测的？客户报、监控报、还是巧合发现？）
- 缓解时间 / Mitigated: ...
- 完全恢复时间 / Resolved: ...
- 影响范围 / Impact: <影响多少客户、多少请求、估算资损 / 信任损>

## 时间线 / Timeline
HH:MM — <事件>
HH:MM — <事件>

## 根本原因 / Root Cause
<技术根因，不是表面症状>

## 5 个为什么 / 5 Whys
Why 1: ...
Why 2: ...
Why 3: ...
Why 4: ...
Why 5: ...

## 哪里做对了 / What Went Right
- 监控在 X 分钟内捕捉到 ...
- ...

## 哪里做错了 / What Went Wrong
- 监控阈值太宽，X 分钟才告警 ...
- ...

## 行动项 / Action Items
- [ ] 工程：调整监控阈值（owner: <name>, ETA: ...）
- [ ] 流程：上线前增加 X 检查（owner: ..., ETA: ...）
- [ ] 文档：更新 runbook ...
```

复盘**不追究个人**，追究**系统**。"是某某错"的复盘是失败的复盘——下次同样情况换个人也会同样错。
Post-mortems target **systems**, not **individuals**. "It was X's fault" is a failed post-mortem — next time someone else would make the same mistake under the same system.

复盘存进 [`meetings/`](../../meetings/)。
Post-mortems live in [`meetings/`](../../meetings/).
