# workspace_human/

> **AI 只读区**（红线 #12）。
> **AI Read-Only Zone** (Red Line #12).

---

## 一句话 / One Line

这是**人写的、人维护的、AI 不许擅自修改的**目录。
This is **human-written, human-maintained, off-limits-to-AI-edits**.

---

## 这里放什么 / What Goes Here

- **`prd/`** —— 人写的产品需求文档 / Human-written PRDs
- **`prd/compaction/`** —— `COMPACT-NNNN` 反熵压缩提案 / Anti-entropy rollup proposals
- **`meetings/`** —— 会议纪要、ADR、客户案例复盘 / Meeting notes, ADRs, customer reviews
- **`meetings/adr/`** —— Architecture Decision Records
- **`meetings/customer_interviews/`** —— 客户访谈纪要（脱敏）
- **`meetings/weekly_ops/`** —— 团队周复盘
- **`meetings/monthly/`** —— 月度复盘
- **`meetings/research/`** —— 市场调研报告
- **`meetings/competitor/`** —— 竞品分析
- **`meetings/customer_followups/`** —— 客户电话跟进
- **`meetings/partner/`** —— 合作伙伴沟通纪要
- **`meetings/analysis/`** —— 数据汇总分析

子目录可以按需新建。
Create subdirectories as needed.

---

## AI 在这下面允许做什么 / What AI May Do

- ✅ **读** —— 任何文件都可以读 / Read any file
- ✅ **引用** —— 在其他地方引用本目录的内容 / Reference content elsewhere
- ✅ **追加"实施记录"段** —— 仅在 PRD 文件**末尾**追加被人**显式授权**的"## 实施记录" 段 / Append "Implementation Log" at the **end** of a PRD with **explicit human authorization**

---

## AI 严禁做的 / What AI May NOT Do

- ❌ 修改任何已有文件的主体段 / Edit any existing file's body
- ❌ 修改 PRD 的需求段 / 验收段 / Edit PRD requirements / acceptance sections
- ❌ 修改会议纪要的发言记录 / Edit speech records
- ❌ 删除任何文件 / Delete any file
- ❌ 在没人显式授权的情况下追加任何段 / Append anything without explicit authorization

授权的样子（合法）/ Legitimate authorization:
> "请在 `workspace_human/prd/PRD-0042_*.md` 末尾追加一段 `## 实施记录`，写下你今天完成的事。"

不算授权（违规）/ Not authorization:
> "你随便看着办" → 不允许修改

---

## 命名规则 / Naming

- PRD: `PRD-NNNN_短标题.md`
- ADR: `ADR-NNNN_短标题.md`
- 会议纪要: `YYYY-MM-DD_<topic>.md`
- 客户访谈: `YYYY-MM-DD_<customer_label>.md` （客户脱敏）
- COMPACT 提案: `COMPACT-NNNN_<目标文件简述>.md`

---

## 当前状态 / Current State

```
workspace_human/
├── README.md       ← 你正在看
├── prd/            ← 你的真实 PRD 放这里（开工时新建）
└── meetings/       ← 你的真实会议纪要放这里（开会后新建）
```

如果你（团队）从这份仓库起步：
- `prd/` 暂时是空的，从你下一个真实需求开始往里写
- `meetings/` 暂时是空的，从你下次会议起开始往里写

如果你想看真实样例长什么样，去 [`case_studies/`](../case_studies/) 看 3 份完整案例。

---

## 找"同事日常交接区"？/ Looking for the Daily Handoff Zone?

→ [`../handoffs/`](../handoffs/)

不在本目录的原因：outbox 一侧含 AI 协助产物，AI 必须可写，与本目录"AI 只读"语义（红线 #12）冲突。详见 [`prd/PRD-0003_daily_handoff_zone.md`](prd/PRD-0003_daily_handoff_zone.md) §1.4。
