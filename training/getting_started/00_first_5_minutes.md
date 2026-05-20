# 00 · 第一个 5 分钟 / Your First 5 Minutes

> 不分角色。让 AI 认识仓库 + 学会一句通用开场白。
> Universal. Make AI recognize the repo + learn a universal opening line.

---

## §1 让 AI 认识这个仓库 / Make AI Recognize This Repo

把整个 `TUVE_AI/` 文件夹拖进你的 AI 工具（Claude Code / Cursor / Codex / Trae）的工作目录。四个入口文件 [`CLAUDE.md`](../../CLAUDE.md) / [`AGENTS.md`](../../AGENTS.md) / [`.cursorrules`](../../.cursorrules) / [`CODEX.md`](../../CODEX.md) 已经预先写好——AI 启动时会自动读，不用你手动喂。

详细工具配置：[`README.md` §"5 分钟快速开始"](../../README.md)。

---

## §2 通用开场白（任何角色都能用）/ Universal Opening Line

复制下面整段，把 `<...>` 处替换成你今天的实际情况：

```
请先读 AI_MANUAL.md 和 principles/000_CORE_RED_LINES.md。
我的角色：<销售 / 产品 / 开发 / ...>，今天要做：<具体一句话>。
我希望你：1) 给我一个实施草图，2) 列出你还不确定的点（不许硬填），3) 涉及客户面文案 / 真实数据时主动告诉我红线 #2 / #3 是否被触发。

Read AI_MANUAL.md and principles/000_CORE_RED_LINES.md first.
My role: <sales / PM / dev / ...>; today's task: <one sentence>.
I want you to: 1) draft a sketch, 2) list unknowns (no guessing), 3) flag whenever rules #2/#3 are at risk.
```

> 通用开场白只解决"冷启动"。**真正贴你角色的开场白**在 [`README.md`](README.md) 路径表里你那份角色文件的 §2。
> The universal line only handles cold-start. Your **role-specific opening line** lives in §2 of your role file.

---

## §3 你接下来去哪 / Where to Go Next

1. 找你的角色文件 → [`README.md`](README.md) 的 14 角色路径表
2. 用角色文件 §2 的逐字脚本作为今天和 AI 的第一句
3. 用角色文件 §3 推荐的工作流和模板做今天的第一件事
4. 卡了 → [`common_obstacles.md`](common_obstacles.md)
5. 学完想深入 → [`what_next.md`](what_next.md)

---

## §4 三件事不要做 / Three Things Not to Do

1. **不要把"未脱敏的真实客户名 / 合同金额 / 真实手机号 / 内部代号"贴给 AI**——红线 #3。
2. **不要让 AI 在客户面文案里写内部 PRD 编号 / 模型 ID / 内部岗位代号**——红线 #2。
3. **不要让 AI 直接改 [`workspace_human/`](../../workspace_human/) 下的任何文件**——红线 #12，那是人写 PRD 和受保护原始资料的只读区。
