---
name: 01 - 演示前 30 分钟自查
retention: permanent
retention_reason: 演示前关键准备步骤
---

# 演示前 30 分钟自查 / Pre-Flight Checklist (30 min)

> 演讲者在登台前 30 分钟必过的清单。
> Speaker must walk through this 30 min before going on stage.

---

## 30 分钟前 / 30 Min Out

- [ ] 笔记本电池已充满 / 接电源 / Laptop charged or plugged in
- [ ] 备用电源 / 充电线就位 / Backup power / cables ready
- [ ] AI 工具的入口（Cursor / Claude Code）已经能正常打开 / AI tools open and working
- [ ] **测试一次**：发"请读 AI_MANUAL.md"看 AI 是不是能正常加载仓库 / Test loading the repo into the AI tool
- [ ] 互联网连接：会场 WiFi 已连 + 移动热点备份 / Venue WiFi connected, mobile hotspot ready
- [ ] 屏幕投影测试：打开 IDE，所有人能看清字号 / Test projection, font size readable
- [ ] 话筒 / 音响测试 / Mic / audio test

---

## 20 分钟前 / 20 Min Out

- [ ] 把仓库 `git pull` 到最新（确保和材料一致）/ git pull to latest
- [ ] 把 [`projects/customer_brief_generator/`](../../projects/customer_brief_generator/) 跑一遍：
  ```bash
  python3 customer_brief_generator.py examples/sample_input.txt
  ```
  确认能生成两份输出 / Verify generates both output files
- [ ] 跑测试：`python3 -m pytest tests/`，确认全过 / Run pytest, confirm green
- [ ] **手动**测一遍 ANTHROPIC_API_KEY 是否生效（如果演示要用 AI 模式）
  ```bash
  ANTHROPIC_API_KEY=sk-ant-... python3 customer_brief_generator.py examples/sample_input.txt
  ```
- [ ] 准备一份**预先生成好的 AI 输出**（如果现场 API 调用失败可以替代）

---

## 10 分钟前 / 10 Min Out

- [ ] 浏览器只开 1-2 个 tab（不要开内部 wiki / Slack / 邮箱——避免敏感内容意外被投影）
  Browser open with 1-2 tabs only (no internal wiki / Slack / email — to avoid accidental projection)
- [ ] **桌面截屏检查一次**：投影屏上有没有：
  - 内部代号 / 项目代号？
  - 客户名 / 客户 logo？
  - 内部邮件 / 群消息？
  - 私人聊天？
- [ ] 通知静音（电脑 + 手机）/ Notifications silenced
- [ ] 记得带：水、纸笔、备用 USB / 网线 / Bring: water, pen+paper, backup cables

---

## 5 分钟前 / 5 Min Out

- [ ] 打开第一张 slide（如有）
- [ ] 把 IDE 的 zoom 调到投影合适（通常 14-16pt 字号）/ Adjust IDE zoom for projection
- [ ] 把 AI 对话窗口准备好（空白状态，可以直接开始演示）
- [ ] 深呼吸

---

## 后台跑的"应急素材" / Backup Materials Ready in Background

- [ ] 预先生成好的 customer_brief_generator 输出（在新 tab 打开）
- [ ] 预先准备好的 AI 对话截图（Plan B：如果现场 AI 调用失败）
- [ ] 预先准备好的"反例 vs 正例"对比 slides（Plan B：如果时间紧需要跳过现场跑）

---

## 关键风险

| 风险 / Risk | 应急 / Backup |
|---|---|
| WiFi 断 / 网络慢 | 切移动热点 / 用预生成的输出 |
| AI API 限流 / 失败 | 切到模板模式 + 用预生成的输出 |
| 笔记本死机 | 重启需要 5 分钟，过渡到讲非演示部分 |
| 投影失败 | 用大字打印的 slides 应急 |
| 麦克风失效 | 用大声讲 |

---

## 心态

> 这场培训的目的不是"完美演示"，是"让大家学到东西"。
> 现场出问题不是事故——只要你保持冷静、用 Plan B、继续讲解，听众会反而更佩服。
>
> 真实的故障 + 真实的应急处理 = 最好的"工程纪律"现场教学。
