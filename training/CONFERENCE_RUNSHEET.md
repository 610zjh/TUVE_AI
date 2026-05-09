---
name: 培训现场跑场单 / Conference Runsheet
retention: permanent
retention_reason: 演讲者当日对照的一页 facilitator reference，把分散在 part_1 / part_2 / live_demo / speaker_notes 的关键步骤聚合 / One-page facilitator reference unifying steps scattered across part_1 / part_2 / live_demo / speaker_notes
---

# 培训现场跑场单 / Conference Runsheet

> 演讲者当日把这份打印出来 / 放在另一块屏幕上对照执行。
> Print this for D-Day or keep it on a second screen.
>
> 详细脚本 / 讲稿在各分文件里；本份只是"现在该做哪一步"的索引。
> Detailed scripts / talk tracks live in their own files; this is just the "what step now" index.

---

## D-1（培训前一天）准备清单 / D-1 Prep Checklist

打勾后再走人 / Tick before leaving the office:

### 内容与边界
- [ ] 重读 [`speaker_notes/what_not_to_reveal.md`](speaker_notes/what_not_to_reveal.md) —— 当晚再读一遍**不该讲的清单**
- [ ] 重读 [`speaker_notes/anticipated_questions.md`](speaker_notes/anticipated_questions.md) —— 心里过一遍最难的 5 个问题怎么答
- [ ] 把 [`speaker_notes/timing_and_pacing.md`](speaker_notes/timing_and_pacing.md) 的时间块抄到手机日历提醒里

### 仓库就绪
- [ ] `cd TUZHAN_AI && bash setup.sh` 跑通，最后 5 项核心文件检查全 ✅
- [ ] `cd projects/customer_brief_generator && python3 -m pytest tests/ -v` 全过
- [ ] `python3 customer_brief_generator.py examples/sample_input.txt` 不带 API Key 跑出 template-fill 输出
- [ ] `export ANTHROPIC_API_KEY=...` 后再跑一次，确认带 AI 模式也跑通
- [ ] `git status` 干净，无未提交改动

### 设备与网络
- [ ] IDE（Claude Code / Cursor）字号调到 14-16pt（投影看得清）
- [ ] 关掉所有"会弹出私人通知"的 App（IM / 邮件 / 日历）
- [ ] 准备**移动热点**作为网络备份
- [ ] 准备 [`live_demo_walkthrough/03_recovery_if_things_break.md`](live_demo_walkthrough/03_recovery_if_things_break.md) 里写的"预生成输出截图"备份文件夹

### 现场材料
- [ ] U 盘 / 共享盘里放好 `TUZHAN_AI/` 的最新 zip（让现场没装 git 的人也能拷走）
- [ ] 打印 ~10 份本份 runsheet + ~10 份 [`workflows/ai_basics/how_to_give_clear_instructions.md`](../workflows/ai_basics/how_to_give_clear_instructions.md) 的"6 件事速查卡"放讲台前桌上

---

## D-Day 时间块 / Day-of Time Blocks

> 总长 ~3.5 小时（含中间 5 分钟休息）。
> 实际开场前 30 分钟到场。

### 09:30 - 10:00 · 开场前 30 分钟
- 到场，检查投影 / 麦克风 / 网络
- 把 IDE 打到大字号
- **开两个 IDE 对话窗口**（一个用作"反例"，一个用作"正例"，详见 [`live_demo_walkthrough/02_demo_script_keystroke_level.md`](live_demo_walkthrough/02_demo_script_keystroke_level.md) §A.3-A.4）
- 跑一次 [`projects/customer_brief_generator/`](../projects/customer_brief_generator/) 的 dry-run 确认环境就绪
- 站在台前接听众进场

### 10:00 - 10:10 · 第一部分 - 第 01 节 · 开场与动机（10 分钟）
- 文件：[`part_1_for_everyone/01_opening_and_motivation.md`](part_1_for_everyone/01_opening_and_motivation.md)
- 关键节点：
  - 2 分钟开场
  - 3 分钟讲 5 条核心信念（不背，但讲透）
  - 3 分钟讲今天讲什么
  - 2 分钟现场互动（三个举手问题）
- ⚠️ 不讲：本公司具体产品的实现 / 架构 / 真实客户名 / 真实合同金额（[`speaker_notes/what_not_to_reveal.md`](speaker_notes/what_not_to_reveal.md)）

