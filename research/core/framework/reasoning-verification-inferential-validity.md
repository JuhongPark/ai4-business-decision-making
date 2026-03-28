# Inferential Validity Assessment Method

status: active
phase: 2.3
date: 2026-03-28
purpose: Structured method for assessing whether conclusions in AI-generated business reasoning follow from their premises.

## The Problem

Even when all facts and sources are correct, the logical chain connecting evidence to conclusions may be flawed. AI outputs frequently present confident conclusions that do not logically follow from the evidence provided. This method gives practitioners a structured way to check inferential validity without formal logic training.

---

## Step 1: Decompose the Reasoning Chain

Break the AI output into discrete inferential steps. Each step has the form:

```
[Evidence/Premise] → [Inference type] → [Claim/Conclusion]
```

For a typical AI business analysis, identify:
- The foundational premises (market data, trends, company facts)
- The intermediate inferences (interpretations, comparisons, causal claims)
- The final conclusions and recommendations

Number each step. A typical business analysis contains 5-15 inferential steps.

## Step 2: Classify Each Inference

For each inferential step, identify which type of reasoning is being used:

| Type | Definition | Strength | Key Risk |
|---|---|---|---|
| **Deductive** | Conclusion necessarily follows from premises | Strongest if premises are true | Premises may be false or incomplete |
| **Inductive** | Conclusion is probable given evidence | Moderate — depends on sample quality | Sample may not be representative |
| **Abductive** | Best explanation for observed data | Weakest — depends on alternatives considered | Better explanations may exist |
| **Analogical** | Reasoning by similarity to another case | Variable — depends on similarity depth | Critical differences may be hidden |

## Step 3: Apply Type-Specific Validity Checks

### For Deductive Inferences
- Are the premises explicitly stated and verifiable?
- Does the conclusion necessarily follow? (If premises are true, can the conclusion be false?)
- Are there hidden premises that are assumed but not stated?

### For Inductive Inferences
- Is the sample representative of the population being generalized to?
- Is the sample size adequate for the strength of the conclusion?
- Are there important differences between the sample cases and the target case?
- Is the base rate accounted for?

### For Abductive Inferences
- What alternative explanations exist for the same observation?
- Were alternatives considered and explicitly ruled out?
- What evidence would distinguish between competing explanations?
- Is the chosen explanation the simplest that accounts for the data?

### For Analogical Inferences
- What are the specific similarities between the compared cases?
- What are the critical differences?
- Are the similarities relevant to the conclusion being drawn?
- Would the conclusion hold if the differences were weighted more heavily?

## Step 4: Check for Common Inferential Failures

For each step, check against these known failure patterns:

| Failure | Check Question |
|---|---|
| Correlation-causation (B1) | Is a causal mechanism identified, or just a correlation? |
| Unjustified generalization (B2) | Is the sample large and representative enough for this claim? |
| Missing premises (B3) | What assumptions must be true for this inference to hold? Are they stated? |
| False dichotomy (B4) | Are these really the only options? |
| Scope mismatch (B5) | Does this reasoning apply in the target context, or only in the source context? |
| Confidence-evidence gap (B6) | Is the conclusion stated more strongly than the evidence warrants? |
| Circular reasoning (B7) | Does the conclusion appear (in different words) in the premises? |

## Step 5: The Reverse Test

For the final conclusion, ask:

> "What would have to be true for this conclusion to be wrong?"

This is the single most powerful validity check. It forces examination of the conditions under which the reasoning fails.

Evaluate:
- Are these failure conditions plausible? If yes, the reasoning needs to address them.
- Did the AI output acknowledge these conditions? If not, the reasoning has unexamined vulnerabilities.
- Are these conditions easily testable? If yes, they should be tested before acting on the conclusion.

If the AI output does not survive the reverse test — if plausible failure conditions are unacknowledged — the inferential validity is compromised regardless of how well-structured the reasoning appears.

## Step 6: Assess Overall Validity

| Rating | Criteria |
|---|---|
| **Valid** | All major inferential steps use appropriate reasoning types, pass type-specific checks, and survive the reverse test |
| **Conditionally valid** | Reasoning holds under stated conditions, but those conditions are not guaranteed. Decision-maker must assess whether conditions hold in their specific context. |
| **Invalid** | One or more critical inferential steps fail validity checks. The conclusion does not reliably follow from the evidence. |

---

## Worked Example

**AI output**: "Company X entered the Asian market with a direct-to-consumer strategy and achieved 40% growth in Year 1. Our company has a similar product and brand positioning. We should therefore pursue a direct-to-consumer strategy in Asia."

**Decomposition**:
- Step 1: Company X entered Asia with DTC → 40% growth (factual premise — verify)
- Step 2: Our company has similar product and positioning (analogical premise — assess)
- Step 3: Therefore the same strategy will work for us (analogical inference)

**Classification**: Analogical reasoning (Step 3)

**Validity checks for analogical inference**:
- Similarities: product type, brand positioning (stated)
- Differences not addressed: market timing, competitive landscape, distribution infrastructure, regulatory environment, pricing, team capability, capital availability
- Relevance: product similarity is necessary but not sufficient for strategy transferability

**Reverse test**: "What would have to be true for this to be wrong?"
- Company X entered an underserved market; ours may already be saturated
- Company X had existing distribution partnerships; we may not
- Market conditions may have changed since Company X's entry
- Company X's 40% growth may not have been sustained

**Assessment**: Conditionally valid. The analogy holds only if the unstated conditions (market saturation, distribution access, timing, competitive response) are similar. The AI output does not address these conditions. Before acting, each condition must be independently verified.
