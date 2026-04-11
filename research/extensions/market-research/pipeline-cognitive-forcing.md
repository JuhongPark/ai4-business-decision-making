# Pipeline-Level Cognitive Forcing: Where to Place Human Checkpoints

status: research deliverable
date_created: 2026-04-11
purpose: determine how to distribute cognitive forcing interventions across a multi-stage AI pipeline to maximize quality while minimizing total friction

## The Gap This Fills

All existing cognitive forcing studies (Buçinca 2021, Fogliato 2022, de Jong 2025, Vasconcelos 2023, Swaroop 2026) test SINGLE decisions. They ask: "Does forming your own answer before seeing AI improve this one decision?"

But business analysis is not a single decision — it's a pipeline of 6-18 connected stages. The question becomes: if you can only insert cognitive forcing at some stages (because forcing at ALL stages is prohibitively expensive), which stages yield the highest return?

## Analysis: Stage Vulnerability × Downstream Impact

From the actual sycophancy experiment, we can rank each stage on two dimensions:

**Sycophancy vulnerability** (how much the stage generates biased output):
Based on actual confirmation rates — Stage 5 (100%) > Stage 3 (91%) > Stage 2 (84%) > Stage 6 (78%) > Stage 4 (75%) > Stage 1 (70%)

**Downstream amplification** (how much the stage's bias propagates to subsequent stages):
- Stage 1 output feeds ALL subsequent stages → highest amplification
- Stage 3 output shapes Stages 4-6 → high amplification
- Stage 5 output directly informs Stage 6 → moderate amplification
- Stage 6 is terminal → zero downstream amplification

**Combined priority = vulnerability × amplification:**

| Stage | Vulnerability Rank | Amplification Rank | Combined Priority | Intervention |
| --- | --- | --- | --- | --- |
| 3. Customer need extraction | 2nd (91%) | 2nd (shapes 4-6) | **HIGHEST** | Full cognitive forcing |
| 1. Environmental scanning | 6th (70%) | 1st (feeds all) | **HIGH** | Bidirectional prompt |
| 5. Market sizing | 1st (100%) | 3rd (informs 6) | **HIGH** | Full cognitive forcing |
| 2. Trend identification | 3rd (84%) | 4th (shapes 3-6) | **MEDIUM-HIGH** | Checkpoint challenge |
| 6. Concept generation | 4th (78%) | 5th (terminal) | **MEDIUM** | Adversarial split |
| 4. Competitive mapping | 5th (75%) | 6th (shapes 5-6) | **LOWER** | Already balanced |

## Three Checkpoint Distribution Strategies

### Strategy A: Maximum Quality (3 checkpoints)

Insert full cognitive forcing ("own answer first") at Stages 3, 5, and the Stage 2→3 boundary.

```
Stage 1 → [bidirectional prompt only]
Stage 2 → [checkpoint challenge prompt]
  ══════ HUMAN CHECKPOINT: Own answer for customer needs ══════
Stage 3 → [compare human vs AI needs]
Stage 4 → [already balanced by task structure]
  ══════ HUMAN CHECKPOINT: Own market estimate ══════
Stage 5 → [compare human vs AI sizing]
Stage 6 → [adversarial split prompt]
```

**Total human time**: ~60-90 minutes for 3 checkpoints
**Expected quality**: Pipeline confirmation rate ~58-65% (near professional standard of 50-70%)
**When to use**: High-stakes decisions (product launch, market entry, major investment)

### Strategy B: Efficient Quality (1 checkpoint)

Insert full cognitive forcing ONLY at the Stage 2→3 boundary — the critical transition point where the pipeline shifts from data synthesis to interpretation.

```
Stage 1 → [bidirectional prompt]
Stage 2 → [checkpoint challenge prompt]
  ══════ SINGLE CHECKPOINT: Own answer for customer needs ══════
Stage 3 → [compare human vs AI needs]
Stage 4-6 → [bidirectional prompts only, no human forcing]
```

**Total human time**: ~20-30 minutes for 1 checkpoint
**Expected quality**: Pipeline confirmation rate ~65-72%. The single checkpoint breaks the compounding chain at its most vulnerable point. Downstream stages benefit because Stage 3 output is more balanced.
**When to use**: Standard business analysis where time matters but quality can't be sacrificed entirely

### Strategy C: Prompt-Only (0 checkpoints)

No human cognitive forcing. Use bidirectional prompt structures (A/B/C/D from the taxonomy) at every stage.

```
Stages 1-6 → [appropriate bidirectional prompt structure per task type]
No human interruption during pipeline
```

**Total human time**: 0 during pipeline; review of final output only
**Expected quality**: Pipeline confirmation rate ~63-68%. Better than unstructured prompts (83%) but worse than human checkpoints. Bidirectional prompts alone reduce sycophancy by ~15-20 percentage points.
**When to use**: Exploratory analysis, low-stakes decisions, time-critical situations, shadow AI formalization (where any friction may cause users to abandon the tool)

## The Key Insight: One Checkpoint at Stage 2→3

If an organization can implement only ONE change to their AI pipeline, it should be:

> **Require a human to produce their own customer need assessment before viewing AI's customer need extraction.**

This single checkpoint:
1. Breaks the sycophancy chain at its most vulnerable point
2. Costs 20-30 minutes (acceptable even under time pressure)
3. Produces a reference point that improves ALL downstream judgment
4. Is the simplest possible implementation of cognitive forcing in a pipeline

The evidence: Stage 2→3 was confirmed as the critical transition in the actual experiment. Customer need extraction had 91% confirmation and diversity of 1. This is where "what the data shows" becomes "what the product should do" — the exact boundary where AI sycophancy is most dangerous.

## Interaction with Layer A (Bidirectional Prompts)

Cognitive forcing and bidirectional prompts are complementary, not substitutes:

| Intervention | What it does | What it can't do |
| --- | --- | --- |
| Bidirectional prompt (Layer A) | Forces AI to consider both sides | Can't ensure the human actually engages with the counter-evidence |
| Cognitive forcing (Layer C) | Forces human to form independent judgment | Can't improve the AI output itself |
| **Combined** | AI produces balanced output AND human has independent reference | Addresses both AI-side and human-side failure modes |

Strategy A (3 checkpoints) combines both interventions at the critical stages. Strategy C (prompt-only) relies on Layer A alone. Strategy B (1 checkpoint) is the minimum effective combination.

## Research Validation Needed

This analysis is theoretical — derived from the actual experiment data and the cognitive forcing literature. Empirical validation requires:

1. Run the pipeline under Strategy B (single checkpoint at Stage 2→3)
2. Compare confirmation rates at Stages 3-6 against Condition 1 (no intervention) from the actual experiment
3. Measure whether the Stage 3 checkpoint propagates quality improvement to Stages 4-6 without additional intervention
4. This is testable with the current subscription — the researcher can serve as the human checkpoint subject
