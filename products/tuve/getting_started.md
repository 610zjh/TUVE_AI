---
name: TUVE 新手快速起步 / TUVE Getting Started
description: 5 分钟做出第一支 TUVE 短视频——从注册 SEE2AI 到出片完整路径，含对话开场白模板和高质量 Prompt 写法
type: permanent
retention: permanent
retention_reason: 客户首次使用 TUVE 的 SOP；最常分享的"上手"页面 / SOP for first-time TUVE use; most-shared onboarding page
---

# TUVE · 新手快速起步 / Getting Started

> 这一份给"准备做第一支 TUVE 短视频"的用户。语气鼓励，目标是 **5 分钟内拿到一支可下载的成片**。
> For users about to make their first TUVE video. Tone: encouraging. Goal: **a downloadable finished video within 5 minutes**.

---

## 准备工作 / Prerequisites

TUVE 是 SEE2AI 平台之上的应用，所以使用 TUVE 需要先有 SEE2AI 租户账号 + 余额。
TUVE is an app on the SEE2AI platform, so you need a SEE2AI tenant account + balance first.

如果还没有：先按 [`../see2ai/getting_started.md`](../see2ai/getting_started.md) 完成：
If you don't yet, first complete [`../see2ai/getting_started.md`](../see2ai/getting_started.md):

1. ✅ 注册并登录租户账号 / Sign up and log in
2. ✅ 完成充值。TUVE 视频生成是计算密集型任务，建议提前一次性准备较充足的余额，具体金额可参考 `/tenant/recharge` 页面当前展示的档位建议或结合 `/actions` 页面的单价评估 / Complete recharge. TUVE video generation is compute-heavy — recharge a generous balance up front; refer to the tier suggestions on `/tenant/recharge` or estimate from per-call prices on `/actions`

> 💡 第一次试用 TUVE 不需要 API Key——TUVE 是浏览器内的可视化应用，登录账号即可。API Key 是给"代码集成"准备的。
> 💡 First-time TUVE use doesn't need an API key — TUVE is a browser-based visual app; just log in. API keys are for code integration.

---

## 第一步：进入 TUVE 工作台 / Step 1 — Enter the TUVE workbench

1. 浏览器登录您的 SEE2AI 租户账号 / Log in to SEE2AI in your browser
2. 访问 `/apps/tuve` / Visit `/apps/tuve`
3. 您会看到 TUVE 的主工作台：左侧是对话框（Chat），右侧是任务面板和媒体引用区 / You'll see the TUVE workbench: left = chat, right = task rail + media reference area

> 💡 推荐使用最新版 Chrome 或 Edge 浏览器，TUVE 使用 WebSocket 进行实时通信。
> 💡 Use the latest Chrome or Edge — TUVE uses WebSocket for real-time communication.

---

## 第二步：在对话框告诉 TUVE 您想要什么 / Step 2 — Tell TUVE what you want

打开对话框，发第一条消息。下面是 4 个推荐的开场白模板。
Open chat and send your first message. Here are 4 recommended opener templates.

### 模板 A：自媒体作者 / Solo creator

> "我想做一支 30 秒的短视频，主题是远程办公的 5 个隐形成本。风格要轻松、节奏明快，适合发到短视频平台。请先帮我出脚本草稿，我看完再让你继续做下一步。"
> "I want a 30s short on the 5 hidden costs of remote work. Tone light, pacing snappy, formatted for short-video platforms. Draft the script first; I'll review before you proceed."

### 模板 B：电商商详 / E-commerce detail page

> "给一款新出的便携咖啡机做一支 15 秒商详页短视频。卖点：便携、静音、3 分钟出咖啡。视觉风格要日系明亮，节奏紧凑，最后 2 秒留出来给品牌 logo。"
> "15s product-detail video for a new portable coffee machine. Selling points: portable, silent, coffee in 3 minutes. Bright Japanese style, tight pacing, last 2s for brand logo."

