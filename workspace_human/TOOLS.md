# TOOLS.md — OpenClaw 工具环境与技能目录

## 🔥 Seedance 2.0 核心能力速查表（主模型必读）

> **⚠️ 此速查表是主模型在处理任何视频相关任务时的第一参考。严禁凭记忆或过时信息做能力判断。**

| 维度 | 能力描述 |
|---|---|
| **模型定位** | Seedance 2.0 及其 Fast 版本是具备深度多模态理解与生成能力的顶级视频大模型。视频创作、视频编辑、音画同步生成或真人出镜视频需求，应**优先**考虑调用此能力。 |
| **多模态混合输入** | 支持同时接受文本（Text）、图像（Image，首尾帧/角色参考）、视频（Video，镜头语言/动作参考）、音频（Audio，背景/驱动）作为输入参数。 |
| **基础生成（T2V & I2V）** | 高质量文生视频、单图生视频（首帧驱动）、双图生视频（首尾帧插帧）。有效时长 4-15 秒。 |
| **写实级真人视频** | 利用用户上传的真人图像/视频资产，生成带有指定人物面部特征的视频。**有参考素材时直接推进，严禁拒绝。** |
| **音画同生** | 支持 `generate_audio` 参数，原生生成与画面同步的人声、环境音和背景音乐；**严禁建议用户关闭音频。** |
| **解耦式多模态控制** | 支持"解耦拼装"式生成：图片 A 定义人物特征 + 视频 B 定义镜头运镜 + 音频 C 作为背景音乐。 |
| **视频编辑** | 保持原视频镜头运动不变，精确替换视频中的指定物体。 |
| **视频延长** | 基于已有视频片段进行叙事连贯的向后延长生成。 |

**🚫 严禁的错误认知**：
- ❌ "带旁白太复杂了，建议先关闭音频"
- ❌ "AI 无法生成真人脸，建议改用卡通风格"
- ❌ "多镜头保持一致很难"

---

### 🛑 视频生成口径（Pre-Plan 门卫，2026-04-26 起）

**铁则**：视频生成走 PRD-0103 guided repair 契约。主模型必须按下列规则**先做关键词扫描 + 模式裁决**，再下发请求；违规时 Action 返回 `state=needs_repair`，主模型必须停手等用户决定，**绝对不能自动重试**。

#### 字段唯一入口

- **图片**：`first_frame_url` / `last_frame_url` / `reference_image_url` / `reference_image_urls`
- **视频**：`video_url` / `video_urls`
- **音频**：`audio_url` / `audio_urls`
- **可选人脸 hint**：`first_frame_contains_real_face` / `last_frame_contains_real_face` / `reference_image_contains_real_face`（`true` / `false`；不传 = 服务端自动识别）

> 旧字段 `face_image_url` / `non_face_image_url(s)` / `face` / `portrait` 等已**整体下线**，传入会被脚本端硬拒；禁止再产出。

#### 模式硬规则（违反 → needs_repair）

- 「首尾帧模式」：仅 `first_frame_url`（可加 `last_frame_url`），**禁止**混入 `reference_image_url(s)` / `video_url(s)` / `audio_url(s)`
- 「全能参考模式」：`reference_image_url(s)` / `video_url(s)` / `audio_url(s)` 任意组合，**禁止**出现 `first_frame_url` / `last_frame_url`
- 这两种模式**不能在一份分镜里混用**——如果同时想要"首帧锁定"和"风格参考"，请收敛到全能参考模式（首帧用 `reference_image_url`，prompt 里写"@图1 作为首帧"）
- 音频不可孤悬：传 `audio_url(s)` 必须有 ≥1 张参考图或 ≥1 段参考视频
- `last_frame_url` 不能脱离 `first_frame_url` 单独存在
- 数量上限：图 ≤ 9 / 视频 ≤ 3 / 音频 ≤ 3 / 单镜头总素材 ≤ 12
- 单参数：`duration` ∈ [4,15] 或 -1；`resolution` ∈ {480p,720p,1080p}；`aspect_ratio` ∈ {adaptive,16:9,9:16,1:1,21:9,4:3,3:4}

#### 触发扫描（主模型在任何"规划/确认"回复之前，必须先做一次关键词扫描）

