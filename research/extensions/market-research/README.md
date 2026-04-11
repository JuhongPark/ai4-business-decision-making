# Market Research Track Guide

This track tests the reasoning verification framework against a concrete domain: AI-autonomous market research for product ideation. It is the first domain-specific empirical validation of the core reasoning failure taxonomy and verification protocols.

## Why Market Research

Market research combines low verifiability, high interpretive burden, temporal sensitivity, and sycophancy vulnerability. These properties make it both the hardest test domain for reasoning verification and the domain where verification matters most for practitioners without professional training.

## Canonical Documents

- Track plan: [market-research-plan.md](market-research-plan.md) `status: active plan`
- Professional benchmark: [professional-benchmark.md](professional-benchmark.md) `status: Phase 1 deliverable`
- Literature landscape: [literature-landscape.md](literature-landscape.md) `status: Phase 1 deliverable`
- Task decomposition: [task-decomposition.md](task-decomposition.md) `status: Phase 2 deliverable`
- Automation boundary analysis: [automation-boundary-analysis.md](automation-boundary-analysis.md) `status: analytical memo`
- De facto automation countermeasures: [de-facto-automation-countermeasures.md](de-facto-automation-countermeasures.md) `status: Track A deliverable`
- Prediction-judgment interleave: [prediction-judgment-interleave.md](prediction-judgment-interleave.md) `status: Track B deliverable`
- Sycophancy compounding analysis: [sycophancy-compounding-analysis.md](sycophancy-compounding-analysis.md) `status: Track C deliverable`
- Automation boundary scoring: [automation-boundary-scoring.md](automation-boundary-scoring.md) `status: Track D deliverable`

## Recommended Reading Order

1. [market-research-plan.md](market-research-plan.md) — research design and scope
2. [professional-benchmark.md](professional-benchmark.md) — what professional-grade reasoning looks like
3. [literature-landscape.md](literature-landscape.md) — relevant literature mapping
4. [task-decomposition.md](task-decomposition.md) — reasoning tasks and failure mode predictions
5. [automation-boundary-analysis.md](automation-boundary-analysis.md) — when full automation works vs fails
6. [prediction-judgment-interleave.md](prediction-judgment-interleave.md) — where humans must intervene in the pipeline
7. [de-facto-automation-countermeasures.md](de-facto-automation-countermeasures.md) — evidence-backed interventions
8. [sycophancy-compounding-analysis.md](sycophancy-compounding-analysis.md) — how bias accumulates across stages
9. [automation-boundary-scoring.md](automation-boundary-scoring.md) — predictive tool for automate/do-not-automate decisions

## Research Phases

| Phase | Weeks | Focus | Deliverable |
| --- | --- | --- | --- |
| 1 | 1-3 | Professional benchmark and literature landscape | professional-benchmark.md, literature-landscape.md |
| 2 | 3-5 | Task decomposition and failure mode mapping | task-decomposition.md |
| 3 | 5-9 | Empirical testing with frontier LLMs | empirical-failure-catalog.md |
| 4 | 9-12 | Verification framework development | verification-checklist.md, authority-mapping.md |
| 5 | 12-14 | Synthesis and integration | synthesis.md |

## Connection to Core Assets

- Reasoning failure taxonomy: `research/core/framework/reasoning-failure-taxonomy.md`
- Delegation framework: `research/core/framework/evaluation-framework.md`
- Verification protocols: `research/core/framework/reasoning-verification-*.md`
- Cross-domain analysis: `research/core/domain-analysis/analysis.md`
- Information structure extension: `research/extensions/information-structure/`
