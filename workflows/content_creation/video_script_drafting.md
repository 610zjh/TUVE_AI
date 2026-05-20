# 短视频脚本起草 / Short-Video Script Drafting

> 适用：视频制作、运营、营销在写 30-90 秒短视频脚本时。
> For: video / ops / marketing drafting 30-90 second short-video scripts.

---

## 一句话 / One Line

**短视频脚本的成败在前 3 秒。** AI 帮你把"勾住"做成机械流程。
**Short-video success or failure happens in the first 3 seconds.** AI turns "hooking" into a mechanical process.

---

## 一份完整脚本的结构 / Standard Script Structure

```
[0:00-0:03] 钩子 / Hook —— 一句话让观众停下不划走
[0:03-0:10] 设景 / Setup —— 这件事和观众有什么关系
[0:10-0:50] 内容主体 / Body —— 1-3 个具体点，配画面 / 字幕 / 演示
[0:50-0:55] 反转或顿悟 / Twist or Aha —— 给观众一个值得记住的点
[0:55-end] 召唤 / CTA —— 关注 / 点赞 / 看下一支
```

不是每支视频都需要 5 段都做；30 秒视频可能只有钩子 + 主体 + CTA。
Not every video needs all 5 sections; 30s might just be Hook + Body + CTA.

---

## 用 AI 起草的 5 步 / 5 Steps with AI

### 步 1：定主题 + 观众 / Step 1: Topic + Audience

```
我要写一支短视频脚本。
- 主题：[一句话]
- 观众：[谁、几岁、什么平台、什么时候看（地铁通勤？睡前？）]
- 时长：[X 秒]
- 平台：[抖音 / 小红书 / B 站 / 视频号 / 多平台]
- 我们的发布账号定位：[官方专业 / 个人 IP / 产品演示]

请帮我列：
- 5 个候选钩子（前 3 秒能说的"让人停下来"的话）
- 每个钩子对应的视频走向
- 每个钩子的"如果观众不喜欢这种风格"的退路
```

### 步 2：挑钩子 + 起脚本 / Step 2: Pick Hook + Draft

```
我选钩子 [X]。请基于这个钩子起一份完整脚本：

格式：每行一个镜头
[时间] | [画面描述] | [字幕 / 旁白]

约束：
- 总时长 [X 秒]，每个镜头 ≤ 3 秒
- 字幕单行 ≤ 12 字
- 不出现具体客户名 / PRD 编号 / 内部代号（红线 #2）
- 不引用未发布的功能 / 未开放的价格
```

### 步 3：拍摄前的"内部词清单" 检查 / Step 3: Internal-Word Blocklist Check

短视频字幕里出现内部代号 / 客户名后果严重（参考 [`templates/video_script/internal_words_blocklist.md`](../../templates/video_script/internal_words_blocklist.md)）。
Internal codes / customer names in subtitles have serious consequences.

```
请扫一遍上面的脚本：
- 是否出现 PRD-XXXX、Bug-XXXX 这类编号？
- 是否出现具体客户名（除了 TUZHAN 自己）？
- 是否出现"内部""运维""项目代号"等暴露内部分工的词？
- 是否出现具体合同金额、内部成本、销售管线？
- 是否出现模型 endpoint、API 路径？

如果有，列出来 + 给替代方案。
```

### 步 4：A/B 候选 / Step 4: A/B Candidates

```
基于上面的脚本，再起 2 个变体：
- 变体 A：偏紧凑（节奏更快、信息密度更高）
- 变体 B：偏故事（用一个具体场景导入）

我会从 3 个里挑一个再深化。
```

### 步 5：拍摄 + 后期注释 / Step 5: Production + Post Notes

```
基于最终选定的脚本，列：
- 拍摄要点（场景 / 演员表情关键时刻 / 镜头切换）
- 后期要点（字幕样式 / BGM 类型 / 哪一段需要特效）
- 需要准备的物料（道具 / 背景 / 屏幕截图）
- 拍摄时段建议（自然光？需要打光？）
```

---

## 红线提醒 / Red Line Reminders

### 涉及客户案例的脚本 / Scripts Citing Customer Cases