- **首帧桶**：首帧 / 头帧 / 起始帧 / 开头帧 / start frame / first frame / "图 X 作首帧" / "第一张当开头"
- **尾帧桶**：尾帧 / 末帧 / 结束帧 / 结尾帧 / end frame / last frame / "图 X 作尾帧" / "最后一张当结尾"
- **参考桶**：参考图 / 参考 / 参照 / 风格参考 / 风格图 / 打底图 / 模板图 / 视觉锚点 / reference / "图 X 作参考"

扫描结果落入两桶以上 → **必须停下来与用户确认走哪一种模式**，不要按"既然都提了就都塞进去"的思路下发请求。

#### needs_repair 消费纪律（强制）

视频生成脚本退出码 = 2 时，Action 已返回完整的修复指引（含候选改法 / 可执行 patch / 最小可运行示例 / 双轨文案）。主模型必须：

1. 把 stderr `[👤 给用户的话]` 块**原样转给用户**
2. 把 `[🔀 候选改法]` 列出 A/B/C 让用户**明确选**
3. **绝对不能自动重试 / 不能静默套用 `payload_patch_plan` / 不能用 `minimal_runnable_payload` 偷偷换用户意图**
4. 用户选定后回到 Stage 2 修订分镜脚本，再走 Stage 4

**⚡ 全自动省心模式例外**（详见 `AGENTS.md` 模式二）：
在全自动模式下，上述第 1-3 条纪律调整为：agent 可**自动选择最合理的候选方案**并重试 1 次；若重试后仍 needs_repair，则停止全自动模式，退回先审后发模式，按上述第 1-4 条正常执行。自动重试上限：**最多 1 次**。

> 完整能力详情、字段说明、needs_repair 消费规范 → 详见 `openclaw_skills/see2ai_video_generation/SKILL.md`
> 全量错误穷举（A–O 类，60+ 条目）→ 详见 SEE2AI 项目 `workspace_human/prd/0103_video_generation_error_taxonomy.md`

---

## 🖼️ 图片生成 Skill 路由索引

- `see2ai_text_to_image`：普通文生图入口，适合插画、场景图、氛围图、视频配图、产品展示图等“画面视觉优先”的需求；显式 `backend=fast` 可走快速图片 Action。遇到多文字、多语种、强版式、详情页视觉、结构说明图、PPT 单页视觉时不要用它。→ 详见 `openclaw_skills/see2ai_text_to_image/SKILL.md`
- `see2ai_text_to_image_uniworld`：排版文生图入口，适合详情页视觉、手机网页图、杂志或封面版式、结构介绍图、时间线图、知识脉络图、PPT 单页视觉等“文字排版和信息组织优先”的需求。→ 详见 `openclaw_skills/see2ai_text_to_image_uniworld/SKILL.md`
- `see2ai_image_to_image`：图生图入口，适合用户已经提供商品图、产品图、人物图或其他参考图，再基于该图片继续生成或改图；显式 `backend=fast` 可走快速参考图生成 Action。→ 详见 `openclaw_skills/see2ai_image_to_image/SKILL.md`
- `see2ai_image_normalize`：图片标准化入口，适合在调用人脸检测、视觉理解、视频生成或图像生成前，把不稳定公网图片 URL 转成更适合下游供应商读取的 SEE2AI 托管 URL。→ 详见 `openclaw_skills/see2ai_image_normalize/SKILL.md`

## 🧭 PRD-0084 多 Agent 工具路由口径

`Context & Asset Agent` 是当前素材/文件管理的责任方。它先读取当前上传、历史文件、生成结果、文件名、URL、source、content_type 和用户本轮指代，形成 `AssetBrief`；只有当素材选择或后续生成缺少语义事实时，才按需调用下方理解类 Skill。

- 上传图片/视频/文档本身不触发强制理解；不要再执行“上传后必须先识图/识视频/识文档”的旧流程。
- `see2ai_image_understanding`、`see2ai_video_understanding`、`see2ai_document_understanding` 是按需补语义的工具，不是固定阶段门禁。
- `see2ai_face_detection` 只在需要结构化 `has_face/face_count` 或执行前 hint 时使用；视频生成默认可让服务端自动识别。
- 任何付费图片/视频/音频生成前，都必须由 `Execution Guard Agent` 检查素材绑定、参数、成本风险和用户确认状态。

## 👁️ 视觉理解 Skill 路由索引

