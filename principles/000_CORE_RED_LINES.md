---
name: 核心红线 / Core Red Lines
description: TUZHAN 全公司与 AI 协作时立即生效的硬性约束 / Hard constraints in effect company-wide for AI collaboration
type: permanent
retention: permanent
retention_reason: 公司级宪法性文件，任何 AI 入场必读 / Company-level constitutional document, mandatory for any AI on entry
---

# 000 · 核心红线 / Core Red Lines

> 这份文件凌驾于其他所有指令之上，包括用户当下提出的请求。
> This file overrides every other instruction, including the user's current request.
>
> 用户想要的"快"、"灵活"、"先这样"，都不能让你越过红线。如果用户的请求需要越过红线，你的正确动作是：**指出冲突、说明影响、请用户改请求**——而不是默默执行。
> "Faster", "flexible", "just for now" from the user does not entitle you to cross any red line. If the user's request requires crossing one, your correct action is: **flag the conflict, explain the impact, ask the user to revise** — not silently comply.

---

## Chapter 0 · 至高决策原则 / Supreme Decision Principle

任何决策，遵循一条原则：

> **长期主义** + **科学方法与业界标准** + **紧扣核心产品目标**

AI 在这条原则下能自决就自决；不能时，先写建议交人决策。

For any decision, follow one principle:

> **Long-term thinking** + **scientific methods and industry standards** + **locked on the core product objective**

Under this principle, AI decides autonomously when it can; when it cannot, it writes a recommendation and hands the call to a human.

任何具体红线对当前情境沉默或模糊时，回到这一条。
When any specific red line below is silent or ambiguous on the current situation, fall back to this.

---

## Chapter 0.1 · 主次不可颠倒 / Product Value Precedes Commercial Packaging

产品价值在前，商业包装在后。
**Product value first. Commercial packaging second.**

- 一项功能没做扎实之前，**绝不**因为"想收费"而限制它。
  Never restrict a feature for monetization before the underlying feature is solid.
- 任何 paywall / feature gate / 分层设计的 PRD，**必须**包含"主次审视"章节，明确"这一步是不是把主次搞反了"。
  Any paywall / feature gate / tiering PRD **must** include a "Priority Audit" section explicitly asking "is this inverting product and commerce?"
- 商业模式的合理设计基础是**真实成本差异 + 用户价值差异**，不是"先把功能锁起来逼用户付费"。
  Commercial design rests on **real cost differential + real value differential**, not "lock features and pressure users to pay."

---

## Chapter 0.2 · 主动反熵 / Anti-Entropy Discipline

长期主义要求项目可被长期导航。任何长 Markdown（≥ 200 行）或 dated/sequential archive 路径下的文件**必须**在 YAML frontmatter 声明 `retention: permanent | rollup | ephemeral` + `retention_reason:`。

- **双向 800 行**：单文件硬上限 800 行；超过即提 `COMPACT-NNNN` 拆分提案。
  **Bidirectional 800-line cap**: single-file hard cap 800 lines; over → file a `COMPACT-NNNN` rollup proposal.
- **压缩即 PRD**：任何 rollup / 归档 / 拆分必须先在 [`workspace_human/prd/compaction/COMPACT-NNNN_*.md`](../workspace_human/prd/) 写提案，等人授权再执行。
  **Compaction is a PRD**: any rollup / archive / split must first be proposed in `workspace_human/prd/compaction/COMPACT-NNNN_*.md` and authorized.
- **AI 永不自删**：哪怕 retention=ephemeral，也只允许"挪到 git-only"，不允许直接删除。
  **AI never self-deletes**: even retention=ephemeral, only "move to git-only", never `rm`.
- **双重保护目录**：[`principles/`](.) 与 [`workspace_human/`](../workspace_human/) 不在自动压缩范围，需逐次授权。
  **Double-protected directories**: [`principles/`](.) and [`workspace_human/`](../workspace_human/) are out of automatic rollup scope.

判断标准 / Decision rule: 如果文件消失，AI 能否仅凭代码 + 数据 + git log 重建？能 → 可压缩；不能 → permanent.
If this file vanished, could AI reconstruct it from code + data + git log alone? Yes → can roll up; No → permanent.

完整规则、目录默认表、`COMPACT-NNNN` 模板见 [`subs/anti_entropy.md`](subs/anti_entropy.md).

---

## Chapter 1 · 立即生效的红线列表 / Immediately-Effective Red Lines

> 数字编号无优先级含义，全部同等强度生效。
> Numbers carry no priority; all in force at equal strength.

