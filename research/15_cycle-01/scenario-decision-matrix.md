# Cycle 01: Scenario Decision Matrix

status: completed
purpose: Convert scenario pack findings into a decision matrix that can drive report conclusions and recommendations.

## Matrix

| Domain | Baseline Preferred Mode | Stress Preferred Mode | Edge-Case Preferred Mode | Escalation Rule | Fallback Rule |
| --- | --- | --- | --- | --- | --- |
| Operations | automate with guardrails | recommend or automate with guardrails | assist | escalate autonomy only when data quality and routing constraints remain stable | revert to assist when telemetry or service conditions degrade |
| Finance | assist or tightly governed recommend | assist | assist | escalate only when fairness monitoring, explainability, and auditability are strong | revert to assist when drift, subgroup impact, or macro instability rises |
| Healthcare | assist or tightly governed recommend | recommend | assist | escalate only when clinician override remains explicit and safe | revert to assist when information is incomplete or patient presentation is atypical |

## Core Rule

The preferred AI role should be determined by the `domain-scenario-condition` combination rather than by domain type alone.

## Interpretation

- operations tolerates the most autonomy, but only while the environment remains structured
- finance remains recommendation-constrained even in baseline settings
- healthcare can justify stronger recommendation support under surge conditions, but safety pressure still blocks broad automation

## Report Implication

The long-form report should present autonomy as conditional and reversible. Escalation and fallback are both necessary parts of AI deployment design.
