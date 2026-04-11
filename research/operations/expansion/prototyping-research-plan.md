# Prototyping Research Plan

status: active (prototypes built, validation in progress)
date_created: 2026-04-11
purpose: translate the accumulated research assets into working prototypes that validate the delegation framework, reasoning verification protocols, and automation boundary tools through functional implementation and empirical testing
note: the research direction has evolved toward minimum viable governance (3-layer solution). The prototypes below validate the theoretical foundation; the practical contribution is distilled in practical-solution-synthesis.md

## Why Prototyping Now

The research portfolio has reached a point where theoretical contributions are complete but empirical validation is missing. The gap:

| What exists | What does not exist |
| --- | --- |
| 6-dimensional delegation framework with scoring | A tool that applies the scoring in practice |
| 25-type reasoning failure taxonomy | A detector that identifies failures in real AI output |
| 4 verification protocols (source, inference, calibration, normative) | An integrated verification suite that a practitioner can use |
| Sycophancy compounding hypothesis with 4 indicators | Measured data from actual multi-stage AI pipelines |
| Automation boundary scoring with 100% retrospective accuracy | Prospective validation on new cases |
| 3 countermeasure designs (pre-commitment, checkpoint, assembly) | Evidence that countermeasures change behavior |
| 18-task decomposition with handoff protocols | A workflow system that routes tasks to the right protocol |

Prototyping bridges this gap. Each prototype simultaneously validates a theoretical claim and produces a usable tool.

## Prototype Architecture

Five prototypes, each building on the last:

```
Prototype 1: Delegation Scoring Engine
     ↓ (feeds authority levels into)
Prototype 2: AI Output Verification Suite
     ↓ (verification applied to)
Prototype 3: Sycophancy Compounding Experiment
     ↓ (results inform)
Prototype 4: Market Research Workflow System
     ↓ (system tested by)
Prototype 5: Practitioner Validation Study
```

## Prototype 1: Delegation Scoring Engine

### What It Is

An interactive tool that takes a business AI use case as input and outputs the recommended authority level (ASSIST / RECOMMEND / AUTOMATE WITH GUARDRAILS) with justification, override status, and automation boundary assessment.

### Components

**Module A: 6-Dimensional Delegation Scorer**
- Input: 6 dimension ratings (1-3 each) via structured questionnaire
- Processing: Sum scores, apply override rules (3 rules), map to authority band
- Output: Recommended authority level + override status + justification text
- Source: `research/core/taxonomy/scoring-sheet.md`, `decision-tree.md`

**Module B: Automation Boundary Scorer**
- Input: 6 boundary dimension ratings (1-3 each)
- Processing: Sum scores, apply override rules (3 rules), map to automation band
- Output: Automation assessment (Automatable / Conditional / Not Automatable)
- Source: `research/extensions/market-research/automation-boundary-scoring.md`

**Module C: Prediction-Judgment Classifier**
- Input: Task description
- Processing: Classify into prediction-dominant / interleaved / judgment-dominant
- Output: Recommended handoff protocol (clean / checkpoint / parallel path) + estimated time
- Source: `research/extensions/market-research/prediction-judgment-interleave.md`

**Module D: Case Library**
- 20 validated cases (6 success + 10 failure + 2 regulatory + 2 constrained) with pre-scored dimensions
- User can compare their use case score against documented cases
- Source: `automation-boundary-scoring.md` validation table

### Implementation

- Format: Python CLI tool or Streamlit web app
- Complexity: Low — primarily scoring logic and conditional routing
- Dependencies: None (pure computation)
- Estimated build time: 1-2 weeks

### Validation Test

Apply the scoring engine to 10 new AI deployment cases not in the original 20-case validation set. Measure:
- Agreement between Module A and Module B (should be >90% directional consistency)
- Agreement between tool recommendation and expert judgment (target: >80%)
- Time to complete assessment (target: <15 minutes per use case)

---

## Prototype 2: AI Output Verification Suite

### What It Is

A structured verification tool that takes AI-generated business analysis as input and produces a quality assessment using the 4 verification protocols, with failure types classified by the 25-type taxonomy.

### Components

**Module A: Source Quality Auditor**
- Input: AI-generated text
- Processing:
  1. Extract all claims with factual or quantitative content
  2. Identify source cited for each claim (or flag as unsourced)
  3. Classify each source on the 5-level hierarchy
  4. Match source level against claim type (using source-claim matching rules)
  5. Flag mismatches (claim requires Level 4+ source but cites Level 2)
