# 客户简报生成 / Customer Brief Generation

> 适用：销售、客户成功、产品在给客户出"项目简报""方案简报""阶段总结"等正式材料时。
> For: drafting formal customer briefs (project / proposal / phase summary) for customers.

---

## 一句话 / One Line

**客户简报的目标是让客户能在 5 分钟内 (a) 确认"我们听对了你需要什么" (b) 知道接下来会发生什么。**
**A customer brief gets the customer to (a) confirm "we heard what you need" and (b) know what happens next, in 5 minutes.**

---

## 标准结构 / Standard Structure

```markdown
# [项目名] - 客户简报

- 提交日期：YYYY-MM-DD
- 我方负责人：[name + 联系方式]
- 客户对接人：[name]
- 文档版本：v0.X

## 1. 我们对您需求的理解
（用客户自己的语言描述他想达成什么）
（一两句话，让客户读完后说"对，就是这意思" 或 "不对，是 ..."）

## 2. 我们建议的方案
（针对上面的需求，我们提议怎么做）
（用客户能懂的语言，不堆术语）

## 3. 时间表
- 阶段 1（时间 X-Y）：[做什么]
- 阶段 2（时间 Y-Z）：[做什么]
- 阶段 3（时间 Z-W）：[做什么]

## 4. 接下来的事
- 我们：在 [日期] 之前做 [具体动作]
- 您：在 [日期] 之前确认 [具体内容]
- 双方：在 [日期] 一起做 [具体动作]

## 5. 您可能想问
（提前回答 top-3 客户最可能问的问题——既显示主动，也减少来回邮件）

## 6. 联系方式
- 我方主负责人：[name + 邮箱 + 微信 / WhatsApp]
- 我方备用联系人：[name + 邮箱]（出差 / 假期时）
```

---

## 用 AI 起草的 3 步 / 3 Steps with AI

### 步 1：拼齐输入 / Step 1: Gather Inputs

```
我要为客户 [脱敏标签，如"客户 A，教育-中型"] 起一份项目简报。

输入材料：
- 客户初次访谈纪要：[粘贴或路径]
- 双方过去几次沟通的关键决议：[粘贴]
- 我们内部的实施方案草稿：[粘贴或路径]

输出：客户简报 v0.1，按 [`templates/customer_brief/`](../../templates/customer_brief/) 模板。

约束：
- 不出现 PRD 编号 / Bug 编号 / 内部代号（红线 #2）
- 不点名其他客户
- 数字 / 时间 / 承诺必须可兑现
- 客户能看的字面所有内容
```

### 步 2：审"听对了吗"段 / Step 2: Review "We Heard You" Section

第 1 段（"我们对您需求的理解"）是简报最关键的一段。
Section 1 ("Our understanding of your needs") is the most important section.

```
请基于客户原话（粘贴），重写第 1 段，确保：

1. 用客户自己的语言（不要"提升数字化转型"这种 AI 套话）
2. 包含客户提过的具体痛点（"内容产出量上不去""人手不够"...）
3. 不解读 / 不延伸——只镜像客户说过的
4. 长度 ≤ 150 字

如果客户原话里**没有明确**说出某个需求，但你（基于过往经验）感觉客户"应该"也需要——单独标"假设"段，让客户看到我们的假设并能纠正。
```

### 步 3：把客户面三道闸跑一遍 / Step 3: Run the 3 Customer-Facing Gates

```
对全文，自查：

闸 1：扫禁词 → PRD-XXXX / Bug-XXXX / 模型 endpoint / 内部岗位代号 / 其他客户名
闸 2：品牌声音 → 是不是 TUZHAN 的语气（不卑不亢、专业但有人情味，不堆术语）
闸 3：法务可承诺 → 简报里所有承诺（功能 / 时间 / 效果）能兑现吗？是不是过紧了？

把发现的问题列出来。
```

---

## 双语简报 / Bilingual Briefs

跨国客户经常需要双语简报。
Multinational customers often need bilingual.

布局选项：
Layout options:

```
选项 A：上下双语（每段中英对照）
- 适合：双方读者都不强占主导
- 缺点：篇幅 ×2

选项 B：单文档双语（中文先，英文后）
- 适合：中文是主沟通语言，英文是备份
- 优点：篇幅经济

选项 C：两份独立文档（中文版 + 英文版）
- 适合：客户内部分中外两批读者
- 缺点：需保持版本同步
```

参考 [`workflows/content_creation/multilingual_localization.md`](../content_creation/multilingual_localization.md)。

---

## 客户简报的常见错误 / Common Brief Mistakes

| 错误 / Mistake | 表现 / Symptom | 修正 / Fix |
|---|---|---|
| **AI 套话"** | "在数字化时代""提升业务效率" | 用客户具体场景的语言 |
| **过度承诺** | "我们保证 X% 的效率提升" | 改成"基于过往同类客户的经验，X% 的提升是合理预期" |
| **时间表模糊** | "近期完成" | 改成具体日期 |
| **下一步没主语** | "确认方案细节" | 改成"您 [日期] 前确认 [具体内容]" |
| **没有联系方式** | 客户找你要打几次电话才找到 | 邮箱 + 即时通讯 + 备用联系人 |
| **暴露内部信息** | "我们的研发会按 PRD-XXXX 实现" | 改成"我们的团队将在 [日期] 前实现这些能力" |

---

## 简报版本管理 / Brief Versioning

每次客户提反馈 → 出新版本 v0.2 / v0.3。
Each customer-feedback round → new version.

**不要静默修改**——保留历史版本，让客户看到改动轨迹。
**Don't silently edit** — keep history; let customer see edits.

```
v0.1 - 2026-04-23 - 初稿
v0.2 - 2026-04-25 - 按客户 4/24 反馈调整方案细节
v0.3 - 2026-04-29 - 添加预算明细段
```

最终签字版本（v1.0）后，不再改。后续变更走"变更单"流程（[`templates/customer_brief/change_request.md`](../../templates/customer_brief/)）。
After signed version (v1.0), no edits. Later changes via "change request" flow.

---

## 红线提醒 / Red Line Reminders

- 红线 #2：客户面文案禁止内部信息
- 红线 #5：方案细节落地要对应 PRD（**但 PRD 编号不出现在简报里**——只在内部交叉引用）
- 红线 #8：简报发出前人审 + 客户确认是关键节点
- 红线 #15：如果简报涉及付费档 / 限制免费档，**必含主次审视**

---

## 速查 / Cheat Sheet

```
结构 6 段：理解 / 方案 / 时间 / 下一步 / 您可能想问 / 联系

3 步法：拼输入 → 审"听对了"段 → 跑三道闸

陷阱：AI 套话 / 过度承诺 / 时间表模糊 / 下一步没主语 / 没联系方式 / 暴露内部

要：客户的具体场景语言 / 可兑现的承诺 / 具体日期 / 可识别的下一步
```
