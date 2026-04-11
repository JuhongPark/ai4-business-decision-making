# Prototypes

Working prototypes that validate the delegation framework, reasoning verification protocols, and automation boundary tools.

## Quick Start

```bash
# P1: Delegation Scoring Engine
python -m prototypes.scoring_engine demo                    # Zillow iBuying case demo
python -m prototypes.scoring_engine delegation              # Interactive delegation scoring
python -m prototypes.scoring_engine boundary                # Automation boundary assessment
python -m prototypes.scoring_engine market-research 3.2     # Lookup specific task

# P2: AI Output Verification Suite
python -m prototypes.verification_suite                     # Full verification demo

# P3: Sycophancy Compounding Experiment
python -m prototypes.sycophancy_experiment                  # Experiment design overview

# P4: Market Research Workflow System
python -m prototypes.workflow_system                        # Full 18-task pipeline routing
```

## Prototypes

| # | Name | Status | What It Does |
| --- | --- | --- | --- |
| P1 | Scoring Engine | Working | 6-dimensional delegation scoring + automation boundary + PJ classification |
| P2 | Verification Suite | Working | Source quality audit + confidence calibration + sycophancy detection + integrated assessment |
| P3 | Sycophancy Experiment | Framework ready | 6-stage pipeline with 3 conditions; needs LLM API adapter to run |
| P4 | Workflow System | Working | Routes 18 market research tasks to appropriate handoff protocols |
| P5 | Validation Study | Protocol ready | Practitioner study design with 12 stimuli, 3 conditions, 30 participants |

## Architecture

```
P1: Scoring Engine ──────────┐
  delegation_scorer.py       │
  automation_boundary.py     ├──→ P4: Workflow System
  pj_classifier.py           │     router.py (task routing + countermeasures)
                             │
P2: Verification Suite ──────┤
  source_quality.py          │
  confidence_calibration.py  ├──→ P5: Validation Study
  sycophancy_detector.py     │     study_protocol.md
  integrated_assessment.py   │
                             │
P3: Sycophancy Experiment ───┘
  pipeline.py (6-stage experiment framework)
```

## Connection to Research

| Prototype | Primary Research Source |
| --- | --- |
| P1 | `research/core/taxonomy/scoring-sheet.md`, `automation-boundary-scoring.md` |
| P2 | `research/core/framework/reasoning-verification-*.md` |
| P3 | `research/extensions/market-research/sycophancy-compounding-analysis.md` |
| P4 | `research/extensions/market-research/prediction-judgment-interleave.md` |
| P5 | `research/operations/expansion/prototyping-research-plan.md` |