- Output: Source quality report with claim inventory, source distribution, match results
- Source: `research/core/framework/reasoning-verification-source-quality.md`

**Module B: Confidence Calibration Auditor**
- Input: AI-generated text + Source quality report from Module A
- Processing:
  1. Identify 3-5 highest-stakes claims
  2. Rate expressed confidence (high/medium/low) via linguistic markers
  3. Rate evidence strength from source quality assessment
  4. Map expressed vs warranted confidence
  5. Flag over-confidence zone (high confidence + weak evidence)
  6. Run hedge test: remove hedging language, assess bare claims
- Output: Calibration report with flagged over-confident claims
- Source: `research/core/framework/reasoning-verification-confidence-calibration.md`

**Module C: Inferential Validity Checker**
- Input: AI-generated text (analyst marks key reasoning chains)
- Processing:
  1. Decompose marked reasoning into [Premise] → [Inference] → [Conclusion]
  2. Classify each inference type (deductive / inductive / abductive / analogical)
  3. Apply type-specific checks
  4. Run reverse test: "What would have to be true for this to be wrong?"
  5. Rate validity (valid / conditionally valid / invalid)
- Output: Validity report with flagged invalid steps
- Source: `research/core/framework/reasoning-verification-inferential-validity.md`

**Module D: Sycophancy Detector**
- Input: AI-generated text + original prompt
- Processing:
  1. Extract implicit hypothesis from prompt framing
  2. Measure confirmation rate (% claims supporting hypothesis)
  3. Measure diversity (number of distinct alternatives considered)
  4. Check for counter-evidence (% of disconfirming evidence cited)
  5. Check for progressive sycophancy markers (increasing confidence, narrowing alternatives)
- Output: Sycophancy risk assessment (low / medium / high) with indicators
- Source: `research/core/framework/reasoning-failure-taxonomy.md` (sycophantic category) + `sycophancy-compounding-analysis.md`

**Module E: Integrated Assessment**
- Input: Reports from Modules A-D
- Processing: Weakest-link integration — overall quality = minimum of component scores
- Output: Integrated quality assessment + priority action items
- Source: `research/core/framework/reasoning-verification-scoring-integration.md`

### Implementation

- Format: Python tool with structured input (AI text + metadata) and structured output (JSON report)
- Semi-automated: Modules A, B, D are automatable with NLP/LLM assistance; Module C requires analyst annotation
- Dependencies: LLM API for claim extraction and linguistic analysis
- Estimated build time: 3-5 weeks

### Validation Test

Apply the verification suite to 20 AI-generated market research outputs:
- 10 outputs with known significant reasoning failures (planted by researcher)
- 10 outputs with sound reasoning
- Measure: detection rate (true positive), false alarm rate (false positive), time to verify
- Target: >70% detection rate for significant failures, <20% false alarm rate

---

## Prototype 3: Sycophancy Compounding Experiment

### What It Is

The empirical test designed in Track C — running a 6-stage market research pipeline under 3 conditions and measuring sycophancy compounding with 4 indicators.

### Experimental Setup

**Scenario**: AI-autonomous market research for B2B SaaS sustainability compliance platform in Europe.

**Conditions**:
1. Full automated pipeline (no intervention)
2. Pipeline with verification checkpoints (using Prototype 2 at each stage)
3. Pipeline with adversarial counter-analysis (inverted prompt at each stage)

**Models**: Run with 3 frontier LLMs (Claude, GPT-4, Gemini)

**Measurements at each of 6 stages**:
- Confirmation rate (% claims supporting initial hypothesis)
- Diversity decay (number of distinct alternatives)
- Confidence inflation (average expressed confidence level)
- Counter-evidence suppression (% disconfirming evidence cited)

### Implementation

- Format: Python orchestration script
- Calls LLM APIs sequentially for each pipeline stage
- Automated measurement for confirmation rate and confidence inflation
- Human coding for diversity and counter-evidence (2 independent raters)
- Estimated execution time: 2-3 weeks (including coding and analysis)
- Dependencies: Prototype 2 (for Condition 2 checkpoints), LLM API access

### Expected Output

- Stage-by-stage compounding graphs for each indicator × condition × model
- Statistical comparison of 3 conditions (does intervention reduce compounding?)
- Identification of highest-compounding stage transitions
- Cross-model comparison (is compounding model-general or model-specific?)

