# AGENTS.md · Codex / OpenAI 系工具入口文件 / Codex Entry File

> 内容与 [`CLAUDE.md`](CLAUDE.md) 一致。Codex 及多数 OpenAI 系工具会自动读取这份文件。
> Identical content to [`CLAUDE.md`](CLAUDE.md). Codex and most OpenAI-family tools auto-load this file.

如果你的工具同时识别两份文件，以 `AGENTS.md` 优先。
If your tool recognizes both, `AGENTS.md` takes precedence.

---

## 立即动作 / Immediate Actions

1. **读完 [`AI_MANUAL.md`](AI_MANUAL.md)**
2. **读完 [`principles/000_CORE_RED_LINES.md`](principles/000_CORE_RED_LINES.md)**
3. **扫一眼 [`issues/known.md`](issues/known.md)**
4. **扫一眼 [`workspace_human/prd/`](workspace_human/prd/)**
5. **等用户任务，在此之前不动文件**

---

## 至高原则 / Supreme Principle

**长期主义 · 业界标准 · 核心目标。**
**Long-term · Industry standards · Core objective.**

红线沉默时回到这条。
Fall back here when red lines are silent.

---

## 15 条红线速查 / 15 Red Lines

完整列表见 [`principles/000_CORE_RED_LINES.md`](principles/000_CORE_RED_LINES.md)。
Full list: [`principles/000_CORE_RED_LINES.md`](principles/000_CORE_RED_LINES.md).

1. 至高原则 / Supreme principle
2. 客户面无内部信息 / No internal info in customer-facing copy
3. 保密数据脱敏 / Redact confidential data
4. Bug 单一登记本 / Issue SSOT
5. 改代码先有 PRD / PRD before code
6. 决策落字 / Decisions written down
7. 单文件 ≤ 800 行 / File ≤ 800 lines
8. 不可逆动作必须确认 / Irreversible actions need confirmation
9. 命名永久化 / Names are forever
10. 收尾五件套 / Five-part closeout
11. 长 Markdown 声明 retention / Long Markdown declares retention
12. `workspace_human/` 只读 / Read-only
13. 修 Bug 清反向断言测试 / Clean reverse-assertion tests
14. 线上故障先看日志 / Logs first on incident
15. 产品价值在前商业包装在后 / Product before paywall

---

## Codex 特性提示 / Codex Specifics

- 命令行批量任务可用 `codex run -- <task>`，但生产数据操作仍需 #8 确认
  Batch CLI tasks via `codex run -- <task>`, but production data ops still need confirmation per #8
- shell 脚本生成时优先 POSIX 兼容（macOS / Linux 同事都跑得起来）
  Prefer POSIX-compatible shell so both macOS and Linux teammates can run
- 长任务用 `--background` 选项，不要在前台 sleep
  Use `--background` for long tasks, no foreground sleep

---

## 完整入口表见 [`CLAUDE.md`](CLAUDE.md) 同名段落 / Full sections mirror those in [`CLAUDE.md`](CLAUDE.md)
