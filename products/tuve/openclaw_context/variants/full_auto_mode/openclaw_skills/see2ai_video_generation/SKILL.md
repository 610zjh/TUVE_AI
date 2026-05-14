---
name: see2ai_video_generation
description: >
  基于文本、首尾帧、参考图、视频与音频生成高质量视频（SEE2AI 视频生成模型）。
  2026-04-26 起对齐 PRD-0103 guided repair 契约：请求不可执行时上游会返回 422 +
  完整结构化「修复指引」（双轨：用户客服式 + Agent 机器指令 + 候选改法 +
  可执行 patch + 最小可运行示例）。本 Skill 必须把这份指引「双轨」呈现给用户
  与上游 Agent；默认不得自动重试也不得吞掉指引，但在全自动省心模式下允许
  按 `AGENTS.md` 的 Mode 2 纪律自动择优重试 1 次。
  Do NOT use for video editing or video concatenation.
version: 4.0.0
author: TUVE
update: 2026-04-29
action: see2ai_video_generation_v1
metadata:
  emoji: "🎬"
  requires:
    - SEE2AI_BASE_URL
    - SEE2AI_API_KEY
dependency:
  python:
    - requests
---

# 📋 能力声明 (Capability Declaration)

## trigger_when

- 用户要生成全新视频，而不是剪辑、拼接或理解已有视频
- 用户提供了文字描述，或补充了首帧、尾帧、参考图、参考视频、参考音频，希望据此生成视频
- 用户要做真人口播、商品展示、场景动态化、镜头语言参考、音画同步生成

## do_NOT_trigger_when

- 用户要剪视频、拼接视频、延长已有片段，请改走其他对应 Skill
- 用户只是想理解图片/视频内容，不要调用本 Skill
- 用户只是要图片，不要调用本 Skill

## can_do

- 文生视频、首帧驱动、首尾帧插值、参考图驱动、视频参考、音频参考、多模态混合参考
- 服务端自动识别真人脸（不需要 Agent 自己判断）；已知答案时可显式传 `*_contains_real_face` hint
- 输出分辨率支持 `480p` / `720p` / `1080p`
- 同步等结果或异步只取 `task_id`
- 错误请求得到完整 guided repair（候选改法 + 可执行 patch + 最小可运行示例 + 双轨文案）

## cannot_do

- 不替代视频编辑、视频拼接、视频理解 Skill
- 不能保证上游当前一定接受 `1080p`；若上游尚未放量，可能直接返回 422/4xx
- 不能在用户本轮明确认可前直接发起真实生成；**全自动省心模式**除外，此时由工具确认卡片替代文字确认

## known_limitations

- `reference_image_contains_real_face` 对 `reference_image_url` 与 `reference_image_urls` 共用同一个布尔 hint，不支持逐张单独标注

## fallback_candidates

- `see2ai_video_concat`
- `see2ai_video_understanding`

---

# 0号铁律：真实调用前强制门禁

> 本节优先级高于普通示例与推荐写法。只要还没完成自检和用户确认，绝对不能发起真实视频生成；**全自动省心模式**除外，此时由 `AGENTS.md` 的 Mode 2 规则接管。

## 绝对执行规则

1. 任何一次真实调用之前，必须先完成调用前自检。
2. 自检未完成、自检未通过、或用户尚未明确认可时，绝对禁止真实调用；**全自动省心模式**除外，此时以 `AGENTS.md` 的 Mode 2 为准。
3. 只要 Prompt、素材、时长、参数任一项变化，就必须重新展示最终方案并再次确认。
4. 即使用户说"直接跑"，也不能跳过确认门禁；**只有在明确进入全自动省心模式时**，才允许由工具确认卡片替代文字确认。
5. 除非用户明确要求，否则不要关闭 `generate_audio`。

## 调用前自检清单

- [ ] Prompt 中已经包含明确的画面描述；如果有台词，台词已经写入 Prompt 本体
- [ ] 已经把本轮最终使用的素材映射、Prompt、时长、分辨率、关键参数完整展示给用户
- [ ] 用户已对本轮方案作出明确认可；或当前已明确进入全自动省心模式
- [ ] 若已知某张图是否含真人脸，只在"明确知道答案"时才传 `*_contains_real_face`
- [ ] 若计划启用 `1080p`，已提醒用户其成本约为 `720p` 的 2.25 倍

