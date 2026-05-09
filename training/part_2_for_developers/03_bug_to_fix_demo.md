---
name: 03 - Bug 到修复现场演示
retention: permanent
retention_reason: 培训第二部分核心演示段
---

# 第二部分 - 第 03 节：Bug-到-修复 现场演示（25 分钟）

> Part 2, Section 03: Bug-to-Fix Live Demo (~25 min)

---

## 演示场景

我们现场修一个 **Bug**：让 customer_brief_generator 的红线 #2 检查更全面（当前只覆盖 PRD 编号 / Bug 编号 / 内部代号 / 模型 ID，但漏了"内部排期措辞"如"运维同步回填""下个迭代"）。

实际上这个 Bug 已经在 PRD-0001 中被涵盖（红线 #2 完整列表），但有一个微妙的 case：**"运维同步回填"** 如果是带空格或换行的形式，原始 regex 可能漏抓。

完整 6 步都演示：
1. 复现 + 看真实证据
2. 登记到 known.md
3. 定位根因
4. 选修复策略
5. 写修复 + 测试
6. 移位到 fixed/

---

## 现场脚本（25 分钟）

### 步 1：复现 + 拿证据（5 分钟）

> 假设客服收到客户截图："你们的简报又出现了'运维同步回填' 这种话"。
>
> 我们现场跑一下 customer_brief_generator 看是不是能抓住：
>
> （**演讲者准备一份 input file 含"运 维 同 步 回 填"或带换行的"运维\n同步\n回填"**）
>
> 然后跑：
>
> ```bash
> python3 customer_brief_generator.py malformed_input.txt
> ```
>
> 看输出——红线 #2 的警告**没**触发。
>
> 这就是"真实证据"。**在没看到这个真实输出前，我不会动代码**——可能我以为有 Bug 但其实没。

### 步 2：立刻登记 issues/known.md（3 分钟）

> 现在我打开 [`issues/known.md`](../../issues/known.md)，登记：

```markdown
## B-2026-0509-A: 红线 #2 grep 漏抓"运维同步回填"带空格 / 换行的形式

- 发现时间：2026-05-09
- 发现人：客服反馈
- 影响范围：可能让"运维同步回填" 这类内部信息误漏到客户面简报
- 严重度：P1（红线 #2 违规风险）
- 复现步骤：
  1. 准备含"运 维 同 步 回 填" 或带换行的"运维\n同步\n回填" 的输入
  2. 跑 customer_brief_generator
  3. 警告**没**触发
- 暂时绕行：人工复审客户面输出（红线 #8 第三道闸）
- 拟修复：[name]，2026-05-12 前
- 关联：PRD-0001 §4.1.4
```

> 现在 known.md 里有这条 Bug。即使我今天忘了修，将来一定会修。

### 步 3：让 AI 定位根因（5 分钟）

> 我把 traceback / 实际行为发给 AI：
>
> > 看 customer_brief_generator.py 的 INTERNAL_TOKEN_PATTERNS。当前我有这段输入："运 维 同 步 回 填"（每个字之间有空格）。它没被 grep 抓到。
> >
> > 请：
> > 1. 解读为什么没抓到
> > 2. 列 top-3 修复策略 + 优劣
> > 3. 不要立刻改代码
>
> AI 回复：
>
> > 没抓到的原因：当前 pattern `r"运维同步回填"` 是字面匹配，不允许字符间空格。
> >
> > 策略：
> > 1. 在 pattern 里加 `\s*`：`r"运\s*维\s*同\s*步\s*回\s*填"`
> >    优势：简单直接
> >    劣势：所有内部短语都要更新；可读性变差
> >
> > 2. 在扫描前先清洗：把多余空白去掉再 grep
> >    优势：扫描逻辑简单
> >    劣势：可能误清洗合法内容（带空格的客户名等）
> >
> > 3. 用更聪明的语义匹配（fuzzy match）
> >    优势：覆盖更多变种
> >    劣势：太重了，过度工程
>
> 我倾向 1。原因：当前已经是 regex pattern list；改成 `\s*` 一致性强。

### 步 4：实施修复 + 写回归测试（7 分钟）

> 让 AI 实施：
>
> > 按策略 1 改。同时：
> > 1. 加一个**回归测试**：含空格变体的"运维同步回填" 输入应该被抓到
> > 2. 看现有测试有没有"反向断言旧错误行为"的（红线 #13）—— 如果有，同 commit 翻转或删除
>
> AI 修改：
>
> ```python
> INTERNAL_TOKEN_PATTERNS = [
>     # ...
>     r"运\s*维\s*同\s*步\s*回\s*填",  # 允许字符间空格
>     # ...
> ]
> ```
>
> 加测试：
>
> ```python
> def test_scan_internal_tokens_catches_internal_role_codename_with_spaces():
>     text = "运 维 同 步 回 填后即可看到全部数据。"
>     hits = scan_for_internal_tokens(text)
>     assert any("运" in h for h in hits)
> ```
>
> 检查现有测试：当前 `test_scan_internal_tokens_catches_internal_role_codename` 仍然合法（断言修复后正确行为）—— 不需要清理。
>
> 跑测试：
>
> （**演讲者跑测试**）
>
> 全过 ✅。

### 步 5：移位到 fixed/（5 分钟）

> 修复 PR 合并后，**当天**把 known.md 的条目搬到 `issues/fixed/2026-05-09.md`：

```markdown
# Fixed Issues — 2026-05-09

## B-2026-0509-A: 红线 #2 grep 漏抓"运维同步回填"带空格 / 换行的形式
（原始登记内容全部保留）

### 修复 / Fix
- 修复时间：2026-05-09 14:23
- 修复人：[演讲者]
- 修复 commit：abc1234
- 关联 PRD：PRD-0001 §4.1.4
- 根本原因：INTERNAL_TOKEN_PATTERNS 里的字面匹配不允许字符间空格
- 验证：新加测试 test_scan_internal_tokens_catches_internal_role_codename_with_spaces 通过
- 反向断言测试清理：✅ 无需清理（现有测试断言的是修复后行为，不冲突）
```

> 现在 known.md 里这条没了；fixed/2026-05-09.md 有这条 + 修复段。
>
> 6 个月后某位新员工查"为什么 INTERNAL_TOKEN_PATTERNS 里有 \s*"——他能找到这份 fixed 文件，看到当时为什么这么改。

---

## 反例对照（如时间允许，2 分钟）

> 如果不走这套流程：
> - 直接修代码 + push → 没人知道为什么改 → 6 个月后被 review 的同事 revert 这个 \s*
> - 没加回归测试 → 下次同样的 Bug 还会出现
> - 没移位到 fixed → known.md 里挂着，新人以为还没修
>
> 每一条都是真实事故等价物。

---

## 现场互动

> 大家在自己的环境里跑：
>
> ```bash
> python3 -m pytest tests/test_redaction.py -v
> ```
>
> 应该看到 13 条全过（原 12 + 新加 1）。
>
> 谁的环境有问题举手。

---

## 这一节用到的引用

- [`workflows/engineering/debugging_workflow.md`](../../workflows/engineering/debugging_workflow.md) 全文
- [`workflows/engineering/bug_tracking_ssot.md`](../../workflows/engineering/bug_tracking_ssot.md)
- 红线 #4（Bug SSOT）+ #13（反向断言测试）+ #14（看日志）

---

## 节奏

- 复现：5 分钟
- 登记：3 分钟
- 定位：5 分钟
- 修复：7 分钟
- 移位：5 分钟
- 总：25 分钟

→ 进入 [`04_deployment_and_red_lines.md`](04_deployment_and_red_lines.md)。
