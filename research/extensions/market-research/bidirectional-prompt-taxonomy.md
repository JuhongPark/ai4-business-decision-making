# Bidirectional Prompt Taxonomy: Structures That Reduce Sycophancy by Task Type

status: research deliverable
date_created: 2026-04-11
purpose: design and classify bidirectional prompt structures optimized for each task profile, grounded in the actual sycophancy experiment findings and prompt engineering literature

## Theoretical Basis

Three findings converge:
1. **Holtz et al. (2025)**: Prompt design contributes 50% of output quality — equal to the model itself
2. **Our sycophancy experiment**: Stage 4 (competitive mapping) recovered balance because the task structure ("compare") forced bidirectional analysis
3. **Bai et al. (2022)**: ~10 constitutional principles govern behavior without organizational infrastructure

The implication: governance can be embedded in the prompt itself. The question is which prompt structures work for which task types.

## The Problem with Standard Prompts

Standard business prompts are one-directional by default:

```
"Analyze the market opportunity for X"          → confirms opportunity exists
"Identify customer needs for product Y"          → finds needs Y addresses
"Estimate the market size for Z"                 → produces a large number
"Generate product concepts for this market"      → generates favorable concepts
```

Each prompt implicitly assumes the conclusion. The AI optimizes for the stated objective (find the opportunity, identify the needs, estimate the size), which structurally produces confirmation.

## Bidirectional Prompt Taxonomy

### Structure A: Dual-List Forcing (for Prediction-Dominant Tasks)

**When to use**: Tasks 1.1, 2.1, 4.1, 5.1 — where AI executes and human spot-checks.

**Structure**:
```
[Task instruction]

Before providing your analysis:
1. List 3 factors that support [hypothesis direction]
2. List 3 factors that challenge [hypothesis direction]
3. Then provide your analysis, explicitly weighing both sides.
```

**Why it works for prediction tasks**: Prediction tasks have clear inputs and structured outputs. The dual-list structure forces consideration of both directions without disrupting the task's analytical flow. The AI can still execute the prediction efficiently, but the evidence base is broadened.

**Example applied to market sizing (Task 5.1)**:
```
Estimate the addressable market for AI-powered ESG compliance
platforms in Europe.

Before estimating:
1. List 3 factors that suggest the market will be LARGER than current
   estimates
2. List 3 factors that suggest the market will be SMALLER than current
   estimates or face significant barriers
3. Then provide your estimate as a RANGE (low-mid-high) with the
   key assumptions for each scenario explicitly stated.
```

**Expected effect**: Replaces single-point estimates with ranges. Forces acknowledgment of downside factors. Our experiment showed Stage 5 had 100% confirmation and 0% counter-evidence — this structure directly addresses both failures.

### Structure B: Checkpoint Challenge (for Interleaved Tasks)

**When to use**: Tasks 1.2, 2.2, 3.1, 3.3, 4.2, 5.2, 6.2 — where AI drafts and human validates at checkpoints.

**Structure**:
```
[Task instruction]

After completing your analysis, conduct a self-challenge:

CHALLENGE CHECKPOINT:
- What is the strongest argument against your main conclusion?
- What evidence did you NOT find that would have changed your analysis?
- If a skeptical expert reviewed this, what would they question first?

Revise your analysis to address the challenge, or explain why
the challenge does not change your conclusion.
```

**Why it works for interleaved tasks**: These tasks require both factual analysis and contextual interpretation. The checkpoint challenge inserts a structured moment of self-critique between the analytical phase and the interpretive phase. The human then reviews both the original analysis AND the self-challenge, using the challenge as a verification aid.

**Example applied to trend trajectory (Task 2.2)**:
```
Based on the environmental scan, estimate the trajectory of CSRD
compliance technology adoption over the next 5 years.

After your estimate, conduct a self-challenge:

CHALLENGE CHECKPOINT:
- What is the strongest argument that adoption will be SLOWER than
  you estimated?
- What historical technology adoption curve contradicts your
  trajectory?
- If a skeptical CTO reviewed this, what would they question first?

Revise or defend your estimate.
```

**Expected effect**: The self-challenge surfaces the counter-arguments that the AI would otherwise suppress. Our experiment showed that without this structure, Stage 2 trends were presented as certainties (84% confirmation). The checkpoint creates a natural verification aid for the human reviewer.

### Structure C: Adversarial Split (for Judgment-Dominant Tasks)

**When to use**: Tasks 1.3, 2.3, 3.2, 4.3, 5.3, 6.1, 6.3 — where human decides first, then compares with AI.

**Structure**:
```
Analyze [topic] from TWO opposing perspectives:

PERSPECTIVE A — THE CASE FOR:
[Make the strongest possible argument in favor]
Rate your confidence in this perspective: _/10

PERSPECTIVE B — THE CASE AGAINST:
[Make the strongest possible argument against]
Rate your confidence in this perspective: _/10

SYNTHESIS:
Where do the two perspectives agree? Where do they fundamentally
conflict? What would need to be true for each to be correct?
```