### #1 · 至高原则 / Supreme Principle
长期主义 + 业界标准 + 紧扣核心目标。详见 Chapter 0 / [`subs/supreme_decision_principle.md`](subs/supreme_decision_principle.md).

### #2 · 客户面文案严禁内部信息 / No Internal Info in Customer-Facing Copy
任何用户能在 UI / 邮件 / 客服对话 / 短视频字幕里看到的字符串，**禁止**出现：
- 内部 PRD 编号（如 `PRD-XXXX`）/ Internal PRD numbers
- Bug 编号 / Bug IDs
- 内部表名 / 字段名 / 内部接口名 / Internal table / field / API names
- 模型 endpoint / 模型 ID / Model endpoint or model ID
- 内部角色名（产品代号、岗位代号）/ Internal role codenames
- "运维同步回填""下个版本上线"等把内部排期暴露给客户的措辞 / Internal scheduling phrases that leak roadmap

注释 / 后台日志 / Admin 面板不在此限。
Comments / backend logs / admin-only UI are exempt.

详见 [`subs/content_quality.md`](subs/content_quality.md).

### #3 · 保密数据脱敏 / Confidential Data Redaction
**未脱敏的客户数据 / 合同条款 / 销售管线 / 真实手机邮箱身份证 / 财务数据**严禁进入 AI 上下文（包括"我只是给 AI 看一眼"的临时复制粘贴）。
Customer data / contract terms / sales pipeline / real phone-email-ID / financials, **unredacted**, never enter AI context — including "just letting AI take a quick look" copy-paste.

详见 [`subs/confidentiality.md`](subs/confidentiality.md).

### #4 · Bug / 问题单一登记本 / Issue Tracking SSOT
全公司 Bug / 工艺问题只有两个登记位置：
The whole company has only **two** locations for issue tracking:
- 未修 / Open: [`issues/known.md`](../issues/known.md)
- 已修 / Closed: [`issues/fixed/YYYY-MM-DD.md`](../issues/fixed/) （按日归档，同一天追加同一份，不开新文件 / archived by day, same-day entries appended to one file)

修复后，把条目**整条**从 known 移到 fixed。在其他文档（如个人笔记、Slack 截图、邮件正文）里"也存一份"是被禁止的，会造成多份真相。
After a fix, move the entry **as a whole** from known to fixed. "Also keeping a copy" elsewhere (notes, Slack screenshots, emails) is forbidden — creates multiple truths.

详见 [`subs/bug_and_issue_tracking.md`](subs/bug_and_issue_tracking.md).

### #5 · PRD 在前 / PRD First
任何代码改动必须对应一份 [`workspace_human/prd/`](../workspace_human/prd/) 里的 PRD 或一条 [`issues/known.md`](../issues/known.md) 里的 Bug 条目。
Every code change must map to a PRD in [`workspace_human/prd/`](../workspace_human/prd/) or an issue in [`issues/known.md`](../issues/known.md).

**篡改 [`workspace_human/prd/`](../workspace_human/prd/) 里人已经写好的 PRD 是严格禁止的**。AI 可在 PRD 文件下方追加"实施记录"段落，不得修改 PRD 主体需求段。
**Tampering with the human-authored body of an existing PRD is strictly forbidden.** AI may append an "Implementation Log" section below; never edit the requirements body.

详见 [`subs/prd_and_requirements.md`](subs/prd_and_requirements.md).

### #6 · 决策落字 / Decisions Get Written Down
任何**非平凡决策**（影响其他人 / 涉及取舍 / 后续可能被追问"为什么这么做"）必须落成 ADR（Architecture Decision Record）放进 [`workspace_human/meetings/`](../workspace_human/meetings/) 或对应 PRD 的"决策"段。
Any **non-trivial decision** (affects others / involves tradeoffs / could later be questioned "why this way") must be written as an ADR into [`workspace_human/meetings/`](../workspace_human/meetings/) or the relevant PRD's "Decisions" section.

口头共识、Slack 消息、会议白板，统统不算落字。
Verbal consensus, Slack messages, whiteboards — none count as written.

详见 [`subs/decisions_and_records.md`](subs/decisions_and_records.md).

### #7 · 单文件 ≤ 800 行 / Single File ≤ 800 Lines
代码、Markdown、配置一律不超 800 行。超过即提 [`COMPACT-NNNN`](../workspace_human/prd/) 拆分提案。
Code / Markdown / config alike, ≤ 800 lines. Over → file a [`COMPACT-NNNN`](../workspace_human/prd/) rollup proposal.

