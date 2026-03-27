# Layer 2: Transition Conditions for AI Authority

## Status: research_complete
## Phase: 21 — Adaptive Governance Extension
## Date: 2026-03-10

---

## 1. Purpose

Phases 00-20 established that AI authority should be adaptive, not fixed. The domain recommendation table (Phase 18) defines default roles with qualitative escalation conditions and fallback triggers. But these conditions are described in natural language ("stronger evidence," "stable conditions") without measurable criteria.

This document bridges the gap by defining **graduation criteria** — specific, observable conditions under which AI authority can escalate from one mode to the next, and **regression criteria** — conditions that force authority reduction. The goal is to make the assist/recommend/automate framework responsive to AI capability changes without requiring full research revision each time a new model is released.

**Design principle:** Transition conditions should be evaluated continuously, not at fixed review intervals. When conditions change, authority level should change.

---

## 2. Architecture: Three-Layer Governance Model

```
┌──────────────────────────────────────────────────────────────────┐
│  Layer 1: Durable Principles (update cycle: years)               │
│  - AI authority must be adaptive, not fixed                      │
│  - Higher stakes require stronger governance                     │
│  - Escalation and fallback rules must be predefined              │
│  - Evidence strength constrains allowable autonomy               │
│  → Established in Phases 00-20                                   │
├──────────────────────────────────────────────────────────────────┤
│  Layer 2: Transition Conditions (update cycle: quarters)         │
│  - Measurable graduation criteria for mode escalation            │
│  - Measurable regression criteria for mode reduction             │
│  - Capability-indexed thresholds                                 │
│  - Domain-specific condition sets                                │
│  → THIS DOCUMENT                                                 │
├──────────────────────────────────────────────────────────────────┤
│  Layer 3: Living Evidence (update cycle: continuous)             │
│  - Current model capabilities and benchmarks                     │
│  - Active case evidence from deployments                         │
│  - Incident reports and failure patterns                         │
│  - Updated domain-specific recommendations                      │
│  → Next document in this phase                                   │
└──────────────────────────────────────────────────────────────────┘
```

---

## 3. Graduation Criteria Framework

### 3.1 General Graduation Criteria

To escalate AI authority from one mode to the next, **all** criteria in the target level must be satisfied. To maintain current authority, **all** criteria in the current level must remain satisfied.

#### Assist → Recommend

The system may move from assist to recommend when:

| Dimension | Criterion | Measurement |
|-----------|-----------|-------------|
| Performance | AI output quality meets or exceeds human baseline on the target task | Side-by-side evaluation, holdout comparison, or A/B test with statistical significance |
| Consistency | AI produces stable outputs across repeated evaluations of similar inputs | Variance analysis across evaluation runs; coefficient of variation below domain threshold |
| Coverage | AI handles the expected input distribution without systematic failure modes | Coverage analysis showing failure rate below domain threshold across defined subgroups |
| Explainability | AI outputs can be meaningfully explained to the decision reviewer | Explanation review by domain experts; minimum comprehension threshold met |
| Override design | Human override mechanism is operationally functional, not just documented | Override tested under realistic conditions; mean time to override measured and acceptable |
| Monitoring | Drift detection, performance tracking, and subgroup analysis are operational | Monitoring infrastructure verified; alert routing confirmed |
| Evidence | At least moderate evidence (Tier 2+) supports the system design in this domain | Evidence register updated and reviewed |

#### Recommend → Automate with Guardrails

The system may move from recommend to automate with guardrails when:

| Dimension | Criterion | Measurement |
|-----------|-----------|-------------|
| Track record | The system has operated in recommend mode for a defined observation period without material governance failures | Minimum observation period completed; incident log reviewed |
| Decision structure | Target decisions are sufficiently structured, repeated, and measurable | Decision classification confirmed; feedback loop verified |
| Risk level | Target decisions are low-to-medium risk with bounded external impact | Risk assessment documented; impact boundaries defined |
| Accuracy | System accuracy in recommend mode meets or exceeds human+AI combined baseline | Production accuracy metrics over observation period |
| Exception handling | Exception detection and routing to human review are operational and tested | Exception rate tracked; resolution quality measured |
| Rollback | Rollback capability is tested and executable within defined time bounds | Rollback tested under realistic conditions; execution time documented |
| Fairness | No material adverse impact on protected subgroups detected during observation period | Subgroup analysis completed; adverse impact metrics within thresholds |
| Governance | Audit trail, accountability assignment, and incident management are in place | Governance checklist completed by independent reviewer |
| Evidence | Strong evidence (Tier 1) supports the system design, or moderate evidence with extended successful observation period | Evidence register updated |

---

### 3.2 Regression Criteria

