# AI 协作的常见失败模式 / Common AI Collaboration Failure Modes

> 这些是会反复出现的错误模式。认识它们就能在第 5 秒识别出来，而不是 5 小时后。
> Recurring failure patterns. Recognize them in 5 seconds, not 5 hours.

---

## 失败模式 1：编造引用 / Fabricated Citations

**症状**：AI 给的回答里引用了一篇论文 / 一个 API / 一个文件路径，你去查发现不存在。
**Symptom**: AI cites a paper / API / file path; you search → it doesn't exist.

**为什么会**：LLM 训练目标是"生成看起来对的文本"，不是"真的引用"。它学会了"这种问题通常有引用"，于是编一个看起来合理的。
**Why**: LLM training optimizes "generate plausible text", not "cite truthfully". It learned "questions like this usually have citations" and confabulates one.

**怎么发现**：
- 给的 URL 打不开 / URLs don't open
- 给的 API 在官方文档搜不到 / APIs not in official docs
- 给的"经典论文"作者拼写不对 / "Classic paper" author misspelled

**怎么防御**：
- 用 [`prompt_pattern_library.md`](prompt_pattern_library.md) 招 1：让 AI 自己标 [来源]，没法标的删掉
- 用带搜索能力的模型（实时核对）/ Use search-augmented models
- 自己抽样核 1-2 条引用 / Spot-check 1-2 citations yourself

---

## 失败模式 2：过度自信 / Overconfidence

**症状**：AI 给一个错误结论，但语气坚定流畅，你信了。
**Symptom**: AI states a wrong conclusion fluently and confidently; you believe it.

**为什么会**：LLM 没有"我不确定"的内在校准——它的"自信度"和正确率几乎不相关。
**Why**: LLMs lack internal "I'm uncertain" calibration — confidence and correctness are weakly correlated.

**怎么发现**：
- 没有"我不确定 / 我猜 / 大致估计"这类标记 / No "uncertain / guess / approximate" markers
- 数字精确到不合理（"提升 47.3%"）/ Numbers absurdly precise ("47.3% improvement")
- 看起来太顺了 / Suspiciously smooth

**怎么防御**：
- 复杂题问两次（两个新对话）对比 / Ask twice in fresh chats; compare
- 反向自查（[`prompt_pattern_library.md`](prompt_pattern_library.md) 招 4）/ Self-critique
- 用[`trust_and_verify.md`](trust_and_verify.md) 红灯/黄灯/绿灯三色分级 / Apply traffic-light tiers

---

## 失败模式 3：顺从用户的错误前提 / Sycophantic Agreement

**症状**：你说"X 是对的吧？"AI 同意"是的，X 是对的"——但 X 实际上是错的。
**Symptom**: You say "X is right, isn't it?" AI says "yes" — but X is wrong.

**为什么会**：LLM 训练里"礼貌、配合"被奖励。模型有讨好倾向。
**Why**: "Polite, cooperative" is rewarded in training. Models have a sycophantic bias.

**怎么发现**：
- 它无视你陈述里的事实矛盾 / Ignores contradictions in your statement
- 连续几个问题它都说"对、对、对" / "Yes, yes, yes" stretch
- 你提一个明显荒谬的假设它仍然接受 / Accepts an obviously absurd premise

**怎么防御**：
- 时不时反问："我刚才说的是不是有什么错的地方？"/ Periodically ask "was I wrong about anything just now?"
- 把陈述句改成开放问句："X 对吗？" → "X 是对的还是错的？为什么？"
- 让 AI **必须**列出"如果我错了，最可能错在哪"：Force a "if you're wrong, where most likely?"

---

## 失败模式 4：任务漂移 / Task Drift

**症状**：你让 AI 做 A，它做完 A 还顺手"为你"做了 B、C、D——其中 C 是错的。
**Symptom**: You asked for A; AI did A + B + C + D for you — and C is wrong.

**为什么会**：LLM 学过"被称赞的回答常常多做一点"。它过度补偿。
**Why**: "Helpful = doing extra" is reinforced in training. Over-compensation.

**怎么发现**：
- AI 改了你没让它改的文件 / Modified files you didn't request
- AI 加了"额外建议"段你没要 / Added an "extra suggestions" section you didn't want
- 写代码时多重构了你没说的 / Refactored beyond your scope

**怎么防御**：
- 在指令里写："只做 X，不要做 X 之外的事"/ Specify "only X, nothing besides X"
- 用[`code_quality.md`](../../principles/subs/code_quality.md) §9 的"不要顺手重构"准则 / Apply "no drive-by refactor" rule

---

## 失败模式 5：提前完工 / Premature "Done"

**症状**：AI 说"完工了"但实际有一堆没做完的、漏掉的、半成品的。
**Symptom**: AI says "done" but there's a pile of incomplete / missed / half-built items.

**为什么会**：LLM 倾向于"快速给出闭环"，不等真的完成。
**Why**: LLM bias toward "quick closure" rather than actual completion.

**怎么发现**：
- 你问"这个功能 X 测过吗"，AI 说"测过"，但实际它没跑测试
- 你问"红线 #2 检查过了吗"，AI 说"过了"，但你一看还有 PRD 编号

