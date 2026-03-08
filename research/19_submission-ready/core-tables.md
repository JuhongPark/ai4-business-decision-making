# Submission-Ready Core Tables

status: completed
purpose: Freeze the three core tables that anchor version 1 of the report.

## Table 1: Category Taxonomy

| Dimension | Categories | Why It Matters |
| --- | --- | --- |
| Domain | strategy, operations, finance, healthcare, investment, product, marketing, market research | identifies the business context of the decision |
| Decision Structure | structured, semi-structured, unstructured | determines how far autonomy can safely scale |
| Risk Level | low, medium, high | determines governance intensity and downside tolerance |
| Scenario Condition | baseline, stress, edge-case | captures when autonomy should escalate or fall back |
| AI Role | assist, recommend, automate with guardrails | defines the level of authority assigned to AI |
| Evidence Strength | strong, moderate, weak | limits how confidently claims can support deployment |

## Table 2: Domain Recommendation Table

| Domain | Default Role | Escalation Condition | Fallback Trigger | Main Governance Concern |
| --- | --- | --- | --- | --- |
| Strategy | assist | stronger evidence and bounded decision scope | ambiguity, low measurability, synthetic overconfidence | accountability for strategic judgment |
| Operations | automate with guardrails | stable data, clear metrics, bounded objectives | degraded telemetry, disruption, conflicting service goals | monitoring and exception handling |
| Finance | assist or tightly governed recommend | strong fairness controls, auditability, stable conditions | drift, subgroup anomaly, macro instability | fairness, compliance, model risk |
| Healthcare | assist or tightly governed recommend | clinician override, validated workflow support, bounded recommendation logic | incomplete information, atypical presentation, signal unreliability | patient safety and liability |
| Investment | assist or tightly governed recommend | clear disclosure, suitability checks, auditable advisory logic | market volatility, suitability ambiguity, disclosure weakness | investor protection |
| Product | assist or recommend | stable experimentation logic and clear proxy metrics | ambiguous tradeoffs, weak user signal quality | proxy metric misuse |
| Marketing | recommend | bounded optimization, privacy controls, measurable feedback | short-term optimization bias, privacy risk, objective conflict | manipulation and privacy |
| Market Research | assist | strong analyst review and method transparency | weak sampling, hallucinated synthesis, novel context | inference quality |

## Table 3: Scenario Decision Matrix

| Domain | Baseline Preferred Mode | Stress Preferred Mode | Edge-Case Preferred Mode | Escalation Rule | Fallback Rule |
| --- | --- | --- | --- | --- | --- |
| Operations | automate with guardrails | recommend or automate with guardrails | assist | escalate autonomy only when data quality and routing constraints remain stable | revert to assist when telemetry or service conditions degrade |
| Finance | assist or tightly governed recommend | assist | assist | escalate only when fairness monitoring, explainability, and auditability are strong | revert to assist when drift, subgroup impact, or macro instability rises |
| Healthcare | assist or tightly governed recommend | recommend | assist | escalate only when clinician override remains explicit and safe | revert to assist when information is incomplete or patient presentation is atypical |

## Freeze Rule

These tables should be treated as the stable structural core of version 1 unless the analytical model itself changes.
