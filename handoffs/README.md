# handoffs/ · 日常工作传递区

> 同事之间每日轻量传递文档的临时落点。inbox 收上游、outbox 发下游。

---

## 是什么 / 不是什么

| ✅ 这里放 | ❌ 这里不放 → 去哪 |
|---|---|
| 销售当天给运营的客户需求要点 | 项目级接力（接力棒）→ [`projects/`](../projects/) + 对应 PRD |
| 运营给视频组的本周拍摄要点 | 岗位交接（离职 / 调岗）→ 走专门流程（未来 PRD） |
| 算法给产品的 A/B 实验初步分析 | 客户合同 / 报价 / 法务回执 → 走签批流程，**不进 git** |
| 某个临时小任务的中间产物 | 客户电话**纪要** → [`workspace_human/meetings/customer_followups/`](../workspace_human/meetings/customer_followups/) |
| 不值得开 PRD、但要让同事看到的东西 | 长期复用资料 → [`runbooks/`](../runbooks/) / [`templates/`](../templates/) / [`training/`](../training/) |
|  | Bug / 工艺问题 → [`issues/known.md`](../issues/known.md)（红线 #4 SSOT）|

混进上述任何一类 = 范围漂移。看到混入立刻挪走。

---

## 目录

- [`inbox/`](inbox/) — 同事交过来的，待我处理
- [`inbox/_raw/`](inbox/_raw/) — 未脱敏暂存（已 .gitignore）
- [`outbox/`](outbox/) — 我交付出去的，已完成 / 待发送

---

## 命名

```
YYYY-MM-DD_<from-or-to>_<topic>.md
```

- `<from-or-to>`：kebab-case 角色或团队（`sales-to-ops`、`algo-to-product`、`video-team`）
- `<topic>`：kebab-case 主题（`customer-needs`、`weekly-shoot-brief`、`ab-test-summary`）
- 默认 `.md`；其他扩展允许，优先 markdown
- **禁**：`demo_*` / `tmp_*` / `temp_*` / `new_*` / `final_*`（红线 #9）

✅ `2026-05-10_sales-to-ops_customer-needs.md`
✅ `2026-05-10_algo-to-product_ab-test-summary.md`
✅ `2026-05-10_video-team_weekly-shoot-brief.md`
❌ `tmp_客户需求.md` · `final_v2.md` · `untitled.md`

---

## 30 天反熵约定

进入 inbox/ 或 outbox/ 顶层超过 30 天没改过的文件，自动列入下一次周复盘的"清理候选"。4 选 1：

1. 仍在用 → 留下
2. 已成熟为长期资料 → 挪到对应区域（runbooks / templates / case_studies / workspace_human/meetings）
3. 已过时 → `git rm`
4. 有归档价值但不需常态可见 → 挪到 `archive/`（如开则提 COMPACT 提案）

AI **不允许**自动删 / 自动归档（红线 Chapter 0.2 第 3 条）——清理由人在周复盘时手动执行。

---

## 怎么用

详见 [`workflows/operations/handing_off_work.md`](../workflows/operations/handing_off_work.md)。
