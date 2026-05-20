# handoffs/inbox/ · 收件区

> 同事 / 上游交过来的资料，待我处理。

---

## 双层

```
inbox/
├── _raw/             ← 未脱敏暂存（.gitignore，本地用，不入 git）
└── *.md（顶层）       ← 已脱敏，入 git
```

**任何含未脱敏客户数据 / 真实手机邮箱 / 合同金额的文件**——先扔 `_raw/`，处理完再进顶层。

---

## 三步流转

1. **接收原文**：把同事发来的截图 / PDF / 邮件转发 / 语音转文字扔进 `_raw/`
2. **提取 + 脱敏**：在顶层新建 `YYYY-MM-DD_<from>_<topic>.md`，写要点；客户名脱敏成"客户 A"，手机 / 邮箱 / 身份证 / 合同金额删除或替换
3. **处理完**：把 `_raw/` 里的原始文件**本地删除或移到仓库外**；顶层 `.md` 留给下游 / AI 引用

---

## 脱敏自查（入 git 前）

- [ ] 无客户公司真实名（已替换为"客户 A / Customer A"）
- [ ] 无真实手机号 / 邮箱 / 身份证号
- [ ] 无合同金额 / 报价 / 折扣
- [ ] 无内部 PRD-XXXX / Bug ID / 模型 endpoint / 内部代号（红线 #2）
- [ ] 无未公开的内部排期 / 路线图

任一未通过 → 文件名前加 `[REDACT-PENDING]_`，**禁止 git commit**。

---

## 处理完之后

- 已被下游消化 → 进入 30 天反熵窗口（[../README.md](../README.md)）
- 已成型为可复用资料 → 挪到 `templates/` / `runbooks/` / `case_studies/` / `meetings/`
- 已过时 → `git rm`

详见 [`workflows/operations/handing_off_work.md`](../../workflows/operations/handing_off_work.md)。
