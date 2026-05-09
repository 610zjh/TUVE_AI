---
name: 代码质量 / Code Quality
description: 命名、文件长度、注释、测试、删旧代码的纪律 / Discipline for naming, file length, comments, tests, removing dead code
type: permanent
retention: permanent
retention_reason: 工程师每天每个 commit 都用得上 / Used by engineers every day, every commit
---

# 代码质量 / Code Quality

## 1. 命名永久化（红线 #9）/ Names Are Forever (Red Line #9)

**禁止**的命名 / **Banned** name patterns:

| 反模式 / Anti-pattern | 例子 / Example | 改正 / Fix |
|---|---|---|
| `demo_*` | `demo_uploader.py` | 描述实际功能：`uploader.py` |
| `sample_*` | `sample_data.py` | 描述实际数据：`onboarding_seed_data.py` |
| `placeholder_*` | `placeholder_logic.py` | 写真实逻辑或者别建文件 |
| `test_*`（不是真测试时）/ when not actual tests | `test_new_flow.py` 里跑的是生产代码 | 测试文件单独放 `tests/`；生产代码用业务名 |
| `tmp_*` / `temp_*` | `tmp_calculator.py` | 直接用业务名 |
| `new_*` / `final_*` / `final_v2_*` | `new_pricing.py`, `final_v2_handler.py` | 不要用版本暗示词；让 git 管版本 |
| 拼音首字母乱拼 / Random pinyin abbreviations | `ckb_qcl.py` | 用完整词或英语 |
| 内部代号 / Internal codenames | `pegasus_module.py` | 用功能名（参考红线 #2）|

**原则**：每个名字假定**它会活 5 年**。5 年后还能让新同事一眼看懂"这是干什么的"，就 OK。否则改。
**Principle**: assume every name **lives 5 years**. If a future colleague can tell "what this does" in one glance 5 years from now → OK. Otherwise rename.

**例外**：纯演示代码 / 临时脚本 / 写完即删的，可以用 `scratch_*`，但**必须放在 `scratch/` 目录下**且不进生产 commit / 主分支。
**Exception**: pure scratch / one-off / write-and-delete scripts may use `scratch_*`, but **must live under `scratch/`** and never enter prod commits or main branch.

---

## 2. 单文件 ≤ 800 行（红线 #7）/ Single File ≤ 800 Lines (Red Line #7)

代码、Markdown、配置一律。超过 800 行 → 提 [`COMPACT-NNNN`](../../workspace_human/prd/) 拆分提案。
Code, Markdown, config — all the same. Over 800 lines → file a [`COMPACT-NNNN`](../../workspace_human/prd/) rollup proposal.

为什么 800 / Why 800:
- 屏幕能看到上下文的边界 / Context-window readability
- AI 工具一次能完整读进去的边界 / AI tools' single-read window
- 人类工作记忆极限 / Human working-memory limit

例外 / Exempt:
- 纯数据文件（CSV、大型 JSON、模型参数）/ Pure data files (CSV, large JSON, model params)
- 第三方库 vendored 进来的代码 / Vendored 3rd-party code
- 自动生成的 schema / migrations / Auto-generated schema / migrations

例外文件需要在仓库根 `.codeowners` 或 [`principles/000_CORE_RED_LINES.md`](../000_CORE_RED_LINES.md) 显式登记。
Exempt files must be explicitly registered in `.codeowners` or `000_CORE_RED_LINES.md`.

---

## 3. 注释纪律 / Comment Discipline

**默认不写注释**。每写一条问自己："这条注释如果删了，后人会不会被困惑？"
**Default to no comments**. For each one ask: "If I delete this, will a future reader be confused?"

