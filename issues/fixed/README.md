# issues/fixed/

> 已修 Bug 按日归档。一天一份文件，当天有修复就追加进同一份。
> Fixed bugs archived by day. One file per day; append to same file for same-day fixes.

---

## 命名规则

```
YYYY-MM-DD.md
```

例：`2026-05-09.md` 是 2026-05-09 修的所有 Bug。

如果一天没有 Bug 修复，**不创建当天文件**。

---

## 移位纪律（红线 #4）

修完 PR 合主干当天 → 把 [`../known.md`](../known.md) 中的对应条目**整条**搬到当天的 `fixed/YYYY-MM-DD.md`。

加一段 `### 修复 / Fix`：

```markdown
### 修复 / Fix
- 修复时间：YYYY-MM-DD HH:MM
- 修复人：<name>
- 修复 commit：abc1234
- 关联 PRD：PRD-XXXX（如有）
- 根本原因：<一两句技术原因>
- 验证：<回归测试名 + 手动验证步骤>
- 反向断言测试清理：✅ 已删除/翻转 [测试名]（红线 #13）
```

---

## 不允许的

- ❌ 把 `known.md` 中的条目**删掉**而不归档
- ❌ 把"已修但没验证"的搬到 fixed
- ❌ 修一个 Bug 时顺手"清理"无关的 known.md 条目

---

## retention class

`fixed/YYYY-MM-DD.md` 的 retention 是 `rollup`：每年底归一份年度汇总，原始日文件保留索引。详见 [`principles/subs/anti_entropy.md`](../../principles/subs/anti_entropy.md)。

---

## 季度复盘

每季度扫一遍当季 fixed 文件，回答：
1. 重复出现的根因？
2. 最长存活的是哪些（known 挂 ≥ 30 天）？
3. 客户先发现还是我们先发现？
4. 是否有新一类 Bug 反复出现？

详见 [`workflows/engineering/bug_tracking_ssot.md`](../../workflows/engineering/bug_tracking_ssot.md) §"季度 Bug 复盘"。
