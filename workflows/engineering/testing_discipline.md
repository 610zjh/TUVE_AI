---
name: 测试纪律 / Testing Discipline
retention: permanent
retention_reason: 工程团队长期复用的测试原则与取舍 / Long-lived testing principles for engineering teams
---

# 测试纪律 / Testing Discipline

> 适用：所有开发。从单元测试到端到端测试的写法和取舍。
> For: every engineer. From unit tests to end-to-end tests.

---

## 一句话 / One Line

**测试不是为了"覆盖率"，是为了"未来这段代码被改错时能立刻知道"。**
**Tests aren't for "coverage"; they're so future-you knows immediately when this code is broken.**

---

## 测试金字塔 / Testing Pyramid

```
       /\
      /E2\         端到端 (少而宝贵)
     /----\
    / 集成  \      集成测试 (中等量)
   /--------\
  /  单元    \     单元测试 (多)
 /------------\
```

**单元测试**：测一个函数 / 一个类的行为；快、孤立、多 / Unit: function / class behavior; fast, isolated, many
**集成测试**：测多个组件之间的协作；中速、半隔离 / Integration: components together; medium speed, semi-isolated
**端到端测试**：测真实用户路径；慢但必要 / E2E: real user paths; slow but necessary

每层都不可缺。但比例：单元 70% / 集成 20% / E2E 10%。
All layers needed. Ratio: unit 70% / integration 20% / E2E 10%.

---

## 单元测试的写法 / Writing Unit Tests

### "AAA"结构 / AAA Structure

```python
def test_<被测函数>_<在什么情况下>_<期望什么>():
    # Arrange — 准备输入和上下文
    input_a = ...
    input_b = ...

    # Act — 调用被测代码
    result = function_under_test(input_a, input_b)

    # Assert — 断言结果
    assert result == expected
```

### 一个测试只测一件事 / One Test, One Thing

❌ 一个测试同时验证"返回值 + 副作用 + 异常"——失败时不知道哪个出问题
**修复**：拆成 3 个测试。

### 测试名字要"自说明" / Self-Documenting Test Names

❌ `test_func1`
✅ `test_calculate_pricing_with_no_discount_returns_base_price`

测试名 = 一句话陈述"在什么情况下应该发生什么"。
Test name = a sentence "when X, expect Y".

### 测什么 / What to Test

- ✅ 业务逻辑（条件分支、算法核心）/ Business logic
- ✅ 边界 case（空 / 极大 / 极小 / 非法）/ Edge cases
- ✅ 错误处理（应该抛什么异常 / 应该返回什么错误）/ Error handling
- ✅ 修过的 bug（每个 bug 一个回归测试）/ Fixed bugs

不必测 / Don't test:
- ❌ 框架本身的行为（你测不出 Django 的 ORM 是不是对）
- ❌ 第三方库（应当假设它们是对的，除非你怀疑）
- ❌ 简单的 getter/setter
- ❌ 系统级别的（OS、网络）

---

## 集成测试 / Integration Tests

测两个或更多组件协作的：
Tests for cooperating components:

- 你的服务 + 数据库 / Your service + DB
- 服务 A 调服务 B / Service A calling B
- 异步任务执行后的状态 / Async task post-state

### 集成测试用真实数据库 / Use Real DB for Integration

不要 mock 数据库。
Don't mock the DB.

历史教训：mock 过的测试可能让"实际生产中数据库行为变化"被掩盖（比如 SQL 写法 mock 时通过，但真数据库迁移失败）。
Historical lesson: mocks may mask actual DB behavior changes (SQL passes mock but fails real migration).

集成测试用 docker / 测试服小数据库实例。慢一点没关系。
Integration tests use docker / staging-small DBs. Slower is fine.

---

## 端到端测试 / End-to-End Tests

测最关键的用户路径（happy path 和最重要的 sad path）：
Test critical user journeys (happy + most important sad):

- 用户注册 → 登录 → 完成核心动作 / Sign up → log in → core action
- 客户付费 → 看到付费功能 / Pay → see paid feature
- 关键工作流不被破坏 / Critical workflows preserved

