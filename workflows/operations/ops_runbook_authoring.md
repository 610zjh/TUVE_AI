# 运营手册 / Runbook 编写 / Authoring Operations Runbooks

> 适用：运营、客户成功、IT、财务、HR 在把"反复做的事"标准化时。
> For: ops / CS / IT / finance / HR standardizing recurring procedures.

---

## 一句话 / One Line

**Runbook 不是给"现在的你"写的，是给"凌晨 2 点临时上手的同事"写的。** 假设读者一无所知。
**A runbook is not for "today-you"; it's for "the colleague picking it up at 2 AM cold".** Assume the reader knows nothing.

---

## 一份好 Runbook 的 8 个标准 / 8 Standards

1. **目标**：这个 runbook 解决什么问题？什么时候用 / 不用 / Purpose: when to use / not use
2. **前置条件**：开始之前需要什么权限 / 工具 / 数据 / Preconditions: what access / tools / data
3. **步骤**：每步有动词 + 对象 + 验证方式 / Steps: verb + object + verification
4. **决策点**：明确写"如果 A 发生，去步骤 X；如果 B，去步骤 Y" / Decision points
5. **常见失败 + 对策**：top-3 失败模式和怎么处理 / Top-3 failure modes
6. **谁来做 + 多久一次**：负责人 + 频率 + 上次执行时间 / Owner + cadence + last run
7. **完成验证**：怎么知道真的做完了 / How to verify done
8. **回退方案**：如果做错了怎么撤销 / Rollback plan

模板见 [`templates/`](../../templates/) 下"runbook" 子目录（如有）。
Template at `templates/` runbook subdirectory if available.

---

## 用 AI 协助起草的 4 步 / 4 Steps with AI

### 步 1：从你"目前怎么做"开始 / Step 1: Start from "How I Do It Today"

```
我每月要做一件事：[一句话描述]。
我目前的做法是：[把你脑子里的步骤说出来，从开始到结束]
（讲流水账没关系，一步都不要省略）

请帮我把这段流水账整理成 runbook 格式：
- 目标：...
- 前置条件：...
- 步骤 1, 2, 3 ...
- 决策点 ...
- 完成验证 ...
- 回退方案 ...

如果某些信息我没说但 runbook 需要，请列出 top-5 你需要补的问题。
```

### 步 2：自查"凌晨 2 点测试" / Step 2: 2-AM Test

```
对你刚才整理的 runbook，自查：

假设读者是凌晨 2 点临时上手的同事，对这件事一无所知：
1. 步骤 X 他能不能照做下来？哪一步缺背景？
2. 决策点 Y 他能不能判断？需要补什么经验值？
3. 验证段他能不能确认"做完了"？需要补什么具体检查？
4. 失败时他能不能自救？还是必须升级？给个升级判断标准。

把发现的问题列出来 + 给修补建议。
```

### 步 3：补"反例" / Step 3: Add Anti-Examples

很多 runbook 缺一段"看起来在做对但其实做错了"的反例。
Many runbooks lack a "looks right but actually wrong" anti-example section.

```
基于上面的步骤，列出 top-3 "看起来对但其实是错的" 反例：
- 反例 1：[读者可能误以为完成了，但其实漏掉了什么]
- 反例 2 ...
- 反例 3 ...

每个反例附"如何识别 / 如何修正"。
```

### 步 4：试跑 + 校准 / Step 4: Dry Run

让另一位**没参与**起草的同事，按 runbook 执行一遍。
Have a **non-author** colleague execute the runbook.

观察：
Observe:
- 哪一步他犹豫了？/ Where did they hesitate?
- 哪些验证他跳过了？/ Which checks did they skip?
- 哪些决策点他选错了？/ Which decisions did they get wrong?

按观察修订 runbook。
Revise based on observations.

试跑通过 → 入库到 [`runbooks/`](../../runbooks/)。
Dry run passes → save to [`runbooks/`](../../runbooks/).

---

## Runbook 的命名 / Naming

```
runbooks/<owner_team>_<verb>_<object>.md

例子：
- runbooks/sales_lead_handoff.md
- runbooks/ops_partner_onboarding.md
- runbooks/engineering_emergency_rollback.md
- runbooks/finance_monthly_close.md
```

文件名让"是哪个团队、做什么动作、对哪个对象"一眼可见。
Filename reveals "which team, what action, on what object" at a glance.

---

## Runbook 的"过期"管理 / Expiry Management

每份 runbook 顶部加：
Each runbook starts with:

```yaml
---
last_executed: 2026-04-23  # 上次实际跑的时间
last_reviewed: 2026-03-10  # 上次审阅的时间
review_cadence: quarterly   # 多久审一次
owner: ops-Z               # 责任人
---
```

如果 `last_executed` 超过 review_cadence 期限 → 自动列入"过期 / 待审"清单。
If `last_executed` exceeds the cadence → auto-flagged for review.

过期 runbook 不删（红线 #11 反熵），但要标 `Status: Stale`，并且**任何人按这份执行前必须重新审一遍**。
Stale runbooks aren't deleted (Red Line #11), but marked `Status: Stale`. **Anyone executing must re-review first**.

---

## Runbook 的"AI 辅助跑"与"AI 自跑"边界 / AI-Assisted vs AI-Autonomous

| 步骤 / Step type | AI 辅助 / AI-assisted | AI 自跑 / AI autonomous |
|---|---|---|
| 数据查询 / Data query | ✅ | ✅（只读）|
| 文档生成 / Doc generation | ✅ | ⚠️（人审过模板后）|
| 通知 / 邮件 / Notify / email | ✅（起草）| ❌（红线 #8）|
| 修改生产数据 / Modify prod data | ✅（人逐步确认）| ❌ |
| 部署 / Deploy | ✅（人确认）| ❌ |
| 退款 / 转账 / Refund / transfer | ✅（人确认）| ❌ |

不可逆动作 = 永远人确认，无论 runbook 多熟。
Irreversible actions = always human-confirm, no matter how routine.

---

## 速查 / Cheat Sheet

```
8 标准：目标 / 前置 / 步骤 / 决策点 / 失败 / 谁做多久 / 验证 / 回退

4 步：从流水账开始 → 凌晨 2 点测试 → 加反例 → 试跑校准

命名：<team>_<verb>_<object>.md

过期管理：last_executed + review_cadence；过期标 Stale 不删

不要：把"我自己懂就行"的隐含步骤跳过；让 AI 自跑不可逆动作
```
