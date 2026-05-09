---
name: 03 - 演示崩了的应急
retention: permanent
retention_reason: 演讲者必备的应急 playbook
---

# 演示崩了的应急 Playbook / Recovery When Things Break

> 现场演示崩了不必慌。每种崩法有对应应急。
> If something breaks live, don't panic. Each failure mode has a backup.

---

## 崩法 1：AI 调用失败 / API 错误

**症状**：发 prompt 给 AI，AI 没回 / 回错误码 / 超时

**应急**：

1. 不要在台上反复重试 5 次——让观众看你 troubleshooting 比讲解更不专业
2. 立刻说："AI 服务这会儿响应慢/有问题。我切到模板模式给大家看效果"
3. 切到 [`projects/customer_brief_generator/`](../../projects/customer_brief_generator/) 的 template-fill 模式（不需 API key）
4. 或者打开预先准备好的"AI 已生成"输出截图

**预防**：
- 演示前 30 分钟自己测一次 API
- 提前缓存好"理想 AI 输出"作为 Plan B

---

## 崩法 2：网络断

**症状**：浏览器打不开 / git pull 失败 / API 调用超时

**应急**：

1. 立刻切移动热点（笔记本应该已经连好热点）
2. 如果热点也慢——切到完全离线模式：
   - 演示 customer_brief_generator 用 template-fill 模式（无 API 调用）
   - 用预先生成好的 AI 对话截图（多 slide 形式）
   - 焦点切到讲解仓库结构 / 红线 / 工作流（不需要联网）

**预防**：
- 演示前确认会场 WiFi + 自己的移动热点都能用
- 不要全场依赖 AI 实时响应——多用本地能跑的部分

---

## 崩法 3：IDE 死机 / 笔记本卡

**症状**：屏幕冻了 / 鼠标不响应 / IDE 无响应

**应急**：

1. 不要等它"自己恢复"——通常不会
2. 强制关闭 IDE / 重启笔记本（说："设备打个嗝，2 分钟搞定"）
3. 等待时讲解非演示部分（红线 / 真实事故 / 客户故事）—— 这部分**不依赖**屏幕

**预防**：
- 演示前关掉所有不必要的应用 / 浏览器 tab
- 笔记本预先重启过（"冷启动"）

---

## 崩法 4：测试失败（不应该但万一）

**症状**：现场跑 `python3 -m pytest tests/` → 红色

**应急**：

1. **不要慌张**——这反而是个教学时刻
2. 说："看，这就是为什么我们重视测试。我们现在现场 debug 一次"
3. 跑 `pytest -v` 看具体哪条 fail
4. 用 AI 协作流程实际 debug（[`workflows/engineering/debugging_workflow.md`](../../workflows/engineering/debugging_workflow.md) 6 步）
5. 修好后说："这就是真实工程协作的样子——不是'演示完美'，是'有失败也能通过流程恢复'"

**预防**：
- 演示前 30 分钟跑过一次测试，全绿才上场
- 不要在演示前 1 小时改代码

---

## 崩法 5：投影信号丢失

**症状**：台下大屏黑屏 / 信号闪烁

**应急**：

1. 打开纸质大字 slide（应急用）
2. 让大家围近一点看你的笔记本（小型培训 < 30 人 OK）
3. 如果纯黑屏不可恢复 → 改"白板讲法"——把红线 / 工作流写在白板上

**预防**：
- 演示前测投影 + 备一份打印 slides

---

## 崩法 6：忘词 / 卡壳

**症状**：你突然想不起来要讲什么

**应急**：

1. 暂停 1-2 秒（很自然，听众不会觉得不专业）
2. 说："让我看一下笔记"，看你提前打好的笔记（[`02_demo_script_keystroke_level.md`](02_demo_script_keystroke_level.md)）
3. 找回节奏后继续

**预防**：
- 提前练习 ≥ 1 次
- 笔记打印在纸上备份

---

## 崩法 7：观众问超出准备的问题

**症状**：有人问一个你不会答的难题

**应急**：

1. 诚实说："这个问题我现场答不准，怕给错误信息。我把它记下来在 [`training/post_conference/`](../post_conference/) 整理后回复"
2. 把问题写到笔记本上（让观众看到"被记下来"）
3. 继续推进

**预防**：
- 看 [`speaker_notes/anticipated_questions.md`](../speaker_notes/anticipated_questions.md)，提前准备 top-10 问题答案
- 不要假装知道一个你不知道的问题

---

## 崩法 8：时间不够 / 时间太多

**时间不够**：
- 砍 [`part_2_for_developers/02_prd_to_code_demo.md`](../part_2_for_developers/02_prd_to_code_demo.md) 的"反例对照"段（5 分钟，可省）
- 砍 [`part_2_for_developers/03_bug_to_fix_demo.md`](../part_2_for_developers/03_bug_to_fix_demo.md) 的"反例对照"段
- 让 Q&A 缩到 2 分钟

**时间太多**：
- 拉长动手练习（[`part_1_for_everyone/04_hands_on_exercise.md`](../part_1_for_everyone/04_hands_on_exercise.md)）
- 多让几位同事上来分享他们的 prompt
- 多回答 Q&A

---

## 通用心态

> 演示崩了不是事故——只要你**保持冷静 + 用 Plan B + 继续讲解**，听众会觉得你专业。
>
> 反过来——演示一切完美但你**听上去紧张** —— 听众反而会怀疑这套方法是不是真在用。
>
> **真实的故障 + 真实的应急处理 = 最好的"工程纪律"现场教学。**
