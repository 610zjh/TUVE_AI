---
name: Top-5 教训 / Top-5 Takeaways
retention: permanent
retention_reason: 这份案例最浓缩的版本，新人 5 分钟读完就能拿走最核心的部分
---

# Top-5 教训 / Top-5 Takeaways

> 5 分钟读完。把这份案例的精华浓缩成 5 条带走。
> 5 minutes. The 5 lessons to take away.

---

## 1. 开工前列不确定问题 = 节省后续 1-2 周返工

工程 lead 在 W1 没急着写代码，先列了 7 个澄清问题让产品答。
这一天 vs 后期"猜错→重做"的代价 = 几小时 vs 几周。

**操作**：参考 [`prd_to_implementation.md`](../../workflows/engineering/prd_to_implementation.md) "开工前必走"段。

---

## 2. 风险段的"对策"必须真的提前执行

PRD §8 写的"性能负载测试提前做"——这不是"备选方案"，是"提前到 W2 真去做"。
真去做了 → 抓到 P95 不达标 → 改架构 → 上线后 P95 优于目标。

**操作**：写 PRD 风险段时不要"会评估""会监控"，写"什么时候做什么具体动作"。

---

## 3. 客户原型在"PRD 没限定的灵活段"做校准

PRD §2 没限定具体哪 7 个数字（产品给了"可调"的余地）。我们在 W3 让真实客户看 Figma → 客户立刻指出我们漏了一个核心数字。
如果 PRD 写死了，客户就没机会校准。

**操作**：PRD 里有意保留"灵活段"——让客户和实际场景在实施过程中校准。

---

## 4. 客户面文案永远 grep 一遍，不靠"应该没漏吧"的感觉

工程同事的发布说明初稿里有"PRD-0042 / 下个迭代"——红线 #2 双重违规。
靠 grep 闸抓住了。

**操作**：[`workflows/content_creation/marketing_copy_workflow.md`](../../workflows/content_creation/marketing_copy_workflow.md) 三道闸（关键词 grep / 品牌声音 / 法务）每次必过。

---

## 5. 顺手重构 = 范围漂移 + rollback 风险 + PRD 没登记

工程 lead 顺手重构了相邻"通知 API" → 评审时被退回，拆 PR。

为什么不允许：
- 范围扩大让 review 更难
- rollback dashboard 时通知会被连带回滚到旧形态
- 重构没在任何 PRD 里登记 → 6 个月后没人知道为什么改

**操作**：看到旁边代码"明显能改进"，写到 [`issues/known.md`](../../issues/known.md) 或下次 PRD，**不要在当前 PR 里顺手做**。

---

## 一张图速查 / One-Glance

```
开工前：列澄清问题      ← 省后期返工
风险段：写"提前做的动作" ← 不是"备选方案"
PRD 灵活段：留校准空间   ← 让客户能调
客户面文案：必 grep      ← 不靠感觉
不要顺手重构            ← 拆 PR
```

---

## 这份案例的红线 / 工作流 引用清单

读这份案例时引用的：
- 红线 #2（客户面文案）
- 红线 #5（PRD 在前）
- 红线 #6（决策落字 ADR）
- 红线 #10（收尾五件套）
- 红线 #15（主次审视——本次自愿做）
- [`workflows/research_and_analysis/customer_interview_synthesis.md`](../../workflows/research_and_analysis/customer_interview_synthesis.md)
- [`workflows/engineering/prd_to_implementation.md`](../../workflows/engineering/prd_to_implementation.md)
- [`workflows/engineering/code_review_with_ai.md`](../../workflows/engineering/code_review_with_ai.md)
- [`workflows/content_creation/marketing_copy_workflow.md`](../../workflows/content_creation/marketing_copy_workflow.md)
- [`workflows/engineering/deployment_hygiene.md`](../../workflows/engineering/deployment_hygiene.md)

读完案例后回头扫这些工作流，会发现"原来这些规矩在真实工作里这样用"。
