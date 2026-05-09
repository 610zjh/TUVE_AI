---
name: 故障响应 / Incident Response Workflow
retention: permanent
retention_reason: 线上故障第一份必读，跨职能长期复用 / First read on production incidents, cross-functional and long-lived
---

# 故障响应 / Incident Response Workflow

> 适用：所有人遇到"线上问题"时的第一份必读。
> For: anyone hitting a "production issue" — read this first.

---

## 一句话 / One Line

**故障响应的第 1 个动作 = 看真实日志。** 没看日志前 ≤ 3 轮静态猜测，超过就停。
**Action #1 in incident response = look at real logs.** Pre-log static guessing capped at 3 rounds.

这是红线 #14。
This is Red Line #14.

---

## 标准响应阶梯 / Standard Response Ladder

```
听到"线上挂了" / "Production is down"
                │
                ▼
1. 拉日志（30 秒内）/ Pull logs (within 30s)
                │
                ▼
2. 找 traceback / 异常堆栈 / Find traceback
                │
                ▼
3. 看时间线（什么时候开始的、影响多少请求）/ Timeline
                │
                ▼
4. 看是不是上一次部署后开始的 / Did it start right after the last deploy?
                │
        ┌───────┴───────┐
        ▼               ▼
       是 / Yes        否 / No
        │               │
        ▼               ▼
  rollback 或          看 traceback 定位
  forward fix          代码 / 数据 / 第三方
```

---

## 5 个角色 / 5 Roles

故障响应中的角色（一人可以兼几个，但不能没人担）：
Roles in an incident (one person can wear multiple, but none can be vacant):

| 角色 / Role | 责任 / Responsibility |
|---|---|
| **指挥 / IC (Incident Commander)** | 拍板决策、协调资源、对外沟通 |
| **技术 / Tech Lead** | 真正动手定位 + 修 |
| **沟通 / Comms** | 内部告知（销售 / 客户成功）+ 外部告知（客户）|
| **记录 / Scribe** | 实时记录时间线（每个动作 + 时间）|
| **观察 / Observer** | 监控指标 / 客户反馈，给指挥反馈 |

P0 故障：5 个角色齐 + 实时同步（语音 / Slack 群）。
P0 incidents: all 5 roles + real-time sync.
P1：3 个角色（指挥 + 技术 + 沟通）+ 30 分钟同步一次。
P1: 3 roles (IC + Tech + Comms) + 30-min sync intervals.
P2 / P3：1-2 人，按 SLA 处理即可。
P2 / P3: 1-2 people, by SLA.

---

## 故障的 5 个阶段 / 5 Phases of Incident

### 阶段 1：检测 / Detect

谁先发现？/ Who detected?
- 监控告警 → 反应最快
- 客户报 → 反应慢但是真实信号
- 内部测试 → 不算事故，是 bug

如果"客户报先于监控"——监控本身有 gap，加入 post-mortem 行动项。
If "customer reported before monitoring", monitoring has a gap → action item in post-mortem.

### 阶段 2：止损 / Mitigate

不一定要"修"，先**让症状消失**：
Not necessarily "fix"; first **make symptoms stop**:
- Rollback 上一次部署 / Rollback last deploy
- 重启服务 / 切流量 / Restart service / shift traffic
- 降级（关掉某个功能保整体可用）/ Degrade (disable one feature to keep overall up)
- 客户层面手动兜底（"请客户成功手动处理这位客户的请求"）/ Manual fallback

止损是给真正修复**买时间**，不是修复本身。
Mitigation buys time for real fix; not the fix itself.

### 阶段 3：定位 / Diagnose

红线 #14 在这里发挥：
Red Line #14 applies here:
- 第 1 个动作 = 看真实日志
- 不超过 3 轮静态猜测

```
拉日志的标准命令：
- 测试服：[填具体命令]
- 正式服：[填具体命令]

要拿到的关键信息：
- 完整 traceback
- 时间戳
- 影响请求数 / 用户数
```

### 阶段 4：修复 / Fix

修法分两类：
Two flavors:
- **Forward fix**：写新代码修，重新部署
- **Rollback**：回到上一个稳定版本

选择标准：
Decision rule:
- 上一次部署后才出现 → Rollback 优先
- 上一次部署前已经存在 → Forward fix
- 不知道 → 优先 rollback（保守）

