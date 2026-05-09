# 客户电话 / 拜访跟进 / Sales Call Followup

> 适用：销售、客户成功、产品在和客户沟通后整理跟进材料。
> For: sales / CS / product after customer calls or visits.

---

## 一句话 / One Line

**电话结束后 24 小时内的动作决定 80% 的成单 / 续费。** AI 帮你把整理时间从 60 分钟降到 15 分钟。
**The 24h after a call drives 80% of close / renewal.** AI cuts post-call ops from 60 min to 15.

---

## 电话当天 4 步法 / 4-Step Same-Day Process

### 步 1：电话进行中（手写要点）/ Step 1: During the Call (Hand Notes)

不要在电话中盯着电脑打字——客户能听出你在分心。
Don't type during a call — customer can hear distraction.

手写记录 4 类信息：
Hand-write 4 categories:
- **客户原话**（关键的几句，加引号）/ Direct quotes
- **客户的"为什么"**（他们关心的根因）/ The "why" behind concerns
- **客户的具体反对 / 担心** / Specific objections / concerns
- **下一步双方约定** / Mutual next steps

### 步 2：电话后 30 分钟内（趁记忆鲜活）/ Step 2: Within 30 min (Memory Fresh)

把手写笔记数字化。先写客观纪要（事实），不夹杂判断。
Digitize. Objective minutes first; no judgment yet.

```markdown
# 客户跟进 - YYYY-MM-DD HH:MM

- 客户：[已脱敏 / 仅内部用真名取决于场景]
- 沟通方式：电话 / 视频 / 现场
- 时长：N 分钟
- 我方参与：[姓名]
- 客户方参与：[角色，可脱敏成"采购负责人/CTO"]

## 客户原话
- "..."
- "..."

## 客户主动表达的关注点
- ...

## 客户的反对 / 担心
- ...

## 双方约定的下一步
- 我们：[具体动作 + 截止]
- 客户：[具体动作 + 截止]
```

### 步 3：用 AI 帮你做 3 类输出 / Step 3: AI Generates 3 Outputs

#### 输出 A：给客户的跟进邮件 / Output A: Followup Email to Customer

```
基于上面的纪要，起一份给客户的跟进邮件：

约束：
- 简短（200 字内）
- 三段式：感谢上次会议 / 确认下一步 / 联系方式
- 不出现 PRD 编号 / 内部代号 / 其他客户名（红线 #2）
- 不夸大上次会议中没承诺的事
- 不催促得太紧（如果下一步是客户先做）
- 客户的原话可以在适当地方引用，让他感受到"被听到"

输出后我审核再发。
```

#### 输出 B：给内部的客户简报 / Output B: Internal Customer Brief

```
基于上面的纪要，起一份给内部团队（产品 / 客户成功 / 销售总）的简报：

包含：
- 客户当前状态（兴趣度 / 阶段）
- 客户最关心的 top-3 问题
- 客户最大的反对 / 顾虑
- 我们承诺给客户的动作（含截止）
- 我建议的下一步（不止"再约一次"）
- 这个客户的"特殊性"（行业 / 规模 / 决策链）

不会发给客户，仅内部用。可以用具体客户名 / 内部代号。
```

存到 [`workspace_human/meetings/customer_followups/`](../../workspace_human/meetings/) 下。
Save under `workspace_human/meetings/customer_followups/`.

#### 输出 C：CRM / 客户管理系统的更新 / Output C: CRM Update

```
基于上面的纪要，给我一份可以直接粘到 CRM 的更新：

- 阶段：[字段]
- 下次跟进时间：[日期]
- 此次会议总结：[≤ 100 字]
- 风险标签：[如有]
- 决策链：[如新发现的]
```

### 步 4：人审 + 发送 / Step 4: Human Review + Send

AI 给的三类输出**都要人审**：
All 3 outputs need human review:

- 邮件给客户前：再过红线 #2 三道闸
- 内部简报：判断段是不是合理（不要 AI 替你下结论）
- CRM 更新：字段是不是按你公司的 CRM 字段标准

---

## 反复跟进的客户 / Recurring Customers

如果一位客户已经跟进 ≥ 3 次：
For customers tracked ≥ 3 times:

```
请把这位客户的所有历次跟进纪要（粘贴）汇总：

1. 时间线：每次接触的核心进展
2. 客户态度变化：从首次到最近的演变
3. 反复出现的关注点 vs 已解决的关注点
4. 当前阻碍成单 / 续费的 top-3 因素
5. 我下一步最有效的 1 个动作（不要给"继续保持沟通"这种空话）
```

让 AI 把"零散的纪要"提炼成"客户决策画像"。
Let AI distill scattered notes into a "customer decision profile".

---

## 红线提醒 / Red Line Reminders

### 红线 #2：客户面邮件

发给客户的邮件**禁止**：
- PRD 编号 / Bug 编号
- 模型 endpoint / 内部 API 名
- 其他客户名 / 案例数字
- 内部岗位代号（"运维"/"红喵"/"项目经理"等）
- 内部排期措辞（"下个版本""上线后")

### 红线 #3：内部简报里的客户数据

内部简报可以提客户名 / 行业 / 规模，但**不要**把客户的合同金额 / 销售管线明细放进 AI 上下文（除非脱敏到只有量级）。
Internal briefs can name customers / industry / size, but don't put exact contract amounts / detailed pipeline into AI context unredacted.

### 红线 #8：发邮件前必须人确认

AI 起草的邮件**不能直接发**。人审过再发。
AI-drafted email **never auto-sends**. Human reviews before send.

---

## 速查 / Cheat Sheet

```
电话中：手写 4 类信息（原话 / 为什么 / 反对 / 下一步）
30 分钟内：数字化客观纪要
然后 AI 起 3 类输出：客户邮件 / 内部简报 / CRM 更新
人审过 → 发送 / 入库

不要：在电话中打字（客户能感觉到分心）
不要：让 AI 自动发邮件（红线 #8）
要：纪要 24h 内出，跟进 48h 内启动
```
