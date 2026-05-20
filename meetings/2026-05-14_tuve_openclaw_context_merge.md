---
type: archive
retention: permanent
retention_reason: 记录 TUVE OpenClaw 上下文并入 TUVE_AI 的讨论结论、边界和行动项
---

# 会议纪要 / Meeting Notes — TUVE OpenClaw 上下文合并

- **时间 / Date**: 2026-05-14（异步整理）
- **时长 / Duration**: 30 分钟
- **形式 / Format**: 远程
- **主持 / Chair**: Zhong Jiaheng
- **参会人 / Attendees**: Zhong Jiaheng，AI 协作助手
- **缺席（影响决策的）/ Absent (decision-relevant)**: 无
- **录音 / Recording**: 否

---

## 议程 / Agenda

1. 明确“合并”到底意味着什么
2. 确认主规则与补充上下文的边界
3. 确认 secrets、meeting、PRD 与导航文件的处理方式

---

## 议题 1: 合并目标不是简单搬文件夹

### 背景 / Context

`TUVE_AI` 是工作流和规则底座，`TUVE_OpenClaw` 则提供 TUVE 在 OpenClaw 下的运行时 config 和 skill 上下文。用户明确说明“合并”不等于直接把两个目录并排放在一起。

### 讨论要点 / Discussion

- Zhong Jiaheng: 需要把 OpenClaw 的上下文带进 `TUVE_AI`，否则 AI 在工作流仓库里看不到 skill 和 config 的真实边界
- AI 协作助手: 如果直接整目录搬运，会让 `TUVE_AI` 的总规则和 OpenClaw 的产品规则发生层级混淆
- 结论趋向: 采用“知识底座整合”，而不是“运行目录并入”

### 决议 / Decision

- 决议：把 `openclaw_configs` 与 `openclaw_skills` 提炼成 `TUVE_AI` 内的 TUVE 运行时上下文包
- 决议人：Zhong Jiaheng
- 反对 / 沉默 / 保留：无

### 行动项 / Action Items

- [ ] 新建 `products/tuve/openclaw_context/`
- [ ] 在其中整理运行时契约、skill 清单、配置模板和映射表

---

## 议题 2: 主次关系与保密边界

### 背景 / Context

两边都有规则文件，但用户明确要求以 `TUVE_AI` 为主，只把 OpenClaw 中对 TUVE 运行时有价值的上下文带入。

### 讨论要点 / Discussion

- Zhong Jiaheng: 以 `TUVE_AI` 为主，OpenClaw 只是补充上下文
- AI 协作助手: `openclaw.json` 里有真实 key/token，不应该原样迁入工作区
- Zhong Jiaheng: 配置只保留占位符和结构，不带真实 secrets

### 决议 / Decision

- 决议：公司级规则、红线、PRD/meeting/ADR 规范继续以 `TUVE_AI` 为唯一主规则
- 决议：OpenClaw 配置仅以脱敏模板形式并入
- 决议人：Zhong Jiaheng
- 反对 / 沉默 / 保留：无

### 行动项 / Action Items

- [ ] 把 `openclaw.json` 脱敏成模板文件
- [ ] 在文档中明确“最终 skill 边界仍以原始 `SKILL.md` 为准”

---

## 议题 3: 本次需要同时留下 meeting、PRD 与导航变更

### 背景 / Context

本次不是单次临时整理，而是仓库结构层面的长期调整，需要被后续维护者理解与复用。

### 讨论要点 / Discussion

- Zhong Jiaheng: 需要改 `README.md`、`AI_MANUAL.md` 和入口文件
- AI 协作助手: 这类非平凡结构决策还应落字成 ADR
- Zhong Jiaheng: 明确授权写 `meetings/` 和 `workspace_human/prd/`

### 决议 / Decision

- 决议：新增一份 PRD、一份 meeting note，并补一份 ADR
- 决议：把 TUVE 运行时上下文入口接入主导航与工具入口文件
- 决议人：Zhong Jiaheng
- 反对 / 沉默 / 保留：无

### 行动项 / Action Items

- [ ] 新增 `PRD-0004_tuve_openclaw_context_merge.md`
- [ ] 新增 `adr/ADR-0001_tuve_ai_primary_openclaw_context_secondary.md`
- [ ] 更新 `README.md`、`AI_MANUAL.md`、`AGENTS.md`、`CLAUDE.md`、`CODEX.md`、`.cursorrules`

---

## 未决 / 悬挂 / Open Items

- 后续是否还需要把 `TUVE_OpenClaw` 旧版本目录中的历史 skill 一并做归档映射，待下一轮整理决定

---

## 行动项汇总 / Action Items Summary

| # | 谁 / Who | 做什么 / What | 何时 / By When | 状态 / Status |
|---|---|---|---|---|
| 1 | AI 协作助手 | 建立 `openclaw_context/` 上下文包 | 2026-05-14 | 完成 |
| 2 | AI 协作助手 | 新增 PRD / meeting / ADR | 2026-05-14 | 进行中 |
| 3 | AI 协作助手 | 更新导航与入口文件 | 2026-05-14 | 进行中 |

---

## 下次会议 / Next Meeting

- 时间：待定
- 主题：TUVE 运行时上下文的第二轮补齐范围
- 议程候选：是否补历史 skill、是否增加 SEE2AI 内置 skill 的外链索引

---

## 附：关联 / Related

- 关联 PRD: `workspace_human/prd/PRD-0004_tuve_openclaw_context_merge.md`
- 关联 ADR: `meetings/adr/ADR-0001_tuve_ai_primary_openclaw_context_secondary.md`
