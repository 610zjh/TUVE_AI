# 什么时候要落 ADR / When to Record an ADR

> 适用：所有人。判断"这件事我要不要写一份 ADR"。
> For: everyone deciding "should this become an ADR".

---

## 一句话 / One Line

**满足任意一条 → 落 ADR：影响他人 / 涉及取舍 / 难以撤销 / 半年后会被追问。**
**Any of: affects others / involves tradeoffs / hard to undo / will be questioned in 6 months → ADR.**

---

## 4 道判断题 / 4 Diagnostic Questions

### 1. 影响其他人吗？/ Affects Others?

如果决策结果会被销售 / 运营 / 视频 / 开发 / 产品里的 ≥ 1 个其他职能用到 → ADR。
If the outcome is used by ≥ 1 other function → ADR.

例：
- ✅ 决定"所有视频统一改成 60 秒上限" → 视频 + 营销 + 销售都受影响 → ADR
- ❌ 决定"我下午先改 X 页面再改 Y 页面" → 只影响你自己 → 不必

### 2. 涉及取舍吗？/ Tradeoff Involved?

选了 A 就放弃了 B 的某些好处 → ADR。
Choosing A gives up B's benefits → ADR.

例：
- ✅ 决定"用 React 不用 Vue"（放弃了 Vue 的某些生态优势）→ ADR
- ❌ 决定"先改这个 typo 再改那个" → 没取舍 → 不必

### 3. 难以撤销吗？/ Hard to Undo?

撤销要付额外成本（不止一次代码改 / 一封邮件）→ ADR。
Reversal incurs more than one code change / one email → ADR.

例：
- ✅ 决定"所有视频先发到 A 平台再发 B 平台" → 改了之后影响产能、人手分配 → ADR
- ❌ 决定"今天发哪条短视频" → 容易换 → 不必

### 4. 半年后会被追问吗？/ Will Be Questioned in 6 Months?

未来某天有人问"当初为什么这么定？" → ADR。
Someone will ask "why was this decided?" → ADR.

例：
- ✅ 决定"不接 [某行业] 的客户" → 半年后销售看到这个行业的大单会问 → ADR
- ❌ 决定"今天午饭吃什么" → 没人会追问 → 不必

---

## 判断速查表 / Quick Decision Table

| 情境 / Situation | 落字成 ADR？ |
|---|---|
| 决定下周一全员去客户现场而不是远程开 | ❌ 执行性安排 |
| 决定不接一个客户 | ✅ |
| 决定下一支视频用 60 秒而不是 90 秒 | ❌ 创作选择 |
| 决定**所有**视频统一 ≤ 60 秒 | ✅ |
| 决定 Bug 这周不修，先排到下周 | ❌ known.md 登记就够 |
| 决定不修这一类 Bug（永久作为 wontfix） | ✅ |
| 决定面试时多加一个轮次 | ⚠️ 看影响范围 |
| 决定改公司 OKR 的某条 | ✅ |
| 决定用 X 工具 vs Y 工具 | ✅ |
| 决定一个客户的折扣点 | ⚠️ 单次让步不必；如果是"以后这类客户都给"则必 |

---

## "不必落字"的情况 / When NOT to Record

不要把 ADR 当成"流水账"——会让真正重要的 ADR 被噪声淹没。
Don't ADR-everything — important ADRs get drowned in noise.

不必落字的 / Skip:
- 显而易见的执行选择（"先做 X 再做 Y"）/ Obvious sequencing
- 完全可逆的微调 / Fully reversible micro-adjustments
- 业界已有标准做法（"用 git""用 markdown""用 12-hour cron"）/ Industry-default tools
- 个人偏好层面（"我喜欢用 vim 别人喜欢 vscode"）/ Personal style

---

## "应该落但忘了"怎么办 / "Should've Recorded but Forgot"

发现某个决定 2 个月前定了但当时没落字：
If a decision was made 2 months ago without ADR:

→ **现在补一份"追溯型 ADR"**：
→ **Write a retroactive ADR now**:

```markdown
# ADR-NNNN: <标题>

- 实际决策时间 / Actual decision date: 约 2026-XX-XX (estimated)
- 追溯补写时间 / Retroactively written: 2026-MM-DD by [name]
- 状态 / Status: Accepted (retroactive)

## 注：此 ADR 为追溯补写
当时决策没落字。现在补写以保留决策历史。我尽量诚实重建当时的考量，
但部分细节可能已记不准。

## 背景 / Context
（基于现在能找回的资料 + 我的回忆）...

## 选项 / Options
（如果当时确实考虑过其他选项）...
（如果想不起来，写"当时具体考虑过的选项已记不准"，比假装记得好）

## 决策 / Decision
当时选了 X，原因（基于 git log / 当时邮件 / 我的回忆）是 ...

## 后续观察 / Observations Since
（这个决策落地后这几个月里的实际表现）
```

不要假装它是当时写的。诚实标注追溯。
Don't pretend it was written at the time. Honestly mark it retroactive.

---

## 不要把 ADR 写得太大 / Don't Bloat ADRs

经验：一份 ADR 1-2 页足够。
Heuristic: 1-2 pages per ADR.

500 行的 ADR 试图把一个大主题的所有面都覆盖——没人会读完。
A 500-line ADR trying to cover everything → nobody finishes.

正确做法：把大决策**拆成多份小 ADR**，每份 1-2 页，互相引用。
Right: split big decisions into multiple small ADRs, cross-referenced.

---

## ADR 是不是越多越好 / Quantity vs Quality

不是。
No.

写 50 份没人读的 ADR = 写了一份索引混乱的目录。
50 unread ADRs = chaotic index of nothing.

每写一份，问自己：
For each:
- 这份决策值不值得 6 个月后的人翻出来？
- 它具体到"放弃了什么、复评条件是什么"了吗？
- 它编号清楚、命名清楚、能被搜到吗？

3 个都"是" → 写。任何一个"否" → 先把它修到都"是"。

---

## 季度 ADR 复评 / Quarterly ADR Review

每季度，由相关负责人扫一遍 ADR 列表：
Quarterly, the relevant lead scans the ADR list:

- 哪些已经触发"复评条件"？/ Which have triggered re-review?
- 哪些状态还是 Proposed 但已经过时了？/ Which are still Proposed but stale?
- 哪些被实际行为推翻了但状态没更新？/ Which were superseded in practice but not marked?

更新状态。该推翻的推翻，该补 superseded by 链接的补。
Update statuses. Mark superseded with links.

---

## 速查 / Cheat Sheet

```
4 道判断题：
1. 影响他人？
2. 涉及取舍？
3. 难以撤销？
4. 半年后会被追问？

任一是 → ADR。

不必落字：执行性 / 完全可逆 / 业界标准 / 个人偏好

补救：发现遗漏立刻写"追溯型 ADR"，诚实标注

不要：写超过 2 页 / 写没人读的 / 把每件小事都 ADR
```