### 10:10 - 10:35 · 第一部分 - 第 02 节 · 15 条红线快速过（25 分钟）
- 文件：[`part_1_for_everyone/02_core_principles.md`](part_1_for_everyone/02_core_principles.md)
- 关键节点：
  - 把 15 条分 4 组：(1) 外部沟通 #2/#3/#8 (2) 写下来 #5/#6/#10/#11 (3) 质量底线 #7/#9/#13/#14 (4) 业务方向 #1/#15/#12/#4
  - 4 分钟现场互动（3 个红线测验问题）
- ⚠️ 提到"真实事故"时，按 file 里写的脱敏版本讲，**不要 ad-lib 加细节**

### 10:35 - 11:00 · 第一部分 - 第 03 节 · 通用工作流走查（25 分钟）
- 文件：[`part_1_for_everyone/03_workflow_walkthrough.md`](part_1_for_everyone/03_workflow_walkthrough.md)
- 关键节点：
  - 10 分钟现场演示"6 件事检查清单"（**反例 → 正例**，按 [`live_demo_walkthrough/02_demo_script_keystroke_level.md`](live_demo_walkthrough/02_demo_script_keystroke_level.md) §A.3-A.6）
  - 10 分钟过 8 种 AI 失败模式
  - 5 分钟讲实战策略"让 AI 列 top-3 不确定"

### 11:00 - 11:25 · 第一部分 - 第 04 节 · 动手练习（25 分钟）
- 文件：[`part_1_for_everyone/04_hands_on_exercise.md`](part_1_for_everyone/04_hands_on_exercise.md)
- 关键节点：
  - 5 分钟准备（让全场打开自己的 IDE + 仓库）
  - 10 分钟练习 1（让 AI 起客户简报）
  - 5 分钟练习 2（让 AI 自查红线）
  - 5 分钟反思（45 分钟 → 12 分钟的对比 + 数学）

### 11:25 - 11:30 · 第一部分 - 第 05 节 · Q&A 和总结（5 分钟）
- 文件：[`part_1_for_everyone/05_qa_and_wrap.md`](part_1_for_everyone/05_qa_and_wrap.md)
- 关键节点：
  - 2 分钟总结
  - 1 分钟仓库导航（强调 [`AI_MANUAL.md`](../AI_MANUAL.md) 是"地图"）
  - 2 分钟 Q&A
  - **告诉非开发者可以离场了**

### 11:30 - 11:35 · 中间休息（5 分钟）
- 让非开发者离场
- 喝水 / 上厕所 / 检查设备
- 开发者留下

### 11:35 - 11:45 · 第二部分 - 第 01 节 · 工程场开场（10 分钟）
- 文件：[`part_2_for_developers/01_engineering_track_intro.md`](part_2_for_developers/01_engineering_track_intro.md)
- 关键节点：
  - 3 分钟欢迎 + 第二部分概述
  - 3 分钟工程纪律 vs 通用纪律的关系
  - 4 分钟工程师特殊角色（4 条理由）

### 11:45 - 12:15 · 第二部分 - 第 02 节 · PRD-到-代码现场演示（30 分钟）
- 文件：[`part_2_for_developers/02_prd_to_code_demo.md`](part_2_for_developers/02_prd_to_code_demo.md)
- 演示脚本：[`live_demo_walkthrough/02_demo_script_keystroke_level.md`](live_demo_walkthrough/02_demo_script_keystroke_level.md) §C
- 关键节点（按演示文件的 6 步走）：
  1. 打开 PRD-0002（**预先准备好的 PRD 草稿**）
  2. 让 AI 列澄清 top-3 问题
  3. 让 AI 起 Mermaid 实施图
  4. 让 AI 实施代码
  5. 跑五件套清单
  6. 看测试通过

### 12:15 - 12:40 · 第二部分 - 第 03 节 · Bug-到-修复现场演示（25 分钟）
- 文件：[`part_2_for_developers/03_bug_to_fix_demo.md`](part_2_for_developers/03_bug_to_fix_demo.md)
- 演示脚本：[`live_demo_walkthrough/02_demo_script_keystroke_level.md`](live_demo_walkthrough/02_demo_script_keystroke_level.md) §D
- 关键节点（按演示文件的 6 步走）：
  1. 拿"运 维 同 步 回 填"含空格的 input
  2. 跑工具看红线警告**没**触发
  3. 登记 [`issues/known.md`](../issues/known.md)
  4. 让 AI 定位根因
  5. 修 + 加回归测试
  6. 移位到 [`issues/fixed/`](../issues/fixed/)

