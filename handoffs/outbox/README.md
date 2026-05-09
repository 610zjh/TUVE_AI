# handoffs/outbox/ · 发件区

> 我交付给同事 / 下游的成品。已完成 / 待发送。

---

## 单层

不像 inbox/ 有 `_raw/` 暂存——outbox 按定义是**已脱敏的成品**。如果还没脱敏，它根本不该在这里。

---

## 三步流转

1. **写成品**：新建 `YYYY-MM-DD_<to>_<topic>.md`，AI 协助起草也可
2. **脱敏自查**（同 inbox/ README 的 5 条）+ 红线 #2 客户面口径自查（无内部 PRD-XXXX / Bug ID / 模型 ID / 内部代号 / 未公开排期）
3. **通知下游**：在 Slack / 邮件给收件人贴本文件相对路径，让对方知道在哪取

---

## AI 协助起草 outbox

AI 可以**直接写**到本目录（不像 [`workspace_human/`](../../workspace_human/) 是只读区）。但起草前请提供：
- 收件方角色（决定语气）
- 是否含敏感字段（决定是否要先走 `inbox/_raw/` 路径）
- 是否对外（客户面 → 红线 #2 收紧）

---

## 处理完之后

- 下游已确认收到、消化完毕 → 进入 30 天反熵窗口（[../README.md](../README.md)）
- 反复被引用、有长期复用价值 → 挪到 `templates/` / `runbooks/` / `case_studies/`
- 一次性、消化即弃 → 30 天后 `git rm`

详见 [`workflows/operations/handing_off_work.md`](../../workflows/operations/handing_off_work.md)。
