# Practical Solution Synthesis: Three-Layer Intervention

status: synthesis document
date_created: 2026-04-11
purpose: distill the entire research portfolio into the three actionable interventions that the empirical evidence supports

## The Problem in One Sentence

AI produces fluent analysis that confirms what you want to hear, people accept it without checking, and checking requires the expertise AI was supposed to replace.

## The Three-Layer Solution

### Layer A: Design Tasks Bidirectionally (AI Side)

**What**: Instead of asking AI to "analyze," ask it to "analyze both sides."

**Why it works**: The sycophancy experiment (Condition 1, actual outputs with locked coding protocol) revealed that task structure determines output balance more than any post-hoc verification:

- Stage 4 (competitive mapping): confirmation rate 75%, diversity 3 — because the task structure ("compare competitors") forces the AI to present both strengths and weaknesses
- Stage 3 (customer needs): confirmation rate 91%, diversity 1 — because the task structure ("extract needs") invites one-directional confirmation
- Stage 5 (market sizing): confirmation rate 100%, diversity 1 — because the task structure ("estimate the size") invites a single number without alternatives

The intervention is at the prompt level, not the governance level:

| One-Directional Task (Sycophancy-Prone) | Bidirectional Task (Balanced) |
| --- | --- |
| "Extract customer needs for this product" | "List 3 needs this product addresses AND 3 needs it cannot address" |
| "Estimate the market size" | "List 3 reasons the market could be large AND 3 reasons it could be small, then estimate with ranges" |
| "Generate product concepts" | "Propose 2 concepts for entering this market AND 2 reasons not to enter at all" |
| "Assess the competitive landscape" | (Already bidirectional — "compare" naturally produces balance) |

**Evidence base**: Stage 4 recovery in the actual sycophancy experiment; adversarial counter-analysis design from Track C.

**Implementation cost**: Zero — this is a prompt engineering change.

### Layer B: Intervene Only at Judgment Boundaries (Process Side)

**What**: Classify every task as prediction-dominant, interleaved, or judgment-dominant. Apply human effort only where judgment is required.

**Why it works**: The prediction-judgment interleave mapping classified all 18 market research tasks:

- 4 tasks (22%) are prediction-dominant → AI executes, human spot-checks (5-10 min each)
- 7 tasks (39%) are interleaved → AI drafts, human validates at checkpoints (15-25 min each)
- 7 tasks (39%) are judgment-dominant → human decides first, then compares with AI (20-40 min each)

Verifying all 18 tasks costs 4.4-8.1 hours. Focusing human effort on the 7 judgment tasks costs 2.3-4.7 hours — roughly half the time for the decisions that actually matter.

The key insight: **the verification paradox is solvable by not trying to verify everything.** Prediction tasks (source collection, pattern detection, market calculation) can be spot-checked. Judgment tasks (need interpretation, strategic assessment, go/no-go decisions) require human engagement.

**Evidence base**: Prediction-judgment interleave mapping; automation boundary scoring (judgment-dominant tasks score 14-18, never automatable).

**Implementation**: Task router assigns each task to the right protocol. The workflow system prototype (P4) already implements this.

### Layer C: Enforce "Own Answer First" at Judgment Points (Human Side)

**What**: At every judgment-dominant task, require the human to record their own preliminary answer before seeing AI output.

**Why it works**: Buçinca, Malaya, and Gajos (2021, CSCW, N=199) demonstrated that this single intervention triples AI error detection rate (from 3% to 9% in their controlled experiment). Fogliato et al. (2022, FAccT) confirmed it works even for expert professionals (radiologists).

The mechanism: when a person forms their own answer first, they have an independent reference point. AI output is evaluated against this reference rather than accepted as the default. Without this step, the cognitive default is acceptance — the human reads the AI output, finds no obvious error, and proceeds.

