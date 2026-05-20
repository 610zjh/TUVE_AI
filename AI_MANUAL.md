# AI_MANUAL · AI 工作总导航

> AI 助手第一次进入这个仓库时，应该读完这份文件再问"我们今天要做什么"。
> AI assistants entering this repo should read this file end-to-end before asking "what are we working on today?"

---

## 0. 至高决策原则 / Supreme Decision Principle

> 任何决策，遵循一条原则：**长期主义 · 科学方法与业界标准 · 紧扣核心产品目标**。
> AI 在这条原则下能自决就自决；不能时，先写建议交人决策。
>
> Every decision follows one principle: **long-term thinking · scientific methods and industry standards · locked on the core product objective**.
> Under this principle, AI decides autonomously when it can; when it can't, it writes a recommendation and hands the call to a human.

完整说明 / Full text: [`principles/subs/supreme_decision_principle.md`](principles/subs/supreme_decision_principle.md)

任何具体红线对当前情境沉默或模糊时，回到这条。
When any specific red line below is silent or ambiguous on the current situation, fall back here.

---

## 1. 立即生效的红线（必读）/ Immediately-Effective Red Lines (must read)

不读完这份就开始干活 = 违反第 0 条。
Working without finishing this section = violating Rule 0.

| # | 红线 / Red Line | 详见 / See |
|---|---|---|
| 1 | 长期主义 + 业界标准 + 核心目标——上述至高原则 / Long-term + industry standard + core objective — the supreme principle above | [`principles/subs/supreme_decision_principle.md`](principles/subs/supreme_decision_principle.md) |
| 2 | 客户面文案严禁出现内部代号 / PRD 编号 / 模型 ID / 内部角色名 / Customer-facing copy NEVER exposes internal codes, PRD IDs, model IDs, internal role names | [`principles/subs/content_quality.md`](principles/subs/content_quality.md) |
| 3 | 保密数据（客户数据、合同、销售管线）不得未脱敏进入 AI 上下文 / Confidential data (customer data, contracts, sales pipeline) never enters AI context unredacted | [`principles/subs/confidentiality.md`](principles/subs/confidentiality.md) |
| 4 | Bug / 问题单一登记本（SSOT）：未修在 [`issues/known.md`](issues/known.md)，已修按日归档到 [`issues/fixed/YYYY-MM-DD.md`](issues/fixed/) / Issue tracking SSOT: unfixed in [`issues/known.md`](issues/known.md), fixed archived to [`issues/fixed/YYYY-MM-DD.md`](issues/fixed/) | [`principles/subs/bug_and_issue_tracking.md`](principles/subs/bug_and_issue_tracking.md) |
| 5 | 改代码前先有 PRD；而写 PRD 前先做 meeting / 密听 / 需求挖掘，需求没挖清前禁止直接开干；改 [`workspace_human/prd/`](workspace_human/prd/) 已写好的 PRD 是禁止的 / No code change without a PRD; and a meeting / discovery pass must happen before drafting the PRD when requirements are still unclear | [`principles/subs/prd_and_requirements.md`](principles/subs/prd_and_requirements.md) |
| 6 | 非平凡决策必须落字成 ADR / Non-trivial decisions must be written down as ADRs | [`principles/subs/decisions_and_records.md`](principles/subs/decisions_and_records.md) |
| 7 | 单文件 ≤ 800 行；超过即提压缩提案 / Single file ≤ 800 lines; over → propose a rollup | [`principles/subs/anti_entropy.md`](principles/subs/anti_entropy.md) |
| 8 | 不可逆动作（发外部消息 / 删数据 / 部署 / 退款）必须先和人确认 / Irreversible actions (sending external messages, deleting data, deploying, refunding) require human confirmation | [`principles/subs/working_with_ai.md`](principles/subs/working_with_ai.md) |
| 9 | 命名一律按"长期复用"写，禁止 demo_/sample_/placeholder_ 这类一次性命名 / Name everything as if reused long-term; banned: demo_/sample_/placeholder_ | [`principles/subs/code_quality.md`](principles/subs/code_quality.md) |
| 10 | 干完活前必须登记版本 / 状态 / 收尾，禁止"完工"字眼除非清单全齐 / Before saying "done": register version, update status, close out — banned to use "完工/done" unless checklist complete | [`principles/subs/prd_and_requirements.md`](principles/subs/prd_and_requirements.md) |
| 11 | 长 Markdown（≥ 200 行）或 dated archive 必须在 frontmatter 声明 retention class / Long Markdown (≥ 200 lines) or dated archive must declare retention class in frontmatter | [`principles/subs/anti_entropy.md`](principles/subs/anti_entropy.md) |
| 12 | [`workspace_human/`](workspace_human/) 是只读目录，AI 严禁修改（除非人明确授权） / [`workspace_human/`](workspace_human/) is AI read-only (unless explicitly authorized) | [`principles/subs/data_and_privacy.md`](principles/subs/data_and_privacy.md) |
| 13 | 修 Bug 必须同步清理"反向断言旧错误行为"的测试 / Fixing a bug requires cleaning up tests that asserted the old buggy behavior | [`principles/subs/code_quality.md`](principles/subs/code_quality.md) |
| 14 | 线上故障第 1 个动作 = 拉真实日志，禁止在没看日志前做超过 3 轮静态猜测 / On a production incident, action #1 is to pull real logs — banned to do >3 rounds of static guessing before that | [`principles/subs/deployment_and_ops.md`](principles/subs/deployment_and_ops.md) |
| 15 | 主次不可颠倒：产品价值优先于商业包装；功能未做扎实之前不引付费墙 / Product value precedes commercial packaging; never add paywalls before the underlying feature is solid | [`principles/subs/business_priorities.md`](principles/subs/business_priorities.md) |

