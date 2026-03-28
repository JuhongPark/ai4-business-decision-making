# Scoring System Integration: Reasoning Verification in the Delegation Framework

status: active
phase: 2.6
date: 2026-03-28
purpose: Define how reasoning verification integrates into the existing 6-dimensional delegation scoring system.

## Current System

The delegation framework uses a 5-dimension scoring sheet:

| Dimension | 1 (Unfavorable) | 2 (Mixed) | 3 (Favorable) |
|---|---|---|---|
| Decision structure | Unstructured | Semi-structured | Structured |
| Risk level | High | Medium | Low |
| Scenario stability | Edge-case | Stress | Baseline |
| Evidence strength | Weak | Moderate | Strong |
| Governance readiness | Weak | Partial | Strong |

Score range: 5-15. Authority bands: 5-8 (assist), 9-11 (assist/recommend), 12-13 (recommend), 14-15 (recommend/automate with guardrails).

Three override rules:
1. High-risk + weak governance → cap at ASSIST
2. Edge-case scenario → cap at ASSIST
3. Weak evidence in consequential decision → reduce one level

## The Gap

Evidence strength currently measures institutional credibility of the AI system:
- Strong (3): regulator-backed, audited, or peer-reviewed
- Moderate (2): official company or technical documentation
- Weak (1): reported or secondary evidence without direct primary confirmation

This measures whether the AI system has been validated, not whether a specific output's reasoning is sound. An AI system can score "strong" on evidence strength (because it is FDA-approved) while producing a specific output with flawed reasoning. The framework has no mechanism for instance-level reasoning assessment.

## Integration Design

Two complementary mechanisms address two different questions:

### Mechanism 1: Extend Evidence Strength (Systemic Assessment)

Revise evidence strength into a two-component dimension:

**Component A — System-Level Evidence (existing, unchanged)**
- Strong (3): regulator-backed, audited, or peer-reviewed
- Moderate (2): official company or technical documentation
- Weak (1): reported or secondary evidence

**Component B — Reasoning Output Quality (new)**
- Strong (3): Output passes all four verification checks (source quality adequate, inferential validity confirmed, normative acceptability cleared, confidence well-calibrated)
- Moderate (2): Output passes source quality and inferential validity checks; minor issues in normative or calibration dimensions
- Weak (1): Output fails one or more checks at the source quality or inferential validity level

**Combined score = minimum of Component A and Component B** (weakest-link principle).

Rationale: A well-validated system (Component A = 3) that produces flawed reasoning on a specific output (Component B = 1) should not receive a strong evidence score for that decision. Conversely, a weakly validated system that happens to produce good reasoning on one output should not receive unwarranted confidence.

The weakest-link principle ensures that neither systemic validation nor instance-level quality alone can mask a deficiency in the other.

### Mechanism 2: Reasoning Verification Gate (Instance Assessment)

Before applying the scoring sheet to a specific decision, a prerequisite gate:

| Gate Status | Condition | Effect |
|---|---|---|
| **Not verified** | No reasoning verification applied to this specific output | Default to ASSIST regardless of framework score |
| **Verified with issues** | Verification applied; one or more issues identified at moderate severity | Framework score applies with one-level reduction |
| **Verified and passed** | Verification applied; all checks passed or issues at low severity only | Framework score applies normally |

This gate addresses the alignment literature bridge's Gap #2: the framework previously had no instance-level guidance. The gate provides it.

## Integration with Override Rules

The existing three override rules continue to function. The reasoning verification adds reinforcement:

| Override Rule | Current Trigger | Additional Reinforcement |
|---|---|---|
| Rule 1: High-risk + weak governance → ASSIST | Unchanged | If reasoning verification also shows weak output quality, this confirms the ASSIST cap |
| Rule 2: Edge-case → ASSIST | Unchanged | Edge-case reasoning is precisely where LLMs are least reliable; verification gate provides additional protection |
| Rule 3: Weak evidence → reduce one level | Now triggered by either system-level OR output-level weakness | Extended evidence strength (weakest-link) means a specific output with bad reasoning triggers this rule even when the system is well-validated |

New effective override: **Unverified output in consequential decision → ASSIST**. This is the gate mechanism. It operationalizes the finding that nominal human oversight without actual verification is functionally equivalent to no oversight.

## Integration with Alignment Layers

| Layer | Previous Gap | How Reasoning Verification Fills It |
|---|---|---|
| Layer 3: Trust alignment | Identified that users should rely on AI "for the right reasons" but provided no method | The four verification methods (source, inferential, normative, confidence) ARE the method for determining whether reliance is justified |
| Layer 4: Validation alignment | Identified the rubber-stamp problem but had no remedy | The verification gate converts symbolic review into substantive review. A "verified and passed" gate status requires documented application of the protocol. |

## Worked Scoring Example

**Scenario**: Financial risk assessment for a lending decision (high-stakes).

### Without reasoning verification:

| Dimension | Score |
|---|---|
| Decision structure: Semi-structured | 2 |
| Risk level: High | 1 |
| Scenario stability: Baseline | 3 |
| Evidence strength: System is regulator-reviewed → Moderate | 2 |
| Governance readiness: Strong | 3 |
| **Total** | **11** |

Authority band: 9-11 → Assist or Recommend.
No override triggered (governance is strong, evidence is moderate).
Result: **Recommend** is permitted.

### With reasoning verification:

Same scores for structure, risk, scenario, governance.

Evidence strength — Component A (system): Moderate (2).
Evidence strength — Component B (output): AI output cites industry average default rates but uses them to justify a specific loan approval without accounting for the applicant's unique risk factors (inferential failure B5: scope mismatch). Source quality check reveals the default rate data is 18 months old (A5: temporal decay). → Weak (1).

Combined evidence strength: min(2, 1) = **Weak (1)**.

| Dimension | Score |
|---|---|
| Decision structure: Semi-structured | 2 |
| Risk level: High | 1 |
| Scenario stability: Baseline | 3 |
| Evidence strength: Weak (output quality limited) | 1 |
| Governance readiness: Strong | 3 |
| **Total** | **10** |

Authority band: 9-11 → Assist or Recommend.
But override rule 3 triggered: weak evidence in consequential decision → reduce one level.
Result: **Assist only**.

The same decision, with the same AI system, scored differently because reasoning verification revealed that the specific output did not meet the quality standard. The framework now captures what it previously could not: an organizationally sound deployment producing a specific output that should not be trusted at the recommended authority level.
