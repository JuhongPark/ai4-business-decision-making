# Healthcare Scenario Pack

status: completed
domain: healthcare
dataset_anchor: MIMIC-IV plus FDA governance context
recommended_default_mode: assist or tightly governed recommend

## Scenario H1

scenario_id: H1
scenario_class: baseline
ai_role_focus: clinical support in routine triage

### Business Context

A hospital uses AI-supported triage and deterioration-risk tools to support clinical workflow.

### Triggering Condition

Routine patient intake with normal staffing and manageable patient load.

### Decision Required

How much authority should AI have in prioritizing patient review and triage escalation?

### Available Data

- vital signs
- encounter timing
- prior patient history
- early deterioration indicators

### Mode Comparison

- `human-only`: slower and more variable under volume pressure
- `AI assist`: strong support for signal detection
- `AI recommend`: plausible if clinicians retain final authority
- `AI automate with guardrails`: too risky for broad use in patient-priority decisions

### Preferred Mode

assist or tightly governed recommend

### Why

Routine support can be valuable, but clinical responsibility and safety burden remain human-centered.

## Scenario H2

scenario_id: H2
scenario_class: stress
ai_role_focus: triage during surge

### Business Context

The hospital faces high patient inflow and limited clinician capacity.

### Triggering Condition

High-acuity surge with elevated workload and compressed decision time.

### Decision Required

Should AI take a stronger role in prioritization under time pressure?

### Available Data

- live triage signals
- patient queue
- staffing constraints
- acuity indicators

### Mode Comparison

- `human-only`: vulnerable to overload and inconsistency
- `AI assist`: useful for triage support and alert prioritization
- `AI recommend`: useful if clinicians can rapidly review suggestions
- `AI automate with guardrails`: still too risky because false negatives and opaque escalation logic can create patient harm

### Preferred Mode

recommend

### Why

Under surge, stronger recommendation support may be justified, but clinical override must remain available and expected.

## Scenario H3

scenario_id: H3
scenario_class: edge_case
ai_role_focus: uncertainty and incomplete information

### Business Context

The system encounters an atypical patient presentation with weak signal quality and limited historical similarity.

### Triggering Condition

Incomplete information, unusual presentation, or out-of-distribution case.

### Decision Required

Should clinicians continue to rely on AI guidance?

### Available Data

- incomplete patient history
- uncertain signal quality
- non-standard feature combinations

### Mode Comparison

- `human-only`: best for contextual and cautious judgment
- `AI assist`: useful only as one weak signal among many
- `AI recommend`: risky because uncertainty may not be well represented
- `AI automate with guardrails`: inappropriate

### Preferred Mode

assist

### Why

Safety-critical edge cases require humility, transparency, and clinician-led judgment.

## Domain Takeaway

Healthcare is a classic governance-first domain. AI can materially improve support quality, but the preferred mode remains assist or tightly governed recommend, especially when safety risk rises.