完整红线见 [`principles/000_CORE_RED_LINES.md`](principles/000_CORE_RED_LINES.md)。
Full red lines: [`principles/000_CORE_RED_LINES.md`](principles/000_CORE_RED_LINES.md).

---

## 2. 仓库地图 / Repository Map

```
TUVE_AI/
├── AI_MANUAL.md                 ← 你正在看的这份 / this file
├── README.md                    ← 给人看的总入口 / human-facing landing page
├── principles/                  ← 红线 + 12 份子原则 / red lines + 12 sub-principles
│   ├── 000_CORE_RED_LINES.md
│   └── subs/
│       ├── supreme_decision_principle.md
│       ├── working_with_ai.md
│       ├── content_quality.md
│       ├── data_and_privacy.md
│       ├── decisions_and_records.md
│       ├── prd_and_requirements.md
│       ├── bug_and_issue_tracking.md
│       ├── code_quality.md
│       ├── deployment_and_ops.md
│       ├── anti_entropy.md
│       ├── confidentiality.md
│       └── business_priorities.md
├── workflows/                   ← 按工作类型分组的"怎么做"指南
│   ├── ai_basics/               ← 全员必读 / required for everyone
│   ├── planning/                ← 写需求、拆项目、周会
│   ├── research_and_analysis/   ← 市场 / 竞品 / 客户访谈
│   ├── content_creation/        ← 短视频脚本 / 营销文案 / PPT
│   ├── customer_communication/  ← 销售跟进 / 客户简报 / 客服
│   ├── operations/              ← 运营周会 / 事故复盘 / 供应商评估
│   ├── engineering/             ← PRD 到代码 / 代码评审 / Debug / 部署
│   └── decision_records/        ← ADR 怎么写
├── templates/                   ← 复制即用的模板（PRD / Bug / 简报 / 脚本 等）
├── case_studies/                ← 三个跨职能真实案例
├── products/                    ← 兔展旗下 SEE2AI 与 TUVE 的产品材料
│                                  Product materials for TUZHAN's SEE2AI and TUVE
│                                  其中 `products/tuve/openclaw_context/` 额外收录 TUVE 的运行时上下文包
├── handoffs/                    ← 日常工作传递区（inbox / outbox，AI 可写）
│                                  Daily handoff zone (inbox / outbox, AI-writable)
├── meetings/                    ← 会议纪要、ADR、复盘、研究沉淀（AI 可协助）
│                                  Meeting notes, ADRs, retros, research writeups (AI-assisted)
├── workspace_human/             ← 人写的 PRD 与受保护原始资料（AI 只读）
├── issues/                      ← 全公司 Bug/问题单一登记本
├── runbooks/                    ← 部署 / 客户接入 / 销售交接 等操作手册
├── projects/                    ← 实际项目（含一个完整可跑的样例）
├── training/                    ← 内部培训全部教材
├── CLAUDE.md / AGENTS.md /      ← 四种 AI 工具的入口文件（内容一致）
│   .cursorrules / CODEX.md
└── setup.sh / setup.ps1
```

