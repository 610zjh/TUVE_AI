# runbooks/

> 操作手册：把"反复做的事"标准化。
> Operations runbooks: standardizing recurring procedures.

---

## 当前 runbooks

| 文件 / File | 适用场景 / Use Case | 负责人 / Owner |
|---|---|---|
| [`engineering_emergency_rollback.md`](engineering_emergency_rollback.md) | 生产事故快速回滚 | 工程负责人 |
| [`ops_partner_onboarding.md`](ops_partner_onboarding.md) | 新合作伙伴入驻流程 | 运营负责人 |
| [`sales_lead_handoff.md`](sales_lead_handoff.md) | 销售线索移交客户成功 | 销售总 |

按需添加更多。

---

## 命名规则

```
runbooks/<owner_team>_<verb>_<object>.md

例：
- engineering_emergency_rollback.md
- ops_partner_onboarding.md
- sales_lead_handoff.md
- finance_monthly_close.md
```

文件名让"哪个团队、做什么动作、对什么对象" 一眼可见。

---

## 写新 runbook

参考 [`workflows/operations/ops_runbook_authoring.md`](../workflows/operations/ops_runbook_authoring.md)。

要点：写给"凌晨 2 点临时上手的同事"，假设读者一无所知。

---

## 维护

每份 runbook 顶部 frontmatter:
```yaml
---
last_executed: YYYY-MM-DD
last_reviewed: YYYY-MM-DD
review_cadence: quarterly
owner: <team>-<name>
---
```

`last_executed` 超过 review_cadence → 自动列入"过期 / 待审"。
