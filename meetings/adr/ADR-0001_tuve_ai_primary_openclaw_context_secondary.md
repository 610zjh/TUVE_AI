---
type: archive
retention: permanent
retention_reason: 记录 TUVE OpenClaw 上下文并入 TUVE_AI 时的结构决策
---

# ADR-0001: 以 TUVE_AI 为主规则，将 OpenClaw 作为 TUVE 运行时上下文包接入

- **时间 / Date**: 2026-05-14
- **决策人 / Decided by**: Zhong Jiaheng
- **状态 / Status**: Accepted

---

## 1. 背景 / Context

`TUVE_AI` 负责公司级 AI 工作方法、红线、模板和协作流程；`TUVE_OpenClaw` 则沉淀了 TUVE 在 OpenClaw 宿主中的 config、skill 契约和产品级运行时规则。

随着 TUVE 相关工作逐步回到 `TUVE_AI` 工作区内推进，出现了一个结构性问题：如果只保留 `TUVE_AI`，AI 能看到流程与原则，但看不到 TUVE 当前运行时边界；如果把 `TUVE_OpenClaw` 直接整目录并入，又会让两套规则文件并列存在，模糊“公司级主规则”和“产品级补充上下文”的层级。

因此，需要决定如何在 `TUVE_AI` 中接入 OpenClaw 的有效上下文，同时不引入 secrets 泄露风险，也不让工作区退化成第二个运行仓库。

---

## 2. 选项 / Options Considered

### 选项 A: 直接把 `openclaw_configs/` 和 `openclaw_skills/` 原样搬进 `TUVE_AI`

- 优点 / Pros:
  - 信息最完整
  - 不需要额外整理映射
- 缺点 / Cons:
  - 主次混乱，容易让 AI 把 OpenClaw 当成第二套总规则
  - 容易把真实配置结构和敏感字段一起带入
  - 长期维护成本高，形成双份目录与双份真相
- 实施成本估算：低

### 选项 B: 在 `products/tuve/` 下建立 `openclaw_context/`，只并入运行时上下文摘要与脱敏模板

- 优点 / Pros:
  - 保留 TUVE 所需的运行时语义，同时保持 `TUVE_AI` 为主规则
  - 能把 skill、config、状态层语义整理成更适合 AI 和维护者读取的知识层
  - 可避免迁入真实 secrets 和运行脚本副本
- 缺点 / Cons:
  - 需要维护“摘要”和“原始来源”的关系
  - 后续 skill 更新时需要同步更新摘要
- 实施成本估算：中

### 选项 C: 不并入，只在文档中放一个跳转到外部仓库

- 优点 / Pros:
  - 不改现有目录结构
  - 无需维护副本
- 缺点 / Cons:
  - AI 仍无法在同一工作区内稳定拿到 TUVE 上下文
  - 维护者需要跨仓库来回跳转，工作流割裂
- 实施成本估算：低

---

## 3. 决策 / Decision

我们选 **选项 B**。

### 理由 / Reasoning

1. **长期主义角度**: `TUVE_AI` 需要保持为唯一的工作方法底座，而不是逐步演变成多个运行仓库的并列集合。把 OpenClaw 作为上下文包接入，比整目录搬运更可持续。
2. **业界标准角度**: 对运行时配置与产品级约束做“脱敏模板 + 摘要索引 + 原始来源映射”，比复制粘贴整套运行文件更符合知识库治理与配置治理的常见做法。
3. **核心目标角度**: 当前核心目标不是迁移 OpenClaw 运行环境，而是让 `TUVE_AI` 在处理 TUVE 相关任务时拿到足够的 skill/config 上下文，同时继续遵守公司级红线与记录纪律。

---

## 4. 后果 / Consequences

### 正面 / Positive

- `TUVE_AI` 中的 AI 可以在同一工作区内读到 TUVE 运行时上下文
- 主规则和产品级补充上下文的层级更清楚
- secrets 不会随上下文整理进入工作区
- 后续 PRD / meeting / ADR 可以直接引用工作区内的 TUVE 上下文包

### 负面（被取舍掉的部分）/ Tradeoffs

- 需要维护摘要与原始 `SKILL.md` 的同步关系
- 新增文档会让 `products/tuve/` 从纯产品介绍扩展为“对外材料 + 内部运行时上下文”混合目录
- 未来如果 TUVE 宿主从 OpenClaw 切换，可能还需要再做一次映射调整

### 复评触发条件 / When to Re-review

- [ ] 当 TUVE 的默认 skill 列表发生明显变化时，回头评估 `skill_registry.md` 是否仍然成立
- [ ] 当 TUVE 不再以 OpenClaw 作为主要宿主时，回头评估 `openclaw_context/` 的命名与位置
- [ ] 默认每年 1 月例行复评

---

## 5. 关联 / Related

- 关联 PRD：`PRD-0004_tuve_openclaw_context_merge.md`
- 关联 Bug：无
- 推翻了 / Supersedes：无
- 被推翻 / Superseded by：无

---

## 状态变更日志 / Status History

- 2026-05-14 由 Zhong Jiaheng 起草，状态 Proposed
- 2026-05-14 状态变为 Accepted
