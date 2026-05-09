# projects/

> 实际项目目录。新项目建在这里。
> Actual projects directory. Place new projects here.

---

## 当前项目

- [`customer_brief_generator/`](customer_brief_generator/) —— 一个完整可跑的样例项目，把销售电话的原始笔记转成结构化的客户简报。**保留作为 onboarding / 学习参考**；如果你团队不需要这个工具，可以保留作为方法论展示。

---

## 起新项目

1. 在本目录新建文件夹：`projects/<your-project-name>/`
2. 项目内必含：
   - `README.md` —— 项目介绍 + 怎么跑
   - `workspace_human/prd/` —— 该项目的 PRD（如果项目有自己的需求）
3. 跨项目共享的红线 / 工作流 / 模板由仓库根的 `principles/` / `workflows/` / `templates/` 提供——**不必每个项目重复**

---

## 项目命名

按"它做什么"命名，不是"代号"或"demo"：
- ✅ `customer_brief_generator/`
- ✅ `weekly_metrics_dashboard/`
- ❌ `project_alpha/`（代号）
- ❌ `demo_app/`（demo-only 命名）
- ❌ `test_project/`（违反红线 #9）

---

## 项目内的代码红线

每个项目的代码都遵守仓库根的红线：
- 红线 #7（单文件 ≤ 800 行）
- 红线 #9（命名永久化）
- 红线 #13（修 Bug 同步清反向断言测试）
- 红线 #5（PRD 在前）

详见 [`principles/000_CORE_RED_LINES.md`](../principles/000_CORE_RED_LINES.md)。
