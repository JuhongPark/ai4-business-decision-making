# Three Eras of AI Trust: From Interpretability to Reasoning Verification

## A Narrative Bridge

The question at the center of this research — how do humans verify what AI tells them? — is not new to this researcher. It has been the through-line of a career that began in management consulting, moved through medical AI interpretability, and now confronts the most difficult form of that question yet. Each era offered its own answer, and each answer, once sufficient, became the insufficient baseline for what followed.

This document traces that progression across three eras. It is not a literature review but a framing device: a way of showing that the problem of trusting AI reasoning in business decisions did not appear suddenly with large language models. It deepened gradually, and the tools that resolved earlier versions of the problem are precisely what reveal the inadequacy of current approaches.

---

## Era 1: The Interpretability Era — Seeing Why the Model Decided

Before large language models, the central problem of AI adoption was not accuracy. Traditional machine learning models — gradient-boosted trees, random forests, logistic regressions tuned on carefully engineered features — frequently matched or exceeded human performance on well-defined prediction tasks. The problem was that people would not use them.

This researcher encountered this resistance firsthand while working on medical AI systems. A model could predict tissue malignancy with measurable precision, yet clinicians declined to incorporate its outputs into diagnostic workflows. The objection was not that the model was wrong. The objection was that no one could see *why* it reached its conclusion. A prediction without a rationale was, to a domain expert, not evidence but assertion. And assertions from opaque systems do not survive the scrutiny that high-stakes decisions demand.

The solution that emerged — and that this researcher contributed to through work with SHAP (SHapley Additive exPlanations) and related interpretability methods — was to open the model's reasoning to inspection. Feature attribution techniques decomposed a prediction into the contributions of individual input variables. In the medical context, this meant showing a physician not just that a tissue sample was flagged as suspicious, but that the model's assessment was driven by specific morphological characteristics: cell density in a particular region, irregularity of nuclear boundaries, the ratio of stromal to epithelial tissue.

The effect was transformative, and it was transformative for a precise reason. When a physician saw that the model attended to the same tissue features that pathological training had taught them to examine, the model's output shifted from unexplained assertion to evaluable evidence. The physician could apply independent domain knowledge to the model's reasoning chain: *Yes, those are the right features to consider for this tissue type. The weighting makes clinical sense. I would have looked at the same regions.* Trust was not granted on the basis of accuracy statistics. It was constructed through a verification loop in which the human expert assessed the model's reasoning against their own professional judgment.

This verification loop worked because three conditions held simultaneously:

1. **Evidence was discrete.** Feature weights and attribution scores are concrete, enumerable quantities. A physician could examine each contributing factor individually.
2. **Domain experts possessed independent knowledge.** The clinician's training provided a standard against which the model's feature selection could be evaluated without relying on the model itself.
3. **Verification was binary in practice.** Either the model focused on clinically relevant features or it did not. The assessment, while requiring expertise, was not ambiguous.

These conditions made the interpretability era's trust problem genuinely solvable. The tools matched the task. For the consulting world this researcher came from — trained at BCG in evidence verification for recommendations worth tens of billions of won — the logic was familiar. A junior consultant's analysis was never accepted on the strength of its conclusions alone. Partners examined the evidence chain: which data sources, which analytical method, which assumptions. Interpretability tools gave AI outputs the same kind of auditable trail.

The era closed not because interpretability failed, but because the nature of AI output changed.

---

## Era 2: The LLM Fact-Checking Era — When Trust Inverted

The arrival of large language models inverted the trust dynamic entirely. Where traditional ML suffered from too little trust, LLMs generated too much.

The reason was immediately apparent to anyone who had worked in professional services. LLM outputs did not look like the terse numerical predictions of traditional models. They looked like consultant memos. They were fluent, structured, and confident. They used appropriate hedging language. They organized arguments into numbered lists with topic sentences. They cited sources. To a business user accustomed to receiving polished deliverables, the form of LLM output activated the same cognitive heuristics that signal trustworthiness in human-authored professional communication.

The initial wave of concern focused on hallucination — the tendency of language models to fabricate facts, invent citations, and present non-existent studies as established findings. This was a serious problem, but it was, in an important sense, a tractable one. Fact-checking is laborious but methodologically straightforward. A claim can be traced to its purported source. A citation can be looked up. A statistic can be verified against the original dataset. Given sufficient time and access, individual factual claims in an LLM output can be confirmed or refuted.

What this researcher observed in practice, however, was that even this tractable form of verification proved too demanding for most organizational contexts.

At company after company, the pattern was the same. Employees received LLM-generated outputs — market analyses, strategic summaries, draft recommendations — and accepted them without checking even the most basic factual claims. The fluency of the output, its structural resemblance to professionally authored documents, created a presumption of reliability that bypassed the verification habits these same employees would have applied to a junior colleague's work. A human analyst who cited a statistic would be asked for the source. An LLM that cited the same statistic was taken at its word.

This was not laziness or negligence. It was a rational response to an irrational situation. The volume of LLM output overwhelmed existing verification workflows. A tool that could produce in seconds what previously took days created an implicit expectation that the output should be consumed at comparable speed. The organizational incentive structures that once allocated time for evidence review had not adapted to a context in which the bottleneck shifted from production to verification.