### Validation of Research Claims

| Claim | Test | Success Criterion |
| --- | --- | --- |
| Sycophancy compounds across stages | Confirmation rate increases monotonically in Condition 1 | Stage 6 confirmation >90% |
| Checkpoints reduce compounding | Condition 2 < Condition 1 at Stage 6 | Statistically significant difference |
| Adversarial prompting outperforms checkpoints | Condition 3 < Condition 2 | Significant on at least 2 of 4 indicators |
| Stage 2→3 is the critical transition | Largest compounding jump at Stage 2→3 | Stage 2→3 delta > other stage deltas |
| Compounding is model-general | Similar patterns across 3 LLMs | Same direction of effect in all models |

---

## Prototype 4: Market Research Workflow System

### What It Is

An end-to-end workflow system that implements the delegation framework for market research: routing each of 18 tasks to the appropriate handoff protocol, integrating verification at the right points, and enforcing countermeasures against de facto automation.

### Architecture

```
[Task Router]
  ├── Prediction-dominant tasks (3) → Clean Handoff Protocol
  │     AI executes → human spot-checks (5-10 min)
  │
  ├── Interleaved tasks (7) → Checkpoint Protocol
  │     AI generates intermediate → human validates → AI integrates → repeat
  │     Verification Suite runs at each checkpoint
  │
  └── Judgment-dominant tasks (7) → Parallel Path Protocol
        AI generates analysis ─┐
                               ├→ Human reconciles
        Human generates first ─┘
        Pre-commitment enforced (analyst answers before seeing AI)
```

### Countermeasure Integration

| Authority Level | Countermeasure | Implementation |
| --- | --- | --- |
| ASSIST (10 tasks) | Pre-commitment protocol | System requires analyst preliminary assessment before displaying AI output |
| RECOMMEND (8 tasks) | Checkpoint decomposition | System gates each reasoning step; analyst validates before proceeding |
| Pipeline-level | Selective automation with assembly | System delivers stage outputs as components; analyst assembles final report |

### Implementation

- Format: Web application (Streamlit or Next.js)
- Integrates: Prototype 1 (scoring), Prototype 2 (verification), LLM APIs (AI generation)
- Workflow engine: Task routing + protocol enforcement + audit trail
- Estimated build time: 4-6 weeks
- Dependencies: Prototypes 1 and 2, LLM API access

### Validation Test

Run 5 complete market research projects through the system:
- 3 with the workflow system (treatment group)
- 2 without system, standard AI use (control group)
- Measure: reasoning quality of final output (scored by expert using taxonomy), time to complete, analyst satisfaction, number of AI failures caught

---

## Prototype 5: Practitioner Validation Study

### What It Is

A controlled study testing whether non-expert practitioners can detect reasoning failures in AI-generated market research using the verification tools (Prototype 2) and workflow system (Prototype 4) versus unassisted evaluation.

### Study Design

**Participants**: 20-30 practitioners (product managers, marketing directors, business analysts) with no formal market research training.

**Materials**: 12 AI-generated market research outputs
- 6 with significant reasoning failures (2 source, 2 calibration, 2 sycophantic)
- 6 with sound reasoning
- All outputs professionally formatted to appear equally competent

**Conditions**:
- Condition A: Unassisted evaluation (read output, assess quality, make decision)
- Condition B: Verification suite only (Prototype 2 applied, results shown to practitioner)
- Condition C: Full workflow system (Prototype 4 with countermeasures active)

**Within-subjects design**: Each participant evaluates 4 outputs per condition (2 flawed, 2 sound), counterbalanced.

**Measurements**:
- Detection rate: Did the practitioner identify the flawed outputs?
- False alarm rate: Did the practitioner reject sound outputs?
- Decision quality: Would the practitioner's decision have been different with vs without the tool?
- Time: How long did evaluation take in each condition?
- Satisfaction: How did the practitioner rate their confidence in their assessment?

### Expected Results

| Condition | Predicted Detection Rate | Predicted False Alarm | Predicted Time |
| --- | --- | --- | --- |
| A: Unassisted | 20-30% | 10-15% | 5-10 min/output |
| B: Verification suite | 50-65% | 15-20% | 15-25 min/output |
| C: Full workflow | 65-80% | 10-15% | 20-35 min/output |

### What This Proves

If results match predictions:
- The verification suite **triples** detection rate versus unassisted evaluation
- The full workflow system **further improves** detection while reducing false alarms
- The time cost (2-3x longer) is the price of verification quality
- Non-expert practitioners can perform meaningful AI reasoning verification with structured tools

