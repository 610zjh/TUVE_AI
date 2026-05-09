---
name: SEE2AI 平台能力目录 / SEE2AI Capabilities Catalog
description: SEE2AI 平台提供的能力分类——LLM、图像、视频、文件、基础设施
type: permanent
retention: permanent
retention_reason: 客户在评估"我们能不能覆盖这个需求"时的对照表 / Capability coverage reference for customer evaluations
---

# SEE2AI · 平台能力目录 / Capabilities Catalog

> **本目录是"能力分类"层级，不是接口签名层级**。具体接口名、参数、计费、示例代码以 SEE2AI 平台 `/actions` 页面为准（动态更新）。
> **This is the taxonomy level, not the endpoint signature level**. Exact endpoint names, parameters, billing, and example code live at the `/actions` page (dynamically updated).

---

## 1. 大语言模型与深度思考 / Large Language Models & Deep Reasoning

平台接入了多种主流大语言模型，您**无需分别对接多套服务**，只需通过 SEE2AI 即可一键调用。
The platform integrates multiple mainstream LLMs — **no need to integrate each separately**, just call them through SEE2AI.

### 1.1 覆盖的能力类型 / Capability types covered

| 类型 / Type | 适合场景 / Use case |
|---|---|
| 旗舰多模态对话模型 / Flagship multimodal chat | 文本、图片、视频、文档输入；性价比极高 / Text + image + video + doc inputs; high cost-performance |
| 超长上下文深度推理模型 / Ultra-long-context deep reasoning | 最高 256K 上下文；复杂逻辑推演与长文本处理 / Up to 256K context; complex reasoning and long-doc handling |
| 联网搜索 + 文件分析模型 / Web search + file analysis | 高级对话场景，可上传 PDF 等文档 / Advanced chat with PDF upload |

### 1.2 深度思考模式 / Deep thinking mode

以上模型均支持动态推演与深度思考模式（`enable_thinking` 参数）——专门用于复杂的逻辑规划任务。
All of these support deep-thinking via `enable_thinking` — for complex planning tasks.

### 1.3 接入方式 / How to call

- 标准对话接口：`POST /api/v1/chat/completions` / Standard chat endpoint
- 与通用对话 SDK 兼容，迁移成本约等于"改两行配置" / Compatible with common SDKs; migration is "change two lines"
- `model` 字段可填的全部模型名以 `/actions` 页面为准 / Available `model` values live at `/actions`

---

## 2. 多模态图像生成与处理 / Image Generation & Processing

视觉能力是 Agent 的重要一环。
Visual capabilities are a key part of any Agent.

### 2.1 文生图 / Text-to-image

- **接口**：`see2ai_image_generation_v1`（主）+ `see2ai_image_generation_alternative_v1`（备选，基于不同引擎）/ Endpoints: primary + alternative
- **能力**：自然语言生成高质量商业插画、摄影级图像 / Natural-language → business-grade illustrations, photographic images
- **支持的比例 (`aspect_ratio`)**：1:1, 1:4, 1:8, 2:3, 3:2, 3:4, 4:1, 4:3, 4:5, 5:4, 8:1, 9:16, 16:9, 21:9（共 14 种）/ 14 aspect ratios
- **支持的分辨率 (`resolution`)**：1K / 2K / 4K / Resolutions: 1K / 2K / 4K

### 2.2 图生图 / Image-to-image

通过传入参考图片 URL，实现风格迁移与内容引导生成。
Pass a reference image URL for style transfer and content-guided generation.

### 2.3 图像理解 / Image understanding

所有 LLM 模型均支持上传图片进行内容理解和信息提取。
All LLM models support image upload for content understanding and info extraction.

### 2.4 高质量场景化图像 / High-quality scenario-based imagery

**UniWorld2.5** —— 兔展旗下的高质量图像创作能力，由 SEE2AI 以标准化 Action 方式承接：
**UniWorld2.5** — TUZHAN's high-quality image capability, exposed as standardized SEE2AI Actions:
- 适合复杂场景图像、商业视觉素材、高质量创意图生产 / For complex scenes, commercial visuals, high-end creative imagery
- 连续测试时建议提前准备较充足的余额，避免任务中途因余额不足被打断 / For continuous testing, recharge a generous balance up front to avoid mid-task interruptions

