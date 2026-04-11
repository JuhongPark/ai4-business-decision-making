# Prediction-Judgment Interleave Mapping

status: Track B deliverable
date_created: 2026-04-11
purpose: classify the 18 market research tasks by prediction-judgment profile, identify where prediction ends and judgment begins within each task, and design handoff protocols for each boundary type

## Analytical Basis

Agrawal, Gans, and Goldfarb (2018) distinguish prediction (estimating what will happen given inputs) from judgment (deciding what to do given a prediction, factoring in values, context, and risk tolerance). This distinction is clean in theory but blurred in practice. Most real tasks interleave prediction and judgment within a single workflow step.

This analysis classifies each of the 18 market research tasks from the task decomposition (task-decomposition.md) into one of three profiles and identifies the specific handoff point where AI authority should transfer to human judgment.

## Task Classification

### Profile Definitions

| Profile | Definition | AI Role | Human Role | Handoff Design |
| --- | --- | --- | --- | --- |
| **Prediction-dominant** | Output is primarily a factual estimate or data synthesis. Judgment is minimal or deferred to a later stage. | Execute and present | Review output quality, check for errors | **Clean handoff**: AI delivers complete output; human validates before passing to next stage |
| **Interleaved** | Task requires both factual estimation and contextual interpretation within the same step. Prediction and judgment cannot be cleanly separated. | Generate intermediate analysis | Interpret, contextualize, and complete | **Checkpoint handoff**: AI produces intermediate output; human validates and adds judgment at each checkpoint |
| **Judgment-dominant** | Output requires values, priorities, strategic context, or normative assessment. Factual inputs are necessary but insufficient. | Prepare inputs and options | Make the decision; use AI as input, not answer | **Parallel path**: AI and human produce independent analyses; human reconciles |

### Classification of All 18 Tasks

#### Stage 1: Environmental Scanning

| Task | Profile | Prediction Component | Judgment Component | Handoff Point |
| --- | --- | --- | --- | --- |
| 1.1 Source identification | **Prediction-dominant** | Identify and collect relevant sources from defined scope | Minimal: inclusion criteria are pre-specified | Clean handoff: AI delivers curated source list; human spot-checks source quality ratings |
| 1.2 Regulatory assessment | **Interleaved** | Identify current regulations and recent changes | Interpret compliance implications for the specific business context | Checkpoint: AI delivers regulatory landscape → human interprets implications |
| 1.3 Signal-noise discrimination | **Judgment-dominant** | Identify candidate signals from data | Determine which signals are durable vs noise; requires industry intuition | Parallel: AI generates candidate signal list; human independently assesses; reconcile |

#### Stage 2: Trend Identification

| Task | Profile | Prediction Component | Judgment Component | Handoff Point |
| --- | --- | --- | --- | --- |
| 2.1 Trend pattern recognition | **Prediction-dominant** | Detect temporal patterns in data series | Minimal: pattern detection is primarily statistical | Clean handoff: AI delivers identified patterns with evidence; human validates data quality |
| 2.2 Trend trajectory estimation | **Interleaved** | Extrapolate trend direction and magnitude | Select appropriate analogies; assess whether historical patterns apply to current context | Checkpoint: AI generates trajectory estimate with assumptions → human validates assumptions and adjusts |
| 2.3 Trend significance assessment | **Judgment-dominant** | Rank trends by quantitative indicators | Assess strategic relevance, which requires understanding business priorities and competitive position | Parallel: AI ranks by data; human ranks by strategic relevance; reconcile |

#### Stage 3: Customer Need Extraction

| Task | Profile | Prediction Component | Judgment Component | Handoff Point |
| --- | --- | --- | --- | --- |
| 3.1 Feedback synthesis | **Interleaved** | Extract themes from customer data | Interpret what themes mean for product decisions; distinguish genuine needs from noise | Checkpoint: AI extracts themes → human validates against domain knowledge → AI refines |
| 3.2 Latent need identification | **Judgment-dominant** | Identify behavioral patterns that suggest unmet needs | Infer causal motivation (JTBD); requires empathetic and contextual reasoning | Parallel: AI proposes latent needs; human proposes independently; compare for convergence and divergence |
| 3.3 Need prioritization | **Interleaved** | Score needs against quantitative criteria (market size, frequency) | Weight criteria, resolve trade-offs, assess strategic fit | Checkpoint: AI scores → human reviews weights and adds strategic judgment → final prioritization |

