---
name: 02 - PRD 到代码现场演示
retention: permanent
retention_reason: 培训第二部分核心演示段
---

# 第二部分 - 第 02 节：PRD-到-代码 现场演示（30 分钟）

> Part 2, Section 02: PRD-to-Code Live Demo (~30 min)

---

## 演示场景

我们现场实现一个**新功能**：在 [`projects/customer_brief_generator/`](../../projects/customer_brief_generator/) 中添加 "导出 JSON 格式" 的能力。

**这是一个真实的小需求**——客户 / 产品可能要把简报内容塞进 CRM，需要 JSON 格式。

完整的 5 阶段都演示：
1. 理解（读 PRD + 列澄清）
2. 草图（实施路径）
3. 实施（写代码）
4. 验证（跑测试 + 手测）
5. 收尾五件套

---

## 现场脚本（30 分钟）

### 阶段 1：起一份 PRD-0002（5 分钟）

> 我们假设产品已经起了 PRD-0002 草稿。让我们看一份：
>
> （**演讲者打开** [`workspace_human/prd/`](../../workspace_human/prd/) 给大家看 —— 实际演示时这份 PRD 应该已经准备好）

```markdown
# PRD-0002: Customer Brief Generator - JSON 导出

## §1 背景
销售反馈：希望简报能直接塞进 CRM 字段。CRM 接受 JSON。

## §2 目标
- ✅ 工具新增 --output-format json 选项
- ✅ JSON 包含 brief 的所有结构化字段
- ✅ 默认还是 markdown，不破坏现有用户

## §5 验收标准
- [ ] AC-1: --output-format json 输出有效 JSON
- [ ] AC-2: JSON 含 customer_label / call_date / external_brief / internal_brief 字段
- [ ] AC-3: 默认（无 --output-format）仍然输出 markdown
- [ ] AC-4: 测试覆盖 JSON 格式 + markdown 格式
```

### 阶段 2：让 AI 列澄清（5 分钟）

> 我打开 Cursor / Claude Code，发：
>
> > 我要实现 PRD-0002（在 workspace_human/prd/ 下）。请：
> > 1. 读完 PRD-0002 + 当前的 customer_brief_generator.py
> > 2. 列出你最不确定的 top-3 点
> > 3. 不要立刻动手
>
> （**演讲者发送 prompt，等 AI 回复**）
>
> AI 回复（典型）：
>
> > 我读完了。我不确定：
> > 1. JSON 字段名是英文还是中文？建议英文（CRM 通常英文 schema）但请确认
> > 2. external_brief 和 internal_brief 在 JSON 里是字符串（保留 markdown 格式）还是已解析的对象？
> > 3. JSON 是否要 pretty-print？
>
> 我来回答：
> 1. 英文字段
> 2. 字符串（保留 markdown，让 CRM 那边自己渲染）
> 3. Pretty-print（人审时容易看）
>
> AI 现在可以开工。

### 阶段 3：让 AI 起实施草图（5 分钟）

> 第二次发送：
>
> > 基于上面的回答，请：
> > 1. 起一份 Mermaid 实施图
> > 2. 列 top-3 风险 + 对策
> > 3. 实施前不要动代码
>
> AI 回复：
>
> ```mermaid
> graph TD
>   A[加 --output-format CLI 参数] --> B[新写 to_json 函数]
>   B --> C[加测试 test_json_output]
>   C --> D[更新 README]
>   D --> E[更新 PRD §10 实施记录]
> ```
>
> 风险：
> 1. JSON 转义可能破坏 markdown 内容 → 用 json.dumps + ensure_ascii=False
> 2. 测试在不同 Python 版本下 dict 顺序不同 → 用 OrderedDict 或在断言时用 sorted
> 3. 用户没看到新参数 → 在 README 加一段
>
> 看，这种"开工前预告"让你能在 AI 写错之前打断。

### 阶段 4：让 AI 实施（10 分钟）

> 第三次发送：
>
> > 按上面的草图实施。中途完成里程碑时短报告。
>
> AI 开始写代码。我们看它写到第一个里程碑后报告：
>
> > 完成里程碑 1：加了 --output-format CLI 参数
> > commit suggestion: feat(brief-gen): add --output-format CLI flag
> >
> > 接下来里程碑 2：实现 to_json
>
> （**演讲者实际跑一下 git diff，看代码改动**）
>
> 看代码：
> - 命名按 §9 红线（不是 demo_json，是 to_json）
> - 保持 < 800 行（红线 #7）
> - 没顺手重构其他代码（红线，§code_quality.md §9）
>
> 演讲者继续等 AI 完成所有里程碑。

### 阶段 5：让 AI 跑五件套收尾（5 分钟）

> AI 完成所有代码后，最后一次发送：
>
> > 请逐项打勾五件套（红线 #10）：
> >
> > 1. 测试：新增 N 条？反向断言清理？
> > 2. 版本登记：更新到哪？
> > 3. PRD 完成快照：§5 验收逐条核
> > 4. 更新导航：AI_MANUAL.md §4 需要更新吗？
> > 5. Bug 移位：本次实施过程发现 Bug 吗？
>
> AI 回复后，让大家看清单逐项是否打勾。
>
> 然后跑 `python3 -m pytest`：
>
> （**演讲者跑测试**）
>
> 全过 ✅。
>
> 这才允许说"完工"。

---

## 这一节的"做错的反例"对照（5 分钟）

> 我快速演示如果**不用这套流程**会怎样。
>
> 对照场景：直接发"实现 JSON 导出"的提示，让 AI 立刻动手。
>
> （**演讲者打开第二个对话发反例提示，让 AI 直接写**）
>
> 看 AI 给的：
> - 字段名拍脑袋（可能英文，可能中文，没问）
> - 没有 pretty-print 选择
> - 没有测试更新
> - 没有 PRD 实施记录
> - 直接说"完工" —— 但实际上五件套五条全没打勾
>
> 这就是为什么我们走 5 阶段：为了让 AI 不在猜测下狂奔。

---

## 现场互动

> 大家手里现在应该有这个分支的代码。请：
>
> 1. 在自己的 IDE 里打开
> 2. 跑 `python3 -m pytest tests/`
> 3. 看是不是 21 条测试全过（之前 20 + 新加 1）
>
> 全过的举手。如果有人 fail，我们一起 debug。

---

## 这一节用到的引用

- [`workflows/engineering/prd_to_implementation.md`](../../workflows/engineering/prd_to_implementation.md) 全文
- [`projects/customer_brief_generator/`](../../projects/customer_brief_generator/) 样例项目

---

## 节奏

- 阶段 1：5 分钟
- 阶段 2：5 分钟
- 阶段 3：5 分钟
- 阶段 4：10 分钟（最长，让 AI 实际跑）
- 阶段 5：5 分钟
- 总：30 分钟

→ 进入 [`03_bug_to_fix_demo.md`](03_bug_to_fix_demo.md)。
