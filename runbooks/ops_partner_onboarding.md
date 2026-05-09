---
last_executed: 2026-04-15
last_reviewed: 2026-04-01
review_cadence: quarterly
owner: ops-lead
retention: permanent
retention_reason: 关键运营流程，按 ADR-0023/24/25 重构后的标准流程
---

# 合作伙伴入驻 / Partner Onboarding Runbook

> 用于：新合作伙伴从签意向到第一次合作落地的完整 4 阶段流程。
> Use case: new partner from intent-signed to first joint delivery.

按 [`case_studies/partner_onboarding_revamp_2026Q1/`](../case_studies/partner_onboarding_revamp_2026Q1/) 的 ADR-0023/24/25 流程。

---

## 前置条件

- [ ] 销售已确认伙伴意向（书面 / 邮件 / 微信明确表态）
- [ ] 在工单系统创建了"伙伴入驻 - <伙伴名>"工单
- [ ] 销售判断了伙伴分级（核心 / 战略 / 长尾），按 ADR-0023

---

## 4 阶段 / 4 Phases

### 阶段 1：销售签意向 → 销售 owner（≤ 5 工作日）

- 销售：发出标准伙伴介绍 PPT（[`templates/customer_brief/`](../templates/customer_brief/) 改一份）
- 销售：协调 1 次双方深度对齐会（含我方法务 + 伙伴方法务）
- 销售：会后 24 小时内出会议纪要（[`templates/meeting_notes/`](../templates/meeting_notes/)）

完成判定：纪要存档 + 工单状态推到"阶段 2"

### 阶段 2：合同签订 → 法务 + 运营 co-owner（≤ 5 工作日）

- 法务：根据伙伴分级（ADR-0023）选合同模板（ADR-0024 的 3 套）
- 法务：标注哪些条款可小幅修订
- 运营：协调签字流程（电子签 / 实体签）
- **任一方法务要求超 5 工作日的合同条款 → 立刻找运营 lead 升级**

完成判定：双方电子签 / 邮件确认完成 + 合同入档

### 阶段 3：技术 / 商务 onboarding → 运营 owner（≤ 5 工作日）

- 运营：发"伙伴技术接入指南"（按伙伴分级）
- 运营：协调 1 次技术对接会（伙伴方技术 + 我方对应职能）
- 运营：开伙伴方系统账号（按权限模型）
- 运营：第一次试用数据 / 试运行（如适用）

完成判定：伙伴方能在我们系统里完成自己的第一个测试用例

### 阶段 4：第一次合作落地 → 客户成功 owner（≤ 5 工作日）

- 客户成功：和伙伴方对接人开 1 次"上路同步会"
- 客户成功：协调第一次真实合作（如：第一次给伙伴客户的服务）
- 客户成功：上线后 24 小时内确认无重大问题
- 客户成功：邀请伙伴填一份"入驻体验"问卷

完成判定：第一次合作真实落地 + 问卷填完

**总目标 / Total goal**：≤ 20 工作日 = 4 周

---

## 各阶段超时处理

任何阶段超 5 工作日：
- owner 在工单里写"超时原因 + 预计完成时间"
- @ 运营 lead（不是事后说，是当前一刻）
- 决定：(a) 等 / (b) 升级 / (c) 终止合作

---

## 红线提醒

- 合同条款 / 价格 / 收入分成 → 法务必须过审，不许销售自行答应
- 客户面材料（伙伴对外宣传我们时用的）→ 红线 #2 三道闸
- 伙伴的客户数据 → 红线 #3 脱敏后才能出 NDA 之外
- 任何"额外 SLA / 特殊条款"承诺 → 落字成 ADR

---

## 完成后

- 工单状态推到"已入驻"
- 在 [`workspace_human/meetings/partner/`](../workspace_human/meetings/) 存"<伙伴名> 入驻完成总结"
- 客户成功开始正常的伙伴维护节奏（月度同步会等）
