# The Structural Assumption: Where the Delegation Framework Depends on Verification It Does Not Provide

status: draft
date: 2026-03-28
purpose: Identify every point in the delegation framework where the logic assumes a human verification capability that the framework does not define, measure, or supply.

## Why This Document Exists

The 6-dimensional delegation framework — built grounded in 71 documented AI governance failures and existing governance research (NIST, 2023; Amodei et al., 2016; Lee and See, 2004) — answers a specific question: given a business decision context, how much authority should AI receive? It answers this through five scored dimensions (decision structure, risk level, scenario stability, evidence strength, governance readiness), three override rules, a decision tree with six sequential steps, and a 7-dimension evaluation framework with restriction defaults.

The framework is structurally sound. Its logic is internally consistent: when conditions are unfavorable, authority decreases. When risk is high and governance is weak, override rules cap authority at assist. When evidence is weak in a consequential decision, autonomy drops one level. The incident analysis validates this: applied retroactively, the framework would have recommended lower authority in 12 of 20 documented incidents.

But the framework contains a hidden dependency. Every authority level above "do not use AI" assumes that humans can meaningfully evaluate AI outputs. This document traces that assumption through each component of the framework, shows where it is empirically violated, and identifies the structural gap that reasoning verification must fill.

## Part I. The Assumption in the Scoring System

### The Assist Band (Score 5-8)

The scoring sheet defines the assist band as appropriate when "uncertainty, risk, weak evidence, or weak governance makes higher autonomy inappropriate." In assist mode, the evaluation framework specifies that "AI generates signals, summaries, or forecasts, while humans retain decision authority."

The assumption embedded here is that the human who receives the AI's signal, summary, or forecast evaluates it against independent judgment and decides whether to act on it. Assist mode is the framework's most conservative operational posture. It is the floor that the override rules enforce. It is where the framework sends decisions when conditions are unfavorable.

But assist mode still requires the human to do something specific: assess whether the AI's output is sound. If a lending model in assist mode produces a risk assessment, the human loan officer must evaluate whether that assessment reflects the applicant's actual creditworthiness. If a clinical decision support system in assist mode flags a potential diagnosis, the physician must determine whether the clinical reasoning behind the flag is valid.

The framework does not specify how this evaluation happens. It does not ask whether the human has the domain knowledge to evaluate the output, the time to do so, or a method for distinguishing sound AI reasoning from fluent but flawed AI reasoning. The assumption is that placing a decision in assist mode is sufficient. But if the human in assist mode lacks the capability or method to evaluate what the AI tells them, assist mode produces the same outcome as higher authority levels: the human accepts the AI's output.

### The Recommend Band (Score 12-13)

The scoring sheet defines the recommend band as appropriate when "the environment can support stronger AI authority, but human approval should remain visible." The evaluation framework elaborates: "AI recommends actions that humans confirm or override."

The assumption here is more demanding. In recommend mode, the human is not merely receiving a signal. The human is receiving a complete recommendation — a proposed action with implicit reasoning — and is expected to critically evaluate it before confirming or overriding. The decision tree output states this explicitly: the human confirms or overrides.

But what does "confirm or override" require? It requires that the human can assess whether the recommendation follows from the evidence, whether the reasoning chain is valid, whether the sources underlying the recommendation are credible, and whether there are contextual factors the AI has missed. The framework provides no guidance on how the human performs this assessment. It assumes the capability exists.

This is where the gap becomes operationally dangerous. The scoring system can correctly identify that a decision context warrants recommend-level authority. The decision tree can correctly route the decision through all six steps. The override rules can correctly verify that no hard constraints are violated. And the human can still rubber-stamp the recommendation because they have no method for evaluating whether the AI's reasoning deserves confirmation.

### Override Rule 3: Weak Evidence in Consequential Decisions

Override rule 3 states: "any weak evidence base in a consequential decision: reduce one autonomy level." This is the framework's most reasoning-adjacent safeguard. It recognizes that evidence quality matters and that weak evidence should constrain AI authority.

But the evidence strength scale in the scoring sheet measures institutional credibility, not reasoning validity:

- Strong (3): regulator-backed, audited, or peer-reviewed
- Moderate (2): official company or technical documentation
- Weak (1): reported or secondary evidence without direct primary confirmation

All three levels evaluate the external provenance of evidence — what institutions or processes stand behind the claim. None of them evaluate whether the reasoning from evidence to conclusion is valid. A system can receive a strong evidence rating because a regulator approved the underlying model, even if the specific output in a specific case applies that model's logic incorrectly. Conversely, an AI output that reasons soundly from well-sourced evidence would score identically on this scale to one that reasons poorly from the same sources, because the scale does not assess the inferential step.

Override rule 3 protects against situations where the evidence base is institutionally weak. It does not protect against situations where the evidence base is institutionally credible but the reasoning applied to that evidence is flawed. The interpretability bridge document identifies this same gap from a different angle: the evidence strength dimension captures performance trust and purpose trust but not process trust.