---

# 字段语义（2026-04-26 起，唯一入口）

## 核心规则

1. **图片字段唯一入口**：
   - `first_frame_url`
   - `last_frame_url`
   - `reference_image_url`
   - `reference_image_urls`
2. **默认不需要 Agent 自己判断人脸**——不传 hint，让服务端自动识别即可。
3. 业务上下文已经明确知道答案时，才传：
   - `first_frame_contains_real_face`
   - `last_frame_contains_real_face`
   - `reference_image_contains_real_face`
4. **首尾帧模式 与 参考图模式 不可混用**：同时传 `first_frame_url` 与 `reference_image_url(s)` 会被 Action 直接拒绝（返回 needs_repair + 二选一方案）。
5. **`face_image_url` / `non_face_image_url` / `non_face_image_urls` 等旧字段已下线**——本 Skill 不再接受，传入会立即报错并指向新字段。

## hint 何时该传

- Skill 刚生成了真人头像、写真、数字人口播图，明确有人脸：传对应的 `*_contains_real_face=true`
- 素材明确是产品图、风景图、截图，明确无人脸：传对应的 `*_contains_real_face=false`
- 用户上传图、来源复杂、无法确认：不要传 hint，让服务端自动识别

## 仍需注意的边界

- `last_frame_url` 不能脱离 `first_frame_url` 单独存在（Action 会以 warning 提醒）
- `audio_url(s)` 不能孤悬，必须搭配至少 1 张参考图或 1 段参考视频（Action 会拒绝并给二选一方案）
- 单次素材数量上限：图 ≤ 9 / 视频 ≤ 3 / 音频 ≤ 3 / 总素材 ≤ 12
- `duration` ∈ [4, 15] 或 -1（自动）

---

# 🚨 如何消费 needs_repair 响应（强制规范）

> Action 端在 PRD-0103 之后引入 guided repair 契约。当请求不可执行时，本 Skill 退出码 = `2`，stderr 上同时包含「给用户的话」与「给 Agent 的机器指令」两块。下面是**强制**的消费流程。

## 何时会出现 needs_repair

- 字段冲突（如首尾帧模式与参考图模式同时存在）
- 范围越界（duration<4 / >15、resolution 不在 480p/720p/1080p、aspect_ratio 不在白名单）
- 数量超限（图>9 / 视频>3 / 音频>3 / 总素材>12）
- 音频孤悬
- prompt 中 `@图N / @视频N / @音频N` 越界
- URL 非 http(s) / 扩展名非法
- 入口为空（无 prompt 也无任何素材）

完整类目见 SEE2AI 项目中的 `workspace_human/prd/0103_video_generation_error_taxonomy.md`（A–O 类）。

## 退出码契约

| 退出码 | 含义 | Agent 必须做的事 |
|---|---|---|
| `0` | 成功 / running / awaiting_approval | 把视频 URL 或任务 ID 转给用户 |
| `2` | needs_repair | **停手**，按下文流程把改法报给用户 |
| `3` | awaiting_user_approval | 把授权链接转给用户，等待用户点击 |
| `1` | 其他错误（网络/鉴权/上游 5xx） | 报错给用户，必要时换 fallback Skill |

## Agent 收到 needs_repair (退出码 2) 后的标准动作

1. **默认绝对不要自动重试** —— guided repair 的本意是「停下来让用户决定」，自动改 payload 重试等于偷偷改用户意图。**全自动省心模式**是唯一例外：允许自动择优重试 1 次。
2. **先把「给用户的话」原样转给用户** —— stderr 中 `[👤 给用户的话]` 块下面的内容就是客服式中文，直接展示。
3. **若有候选改法 (`[🔀 候选改法]` 块)**，把方案 A/B/C 列给用户，让用户**明确选一个**。
4. **若有 `payload_patch_plan`**，把它解释成自然语言（"我需要把 duration 改成 4，可以吗？"），等用户点头再发起新请求。**禁止静默套用 patch**。
5. **若有 `minimal_runnable_payload`**，是兜底——只在用户说"我也不知道怎么改了，给我一个能跑的最小例子"时才推荐使用。
6. **若有 `warnings` / `hints`**，建议在用户确认改法时一并提及（"另外你这次还触发了 X 警告，建议一并处理"）。

