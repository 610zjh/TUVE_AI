# 用 AI 做代码评审 / Code Review with AI

> 适用：开发在做 PR 自查、互相评审、合并前最后一道关。
> For: engineers self-reviewing PRs, peer reviewing, last gate before merge.

---

## 一句话 / One Line

**AI 是评审的"第 0 道"，不是"最后一道"。** AI 抓低级错误（命名、unused、超长函数），人抓高级判断（架构、业务一致性）。
**AI is the "Gate 0", not the "final gate".** AI catches low-level (naming, unused, long functions), humans catch high-level (architecture, business consistency).

---

## 4 道关 / 4 Gates

```
作者自查 → AI 自动 → 同行评审 → 合并
Self-check → AI auto → Peer review → Merge
```

不要让 AI 替代任何一道。它**加一道**。
AI doesn't replace any gate. It **adds one**.

---

## 作者自查阶段 / Author Self-Check

提交 PR 前自己过一遍：
Before opening PR:

- [ ] PR 描述对应一份 PRD（编号）或一条 Bug 条目（编号）
- [ ] 单文件 ≤ 800 行（红线 #7）
- [ ] 命名按"5 年后还看得懂"（红线 #9）
- [ ] 删了 dead code / commented-out old code
- [ ] 反向断言测试已清理（红线 #13）
- [ ] 自己跑过基本验证
- [ ] PR 描述含 rollback 方案（如非 trivial）

---

## AI 自动评审阶段 / AI Auto-Review

### 用 AI 检查的 6 件事 / 6 Things AI Checks

```
请审下面这份 PR diff（粘贴）：

1. 有没有违反红线 #2 的客户面字符串（PRD 编号 / Bug 编号 / 内部代号）
2. 有没有违反红线 #9 的命名（demo_, sample_, placeholder_, tmp_, new_, final_）
3. 有没有 ≥ 800 行的文件（红线 #7）
4. 有没有"反向断言"测试残留（红线 #13）—— 看测试是不是断言了和现在代码相反的行为
5. 有没有不必要的防御性代码（catch all exception 但没具体处理）
6. 有没有"AI 套话"注释（"这里我用了 X 算法这种自我表扬"、"// 解释什么是 for 循环"）

把发现的问题分成：
- 必须修（违反红线 / 严重质量问题）
- 建议修（小质量问题）
- 风格观察（个人偏好级别）
```

### AI 不擅长检查的 / What AI Misses

| 类型 / Type | 为什么 / Why |
|---|---|
| **业务一致性** | AI 不知道你的业务；它检查的是代码本身的"看起来对" |
| **架构选择** | AI 倾向"建议加一个抽象层"——常常是过度工程 |
| **性能 / 并发** | 复杂场景下 AI 会给"看似合理但实际错"的建议 |
| **边界 case** | AI 抓不到你领域里的特殊边界 |
| **是否真的需要这个改动** | AI 默认假设"改动是必要的"，不会问"为什么改" |

这些**只有人能判断**。
**Only humans** can judge these.

---

## 同行评审阶段 / Peer Review

### 评审者的 5 个问题 / 5 Questions for Reviewer

每次评审问自己：
For each PR ask yourself:

1. **这个改动真的解决了它声称要解决的问题吗？** / Does it actually solve the stated problem?
2. **改动范围有没有超出 PRD / Bug 范围？** / In scope vs PRD/bug?
3. **新增的依赖 / 抽象 / 复杂度有必要吗？** / New deps / abstractions / complexity justified?
4. **如果上线后出问题，回退方案清晰吗？** / Rollback plan clear?
5. **6 个月后接手这块代码的人能看懂吗？** / Maintainable in 6 months?

### 评审注释的语气 / Review Comment Tone

- **直接陈述，不情绪化**："这里 X 在 Y 情况会失败，建议 Z" 比"你怎么没考虑 Y" 好
- **区分"必须改"和"建议"**：标记 `nit:` (preference) / `suggestion:` (recommended) / `blocker:` (must fix)
- **不评价人**：评价代码，不评价作者 / Critique code, not author

---

## 合并前最后一道 / Final Gate Before Merge

- [ ] CI 全绿 / CI green
- [ ] 至少 1 位同行评审 approve（重要改动 ≥ 2 位）/ ≥1 peer approval (≥2 for big changes)
- [ ] 所有 `blocker:` 注释已解决 / All blockers resolved
- [ ] PR 描述更新（如有变化）/ PR description updated
- [ ] commit message 干净（不是"WIP""asdf"那种）/ Commit messages clean

---

## 不需要评审就能合的 / Direct Merge OK

仅以下情况：
Only:
- typo 修正 / Typo fixes
- 文档纯排版调整 / Pure doc formatting
- 本地脚本 / 工具调整 / Local scripts / tooling tweaks

任何代码逻辑改动**都要走评审**。
Any code logic change → review required.

---

## 让 AI 帮你写 PR 描述 / AI-Assisted PR Description

```
我刚改了下面这些（git diff 粘贴）。请帮我起 PR 描述：

约束：
- 标题前缀按改动类型（feat: / fix: / refactor: / docs: / test: / chore:）
- 标题 ≤ 70 字
- 正文必含：
  - 关联 PRD / Bug 编号
  - 改动了什么 / 为什么改
  - 测试方法
  - rollback 方案（如果非 trivial）
- 不要"这是一个伟大的改动"这种废话
```

---

## 评审中的常见错误 / Common Review Mistakes

### 错误 1：作者顺手重构 / Drive-By Refactor

❌ 作者在修 Bug 时顺手"美化"了无关代码
**问题**：(1) 评审范围扩大 (2) 如果重构有问题，回滚 Bug 修复也连带 (3) 重构没在 PRD 里登记
**修复**：评审者要求作者**拆**——重构单独 PR

### 错误 2：评审者只看代码不看测试 / Skip Test Review

❌ 评审者只看代码改动，跳过测试
**问题**：测试是代码的一部分；测试如果错，等于代码错
**修复**：评审 = 代码 + 测试两个文件夹都看

### 错误 3：评审者只看新增不看删除 / Skip Deletion Review

❌ 评审者主要看 + 号行，忽略 - 号行
**问题**：删除常常是更危险的（"我以为这段没用"）
**修复**：评审 = + 和 - 都仔细看

### 错误 4：用 AI 自动 approve / AI Auto-Approve

❌ AI 给"一切看起来好"就直接合
**问题**：AI 不能判断业务一致性、架构合理性、是否真的需要这个改动
**修复**：AI 是 Gate 0；Gate 1 必须真人

### 错误 5：评审拖太久 / Slow Review

❌ PR 挂了一周没人评
**问题**：作者上下文丢失，回头改时容易引入新错
**修复**：团队 SLA：PR 提出后 24 工作小时内必须有第一次评审；72 小时内必须 approve 或明确指出还差什么

---

## 速查 / Cheat Sheet

```
4 道关：作者自查 → AI 自动 → 同行评审 → 合并

AI 抓：违反红线 / 命名 / 文件长度 / 反向断言 / 防御性代码 / AI 套话注释
人抓：业务一致性 / 架构 / 性能并发 / 边界 case / 是否真的需要

评审注释：直接 + 标 nit/suggestion/blocker / 评论代码不评论人

陷阱：顺手重构 / 跳过测试评审 / 跳过删除审 / AI 替代人 approve / 评审太慢
```