### 模板 C：知识付费课程 / Knowledge content

> "我把一篇 800 字的图文课件粘贴在下面，请帮我把它压缩成一支 60 秒的短视频脚本，保留 3 个核心观点，配上对应的视觉素材建议。"
> "I'm pasting an 800-word lesson below — compress it into a 60s short-video script with 3 core points and matching visual suggestions."

### 模板 D：品牌方持续内容 / Brand continuous content

> "请用我们品牌的标准模板做一支 20 秒短视频。这次的主题是「夏季新品上市」，要突出清爽和冰凉感。如果之前我们存过模板，请直接复用。"
> "Make a 20s video using our brand's standard template. Theme: 'summer new arrival' — highlight crispness and coolness. Reuse a template if we've saved one."

---

## 第三步：跟 TUVE 协作 / Step 3 — Collaborate with TUVE

TUVE 不是"按一次按钮全部产出"——它是 Agent，会一步步执行并在关键节点暂停等您确认。
TUVE isn't "press once, get everything" — it's an Agent that executes step by step, pausing at key gates for your confirmation.

### 3.1 典型流程 / Typical flow

```
您发主题 → TUVE 出脚本草稿 → 您调整 → TUVE 生成分镜图 → 您勾选/调整 → TUVE 合成视频片段 → 您预览 → TUVE 拼接成片 → 您下载
You send topic → TUVE drafts script → you adjust → TUVE generates storyboard → you select/adjust → TUVE synthesizes clips → you preview → TUVE stitches → you download
```

每一步 TUVE 都会在对话里给您看进度，您可以直接说话调整：
At each step TUVE shows progress in chat; just talk to adjust:

- "第二个镜头改成俯拍" / "Change shot 2 to top-down"
- "脚本第三段太长了，砍掉一半" / "Script paragraph 3 is too long, cut by half"
- "整体配色再暖一点" / "Warmer overall palette"
- "重新生成第一支视频片段，这次镜头多一些近景" / "Regenerate clip 1 — more close-ups this time"

### 3.2 高质量 Prompt 的 4 个要素 / 4 elements of a high-quality prompt

把这 4 件事写清楚，TUVE 出片的质量明显更高：
Spell out these 4 things and TUVE's quality jumps:

1. **时长**：你想要多少秒？/ **Duration**: how many seconds?
2. **风格**：日系明亮 / 复古胶片 / 电影级 / 清新简约 / 高对比赛博朋克...... / **Style**: Japanese bright / vintage film / cinematic / minimalist / cyberpunk high-contrast...
3. **节奏与情绪**：紧凑/舒缓、活力/沉稳、欢快/严肃 / **Pacing & mood**: tight/relaxed, energetic/calm, cheerful/serious
4. **核心信息 + 必须保留的元素**：哪几句话必须出现？哪个产品/logo/人物必须入镜？ / **Core message + must-keep elements**: which sentences must appear? which product/logo/person must be on screen?

模糊 prompt 例 / Vague prompt:
> "做个咖啡机的视频" / "Make a coffee machine video"

清晰 prompt 例 / Clear prompt:
> "30 秒、日系明亮风、节奏紧凑、突出便携和静音。最后 2 秒打 logo，文字"3 分钟一杯好咖啡"必须出现。"
> "30s, bright Japanese style, tight pacing, highlight portable + silent. Last 2s logo card with text 'A great coffee in 3 minutes' that must appear."

---

## 第四步：调整与导出 / Step 4 — Adjust and export

### 4.1 在对话里调整任何环节 / Adjust any step via chat

视频拼接成片之后，您仍然可以通过对话调整：
After the final stitch, you can still adjust via chat:

- "把第一个镜头剪短到 2 秒" / "Trim shot 1 to 2 seconds"
- "整段配音换成女声" / "Switch the VO to a female voice"
- "结尾再加一段品牌口号" / "Add a brand tagline at the end"

