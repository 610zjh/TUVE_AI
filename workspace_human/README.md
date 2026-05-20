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
- ❌ 删除任何文件 / Delete any file
- ❌ 在没人显式授权的情况下追加任何段 / Append anything without explicit authorization

授权的样子（合法）/ Legitimate authorization:
> "请在 `workspace_human/prd/PRD-0042_*.md` 末尾追加一段 `## 实施记录`，写下你今天完成的事。"

不算授权（违规）/ Not authorization:
> "你随便看着办" → 不允许修改

---

## 命名规则 / Naming

- PRD: `PRD-NNNN_短标题.md`
- COMPACT 提案: `COMPACT-NNNN_<目标文件简述>.md`

---

## 当前状态 / Current State

```
workspace_human/
├── README.md       ← 你正在看
└── prd/            ← 你的真实 PRD 放这里（开工时新建）
```

如果你（团队）从这份仓库起步：
- `prd/` 暂时是空的，从你下一个真实需求开始往里写

如果你想看真实样例长什么样，去 [`case_studies/`](../case_studies/) 看 3 份完整案例。

---

## 找"会议纪要区"？/ Looking for the Meeting Zone?

→ [`../meetings/`](../meetings/)

会议纪要、ADR、研究沉淀已迁到仓库根目录的 `meetings/`，方便 AI 协助起草与整理；`workspace_human/` 只保留受保护的人写 PRD 与原始资料。

---

## 找"同事日常交接区"？/ Looking for the Daily Handoff Zone?

→ [`../handoffs/`](../handoffs/)

不在本目录的原因：outbox 一侧含 AI 协助产物，AI 必须可写，与本目录"AI 只读"语义（红线 #12）冲突。详见 [`prd/PRD-0003_daily_handoff_zone.md`](prd/PRD-0003_daily_handoff_zone.md) §1.4。
