# Customer Brief Generator

> 把销售电话 / 拜访的原始笔记转成结构化的客户简报。
> Turns raw sales-call notes into a structured customer brief.

约 200 行 Python，可单文件运行。
~200 lines of Python, runs as a single script.

---

## 为什么有这个工具 / Why

销售每次电话后要花 30-60 分钟整理跟进材料（参见 [`workflows/customer_communication/sales_call_followup.md`](../../workflows/customer_communication/sales_call_followup.md)）。这个工具用 AI 把整理时间降到 5-10 分钟。

工具承诺：
- 把原始笔记结构化成 [`templates/customer_brief/`](../../templates/customer_brief/) 模板格式
- 客户面文案过红线 #2 自查（grep 内部代号 / 客户名等）
- 输出两份：给客户看的简报版 + 给内部团队的简报版

工具**不**做的：
- 不替代你的判断（AI 给草稿，你审核 + 定稿）
- 不发送邮件（红线 #8）
- 不存任何客户数据到外部服务（除你配置的 AI 厂商）

---

## 怎么跑 / How to Run

### 前置条件

```bash
# Python 3.10+
python3 --version

# 安装依赖
pip install anthropic
```

设置环境变量：
```bash
export ANTHROPIC_API_KEY="sk-ant-..."  # 你的 Claude API key
```

> 没有 API key 也能跑——会以"模板填充模式" 输出，不调 AI。

### 跑一次

```bash
# 1. 准备一份你今天的电话笔记
cp examples/sample_input.txt my_call_notes.txt
# 编辑 my_call_notes.txt，填写真实笔记（脱敏！客户名 / 金额按红线 #3）

# 2. 运行
python3 customer_brief_generator.py my_call_notes.txt

# 3. 看输出
ls -lt output/
# 会有两个文件：
# - <date>_<customer-label>_external.md  给客户看的版本
# - <date>_<customer-label>_internal.md  给内部团队的版本
```

### 跑测试

```bash
python3 -m pytest tests/
```

---

## 文件结构 / Files

```
customer_brief_generator/
├── README.md                              ← 你正在看
├── customer_brief_generator.py            ← 主脚本
├── prompts/
│   ├── extract_facts.md                   ← 提取事实的 prompt
│   ├── draft_external.md                  ← 起草客户面简报的 prompt
│   └── draft_internal.md                  ← 起草内部简报的 prompt
├── examples/
│   ├── sample_input.txt                   ← 笔记输入示例
│   ├── sample_output_external.md          ← 客户面简报输出示例
│   └── sample_output_internal.md          ← 内部简报输出示例
├── tests/
│   ├── test_redaction.py                  ← 红线 #2 / #3 自查测试
│   └── test_template_filling.py           ← 模板填充测试
└── workspace_human/
    └── prd/
        └── PRD-0001_customer_brief_generator.md  ← 这个工具的 PRD
```

---

## 这个项目作为"教学样本" / This Project as Teaching Sample

新人按下面顺序读这个项目，能看到 TUZHAN_AI 方法论怎么落地：

1. [`workspace_human/prd/PRD-0001_*.md`](workspace_human/prd/PRD-0001_customer_brief_generator.md) —— 一份完整的 PRD（含主次审视段）
2. [`customer_brief_generator.py`](customer_brief_generator.py) —— 工程纪律（命名、文件长度、红线 #2 自查 hook）
3. [`tests/`](tests/) —— 测试纪律（含针对红线 #2 / #3 的反向断言保护）
4. [`prompts/`](prompts/) —— 提示词模式库（[`workflows/ai_basics/prompt_pattern_library.md`](../../workflows/ai_basics/prompt_pattern_library.md) 的真实应用）

整个项目展示：**红线 + 工作流 + 模板** 在一个真实的代码项目里**怎么串起来**。

---

## 红线在这个项目里的体现 / Red Lines in This Project

- **红线 #2**（客户面文案）：脚本输出"external" 简报前自查，扫到 PRD 编号 / 内部岗位代号 / 客户名 → 报警
- **红线 #3**（保密数据）：默认假设输入笔记**已脱敏**——脚本会扫常见的"未脱敏"模式（手机号 / 邮箱 / 身份证），发现就警告并退出
- **红线 #5**（PRD 在前）：本项目自身有 PRD-0001
- **红线 #7**（单文件 ≤ 800 行）：主脚本 200 行
- **红线 #8**（不可逆动作要确认）：脚本不发送邮件，只生成本地文件
- **红线 #9**（命名永久化）：所有变量 / 函数命名按"5 年后还看得懂"
- **红线 #10**（收尾五件套）：项目附带测试 + 版本登记 + PRD 完成快照
- **红线 #15**（主次审视）：PRD-0001 的 §6 详细审视

---

## 二次复用 / Adoption

如果你（合作伙伴）想拿这个项目用作起点：
- 直接 `cp -r customer_brief_generator/ your_project_name/` 改名
- 改 prompts/ 里的提示词以匹配你公司的语境
- 改 PRD 起新的需求
- 改 tests/ 里的红线检查（匹配你公司的内部代号）