---

## 3. AI 第一次进入的标准动作 / Standard First-Entry Actions for AI

按顺序：
In order:

1. 读完这份 `AI_MANUAL.md`（你正在做） / Finish reading this `AI_MANUAL.md`
2. 读 [`principles/000_CORE_RED_LINES.md`](principles/000_CORE_RED_LINES.md) / Read [`principles/000_CORE_RED_LINES.md`](principles/000_CORE_RED_LINES.md)
3. 看一眼 [`issues/known.md`](issues/known.md) 知道当前未解决的问题清单 / Glance at [`issues/known.md`](issues/known.md) to see open issues
4. 看一眼 [`workspace_human/prd/`](workspace_human/prd/) 知道当前正在做的需求 / Glance at [`workspace_human/prd/`](workspace_human/prd/) to see active PRDs
5. 如果用户的需求还在模糊阶段，先走 [`workflows/planning/meeting_prep_with_ai.md`](workflows/planning/meeting_prep_with_ai.md) 做 meeting / 密听 / 需求挖掘 / If the request is still fuzzy, start with [`workflows/planning/meeting_prep_with_ai.md`](workflows/planning/meeting_prep_with_ai.md)
6. 等用户告诉你今天的任务，或在需求已明确后再进入对应工作流 / Wait for the user's actual task, or enter the relevant workflow only after the requirement is clarified

不要在第 5 步之前自作主张改任何文件。
Do not modify any file before step 5 unless the user explicitly asked.

---

## 4. 最常见任务的入口 / Most-Common Task Entry Points

