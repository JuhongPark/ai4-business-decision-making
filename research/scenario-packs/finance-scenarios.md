# Finance Scenario Pack

status: completed
domain: finance
dataset_anchor: HMDA plus Federal Reserve stress test scenarios
recommended_default_mode: assist or tightly governed recommend

## Scenario F1

scenario_id: F1
scenario_class: baseline
ai_role_focus: underwriting support

### Business Context

A lender must review credit applications efficiently while managing approval quality and fairness exposure.

### Triggering Condition

Baseline macro conditions with stable approval volumes.

### Decision Required

How should the institution use AI in underwriting and risk classification?

### Available Data

- applicant attributes
- loan characteristics
- historical approval patterns
- repayment and risk signals

### Mode Comparison

- `human-only`: slower, less scalable, and potentially less consistent
- `AI assist`: strong support for screening and prioritization
- `AI recommend`: plausible if the decision path is reviewable and auditable
- `AI automate with guardrails`: too aggressive for consequential lending decisions without unusually strong controls

### Preferred Mode

assist or tightly governed recommend

### Why

Even under baseline conditions, lending decisions affect access and fairness. Human accountability should remain explicit.

## Scenario F2

scenario_id: F2
scenario_class: stress
ai_role_focus: lending under macro deterioration

### Business Context

The lender faces adverse macro conditions such as unemployment growth, higher default risk, and tighter capital pressure.

### Triggering Condition

Stress-test style downturn scenario.

### Decision Required

Should AI recommendations be trusted more, less, or differently under deteriorating conditions?

### Available Data

- baseline loan and approval data
- macro scenario variables
- stress-adjusted delinquency assumptions

### Mode Comparison

- `human-only`: may become inconsistent under pressure
- `AI assist`: useful for scenario sensitivity analysis
- `AI recommend`: useful if model uncertainty and fairness monitoring are visible
- `AI automate with guardrails`: not preferred because adverse conditions magnify model-risk and fairness concerns

### Preferred Mode

assist

### Why

Stress conditions increase the cost of hidden model error. Human judgment and explicit governance become more important, not less.

## Scenario F3

scenario_id: F3
scenario_class: edge_case
ai_role_focus: fairness-sensitive outlier decision

### Business Context

The institution faces an outlier application pattern or model drift signal that raises explainability concerns.

### Triggering Condition

Unexpected subgroup impact, policy shift, or model change affecting credit recommendations.

### Decision Required

Should the institution continue using AI recommendations for approval and pricing decisions?

### Available Data

- subgroup approval patterns
- drift indicators
- monitoring and audit outputs

### Mode Comparison

- `human-only`: stronger for cautious review and hold decisions
- `AI assist`: useful for surfacing anomalies
- `AI recommend`: too risky if fairness concerns are unresolved
- `AI automate with guardrails`: inappropriate

### Preferred Mode

assist

### Why

If fairness or drift concerns appear, the institution should restrict autonomy until the evidence base and control logic are revalidated.

## Domain Takeaway

Finance may benefit heavily from AI, but the preferred mode rarely moves beyond tightly governed recommend. Under stress or fairness uncertainty, the system should revert toward assist.