**What does NOT work** (evidence from the literature review):
- Showing AI explanations → increases agreement regardless of correctness (Bansal et al., 2021)
- Training about AI limitations → no behavioral change for most users (Parasuraman and Manzey, 2010)
- Accountability checklists without enforcement → rubber-stamped (no controlled evidence found)
- Static confidence displays → users habituate within days (Okamura and Yamada, 2020)

**Implementation**: The system does not display AI output until the human submits their preliminary assessment. This is a UI constraint, not a policy — it cannot be bypassed by clicking through.

## How the Three Layers Interact

```
User submits a market research task
         │
    ┌────▼─────────────────────────┐
    │  Layer A: Bidirectional Prompt │
    │  Rewrite task to require both  │
    │  supporting and challenging    │
    │  analysis                      │
    └────┬─────────────────────────┘
         │
    ┌────▼─────────────────────────┐
    │  Layer B: Task Classification  │
    │  Prediction → AI executes      │
    │  Interleaved → Checkpoint      │
    │  Judgment → Human first        │
    └────┬─────────────────────────┘
         │
         ├── Prediction: AI output → spot-check → done
         │
         ├── Interleaved: AI draft → human checkpoint → AI revises → done
         │
         └── Judgment:
              │
         ┌────▼─────────────────────┐
         │  Layer C: Own Answer First │
         │  Human records preliminary │
         │  assessment (system blocks │
         │  AI output until submitted)│
         └────┬─────────────────────┘
              │
              ▼
         AI output revealed → Human reconciles → Final decision
```

## What This Costs

| Without this system | With this system |
| --- | --- |
| AI generates full analysis: 1-2 hours | AI generates bidirectional analysis: 1-2 hours |
| Human glances at it: 5-10 minutes | Human spot-checks 4 prediction tasks: 20-40 min |
| Total: ~2 hours, quality unknown | Human checkpoints 7 interleaved tasks: 1.75-2.9 hrs |
| | Human judges 7 judgment tasks (own answer first): 2.3-4.7 hrs |
| | **Total: 5.3-9.6 hours, quality verified** |

**Comparison**: Traditional human-only market research takes 40-80 hours. This system takes 5.3-9.6 hours — a **75-90% time reduction** with structured quality verification.

The honest trade-off: the "just let AI do it" approach takes 2 hours but has unknown (and likely poor) reasoning quality. This system takes 3-5x longer but produces verifiable output. The cost of verification is the price of being able to trust the analysis.

## What Each Research Component Contributes to This Solution

| Research Asset | What It Proves for the Solution |
| --- | --- |
| 71-incident analysis | Most failures were delegation calibration failures, not technical failures → the problem is real |
| 6-dimensional framework | Contextual scoring identifies which decisions need human judgment → Layer B classification |
| Reasoning failure taxonomy | 25 failure types show what goes wrong → informs bidirectional prompt design (Layer A) |
| Sycophancy experiment (actual) | Task structure determines output balance → Layer A is the most impactful intervention |
| De facto automation literature | "Own answer first" triples detection → Layer C is evidence-backed |
| Prediction-judgment mapping | 22% prediction / 39% interleaved / 39% judgment → Layer B allocation of human effort |
| Automation boundary scoring | Judgment tasks should never be automated → Layer B hard boundary |
| Practitioner simulation | Detection improves from 28% to 59% with tools → the system works (simulated, needs real validation) |

## Limitations

1. **Layer A depends on AI following bidirectional instructions.** Current LLMs generally do, but the quality of the "challenging" side may be weaker than the "supporting" side. The bidirectional prompt reduces but does not eliminate sycophancy.

2. **Layer B requires someone to classify tasks.** The prototype automates this for market research, but new domains require new classification. The prediction-judgment boundary is not always obvious.

3. **Layer C imposes real time cost.** "Own answer first" adds 20-40 minutes per judgment task. Organizations under time pressure may resist. The tension between verification quality and speed is fundamental, not solvable by design.

4. **The experiment was self-generated and self-coded.** The actual sycophancy data comes from a single model (Claude) generating and coding its own outputs. Independent replication with multiple models and human coders is required before these findings can be treated as established.