This is the empirical evidence the research portfolio currently lacks: proof that the framework produces measurable improvements in human-AI decision quality.

---

## Execution Timeline

| Phase | Prototype | Weeks | Dependencies |
| --- | --- | --- | --- |
| 1 | Delegation Scoring Engine | Weeks 1-2 | None |
| 2 | AI Output Verification Suite | Weeks 2-6 | LLM API access |
| 3 | Sycophancy Compounding Experiment | Weeks 5-8 | Prototype 2, LLM APIs |
| 4 | Market Research Workflow System | Weeks 7-12 | Prototypes 1-2 |
| 5 | Practitioner Validation Study | Weeks 12-16 | Prototype 4, Participant recruitment |

Total timeline: **16 weeks** from start to first practitioner validation results.

**Parallel tracks**:
- Prototypes 1-2 build sequentially (scoring engine → verification suite)
- Prototype 3 (sycophancy experiment) can begin once Prototype 2 is functional
- Prototype 4 integrates Prototypes 1-2 and incorporates Prototype 3 findings
- Prototype 5 runs after Prototype 4 is stable

## Technology Stack Options

| Option | Stack | Pros | Cons |
| --- | --- | --- | --- |
| Minimal | Python CLI + JSON | Fast to build, no infrastructure | No UI, hard for non-technical practitioners |
| Mid-range | Python + Streamlit | Good UI, rapid iteration, shareable | Limited scalability, basic interactivity |
| Full | Next.js + Python backend + DB | Production-quality UI, audit trails, multi-user | Longer build time, infrastructure needed |

**Recommendation**: Start with Streamlit for Prototypes 1-3 (research validation). Move to production stack for Prototype 4 only if practitioner validation succeeds.

## Resource Requirements

| Resource | Purpose | Estimated Cost |
| --- | --- | --- |
| LLM API access | AI generation for experiments and verification | $200-500/month (3 providers) |
| Hosting | Streamlit Cloud or equivalent | $0-50/month |
| Participant compensation | Practitioner validation study (20-30 people × 2 hours) | $2,000-4,500 |
| Expert raters | Sycophancy experiment coding (2 raters × 40 hours) | $2,000-4,000 |
| **Total** | | **$4,500-9,500** |

## Success Criteria

The prototyping research succeeds when:

1. **Scoring engine**: Produces authority recommendations that agree with expert judgment >80% of the time on new cases
2. **Verification suite**: Detects >70% of significant reasoning failures with <20% false alarms
3. **Sycophancy experiment**: Demonstrates statistically significant compounding in Condition 1, with Conditions 2 and 3 showing measurable reduction
4. **Workflow system**: Produces market research outputs with higher reasoning quality scores than unassisted AI use
5. **Practitioner validation**: Non-experts using the tools detect at least 2x more failures than unassisted evaluation

## Connection to Publication Strategy

| Prototype | Publication Target | Venue |
| --- | --- | --- |
| 1 (Scoring engine) + validation | Framework paper with prospective validation | MISQ SI on AI-IA Nexus (deadline Oct 2025) |
| 2 (Verification suite) + 3 (Sycophancy experiment) | Empirical paper on reasoning verification | Management Science SI on AI Decisions (deadline Dec 2025) |
| 4 (Workflow system) + 5 (Practitioner study) | Design science paper | FAccT 2026 or CHI 2027 |
| All prototypes integrated | Practitioner-facing tool paper | California Management Review or MISQ Executive |

## Connection to Existing Research Assets

| Prototype | Primary Source | Supporting Sources |
| --- | --- | --- |
| 1. Scoring Engine | `core/taxonomy/scoring-sheet.md`, `decision-tree.md` | `automation-boundary-scoring.md`, `prediction-judgment-interleave.md` |
| 2. Verification Suite | `core/framework/reasoning-verification-*.md` | `reasoning-failure-taxonomy.md`, `professional-benchmark.md` |
| 3. Sycophancy Experiment | `sycophancy-compounding-analysis.md` | `task-decomposition.md`, `literature-landscape.md` |
| 4. Workflow System | `prediction-judgment-interleave.md`, `de-facto-automation-countermeasures.md` | `practitioner-implementation-roadmap.md` |
| 5. Practitioner Study | All of the above | `speculative-futures-governance.md` (scenario methods) |
