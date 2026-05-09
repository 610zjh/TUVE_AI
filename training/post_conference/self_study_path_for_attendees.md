---
name: 培训后的自学路径
retention: permanent
retention_reason: 让没参加培训 / 想复习的同事都有清晰起点
---

# 培训后的自学路径 / Self-Study Path for Attendees

> 给参加过培训想复习的，和**没参加**想自学的两类同事。
> For attendees revisiting and non-attendees self-studying.

---

## 选你的预算

### 如果你只有 1 小时 / 1-Hour Path

按这个顺序：

1. **[`AI_MANUAL.md`](../../AI_MANUAL.md)** —— 5 分钟，把仓库地图记在心里
2. **[`principles/000_CORE_RED_LINES.md`](../../principles/000_CORE_RED_LINES.md)** —— 15 分钟，过一遍 15 条红线
3. **[`workflows/ai_basics/how_to_give_clear_instructions.md`](../../workflows/ai_basics/how_to_give_clear_instructions.md)** —— 10 分钟，6 件事检查清单
4. **[`workflows/ai_basics/common_failure_modes.md`](../../workflows/ai_basics/common_failure_modes.md)** —— 15 分钟，8 种失败模式
5. **挑一份和你角色最相关的工作流** —— 15 分钟，例：
   - 销售/客户成功 → [`workflows/customer_communication/sales_call_followup.md`](../../workflows/customer_communication/sales_call_followup.md)
   - 运营 → [`workflows/operations/weekly_ops_review.md`](../../workflows/operations/weekly_ops_review.md)
   - 视频 → [`workflows/content_creation/video_script_drafting.md`](../../workflows/content_creation/video_script_drafting.md)
   - 产品 → [`workflows/planning/writing_a_prd.md`](../../workflows/planning/writing_a_prd.md)
   - 开发 → [`workflows/engineering/prd_to_implementation.md`](../../workflows/engineering/prd_to_implementation.md)

---

### 如果你有 1 天 / 1-Day Path

加上：

6. **整组 [`workflows/ai_basics/`](../../workflows/ai_basics/)** —— 5 个文件，约 30 分钟
7. **整组你角色相关的 workflows/** —— 4-6 个文件，约 1.5 小时
8. **挑一份案例读完** —— [`case_studies/creator_dashboard_redesign_2026Q1/`](../../case_studies/creator_dashboard_redesign_2026Q1/)（建议第一份，最完整）—— 30 分钟
9. **跑一次客户简报生成器** —— [`projects/customer_brief_generator/`](../../projects/customer_brief_generator/) —— 30 分钟实操
10. **从 [`templates/`](../../templates/) 挑一个最贴近你下周工作的模板** —— 复制 + 试用 —— 30 分钟

---

### 如果你有 1 周（每天 1 小时） / 1-Week Path

加上：

第 1 天（昨天）：1 小时路径
第 2 天：所有 [`workflows/ai_basics/`](../../workflows/ai_basics/)
第 3 天：3 份 [`case_studies/`](../../case_studies/) 全读完
第 4 天：你角色相关的 [`workflows/`](../../workflows/) 全读完
第 5 天：[`projects/customer_brief_generator/`](../../projects/customer_brief_generator/) 完整跑一遍 + 看 PRD-0001 + 看测试代码
第 6 天：[`principles/subs/`](../../principles/subs/) 12 份子原则全读完（约 2 小时但有些可跳）
第 7 天：复习 + 写一份你**自己工作的** PRD（用 [`templates/prd/`](../../templates/prd/)），保存到 [`workspace_human/prd/`](../../workspace_human/prd/)

---

## 学完之后做什么 / After You Finish

### 自我检验（30 分钟测验）

回答下列问题（不必写下来，心里答即可）：

1. 列出 4 组红线分类（外部沟通 / 写下来 / 质量底线 / 业务方向）和每组里的 3-4 条红线
2. 6 件事检查清单（背景 / 目标 / 边界 / 材料 / 形式 / 不确定）
3. 8 种 AI 失败模式中，你最容易犯哪 3 种？为什么？
4. 五件套收尾是哪 5 件？
5. 红线 #14 的具体内容（线上故障第 1 个动作 = ？）
6. workspace_human/ 是谁的？AI 在那能做什么？
7. ADR 和 PRD 的边界（PRD 答"做什么"；ADR 答"为什么这么选"）
8. 主次审视什么时候必填？

每答对一道 +1 分，8 分及格。

---

### 真实应用 / Real Application

**第二周**：选你常做的一类工作（写邮件 / 整理数据 / 起草文档）—— 严格按方法论做 5 次。
**第三周**：写一份你自己的"我的提示模板"放进 [`templates/`](../../templates/)。
**第四周**：发现你工作中**这套方法论没覆盖**的场景 → 起 PRD 提议加新工作流。

---

## 团队成长路径 / Team Growth Path

如果你是团队 lead，让全团队成长：

**第 1 个月**：要求全员读完 1 小时路径
**第 2 个月**：每周一次"AI 协作小分享"——每位成员分享一个他用方法论的真实场景
**第 3 个月**：团队选 1-2 条"我们最容易违反"的红线，建立 CI / lint 自动检查
**第 4 个月**：基于团队真实使用，反向贡献 [`workflows/`](../../workflows/) 改进

---

## 卡住了怎么办 / If You're Stuck

### 找不到对应的工作流

[`AI_MANUAL.md`](../../AI_MANUAL.md) §4 任务-入口表会告诉你。

如果还是找不到 → 这件事在我们工作流体系里**没有**对应——可以是：
- 这件事还不在我们公司核心流程里 → 自然跳过
- 这件事**应该**有但我们漏了 → 起一份 PRD 提议加

### AI 给我的输出违反红线

按红线说的做：
- 红线 #2 违规 → 三道闸（grep / 品牌声音 / 法务）
- 红线 #14 没看日志 → 立刻 SSH 拉日志
- 红线 #5 没 PRD → 先停下，回去补 PRD

---

## 反馈 / Feedback

学习过程中遇到的问题、看不懂的段、写得不好的部分，发给培训发起方（联系方式由当时培训提供）或者直接在 [`workspace_human/meetings/`](../../workspace_human/meetings/) 起一份"自学反馈"。

让仓库随真实使用进化。
