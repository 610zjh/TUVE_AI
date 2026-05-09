---
name: 案例 2 - 合作伙伴入驻流程重构（2026 Q1）
description: 运营主导，跨销售 / 法务 / 客户成功 / Operations-led, cross sales / legal / CS
type: permanent
retention: permanent
retention_reason: 展示运营主导、决策记录密集型项目
---

# 案例 2: 合作伙伴入驻流程重构（2026 Q1）

> Partner Onboarding Revamp — 2026 Q1

- **主导职能**：运营
- **跨到的职能**：销售（识别合作伙伴）、法务（合同模板）、客户成功（入驻后跟进）
- **持续时间**：8 周
- **关联 ADR**：ADR-0023, ADR-0024, ADR-0025
- **状态**：已上线 + 第一批 4 家伙伴已走完新流程

---

## 一句话故事 / One-Liner

我们的合作伙伴入驻流程之前是"邮件来回 6-8 周 + 每位伙伴的合同条款都不一样"。我们重构成"标准化分级 + 模板合同 + 4 周入驻"。这件事好的部分：用 ADR 把跨部门讨论结果落字，避免了"会上达成共识，落地时各做各的"。坏的部分：一开始低估了法务审核合同模板的时间，时间表延误了 2 周。

We rebuilt the partner onboarding flow from "6-8 weeks of email back-and-forth with custom contracts per partner" to "tiered + template-based + 4-week onboarding". What went right: ADRs preserved cross-team agreements. What went wrong: underestimated legal review time on contract templates; 2-week slip.

---

## 文件 / Files

1. [`01_initial_brief.md`](01_initial_brief.md) — 重构的触发原因
2. [`02_prd_or_decision.md`](02_prd_or_decision.md) — 三份关键 ADR
3. [`03_implementation.md`](03_implementation.md) — 8 周落地过程
4. [`04_outcome.md`](04_outcome.md) — 第一批 4 家伙伴的反馈
5. [`what_to_take_away.md`](what_to_take_away.md) — Top-5 教训

---

## 为什么挑这份案例 / Why This Case

- **运营主导**而非工程主导：让非开发角色看到"这套方法论也适用于流程类项目"
- **ADR 密集**：8 周里产生了 3 份 ADR，是决策记录纪律的好示范
- **跨法务**：展示和法务这种"慢节奏 + 合规优先"的职能怎么协作
- **真实失误**：时间表延误的部分是真实教训
