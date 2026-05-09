# 多语言本地化 / Multilingual Localization

> 适用：所有跨语言、跨地域内容（产品 UI、邮件、视频字幕、营销文案、合同）的本地化工作。
> For: all cross-language / cross-region content localization (product UI, emails, video subtitles, marketing, contracts).

---

## 一句话 / One Line

**翻译 ≠ 本地化。** 翻译只换语言，本地化换语言 + 文化语境 + 行业用词 + 法律 / 监管要求。
**Translation ≠ localization.** Translation swaps language; localization swaps language + culture + industry vocabulary + legal/regulatory requirements.

AI 在翻译上 70 分，在本地化上 30 分。剩下的 70 分必须人补。
AI: 70/100 on translation, 30/100 on localization. The remaining 70 needs a human.

---

## 4 类内容的本地化策略 / 4 Content Type Strategies

| 类型 / Type | AI 主导 / AI-led | 人补什么 / Human adds |
|---|---|---|
| 产品 UI 文案 | ✅ 起初稿 | 行业黑话、本地化的语气、本地法律措辞 |
| 客户邮件 / 销售物料 | ⚠️ 起草后必须人重写 | 文化语境、当地客户偏好、销售风格 |
| 视频字幕 | ⚠️ 听写 + 初译 OK | 字数控制、口语化、文化梗 |
| 合同 / 法律文件 | ❌ 不做 | 必须法务起草 / 翻译；AI 仅做术语对照 |

---

## 8 步法（任何内容通用）/ 8-Step Process (Universal)

### 步 1：明确目标读者 + 渠道 / Step 1: Audience + Channel

```
我要本地化的内容是 [描述]。
- 源语言：[X]
- 目标语言：[Y]
- 目标读者：[国家 / 地区 / 行业 / 角色]
- 发布渠道：[官网 / 邮件 / 印刷 / 视频字幕 / ...]
- 法律 / 监管考虑：[GDPR / 个保法 / 食品药品 / ...]
```

### 步 2：建立术语对照表 / Step 2: Glossary

任何反复出现的术语 / 产品名 / 角色名都要先建对照：
Build a glossary for any recurring term / product name / role name:

```
请基于上面的内容，列出所有反复出现的术语 / 专有名词，建对照表：

| 中文 | 英文 | 注释（为什么这么译）|
|---|---|---|
| ... | ... | ... |

约束：
- 品牌名 / 产品名一律保留英文原写（除非品牌就是中文命名）
- 行业黑话用业界标准译法（你不确定的标"待人确认"）
- 不要"自创翻译"——比如把"feature flag"译成"特性旗"，没人这么用
```

术语对照表存到 [`workspace_human/`](../../workspace_human/) 下，跨项目复用。
Save glossary in `workspace_human/`, reuse across projects.

### 步 3：AI 起初稿 / Step 3: AI Draft

```
基于上面的术语对照表，请把以下内容从 [源语] 译成 [目标语]：

[原文]

约束：
- 严格使用术语对照表
- 数字格式按目标读者所在地（中文：万 / 亿；英文：K / M）
- 日期格式按目标读者所在地（中文 YYYY-MM-DD；美式 MM/DD/YYYY；欧式 DD/MM/YYYY）
- 货币按业务约定（人民币 ¥ / 元；美元 $；欧元 €）
- 标点按目标读者所在地（中文全角；英文半角）
- 不出现源语言的"残留"（比如英文译版里出现"哦"这种中文叹词）
```

### 步 4：自查"AI 翻译典型错误" / Step 4: AI-Translation Error Self-Check

```
对你刚才的译文，自查：

1. 有没有把多义词译成了**这个语境里错误的含义**？
2. 有没有把**习语 / 俗语**直译了（应该意译或换成目标语言的对应说法）？
3. 有没有"翻译腔"（语序明显是源语言的，目标语言读起来不自然）？
4. 数字 / 日期 / 货币的格式是不是按目标读者所在地了？
5. 文化语境（节日、人物、典故）有没有需要替换的？

把发现的问题列出来 + 给修改建议。
```