| 你今天要做的事 / What you're doing today | 从哪开始 / Start here |
|---|---|
| 需求还不清楚，需要先密听 / 开 meeting / Requirements are still unclear; need discovery first | [`workflows/planning/meeting_prep_with_ai.md`](workflows/planning/meeting_prep_with_ai.md) → [`templates/meeting_notes/`](templates/meeting_notes/) |
| 写一份新 PRD / Draft a new PRD | 先确认已经过一轮 meeting / 需求挖掘，再读 [`workflows/planning/writing_a_prd.md`](workflows/planning/writing_a_prd.md) → [`templates/prd/`](templates/prd/) |
| 把 PRD 落成代码 / Implement a PRD | [`workflows/engineering/prd_to_implementation.md`](workflows/engineering/prd_to_implementation.md) |
| 修 Bug / Fix a bug | [`workflows/engineering/debugging_workflow.md`](workflows/engineering/debugging_workflow.md) → 找 [`issues/known.md`](issues/known.md) 里的条目 |
| 整理今天的客户电话 / Process today's customer call | [`workflows/customer_communication/sales_call_followup.md`](workflows/customer_communication/sales_call_followup.md) → [`templates/sales_call_summary/`](templates/sales_call_summary/) |
| 给客户出一份项目简报 / Draft a customer brief | [`workflows/customer_communication/customer_brief_generation.md`](workflows/customer_communication/customer_brief_generation.md) → [`templates/customer_brief/`](templates/customer_brief/) |
| 给短视频写脚本 / Draft a short-video script | [`workflows/content_creation/video_script_drafting.md`](workflows/content_creation/video_script_drafting.md) → [`templates/video_script/`](templates/video_script/) |
| 周复盘 / Weekly review | [`workflows/planning/weekly_review_routine.md`](workflows/planning/weekly_review_routine.md) → [`templates/weekly_review/`](templates/weekly_review/) |
| 给同事临时传一份东西 / Daily handoff out to a colleague | [`workflows/operations/handing_off_work.md`](workflows/operations/handing_off_work.md) → [`handoffs/outbox/`](handoffs/outbox/) |
| 收到同事临时传过来一份东西 / Daily handoff in from a colleague | [`workflows/operations/handing_off_work.md`](workflows/operations/handing_off_work.md) → [`handoffs/inbox/`](handoffs/inbox/) |
| 写一条决策记录 ADR / Record an ADR | [`workflows/decision_records/how_to_write_an_adr.md`](workflows/decision_records/how_to_write_an_adr.md) → [`templates/decision_record/`](templates/decision_record/) |
| 上线前自查 / Pre-deploy self-check | [`workflows/engineering/deployment_hygiene.md`](workflows/engineering/deployment_hygiene.md) |
| 出了线上故障 / Production incident | [`workflows/operations/incident_response_workflow.md`](workflows/operations/incident_response_workflow.md) → 红线 #14 |
| 做市场/竞品/客户访谈分析 / Market / competitor / customer-interview analysis | [`workflows/research_and_analysis/`](workflows/research_and_analysis/) |
| 给客户介绍 SEE2AI 平台 / Introduce SEE2AI to a customer | [`products/see2ai/platform_overview.md`](products/see2ai/platform_overview.md) |
| 给客户介绍 TUVE 应用 / Introduce TUVE to a customer | [`products/tuve/app_overview.md`](products/tuve/app_overview.md) |
| 维护 TUVE Agent / Skill / Config 上下文 / Maintain TUVE runtime context | [`products/tuve/openclaw_context/README.md`](products/tuve/openclaw_context/README.md) |
| 协助客户首次接入 SEE2AI / Help customer onboard to SEE2AI | [`products/see2ai/getting_started.md`](products/see2ai/getting_started.md) — 5 分钟跑通首次调用 / first call in 5 min |
| 客户问 SEE2AI 怎么收费 / Customer asks about SEE2AI pricing | [`products/see2ai/pricing_and_account.md`](products/see2ai/pricing_and_account.md) |
| 客户遇到 SEE2AI / TUVE 报错 / Customer hits SEE2AI / TUVE errors | [`products/see2ai/support.md`](products/see2ai/support.md) · [`products/tuve/support.md`](products/tuve/support.md) |
| 不知道从哪开始 / Don't know where to start | [`training/getting_started/`](training/getting_started/) — 14 角色开局引导 / 14-role onboarding（5 分钟读一份就能开工） |

---

## 5. 需求到实施的标准主流程 / Standard Flow from Requirement to Implementation

默认顺序如下，除非用户明确说明需求已经充分收敛：
Default order unless the user explicitly says the requirement is already clarified:

1. **Meeting / 密听 / 需求挖掘**：先把目标、约束、范围、未决问题挖出来；不要一句话需求就直接写方案
2. **PRD**：把 meeting 里已经确认的内容固化成正式产品依据；meeting 只是输入，不是实现依据
3. **Implementation / Execution**：代码、内容、运营动作等实际落地
4. **ADR / Issues / Closeout**：把中途决策、问题和收尾动作补齐

判断是否该先开 meeting，看这 4 个信号：

- [ ] 用户目标还停留在一句话，没有成功标准
- [ ] 范围、边界、角色、约束里至少有一项含糊
- [ ] 你已经能预见会出现 3 个以上澄清问题
- [ ] 任务与 TUVE Agent / skill / config 上下文相关，但上下文还没对齐

只要任意一项为真，就先开 meeting，不要直接写 PRD。
If any item is true, run the meeting/discovery step first instead of jumping into the PRD.

---

## 6. PRD 实施全生命周期清单 / PRD Implementation Lifecycle Checklist

