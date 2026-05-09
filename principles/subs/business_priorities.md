---
name: 业务主次 / Business Priorities
description: 红线 #15 的展开——产品价值优先于商业包装 / Expansion of Red Line #15 — product value before commercial packaging
type: permanent
retention: permanent
retention_reason: 防止"为收费而限制"的常见公司退化 / Prevents the common corporate degradation of "restrict in order to monetize"
---

# 业务主次 / Business Priorities

## 红线 #15 重申 / Red Line #15 Restated

**产品价值在前，商业包装在后。**
**Product value first. Commercial packaging second.**

- 一项功能没做扎实之前，**绝不**因为"想收费"而限制它 / Never restrict a feature for monetization before it's solid
- 任何 paywall / feature gate / 分层 PRD，**必须**包含"主次审视"章节，明确"这一步是不是把主次搞反了" / Any paywall / feature gate / tiering PRD **must** include a "Priority Audit" section explicitly asking "is this inverting product and commerce?"
- 商业模式合理性的基础是**真实成本差异 + 真实用户价值差异**，不是"先把功能锁起来逼用户付费" / Commercial design rests on **real cost differential + real value differential**, not "lock features and pressure users to pay"

---

## 为什么这条这么严 / Why This Rule Is So Strict

### 失败模式：把"功能未做完"伪装成"高级功能要付费" / Failure Mode: Disguising "Unfinished" as "Premium"

经典退化路径：
Classic degradation path:

1. 功能没做扎实（速度慢 / 偶发出错 / 缺细节）/ Feature isn't solid (slow / flaky / missing detail)
2. 团队压力上来（融资 / 季度目标 / 投资人催）/ Team pressure mounts (funding / quarterly target / investors)
3. 决定："把这个功能收费版多加一些限制，免费版变得很难用，让用户付费" / Decision: "add more limits to free, make it painful, push to paid"
4. 实际结果：付费用户也用不爽（因为底层还是没做扎实），免费用户更没机会用 → 留存全崩 / Reality: paid users also unhappy (foundation still flaky), free users locked out → retention collapses
5. 团队反思："看来用户不愿意付费啊" / Team: "users aren't willing to pay"
6. **真相**：用户不是"不愿付费"，而是"产品没把价值做出来到值得付费的程度" / **Truth**: users aren't unwilling, the product just hasn't crossed the value-worthiness threshold yet

每一步都看起来合理。但放在一起是把一个**产品问题**误诊成**商业模式问题**，结果是**两个问题都没解决**。
Each step seems reasonable. But the chain misdiagnoses a **product problem** as a **commercial-model problem**, leaving **both unsolved**.

### 业界已经反复验证 / Industry Has Validated

成功的 SaaS 公司大多遵循"先把核心价值做爆 → 再设计分层"的路径。
Successful SaaS companies overwhelmingly follow "make the core value explode → then design tiers".

把分层做在前面（核心价值还没爆）的公司大多卡死。
Companies that tier before the core value explodes mostly stall out.

---

## 主次审视 / Priority Audit

任何 paywall / feature gate / 分层 PRD，**必须**包含一段"主次审视"。模板：
Any paywall / feature gate / tiering PRD **must** include a "Priority Audit" section. Template:

```markdown
## 主次审视 / Priority Audit

### 1. 当前功能的成熟度 / Current Feature Maturity
- 此功能上线时间：YYYY-MM-DD
- 已发现 Bug 数（known.md 里的）：N
- 客户主动反馈："好用"占 X% / "可用"占 Y% / "难用"占 Z%
- 我们自己使用一周的真实体验：...

### 2. 真实成本差异 / Real Cost Differential
- 免费档：单用户每月对我们的成本 = $X
- 付费档：单用户每月对我们的成本 = $Y
- 差异是不是显著（≥ 30%）？/ Is the differential significant (≥ 30%)?
- 差异来自：算力 / 存储 / 人工服务 / 第三方 API ...

### 3. 真实用户价值差异 / Real User Value Differential
- 免费档用户能完成的核心工作流：...
- 付费档用户多解锁的能力是什么？这些能力对应客户的哪种 ROI 提升？
- 客户原话：付费档用户主动说过这些能力值得多少钱？

### 4. 主次审视结论 / Priority Audit Conclusion
- ✅ 已通过：本 PRD 的分层基于真实成本差 + 真实价值差
- ⚠️ 部分通过：成本差不够显著但价值差成立，建议先做价值差对应的功能完善
- ❌ 未通过：当前不存在显著成本差和价值差，本 PRD 实质是"以收费为目的限制"，**应停止**

### 5. 如果未通过，下一步 / If Not Passed, Next Step
- 撤回本 paywall PRD
- 起一份新 PRD：把现在打算锁的功能"做到值得付费的程度"
- 等做扎实了再回来谈分层
```

---

## 不需要主次审视的情况 / When Priority Audit Is Not Needed

- 纯**新功能**的 PRD（不是 paywall / 分层）/ Pure **new-feature** PRDs (not paywall / tiering)
- 纯 Bug 修复 / Pure bug fixes
- 内部工具 / 流程改进 / Internal tools / process improvements

需要主次审视的情况 / When Priority Audit IS needed:
- 引入 paywall / Introducing a paywall
- 加 feature gate / Adding a feature gate
- 调整分层（升级 / 降级现有档位）/ Adjusting tiers
- 引入用量限额（rate limit / quota）作为限制免费用户的手段（如果是真实成本控制则不在此限）/ Introducing usage limits as a free-user gate (genuine cost control is exempt)

---

## "真实成本差异" 怎么算 / How to Calculate Real Cost Differential