## Part II. The Assumption in the Evaluation Framework

### Human Oversight Requirement

The evaluation framework's sixth dimension, human oversight requirement, operates on three levels:

- Low: humans monitor aggregate performance
- Medium: humans approve exceptions or sensitive cases
- High: humans retain final authority over decisions

At the high level, the framework assumes that human authority is substantive — that retaining final authority means the human exercises independent judgment before a decision is executed.

The Microsoft 2025 Work Trend Index reports that 66% of employees using AI accept AI-generated output without evaluating its accuracy. A separate Salesforce survey found that 91% of executives believe employees are more likely to trust AI output than they should be. These are not edge cases. They describe the dominant pattern of human-AI interaction in organizational settings.

When 66% of the people exercising "human oversight" accept outputs without evaluation, the distinction between high oversight and low oversight collapses in practice. The framework correctly identifies that high-stakes decisions require high human oversight. But high human oversight, as the framework defines it, requires a verification capability that the majority of users demonstrably do not exercise.

### Explainability Requirement

The evaluation framework's fifth dimension, explainability requirement, operates on three levels:

- Low: limited need for detailed reasoning
- Medium: internal explainability needed for management use
- High: explanation needed for legal, ethical, or stakeholder accountability

At the high level, the framework assumes that if AI provides an explanation, humans can evaluate whether that explanation is accurate, complete, and sufficient for the accountability context.

This assumption is technically undermined by research on chain-of-thought (CoT) faithfulness. Turpin et al. (2024) demonstrate that CoT explanations are systematically unfaithful to the model's actual reasoning process — models produce plausible-sounding explanations that do not reflect the computations that generated the output. Lanham et al. (2023) find that early CoT tokens can be corrupted without affecting model outputs, indicating that the stated reasoning chain is not the causal basis for the conclusion. Estimates of CoT unfaithfulness range from 60% to over 80% depending on the task and model.

If the explanation the AI provides does not reliably reflect the process that produced the output, then requiring explainability does not achieve what the framework intends. The human receives an explanation. The human evaluates the explanation and finds it reasonable. But the explanation is not a faithful account of how the AI reached its conclusion. The verification loop appears closed but is not.

The interpretability bridge document reaches the same conclusion from the technical side: post-hoc explanations can be misleading because a saliency map that highlights reasonable input features does not guarantee those features actually drove the decision. The alignment literature bridge identifies this as Gap 1: evidence strength captures performance and purpose trust, but not process trust.

## Part III. The Assumption in the Business-Context Alignment Layers

### Layer 3: Trust Alignment

The business-context alignment framework defines trust alignment as the question: "Are users relying on the AI in the right places and for the right reasons?"

The main failure mode it identifies is "reliance based on fluency, confidence cues, convenience, or interface sequence rather than demonstrated local reliability."

The layer correctly diagnoses the problem. But it provides no method for users to determine whether they are relying on AI for the right reasons. Knowing that trust should be calibrated to local reliability does not help if the user has no way to assess local reliability. The layer identifies what should be true (calibrated trust) without providing how to achieve it (a verification method).

This is precisely the pattern the research direction document describes: organizations accept AI reasoning without scrutiny because they have no method to scrutinize it. The consulting-grade discipline of questioning every link in an analytical chain — source quality, inferential validity, normative acceptability — is a learned capability. Layer 3 assumes its existence. It does not build it.

### Layer 4: Validation Alignment

The business-context alignment framework defines validation alignment as the question: "Does the review architecture actually test the output?"

The main failure mode it identifies is "symbolic human oversight that fails because generation and validation happen inside the same interface or under the same framing pressure."

This is the framework's most precise diagnosis of the verification problem. It correctly identifies the rubber-stamp mechanism: when the AI generates an output and the human reviews it in the same interface, under time pressure, with no independent reference point, review becomes symbolic. The human sees the output, finds it plausible, and approves.

But having identified this failure mode, the alignment framework does not provide the verification architecture that would prevent it. It describes what validation alignment requires — separation of generation and review, independent evidence checks, reviewer expertise, rationale governance, escalation and stop conditions — but does not supply a methodology for any of these components. It defines the requirements without building the capability.

The gap is structural: layer 4 identifies that symbolic review fails, but the framework provides no non-symbolic review method. The human who wants to validate an AI output substantively, rather than symbolically, has no procedure to follow.

## Part IV. The Assumption in the Incident Analysis

### Prevention Through Lower Authority

The alignment failure mapping found that the framework would have prevented 12 of 20 documented incidents by recommending a lower authority level than the one at which the system was deployed. In all 10 general AI incidents and in 2 LLM incidents (CNET, Elegant Enterprise), the framework's override rules or dimension scores would have flagged the deployment as exceeding appropriate authority.

