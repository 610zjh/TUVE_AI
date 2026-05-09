# handoffs/inbox/_raw/ · 未脱敏暂存

> ⚠️ **此目录已被 `.gitignore` 忽略。任何未脱敏内容只可临时存放，处理完必须本地移走。**

---

## 用途

接收同事 / 客户原文（截图、PDF、邮件转发、未处理的语音转文字），不做加工，先落盘。

## 必须遵守

- **不入 git**：`.gitignore` 已配置，但请勿手动 `git add -f` 强制添加
- **本地清理**：处理完（提取要点 + 脱敏 → 已写入 `../*.md`）后，**立即**把这里的原文删除或移到仓库外
- **绝不分享**：`_raw/` 内容仅在你本机；不发 Slack / 邮件 / 截图给他人

## 红线 #3 保密数据脱敏

详见 [`principles/000_CORE_RED_LINES.md`](../../../principles/000_CORE_RED_LINES.md) §#3 + [`principles/subs/confidentiality.md`](../../../principles/subs/confidentiality.md)。

未脱敏数据进入 AI 上下文 = 违反红线 #3。即使在本目录"暂存"也算违反——`_raw/` 是**本地暂存**，不是"AI 可读暂存"。让 AI 读 `_raw/` 内容前必须先脱敏。