## 用户收到 needs_repair 体验

用户应该在 stderr 上看到（顺序固定）：

```
────────────────────────────────────────────────────────────
⚠️  请求暂时无法执行（needs_repair）
────────────────────────────────────────────────────────────
概要: <一句话讲清楚为什么不能跑>

[👤 给用户的话]
<客服式中文，直接告诉用户为什么 + 下一步>

[🔀 候选改法（请选一种再重试）]
  方案 A: <标题>
    · <描述>
    · 保留字段: ...
    · 删除字段: ...
  方案 B: <标题>
    ...
```

后面紧跟 `[🤖 给 Agent 的机器指令]` 块，包含 `error_code / repair_category / agent_instruction / issues / payload_patch_plan / minimal_runnable_payload`，是给 Agent 自动消费用的。

## Agent 不得做的事（红线）

- ❌ 在非全自动省心模式下，把 `payload_patch_plan` 直接套用就重新发起请求
- ❌ 在非全自动省心模式下，自动从 `repair_options` 里挑一个继续跑
- ❌ 把 `agent_facing_instruction` 当作"上游许可"无视用户
- ❌ 吞掉 needs_repair 体，只对用户说"生成失败"
- ❌ 用 `minimal_runnable_payload` 偷偷替换用户原意图

## 全自动省心模式例外

当且仅当上游 `AGENTS.md` 已明确判定进入 **全自动省心模式** 时，本 Skill 允许以下例外：

1. 视频生成前不再额外做一轮文字确认，由工具确认卡片替代
2. 第一次 `needs_repair` 可自动从候选方案中选择最合理的一种并重试 1 次
3. 若自动重试后仍然 `needs_repair`，必须立即停止全自动模式，回退为用户可决策的先审后发流程

---

# ⚡ 推荐：JSON 配置模式

```bash
# 文生视频
python skills/see2ai_video_generation/scripts/video_generation.py \
  --config '{"prompt": "一只猫咪在草地上玩耍"}'

# 使用首帧真人图，明确告诉服务端含真人脸
python skills/see2ai_video_generation/scripts/video_generation.py \
  --config '{"first_frame_url": "https://example.com/portrait.jpg", "first_frame_contains_real_face": true, "prompt": "女孩抬头看向镜头，电影级运镜，温暖光线", "duration": 8, "aspect_ratio": "9:16"}'

# 首尾帧驱动（同时传首帧和尾帧）
python skills/see2ai_video_generation/scripts/video_generation.py \
  --config '{"first_frame_url": "https://example.com/start.jpg", "last_frame_url": "https://example.com/end.jpg", "prompt": "镜头从首帧推进到尾帧，主体自然过渡"}'

# 多参考图，已知全部都不含真人脸
python skills/see2ai_video_generation/scripts/video_generation.py \
  --config '{"reference_image_urls": ["https://example.com/product.jpg", "https://example.com/scene.jpg"], "reference_image_contains_real_face": false, "prompt": "@图1 作为产品细节参考，@图2 作为场景构图参考；镜头从近景推到中景，突出材质与空间层次", "resolution": "1080p"}'

# 图片 + 视频 + 音频联合参考（多模态参考模式，不可混入 first_frame_url / last_frame_url）
python skills/see2ai_video_generation/scripts/video_generation.py \
  --config '{"reference_image_url": "https://example.com/scene.jpg", "video_url": "https://example.com/motion.mp4", "audio_url": "https://example.com/beat.mp3", "prompt": "@图1 为主体参考，参考@视频1的运镜与动作节奏，卡点参考@音频1"}'
```

## 传统 CLI 模式（仍然支持）

