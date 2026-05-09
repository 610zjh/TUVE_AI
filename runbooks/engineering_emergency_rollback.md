---
last_executed: 2026-01-15
last_reviewed: 2026-04-01
review_cadence: quarterly
owner: engineering-lead
retention: permanent
retention_reason: 关键应急流程
---

# 紧急回滚 / Emergency Rollback Runbook

> 用于：生产环境出问题，需要在 5-15 分钟内回滚到上一稳定版本。
> Use case: production incident; need to rollback to last stable in 5-15 min.

---

## 触发条件

满足以下任一：
- P0 故障（全产品停摆 / 数据丢失 / 安全 / 资损）
- P1 故障且无法在 30 分钟内 forward fix
- 监控指标突然恶化超过阈值

---

## 前置条件

- [ ] 你有生产 SSH / 部署系统访问权限
- [ ] 你确认了"是上一次部署引起"的（红线 #14：先看日志）
- [ ] 你已通知工程负责人（语音或群组）

---

## 步骤

### 1. 确认要回滚到哪个版本（30 秒）

```bash
# 查看最近 5 个生产部署版本
git log --oneline production-tag~5..production-tag
```

记下当前版本（要回滚的）+ 上一稳定版本（目标）。

### 2. 通知销售 / 客户成功（不要等回滚完成才通知）

群组消息模板：

> [紧急] 生产正在执行回滚。预计 5-10 分钟内完成。客户感知：[简短描述]。完成后我会再通知。

### 3. 执行回滚

```bash
# 例子（按你公司的部署系统填）
./deploy.sh production rollback --to=<target-version-sha>
```

⚠️ 回滚命令不接 `--force`、不接 `-y`，让它正常进交互确认。

### 4. 等回滚完成（约 2-5 分钟）

部署日志显示"rollback complete" 或类似。

### 5. 验证

- [ ] 监控指标是否恢复（错误率 / 延迟）
- [ ] 关键业务路径手测（首页 / 核心 API）
- [ ] 客户成功 / 客服反馈是否平息

### 6. 通知

群组消息模板：

> 回滚已完成。当前回到版本 [target-version-sha]。监控指标已恢复 / 仍在恢复中。下一步：[forward fix 计划]。

### 7. 立刻在 issues/known.md 登记

包括：
- 触发原因（什么 commit / 什么动作引起）
- 当前状态（已回滚到 X 版本）
- 下一步根本修复计划

---

## 完成验证

- [ ] 监控指标恢复正常（连续 15 分钟无新告警）
- [ ] 客户成功 / 客服无新增相关投诉
- [ ] 在 issues/known.md 登记完毕
- [ ] 通知了所有相关方

---

## 常见失败

### 失败 1：回滚后数据库迁移不兼容

如果上一次部署含 DB migration，回滚代码可能和当前 DB schema 不兼容。

**对策**：
- 先回滚代码（让客户先有可用功能）
- 然后单独跑 migration 回滚 SQL（应在原 PRD 准备好的）
- 如果没有 migration 回滚 SQL → 立刻找数据库负责人

### 失败 2：回滚命令失败

可能是部署系统本身有问题。

**对策**：
- 不要重试 5 次（会让事情更糟）
- 立刻找工程负责人 + 部署平台负责人

---

## 复盘

回滚后 24 小时内**必须**写复盘到 [`workspace_human/meetings/`](../workspace_human/meetings/)。
内容：时间线 / 根因 / 行动项。

参考 [`principles/subs/deployment_and_ops.md`](../principles/subs/deployment_and_ops.md) §"复盘"。