The fact-checking era revealed something important: the interpretability era's verification loop, elegant as it was, depended on the simplicity of what needed to be verified. Feature weights are discrete objects. Factual claims embedded in natural language paragraphs are not. They must be extracted, disambiguated, contextualized, and individually researched. The effort required scales with the length and complexity of the output, and LLMs produce output at a scale that traditional ML never did.

Yet for all its practical difficulty, fact-checking remained conceptually clear. The question "Is this claim true?" has a definite answer in principle, even when finding that answer is expensive. The next era would not offer even that consolation.

---

## Era 3: The Reasoning Trust Era — When Correctness Is Not Enough

The transition to the current era began with a deceptively simple observation: even when every fact in an LLM output is correct, the reasoning that connects those facts may be deeply flawed.

This researcher's recognition of the problem was sharpened by a specific experience. An LLM-generated marketing strategy analysis, produced in a context adjacent to BCG-level consulting work, made the claim that advertising trend cycles had shortened to under one week. The claim was supported by citations — blog posts from marketing platforms, promotional materials from advertising agencies, commentary from industry newsletters. The facts, narrowly construed, were not fabricated. Those sources existed and did say approximately what was attributed to them.

At BCG, however, those sources would never have survived evidence review. Blog posts from platforms with a commercial interest in advertising frequency are not independent evidence of market dynamics. Agency sales materials describing shortened cycles are marketing collateral, not analytical findings. The claim about trend cycle duration was not wrong because the citations were fake. It was wrong because the *reasoning* — the inference from source material to strategic conclusion — failed to apply the evidentiary standards that distinguish rigorous analysis from superficial pattern-matching.

Yet people accepted it. The output was well-structured. The citations were real. The conclusion was plausible. It looked, in every surface respect, like the kind of analysis a competent professional might produce. The failure was invisible precisely because it occurred at the level of reasoning quality rather than factual accuracy.

This experience crystallized three questions that, taken together, define the research problem:

1. **Are the facts correct?** This is hard but ultimately solvable. Given time and resources, factual claims can be verified against primary sources.
2. **Is the reasoning valid?** This is substantially harder. Evaluating whether a conclusion follows legitimately from its premises, whether evidence is weighted appropriately, whether alternative explanations have been considered — these are judgments that require not just domain knowledge but methodological sophistication.
3. **Can the user even tell whether the reasoning is valid?** This is the hardest question, and the most important one.

The third question is where the current era diverges most sharply from its predecessors. In the interpretability era, a domain expert could see the model's feature attributions and apply professional judgment. The verification mechanism was built into the workflow. In the fact-checking era, verification was difficult but the *need* for verification was at least conceptually apparent — everyone understood that LLMs could hallucinate.

In the reasoning trust era, the failure mode is invisible by default. A business user reading a well-structured analysis with accurate citations has no obvious signal that the reasoning connecting those citations to the conclusion is inadequate. The output does not announce its own inferential weakness. It does not flag that its sources, while real, are insufficient for the weight of the conclusion drawn from them. The surface quality of the presentation actively obscures the depth of the reasoning deficit.

The consulting industry solved this problem for human-generated analysis, but the solution took decades and cannot be trivially transferred. Management consulting firms like BCG developed elaborate institutional mechanisms for reasoning verification: structured evidence review processes, explicit standards for source quality, adversarial challenge sessions in which partners systematically probed the logical connections in an analysis. Junior consultants learned, through years of apprenticeship, to distinguish between evidence that *supports* a conclusion and evidence that merely *accompanies* it.

No equivalent mechanism exists for AI-generated reasoning. There is no institutional culture of scrutinizing LLM logic. There is no professional training that teaches business users to evaluate whether an AI's inferential chain meets the standards that the same conclusion would face if presented by a human analyst. The tools of the interpretability era — feature weights, attribution scores — do not apply to free-form reasoning in natural language. The tools of the fact-checking era — source verification, citation checking — catch only the most superficial layer of the problem.

---

## The Continuity of the Question

What connects these three eras is not technology but a persistent human problem: how to evaluate AI outputs when the evaluator cannot replicate the process that produced them. In each era, the gap between AI capability and human verifiability took a different form, and in each era, the solution that closed the previous gap proved insufficient for the next.

The interpretability era closed the gap with transparency — show the human what the model sees, and let domain expertise do the rest. The fact-checking era attempted to close the gap with verification — check the claims individually, even if the process is slow. The reasoning trust era has not yet found its closing mechanism. The gap between what LLMs produce and what humans can meaningfully evaluate remains open.

This research is an attempt to understand the structure of that gap and to ask what it would take to close it. The researcher who poses this question is the same person who helped build SHAP-based trust in medical imaging, who watched clinicians move from suspicion to collaboration when given the right tools for verification, and who now sees business decision-makers accepting AI reasoning that would not survive the first round of partner review at a consulting firm.

The question has deepened, but it has not changed. It is still, at its core: *what does it take for a human to trust AI — not blindly, but with justified confidence?* Each era answered that question for its own level of complexity. The current era has not yet answered it for reasoning. That is the work ahead.