```bash
python skills/see2ai_video_generation/scripts/video_generation.py --prompt "未来城市夜景" --aspect_ratio 16:9 --duration 10
python skills/see2ai_video_generation/scripts/video_generation.py --reference_image_url "https://example.com/product.jpg" --prompt "让产品自然转动并出现高光扫过"
```

---

# JSON 配置参数说明

| JSON 字段 | 必填 | 说明 |
|---|---|---|
| `prompt` | 条件 | 文本提示词，必须把画面描述与台词写进 Prompt 本体 |
| `model_name` | 否 | `see2ai-video-v2`（默认/画质优先）/ `see2ai-video-v2-fast`（速度优先，约为标准版 80% 价） |
| `first_frame_url` | 条件 | 首帧图片 URL |
| `last_frame_url` | 条件 | 尾帧图片 URL；与 `first_frame_url` 配套使用 |
| `reference_image_url` | 条件 | 单张参考图片 URL（与 `first_frame_url` 互斥） |
| `reference_image_urls` | 条件 | 多张参考图片 URL 列表（与 `first_frame_url` 互斥；最多 9 张） |
| `first_frame_contains_real_face` | 否 | `true/false/null`，首帧是否含真人脸的先验 |
| `last_frame_contains_real_face` | 否 | `true/false/null`，尾帧是否含真人脸的先验 |
| `reference_image_contains_real_face` | 否 | `true/false/null`，参考图是否含真人脸的统一先验 |
| `video_url` | 条件 | 参考视频 URL（单视频；与 `first_frame_url` 互斥） |
| `video_urls` | 条件 | 参考视频 URL 列表（最多 3 段；总时长 ≤15s） |
| `audio_url` | 条件 | 参考音频 URL（单音频；不可孤悬，需搭配视觉素材） |
| `audio_urls` | 条件 | 参考音频 URL 列表（最多 3 段；不可孤悬） |
| `duration` | 否 | 视频时长，支持 `4-15` 或 `-1`（自动） |
| `resolution` | 否 | `480p` / `720p` / `1080p`，默认 `720p` |
| `aspect_ratio` | 否 | `adaptive` / `16:9` / `9:16` / `1:1` / `21:9` / `4:3` / `3:4` |
| `generate_audio` | 否 | 是否生成同步音频，默认 `true` |
| `force_asset_upload` | 否 | 强制全部图片/视频走素材库的兜底开关（会显著增加耗时，请仅在普通直传频繁失败时开启） |
| `enable_web_search` | 否 | 联网搜索增强生成（会增加几秒到十几秒延迟） |
| `sync` | 否 | `true` 同步返回结果，`false` 仅返回任务信息（异步） |

> 字段范围 / 互斥规则的最终权威是 Action 的 validator + 错误穷举主文档（`workspace_human/prd/0103_video_generation_error_taxonomy.md`）。本 Skill 不再做本地业务校验——传错了 Action 会返回 needs_repair，本 Skill 会双轨呈现给用户与 Agent。

---

# Prompt 硬规范

- 默认将单个片段视为一次独立生成任务；总时长能一次生成时优先一次生成
- Prompt 中的素材引用必须显式说明用途，例如 `@图1作为首帧，@图2作为风格参考`
- Prompt 优先采用时间轴写法，把多个极短镜头合并进 4-15 秒片段
- Prompt 使用纯中文、控制在 800 字以内，并以负向排除词结尾
- 如果有台词，必须把台词写进 Prompt 本体

---

# 输出格式

## 成功（退出码 0）

```text
https://cdn.see2ai.com/generated/video1.mp4
```

## needs_repair（退出码 2）

stdout 为空；stderr 上是双轨呈现块（详见上方「如何消费 needs_repair 响应」）。Agent 必须停手等用户决定改法。

## 等待用户授权（退出码 0 / 3）

```text
⏳ 等待用户授权（300秒内有效）
授权 ID: appr_xxx
👉 请点击授权: https://see2ai.com/approval/xxx
```

## 异步提交（退出码 0）

```text
🚀 任务已提交（异步模式）。task_id=task_xxx
```