任何"实现 PRD-XXXX"类任务，第一步必须过这份检查表（不要等人提醒）：
For any "implement PRD-XXXX" task, run through this checklist first (don't wait to be reminded):

**开发前 / Before**
- [ ] 找到 [`workspace_human/prd/PRD-XXXX_*.md`](workspace_human/prd/) 这份 PRD，从头读完一次 / Find and fully read the PRD
- [ ] 列出所有"我读完后还不确定"的点，问一遍人，确认了再开工 / List all "still-unsure" points, confirm with the human, only then start
- [ ] 在 PRD 顶部记录"开工时间 / 实现路径草图" / Note "kickoff time / implementation sketch" at top of PRD
- [ ] 画一份 Mermaid 流程节点（哪怕粗）放进 PRD / Sketch a Mermaid node diagram (even rough) into the PRD

**开发中 / During**
- [ ] 每完成一个里程碑，回头给 PRD 节点打勾 / Tick PRD nodes as milestones complete
- [ ] 中途任何决策落字写回 PRD（不要只在脑子里）/ Write all mid-flight decisions back to the PRD
- [ ] 出 Bug 立刻登记到 [`issues/known.md`](issues/known.md)，修完移到 fixed / File bugs immediately to [`issues/known.md`](issues/known.md), move to fixed when done

**开发后五件套 / After (the five must-haves)**
- [ ] 补单元/集成测试 / Add unit/integration tests
- [ ] 在 [`runbooks/`](runbooks/) 或对应 versions 文件登记新版本 / Register new version in [`runbooks/`](runbooks/) or the relevant versions file
- [ ] 给 PRD 写一份"实现完成快照"（对照原始需求一条条核） / Write an "implementation snapshot" on the PRD (item-by-item vs. original requirements)
- [ ] 更新 `AI_MANUAL.md` 第 4 节导航（如果加了新工作流） / Update §4 navigation in `AI_MANUAL.md` if you added new workflows
- [ ] 把所有相关 Bug 移到 [`issues/fixed/`](issues/fixed/) / Move all related bugs to [`issues/fixed/`](issues/fixed/)

任何一项缺失都不许说"完工"。
Any item missing → forbidden to say "done".

---

## 7. 工具特性差异 / Tool-Specific Notes

四个入口文件（CLAUDE.md / AGENTS.md / .cursorrules / CODEX.md）内容一致，但底层工具能力略有差异：
The four entry files share content but the underlying tools differ slightly:

| 工具 / Tool | 强项 / Strength | 入口文件 / Entry file |
|---|---|---|
| Claude Code | 长文档审阅、多步任务、Skill 体系 / Long-doc review, multi-step tasks, Skills | `CLAUDE.md` |
| Cursor | 代码内联编辑、IDE 级体验 / Inline code edits, IDE-grade UX | `.cursorrules` |
| Codex | 命令行任务、脚本化批量 / CLI tasks, scriptable batches | `AGENTS.md` |
| Trae | 兼容 Codex 协议、本土化 / Codex-compatible, localized | `CODEX.md` |

具体在哪种场景挑哪个工具，详见 [`workflows/ai_basics/which_tool_for_which_job.md`](workflows/ai_basics/which_tool_for_which_job.md)。
Tool selection guidance: [`workflows/ai_basics/which_tool_for_which_job.md`](workflows/ai_basics/which_tool_for_which_job.md).

---

## 8. 写在最后 / Final Note

这份手册不是"AI 的镣铐"，而是"AI 的协作合同"。
This manual is not "shackles for the AI" — it is the **collaboration contract** with the AI.

规矩多看起来死板，但每一条都是从过去的真实失败里换来的。新失败可以发生，旧失败不应该再发生。
The rules look heavy, but each one was paid for with a real past failure. New failures may happen; old failures should not happen twice.

如果你（人）发现某条规矩在你的真实工作里其实是阻力大于价值的——把它拿出来在 [`meetings/`](meetings/) 开一个讨论。规矩本身也要随业务进化。
If you (the human) find a rule whose friction outweighs its value in your real work — open a discussion in [`meetings/`](meetings/). The rules evolve with the business too.