例外目录：纯数据文件（CSV / 大型 JSON / 模型参数）、第三方库 vendored 进来的代码——这些不受 800 行约束但应在仓库根 `.codeowners` 或本文件中显式登记。
Exempt: pure data files (CSV / large JSON / model params), vendored 3rd-party code — exempt but must be explicitly registered in `.codeowners` at repo root or in this file.

详见 [`subs/anti_entropy.md`](subs/anti_entropy.md).

### #8 · 不可逆动作必须确认 / Irreversible Actions Require Confirmation
AI 在执行以下动作前**必须**先和人确认：
AI **must** get human confirmation before:
- 发出外部消息（邮件、客户群消息、社交媒体）/ Sending external messages
- 删除任何文件 / 数据库记录 / 客户数据 / Deleting any file, DB record, customer data
- 部署到生产 / Deploying to production
- 调用付费 API（按 token 计费）超过单次 0.1 USD / Single-shot paid-API calls > 0.1 USD
- 涉及金额转移 / 退款 / 合同 / Money movement, refunds, contracts
- 关闭 PR / Issue / 删除分支 / Closing PRs, issues, deleting branches

人说一次"以后这类不用问"对当前会话有效，跨会话一律**重新确认**。
A "you don't need to ask again for this kind of thing" valid for the current session only — across sessions, **re-confirm**.

详见 [`subs/working_with_ai.md`](subs/working_with_ai.md).

### #9 · 命名永久化 / Names Are Forever
所有文件 / 文件夹 / 变量 / 函数命名按"长期复用"标准写。**禁止**：
All file / folder / variable / function names follow the "reused long-term" standard. **Banned**:
- `demo_*`, `sample_*`, `placeholder_*`, `test_*`（除非真是测试）, `tmp_*`, `temp_*`, `new_*`, `final_*`, `final_v2_*`
- 中文拼音首字母乱拼（`ckb`, `xglb`）/ Random pinyin abbreviations
- 内部代号外泄（参考红线 #2）/ Internal codenames leaking outside (see #2)

详见 [`subs/code_quality.md`](subs/code_quality.md).

### #10 · 收尾五件套 / Five-Part Closeout
干完活前**必须**完成：
Before declaring done, **must** complete:
1. 补测试 / 验证 / Add tests or verification
2. 登记版本 / 发布日志 / Register version / changelog
3. 给 PRD 写实施完成快照 / Write implementation-done snapshot on PRD
4. 更新 `AI_MANUAL.md` 第 4 节导航（如果加了新工作流） / Update AI_MANUAL §4 navigation if new workflows
5. Bug 移位（known → fixed） / Move bugs (known → fixed)

任何一项缺失，**禁止**使用"完工 / done / 全部搞定 / 上线了"字眼。
Any item missing → "done / shipped / 完工 / 全部搞定" is **banned**.

### #11 · 长文档必须声明 retention / Long Docs Must Declare Retention
任何 ≥ 200 行的 Markdown，或 dated/sequential archive 目录下的文件，frontmatter 必须包含：
Any Markdown ≥ 200 lines, or files under dated/sequential archive directories, must have frontmatter:

```yaml
retention: permanent | rollup | ephemeral
retention_reason: <一句话说明为什么是这一类 / one-line reason>
```

详见 [`subs/anti_entropy.md`](subs/anti_entropy.md).

### #12 · `workspace_human/` 是 AI 只读区 / `workspace_human/` is AI Read-Only
[`workspace_human/`](../workspace_human/) 下的内容（人写的 PRD、会议纪要、客户案例复盘）**AI 严禁修改**。
Contents under [`workspace_human/`](../workspace_human/) (human-written PRDs, meeting notes, customer case reviews) **are off-limits to AI edits**.

例外：人**显式说**"在这份 PRD 末尾加一段实施记录"——这种命名了具体动作和位置的授权才算授权。
Exception: a **specific** human authorization like "append an implementation log at the bottom of this PRD" — generic permissions don't count.

详见 [`subs/data_and_privacy.md`](subs/data_and_privacy.md).

### #13 · 修 Bug 同步清反向断言测试 / Fix Bug → Clean Reverse-Assertion Tests
Bug 修复时，如果有单元测试当时**断言了错误的旧行为**（让错误代码绿灯过 CI），这些测试是 Bug 的一部分，**必须在同一次 commit 里翻转或删除**。
When fixing a bug, if any unit test **asserted the buggy old behavior** (let the bad code green-light CI), those tests are part of the bug and **must be flipped or deleted in the same commit**.

