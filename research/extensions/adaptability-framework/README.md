# AI-Era Organizational Adaptability Framework Track

status: in_progress
date: 2026-04-22
parent_plan: [`research/operations/expansion/adaptability-framework-research-plan.md`](../../operations/expansion/adaptability-framework-research-plan.md)

This directory contains the empirical and analytical memos produced under the adaptability-framework research plan. The plan evolves the author's original "AI-based business decision making" frame into a research program on organizational adaptability under continuous AI-driven change, while preserving the three-pillar decomposition (AI usage × organization × technical infrastructure).

## Why this track exists

The author's original frame treated AI-supported decision making as the research object. That frame implicitly assumed a stable target — build a decision system once, operate it thereafter. The AI environment across 2022–2026 disproved that assumption: foundation models, tool surfaces, cost curves, and agent capabilities turn over on a monthly cadence. The research object has therefore shifted from "how to decide well with AI" to "how to keep the decision-making system fit under continuous AI-driven change."

This track preserves the two MIT SDM anchor questions (engineering infrastructure / managerial structure) and the author's three-pillar decomposition, but repositions decision making as the instantaneous output of a system that must itself be continuously redesigned.

## Three pillars preserved from the author's original frame

1. **AI usage framework** — how AI is actually employed inside a decision process
2. **Organizational structure** — how humans are arranged, which roles, which workflows, which governance
3. **Technical infrastructure** — datacenter / cloud / AI serving architecture / data-plane design

## Prompt inventory

Eleven prompts in four axes. Each memo is self-contained and can be read independently.

### Axis A — Pillar 1: AI Usage Framework (adaptability lens)

- [a1-foundation-model-transition.md](a1-foundation-model-transition.md) — how production organizations managed foundation model transitions
- [a2-capability-adoption-lag.md](a2-capability-adoption-lag.md) — lag curves between capability release and enterprise adoption
- [a3-workflow-retooling.md](a3-workflow-retooling.md) — workflow retooling patterns across knowledge-work domains

### Axis O — Pillar 2: Organizational Structure (adaptability lens)

- [o1-human-ai-collaboration.md](o1-human-ai-collaboration.md) — human-AI collaboration model evolution at AI-forward firms
- [o2-role-redefinition.md](o2-role-redefinition.md) — role redefinition cycles and triggers
- [o3-learning-velocity.md](o3-learning-velocity.md) — organizational learning velocity under tool flux

### Axis T — Pillar 3: Technical Infrastructure (adaptability lens)

- [t1-build-vs-rent.md](t1-build-vs-rent.md) — build vs. rent decision framework under model flux
- [t2-compute-scaling.md](t2-compute-scaling.md) — compute scaling under 10×/18-month demand growth
- [t3-technical-debt.md](t3-technical-debt.md) — technical debt in AI-native systems

### Axis M — Meta: Cross-Pillar Integration

- [m1-systems-dynamics-map.md](m1-systems-dynamics-map.md) — systems-dynamics map of the three-pillar adaptability problem
- [m2-adaptability-indicators.md](m2-adaptability-indicators.md) — measurable indicators of AI-era organizational adaptability

## Output shape per memo

Each memo follows a common five-section structure:
1. Method — how evidence was gathered
2. Evidence table — concrete cases, dates, sources
3. Pattern findings — synthesized patterns with confidence labels
4. Open questions and negative evidence
5. Feedback to the three-pillar adaptability frame

## Relation to adjacent tracks

- *Reasoning trust verification* — repositioned as a Pillar 1 sub-capability; trust-calibrated AI usage is a prerequisite for safe model swapping (see A1)
- *Scale-based decomposition* — adaptability varies by scale tier; memos should report scale-tier effects where visible
- *Healthcare and bio AI* — regulated-domain stress test; referenced in O3 and T3
- *Kaggle × freelance talent markets* — recategorized as empirical case feeder to M1 / M2

## Language

All tracked documents in this directory remain in English, with no emojis, per the project's working rules.