### 12:40 - 12:55 · 第二部分 - 第 04 节 · 部署纪律 + 工程相关红线（15 分钟）
- 文件：[`part_2_for_developers/04_deployment_and_red_lines.md`](part_2_for_developers/04_deployment_and_red_lines.md)
- 关键节点：
  - 部署纪律的"灰度 → 测试 → 生产"链路
  - 工程相关 7 条红线深讲（#5 / #7 / #9 / #10 / #11 / #13 / #14）

### 12:55 - 13:05 · 第二部分 - 第 05 节 · Q&A + 下周作业（10 分钟）
- 文件：[`part_2_for_developers/05_qa_and_wrap.md`](part_2_for_developers/05_qa_and_wrap.md)
- 关键节点：
  - 5 分钟 Q&A
  - 5 分钟"下周作业"——挑一个真实 PRD 用这套方法做一次

### 13:05 · 散场 / End

- 收集"我从今天的培训带走的 1 件事是 ___"留言
- 把 U 盘 / 共享盘地址再发一遍

---

## 现场崩溃应急 / Emergency Recovery on Stage

完整路径见 [`live_demo_walkthrough/03_recovery_if_things_break.md`](live_demo_walkthrough/03_recovery_if_things_break.md)。

| 出问题 | 第一动作 | 备份手段 |
|---|---|---|
| AI 调用失败 | 切到 template-fill 模式（无 API Key） | 用预生成的输出截图讲解 |
| 网络断 | 切移动热点 | 用本地"已生成"的对话截图 |
| IDE 死机 | 重启（≤ 30 秒） | 切到 Plan B slides 讲方法论 |
| 测试失败（不应该发生） | 把"失败"作为教学时刻 | 让观众看真实 debug 过程 |
| 讲漏了不该讲的 | 1 秒内"撤回"（[`speaker_notes/what_not_to_reveal.md`](speaker_notes/what_not_to_reveal.md) §"我不小心讲漏了"）| 培训后 30 分钟内通报合规 |

---

## D+1（培训后第二天）收尾 / D+1 Wrap

- [ ] 在 [`workspace_human/meetings/`](../workspace_human/meetings/) 写 `YYYY-MM-DD_conference_retrospective.md`，记下：
  - 哪些段落听众反应最好 / 最差
  - 哪些问题来自哪些角色（销售 / 运营 / 开发）
  - 哪些建议反向更新到 [`workflows/`](../workflows/) 或 [`principles/`](../principles/)
- [ ] 把现场收集的"我带走的 1 件事"留言整理进 [`training/post_conference/feedback_collection.md`](post_conference/feedback_collection.md)
- [ ] 一周后做 30 分钟答疑回访（在群里发问"谁这周用过一次？分享一下"）

---

## 关键引用速查 / Key References at a Glance

| 你需要 | 看哪 |
|---|---|
| 某段讲不下去了，看演讲者笔记 | [`speaker_notes/`](speaker_notes/) |
| 现场演示崩了 | [`live_demo_walkthrough/03_recovery_if_things_break.md`](live_demo_walkthrough/03_recovery_if_things_break.md) |
| 不确定能不能讲 | [`speaker_notes/what_not_to_reveal.md`](speaker_notes/what_not_to_reveal.md) |
| 听众问的具体问题 | [`speaker_notes/anticipated_questions.md`](speaker_notes/anticipated_questions.md) |
| 时间没控制好 | [`speaker_notes/timing_and_pacing.md`](speaker_notes/timing_and_pacing.md) |
| 听众问"我能拿这份回我公司用吗" | [`README.md`](../README.md) §"二次复用" + [`LICENSE`](../LICENSE) |

---

## 红线 #2 / #18 现场提醒 / On-Stage Confidentiality Reminder

> 即使是合作伙伴 + 自己人，也禁止：
> - 真实客户名字
> - 真实合同金额 / 销售管线
> - 真实内部 PRD 编号 / Bug 编号 / 内部代号
> - 真实员工姓名（用角色代替）
> - 自家产品的具体技术架构 / 模型 ID / 接口名
>
> 教学示例统一用 `客户 A` / `PRD-XXXX` / `产品-L` / `运营-X` 这类**虚构占位**。