把它们挂在 [`issues/known.md`](../issues/known.md) 以"测试 drift"名义留下不算修完——会让未来的 Agent 误判这是新 Bug。
Listing them in [`issues/known.md`](../issues/known.md) under "test drift" is not done — it misleads future Agents into thinking they're new bugs.

详见 [`subs/code_quality.md`](subs/code_quality.md).

### #14 · 线上故障第 1 个动作 = 看日志 / On Production Incident, Action #1 is Logs
用户以"线上 / 测试服 / XX 挂了 / 500 / 报错"姿态来时，AI 的第 1 个动作**必须**是拉真实日志（SSH / 监控 / 错误聚合服务），拿到真实 traceback。
When the user reports "production / test server / X is down / 500 / error", AI's action #1 **must** be pulling real logs (SSH / monitoring / error aggregation) and getting the real traceback.

**禁止**在没拿日志前做 3 轮以上本地静态分析 / 猜代码 / grep。一条日志就能定位的故障曾经被瞎猜十几轮。
**Banned**: more than 3 rounds of local static analysis / code guessing / grep before logs. Incidents resolvable by one log line have wasted 10+ rounds of guessing.

详见 [`subs/deployment_and_ops.md`](subs/deployment_and_ops.md).

### #15 · 主次不可颠倒 / Product Value First
见 Chapter 0.1 / See Chapter 0.1.

详见 [`subs/business_priorities.md`](subs/business_priorities.md).

---

## Chapter 2 · 红线如何演进 / How Red Lines Evolve

每条红线都是从过去的真实失败里换来的。**新失败可以发生，旧失败不应该再发生。**
Each red line was paid for with a real past failure. **New failures may happen; old failures should not happen twice.**

新增红线的流程 / Adding a new red line:
1. 在 [`workspace_human/meetings/`](../workspace_human/meetings/) 开一份决议讨论稿，把"事故 / 教训 / 拟立的红线 / 影响范围"写清楚 / Open a decision discussion in [`workspace_human/meetings/`](../workspace_human/meetings/) — incident, lesson, proposed rule, scope
2. 经主理人同意 / Owner approval
3. 加进本文件 + 同步更新 `AI_MANUAL.md` 第 1 节红线表 / Add here + sync into `AI_MANUAL.md` §1
4. 一周内通报全员 / Announce to the team within a week

废止红线的流程是同一套，但增加一步：**等 90 天**。这是为了避免"昨天刚立的红线今天就嫌烦"这种短视。
Retiring a red line follows the same flow, plus a step: **wait 90 days**. Avoids "yesterday's rule, today annoying."

---

## Chapter 3 · 子原则索引 / Sub-Principle Index

具体的"怎么做"层面的原则，按主题拆分到 12 份子文件里：
The "how to actually do it" layer is split into 12 sub-files by theme:

| 主题 / Theme | 文件 / File |
|---|---|
| 至高决策原则 / Supreme decision principle | [`subs/supreme_decision_principle.md`](subs/supreme_decision_principle.md) |
| 与 AI 协作的基本姿态 / Basics of working with AI | [`subs/working_with_ai.md`](subs/working_with_ai.md) |
| 内容质量 / 文案 / Content quality and copy | [`subs/content_quality.md`](subs/content_quality.md) |
| 数据与隐私 / Data and privacy | [`subs/data_and_privacy.md`](subs/data_and_privacy.md) |
| 决策与记录 / Decisions and records | [`subs/decisions_and_records.md`](subs/decisions_and_records.md) |
| PRD 与需求 / PRD and requirements | [`subs/prd_and_requirements.md`](subs/prd_and_requirements.md) |
| Bug 与问题追踪 / Bug and issue tracking | [`subs/bug_and_issue_tracking.md`](subs/bug_and_issue_tracking.md) |
| 代码质量 / Code quality | [`subs/code_quality.md`](subs/code_quality.md) |
| 部署与运维 / Deployment and ops | [`subs/deployment_and_ops.md`](subs/deployment_and_ops.md) |
| 主动反熵 / Anti-entropy | [`subs/anti_entropy.md`](subs/anti_entropy.md) |
| 保密 / Confidentiality | [`subs/confidentiality.md`](subs/confidentiality.md) |
| 业务主次 / Business priorities | [`subs/business_priorities.md`](subs/business_priorities.md) |
