---
name: see2ai_media_url_health_check
description: >
  Probe a public media URL (video / image / audio) with HEAD or short Range GET
  to determine whether the link itself is healthy, before deciding to regenerate
  any paid media. Returns structured `ok / status_code / content_type /
  content_length / accept_ranges / notes`. ⚠️ MUST be used before re-generating
  any video / image / audio when the user reports "我点不开 / 打不开 / 链接坏了 /
  加载失败" type issues — re-generation costs real money and usually doesn't fix
  the actual problem (mobile codec / CORS / Range / DNS).
version: 1.0.0
author: TUVE
update: 2026-05-07
action: see2ai_media_url_health_check_v1
metadata:
  emoji: "🩺"
  requires: []
dependency:
  python:
    - httpx
---

# 📋 能力声明 (Capability Declaration)

## trigger_when

- 用户对一段 **本平台先前生成或已上传** 的媒体（视频 / 图片 / 音频）报告
  "我点不开 / 打不开 / 加载不出来 / 链接坏了 / 没反应 / 黑屏" 等问题。
- 在调用 `see2ai_video_generation_*` / `see2ai_image_generation_*` /
  `see2ai_voice_recognition_*` 这类**付费**生成 Skill 前，需要先确认
  "失败"是不是因为链接本身根本访问不到。
- Agent 内部需要快速判断一个 CDN URL 是不是已经 404 / 403 / DNS 过期。

## do_NOT_trigger_when

- 用户给出的是非 http(s) 链接（如本地路径）。
- 用户说的"打不开"指的是图片**内容看不清楚**（应去缩放 / 重新生成构图，
  而不是探活）。
- 用户没有提到任何具体链接，只是说"上次的视频还好吗" — 这是闲聊，不需要探活。

## can_do

- 对公网 URL 发 HEAD（5s 超时），必要时降级为 `Range: bytes=0-0` 的短 GET。
- 解析 HTTP 状态码 / Content-Type / Content-Length / Accept-Ranges。
- 返回结构化结果，让 LLM 可以基于事实做下一步决定。
- 不下载完整对象、不消耗租户余额（探活属于平台基础动作）。

## cannot_do

- 不能验证视频是否能在用户的具体浏览器/手机上播放（编码兼容性）。
- 不能修复 / 重新转码 — 这属于另一组 Skill。
- 不能跨身份探活：被探活的 URL 必须是公网可访问的。

## must_use_before

- `see2ai_video_generation_v1`
- `see2ai_video_generation_v2`
- `see2ai_video_generation_kling_3_0_v1`
- `see2ai_video_concat_v1`
- `see2ai_video_poster_v1`
- `see2ai_image_generation_v1` 等付费媒体生成 Skill

— 当且仅当触发原因是用户报告"已生成媒体打不开"。

# 🤖 Agent 行为契约 (Agent Behavior Contract)

## 决策树

1. 用户语气含"我点不开 / 打不开 / 链接坏了 / 加载不出来"且**指向已生成的媒体 URL**
   → **必须**先调用 `see2ai_media_url_health_check`。
2. `ok=true`：
   - **禁止**重新调用付费生成 Skill。
   - 回复模板（中文）：
     > 链接本身是健康的（HTTP {status_code}, {content_type}）。建议你：
     > ① 复制链接到浏览器地址栏直接打开；② 或者长按链接选择"保存到本地"
     > 后用本地播放器打开；③ 移动端可以试试微信"用浏览器打开"。如果还是不行，
     > 告诉我你看到的具体错误提示，我来排查。
3. `ok=false`：
   - 文案告知用户原链接已失效，正在重新生成。**然后**才允许调用付费生成 Skill。

## 反幻觉

- 不许在没调用本 Skill 的情况下，凭空声称"我已经验证过链接是好的"或
  "已经检测到链接失效"。每一句关于 URL 健康度的事实都必须有本 Skill
  返回值作为依据。
