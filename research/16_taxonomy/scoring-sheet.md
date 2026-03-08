# Phase 16: Scoring Sheet

status: completed
purpose: Provide a lightweight scoring model for selecting AI authority.

## Scoring Dimensions

Score each dimension from 1 to 3.

### Decision Structure

- 1: unstructured
- 2: semi-structured
- 3: structured

### Risk Level

- 1: high-risk
- 2: medium-risk
- 3: low-risk

### Scenario Stability

- 1: edge-case
- 2: stress
- 3: baseline

### Evidence Strength

- 1: weak
- 2: moderate
- 3: strong

### Governance Readiness

- 1: weak
- 2: partial
- 3: strong

## Interpretation

### Total Score 5-8

preferred_mode: assist
reason: uncertainty, risk, weak evidence, or weak governance makes higher autonomy inappropriate

### Total Score 9-11

preferred_mode: assist or recommend
reason: partial structure or moderate confidence justifies support, but not broad automation

### Total Score 12-13

preferred_mode: recommend
reason: the environment can support stronger AI authority, but human approval should remain visible

### Total Score 14-15

preferred_mode: recommend or automate with guardrails
reason: the environment is structured, stable, lower-risk, evidence-backed, and governance-ready

## Override Rules

- any high-risk domain with weak governance: do not exceed `assist`
- any edge-case scenario: do not exceed `assist`
- any weak evidence base in a consequential decision: reduce one autonomy level