不要算"我们希望用户感觉差很多"——算"我们实际付出的成本差"。
Don't calculate "the gap we want users to feel" — calculate "the gap we actually pay".

| 项目 / Item | 算法 / How to calculate |
|---|---|
| **API 成本** API costs | 平均 token 消耗 × 模型单价 |
| **存储** Storage | 用户文件大小 × 存储单价 × 月份 |
| **算力** Compute | 平均 CPU/GPU 时长 × 算力单价 |
| **人工** Human ops | 客服 / 集成 / 培训 平均工时 × 工时成本 |
| **第三方** 3rd-party | 外部服务每用户实付 |

**不算入成本差的**：
**Not counted as cost differential**:
- 团队工资（除非是付费档专属人工服务）/ Team salary (unless paid-tier-exclusive human services)
- 营销成本 / Marketing cost
- "稀缺性"（稀缺不是成本，是营销策略）/ "Scarcity" (not a cost, just marketing tactic)

---

## "真实价值差异" 怎么验证 / How to Validate Real Value Differential

不要算"我们觉得这个 feature 值多少钱"——验证"客户用了多了之后真实带来的 ROI"。
Don't compute "what we think this feature is worth" — validate "what ROI customers actually realized".

方法 / Methods:
1. **小范围 beta**：让一组核心用户先用，跟踪他们的真实工作流变化 / Small beta: track core users' actual workflow shifts
2. **客户访谈**：访谈用了 1-3 个月的付费用户，问"哪一项功能让你觉得这个价格是值得的" / Customer interview: ask 1-3 month paid users which feature justifies the price
3. **流失分析**：流失客户的退订理由里是不是反复提到"X 功能不够好" / Churn analysis: do exit reasons cluster around a specific feature gap
4. **付费意愿测试**：让客户主动报价"愿意为 X 功能多付多少" / WTP test: ask customers what they'd pay extra for X

数据撑不住"真实价值差异"时，就还没到分层的时机。
If data doesn't support "real value differential", it's not yet time to tier.

---

## 真实价值差异 vs 营销话术差异 / Real Value Differential vs Marketing Differential

营销话术可以放大真实价值差异，但**不能制造**真实价值差异。
Marketing can amplify real value differential, but **cannot manufacture** it.

| 例子 / Example | 是真实价值差吗？ |
|---|---|
| 付费档可以批量上传（免费档单个）/ Paid: bulk upload, free: single | ✅ 是（真实工作流加速） |
| 付费档解锁"高级 AI 模型"（免费档用基础模型）/ Paid: premium AI, free: basic | ⚠️ 看模型差是否能让用户感受到效果差 |
| 付费档的 logo 颜色更鲜艳 / Paid: brighter logo color | ❌ 假差异 |
| 付费档可以导出 mp4 / 免费档只能 mov / Paid: mp4, free: mov | ❌ 假差异（除非真有兼容性差异） |
| 付费档客户被分配专属客服 / Paid: dedicated CSM | ✅ 是（真实成本 + 价值差） |
| 付费档可以批量自动化 / 免费档要逐条手动 / Paid: batch automation, free: per-item | ✅ 是（真实工作流差） |

---

## 当老板 / 投资人压力来了 / When Pressure Mounts (Boss / Investor)

经典对话：
Classic dialogue:

> 老板：「下个季度收入要翻倍。把免费档功能砍 30%，逼一波转化。」

错误反应（顺从）/ Wrong reaction:
- 起一份 PRD 把 30% 功能塞进 paywall
- 上线
- 三个月后留存崩，收入没翻倍，团队疲惫

正确反应（push back with data）/ Right reaction:
1. 引用本红线，说"按照我们的工作纪律，paywall PRD 必须先过主次审视" / Cite this rule
2. 起一份**主次审视**草稿，里面诚实评估"现在加 paywall 是不是把主次搞反了" / Draft a Priority Audit honestly evaluating
3. 把审视结论交给老板：
   - 如果 ✅ 通过：执行 / If passes: execute
   - 如果 ⚠️ 部分通过 或 ❌ 未通过：和老板讨论"先把核心价值做扎实" 的替代方案 / If partial / fails: discuss alternatives with boss

老板拍板说"我知道审视没过，但我就是要这么干"——这是越过红线的请求，按红线 #2 的"红线如何演进"流程走（[`000_CORE_RED_LINES.md`](../000_CORE_RED_LINES.md) Chapter 2），不是默默执行。
If boss says "I know it failed audit, do it anyway" — that's a red-line-crossing request. Follow the red-line-evolution flow (`000_CORE_RED_LINES.md` Chapter 2), don't silently comply.

---

## "做扎实"是什么意思 / What "Solid" Means

具体可衡量的"做扎实"标准：
Concrete measurable "solid" standards:

- 功能上线后 ≥ 90 天 / In production ≥ 90 days
- 客户主动反馈"难用"比例 ≤ 15% / Customer "hard-to-use" feedback ≤ 15%
- 已发现 Bug 中 P0/P1 数为 0 / Open P0/P1 bugs = 0
- 自然留存（没营销活动推动的）≥ 业界中位数 / Organic retention (no marketing-pushed) ≥ industry median
- 单位经济模型（每用户对我们的成本/收益）已建模 / Unit economics modeled

至少 4/5 满足，才算可以谈商业包装。
At least 4/5 pass before commercial packaging discussion can begin.

---

## 一句口诀 / Mnemonic

> 当你想加 paywall 时，先问自己："我是在**抽走客户已经在享受的价值**，还是在**为新增的更高价值定价**？"
> When you want to add a paywall, ask: "Am I **extracting value customers already enjoy**, or **pricing newly-added higher value**?"
>
> 前者是反向，后者是顺向。
> Former is regressive. Latter is progressive.
