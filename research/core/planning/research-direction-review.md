# Research Direction Review: From Delegation Calibration to Reasoning Trust Verification

date: 2026-03-28
purpose: Assess how the new research direction (AI reasoning trustworthiness verification) relates to the existing body of work in this repository, identify continuities and gaps, and determine what this means for the project's evolution.

## The Journey So Far

This project has followed a coherent intellectual trajectory:

1. **Starting question**: When should firms use AI to assist, recommend, or automate high-stakes business decisions?
2. **Framework answer**: AI authority should be adaptive, assigned by a 6-dimensional category system (domain, decision structure, risk level, scenario condition, AI role, evidence strength) rather than by domain label alone.
3. **Alignment extension**: Delegation calibration is an alignment problem. Even a technically aligned model may produce harmful outcomes if deployed at an inappropriate authority level.
4. **Interpretability bridge**: The evidence strength dimension is the framework's weakest point because it relies on external proxies. Mechanistic interpretability could provide genuine process trust.

Each step was a natural deepening of the same question. The project moved from "when should we use AI?" to "how do we know we can trust what AI produces?"

## The New Direction: Reasoning Trust Verification

The new research direction arrives at a problem the existing framework implicitly assumes but does not solve:

> Even if we correctly calibrate the authority level, the human who receives AI output at the "assist" or "recommend" level still needs to evaluate whether the AI's reasoning is sound. The framework tells organizations when to keep humans in the loop, but not how those humans should verify what the AI tells them.

This is not a departure from the existing research. It is the next logical step.

## How the New Direction Connects to Existing Work

### Connection 1: The Evidence Strength Gap

The interpretability bridge document identifies that evidence strength relies on external proxies (regulatory approval, peer review) and lacks process trust. The new direction attacks the same gap from a different angle:

- **Interpretability approach**: Give researchers tools to inspect model internals
- **Reasoning verification approach**: Give decision-makers tools to evaluate model outputs

These are complementary. Interpretability asks "what is the model actually doing?" Reasoning verification asks "does what the model says make sense?" Both are needed, but reasoning verification is more immediately actionable because it does not require access to model internals.

### Connection 2: The Override Rules Depend on Human Judgment

The framework's three override rules (high-risk + weak governance = cap at ASSIST; edge-case scenario = cap at ASSIST; weak evidence = reduce one level) all assume that a human decision-maker can meaningfully override AI recommendations. But the literature survey reveals:

- 66% of employees rely on AI output without evaluating accuracy (Microsoft, 2025)
- 91% of executives say employees overtrust AI (McKinsey, 2024-2025)
- AI explanations do not robustly reduce overreliance (Schemmer et al., 2023; JAIR, 2025)
- Users trust step-by-step reasoning even when conclusions are incorrect (arxiv, 2026)

If humans cannot or will not verify AI reasoning, the override rules are nominal rather than functional. The framework assumes meaningful human oversight, but the empirical evidence shows this assumption is increasingly violated. Reasoning verification methodology is what makes the override rules actually work.

### Connection 3: The 71 Incidents

The incident inventory catalogs 71 AI governance failures. Many of these involved situations where AI reasoning was accepted without adequate scrutiny:

- **Specification gaming**: The AI optimized for proxy metrics. A reasoning verification check would ask "does this reasoning path rely on the intended causal mechanism, or on a statistical shortcut?"
- **Fluent hallucination**: The AI produced confidently wrong outputs. A reasoning verification check would ask "are the intermediate steps factually grounded, not just the conclusion?"
- **Oversight failure**: Human-in-the-loop was nominal. Reasoning verification methodology converts nominal oversight into substantive oversight by giving humans a structured method to apply.

### Connection 4: The Taxonomy's AI Role Dimension

The taxonomy defines five AI roles: assist, recommend, automate with guardrails, automate without guardrails, and full autonomy. For the first three roles, a human is involved in the decision. Reasoning verification is what makes "assist" and "recommend" meaningfully different from "automate" -- the human is supposed to evaluate the AI's reasoning, not just receive its output.

Without reasoning verification capability, the distinction between "recommend" and "automate" collapses in practice. The AI recommends, and the human rubber-stamps. The new research direction addresses this collapse directly.

## What the Literature Survey Reveals