#### Stage 4: Competitive Mapping

| Task | Profile | Prediction Component | Judgment Component | Handoff Point |
| --- | --- | --- | --- | --- |
| 4.1 Competitor capability assessment | **Prediction-dominant** | Compile competitor data from public sources | Minimal: synthesis of verifiable information | Clean handoff: AI delivers competitor profiles; human validates currency and completeness |
| 4.2 White space identification | **Interleaved** | Identify gaps in competitor coverage by cross-referencing need map with capability map | Assess whether gaps represent real opportunities or reflect data limitations | Checkpoint: AI identifies gaps → human assesses which gaps are genuine market opportunities |
| 4.3 Competitive response prediction | **Judgment-dominant** | Model likely competitor moves based on capability and history | Assess competitor intent, risk tolerance, and strategic priorities — requires game-theoretic reasoning about intentional actors | Parallel: AI generates response scenarios; human adds strategic intuition; reconcile |

#### Stage 5: Market Sizing

| Task | Profile | Prediction Component | Judgment Component | Handoff Point |
| --- | --- | --- | --- | --- |
| 5.1 Market size estimation | **Prediction-dominant** | Calculate addressable market using data and assumptions | Minimal: estimation is primarily quantitative, though assumption selection involves judgment | Clean handoff: AI delivers estimate with assumptions; human validates assumptions |
| 5.2 WTP assessment | **Interleaved** | Estimate price sensitivity from data and analogies | Select appropriate analogies; assess whether pricing context applies | Checkpoint: AI generates WTP range → human validates analogy selection and adjusts |
| 5.3 Opportunity prioritization | **Judgment-dominant** | Rank opportunities by quantitative scores | Weight dimensions, resolve trade-offs between market size and strategic fit, make go/no-go recommendations | Parallel: AI ranks quantitatively; human ranks by strategic priority; reconcile |

#### Stage 6: Concept Generation

| Task | Profile | Prediction Component | Judgment Component | Handoff Point |
| --- | --- | --- | --- | --- |
| 6.1 Concept generation | **Judgment-dominant** | Generate concept options based on need-capability map | Evaluate novelty, strategic alignment, and creative quality — requires vision and values | Parallel: AI generates concepts; human generates independently; merge for diversity |
| 6.2 Feasibility assessment | **Interleaved** | Evaluate concepts against technical and financial constraints | Assess which constraints are hard vs soft; weigh trade-offs between ambition and feasibility | Checkpoint: AI evaluates constraints → human assesses constraint flexibility → joint feasibility score |
| 6.3 Concept screening | **Judgment-dominant** | Score concepts on defined criteria | Make go/no-go decisions with resource commitment implications; requires risk tolerance and strategic conviction | Parallel: AI scores; human makes independent assessment; AI score is one input to human decision |

## Summary Distribution

| Profile | Tasks | Count | Percentage |
| --- | --- | --- | --- |
| Prediction-dominant | 1.1, 2.1, 4.1, 5.1 | 4 | 22% |
| Interleaved | 1.2, 2.2, 3.1, 3.3, 4.2, 5.2, 6.2 | 7 | 39% |
| Judgment-dominant | 1.3, 2.3, 3.2, 4.3, 5.3, 6.1, 6.3 | 7 | 39% |

**Key finding**: Only 22% of market research tasks are prediction-dominant. The remaining 78% require human judgment at some point within the task, not just as post-hoc review.

## Handoff Protocol Designs

### Protocol 1: Clean Handoff (Prediction-Dominant Tasks)

```
[AI executes full task] → [AI delivers output with metadata] → [Human spot-checks] → [Pass to next stage]

Metadata required:
- Sources used and their quality levels
- Assumptions made
- Confidence assessment
- Known gaps in coverage

Human check (5-10 minutes):
- Source quality adequate? (Level 3+ for substantive claims)
- Assumptions reasonable? (No obviously flawed premises)
- Coverage gaps acceptable? (No critical blind spots)

Decision: Accept / Request revision / Flag for deeper review
```

**Applicable to**: 1.1 Source identification, 2.1 Trend pattern recognition, 4.1 Competitor capability assessment, 5.1 Market size estimation

