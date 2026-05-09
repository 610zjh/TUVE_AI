# workspace_human/meetings/

> 会议纪要、ADR、客户案例复盘的存放位置。AI 只读。
> Meeting notes, ADRs, customer case reviews. AI read-only.

---

## 子目录

- **`adr/`** —— Architecture Decision Records（公司级决策）
- **`customer_interviews/`** —— 客户访谈纪要（脱敏）
- **`weekly_ops/`** —— 团队周复盘
- **`monthly/`** —— 月度复盘
- **`research/`** —— 市场调研报告
- **`competitor/`** —— 竞品分析
- **`customer_followups/`** —— 客户电话跟进
- **`partner/`** —— 合作伙伴沟通纪要
- **`analysis/`** —— 数据汇总分析

子目录可以按需新建。

---

## 命名规则

- ADR: `adr/ADR-NNNN_短标题.md`
- 普通会议: `YYYY-MM-DD_<topic>.md`
- 客户访谈: `customer_interviews/YYYY-MM-DD_<customer_label>.md`
- 周复盘: `weekly_ops/YYYY-Wnn.md`（ISO 周编号）
- 月度复盘: `monthly/YYYY-MM.md`

---

## 起新纪要 / 新 ADR

1. 复制对应模板（见 [`templates/`](../../templates/)）
2. 按命名规则放进对应子目录
3. AI 可以辅助起草，但你保存 + 定稿

---

## 当前状态

空。从你下次会议 / ADR 起开始填。

真实样例见 [`case_studies/`](../../case_studies/) 中的 3 份案例。