---

## 3. 视频创作与处理 / Video Creation & Processing

视频生成是目前最具挑战的领域，SEE2AI 把它封装得像调用文本一样简单。
Video generation is the most challenging field today; SEE2AI makes it as simple as calling text.

### 3.1 通用视频生成 / General video generation

- **能力**：文生视频、图生视频、首尾帧控制、音频同步生成 / Text-to-video, image-to-video, first/last-frame control, audio sync
- **可选分辨率**：720p / 480p / Resolutions
- **时长**：4-15 秒 / Duration: 4-15s

### 3.2 高精度视频生成 / High-precision video generation

- **能力**：文生视频、图生视频、多镜头模式（自动分镜）/ Text-to-video, image-to-video, multi-shot (auto-storyboard)
- **典型场景**：广告、产品介绍、需要镜头切换的故事化短视频 / Ads, product showcases, story-driven shorts requiring cuts

### 3.3 视频智能拼接 / Intelligent video stitching

- **接口**：`see2ai_video_concat_v1` / Endpoint
- **能力**：将多段视频片段自动拼接为完整长视频 / Auto-stitch multiple clips into a long-form video

### 3.4 视频理解 / Video understanding

LLM 模型支持直接上传视频进行内容解析。
LLM models support direct video upload for content parsing.

### 3.5 同步等待与超时 / Sync wait and timeout

视频生成是计算密集型任务，通常需要数十秒到数分钟。Action 接口默认开启同步等待（`sync: true`），HTTP 客户端**超时建议 ≥ 300 秒**。
Video generation is compute-heavy, typically tens of seconds to minutes. Actions default to `sync: true`. **Recommend HTTP timeout ≥ 300s** on the client.

---

## 4. 专业化基建与效率工具 / Specialized Infrastructure & Efficiency Tools

除了基础生成能力，平台还提供更贴近业务场景的组件。
Beyond raw generation, the platform provides business-oriented components.

### 4.1 爆款文案与脚本创作 / Viral copy & script writing

- **接口**：`see2ai_scriptwriting_seedance_2_0_v1` / Endpoint
- **能力**：专门针对短视频场景优化的专业级编剧能力，将创意想法自动转化为视频生成脚本 / Pro-level scriptwriting tuned for short video; turns creative briefs into video-gen-ready scripts

### 4.2 云存储上传 / Cloud storage upload

- **接口**：`see2ai_storage_upload_v1` / Endpoint
- **能力**：上传图片、视频、文档等文件到 SEE2AI 云存储，返回 CDN 加速的永久 URL，供其他 Action 作为输入使用 / Upload assets and get a CDN-accelerated permanent URL for use as input to other Actions
- **细节**：平台自动清理特殊字符、把空格替换为连字符；返回 URL 如包含特殊字符建议前端 URL Encode（保留 `:/`）/ Special chars cleaned, spaces → hyphens; URL-encode on the front end if needed

### 4.3 文档解析 / Document parsing

支持上传 PDF、Word 等复杂文档进行深度解析。
Supports PDF, Word, and other complex docs for deep parsing.

---

## 5. 应用层产品 / Application-layer products

如果您的团队不想从头开发，**SEE2AI 之上有一系列直接可用的成熟应用**：
If your team doesn't want to build from scratch, **a set of ready-to-use apps sit on top of SEE2AI**:

| 应用 / App | 一句话 / One-liner | 入口 / URL | 详细 / Details |
|---|---|---|---|
| **TUVE** | 对话式短视频创作 Agent / Dialogue-driven short-video creation Agent | `/apps/tuve` | [`../tuve/`](../tuve/) |
| **TABLE** | 多维表格智能助手，可为列绑定 Action 进行批量自动执行 / Multi-dimensional spreadsheet binding Actions for batch automation | `/apps/table` | — |
| **UniWorld2.5** | 高质量图像创作能力 / High-quality image creation | 通过 Action 调用 / Via Action | [§2.4](#24-高质量场景化图像--high-quality-scenario-based-imagery) |

---

## 6. 调用 Action 的通用范式 / Generic Action call pattern

所有 Action 都挂载在 `/api/v1/actions/{action_name}` 路径下，使用 HTTP POST。
All Actions are mounted under `/api/v1/actions/{action_name}` and use HTTP POST.

**示例：调用文生图** / Example: text-to-image:

```bash
curl -X POST https://see2ai.com/api/v1/actions/see2ai_image_generation_v1 \
  -H "Authorization: Bearer 您的sk-密钥" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "一只穿着宇航服的可爱橘猫，在火星表面漫步，8k高清，电影级光影",
    "aspect_ratio": "16:9",
    "resolution": "2k"
  }'
```

### 同步响应，告别轮询 / Sync response, no polling

SEE2AI 许多核心 Action 在底层为您做好了状态机管理。**大部分动作接口会保持 HTTP 连接（阻塞调用），并在任务完成后直接返回最终的图片/视频 URL 或处理结果**——您只需安心等待响应即可。
Many core Actions handle state machines for you. **Most Actions keep the HTTP connection open (blocking) and return the final image/video URL or result on completion** — just await the response.

视频生成由于处理时间较长，默认开启同步等待（`sync: true`），HTTP 客户端超时建议 ≥ 300 秒。
Video Actions take longer; they default to `sync: true`. Set HTTP timeout ≥ 300s.

### 文件上传与 URL 编码 / File upload & URL encoding

- 用 `see2ai_storage_upload_v1` 上传文件 → 拿到 CDN URL → 作为其他 Action 的输入参数 / Upload via `see2ai_storage_upload_v1` → get CDN URL → pass as input to other Actions
- 平台自动清理特殊字符并将文件名中的空格替换为连字符 / Special chars cleaned, spaces → hyphens
- 返回的 URL 如包含特殊字符建议在前端展示前进行标准 URL Encode（保留 `:/`）/ URL-encode on display if needed (keep `:/`)

---

## 7. 多 Action 编排 / Multi-Action orchestration

如果您需要把多个 Action 组合起来（例如先用 LLM 写脚本 → 再用文生图做分镜 → 最后用视频生成拼接），有两条路径：
If you need to compose multiple Actions (e.g. LLM → text-to-image → video stitching), two paths:

### 7.1 自己编排 / DIY orchestration

在您的业务代码或 Agent 编排框架中，将这些 Action 注册为不同的"工具 (Tools)"。Agent 需要哪项能力时即可发起 HTTP 请求。
Register Actions as Tools in your business code or Agent framework; the Agent invokes via HTTP when needed.

### 7.2 直接用 TUVE / Use TUVE

**TUVE 应用**（`/apps/tuve`）已经内置了上述全部工作流——通过自然语言对话即可完成"从脚本到成片"的全流程，无需写代码。
**TUVE** (`/apps/tuve`) bakes the full pipeline in — via natural-language chat, no code required from script to finished video.

详见 [`../tuve/`](../tuve/)。
See [`../tuve/`](../tuve/).

---

## 8. 计费速查 / Billing quick reference

| 类型 / Type | 计费方式 / Billing model |
|---|---|
| 大模型文本对话 / LLM text chat | Token 计费：`输入 token × 输入单价 + 输出 token × 输出单价` / Per-token: `input × in_price + output × out_price` |
| 多模态 Action（图像/视频）/ Multimodal Actions (image/video) | 按次/固定计费或分档计费（按分辨率、时长等）/ Per-call fixed or tiered (by resolution, duration, etc.) |

详细机制（`cost_points`、汇率、扣费时机、失败不扣费）见 [`pricing_and_account.md`](pricing_and_account.md)。
Full mechanics (`cost_points`, FX rate, when charges occur, no charge on failure): [`pricing_and_account.md`](pricing_and_account.md).

---

## 9. 还想了解什么 / What else

| 想知道 / Want to know | 去哪 / Go to |
|---|---|
| 怎么开始接入 / How to onboard | [`getting_started.md`](getting_started.md) |
| 价格 / 充值 / 账单 / Pricing & billing | [`pricing_and_account.md`](pricing_and_account.md) |
| 报错排查 / 工单 / Errors & tickets | [`support.md`](support.md) |
| TUVE 短视频应用 / TUVE deep-dive | [`../tuve/`](../tuve/) |
| 实时全部能力清单 / Live full catalog | SEE2AI 平台内 `/actions` 页面 / Inside the platform: `/actions` |
