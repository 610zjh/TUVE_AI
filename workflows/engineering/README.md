# workflows/engineering/

> 涉及"写代码 / 修 Bug / 部署 / 测试"类工作。
> For: writing code / fixing bugs / deploying / testing.

---

## 阅读顺序 / Reading Order

新人按这个顺序读：
New engineers read in this order:

1. [`prd_to_implementation.md`](prd_to_implementation.md) —— PRD 到代码的全生命周期
2. [`code_review_with_ai.md`](code_review_with_ai.md) —— 用 AI 做代码评审
3. [`debugging_workflow.md`](debugging_workflow.md) —— Debug 5 步法
4. [`testing_discipline.md`](testing_discipline.md) —— 测试纪律
5. [`deployment_hygiene.md`](deployment_hygiene.md) —— 部署前 / 中 / 后清单
6. [`bug_tracking_ssot.md`](bug_tracking_ssot.md) —— Bug 单一登记本

---

## 共同纪律 / Shared Discipline

- 红线 #5：改代码前必有 PRD 或 Bug 编号
- 红线 #7：单文件 ≤ 800 行
- 红线 #8：不可逆动作（部署 / 删数据 / 退款）必须人确认
- 红线 #9：命名按"5 年后还看得懂"
- 红线 #10：收尾五件套必须全
- 红线 #13：修 Bug 同步清反向断言测试
- 红线 #14：线上故障第 1 动作看日志
