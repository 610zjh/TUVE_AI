# meetings/

> 会议纪要、ADR、客户案例复盘与研究沉淀的统一目录。
> Unified home for meeting notes, ADRs, customer reviews, and research writeups.

---

## 一句话 / One Line

这里放**可持续引用的会议与决策记录**。和 `workspace_human/` 不同，本目录允许 AI 协助起草和整理。

---

## 子目录 / Subdirectories

- **`adr/`** —— Architecture Decision Records
- **`customer_interviews/`** —— 客户访谈纪要（脱敏）
- **`weekly_ops/`** —— 团队周复盘
- **`monthly/`** —— 月度复盘
- **`research/`** —— 市场调研报告
- **`competitor/`** —— 竞品分析
- **`customer_followups/`** —— 客户电话跟进
- **`partner/`** —— 合作伙伴沟通纪要
- **`analysis/`** —— 数据汇总分析
- **`training_feedback/`** —— 培训反馈与自学反馈

子目录可以按需新建。

---

## AI 在这里可以做什么 / What AI May Do Here

- ✅ 新建会议纪要、ADR、复盘、分析文档
- ✅ 按模板整理已有笔记，补结构和标题
- ✅ 在用户明确要求下修改 AI 起草或 AI 维护的文档
- ✅ 引用、汇总、交叉链接本目录内容

---

## AI 仍然不要做什么 / What AI Still Should Not Do

- ❌ 在没有人明确要求的情况下，静默改写已经定稿的发言记录
- ❌ 把未脱敏的客户隐私、合同、销售管线直接写进本目录
- ❌ 删除已有会议记录或 ADR

---

## 命名规则 / Naming

- ADR: `adr/ADR-NNNN_短标题.md`
- 普通会议: `YYYY-MM-DD_<topic>.md`
- 客户访谈: `customer_interviews/YYYY-MM-DD_<customer_label>.md`
- 周复盘: `weekly_ops/YYYY-Wnn.md`
- 月度复盘: `monthly/YYYY-MM.md`

---

## 起新纪要 / 新 ADR

1. 复制对应模板（见 [`templates/`](../templates/)）
2. 按命名规则放进对应子目录
3. AI 可以直接起草；涉及定稿发言记录时，由人复核后再发出或引用

---

## 关联目录 / Related

- 人写且受保护的 PRD：[`../workspace_human/prd/`](../workspace_human/prd/)
- 日常轻量交接：[`../handoffs/`](../handoffs/)
- 真实样例：[`../case_studies/`](../case_studies/)
