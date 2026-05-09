---
name: 02 - 现场演示逐步脚本
retention: permanent
retention_reason: 演讲者需要的"按键级"演示脚本
---

# 现场演示逐步脚本 / Live Demo Script (Keystroke-Level)

> 演讲者按这个脚本逐步操作，听众看到的是"按键级"的演示，无 ad-libbing 风险。
> Speaker follows this step by step; audience sees a keystroke-level demo with no ad-libbing risk.

---

## 演示 A：客户简报生成器（第 1 部分用，~10 分钟）

### A.1 打开 IDE 和仓库

- 打开 Claude Code（或 Cursor，看你练得熟的）
- 打开 `/Users/.../TUZHAN_AI/`（或 demo 用的副本路径）
- 确认 IDE 字号大（14-16pt 或更大）

### A.2 第一条消息

输入：

```
请先读 AI_MANUAL.md 了解项目导航，然后我会告诉你今天要做什么。
```

- 等 AI 加载 AI_MANUAL.md 完毕（约 5-10 秒）
- 给观众讲："看，AI 自动找到了入口文件 + 红线 + 导航地图"

### A.3 第二条消息（**反例**）

切换到第二个对话（让观众看到"如果不用方法论会怎样"）。输入：

```
帮我写一份客户跟进邮件。
```

- AI 给"通用模板"
- 让观众看：什么客户都不知道、给的内容空洞

### A.4 第三条消息（**正例**）

回到第一个对话。输入：

```
帮我写一份给客户 A（教育-中型）的跟进邮件。

背景：上周二我们和"客户 A"开了第一次需求对齐会。客户对短视频 AI 自动化感兴趣，
但担心数据合规。

目标：让对接人感觉"我们听到了你的需求"，并提议下周二上午做一次产品演示。

边界：
- 不要捏造没在会上发生的事
- 不要在邮件里出现 PRD 编号 / Bug 编号 / 内部代号（红线 #2）
- 不要点名其他客户

形式：
- 中文，约 200 字
- 三段式：感谢 / 回应担心 / 提议下一步

不确定就问：列出 top-3 你最不确定的点，我先回答你再开始。
```

- AI 应该先列 top-3 不确定问题（如果它直接写邮件，让观众看到这是"它该问没问"）
- 假设 AI 列了不确定，回复：

```
1. 邮件主题：建议"下周二产品演示邀约"
2. 上次对接人是 X（我已经在 CRM 里有他的邮箱）
3. 关于数据合规我们承诺：会议中我答应"周五前发合规白皮书"
```

- AI 给出邮件草稿
- **关键**：让观众看到草稿内容**没有** PRD 编号、内部代号、其他客户名

### A.5 让 AI 自查红线

输入：

```
对你刚写的邮件自查：

闸 1（关键词 grep）：扫一遍是否含 PRD-XXXX、Bug-XXXX、模型 endpoint、内部岗位代号、其他客户名
闸 2（品牌声音）：是不是 TUZHAN 的语气（不堆形容词、不 AI 套话）
闸 3（法务可承诺）：所有承诺都能兑现吗？

列出违规处 + 修改建议。
```

- AI 应该自己说"全部三道闸通过"或者"闸 X 发现 ..."
- 让观众看 AI 是怎么自我检查的

### A.6 收尾

> "看，这就是 6 件事检查清单 + 三道闸的实战。整个过程从开始到产出可用草稿大约 5 分钟。"

---

## 演示 B：customer_brief_generator 工具跑一次（第 1 部分用，~5 分钟）

### B.1 切到终端

```bash
cd /Users/.../TUZHAN_AI/projects/customer_brief_generator/
ls examples/
```

- 让观众看 examples/ 目录里有什么

### B.2 跑工具

```bash
python3 customer_brief_generator.py examples/sample_input.txt
```

- 不带 ANTHROPIC_API_KEY → 工具进入 template-fill 模式
- 让观众看输出文件路径

### B.3 看输出

```bash
ls -la output/
cat output/2026-05-08_客户-A-教育-中型_external.md
```

- 让观众看实际输出
- 展示**红线检查警告**（如果有）

### B.4 跑测试

```bash
python3 -m pytest tests/ -v
```

- 让观众看 20 条测试**全过**
- 强调："这就是工程纪律——任何工具都有测试"

### B.5 清理

```bash
rm -rf output/
```

- "演示完不要把 output 文件留在仓库里——它是 runtime artifact"

---

## 演示 C：PRD-到-代码（第 2 部分用，~30 分钟）

按 [`part_2_for_developers/02_prd_to_code_demo.md`](../part_2_for_developers/02_prd_to_code_demo.md) 走。

关键节点：
1. 打开 PRD-0002（要预先准备好这份 PRD 草稿）
2. 让 AI 列澄清 top-3
3. 让 AI 起 Mermaid 实施图
4. 让 AI 实施
5. 跑五件套清单

---

## 演示 D：Bug-到-修复（第 2 部分用，~25 分钟）

按 [`part_2_for_developers/03_bug_to_fix_demo.md`](../part_2_for_developers/03_bug_to_fix_demo.md) 走。

关键节点：
1. 拿"运 维 同 步 回 填"含空格的 input
2. 跑工具看红线警告**没**触发
3. 登记 known.md
4. 让 AI 定位根因
5. 修 + 加回归测试
6. 移位到 fixed/

---

## 应急：现场演示崩了怎么办

详见 [`03_recovery_if_things_break.md`](03_recovery_if_things_break.md)。

要点：
- AI 调用失败 → 切到模板模式 + 用预生成的输出
- 网络断 → 切移动热点 / 用本地的"已生成"对话截图
- IDE 死机 → 重启 + 用 Plan B slides 应急
- 测试失败（实际不应该发生）→ 把"失败"作为教学时刻：让观众看真实 debug