This is a genuine strength. The framework's governance logic works: it identifies when authority is too high and recommends restriction.

But prevention through lower authority is a blunt instrument. The framework prevents harm by preventing deployment at higher authority levels, not by enabling safe deployment through verified reasoning. Every incident that the framework "prevents" is prevented by saying "do not give the AI this much authority." This is correct governance. But it means the framework can only protect organizations by constraining what they do with AI, not by enabling them to do more with AI safely.

For organizations that want to use AI at recommend or automate levels — and there are legitimate, high-value use cases that warrant these levels — the framework offers no path to get there other than accumulating favorable dimension scores. It does not offer a way to verify that a specific AI output, in a specific decision instance, meets the standards that higher authority requires. The distinction between "the environment supports recommend-level authority" and "this specific recommendation is sound" is the distance between governance policy and operational verification.

### The 8 Partial and Missed LLM Incidents

The framework's detection rate for LLM incidents was markedly weaker: 4 fully caught, 5 partially caught, 1 missed entirely. The alignment failure mapping identifies the common pattern: most of the partially caught and missed cases involve output-level reasoning verification that the framework does not model.

The Air Canada chatbot gave fluent but incorrect policy guidance. The Mata v. Avianca attorneys submitted hallucinated legal cases. The Google Bard demo contained a factual error in a high-profile presentation. The DPD chatbot produced adversarial outputs. The Chicago Sun-Times published hallucinated book recommendations.

In each case, the failure was not that the AI had too much formal authority. The failure was that a specific output contained reasoning or factual errors that the human did not catch. The framework's governance logic addresses the first kind of failure (authority calibration) but not the second (output verification). The alignment failure mapping acknowledges this directly: "For LLM deployments, output verification is a distinct requirement that the framework does not model."

This is the clearest empirical signal of the structural gap. The incidents that the framework catches are governance failures — wrong authority level for the context. The incidents that the framework partially catches or misses are verification failures — wrong output accepted because no one had a method to check the reasoning.

## Part V. The Convergent Finding

Five independent components of the framework — the scoring system, the override rules, the evaluation framework, the alignment layers, and the incident analysis — each contain the same hidden dependency. Each assumes that humans can evaluate AI outputs with sufficient rigor to make their designated role meaningful.

This assumption is:

**Empirically violated.** The Microsoft 2025 data shows that 66% of employees accept AI output without evaluating accuracy. The Salesforce executive survey shows that 91% of leaders believe employees overtrust AI. These are not reports of occasional lapses. They describe the dominant mode of human-AI interaction in organizations.

**Technically undermined.** CoT faithfulness research shows that the explanations AI systems provide for their reasoning are unfaithful 60-80% of the time. The explanations sound reasonable but do not reflect the actual computation that produced the output. This means that even when humans attempt to evaluate AI reasoning by examining the AI's self-explanation, they are evaluating an unreliable account of a process they cannot observe.

**Practically unsupported.** No verification methodology exists for non-expert users to assess AI reasoning quality. The consulting industry solved this problem through years of institutional training — source scrutiny, inferential discipline, normative judgment — embedded in organizational culture and enforced through hierarchical review. No equivalent exists for evaluating AI reasoning in business contexts.

The consequence is that the framework's authority levels compress in practice. The intended gradient is:

```
assist → recommend → automate with guardrails
(human decides) → (human approves) → (human monitors)
```

Without verification capability, the effective gradient becomes:

```
assist → recommend → automate with guardrails
(human accepts) → (human accepts) → (AI acts)
```

The distinction between assist and recommend collapses because the human performs the same action in both modes: accepting the AI's output without substantive evaluation. The effective authority is higher than the framework intended at every level.

## Part VI. What This Is and What It Is Not

This analysis is not a criticism of the framework. The framework's governance logic is correct. Graduated authority calibrated to context is the right approach. Override rules that enforce hard constraints are necessary. Scenario sensitivity that reduces authority under stress and edge-case conditions is sound.

The analysis identifies a structural dependency: the framework provides the conditions under which AI authority should be granted (the WHEN) but does not provide the method by which humans verify AI outputs at each authority level (the HOW). This is not a design flaw that can be fixed by adding another dimension or another override rule. It is a missing capability layer.

The framework answers: "Given this domain, this risk level, this scenario, this evidence base, and this governance readiness, the appropriate authority level is X."

It does not answer: "Given that the authority level is X, here is how the human evaluates whether this specific AI output meets the standards that authority level X requires."

The first question is governance. The second question is verification. The framework provides governance. Reasoning verification research provides the method that makes governance operationally effective — the structured capability for humans to assess source quality, inferential validity, normative acceptability, and confidence calibration in AI-generated reasoning.

Without this capability, the delegation framework governs authority levels that exist on paper but collapse in practice. With it, the framework's authority levels become enforceable because humans have a method — not just a mandate — to evaluate what AI tells them.