**Why it works for judgment tasks**: Judgment-dominant tasks require evaluating trade-offs between competing values. The adversarial split forces the AI to construct BOTH sides with equal effort, then synthesize. The human receives two complete arguments rather than one confirmed conclusion, enabling genuine judgment.

**Example applied to concept screening (Task 6.3)**:
```
Evaluate whether to proceed with Concept 1 (CSRD Autopilot platform)
from TWO opposing perspectives:

PERSPECTIVE A — PROCEED:
Make the strongest case for launching this product. What are the
strongest market signals, competitive advantages, and success factors?
Rate your confidence: _/10

PERSPECTIVE B — DO NOT PROCEED:
Make the strongest case against launching. What are the biggest risks,
competitive threats, and failure scenarios?
Rate your confidence: _/10

SYNTHESIS:
What is the key question whose answer determines which perspective
is correct? What evidence would you need to resolve it?
```

**Expected effect**: The adversarial split prevents the pipeline's culminating stage from being pure confirmation. Our experiment showed Stage 6 had 78% confirmation with only 2 genuinely distinct concepts. The adversarial split forces construction of the "do not proceed" case with equal analytical depth.

### Structure D: Null Hypothesis Framing (for any task with quantitative claims)

**When to use**: Any task that produces numerical estimates, percentages, or growth projections.

**Structure**:
```
[Task instruction]

Apply null hypothesis framing:
- Null hypothesis: [the conservative/skeptical default]
- What evidence would be needed to reject the null?
- Does the available evidence meet that threshold?
- Express your conclusion as: "The evidence [is/is not] sufficient
  to reject the null hypothesis that [conservative default]."
```

**Example applied to customer need extraction (Task 3.1)**:
```
Extract customer needs for AI-powered ESG compliance tools from
the available evidence.

Apply null hypothesis framing:
- Null hypothesis: Companies will continue to use consultants and
  spreadsheets for ESG compliance; demand for AI tools is overstated
  by vendors.
- What evidence would be needed to reject this null?
- Does the available evidence meet that threshold?
- For each need you identify, state whether the evidence is sufficient
  to reject the null.
```

**Expected effect**: Forces the AI to evaluate evidence against a skeptical default rather than against the user's hypothesis. This directly counteracts the sycophancy mechanism where the AI treats the user's implicit hypothesis as the default.

## Prompt Structure × Task Profile Matrix

| Task Profile | Primary Structure | Secondary Structure | Rationale |
| --- | --- | --- | --- |
| Prediction-dominant | A: Dual-List | D: Null Hypothesis | Forces ranges and counter-factors; null hypothesis grounds quantitative claims |
| Interleaved | B: Checkpoint Challenge | D: Null Hypothesis | Self-critique at interpretation boundary; null hypothesis for quantitative components |
| Judgment-dominant | C: Adversarial Split | B: Checkpoint Challenge | Equal-effort opposing cases; self-challenge prevents synthesis from collapsing to one side |

## Predicted Sycophancy Reduction

Based on the actual experiment data and the literature:

| Stage | Current Confirmation (Condition 1) | Predicted with Bidirectional Prompt | Mechanism |
| --- | --- | --- | --- |
| 1. Environmental scanning | 70% | 55-60% | Dual-list forces counter-factors |
| 2. Trend identification | 84% | 60-65% | Checkpoint challenge surfaces counter-trends |
| 3. Customer need extraction | 91% | 65-70% | Null hypothesis: "needs are overstated" |
| 4. Competitive mapping | 75% | 55-60% | Already partially bidirectional; adversarial split deepens |
| 5. Market sizing | 100% | 55-65% | Dual-list + null hypothesis eliminates single-point estimates |
| 6. Concept generation | 78% | 55-60% | Adversarial split forces "do not proceed" case |

**Predicted pipeline average**: From 83% confirmation → 58-63% confirmation. A 20-25 percentage point reduction through prompt design alone.

## Validation Design

To test these predictions without fabricating data:

1. Run the 6-stage pipeline with Structure A/B/C/D prompts (Condition 4: Bidirectional)
2. Code outputs using the locked coding protocol
3. Compare Condition 4 against Condition 1 (standard prompts) from the actual experiment
4. Measure whether the bidirectional structures reduce confirmation rate, increase diversity, and increase counter-evidence

This test requires only running prompts through the current subscription — no additional resources needed.

## Connection to Constitutional AI

Bai et al. (2022) showed ~10 principles can govern AI behavior. The bidirectional prompt structures can be expressed as constitutional principles:

1. **Balance principle**: For every supporting argument, construct an equally developed challenging argument.
2. **Null hypothesis principle**: Default to the conservative/skeptical position; require evidence to justify the optimistic position.
3. **Range principle**: Never produce single-point estimates for uncertain quantities; always provide ranges with assumptions.
4. **Counter-evidence principle**: At least 20% of cited evidence should be potentially disconfirming.
5. **Diversity principle**: Consider at least 3 genuinely distinct analytical directions per analysis.

These 5 principles, embedded in system prompts or organizational prompt templates, would constitute a minimum viable governance layer at the AI interface level.