### 4.2 下载成片 / Download

成片在媒体引用区显示。点击下载图标即可保存到本地。
The finished video appears in the media reference area. Click the download icon to save locally.

---

## 常见卡点 / Common stuck points

### Q1: 我说了想要的风格，TUVE 出来的不对 / TUVE's output doesn't match my style

- **更具体地描述风格**：不只说"日系明亮"，可以加"参考无印良品的视觉，柔和漫反射光、低饱和、暖色调" / Describe more concretely: not just "Japanese bright" but "reference Muji visuals — soft diffused light, low saturation, warm tones"
- **给参考素材**：把您喜欢的图片/视频上传到对话框作为参考 / Upload reference assets to chat
- **逐步收敛**：先让 TUVE 出 3 个候选风格，您选最接近的，再让它在那个基础上细化 / Iterate: ask TUVE for 3 candidates, pick the closest, then refine

### Q2: 视频生成等了很久 / Video generation is slow

视频生成是计算密集型任务，单段 4-15 秒视频通常需要数十秒到数分钟。
Video generation is compute-heavy; a single 4-15s clip typically takes tens of seconds to minutes.

- **不要刷新页面**：刷新会丢失当前对话的中间状态。改成切换到其他浏览器 Tab 等待 / **Don't refresh** — that loses intermediate state. Switch to another tab and wait
- **如果连接中断**（弹"WebSocket 断开"提示）→ 刷新即可重连，**历史对话和已完成步骤不会丢失** / If connection drops → refresh to reconnect; **history and completed steps preserved**

### Q3: 余额不够中途被打断 / Balance ran out mid-task

TUVE 的视频生成会根据时长和模型扣费。如果您准备做多支视频或反复迭代，建议余额充足后再开始。
TUVE video generation charges by duration and model. For multi-video sessions or heavy iteration, recharge first.

- 计划连续多轮迭代时建议提前准备较充足的余额，具体金额参考 `/tenant/recharge` 页面当前展示的档位建议或结合 `/actions` 页面的单价评估 / If you plan sustained iteration, recharge a generous balance up front; refer to the tier suggestions on `/tenant/recharge` or estimate from per-call prices on `/actions`
- 详细计费规则见 [`../see2ai/pricing_and_account.md`](../see2ai/pricing_and_account.md) / Full pricing: [`../see2ai/pricing_and_account.md`](../see2ai/pricing_and_account.md)

### Q4: TUVE 拒绝执行某些指令 / TUVE refuses certain requests

TUVE 是面向商业级短视频创作的工具，遵守平台内容规范——以下场景会拒绝执行：
TUVE is built for commercial short-video creation and follows platform content rules. It will refuse:
- 涉及未成年人不当内容 / Inappropriate content involving minors
- 暴力、血腥、明确违法内容 / Violent / gory / explicitly illegal content
- 仿冒已知品牌或公众人物 / Impersonating known brands or public figures
- 政治敏感、宗教煽动、歧视性内容 / Political / religious incitement / discriminatory content

如果您的合理使用场景被误判拒绝，请通过 `/backlog` 提交工单说明使用场景，我们会人工核实。
If a legitimate scenario is misjudged, file a ticket at `/backlog` describing the use case for human review.

---

## 下一步去哪 / Where to go next

| 想知道 / Want to know | 去哪 / Go to |
|---|---|
| TUVE 还能做什么 / What else TUVE can do | [`capabilities.md`](capabilities.md) |
| 出问题怎么办 / 找人工 / Issues / human support | [`support.md`](support.md) |
| 计费 / 充值 / 账单 / Billing / recharge / bills | [`../see2ai/pricing_and_account.md`](../see2ai/pricing_and_account.md) |
| 想给自己的应用接入 SEE2AI 能力 / Integrate SEE2AI capabilities into your own app | [`../see2ai/getting_started.md`](../see2ai/getting_started.md) |
