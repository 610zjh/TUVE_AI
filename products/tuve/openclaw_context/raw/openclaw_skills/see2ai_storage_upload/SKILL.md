---
name: see2ai_storage_upload
description: >
  上传本地文件（图片、视频、文档）到 SEE2AI 云存储，返回带有 CDN 加速的永久 URL。
  Use when the user needs to upload local files to get a public URL for use with other SEE2AI tools.
  Supports common images, videos, documents, and other file types up to 50MB.
  WebP is not accepted by the SEE2AI storage upload service; convert WebP to JPG or PNG first.
  Do NOT use for downloading files or URL fetching.
version: 1.0.0
author: TUVE
update: 2026-04-29
action: see2ai_storage_upload_v1
metadata:
  emoji: "📦"
  requires:
    - SEE2AI_BASE_URL
    - SEE2AI_API_KEY
dependency:
  python:
    - requests
---

# 📋 能力声明 (Capability Declaration)

## trigger_when

- 用户提供本地图片、视频或文档文件，需要转换为公网 URL 后交给其他 SEE2AI Skill 使用。
- 下游 Skill 明确要求公网 `http/https` URL，而当前只有本地路径。

## do_NOT_trigger_when

- 用户给的已经是公网 URL，不需要重复上传，除非 URL 不稳定或需要归档到 SEE2AI 存储。
- 用户要下载网页或抓取远程文件，本 Skill 只上传本地文件。
- 用户要批量上传目录，本 Skill 不处理目录。

## can_do

- 上传本地文件到 SEE2AI 云存储，返回 CDN URL。
- 支持图片、视频、文档等常见文件类型（单文件最大 50MB，不含 WebP）。

## cannot_do

- 不能下载远程 URL。
- 不能上传目录或空文件。
- 不能直接上传 WebP；WebP 需要先转换为 JPG 或 PNG。

## known_limitations

- 文件需存在于运行环境可访问路径中。
- SEE2AI 服务端当前限制为单文件最大 50MB。
- SEE2AI 服务端显式拒绝 WebP，上传前必须先转成 JPG 或 PNG。

## fallback_candidates

- `see2ai_image_normalize`

---

## 能力边界

- ✅ 支持类型：图片(jpg/png/gif)、视频(mp4/mov/avi)、文档(pdf/doc/docx)等
- ✅ 文件限制：最大 50MB
- ✅ 输出：CDN 加速的永久 URL
- ❌ 不支持：目录上传
- ❌ 不支持：下载文件或 URL 抓取
- ❌ 不支持：直接上传 WebP（请先转换为 JPG/PNG）

## 前置条件

### 文件要求

- 文件必须存在且不为空
- 文件大小不超过 50MB
- 支持常见图片、视频、文档格式；WebP 需要先转换为 JPG 或 PNG

## 使用方式

### ⚡ 推荐：JSON 配置模式

```bash
# 上传图片
python skills/see2ai_storage_upload/scripts/storage_upload.py \
  --config '{"file_path": "/path/to/image.jpg"}'

# 上传视频（显示详细信息）
python skills/see2ai_storage_upload/scripts/storage_upload.py \
  --config '{"file_path": "/path/to/video.mp4"}'

# 上传文档
python skills/see2ai_storage_upload/scripts/storage_upload.py \
  --config '{"file_path": "/path/to/document.pdf"}'
```

### 传统 CLI 模式（仍然支持）

```bash
python skills/see2ai_storage_upload/scripts/storage_upload.py /path/to/image.jpg
```

### JSON 配置参数说明

| JSON 字段 | 必填 | 说明 |
|-----------|------|------|
| `file_path` | ✅ | 要上传的本地文件路径 |

## 执行流程

1. **接收需求**：确认用户需要上传的文件路径
2. **验证文件**：检查文件是否存在、是否为文件、大小是否合规
3. **执行上传**：调用 CLI 工具上传文件
4. **返回结果**：展示上传后的 URL 和文件信息

## 输出格式

### 标准输出

```
https://cdn.see2ai.com/uploaded/file.jpg
```

## 示例

### 示例 1：上传图片

```bash
python skills/see2ai_storage_upload/scripts/storage_upload.py \
  --config '{"file_path": "/home/user/photos/vacation.jpg"}'
```

### 示例 2：上传视频

```bash
python skills/see2ai_storage_upload/scripts/storage_upload.py \
  --config '{"file_path": "/home/user/videos/tutorial.mp4", "verbose": true}'
```

### 示例 3：上传文档

```bash
python skills/see2ai_storage_upload/scripts/storage_upload.py \
  --config '{"file_path": "/home/user/documents/report.pdf"}'
```
