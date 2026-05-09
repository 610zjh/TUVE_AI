---
name: 内容质量与文案 / Content Quality and Copy
description: 给客户、合作伙伴、公开渠道的所有文字 / 视频 / 设计内容的最低质量线 / Floor for all customer-facing copy, video, and design content
type: permanent
retention: permanent
retention_reason: 一条不达标的客户文案能毁掉一条成单线 / One off-brand customer-facing string can sink a deal
---

# 内容质量与文案 / Content Quality and Copy

## 红线 #2 重申 / Red Line #2 Restated

**任何客户能在 UI / 邮件 / 客服对话 / 短视频字幕里看到的字符串，禁止出现：**
**Any string a customer could see (UI / email / support chat / video captions) must NOT contain:**

- 内部 PRD 编号（`PRD-XXXX`）/ Internal PRD numbers
- Bug 编号 / Bug IDs
- 内部表名 / 字段名 / 接口名 / Internal table / field / API names
- 模型 endpoint / 模型 ID / 厂商内部代号 / Model endpoint, model ID, vendor codename
- 内部岗位代号 / 项目代号 / Internal role or project codenames
- 内部排期措辞（"运维同步回填""下个版本上线"）/ Internal scheduling phrases
- 测试客户名 / 真实但不同客户名 / Test customer names, or other real customers' names
- 业务线之间的内部价差 / 折扣权限 / 销售底线 / Internal pricing levels, discount authorities, sales floors

**例外**：注释、后台日志、admin-only 面板——AI 内部沟通不在此限。
**Exempt**: comments, backend logs, admin-only panels — internal AI working chat is fine.

---

## 为什么这条这么死 / Why This Rule Is So Strict

一条违规文案能：
A single violating string can:
- 让客户看到内部代号 → 觉得"他们对我们透明吗？" / Make customer see internal codes → "are they being transparent with us?"
- 让竞争对手看到内部排期 → 抢先公关 / Let competitors see internal roadmap → preemptive PR
- 让一位客户看到另一位客户的名字 → 即时信任崩塌（GDPR / 国内个保法都不允许）/ Let one customer see another's name → instant trust collapse (also legally risky)
- 让你内部本来准备升级的功能被客户当成"现在能用"的承诺 → 法务介入 / Let an internal-WIP feature read as a public promise → legal escalation

每一条都是真实事故的等价物。
Each is the equivalent of a real past incident.

---

## 写客户面文案的"红绿灯检查" / Traffic-Light Check for Customer-Facing Copy

写完后默念三个问题：
After drafting, ask three questions:

🟢 **绿灯（可以发）/ Green (ship it)**
- 我把这段抄给"完全不知道我们公司内部情况"的人，他能看懂吗？
  Could a stranger to our company internals understand this verbatim?
- 这段话过 6 个月，组织变化（PRD 编号变了 / 服务名变了）以后，还是对的吗？
  Is this still correct 6 months from now, after PRD numbers / service names change?
- 如果客户截图发到他们老板群里，我会觉得 OK 吗？
  Would I be OK if the customer screenshotted this to their boss's chat?

🟡 **黄灯（停下重写）/ Yellow (pause and rewrite)**
- 含有"我们的内部 X""上个版本""下个版本"这类引用 / Contains "our internal X", "previous version", "next version"
- 含有日期排期但日期可能错 / Contains roadmap dates that might slip
- 借用了行业术语但客户可能不熟 / Uses industry jargon the customer may not know

🔴 **红灯（绝对不能发）/ Red (do not send)**
- 出现红线 #2 列表里的任何一项 / Contains anything from Red Line #2's list
- 引用了一位**其他**客户的名字 / 案例 / 数据 / Cites another customer's name, case, or data
- 出现"内部"、"运维"、"团队"这类把内部分工暴露给客户的词 / Contains "internal", "ops", "team" that leaks internal division of labor
- 含有 admin 截图、后台 URL、调试链接 / Contains admin screenshots, backend URLs, debug links

---

## 错文案 → 对文案 范例库 / Anti-Pattern → Pattern Library

### 例 1：空状态 / Example 1 — Empty state

❌ 错（含 PRD 编号 + 内部排期）/ Wrong:
> 这是 PRD-XXXX 上线之前生成的旧素材；运维同步回填后可在此看到。

✅ 对 / Right:
> 这一区域目前没有内容。新生成的素材将在这里展示。

