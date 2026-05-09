---
name: 合作伙伴沟通 / Partner Communications
retention: permanent
retention_reason: 跨职能合作伙伴沟通工作流，长期复用 / Cross-functional partner-comm workflow, reused long-term
---

# 合作伙伴沟通 / Partner Communications

> 适用：销售、产品、运营、法务在和合作伙伴（渠道、供应商、技术合作）沟通时。
> For: communication with channel partners, suppliers, tech partners (sales / product / ops / legal).

---

## 一句话 / One Line

**合作伙伴不是客户。** 信任建立比客户慢，但一旦建立，价值远高。
**Partners aren't customers.** Trust takes longer but once built, value is far higher.

合作伙伴对你的"专业 / 守规矩 / 落字" 的期待比客户高。
Partners expect more "professionalism / process / written records" than customers.

---

## 4 类合作伙伴沟通 / 4 Types

| 类型 / Type | 沟通频率 / Cadence | 主要文档 / Key docs |
|---|---|---|
| 渠道分销 / Channel | 月度同步 | 月度业绩对账 / 季度规划 |
| 供应商 / Supplier | 按需 + 季度评估 | SLA / SOW / 月度交付报告 |
| 技术合作 / Tech | 双周同步 | API / 接口契约 / 集成路线 |
| 战略联盟 / Strategic | 季度 + 重大事件 | 联合 GTM 计划 / 联名材料 |

---

## 通用结构（任何沟通材料）/ Universal Structure

```markdown
# [合作主题] - 合作伙伴沟通 - YYYY-MM-DD

- 我方负责：[name]
- 合作伙伴方负责：[name]
- 沟通主题：[一句话]
- 沟通方式：会议 / 邮件 / 文档审阅
- 文档版本：v0.X

## 上次进展回顾
- ...

## 本次议题 / 决议候选
- ...

## 决议 / 待决
- 已决议：...
- 待决：...

## 行动项
- 我方：[谁 / 什么 / 何时]
- 伙伴方：[谁 / 什么 / 何时]
- 双方共担：[谁 / 什么 / 何时]

## 风险 / 阻碍
- ...

## 下次同步：YYYY-MM-DD HH:MM
```

存到 [`workspace_human/meetings/partner/`](../../workspace_human/meetings/) 下。
Save under `workspace_human/meetings/partner/`.

---

## 用 AI 协助的 3 步 / 3 Steps with AI

### 步 1：起会前简报 / Step 1: Pre-Meeting Brief

```
我下周二要和 [合作伙伴名称] 开 [类型] 会议。
- 上次进展：[粘贴或路径]
- 本次议题：[3-5 个]
- 我方目标：[本次会议希望达成的具体决议]

请帮我准备：
1. 每个议题的背景一句话提要
2. 每个议题的"决议候选"（2-3 个选项 + 优劣）
3. 对方可能挑战的 top-5 问题 + 我的回应草稿
4. 时间分配建议
```

### 步 2：会后纪要 / Step 2: Post-Meeting Minutes

```
基于这次会议（录音 / 笔记）：[粘贴]

请整理成会议纪要，重点：
- 客观记录"谁说了什么"，不修饰口语化
- 决议必须明确（如果是"再看看"，写"未决，下周二再议"，不要包装成"达成共识"）
- 行动项必须有"谁 / 什么 / 何时"，缺一不可
- 暴露给伙伴方的版本可能要再过一次"敏感信息"过滤

约束：
- 不出现 [我方内部代号 / PRD 编号 / 销售管线 / 内部财务]
- 数字 / 承诺必须基于会议实际讨论
```

### 步 3：起对外沟通材料 / Step 3: External Communication

```
基于上面的纪要，起一份发给合作伙伴的沟通材料（邮件或简报）：

约束：
- 简短（≤ 500 字邮件 / ≤ 1 页简报）
- 重点在"我们达成的共识 + 双方接下来的事"
- 客观，不带强烈情绪 / 暗示压力
- 不暴露我们内部的考虑 / 备选方案

我会审核后发出。
```

---

## 红线在合作伙伴沟通中的特别提醒 / Red Lines in Partner Comms

### 红线 #2：内部信息