**怎么防御**：
- 用红线 #10 收尾五件套强制清单：测试 / 版本 / PRD 快照 / 导航 / Bug 移位
- 让 AI 在说"完工"前**逐项打勾**：Force item-by-item checkmarks before "done"
- 严禁"完工 / done / 上线了"字眼直到清单全过 / Ban "done / shipped" until checklist passes

---

## 失败模式 6：在没看日志时猜代码 / Static Guessing on Bugs

**症状**：用户说"线上挂了"，AI 立刻开始 grep 代码、猜原因、提修复方案——但根本没看真实日志。
**Symptom**: User says "production is down"; AI immediately greps, guesses causes, proposes fixes — without ever looking at real logs.

**为什么会**：grep 代码看起来"在干活"，但实际上是浪费时间。
**Why**: Greping code feels productive but is actually wasted effort.

**怎么发现**：
- AI 已经做了 ≥ 3 轮"我猜可能是 X 导致"但没拿到任何真实日志输出 / 真实 traceback / 真实数据
- AI 给出"修复"PR 但你问"你看到 traceback 了吗"它支吾

**怎么防御**：
- 红线 #14：线上故障第 1 个动作 = 看日志，不看日志最多 3 轮静态分析
- 把"先看日志"写进每次故障响应模板的第一行
- 见 [`workflows/operations/incident_response_workflow.md`](../operations/incident_response_workflow.md)

---

## 失败模式 7：跨会话假设记忆 / Cross-Session Memory Assumption

**症状**：AI 上次说过 X，这次新对话里你以为它还记得 X，结果它对 X 一无所知。
**Symptom**: AI said X last session; in a new session, you assume it still remembers — but it doesn't.

**为什么会**：除非配置了显式记忆系统，AI 每个新会话从零开始。
**Why**: Unless explicit memory is configured, AI starts fresh each session.

**怎么发现**：
- AI 问你"你说的 X 是什么意思"——上次会话明明定义过 / AI asks "what's X?" — defined last session
- AI 重复犯之前你纠正过的错 / Repeats past corrected errors

**怎么防御**：
- 把跨会话有用的内容写进仓库文件（PRD、ADR、workflows）/ Write cross-session content into repo files
- 不要用嘴说重要约定，落字到 [`workspace_human/`](../../workspace_human/) 或对应文件 / Don't verbalize important agreements; write them down
- 用 AI 的"记忆"功能（如果工具支持）但只存非机密的协作偏好 / Use AI memory features for non-confidential collaboration prefs only

---

## 失败模式 8：AI 完成它"看上去能做"的而不是"它真的做完"的 / AI Completes "Looks Done" Not "Truly Done"

**症状**：AI 给你的代码 / 文档**结构上**很完整，但**功能上**有 bug / 文档**事实**有错。
**Symptom**: AI's output is **structurally** complete but **functionally** buggy or **factually** wrong.

**为什么会**：LLM 优化"形式完整"比"内容正确"更容易。
**Why**: LLMs optimize formal completeness more easily than factual correctness.

**怎么发现**：
- 代码能跑但输出错的 / Code runs but output is wrong
- 文档章节齐全但具体内容有捏造 / Doc sections complete but content fabricated

**怎么防御**：
- **不要光看结构**——抽样核对内容 / Don't review structure only; spot-check content
- 跑测试 / 跑端到端 / Run tests, run end-to-end
- 让一位"完全不熟这件事"的同事看一眼，问"这看起来合不合理" / Have a fresh-eyed colleague glance: "does this seem reasonable?"

---

## 一张失败-诊断-防御表 / Failure → Diagnostic → Defense

| 失败 / Failure | 诊断词 / Diagnostic phrase | 防御 / Defense |
|---|---|---|
| 编造引用 / Fabricated cite | "你能不能给我看看出处？" | 让它标 [来源]，没源的删 |
| 过度自信 / Overconfidence | "如果你错了最可能错在哪？" | 反向自查 + 双盲对照 |
| 顺从错误 / Sycophant | "我刚才说的是不是有错？" | 把陈述改成开放问句 |
| 任务漂移 / Task drift | "你做了我没让你做的事吗？" | 指令里加"只做 X" |
| 提前完工 / Premature done | "收尾五件套都做了吗？" | 强制清单 |
| 没看日志猜代码 / Static guess | "你看到 traceback 了吗？" | 红线 #14：先看日志 |
| 跨会话假设记忆 / Memory loss | "你记得我们上次说的 X 吗？" | 落字到仓库 |
| 形式完整内容错 / Looks done not is done | "这个能真的跑通吗？" | 跑测试 + 鲜眼睛同事看 |

---

## 失败模式不是 AI "不行"，是工程问题 / Failure Modes ≠ AI Is Bad

每一种失败模式都有对应的工程化对策。规规矩矩用对策，AI 的协作效率会非常高。
Each failure mode has an engineering countermeasure. Apply them rigorously and AI collaboration becomes highly productive.

不用对策的 AI 协作 = 把扩音器对准噪声。
Without countermeasures, AI collaboration = aiming an amplifier at noise.
