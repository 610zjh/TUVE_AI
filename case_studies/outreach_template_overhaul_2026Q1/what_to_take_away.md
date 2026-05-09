---
name: Top-5 教训
retention: permanent
retention_reason: 5 分钟带走的精华
---

# Top-5 教训

---

## 1. 数据下降不要满足于"市场原因"——做反向证据测试

回复率从 3.2% 降到 1.8% → 业界中位数 2-3% → 我们已经低于中位数 → "市场原因"不能解释全部。
查反向证据排除"销售员素质 / 流量来源 / 季节波动"，锁定"模板内容老化"。

**操作**：诊断指标下降时，先列 ≥ 3 个反向假设并逐一排除，再下结论。

---

## 2. A/B 测试的设计纪律 = 预先约定决策标准

样本量要先算（200 条 / 变体覆盖 1.8% vs 2.5% 差异）。
决策标准要预先约定（统计显著 / 次级指标 / 主观兜底）。
不要测出来"挑对自己有利的"——这是 confirmation bias。

**操作**：A/B 启动前**写一份决策协议**（一页纸），明确"什么数据出来时选 A，什么时候选 B"。

---

## 3. AI 起草的"营销文案"容易堆形容词——必过反 AI 套话清单

v1 的"在数字化时代""革命性""全方位""显著"——典型的 AI 输出特征。
靠销售在前线 5 天反馈才纠正——如果客户都"沉默式拒绝"，我们可能 3 周后才发现。

**操作**：客户面文案 [`workflows/content_creation/marketing_copy_workflow.md`](../../workflows/content_creation/marketing_copy_workflow.md) 三道闸 + AI 起草后强制过 [`principles/subs/content_quality.md`](../../principles/subs/content_quality.md) 的"AI 套话陷阱"清单。

---

## 4. 复评触发"主动提早"——不要等触发了才看

ADR-0028 / 0029 的复评触发是 6 个月。我们 90 天就主动看了一次——发现"创意瓶颈"类视频使用率偏低。
如果等 6 个月触发条件才看，期间我们可能继续做新的创意类视频—— wasted effort。

**操作**：复评触发是底线（没看就违纪），但**主动提早**是更好的纪律。

---

## 5. 基础设施的副产品要主动识别

数据团队为这次 A/B 建了简单看板——后来沿用到其他 A/B 测试。
本来只是一个"项目副产品"，却变成"公司 A/B 平台"。

**操作**：项目结束后回头问"这个项目副产品有没有公司级复用价值？" 有 → 起 ADR / PRD 把它"产品化"。

---

## 三份案例的对比 / All 3 Cases Compared

| 维度 | 案例 1（dashboard）| 案例 2（onboarding）| 案例 3（outreach）|
|---|---|---|---|
| 主导职能 | 产品 | 运营 | 销售 |
| 主要载体 | PRD | 3 份 ADR | PRD + 2 ADR |
| 时长 | 6 周 | 8 周（延 2 周）| 5 周 |
| 关键纪律 | 五件套 + 红线 #2 | ADR + 跨部门时间估算 | A/B 测试 + 内容质量 |
| 主要失误 | 性能目标拍太松 + 顺手重构 | 法务时间低估 + 财务漏审 | v1 营销腔 + 视频类使用率低 |

→ 三份案例的"主要失误"都不一样。每个项目都会有自己的失误——重要的是**有流程能快速发现 + 修正**。

---

## 红线 / 工作流引用清单

- 红线 #2（客户面文案）
- 红线 #6（决策落字 ADR）
- 红线 #15（产品价值 vs 商业包装）—— 数据看板"先扎实简单的"
- [`workflows/research_and_analysis/data_summarization_workflow.md`](../../workflows/research_and_analysis/data_summarization_workflow.md)
- [`workflows/content_creation/marketing_copy_workflow.md`](../../workflows/content_creation/marketing_copy_workflow.md)
- [`workflows/customer_communication/sales_call_followup.md`](../../workflows/customer_communication/sales_call_followup.md)
- [`principles/subs/content_quality.md`](../../principles/subs/content_quality.md)
