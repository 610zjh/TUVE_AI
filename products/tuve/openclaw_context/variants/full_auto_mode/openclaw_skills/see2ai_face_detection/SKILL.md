---
name: see2ai_face_detection
description: >
  使用 SEE2AI 专用人脸检测 Action 判断公网图片中是否包含可识别人脸，并返回
  `has_face` 与 `face_count`。
  Use when the intent is face detection only; do NOT use image understanding for this.
version: 1.0.1
author: TUVE
update: 2026-04-29
action: see2ai_face_detection_v1
metadata:
  emoji: "🙂"
  requires:
    - SEE2AI_BASE_URL
    - SEE2AI_API_KEY
dependency:
  python:
    - requests
---

# 📋 能力声明 (Capability Declaration)

## trigger_when

- 用户明确要判断一张图片里有没有人脸
- `Context & Asset Agent` 或 `Execution Guard Agent` 缺少可信 `has_face` / `face_count`，且该事实会影响视频 hint、素材选择或执行前检查
- 上游逻辑只需要“是否有人脸”的结构化答案，而不需要完整图像描述

## do_NOT_trigger_when

- 用户想让系统描述图片内容、提取图片文字、分析图表，请改用 `see2ai_image_understanding`
- 用户要分析视频里是否有人脸，请改用视频理解或视频专用流程
- 用户给的是本地文件路径而不是公网 URL，请先上传再检测
- 视频生成并不默认要求提前检测人脸；如果缺少可信事实，优先不传 hint，让服务端自动识别
- 已有可信 `has_face/face_count` 时不要重复调用本 Skill

## can_do

- 检测公网 PNG/JPEG 图片中是否包含可识别人脸
- 返回结构化结果：`has_face`、`face_count`
- 返回 `warnings` 以及基础计量字段，便于上游 Agent 记录和复用
- 作为执行前按需判定工具，为 `*_contains_real_face` hint 提供依据

## cannot_do

- 不能替代图像理解，不负责描述场景、识别商品、提取文字或回答开放式视觉问题
- 不能处理本地文件路径、私有内网地址或未上传素材
- 不能保证识别到被严重遮挡、极小尺寸或不满足 Action 输入约束的人脸

## known_limitations

- 输入必须是公网可访问的 `http/https` 图片 URL
- 图片需满足 Action 约束：PNG/JPEG、<2MB、边长 48~4096 像素
- 输出只回答“是否有人脸”和“人脸数量”，不会补充人物身份或画面语义

## fallback_candidates

- `see2ai_storage_upload`
- `see2ai_image_understanding`

---

# 使用方式

## 推荐：JSON 配置模式

```bash
python skills/see2ai_face_detection/scripts/face_detection.py \
  --config '{"image_url": "https://example.com/photo.jpg"}'
```

## 传统 CLI 模式

```bash
python skills/see2ai_face_detection/scripts/face_detection.py \
  https://example.com/photo.jpg
```

## JSON 配置参数说明

| JSON 字段 | 必填 | 说明 |
|---|---|---|
| `image_url` | ✅ | 待检测图片的公网 URL |
| `verbose` | ❌ | 是否在 stderr 输出计量与 warning 信息 |

---

# 执行流程

1. 接收图片 URL
2. 校验是否为公网 `http/https` 地址
3. 调用 `see2ai_face_detection_v1`
4. 输出标准化 JSON，供上游 Agent 直接消费
5. 如 `Context & Asset Agent` / `Execution Guard Agent` 需要，将结果写入当前资产事实中的 `has_face` / `face_count`

---

# 输出格式

stdout 始终输出 JSON：

```json
{
  "has_face": true,
  "face_count": 1,
  "warnings": null,
  "model": "see2ai_face_detection_v1",
  "source": "see2ai",
  "input_tokens": 0,
  "output_tokens": 0,
  "total_tokens": 0,
  "cost_points": 500
}
```

启用 `--verbose` 时，会额外在 stderr 输出计量信息与 `warnings`，不污染 stdout 的 JSON。