### 例 2：错误提示 / Example 2 — Error prompt

❌ 错（含模型 endpoint）/ Wrong:
> 调用 gpt-4o-mini-2025-08-07 失败：连接 anthropic-claude-haiku-4-5-20251001 超时

✅ 对 / Right:
> AI 服务暂时无法响应，请稍后重试或联系客服。

### 例 3：客户邮件 / Example 3 — Customer email

❌ 错（提到另一位客户）/ Wrong:
> 我们刚帮"晨星科技"上了类似的功能，他们效果非常好。

✅ 对 / Right:
> 我们近期为同行业的几家客户落地过类似方案，整体反馈正向（具体数据可在演示时展开）。

### 例 4：营销视频字幕 / Example 4 — Marketing video caption

❌ 错（含项目代号）/ Wrong:
> 内部代号"猎户座"项目，将在 2026 Q3 揭晓。

✅ 对 / Right:
> 我们正在打磨一项全新功能，预计在年内向所有客户开放。

### 例 5：支持工单回复 / Example 5 — Support ticket reply

❌ 错（含 Bug 编号）/ Wrong:
> 已记录 Bug-2026-0417-A，下个版本会修。

✅ 对 / Right:
> 这个问题我们已经识别到，正在修复中，修复后会立刻通知您。

---

## 短视频脚本特殊考虑 / Short-Video Script Specifics

短视频是 TUZHAN 的核心产出之一。除了上述红线外，再加几条：
Short-video is one of TUZHAN's core outputs. Beyond the rules above, add:

1. **不剧透产品具体能力之外的"我们正在做"承诺**——视频在网上的留存时间远超你的预期。
   **Don't promise "we're working on X"** beyond shipped capabilities — videos persist online longer than you expect.
2. **同一支视频里出现的真实人物（员工 / 客户）必须有授权**。授权落字到 [`workspace_human/meetings/`](../../workspace_human/meetings/)。
   **Real persons (employees, customers) appearing in a video must have written authorization** in [`workspace_human/meetings/`](../../workspace_human/meetings/).
3. **数据呈现要保留可追溯性**——用了"提升 47%"的话，背后的统计口径写在拍摄笔记里，方便日后被问到能调出。
   **Numbers must remain traceable** — "47% improvement" → record the methodology in shooting notes for future questioning.
4. **不要把还在 A/B 测试的素材拿去公开发布**——A/B 数据可能反向，先发后撤回比不发更损形象。
   **Don't publish material still under A/B test** — flipping A/B results force a retraction, which hurts more than not publishing.

---

## 多语言文案的额外纪律 / Multi-Language Copy Discipline

TUZHAN 是跨国企业，部分材料需要中英双版本。
TUZHAN is multinational; some material requires CN+EN.

- **AI 翻译后人必须过一遍**，不许"AI 翻完直接发"。AI 在专有名词、行业黑话、文化语境上经常翻车。
  **AI translation must be reviewed by a human** before sending. AI often fails on proper nouns, industry slang, and cultural context.
- **品牌名 / 产品名保留英文原写，不音译**（除非品牌就是音译命名）。
  **Brand and product names keep English** — no Chinese transliteration unless the brand itself is transliterated.
- **数字格式按目标读者所在地**：中文常用"万 / 亿"，英文用 "10K / 1M"。不要混用。
  **Number formats follow target locale**: Chinese uses 万/亿; English uses K/M. Don't mix.

---

## 内容质量自查工具 / Content Self-Check Tool

写完后跑一下 grep（如果有命令行）/ After drafting, run grep:

```bash
# 检查是否含有禁止词 / Check for banned terms
grep -E '(PRD-[0-9]+|Bug-[0-9]+|TUZHAN-internal|内部代号|运维|claude-|gpt-|anthropic-)' your_draft.md
```

如果命中，立即重写。
If matches found, rewrite immediately.

---

## 当 AI 起草客户面文案时 / When AI Drafts Customer-Facing Copy

给 AI 的提示词必须显式包含：
The prompt to AI must explicitly include:

> 这是给客户看的内容。**禁止**出现内部 PRD 编号、Bug 编号、模型 ID、内部岗位代号、其他客户名、内部排期措辞、admin URL。最终客户能看到字面所有内容。

不要假设 AI 默认遵守红线 #2——它不会。每次都明说。
Don't assume AI defaults to Red Line #2 — it won't. Restate every time.
