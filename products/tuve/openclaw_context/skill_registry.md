---
name: TUVE OpenClaw Skill 路由清单 / TUVE OpenClaw Skill Registry
description: 基于 openclaw_skills 当前目录整理的可用 skill、使用边界和调用提醒
type: permanent
retention: permanent
retention_reason: TUVE skill 路由的长期索引，供 AI 与维护者在 TUVE_AI 中快速判断边界
---

# TUVE OpenClaw Skill 路由清单

> 这份清单来自 `openclaw_skills/` 当前目录，目标是让工作区里的 AI 能先快速判断“该看哪个 skill”。真正执行前，仍应回到对应原始 `SKILL.md`。

## 1. 总体路由原则

- 有参考图的图片生成，优先 `see2ai_image_to_image`
- 纯视觉文生图，优先 `see2ai_text_to_image`
- 文字、排版、多语种、信息结构优先的文生图，优先 `see2ai_text_to_image_uniworld`
- 视频生成走 `see2ai_video_generation`
- 拼接既有片段走 `see2ai_video_concat`
- 上传本地文件走 `see2ai_storage_upload`
- 图片标准化走 `see2ai_image_normalize`
- 只需要结构化人脸事实时走 `see2ai_face_detection`
- 链接打不开时先探活，再考虑是否重生成

## 2. 图片相关

| Skill | 什么时候用 | 不该什么时候用 |
|---|---|---|
| `see2ai_text_to_image` | 纯文本生成视觉画面、插画、氛围图、产品展示图 | 用户已提供参考图；或需求是排版、文字、详情页、PPT |
| `see2ai_text_to_image_uniworld` | 图中有文字、数字、多语种、强排版或信息层级 | 用户要纯视觉图；或已有参考图想改图 |
| `see2ai_image_to_image` | 已有参考图，基于原图改图、扩图、换背景、换场景 | 没有参考图；也不能偷偷降级成文生图 |
| `see2ai_image_normalize` | 原图 URL 不稳、过大、宿主不稳定，需要给下游一个更稳定的托管图 | 用户要理解图片、做人脸检测或生成新图 |
| `see2ai_face_detection` | 只需要 `has_face` / `face_count` 这样的结构化人脸事实 | 用户想做图片描述、OCR、开放式视觉问答 |

## 3. 视频相关

| Skill | 什么时候用 | 不该什么时候用 |
|---|---|---|
| `see2ai_video_generation` | 生成新视频，支持文本、首尾帧、参考图、视频、音频混合输入 | 用户只是想拼接、抽封面或理解视频 |
| `see2ai_video_concat` | 已有 2 段及以上视频 URL，需要按顺序拼接 | 用户要生成新视频或做复杂剪辑 |
| `see2ai_video_poster` | 已有视频 URL，需要抽首个非黑屏封面 | 用户要生成视频、拼接视频或理解视频内容 |
| `see2ai_media_url_health_check` | 用户说“链接打不开/坏了/加载失败”时，先验证 URL 是否真的失效 | 用户只是觉得内容不好看或要重做构图 |

## 4. 文件与内部工具

| Skill | 什么时候用 | 备注 |
|---|---|---|
| `see2ai_storage_upload` | 把本地图片、视频、文档上传成公网 URL | 下游 skill 需要公网 URL 时的标准入口 |
| `see2ai_seedance_prompt_renderer` | 上游工作流已经有完整 shot 数据，需要渲染 Seedance 专属 prompt | `workflow_only` 内部工具，主模型不应直接暴露给用户 |

## 5. 特别提醒

### 5.1 图片路由的三个分叉

- **有参考图**：`see2ai_image_to_image`
- **无参考图，但纯视觉优先**：`see2ai_text_to_image`
- **无参考图，但文字/排版优先**：`see2ai_text_to_image_uniworld`

### 5.2 视频生成的硬门禁

`see2ai_video_generation` 有三条必须记住的纪律：

- 生成前必须向用户展示最终方案并获得确认
- 首尾帧模式与参考图模式不能混用
- `needs_repair` 必须停下来让用户选，不得自动修 payload

### 5.3 探活优先于重生成

当用户报告“之前的媒体打不开”时，不应先烧新的图片/视频生成额度。应先用 `see2ai_media_url_health_check` 判断：

- 链接健康：优先排查播放环境、浏览器、下载方式
- 链接失效：再进入重新生成或重新上传流程

## 6. 与配置模板的关系

当前 `openclaw_config.template.json` 里默认暴露的主技能列表包括：

- `see2ai_face_detection`
- `see2ai_image_normalize`
- `see2ai_image_to_image`
- `see2ai_storage_upload`
- `see2ai_text_to_image`
- `see2ai_text_to_image_uniworld`
- `see2ai_video_concat`
- `see2ai_video_generation`
- `see2ai_video_poster`

`see2ai_seedance_prompt_renderer` 不在主模型默认 skill 列表中，应保持 workflow-only。

## 7. 原始依据

- `openclaw_skills/see2ai_face_detection/SKILL.md`
- `openclaw_skills/see2ai_image_normalize/SKILL.md`
- `openclaw_skills/see2ai_image_to_image/SKILL.md`
- `openclaw_skills/see2ai_text_to_image/SKILL.md`
- `openclaw_skills/see2ai_text_to_image_uniworld/SKILL.md`
- `openclaw_skills/see2ai_storage_upload/SKILL.md`
- `openclaw_skills/see2ai_video_generation/SKILL.md`
- `openclaw_skills/see2ai_video_concat/SKILL.md`
- `openclaw_skills/see2ai_video_poster/SKILL.md`
- `openclaw_skills/see2ai_media_url_health_check/SKILL.md`
- `openclaw_skills/see2ai_seedance_prompt_renderer/SKILL.md`
