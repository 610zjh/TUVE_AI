# training/

> 内部培训《如何高效用 AI 完成工作》全部材料。
> Full materials for the internal "Effectively Using AI to Get Work Done" training.

---

## 这是什么 / What This Is

2026 年 TUZHAN 内部培训的全部教材。会议分两部分：

- **第一部分**（全员场，约 90 分钟）：所有人参加；讲方法论 + 通用工作流
- **第二部分**（开发场，约 90 分钟）：开发参加；讲工程纪律 + 代码现场演示

非开发同事第一部分结束后可以离开，开发同事两场都参加。

---

## 为什么把培训材料放进仓库 / Why Training Materials Are in This Repo

让没参加培训的同事 / 之后入职的同事 / 想复习的同事**都能找到**。
So attendees who forget, people who couldn't attend, and future hires can all find this.

**这不是要给参会者看的"演示版本"——这就是真实培训材料的一份归档。**
**This is not a "demo version" for attendees — this IS the archived training material.**

---

## 目录结构 / Structure

```
training/
├── README.md                       ← 你正在看
├── CONFERENCE_RUNSHEET.md          ← 当日跑场单（一页 facilitator reference）
├── part_1_for_everyone/            ← 第一部分（全员场，~90 分钟）
│   ├── 01_opening_and_motivation.md
│   ├── 02_core_principles.md
│   ├── 03_workflow_walkthrough.md
│   ├── 04_hands_on_exercise.md
│   └── 05_qa_and_wrap.md
├── part_2_for_developers/          ← 第二部分（开发场，~90 分钟）
│   ├── 01_engineering_track_intro.md
│   ├── 02_prd_to_code_demo.md
│   ├── 03_bug_to_fix_demo.md
│   ├── 04_deployment_and_red_lines.md
│   └── 05_qa_and_wrap.md
├── live_demo_walkthrough/          ← 现场演示的逐步脚本
│   ├── 01_pre_flight_checklist.md
│   ├── 02_demo_script_keystroke_level.md
│   └── 03_recovery_if_things_break.md
├── speaker_notes/                  ← 演讲者笔记
│   ├── timing_and_pacing.md
│   ├── anticipated_questions.md
│   └── what_not_to_reveal.md
└── post_conference/                ← 会后参考
    ├── self_study_path_for_attendees.md
    └── feedback_collection.md
```

---

## 适合谁读什么 / Who Reads What

| 读者 / Reader | 推荐 / Recommended |
|---|---|
| 参加培训的同事 | 现场参与即可，培训材料作为**复习参考** |
| 错过培训的同事 | 按 [`part_1_for_everyone/`](part_1_for_everyone/) 顺序自学（约 1.5 小时） |
| 想给团队讲一遍的同事 | 先看 [`CONFERENCE_RUNSHEET.md`](CONFERENCE_RUNSHEET.md) 的总跑场单，再细读 [`live_demo_walkthrough/`](live_demo_walkthrough/) + [`speaker_notes/`](speaker_notes/) |
| 想搭自己公司的 AI 培训 | 整个 `training/` 目录可以二次复用 |

---

## 培训和仓库其他部分的关系 / Relationship to the Rest of the Repo

培训只是**入口**。完整方法论在仓库其他位置：

| 培训中提到的概念 | 完整内容在 |
|---|---|
| "至高决策原则" | [`principles/000_CORE_RED_LINES.md`](../principles/000_CORE_RED_LINES.md) Chapter 0 |
| "15 条红线" | [`principles/000_CORE_RED_LINES.md`](../principles/000_CORE_RED_LINES.md) Chapter 1 |
| "AI 协作的 6 件事检查清单" | [`workflows/ai_basics/how_to_give_clear_instructions.md`](../workflows/ai_basics/how_to_give_clear_instructions.md) |
| "PRD 五件套收尾" | [`principles/subs/prd_and_requirements.md`](../principles/subs/prd_and_requirements.md) |
| "Bug 单一登记本" | [`workflows/engineering/bug_tracking_ssot.md`](../workflows/engineering/bug_tracking_ssot.md) |
| "8 种 AI 失败模式" | [`workflows/ai_basics/common_failure_modes.md`](../workflows/ai_basics/common_failure_modes.md) |
| "PRD-XXXX 怎么写" | [`workflows/planning/writing_a_prd.md`](../workflows/planning/writing_a_prd.md) + [`templates/prd/`](../templates/prd/) |
| "客户简报生成器现场演示" | [`projects/customer_brief_generator/`](../projects/customer_brief_generator/) |
| "三份真实案例" | [`case_studies/`](../case_studies/) |

---

## 维护 / Maintenance

每年举办新一届培训时：
- 不要删旧版本——把旧版按年归档（`training/2026/` / `training/2027/`）
- 培训材料 retention class = `permanent`（永久保留作为历史档案）
- 如果某场培训发现新的洞察 → 反向更新 [`workflows/`](../workflows/) 和 [`principles/`](../principles/)，让仓库本身受益