❌ **错误**：
> "我们刚帮 XX 教育公司把内容产出从每周 50 条提升到每周 500 条。"
（点名客户 + 具体数字 → 客户合同条款 + 红线 #2 双重违规）

✅ **正确**：
> "我们的客户用了我们的工具后，内容产出能力实现了 10 倍增长。"
（行业 + 倍数表述 + 不点名）

### 涉及"我们正在做"的承诺 / "We're Working On" Promises

短视频在网上的留存远超你的预期。3 个月后视频还在线，但里面承诺的功能黄了 → 客户截图发出来"你们当时说的呢"。
Videos persist online way longer than you expect. A 3-month-old video promising X — feature dropped, customer screenshots and quotes you publicly.

❌ "下个月我们会上线 [功能]！"
✅ "我们正在打磨一项新能力，敬请期待。"（模糊到不构成承诺）

或者：发布该功能上线**当天**才发推广视频。
Or: release the promo video the same day the feature ships.

---

## 真实人物 / 客户授权 / Real Person / Customer Authorization

视频里出现 / 提及的真实人物（员工 / 客户 / 合作伙伴）必须：
Real people appearing / mentioned in videos must:

- ✅ 有书面同意（邮件、签字、明确的微信回复都算）
  Have written consent
- ✅ 同意范围清晰（在哪些平台用、用多久、能不能再剪辑）
  Consent scope clear (which platforms, how long, re-edit OK?)
- ✅ 同意书存到 [`meetings/`](../../meetings/) 下
  Consents archived

未授权的客户 logo / 真实街景里的路人 / 未授权的音乐 → 都是法律风险。
Unauthorized customer logos / passersby in shots / unauthorized music → legal risks.

---

## 数据 / 案例的依据 / Data and Case Backing

视频里出现"提升 47%"、"3 倍效率"等数字时：
When videos feature "47% improvement" / "3× efficiency":

- 数字来源记录在拍摄笔记里 / Source recorded in shooting notes
- 统计口径记录（哪些客户、什么时间段、什么基线）/ Methodology recorded
- 法务过审（如果是承诺性数字）/ Legal review for promissory numbers

未来被客户 / 监管 / 媒体追问时拿得出依据。
So you can produce evidence when challenged by customers / regulators / media.

---

## 多平台改编 / Multi-Platform Adaptation

同一个核心脚本要发多平台时：
When repurposing one core script across platforms:

| 平台 / Platform | 时长 / Duration | 调整重点 / Key adjustment |
|---|---|---|
| 抖音 / Douyin | 15-60s | 快节奏、视觉密集、强 CTA |
| 小红书 / Xiaohongshu | 30-90s | 偏个人分享、字幕重要 |
| B 站 / Bilibili | 1-5min | 更可以信息密集、容许深度 |
| 视频号 / WeChat Video | 30-90s | 偏专业 / 信任向 |
| YouTube Shorts | 15-60s | 国际化语境（如有英文版本）|

不要"一稿打天下"——同一份核心，3-5 个平台版本各自微调。
Don't "one-fits-all" — same core, 3-5 platform-tuned versions.

---

## A/B 测试纪律 / A/B Test Discipline

短视频领域 A/B 测在前 24-48 小时数据反馈快。但：
Short-video A/B feedback is fast (24-48h). But:

- A/B 测试期间的视频**不要拿去公开发布做大推广**——结果可能反向 / During A/B don't push hard externally; result may flip
- 数据样本 < 1000 次播放时不要下结论 / Sample < 1000 views, no conclusion
- 多个变量同时改的 A/B 是无效的（你不知道哪个变量起作用）/ Multi-variable A/B is invalid

---

## 速查 / Cheat Sheet

```
结构：钩子（前 3s）/ 设景 / 主体 / 反转 / CTA

5 步法：定主题观众 → AI 给 5 个钩子 → 选钩子起脚本 → 内部词清单检查 → A/B 变体 → 拍摄 / 后期

红线：不点名客户 / 不承诺未发布 / 数字有依据 / 真人有授权 / 内部代号绝禁

不要：A/B 期间大推；多变量同时改 A/B；< 1000 播放下结论
```
