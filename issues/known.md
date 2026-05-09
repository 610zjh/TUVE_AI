# Known Issues / 未修问题

> 全公司**单一登记位置**（红线 #4）。修复后**整条**移到 [`fixed/YYYY-MM-DD.md`](fixed/)。
> Company-wide **single tracking location** (Red Line #4). Move whole entries to [`fixed/YYYY-MM-DD.md`](fixed/) on fix.

---

## 当前未修 Issues

> 起步时空。任何人发现 Bug 都直接登记到这份文件。

（暂无）

---

## 登记格式

复制 [`templates/bug_report/bug-template.md`](../templates/bug_report/bug-template.md) 中的 block，填好放在本文件下。

简化版：

```markdown
## B-2026-MMDD-X: <一句话标题>

- 发现时间：YYYY-MM-DD
- 发现人：<name>
- 影响范围：<具体>
- 严重度：P0 / P1 / P2 / P3
- 复现步骤：1, 2, 3 ...
- 暂时绕行：<如有>
- 拟修复：<负责人 + ETA>
- 关联：PRD-XXXX（如有）
```

---

## 严重度判断

| 级别 | 定义 |
|---|---|
| P0 | 全产品停摆 / 数据丢失 / 安全事故 / 资损 |
| P1 | 核心工作流阻断 / 重要客户被影响 |
| P2 | 边角功能 / 小范围 / 有绕行 |
| P3 | 体验性 / typo / 无真实影响 |

不确定时往严重判（降级比升级容易）。

---

## P0 / P1 的特殊纪律

P0 / P1 不是"登记完就行"。立刻：
- 通知工程负责人
- 通知受影响业务方
- 客户感知 → 客户告知（按红线 #2 客户面口径）

---

## 修复后

修完 PR 合主干当天 → 整条搬到 [`fixed/YYYY-MM-DD.md`](fixed/)，加 `### 修复 / Fix` 段。

详见 [`workflows/engineering/bug_tracking_ssot.md`](../workflows/engineering/bug_tracking_ssot.md)。
