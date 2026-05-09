# 调试 / Debugging Workflow

> 适用：所有开发遇到 bug 时的标准工作流。
> For: every engineer when hitting a bug.

---

## 一句话 / One Line

**调试的第 1 个动作是收集事实，不是猜原因。** 红线 #14：先看日志，不超过 3 轮静态猜测。
**Action #1 is gathering facts, not guessing causes.** Red Line #14: logs first, ≤ 3 rounds of static guessing.

---

## 5 步法 / 5-Step Process

### 步 1：稳定复现 / Step 1: Reproduce

不能稳定复现的 bug 是最难修的。先花时间在"如何稳定复现"。
Bugs that can't be reliably reproduced are the hardest to fix. Invest in reproduction first.

```
请帮我把下面这个 bug 报告整理成"复现步骤"：

[Bug 描述、客户原话、错误截图]

输出：
1. 前置条件（用户角色、数据状态、环境）
2. 步骤 1, 2, 3 ...
3. 预期结果 vs 实际结果
4. 复现率（每次都能 / 偶发 / 仅特定情境）
5. 如果复现率不是 100%，列出可能影响因素
```

### 步 2：拉真实日志 / Step 2: Pull Real Logs

红线 #14。不看日志前不超过 3 轮静态猜测。
Red Line #14. ≤ 3 rounds before logs.

```
拉日志的标准命令（按你公司基础设施填）：
- 测试服：[ssh xxx 'docker logs xxx 2>&1 | grep -E "Traceback|500"']
- 正式服：[ssh xxx 'docker logs xxx 2>&1 | grep -E "Traceback|500"']

要拿到的关键信息：
- 完整 traceback（不是只第一行）
- 错误发生时间
- 上下游请求信息
- 当时的并发量 / 数据量
```

### 步 3：定位根因 / Step 3: Find Root Cause

```
我有了 traceback：[粘贴]
和复现步骤：[粘贴]

请：
1. 解读 traceback 的关键栈层
2. 列 top-3 最可能的根本原因（不是表面症状）
3. 每个根因对应一个"如果是这个，我应该看到 [现象] / 数据"的可证伪检查
4. 我应该按什么顺序验证这 3 个根因
```

注意：不要在没看 traceback 前让 AI 推测根因——它会给"听起来合理但实际错"的答案。
Don't guess root cause before logs — AI gives "plausible-sounding but wrong" answers.

### 步 4：修复 / Step 4: Fix

修法两类：
Two flavors:

**修根因 / Root-cause fix**:
- 改代码让 bug 不再发生
- 加回归测试断言修复后的行为（红线 #13）
- 同步**翻转或删除**断言旧错误行为的测试（红线 #13）

**workaround / 绕行**:
- 短期止损用，**必须**同时记录到 [`issues/known.md`](../../issues/known.md)
- 48 小时内出根因修复 PR

### 步 5：验证 + 收尾 / Step 5: Verify + Closeout

- [ ] 修复后再跑复现步骤——bug 消失
- [ ] 回归测试通过
- [ ] 反向断言测试已清理
- [ ] [`issues/known.md`](../../issues/known.md) 中的条目移到 [`issues/fixed/YYYY-MM-DD.md`](../../issues/fixed/) 整条搬
- [ ] PR 描述含 root cause 一句话 + 测试方法
- [ ] 客户告知（如果客户报的 + 影响范围足够）

---

## "猜代码"的反模式 / The "Guess Code" Anti-Pattern

经典违规场景：
Classic violation:

```
用户：线上挂了
AI：让我看看代码 ... grep ... 我猜可能是 X 导致 ... 你试试这个修复
（10 轮过去了，AI 一直在猜，从来没看真实日志）
```

为什么这是反模式：
Why anti-pattern:
- grep 代码看起来"在干活"，但实际上对真实运行时状态零信息
- 猜的修复可能"蒙对"也可能"加新 bug"
- 浪费工程师 / 客户成功 / 客户的时间

**修复**：把"先看日志"做成肌肉记忆。任何"线上 / 测试服 / XX 挂了"出现的瞬间，第 1 个动作打开 SSH 拉日志。
**Fix**: make "logs first" muscle memory. The instant "production / staging is down" appears, action #1 = SSH and pull logs.

---

## 调试中的常见错误 / Common Debugging Errors

### 错误 1：第一个看起来对的修复就提交 / First-Plausible Fix

❌ "这里加个 if x is None: return 应该能修"
**问题**：在没真正理解根因前就掩盖症状
**修复**：先回答"这个 None 是从哪来的？"再决定怎么处理

### 错误 2：不写回归测试 / No Regression Test

❌ 修了 bug 就直接合
**问题**：未来同样的 bug 会再次出现，没人发现
**修复**：每个 Bug 修复必有回归测试断言"这个输入下行为是 X"

### 错误 3：留反向断言测试 / Leave Reverse-Assertion Tests

❌ 修代码后单元测试 fail（因为它断言了旧的错误行为）→ mark as skip
**问题**：违反红线 #13
**修复**：在同一个 PR 里翻转或删除该测试

### 错误 4：修一个 bug 顺手"修"另一个 / Side-Quest Fixes

❌ 修 Bug A 时顺手"修"了 Bug B
**问题**：评审范围扩大、回滚困难、Bug B 没经过完整流程
**修复**：拆 PR，每个 Bug 单独修

### 错误 5：不更新 known.md / Forget known.md

❌ 修完 bug 但忘了把 known.md 里的条目移到 fixed/
**问题**：违反红线 #4 SSOT
**修复**：合 PR 当天就移

---

## 偶发 bug 的特殊纪律 / Special Discipline for Flaky Bugs

某些 bug 每次都能复现 → 容易调试。
Some bugs reproduce every time → easy to debug.

某些 bug **偶发**（5% 概率发生）→ 难调试。
Some are **flaky** (5% reproduction) → hard to debug.

偶发 bug 的常见根因：
Common flaky-bug root causes:
- 并发 / 时序问题 / Concurrency / timing
- 上游状态变化（缓存 / 第三方 / 数据迁移）/ Upstream state changes
- 浮点数精度 / 时区 / Locale / Float precision / timezone / locale
- 测试与生产环境差异 / Staging-prod divergence

操作：
Ops:
- 不要在 100 次跑里"偶尔成功"就当修好了——必须 100 次都通过
- 把偶发 bug 的复现脚本沉淀，跑成 CI 的一部分
- 修了之后**至少跑 1000 次**确认不再偶发
- 长期不能修的偶发 bug **登记到** [`issues/known.md`](../../issues/known.md)，标"flaky"，由团队优先级决定何时啃

---

## 速查 / Cheat Sheet

```
红线 #14：第 1 动作看日志，不超过 3 轮静态猜测

5 步：稳定复现 → 拉日志 → 找根因（3 个候选 + 验证顺序）→ 修复 → 验证 + 收尾

修复两类：根因修 / workaround（必须同步登记 + 48h 内根因修）

陷阱：第一个看起来对的修复 / 不写回归测试 / 留反向断言 / 顺手修旁边 / 忘 known.md
```