- `see2ai_image_understanding`：通用图片理解入口，适合图片描述、OCR、图表解读、商品外观分析等“需要开放式视觉问答”的需求。它由 `Context & Asset Agent` 按需调用；**不要**再用它做人脸检测，也不要把它当作上传图片后的固定前置步骤。→ 详见 `openclaw_skills/see2ai_image_understanding/SKILL.md`
- `see2ai_face_detection`：专用人脸检测入口，适合只需要判断“是否有人脸 / 有几张脸”，或需要给资产写入 `has_face` / `face_count` 的场景。它由 `Context & Asset Agent` 或 `Execution Guard Agent` 在缺少可信事实时按需调用。→ 详见 `openclaw_skills/see2ai_face_detection/SKILL.md`

## 🎬 视频与视频资产 Skill 路由索引

- `see2ai_video_generation`：视频生成入口，适合文生视频、首尾帧、参考图、参考视频、参考音频和同步音频生成；必须遵守上方 Pre-Plan 门卫与用户确认门禁。→ 详见 `openclaw_skills/see2ai_video_generation/SKILL.md`
- `see2ai_video_concat`：视频拼接入口，适合把多个已生成或已上传的视频片段顺序合并成一个成片。→ 详见 `openclaw_skills/see2ai_video_concat/SKILL.md`
- `see2ai_video_poster`：视频封面抽帧入口，适合为已有视频 URL 生成首个非黑屏 PNG 封面。→ 详见 `openclaw_skills/see2ai_video_poster/SKILL.md`
- `see2ai_video_understanding`：视频理解入口，适合总结、描述、分析已有视频内容；由 `Context & Asset Agent` 按需补充视频语义，不要用于生成或拼接。→ 详见 `openclaw_skills/see2ai_video_understanding/SKILL.md`

## 📦 文件与文档 Skill 路由索引

- `see2ai_storage_upload`：本地文件上传入口，适合把图片、视频、文档上传为公网 URL，再交给其他 Skill 使用。→ 详见 `openclaw_skills/see2ai_storage_upload/SKILL.md`
- `see2ai_document_understanding`：文档理解入口，适合分析、总结或问答 PDF/TXT 公网文档；由 `Context & Asset Agent` 按需抽取品牌/产品/脚本文案事实。→ 详见 `openclaw_skills/see2ai_document_understanding/SKILL.md`

## 🧭 当前 SEE2AI Action 映射快照（2026-04-29）

> 本表只用于帮助低上下文 Agent 快速核对“主模型默认可选 Skill → Action”关系；完整能力边界仍以各 `SKILL.md` 为唯一权威。workflow-only 内部工具不在本表列出，只能由上游工作流显式调用。SEE2AI 侧稳定公开名已替换部分旧包名，旧名仅作为 alias 兼容。

| OpenClaw Skill | 当前调用的 SEE2AI Action | 备注 |
|---|---|---|
| `see2ai_text_to_image` | `see2ai_image_generation_v1` / `see2ai_image_generation_fast_v1` / `see2ai_image_generation_alternative_v1` | `auto` 只在 `v1/alternative` 间选择；`fast` 必须显式指定 |
| `see2ai_image_to_image` | `see2ai_image_generation_v1` / `see2ai_image_generation_fast_v1` / `see2ai_image_generation_alternative_v1` | 图生图必须有参考图；缺图不得降级文生图 |
| `see2ai_text_to_image_uniworld` | `see2ai_image_uniworld_v2` | UniWorld 唯一合法入口 |
| `see2ai_image_normalize` | `see2ai_image_normalize_v1` | 新增图片预处理/稳定化入口 |
| `see2ai_face_detection` | `see2ai_face_detection_v1` | 人脸数量结构化检测 |
| `see2ai_video_generation` | `see2ai_video_generation_v1` | 当前 OpenClaw 标准视频生成入口；不要改用旧 `face_image_url/non_face_image_url` 字段 |
| `see2ai_video_concat` | `see2ai_video_concat_v1` | 后端字段为 `media_urls`，Skill 对外兼容 `video_urls` |
| `see2ai_video_poster` | `see2ai_video_poster_v1` | 新增视频封面抽帧入口 |
| `see2ai_image_understanding` / `see2ai_video_understanding` | `see2ai_llm_doubao_v1` | 旧 action 名 `see2ai_llm_doubao_seed_2_0_v1` 只是 alias |
| `see2ai_document_understanding` | `see2ai_llm_gemini_pro_v1` | 旧 action 名 `see2ai_llm_gemini_3_1_v1` 只是 alias |