E2E 测试慢（每条几秒到几分钟），所以**只测最关键的路径**。
E2E is slow (seconds to minutes), so **only critical paths**.

---

## 测试与 Bug 的关系（红线 #13）/ Tests and Bugs (Red Line #13)

每个 bug 修复必须有：
Each bug fix must have:

1. **新增的回归测试** —— 输入是 bug 复现条件，断言是修复后的正确行为
   New regression test — input reproduces bug, asserts correct behavior post-fix
2. **同步清理"反向断言"测试** —— 如果某测试当时断言了错误的旧行为（让 bug 绿灯过 CI），它是 bug 的一部分
   Clean reverse-assertion tests — tests that asserted the buggy behavior are part of the bug

红线 #13 完整规则见 [`principles/subs/code_quality.md`](../../principles/subs/code_quality.md) §5。

---

## "测什么" 的优先级 / Priority of "What to Test"

修 / 加任何代码时，按优先级测：
When fixing / adding code, by priority:

```
P0: 修过的 bug → 必有回归测试
P1: 业务关键路径（付费 / 数据写入 / 客户面动作）→ 集成 + E2E
P2: 业务核心逻辑（计费 / 排序 / 推荐）→ 单元
P3: 边界 case → 单元
P4: 内部工具 / 脚本 → 简单冒烟
```

不要追求 100% 覆盖率；追求"重要的部分有测试"。
Don't chase 100% coverage; chase "important parts are tested".

---

## 测试反模式 / Testing Anti-Patterns

### 反模式 1：测试在测试自己 / Tests Testing Themselves

❌ 测试代码用了和被测代码一模一样的逻辑
**问题**：测试和代码一起错，测试没法发现
**修复**：测试和代码用**不同实现思路**得到相同结果

### 反模式 2：mock 一切 / Mock Everything

❌ 数据库 mock、第三方 mock、文件系统 mock、时间 mock 全 mock 上
**问题**：测试通过了但实际生产里全错
**修复**：mock 只用在"真实依赖代价大"的地方（如外部付费 API）

### 反模式 3：测试依赖顺序 / Tests Depend on Order

❌ 测试 A 必须在测试 B 之前跑，否则失败
**问题**：CI 改个执行顺序就崩
**修复**：每个测试自己 setup + teardown，互相隔离

### 反模式 4：偶尔失败的测试（flaky）/ Flaky Tests

❌ "这个测试经常 fail，retry 几次就过了"
**问题**：你失去了对测试结果的信任
**修复**：flaky 测试**必须**修。修不了 → 在 [`issues/known.md`](../../issues/known.md) 登记 + 临时 skip 但有 ETA

### 反模式 5：测试覆盖率被当成 KPI / Coverage as KPI

❌ "我们要 100% 覆盖率"
**问题**：诱导写"测试存在但不真验证"的水货
**修复**：覆盖率是参考；重要是**质量**

---

## AI 协助写测试 / AI-Assisted Test Writing

```
我刚写了下面的代码：[粘贴]

请帮我列出 top-N 应该测试的 case：
1. Happy path
2. 边界 case（空 / 极大 / 极小 / 非法）
3. 错误处理（应该抛什么异常 / 返回什么错误）
4. 与历史 bug 相关的（如果这块代码改过）

每个 case 给出：
- 测试名（自说明的）
- 输入
- 期望输出 / 行为
- AAA 结构的代码

约束：
- 一个测试一件事
- 测试名是"在什么情况下应该发生什么"的句子
- 不要 mock 数据库（用 docker）
```

⚠️ AI 容易：
- 漏边界 case → 自己补
- 给"看起来通过但其实没真验证"的测试 → 抽查每条断言
- 在测试代码里**重新写一遍**被测代码 → 发现立刻删

---

## 速查 / Cheat Sheet

```
金字塔：单元 70% / 集成 20% / E2E 10%

单元：AAA 结构 / 一个测试一件事 / 测试名自说明

集成：用真实 DB（不 mock）

E2E：仅关键路径

每个 bug 必有：回归测试 + 反向断言测试已清

陷阱：测试在测自己 / mock 一切 / 测试依赖顺序 / flaky / 覆盖率当 KPI
```
