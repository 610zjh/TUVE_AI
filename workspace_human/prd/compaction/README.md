# workspace_human/prd/compaction/

> 反熵压缩提案。任何对仓库结构的拆分 / 归档 / rollup 动作必须先在这里写一份 `COMPACT-NNNN` 提案。
> Anti-entropy rollup proposals. Any structural split / archive / rollup must first be proposed here.

---

## 触发场景

- 某 Markdown 文件超过 800 行（红线 #7）
- 某目录文件累积过多，AI 一次读不完
- 某 dated archive 占空间过大

---

## 提案模板

见 [`principles/subs/anti_entropy.md`](../../../principles/subs/anti_entropy.md) §3 中的 `COMPACT-NNNN` 模板。

---

## AI 永不自删

哪怕 retention=ephemeral，AI 也只允许"挪到 git-only 路径"，不允许 `rm`。详见 [`principles/subs/anti_entropy.md`](../../../principles/subs/anti_entropy.md) §4。

---

## 当前状态

空。等到第一份压缩提案再放进来。