**Estimated time overhead**: 5-10 minutes per task = 20-40 minutes for all 4 tasks

### Protocol 2: Checkpoint Handoff (Interleaved Tasks)

```
[AI generates intermediate analysis] → [Human reviews at checkpoint] → [Human adds judgment] → [AI incorporates] → [Repeat or proceed]

Checkpoint structure:
Step 1: AI produces factual/analytical component
Step 2: Human reviews factual component for accuracy
Step 3: Human adds contextual interpretation or judgment
Step 4: AI integrates human input into next analytical step
Step 5: Human validates integrated output

Pre-commitment option: Human records preliminary judgment before viewing AI output at each checkpoint (from Track A evidence)
```

**Applicable to**: 1.2 Regulatory assessment, 2.2 Trend trajectory, 3.1 Feedback synthesis, 3.3 Need prioritization, 4.2 White space identification, 5.2 WTP assessment, 6.2 Feasibility assessment

**Estimated time overhead**: 15-25 minutes per task = 1.75-2.9 hours for all 7 tasks

### Protocol 3: Parallel Path (Judgment-Dominant Tasks)

```
[AI generates analysis] ──┐
                          ├→ [Human reconciles] → [Final output]
[Human generates analysis]┘

Parallel structure:
Step 1: Human and AI receive the same task prompt
Step 2: Human produces independent analysis (without seeing AI output)
Step 3: AI output is revealed
Step 4: Human reconciles, noting:
  - Where AI and human converge (high confidence)
  - Where AI and human diverge (requires investigation)
  - Where AI added value (novel insight or broader coverage)
  - Where AI was deficient (missed context, sycophantic, miscalibrated)
Step 5: Final output is the human's reconciled analysis

Key rule: The human analysis is the baseline. AI adds to it; it does not replace it.
```

**Applicable to**: 1.3 Signal-noise discrimination, 2.3 Trend significance, 3.2 Latent need identification, 4.3 Competitive response, 5.3 Opportunity prioritization, 6.1 Concept generation, 6.3 Concept screening

**Estimated time overhead**: 20-40 minutes per task = 2.3-4.7 hours for all 7 tasks

## Total Verification Cost Estimate

| Protocol | Tasks | Time per Task | Total Time |
| --- | --- | --- | --- |
| Clean handoff | 4 prediction-dominant | 5-10 min | 20-40 min |
| Checkpoint handoff | 7 interleaved | 15-25 min | 1.75-2.9 hrs |
| Parallel path | 7 judgment-dominant | 20-40 min | 2.3-4.7 hrs |
| **Total** | **18 tasks** | | **4.4-8.1 hrs** |

**Comparison**: A full market research cycle without AI takes an experienced analyst 40-80 hours. With AI and verification, estimated time is 12-20 hours (AI generation) + 4.4-8.1 hours (verification) = 16.4-28.1 hours. This represents a **60-65% time reduction** while maintaining professional reasoning quality.

Without verification: 4-8 hours (AI generation only, no human review). Fast but with unknown error rates and de facto automation of judgment.

## How This Changes Authority Recommendations

The interleave mapping refines the task decomposition authority assignments:

| Original Assignment | Refinement |
| --- | --- |
| ASSIST tasks (10) | 6 are judgment-dominant → Parallel path protocol. 4 are interleaved → Checkpoint protocol. |
| RECOMMEND tasks (8) | 4 are prediction-dominant → Clean handoff sufficient. 3 are interleaved → Checkpoint protocol. 1 is judgment-dominant → should be reclassified to ASSIST. |

**Reclassification candidate**: Task 4.3 (Competitive response prediction) was scored at RECOMMEND but is judgment-dominant with edge-case override. The interleave mapping confirms it should be ASSIST with parallel path protocol.

## Connection to Other Tracks

| Finding | Track | Implication |
| --- | --- | --- |
| 78% of tasks require judgment handoff | Track A | Pre-commitment protocol applies at judgment entry points, not globally |
| Checkpoint protocol interrupts pipeline | Track C | Checkpoints may reduce sycophancy compounding by inserting human judgment between stages |
| 60-65% time reduction with verification | Practitioner roadmap | Quantified cost-benefit for organizational business case |
| Parallel path for judgment tasks | Track D | Judgment-dominant tasks should never score as automatable |
