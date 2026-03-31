# One-Page Executive Briefing

title: AI Authority in Business Decisions
subtitle: When to Assist, Recommend, or Automate
status: completed

---

## Core Thesis

AI authority must be adaptive, not fixed. This conclusion is grounded in an analysis of 71 documented AI governance failures (2018–2026) and a 6-dimensional framework built on established governance research (Amodei et al., 2016; NIST, 2023; Lee and See, 2004). The right level of AI involvement depends on domain risk, scenario condition, evidence quality, and governance readiness. Organizations that treat AI adoption as a binary yes-or-no decision will either over-automate high-risk processes or under-use AI where it is safe and productive.

## The Decision Rule

Before deploying AI in any business decision, answer seven questions in sequence:

1. What domain is this? (operations, finance, healthcare, etc.)
2. How structured is the decision? (structured, semi-structured, unstructured)
3. How severe is the downside risk? (low, medium, high)
4. What is the current scenario condition? (baseline, stress, edge case)
5. How strong is the available evidence? (strong, moderate, weak)
6. Is the governance infrastructure ready? (audit trails, override paths, accountability)
7. What is the lowest authority level justified by the answers above?

If any answer is uncertain, default to a lower authority level.

## Domain Guidance at a Glance

| Domain | Default AI Role | Key Constraint |
| --- | --- | --- |
| Operations | automate with guardrails | revert if data quality degrades or service goals conflict |
| Marketing | recommend | bound optimization; enforce privacy controls |
| Finance | assist or tightly governed recommend | reduce autonomy on drift, subgroup anomaly, or macro instability |
| Healthcare | assist or tightly governed recommend | clinician override mandatory; revert on incomplete information |
| Investment | assist or tightly governed recommend | suitability and disclosure controls required |
| Strategy | assist | high ambiguity and low measurability limit automation |
| Product | assist or recommend | weak signal quality limits confidence |
| Market Research | assist | analyst review required to prevent hallucinated synthesis |

## Scenario Sensitivity

AI that works under normal conditions may fail under stress or edge cases. Every deployment must define:

- **Escalation triggers**: conditions under which AI authority may increase (e.g., stable data, validated workflow, bounded scope)
- **Fallback triggers**: conditions under which AI authority must decrease (e.g., data drift, fairness anomaly, incomplete information, macro instability)

## Three Practical Rules

1. **Governance before autonomy.** Do not expand AI authority until audit, override, and accountability infrastructure is operational.
2. **Evidence gates authority.** Stronger evidence is necessary but not sufficient for high-risk domains. Weak evidence always reduces allowable autonomy.
3. **Design for retreat.** A system without a tested fallback path is not deployment-ready, regardless of baseline performance.

## What This Report Is Not

This is a decision-governance study, not a universal proof that AI improves ROI across all sectors. The strongest claims concern governance logic, restriction rules, and fallback design in high-stakes domains. Operational and marketing domain examples rely on moderate evidence from company materials and are best treated as design illustrations.

---

*Source: AI in Business Decision-Making — A Scenario-Based Study of Human-AI Collaboration Across High-Stakes and Operational Domains (submission_ready_v1)*