修完后**再次确认日志正常**——不要一修完就报告"完毕"。
After fix, **re-verify logs are normal** — don't just declare "done".

### 阶段 5：复盘 / Post-Mortem

参考 [`principles/subs/deployment_and_ops.md`](../../principles/subs/deployment_and_ops.md) §"复盘 (Post-Mortem)"。

P0 / P1 故障 24 小时内必须出复盘。
P0 / P1: post-mortem within 24h.

---

## 客户沟通在故障中的纪律 / Customer Comms During Incident

### 何时通知客户 / When to Notify

| 影响 / Impact | 何时通知 / When |
|---|---|
| 全产品停机 ≥ 5 分钟 | 立即（5 分钟内）|
| 影响 ≥ 10% 客户的功能不可用 | 30 分钟内 |
| 数据延迟（不是停机）≥ 1 小时 | 1 小时内 |
| 数据丢失风险 | 立即 + 法务介入 |
| 边角功能不可用 | 24 小时内 |

### 通知模板 / Notification Templates

**第一通知**（仅说"识别到 + 在调查"）/ First notice:
> 我们识别到当前 [功能 / 区域] 存在异常，正在紧急调查。我们会在 [30 分钟] 后给您下一次更新。给您带来不便深表歉意。

**进展通知**（每 30-60 分钟）/ Progress (every 30-60 min):
> 当前调查进展：[具体动作]。预计恢复时间：[估计]。

**恢复通知** / Resolution:
> [功能 / 区域] 已经恢复。我们将在 [X 小时] 后发出完整事故报告。如您仍遇到问题，请联系 [客服]。

**事后报告** / Post-incident report (within 48-72h):
> 事故时间线 / 影响范围 / 根因 / 预防措施。客观陈述，不甩锅，不夸大。

---

## 故障响应中的常见错误 / Common Mistakes

### 错误 1：没看日志就开始猜 / Guess Before Logs

❌ 红线 #14 经典违规
**修复**：拉日志命令做成"客服 + 销售也能跑的小卡片"，不要让"看日志"成为只有工程师才会的动作。
Make log-pulling commands a card anyone can run; don't gate "look at logs" behind engineering skill.

### 错误 2：让"沟通"角色被技术挤压 / Tech Pushes Comms Aside

❌ 工程师埋头修，没人告诉销售 / 客户成功 / 客户。
**问题**：客户在体验断崖式下降时**沉默**比"持续告知"伤害更大。
**修复**：指挥角色**强制**让沟通角色每 30-60 分钟发外部告知，哪怕只有"还在调查"。

### 错误 3：没等真验证就报告"修好了" / Premature "Fixed"

❌ 发了修复 commit → 立刻报"修好了"。
**问题**：修复 commit 上线后，还要确认日志正常 / 客户反馈正常 / 监控指标恢复。
**修复**：把"恢复确认"作为一道独立的检查 → 全部通过才能报。

### 错误 4：复盘抓个人 / Post-Mortem Blames a Person

❌ "都是因为 X 没做好 Y"
**问题**：抓个人无法防止下次同样情况换个人也犯。
**修复**：抓系统性问题（流程 / 监控 / 文档 / 自动化），让"换个人也不会"。

### 错误 5：故障次数下降被当成成功 / "Fewer Incidents = Success"

❌ "本季度故障数同比降 40%"——不一定是好事，可能是：
**问题**：(1) 监控失效（没检测到的不算）(2) 不敢部署了（停滞 ≠ 安全）(3) 故障的恶劣度上升了
**修复**：除了次数，还看：MTTR（平均恢复时长）/ 客户感知 / 故障严重度分布

---

## 速查 / Cheat Sheet

```
红线 #14：第 1 动作看日志 / 不超过 3 轮静态猜测

5 角色：指挥 / 技术 / 沟通 / 记录 / 观察

5 阶段：检测 → 止损 → 定位 → 修复 → 复盘

止损 ≠ 修复（先让症状消失，再修根本）
通知 ≥ 沉默（哪怕只有"还在调查"）
确认 ≥ 报告（修复 commit 上线后还要 verify）

P0/P1 故障 24h 内必出复盘
```
