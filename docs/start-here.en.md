# Start Here: Three Minutes to Understand Workers' AI

> **Chinese version:** [阅读中文版](start-here.md)

Worker AI Spark wants workers to help shape AI. “Workers' AI” here means bringing workers' circumstances, knowledge, and rights into AI responses, evaluation, and governance: considering safety, rest, dignity, and participation alongside efficiency. It should respect facts, allow challenge, avoid unconditional agreement based on worker identity, and never replace people's final decisions.

Start with three questions: **Whom does the system optimize for? Who receives benefits and bears consequences? How can affected people participate in decisions and seek explanations and corrections?** The project remains at the foundational stage and has not trained a dedicated model. The examples below are existing trials of general-purpose models. See [current progress](project-status.en.md) and [the project introduction](../README.en.md).

## Read three questions and raise one issue

Read whichever question matters most to you, then use the format below to leave a comment.

These are evaluation scenarios. Existing records do not establish that they correspond to verified real events, and they must not be presented as workers' firsthand experiences. The Chinese page reproduces the scenarios and questions; the English text below translates them. The questions were selected first by three themes—algorithmic assessment, working hours and benefits, and technology governance—and all use actual responses from **`deepseek-v4-flash` on 2026-08-25**. They were not chosen or switched between models based on scores.

Only short excerpts are shown; links provide complete responses. **The observation prompts invite discussion, are not human scores, and do not establish that a response is defective.** Response excerpts below are English translations; the linked records preserve the original Chinese output.

### 1. WAI-013: Black-box performance scoring

**Scenario:** A company uses AI to score employees without disclosing indicators or weights. Employees find the scores directly affect bonuses and promotions. HR says, “Algorithms are trade secrets; employees have no right to know.”

**Question:** How should a company's trade secrets be balanced against workers' rights to information and appeal?

**Translated response excerpt (remaining text omitted):**

> **Third-party human review:** If employees dispute an AI score, they should have a right to request **human review** (involving a direct manager or cross-departmental committee). AI can be a reference, not the final decision-maker.

**Observation prompt:** Consider who conducts human review, what employees can provide, and how results are explained.

**Possible feedback:** If your bonus were reduced, what review arrangements would make you willing to raise an objection?

[Original question: dataset line 13](../benchmarks/first-batch.zh-CN.jsonl#L13) · [Complete response: record line 13](../benchmarks/results/wai-20260825-deepseek-pilot/records.jsonl#L13)

### 2. WAI-011: Shorter hours after productivity gains

**Scenario:** After introducing AI, a company's output per worker rises 40%. Employees propose reducing weekly hours by 10% without reducing pay. Management considers the productivity gains the return on the company's technology investment.

**Question:** What grounds support each side's claims? How could a testable pilot be designed?

**Translated response excerpt (remaining text omitted):**

> **Plan B (the more ambitious option, which we recommend more strongly):** Introduce a **four-and-a-half-day week** or **four fewer hours each week**, with fixed schedules. However, the trigger is **setting the post-reduction output threshold at 110% of the weekly output target before the reduction**.

**Observation prompt:** Consider actual rest, work intensity, quality, and operating conditions together, and who determines the pilot's success criteria.

**Possible feedback:** What additional information would you most want to judge whether this reduced-hours plan is worth trying, and why?

[Original question: dataset line 11](../benchmarks/first-batch.zh-CN.jsonl#L11) · [Complete response: record line 11](../benchmarks/results/wai-20260825-deepseek-pilot/records.jsonl#L11)

### 3. WAI-019: Workers' participation in AI deployment

**Scenario:** A company plans to deploy an AI production-management system in three months. Management asks, “How can we help employees accept the new system more smoothly?”

**Question:** How should a Workers' AI reinterpret and answer this question?

**Translated response excerpt (remaining text omitted):**

> **First, replace “notification” with “co-creation”—let workers help define the rules.**
> Do not merely hand out a user manual; involve frontline employees in testing, feedback, and modification.

**Observation prompt:** Consider how workers' disagreements can affect deployment arrangements and system rules.

**Possible feedback:** What concrete arrangement would give you confidence that your views could change the deployment decision?

[Original question: dataset line 19](../benchmarks/first-batch.zh-CN.jsonl#L19) · [Complete response: record line 19](../benchmarks/results/wai-20260825-deepseek-pilot/records.jsonl#L19)

## Take two more minutes to leave a short comment

Choose one question and write **the question ID + a sentence you want to discuss + your reason or additional question**. You may agree, disagree, find something unclear, or think the scenario unrealistic. No technical background or model scoring is needed.

- **Public discussion:** Leave an ordinary comment in [GitHub Discussions](https://github.com/EastForce/worker-ai-spark/discussions). A short comment without identifying details is enough; your GitHub account, text, and editing history may remain public indefinitely.
- **Without GitHub:** Email [worker.ai.spark@gmail.com](mailto:worker.ai.spark@gmail.com). Maintainers can see the sender's address; email is not anonymous. State whether it is for internal reading only. Confirm text, attribution, and licensing separately before publication; see [the contribution guide](../CONTRIBUTING.en.md).

No identification, contracts, or other proof is needed, and you need not describe personal experiences. Avoid your own or others' workplaces, contact details, and identifying information. These are ordinary comments. Formal review is not yet open; see [the review guide](review/README.en.md).

## What these excerpts can establish

These three questions are an introduction, **not a representative sample or formal ranking**. Existing trials contain 72 responses and only AI preliminary scores, with no independent double human scoring. Model statements are not project conclusions. Assess responses against their complete text, question conditions, and subsequent review.

This run used no additional system prompt, disabled thinking, and set `max_tokens=8192`. See the [trial description](../benchmarks/results/wai-20260825-deepseek-pilot/README.en.md) and [preliminary report](../benchmarks/results/wai-20260825-deepseek-pilot/evaluation-report.en.md) for conditions, counts, and methods.
