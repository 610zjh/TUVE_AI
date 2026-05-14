# Full Auto Mode Variant

这是一套面向 **“全自动托管 / 两轮生成”** 需求整理出来的 TUVE OpenClaw 变体包。

## 这个变体解决什么问题

原始 `raw/` 目录里的 Config 和 Skill，已经包含了大量 TUVE 运行时约束，但其中仍保留了很多“先审后发、逐步确认”的强门禁。

你的目标不是简单补一段模式说明，而是让整套上下文在以下事情上 **前后一致**：

- 用户只说 1-2 句需求时，先回一份一次性问题清单
- 用户回答后，即使没有回答全，agent 也能自主补全缺失项
- 内部 1+3 Agent 流程照跑，但跳过多轮用户确认门
- 生成视频时，工具卡片替代文字确认
- `needs_repair` 在全自动模式下允许自动择优重试 1 次
- 图片生成与视频生成的 Skill 文档，不再和全自动模式互相冲突

## 目录说明

- `openclaw_configs/`
  - 在 `raw/openclaw_configs` 基础上复制，并补齐全自动模式下会冲突的身份、状态与门禁规则
- `openclaw_skills/`
  - 在 `raw/openclaw_skills` 基础上复制，仅修改与“必须逐次人工确认”冲突的 Skill 文档
- `openclaw_config.template.json`
  - 变体包对应的配置模板，便于和主模板区分

## 这次重点改了什么

- `openclaw_configs/AGENTS.md`
  - 保留完整的“模式二：全自动省心模式”设计
- `openclaw_configs/IDENTITY.md`
  - 改成“全自动优先，但允许退回先审后发”的角色契约
- `openclaw_configs/USER.md`
  - 把默认协作模式改成全自动省心模式
- `openclaw_configs/MEMORY.md`
  - 增加问题清单、自主决策摘要等更适合全自动模式留痕的字段
- `openclaw_skills/see2ai_video_generation/SKILL.md`
  - 给确认门禁与 `needs_repair` 消费规则加上全自动模式例外
- `openclaw_skills/see2ai_text_to_image/SKILL.md`
  - 给图片生成确认门加上全自动模式例外
- `openclaw_skills/see2ai_image_to_image/SKILL.md`
  - 给图生图确认门加上全自动模式例外
- `openclaw_skills/see2ai_text_to_image_uniworld/SKILL.md`
  - 给排版文生图确认门加上全自动模式例外

## 使用建议

- 如果你要保留原始 OpenClaw 语义，请继续用 `raw/`
- 如果你要验证“全自动托管模式”是否能形成一套自洽上下文，请优先试这套变体包
- 如果后面你决定把这套方案升级成正式默认配置，再从这个目录回合并到正式上下文会更稳