Authority must be reduced when any of the following conditions are detected. Regression is immediate — it does not wait for scheduled review.

#### Automate with Guardrails → Recommend

| Trigger | Detection Method |
|---------|-----------------|
| Performance degradation beyond threshold | Automated monitoring; threshold breach alert |
| Data drift detected | Distribution comparison against training/baseline reference |
| Subgroup anomaly detected | Subgroup performance monitoring shows divergence |
| Exception rate exceeds threshold | Exception counter against predefined limit |
| Rollback failure | Rollback test failure or real rollback exceeding time bound |
| External environment change | Macro indicator monitoring; scenario classification shift |
| Incident requiring investigation | Incident report filed; authority reduced pending resolution |

#### Recommend → Assist

| Trigger | Detection Method |
|---------|-----------------|
| Override rate exceeds threshold | Override tracking shows systematic disagreement |
| Fairness alert | Adverse impact metric breach on any protected subgroup |
| Explainability failure | Decision reviewer unable to understand or evaluate AI recommendation |
| Model integrity concern | Model versioning discrepancy, unauthorized change, or supply chain issue |
| Regulatory change | New regulatory requirement that current mode does not satisfy |
| Scenario shift to edge-case | Scenario classification system detects edge-case conditions |
| Evidence downgrade | Previously supporting evidence invalidated or contradicted |

---

### 3.3 Capability-Indexed Thresholds

Traditional governance fixes authority based on domain and risk. Capability-indexed governance additionally considers what the AI system can demonstrably do.

**Principle:** As AI capability improves, the set of decisions eligible for higher autonomy may expand — but only if governance, evidence, and monitoring conditions are also met. Capability improvement is necessary but not sufficient.

#### Capability Indicators

| Indicator | What It Measures | How It Connects to Authority |
|-----------|-----------------|------------------------------|
| Task accuracy | How well AI performs the target task | Higher accuracy expands eligible task set for recommend/automate |
| Reasoning transparency | Whether AI can explain its reasoning chain | Higher transparency enables recommend in domains requiring explainability |
| Robustness to distribution shift | How well AI handles out-of-distribution inputs | Higher robustness reduces edge-case regression frequency |
| Calibration quality | How well AI confidence scores match actual accuracy | Better calibration enables more reliable automated filtering |
| Adversarial robustness | How well AI resists manipulation or prompt injection | Higher robustness reduces security-related regression risk |
| Multi-step reasoning | Whether AI can reliably execute multi-stage workflows | Higher reliability expands eligible workflow stages for automation |

#### Capability-Governance Coupling Rule

```
IF   capability_improvement = true
AND  governance_conditions_met = true
AND  evidence_conditions_met = true
AND  monitoring_operational = true
THEN escalation_eligible = true

IF   capability_improvement = true
AND  any_governance_condition_unmet = true
THEN escalation_eligible = false
     (capability alone never justifies escalation)
```

This coupling ensures that when a new LLM improves task performance, the framework does not automatically escalate authority. It evaluates whether governance, evidence, and monitoring have also kept pace.

---

## 4. Domain-Specific Transition Conditions

### 4.1 Operations

**Current default:** automate with guardrails (baseline), recommend (stress), assist (edge-case)

#### Graduation: Recommend → Automate with Guardrails (for new task types)

| Condition | Specific Threshold |
|-----------|--------------------|
| Task structure | Decision is repeated at least daily with measurable outcome within 24 hours |
| Historical accuracy | System achieved ≥95% accuracy in recommend mode over 90+ day observation |
| Exception rate | Below 5% of decisions routed to human exception handling |
| Rollback tested | Rollback executable within 15 minutes under realistic conditions |
| Data quality | Input data completeness ≥98%; no systematic gaps in key variables |
| Feedback loop | Outcome feedback collected and linked to decisions within operating cycle |

#### Regression: Automate → Recommend

| Trigger | Threshold |
|---------|-----------|
| Accuracy drop | >3 percentage point decline from baseline over 7-day rolling window |
| Exception rate spike | >2x baseline exception rate sustained over 48 hours |
| Telemetry gap | >10% of expected data points missing for >4 hours |
| Service impact | Customer-facing service metric degradation beyond SLA |

---

### 4.2 Finance

**Current default:** assist or tightly governed recommend (baseline), assist (stress/edge-case)

#### Graduation: Assist → Tightly Governed Recommend

| Condition | Specific Threshold |
|-----------|--------------------|
| Fairness validation | Adverse impact ratio within regulatory thresholds across all protected groups over 180+ day observation |
| Accuracy | Model discrimination metrics (AUC, KS, etc.) stable and within validated range |
| Explainability | Every recommendation accompanied by explanation meeting regulatory standard (e.g., adverse action notice requirements) |
| Audit completeness | 100% of decisions logged with inputs, model version, output, and reviewer action |
| Override mechanism | Reviewer can override within operational workflow without friction or penalty |
| Regulatory alignment | Compliance review confirms system meets current regulatory requirements |
| Observation period | Minimum 180 days in assist mode with satisfactory performance |

