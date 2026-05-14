---
name: TUVE OpenClaw 运行时上下文包 / TUVE OpenClaw Runtime Context Pack
description: 将 TUVE_OpenClaw 的 config 与 skill 语义并入 TUVE_AI 的长期工作底座，但不覆盖 TUVE_AI 的总规则
type: permanent
retention: permanent
retention_reason: TUVE Agent 运行时上下文、skill 边界和配置模板的长期入口；供 AI 与维护者读取
---

# TUVE OpenClaw 运行时上下文包

> 这一组文件的目标不是“把 `TUVE_OpenClaw` 整仓搬进来”，而是把其中对 `TUVE` 运行时真正有价值的 config / skill 上下文，整理成 `TUVE_AI` 可长期复用、可导航、可被 AI 读取的知识层。

## 主从关系

1. **`TUVE_AI` 规则优先**。
   - 公司级红线、保密、PRD/ADR/meeting 规范，以 `TUVE_AI` 为唯一主规则。
2. **`OpenClaw` 只作为 TUVE 运行时上下文补充**。
   - 主要提供 Agent 角色契约、skill 能力边界、配置结构、调用纪律。
3. **真实 secrets 不并入本仓库**。
   - 这里只保留配置结构、字段语义和占位符，不保留真实 token / API key。
4. **Skill 的运行时权威仍是原始 `SKILL.md`**。
   - 本目录做的是工作区可读摘要，不替代原 skill 的最终执行契约。

## 这组文件包含什么

| 文件 | 用途 |
|---|---|
| [`runtime_contract.md`](runtime_contract.md) | 汇总 OpenClaw 中对 TUVE 有效的 Agent 身份、状态层、确认门禁与技能调用纪律 |
| [`skill_registry.md`](skill_registry.md) | 把 `openclaw_skills/` 的可用技能整理成工作区可读的路由清单 |
| [`openclaw_config.template.json`](openclaw_config.template.json) | 从 `openclaw.json` 抽出的脱敏配置模板，只保留结构与占位符 |
| [`source_mapping.md`](source_mapping.md) | 说明原始 `openclaw_configs/` 与 `openclaw_skills/` 各文件如何映射进本工作区 |

## 适用场景

- 维护 TUVE 的 Agent 行为、skill 边界、配置结构
- 在 `TUVE_AI` 里写 TUVE 相关 PRD、meeting、ADR 时补充运行时上下文
- 让 AI 在处理 TUVE 任务时，先遵守 `TUVE_AI` 总规则，再读取 TUVE 的产品级上下文

## 不适用场景

- 直接替代 `TUVE_OpenClaw` 作为运行仓库
- 存放真实线上 secrets
- 代替原始 `SKILL.md` 做最终能力承诺
- 代替 SEE2AI 平台侧未并入本仓库的内置 skill 文档

## 原始来源

- Config 来源：`/Users/zhongjiaheng/Desktop/work/TUVE_OpenClaw/openclaw_configs`
- Skill 来源：`/Users/zhongjiaheng/Desktop/work/TUVE_OpenClaw/openclaw_skills`
- 脱敏配置来源：`/Users/zhongjiaheng/Desktop/work/TUVE_OpenClaw/openclaw_system/openclaw.json`

## 建议读取顺序

1. 先读 [`../../../AI_MANUAL.md`](../../../AI_MANUAL.md)
2. 再读 [`runtime_contract.md`](runtime_contract.md)
3. 然后按任务需要看 [`skill_registry.md`](skill_registry.md) 或 [`openclaw_config.template.json`](openclaw_config.template.json)
4. 需要追根溯源时，再看 [`source_mapping.md`](source_mapping.md) 和原始仓库文件
