---
name: OpenClaw 合并映射表 / OpenClaw Merge Mapping
description: 说明 TUVE_OpenClaw 的 config 与 skill 文件如何映射进 TUVE_AI 工作区
type: permanent
retention: permanent
retention_reason: 记录这次合并的文件级映射关系，避免未来继续按“整文件夹搬运”理解
---

# OpenClaw 合并映射表

## 1. 合并原则

- **不是整目录照搬**：只吸收 `TUVE_AI` 需要的长期上下文
- **不是覆盖主规则**：公司级规则仍以 `TUVE_AI` 为主
- **不是保留真实 secrets**：配置只留下模板与字段语义
- **不是替代原始运行仓库**：原始 `TUVE_OpenClaw` 仍是运行时来源

## 2. Config 文件映射

| OpenClaw 原文件 | 并入后的落点 | 处理方式 |
|---|---|---|
| `openclaw_configs/AGENTS.md` | [`runtime_contract.md`](runtime_contract.md) | 抽取 1+3 Agent 架构、阶段职责、执行门禁 |
| `openclaw_configs/IDENTITY.md` | [`runtime_contract.md`](runtime_contract.md) | 抽取 TUVE 产品身份与角色契约 |
| `openclaw_configs/SOUL.md` | [`runtime_contract.md`](runtime_contract.md) | 抽取交互红线、生成确认纪律、skill 调用纪律 |
| `openclaw_configs/TOOLS.md` | [`skill_registry.md`](skill_registry.md) | 抽取 skill 路由与关键边界 |
| `openclaw_configs/USER.md` | [`runtime_contract.md`](runtime_contract.md) | 抽取用户画像层语义，不原样搬模板 |
| `openclaw_configs/MEMORY.md` | [`runtime_contract.md`](runtime_contract.md) | 抽取任务状态层语义，不继续以旧文件为权威 |
| `openclaw_configs/HEARTBEAT.md` | 不单独迁入 | 当前内容为空，无长期信息密度 |

## 3. Skill 文件映射

| OpenClaw 原文件夹 | 并入后的落点 | 处理方式 |
|---|---|---|
| `openclaw_skills/*/SKILL.md` | [`skill_registry.md`](skill_registry.md) | 统一整理成工作区可读索引 |
| `openclaw_skills/*/capability_manifest.json` | [`skill_registry.md`](skill_registry.md) + [`openclaw_config.template.json`](openclaw_config.template.json) | 吸收 skill 名单、默认暴露关系与元信息 |
| `openclaw_skills/*/scripts/` | 不迁入 `TUVE_AI` | 工作区保留上下文，不保留运行脚本副本 |

## 4. 系统配置映射

| OpenClaw 原文件 | 并入后的落点 | 处理方式 |
|---|---|---|
| `openclaw_system/openclaw.json` | [`openclaw_config.template.json`](openclaw_config.template.json) | 去掉真实 key/token，仅保留结构与默认 skill 列表 |

## 5. 工作流与记录映射

| 需求 | TUVE_AI 落点 |
|---|---|
| 本次合并背景与需求 | `workspace_human/prd/PRD-0004_tuve_openclaw_context_merge.md` |
| 本次讨论纪要 | `workspace_human/meetings/2026-05-14_tuve_openclaw_context_merge.md` |
| 结构决策沉淀 | `workspace_human/meetings/adr/ADR-0001_tuve_ai_primary_openclaw_context_secondary.md` |

## 6. 后续维护方式

- 要改公司级规则：回 `AI_MANUAL.md`、`principles/`、入口文件
- 要改 TUVE 运行时摘要：改本目录文档
- 要改真实 skill 契约：回 `TUVE_OpenClaw/openclaw_skills/*/SKILL.md`
- 要改真实运行配置：回 `TUVE_OpenClaw/openclaw_system/openclaw.json`
