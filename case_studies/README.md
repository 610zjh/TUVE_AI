# case_studies/

> 三份**跨职能**的工作案例。这些不是"假想例子"，是按真实工作节奏写的，让你看到**红线 + 工作流 + 模板**怎么在一个完整任务里串起来。
> Three **cross-functional** case studies. Not "made-up examples"; written in real-work cadence, showing how **red lines + workflows + templates** chain through a complete task.

---

## 三份案例 / Three Case Studies

| # | 案例 / Case | 主导职能 / Lead Function | 跨到的职能 / Cross to | 涉及的红线 / Workflows |
|---|---|---|---|---|
| 1 | [`creator_dashboard_redesign_2026Q1/`](creator_dashboard_redesign_2026Q1/) | 产品 | 设计 / 工程 / 销售 | PRD / ADR / 五件套 / 反熵 |
| 2 | [`partner_onboarding_revamp_2026Q1/`](partner_onboarding_revamp_2026Q1/) | 运营 | 销售 / 法务 / 客户成功 | 决策记录 / 客户简报 / 会议纪要 |
| 3 | [`outreach_template_overhaul_2026Q1/`](outreach_template_overhaul_2026Q1/) | 销售 | 营销 / 短视频 / 数据 | 市场调研 / A/B / 内容质量 |

---

## 怎么用 / How to Use

1. **作为新员工**：按顺序读 3 份，了解 TUZHAN 的工作节奏 / As new hires: read all 3 in order
2. **作为某职能新手**：先读和你职能最相关的一份 / Per-function newbie: read the most-relevant
3. **作为方法论参考**：写自己的 PRD / ADR 时回头翻案例 / As reference: revisit when writing your own PRD/ADR

---

## 替换为你团队的真实案例 / Replace with Your Team's Real Cases

如果你（合作伙伴）把这份仓库拿去自用，**这三份案例可以替换成你团队的真实案例**——本质上是"案例库"，越是真实越有教学价值。
If you're adopting this repo, **replace these with your team's real cases** — the more real, the more instructive.

替换时纪律：
Discipline when replacing:
- 案例必须**已结束**（已上线 / 已收尾），不要把进行中的项目当案例 / Use **completed** projects, not in-flight
- 客户名 / 真实数字 / 内部代号按红线 #2 + #3 脱敏 / Redact per red lines
- 保留教学价值的"做错过的地方"——这些比"看起来完美的案例"更值钱 / Keep the "what we got wrong" — more instructive than perfection

---

## 维护 / Maintenance

- 每年 Q4 添加 1-2 份当年最有教学价值的真实案例 / Each Q4, add 1-2 real cases
- 老案例不删，可标 `Status: Archived (still useful for teaching)` / Old cases archived, not deleted
- 案例 retention class = `permanent`（教学价值长期有效）/ retention = permanent

---

## 案例的统一结构 / Unified Case Structure

每份案例文件夹下：
Each case folder contains:

```
<case_name>/
├── README.md                  ← 案例总览（背景 / 难点 / 收尾）
├── 01_initial_brief.md        ← 最初的需求是什么样的
├── 02_prd_or_decision.md      ← 中间的 PRD / ADR
├── 03_implementation.md       ← 落地过程（做对的 + 做错的）
├── 04_outcome.md              ← 上线后的结果 / 复盘
└── what_to_take_away.md       ← 这份案例的 top-5 教训
```