#### Graduation: Tightly Governed Recommend → Bounded Automate (narrow scope only)

| Condition | Specific Threshold |
|-----------|--------------------|
| Decision scope | Limited to clearly defined, low-complexity decisions (e.g., auto-approval of applications scoring above high-confidence threshold) |
| Auto-approval rate | Automated decisions cover ≤30% of total volume; remainder reviewed |
| Fairness monitoring | Real-time subgroup monitoring with automated alerts |
| Macro stability | No active stress indicators in relevant economic conditions |
| Regulatory approval | Explicit regulatory acknowledgment or sandbox authorization |
| Revert capability | Automatic revert to recommend if any fairness alert triggers |
| Evidence | Tier 1 evidence (regulator-backed) supporting the specific automation design |

#### Regression: Recommend → Assist

| Trigger | Threshold |
|---------|-----------|
| Fairness alert | Any protected subgroup adverse impact ratio exceeding regulatory threshold |
| Model drift | PSI (Population Stability Index) >0.25 on any key variable |
| Override disagreement | Reviewer override rate >15% sustained over 30 days |
| Macro stress | Relevant stress indicators (unemployment, default rates, volatility) exceed predefined thresholds |
| Regulatory action | Any regulatory inquiry, enforcement action, or guidance change affecting the system |

---

### 4.3 Healthcare

**Current default:** assist or tightly governed recommend (baseline), recommend (stress), assist (edge-case)

#### Graduation: Assist → Tightly Governed Recommend

| Condition | Specific Threshold |
|-----------|--------------------|
| Clinical validation | System performance validated against clinical gold standard in relevant patient population |
| Safety record | Zero patient safety incidents attributable to system recommendations over observation period |
| Clinician override | Override mechanism tested and functional; clinician can reject recommendation without workflow disruption |
| Subgroup safety | No material performance degradation across demographic or clinical subgroups |
| Regulatory status | Relevant regulatory clearance (e.g., FDA 510(k) or De Novo for US; CE marking for EU) |
| Workflow integration | System integrated into clinical workflow with appropriate alerts and documentation |
| Observation period | Minimum 180 days in assist mode; minimum patient volume threshold met |

#### Regression: Recommend → Assist

| Trigger | Threshold |
|---------|-----------|
| Safety event | Any patient safety event where system recommendation was a contributing factor |
| Performance degradation | Sensitivity or specificity drops below validated threshold |
| Population shift | Patient population characteristics diverge materially from validation population |
| Signal quality | Input data quality (e.g., lab values, imaging quality) falls below validated threshold |
| Clinician trust | Override rate >25% sustained over 30 days, indicating systematic disagreement |
| Regulatory change | New regulatory requirement or safety communication affecting the system |

---

### 4.4 Investment

**Current default:** assist or tightly governed recommend (baseline)

#### Graduation: Assist → Tightly Governed Recommend

| Condition | Specific Threshold |
|-----------|--------------------|
| Suitability validation | System recommendations consistent with client suitability profiles in ≥98% of evaluated cases |
| Disclosure completeness | All material limitations, conflicts, and assumptions disclosed to clients |
| Performance tracking | Recommendation performance tracked against benchmark over minimum 12-month period |
| Audit trail | 100% of advisory interactions logged with full decision chain |
| Volatility handling | System tested under historical stress scenarios without material suitability failures |
| Regulatory alignment | Compliance review confirms alignment with current investor protection regulations |

---

### 4.5 Strategy, Product, Marketing, Market Research

These domains have lower regulatory burden but still benefit from structured transition logic.

#### Strategy: Assist → Recommend (rare)

| Condition |
|-----------|
| Decision scope narrowed to bounded, measurable sub-problem (e.g., market sizing, competitive benchmarking) |
| AI output validated against expert judgment in at least 3 comparable prior decisions |
| Decision-maker retains explicit authority and accountability for final strategic choice |

#### Product: Assist → Recommend

| Condition |
|-----------|
| Clear proxy metrics with validated connection to business outcomes |
| A/B testing or experimentation framework operational |
| Minimum 90-day observation period with satisfactory recommendation quality |

#### Marketing: Recommend → Automate with Guardrails

| Condition |
|-----------|
| Optimization scope bounded (single channel or campaign type) |
| Privacy controls verified and tested |
| Performance feedback loop operational with ≤24-hour cycle |
| No material fairness or manipulation concerns in automated scope |
| Budget exposure limited to predefined threshold |

