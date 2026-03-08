# Phase 4: Cross-Case Comparison

status: completed
phase_goal: Compare AI use cases across two high-stakes domains and one lower-risk domain to identify when firms should assist, recommend, or restrict automation.

## Cases Included

1. Upstart AI lending and credit underwriting
2. Amazon experimental AI recruiting tool
3. UPS ORION route optimization

## Comparison Table

| Case | Function | Risk Level | Decision Structure | Evidence Tier Mix | Main Value Claim | Main Risk | Default Mode | Overall Lesson |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Upstart | Finance | high | high-impact, regulated, model-based | Tier 1 + Tier 2 | more efficient underwriting and broader credit evaluation | fairness, compliance, model change risk | recommend | high-stakes value claims require governance and regulator-visible controls |
| Amazon hiring | Human resources | high | partially structured but socially sensitive | Tier 3 dominant | faster screening at scale | bias, legitimacy loss, weak trust | assist or restrict | weak evidence and high stakes justify strong caution and limited automation |
| UPS ORION | Operations | lower | structured, repeated, optimization-driven | Tier 2 dominant | route efficiency and service improvement | data brittleness and exception handling | automate with guardrails | lower-risk operational domains are better candidates for controlled automation |

## Cross-Case Findings

### Finding 1: Lower-risk operational domains are the strongest candidates for automation

UPS shows that AI is easiest to justify when decisions are repeated, measurable, and operationally constrained. In these environments, automate-with-guardrails is more defensible than in sensitive people or credit decisions.

### Finding 2: High-stakes decisions require a default bias toward assist or tightly governed recommend

Upstart and the Reuters-reported Amazon hiring case show that when decisions affect fairness, opportunity, or compliance, predictive capability alone is insufficient. Human review, accountability, and evidence quality become threshold conditions.

### Finding 3: The same capability can create value or failure depending on context design

Prediction, ranking, and optimization are not inherently beneficial. Their effect depends on training data, objective choice, workflow integration, and the ability of humans to intervene appropriately.

### Finding 4: Evidence quality should shape how strongly each case is interpreted

Upstart can support stronger claims because it includes regulator-backed material. UPS is informative mainly for design logic and company-reported outcomes. Amazon is best used as a warning example rather than a fully verified internal record.

## Evidence Quality Note

The cases are intentionally not treated as equal. Upstart includes regulator-backed documentation, UPS relies mainly on company-reported materials, and the Amazon hiring case is based on reported investigative coverage rather than direct company disclosure.

## Implications for Phase 5

The analytical framework should evaluate AI adoption using at least the following dimensions:

1. Decision structure
2. Data quality
3. Stakes and external impact
4. Degree of model autonomy
5. Human oversight design
6. Governance and accountability requirement
7. Evidence strength behind adoption claims