### 步 5：人审 / Step 5: Human Review

AI 译稿**必须**有目标语言为母语 / 长期使用 的人审。
AI translation **must** be reviewed by a target-language native or long-term user.

人审重点：
- 术语对照是否正确 / Glossary correctness
- 语气和风格是否匹配品牌 / Tone and style match brand
- 文化语境是否合适 / Cultural fit
- 法律 / 监管措辞是否准确 / Legal / regulatory wording

### 步 6：本地化的"非翻译"调整 / Step 6: Beyond-Translation Localization

不是所有内容都能"翻译"——有些需要**重写**：
Not everything translates — some needs **rewriting**:

| 元素 / Element | 处理 / Treatment |
|---|---|
| **示例 / 案例** | 用目标地区的例子（北美用 Walmart，中国用京东）|
| **客户案例** | 用当地客户（如有）|
| **节日 / 时令** | 替换成目标地区的节日（春节、感恩节）|
| **人物 / 名字示例** | 替换成本地常见名（"张三 / Alice"）|
| **货币示例** | 用本地货币 |
| **法律措辞** | 引用目标地区法律（GDPR vs 个保法 vs CCPA）|
| **支付方式** | 提及本地常用方式（微信 / 支付宝 vs PayPal / Apple Pay）|

### 步 7：技术检查（如果是 UI / 软件）/ Step 7: Technical Check (UI / Software)

软件 UI 的本地化还有技术陷阱：
Software UI localization has technical pitfalls:

- **字符串长度膨胀**：中文 → 英文通常变长 1.5x；德语 / 法语更长。UI 容器要预留空间 / String length expands; budget UI space
- **字符方向**：阿拉伯语 / 希伯来语是 RTL，UI 镜像翻 / RTL languages need mirrored UI
- **日期 / 数字格式占位符**：用 i18n 库（不要硬编码）/ Use i18n libs, don't hardcode
- **图标 / 颜色文化语义**：红色在中国是吉利、在西方是警告 / Cultural semantics differ
- **表情包 / Emoji**：跨平台显示可能不同 / Cross-platform emoji rendering varies

### 步 8：发布后监控 / Step 8: Post-Launch Monitoring

本地化版本发布后要监控：
Monitor post-launch:

- 客户主动反馈（投诉 / 困惑 / 误解）/ Customer feedback (complaints / confusion / misunderstanding)
- 法律 / 监管投诉（如有）/ Legal / regulatory complaints
- 客服 ticket 关键词（哪些词被反复问）/ Support ticket keywords

发现问题 → 回到术语对照表更新 → 重译相关内容。
Issues → update glossary → retranslate affected content.

---

## 红线提醒 / Red Line Reminders

### 不要把客户数据 / 合同条款让 AI 翻译

红线 #3：未脱敏的机密数据严禁进入 AI 上下文。
Confidential data unredacted → never enters AI.

合同 / 法律文件需要翻译时：
For contracts / legal docs:
- 用**专业法务翻译服务**（签 NDA 的）
- 不要图省事用 AI

### 不要让 AI 用"客户面文案口径"翻译内部文档

```
内部 PRD 翻译给海外团队：可以让 AI 译，但译完后还是内部文档，可以保留 PRD 编号 / 内部代号
内部 PRD 翻译为给客户看的：必须重新按红线 #2 处理（去除内部信息）
```

---

## 速查 / Cheat Sheet

```
8 步：受众 → 术语表 → AI 初稿 → 自查典型错 → 人审 → 非翻译调整 → 技术检查 → 发布监控

类型策略：
- UI 文案：AI 起稿 + 人审本地化
- 邮件 / 销售：AI 起草后人重写
- 视频字幕：AI 听写初译 + 字数控制
- 合同：AI 不做（仅术语对照）

陷阱：直译习语 / 翻译腔 / 数字日期格式 / UI 字符串膨胀 / 文化语义

红线：合同不让 AI 译；客户数据不送 AI；客户面文案过红线 #2
```