应该写注释的情况 / When to comment:
- **隐藏的约束**："这个 sleep 是因为外部 API 有 rate limit" / Hidden constraint: "this sleep is because the external API rate-limits"
- **不显然的不变量**："这个列表必须按时间倒序，否则 §X 会出错" / Non-obvious invariant: "list must be in reverse-chrono, else §X breaks"
- **绕过的具体 Bug**："这里 + 1 是为了绕过 issue B-2026-0303-A" / Workaround for a specific bug
- **意外行为的解释**："看起来 dead code 但其实被反射调用" / Surprising behavior: "looks dead but reflectively called"

不应该写注释的情况 / When NOT to comment:
- ❌ 解释**做什么**（命名应该已经告诉你了）/ Explaining **what** (the name should already say)
- ❌ 引用当前任务 / Bug 编号（这些信息在 PR 描述里 + git blame 里）/ Citing current task / bug ID (lives in PR description + git blame)
- ❌ "// 这里我用了 XXX 算法" 之类自我表扬 / Self-praise like "// I used XXX algorithm"
- ❌ 长篇 docstring 描述显而易见的参数 / Long docstrings on obvious params

---

## 4. 函数 / 模块的边界 / Function / Module Boundaries

经验法则 / Heuristics:
- 一个函数做一件事，名字能用一句"动词 + 宾语"概括 / One function, one thing, named "verb + object"
- 函数体超过 50 行 → 八成是两件事在一起，拆 / > 50 lines → likely two things, split
- 函数参数超过 5 个 → 改用配置对象或拆函数 / > 5 params → use a config object or split
- 嵌套超过 3 层 → 用早期返回（early return）拍平 / > 3 levels nested → flatten with early returns

---

## 5. 修 Bug 同步清反向断言测试（红线 #13）/ Fix Bug → Clean Reverse-Assertion Tests (Red Line #13)

如果某个单元测试**断言了错误的旧行为**（让 Bug 绿灯过 CI），它是 Bug 的一部分。
If a unit test **asserts the old buggy behavior** (let the bug pass CI), it's part of the bug.

修 Bug 的同一个 commit 必须：
The fix commit must:
- 翻转这个测试（断言改成正确行为）/ Flip the test to assert correct behavior, OR
- 删除这个测试 / Delete it

**禁止**：
**Forbidden**:
- 修了代码但留着断言旧错误的测试，CI 因此红了 → 然后把测试 mark 为 skip / Code fixed, old test still asserting old behavior, CI breaks → mark test as skipped
- 把 Bug 修了但反向断言测试单独挂在 known.md 里"以后再清" / Fix the code but leave the reverse-assertion test in known.md "to clean later"

历史教训 / Historical lesson:
反向断言测试如果留下，未来某个 Agent 会以为"这是个新 Bug，怎么回事我们的测试在 fail"，浪费几小时定位发现是这条留下来的。
Leave the reverse-assertion behind, and a future Agent thinks "weird new bug, our test is failing", wastes hours diagnosing only to find this leftover.

---

## 6. Dead Code / 半成品 / 注释掉的旧代码 / Dead Code, Half-Built, Commented-Out Old Code

- **Dead code** 删掉。git 会记得它。
  Delete dead code. git remembers it.
- **半成品**不进主分支。要么完整、要么不进。
  Half-built code doesn't reach main. Complete or out.
- **被注释掉的旧代码**删掉。如果"以后可能要回退"——git 会记得。如果是"作为参考留着"——挪到文档里写清楚为什么。
  Delete commented-out old code. "Maybe revert" → git remembers. "For reference" → move to a doc with explicit reason.
- **`// TODO: 改` 写了 6 个月没动**——不再是 TODO，是事实。要么修，要么删，要么提到 known.md 当 Bug。
  `// TODO: fix later` sitting 6 months → no longer a TODO, it's a fact. Fix, delete, or file in known.md.

---

## 7. 防御性代码 / 错误处理 / Defensive Code and Error Handling

不必要的防御性代码是 noise / Unnecessary defensive code is noise:

- ❌ 内部函数 A 调内部函数 B，在 A 里 try/except B 抛的异常 / Internal function A calling internal B, wrapping in try/except for "safety"
- ❌ 对一个永远不会是 None 的参数 `if x is None: return` / `if x is None: return` for a param that's never None
- ❌ 把所有 exception 都 catch 掉以"避免崩溃" / Catching every Exception to "avoid crashes"

应该有的防御 / Necessary defense:
- ✅ 系统边界（接收用户输入、调外部 API、读文件）/ System boundaries (user input, external APIs, file IO)
- ✅ 真的可能失败的操作（网络、并发、第三方）/ Genuinely failure-prone (network, concurrency, 3rd party)
- ✅ 失败有具体处理方案的（重试 / 兜底 / 报警），而不是"static catch + 静默吞掉" / Failure with concrete handling (retry / fallback / alert), not "static catch + silent swallow"

---

## 8. Code Review 的纪律 / Code Review Discipline

**评审前自查**：
**Self-check before requesting review**:
- [ ] PR 描述对应一个 PRD 或 Bug
- [ ] 不超过 800 行单文件
- [ ] 命名按"5 年后还看得懂"
- [ ] 删了 dead code / commented-out old code
- [ ] 反向断言测试已清理
- [ ] 自己跑过基本验证

**评审时关注**：
**Focus during review**:
- 这个改动**真的解决了**它声称要解决的问题吗？/ Does it actually solve the stated problem?
- 改动范围是否**超出了**这个 PRD / Bug 的范围？（顺手重构是反模式）/ Does it stay within the PRD / Bug scope? (Drive-by refactors are anti-pattern)
- 命名 / 注释是否符合上面 1, 3 节？/ Naming and comments per §1, §3 above?
- 是否引入了新依赖？引入的理由站得住吗？/ New dependencies? Justified?
- 测试覆盖是否对应了改动？/ Test coverage matches the change?

不需要评审的（可直接合）/ Direct merge OK (no review):
- typo 修正 / Typo fixes
- 文档纯排版调整 / Pure doc formatting
- 本地脚本 / 工具调整 / Local scripts / tooling tweaks

---

## 9. 不要"顺手"做没授权的重构 / No Drive-By Refactors

修一个 Bug 时只改 Bug 相关的代码。
When fixing a bug, only change the bug-related code.

❌ "我修这个 Bug 时看到旁边的函数命名不好，就顺手改了"
**问题**：(1) 改动范围扩大，review 难度上升；(2) 如果重构有问题，回滚 Bug 修复也连带回滚；(3) 你没在 PRD 里登记这个重构。
**Issues**: (1) review scope balloons; (2) if refactor breaks, bug fix rolls back too; (3) refactor wasn't in any PRD.

✅ 看到顺手能改的小问题 → 在 [`issues/known.md`](../../issues/known.md) 立一条小 Bug，下个独立 PR 修。
**Right**: spotted a small adjacent issue → file a small bug in [`issues/known.md`](../../issues/known.md), fix in a separate PR.

例外：单纯空格 / typo 这种 0 风险的改可以顺手；但 commit message 要单独写一行 "drive-by typo fix"。
Exception: pure whitespace / typo of 0 risk can ride along, but the commit message gets a separate line "drive-by typo fix".

---

## 10. 提 commit / PR 时的纪律 / Commit / PR Discipline

- commit message 解释**为什么**改，不解释**改了什么**（diff 已经显示了）/ Explain **why**, not **what** (diff shows what)
- 一个 PR 解决一件事。一个 PR 修 3 个不相关的 Bug 是反模式 / One PR, one thing. Three unrelated bugs in one PR = anti-pattern
- PR 标题前缀按类型：`fix:` / `feat:` / `refactor:` / `docs:` / `test:` / `chore:` / Prefix per type
- PR 正文必须包含：关联 PRD / Bug 编号 + 测试方法 + rollback 方案（如非 trivial）/ PR body must include: PRD/Bug ref + test plan + rollback plan (if non-trivial)