#### Market Research: Assist → Recommend (rare)

| Condition |
|-----------|
| Analyst review remains required for all synthesized findings |
| Source attribution and confidence scoring operational |
| No hallucination detected in validation sample |

---

## 5. Transition Governance Process

### 5.1 Escalation Process

```
Step 1: Identify candidate decision for escalation
Step 2: Verify all graduation criteria are met (documented evidence required)
Step 3: Review by governance committee (or designated authority)
Step 4: Define observation period and success metrics for new mode
Step 5: Deploy in new mode with enhanced monitoring
Step 6: At end of observation period, confirm or revert
```

**Critical rule:** No escalation without documented evidence that all graduation criteria are met. Capability improvement alone is never sufficient.

### 5.2 Regression Process

```
Step 1: Regression trigger detected (automated or manual)
Step 2: Authority reduced immediately (no waiting for committee review)
Step 3: Incident documented with trigger details
Step 4: Root cause investigation initiated
Step 5: Governance committee reviews within defined timeline
Step 6: Remediation plan or permanent regression decision
Step 7: Re-escalation requires fresh graduation evaluation
```

**Critical rule:** Regression is immediate upon trigger detection. Investigation happens after authority reduction, not before.

### 5.3 Review Cadence

| Review Type | Frequency | Scope |
|-------------|-----------|-------|
| Automated monitoring | Continuous | Performance, drift, fairness, exception rates |
| Operational review | Weekly | Active system status, recent triggers, override patterns |
| Governance review | Monthly | Authority levels, pending escalation requests, incident log |
| Strategic review | Quarterly | Domain-level authority assessment, evidence base update, capability reassessment |
| Framework review | Annually | Transition condition thresholds, new capability categories, structural changes |

---

## 6. New Capability Integration Protocol

When a new AI model or capability becomes available (e.g., new LLM release, new agentic framework), the following protocol applies:

```
Step 1: Classify the capability change
        - Incremental improvement (same task, better performance)
        - New task eligibility (previously ineligible task becomes feasible)
        - New modality (fundamentally different interaction pattern)

Step 2: For incremental improvements
        - Update capability indicators in monitoring system
        - Re-evaluate active graduation criteria
        - If criteria now met, initiate escalation process

Step 3: For new task eligibility
        - Classify the new task against existing taxonomy (domain, structure, risk, scenario)
        - Start at assist mode regardless of capability level
        - Apply standard graduation process

Step 4: For new modality (e.g., agentic AI replacing step-by-step workflow)
        - Flag for framework review
        - Do not apply existing transition conditions without adaptation
        - Design new transition conditions appropriate to the modality
        - This is the expected path for agentic AI systems
```

**Key insight from speed gap analysis:** The most disruptive capability changes are not incremental improvements but modality shifts. The framework must distinguish between these and respond differently. Incremental improvements flow through existing transition conditions. Modality shifts require transition condition redesign.

---

## 7. Interaction with Phase 16 Scoring Sheet

The Phase 16 scoring sheet (5 dimensions, 1-3 each, total 5-15) provides a static snapshot. Layer 2 transition conditions add a dynamic layer:

**Enhanced scoring protocol:**

1. Score using Phase 16 dimensions (decision structure, risk level, scenario stability, evidence strength, governance readiness) — this determines the **maximum allowable mode**
2. Check Layer 2 graduation criteria for the target mode — this determines whether the **transition is currently justified**
3. If scoring sheet allows recommend but graduation criteria are not met, remain at assist
4. If scoring sheet allows automate but graduation criteria are not met, remain at recommend

**The scoring sheet sets the ceiling. Graduation criteria determine the actual level.**

---

## 8. Limitations and Open Questions

1. **Threshold calibration:** Specific thresholds (e.g., 95% accuracy, 180-day observation) are illustrative starting points. Organizations must calibrate to their context.
2. **Measurement infrastructure:** Many graduation criteria require monitoring infrastructure that organizations may not have. Infrastructure readiness is itself a governance constraint.
3. **Agentic AI:** Current transition conditions assume discrete workflow stages with human checkpoints. Agentic AI systems that operate across multiple stages without discrete checkpoints require adapted transition conditions (flagged for future work).
4. **Cross-domain interactions:** Transition conditions are defined per domain. Decisions that span multiple domains (e.g., financial product marketed to consumers) require the most restrictive applicable conditions.
5. **Competitive pressure:** Organizations may face pressure to escalate authority faster than evidence supports. The framework explicitly rejects competitive pressure as a graduation criterion — a position aligned with the Anthropic RSP but contested by the OpenAI Preparedness Framework's competitive pressure clause.