合作伙伴**也不应**看到我们的内部代号 / PRD 编号 / 销售管线明细。
Partners **should not** see our internal codes / PRD numbers / pipeline detail.

例外：明确签了 NDA 的战略合作 + 信息分级清楚的（"这一类信息可以共享，那一类不行"）。
Exceptions: NDA signed + classified info-sharing agreed.

### 红线 #3：客户数据

**绝对**不向合作伙伴透露我们客户的具体数据，除非：
**Never** share our customers' data with partners unless:
- 客户明确同意 / Customer explicitly consents
- 走签 DPA 的数据处理协议 / Via DPA data-processing agreement
- 数据已脱敏 / Data redacted

### 红线 #6：合作伙伴决策落字成 ADR

任何"非平凡"合作决策（年度合作合同、收入分成调整、终止合作）都要落字成 ADR 存到 [`workspace_human/meetings/`](../../workspace_human/meetings/)。
Any non-trivial partner decision (annual contract, revenue split, termination) → ADR in `workspace_human/meetings/`.

### 红线 #8：发送任何对外文档前必须人确认

合作伙伴沟通文档 **不能** AI 自动发送 —— 哪怕是"按模板的常规进度报告"。
AI **never** auto-sends partner comms — even routine progress reports per template.

---

## 合作伙伴沟通的常见错误 / Common Mistakes

### 错误 1：信息单向 / One-Way Info

❌ 我们提供大量信息 / 价值，但伙伴方对我们透明度低。
**问题**：长期不平衡的关系不可持续。
**修正**：协议初期就明确双向信息要求。

### 错误 2：情绪化 / Emotional

❌ 伙伴方延误了交付 → 邮件语气强硬。
**问题**：情绪化在合作伙伴沟通中代价大（信任 + 法律风险）。
**修正**：让 AI 帮你写一版"中性 + 客观陈述事实 + 提议下一步" 版本。

### 错误 3：跨级沟通失序 / Cross-Level Disorder

❌ 我们 A 直接联系伙伴方 B，跳过了双方约定的对接人。
**问题**：破坏对方内部秩序 + 让对方觉得不被尊重。
**修正**：尊重 designated point of contact，跨级沟通需要双方同意。

### 错误 4：口头承诺没记 / Verbal Promise No Record

❌ 会议中口头说"我们这周给"，没写进纪要，到时间没做。
**问题**：信任崩塌的最常见模式。
**修正**：所有口头承诺 24 小时内写到纪要里 + 邮件确认。

### 错误 5：过度披露未来 / Over-Disclosing Future

❌ "我们正在做的 [新功能 / 新产品 / 新合作] 是 ..."
**问题**：(1) 未发布的可能黄 (2) 信息扩散后竞争对手知道 (3) 引起伙伴方"等一下我再决定"
**修正**：合作伙伴沟通里**只说已发布**的能力，未来计划只说大方向。

---

## 合作伙伴关系的"信任阶梯" / Partner Trust Ladder

```
阶梯 1：交易信任 / Transactional trust
- 按合同执行；按时付款 / 交付
- 沟通：基于合同事项

阶梯 2：流程信任 / Process trust
- 双方流程无缝对接
- 沟通：双方流程小调整

阶梯 3：战略信任 / Strategic trust
- 共担风险 / 共享上行
- 沟通：可以聊未来 / 可以提困难

阶梯 4：联盟级 / Alliance
- 联合 GTM / 联合产品 / 资本互持
- 沟通：高频 / 多层 / 战略级
```

不要用阶梯 1 的语气和阶梯 3 的伙伴沟通——会显得疏远。
Don't use Tier-1 tone with a Tier-3 partner — feels distant.

不要用阶梯 3 的开放度和阶梯 1 的伙伴沟通——会显得轻率。
Don't use Tier-3 openness with Tier-1 — feels reckless.

---

## 速查 / Cheat Sheet

```
4 类伙伴：渠道 / 供应 / 技术 / 战略
通用结构：上次进展 / 本次议题 / 决议 / 行动项 / 风险 / 下次

3 步法：会前简报 → 会后纪要 → 对外材料

红线：内部信息分级 / 客户数据脱敏 / 非平凡决策 ADR / 对外发送必人审

陷阱：信息单向 / 情绪化 / 跨级 / 口头承诺没记 / 过度披露未来
```