### The gap is real and documented

The landscape survey (`literature/reasoning-trust-landscape.md`) confirms that no existing framework bridges reasoning quality assessment to the business decision-maker. Existing work falls into:

1. **Technical faithfulness measurement** (for ML researchers, not practitioners)
2. **Governance frameworks** (for boards and CISOs, not individual decision-makers)
3. **Appropriate reliance measurement** (describes the problem, does not solve it)
4. **Hallucination detection** (checks facts, not reasoning structure)
5. **Process reward models** (works for math/logic, not open-ended business reasoning)

The specific gap -- a practitioner-facing methodology for verifying AI reasoning quality in business contexts -- is not addressed by any existing paper, framework, or tool.

### The problem is getting worse

Key data points from the survey:

- CoT unfaithfulness rates: 60-80% in some settings (Anthropic, 2025)
- Sycophancy rates: ~58% of responses exhibit sycophantic tendencies (UNU, 2025)
- Once sycophancy is triggered, it persists in 78.5% of subsequent interactions
- Larger models produce less faithful reasoning (Lanham et al., 2023)
- Personalization features exacerbate sycophancy (MIT, 2026)

As models get more capable and more personalized, the reasoning they show becomes less faithful and more agreeable. This means the problem our research addresses is accelerating, not stabilizing.

### Existing interventions do not work well enough

The most common proposed interventions -- explanations, confidence scores, transparency -- show limited effectiveness:

- Explanations do not robustly reduce overreliance (multiple studies)
- Complex explanations increase cognitive load and can reinforce unwarranted trust
- Confidence scores only help when well-calibrated, and miscalibration worsens trust
- Transparency can overwhelm rather than inform

A new approach is needed. The reasoning verification framework should not rely on the AI explaining itself (which the faithfulness literature shows is unreliable) but on structured external assessment of the reasoning.

## What Changes and What Stays

### What stays

1. **The 6-dimensional framework** remains valid. It answers when to delegate and at what authority level.
2. **The taxonomy** remains valid. The category system structures the delegation decision.
3. **The incident inventory** remains valuable as empirical grounding.
4. **The alignment connection** remains important. Delegation calibration is still an alignment problem.
5. **The interpretability bridge** remains relevant. Model internals matter for evidence strength.

### What the new direction adds

1. **A reasoning verification layer** that sits between the delegation framework and the actual human decision. The framework says "keep a human in the loop at this authority level." The verification methodology tells that human how to evaluate what the AI produces.
2. **A shift in focus from institutional governance to individual capability**. The existing framework is organizational -- it tells firms how to structure AI deployment. The new direction is personal -- it gives individual decision-makers tools to assess AI reasoning.
3. **Attention to reasoning failure modes beyond factual errors**. The new direction explicitly includes normatively deviant reasoning, systematically biased reasoning, and confidently wrong reasoning -- categories that go beyond hallucination detection.
4. **A response to passive acceptance**. The existing framework assumes active human oversight. The new direction addresses the empirical reality that oversight is increasingly passive.

### What might need revision

1. **The evidence strength dimension** may need a reasoning verification component alongside the interpretability component. Evidence strength currently measures institutional credibility and model transparency. It could be extended to include reasoning output quality.
2. **The override rules** may need a reasoning verification prerequisite. "Cap at ASSIST when governance is weak" assumes ASSIST involves genuine human evaluation. If the human cannot verify the reasoning, even ASSIST may be insufficient.
3. **The research question** may evolve from "under what conditions should firms use AI?" to "under what conditions can humans reliably verify AI reasoning, and what should firms do when they cannot?"

## Assessment

The new research direction is not a pivot. It is the resolution of a tension that was always present in the framework: the framework depends on human oversight, but human oversight depends on humans being able to evaluate AI reasoning, and no existing method reliably enables this.

The existing body of work provides the governance structure (when to keep humans in the loop). The new direction provides the verification methodology (how those humans should evaluate what AI tells them). Together, they form a complete answer to the original question: not just when to use AI, but how to use it responsibly and verify that it is working as intended.

The literature survey confirms both the importance and the novelty of this direction. The problem is well-documented (overreliance, unfaithful reasoning, sycophancy) but the solution is not. This positions the research in a productive gap with clear practical value.
