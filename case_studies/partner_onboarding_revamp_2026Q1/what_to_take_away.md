---
name: Top-5 教训
retention: permanent
retention_reason: 5 分钟带走的精华
---

# Top-5 教训

---

## 1. 跨部门项目的时间估算 = 问关键路径部门，不是发起人估

我们以为法务 2 周能审完，实际 4 周。延误的根因是没问法务自己当前容量。

**操作**：跨部门项目开工时**直接和关键路径部门对**——"你们当前 2 周内能审 N 份合同吗？" 不要假设。

---

## 2. ADR 锁住跨部门讨论结果，防止 3 个月后被翻案

W6 财务说"我以为还可以谈"——指向 ADR-0024 立刻终结讨论。
如果当时只是口头共识，大概率会再讨论 2 周。

**操作**：每次跨部门会议达成的非平凡决议立刻落字成 ADR / 写到 PRD"决策"段。

---

## 3. 流程改造的"立刻见效"特征 = 让"卡在哪"可见

ADR-0025 的工单系统不是新功能，是**让现有流程的卡点透明化**。透明化本身就是巨大价值。

**操作**：流程改造类项目的关键 KPI 不仅是"周期变短"，还有"卡点可见"。

---

## 4. 标准化材料先做"覆盖 80% 的最小版本" + 附录扩展

第一份合同模板试图"100% 覆盖"做到 38 页 → 法务审到一半建议拆成"核心 + 附录"。

**操作**：模板 / runbook / 检查清单的第一版**故意不完美**——覆盖 80% 然后随业务进化。追求 100% 第一版会过度设计 + 上线慢。

---

## 5. 试点客户的"被重视感" = 反馈质量

第一家伙伴我们提前告知"您是第一家走新流程的"——他们给了我们最详细的反馈。
如果我们没告知，他们会假设"反正都是这样"，反馈会潦草。

**操作**：流程 / 产品改版的"第一批客户"主动告知 + 索取反馈 + 透明回应。试点客户 = 共建合作伙伴，不是普通客户。

---

## 这份案例和案例 1 的对比 / Contrast with Case 1

| 维度 | 案例 1（dashboard）| 案例 2（onboarding）|
|---|---|---|
| 主导职能 | 产品 | 运营 |
| 主要载体 | PRD | ADR 集合 |
| 时长 | 6 周 | 8 周（延 2 周）|
| 跨部门 | 设计 + 工程 | 销售 + 法务 + 客户成功 |
| 关键纪律 | 五件套 + 红线 #2 | ADR + 跨部门时间估算 |

→ 不是所有项目都用 PRD。流程改造类项目用 ADR 集合更合身。

---

## 红线 / 工作流引用清单

- 红线 #6（决策落字 ADR）
- 红线 #15（不为收费而限——本案是流程改造，不涉及但可对照）
- [`workflows/decision_records/how_to_write_an_adr.md`](../../workflows/decision_records/how_to_write_an_adr.md)
- [`workflows/decision_records/when_to_record_a_decision.md`](../../workflows/decision_records/when_to_record_a_decision.md)
- [`workflows/operations/ops_runbook_authoring.md`](../../workflows/operations/ops_runbook_authoring.md)
- [`workflows/customer_communication/partner_communications.md`](../../workflows/customer_communication/partner_communications.md)
