# Workflow Authority and Trust-Calibration Matrix

status: draft
date: 2026-03-25
purpose: translate the business-context alignment framework into a workflow-level decision aid

## Why This Note Exists

The repository already distinguishes between assist, recommend, and automate-with-guardrails.

This note extends that logic to common workflow roles that appear across many business settings, especially with LLM systems.

The goal is not to produce a universal rule.

The goal is to make practical authority visible and to show where stronger validation, grounding, or fallback logic is required.

## Reading Rule

This matrix should be used conservatively.

- If a role is high-stakes, policy-facing, or difficult to validate independently, keep authority lower.
- If the workflow cannot support real review, reduce authority even if the model appears capable.
- If the organization cannot explain who owns escalation and override, the system is not governance-ready for higher authority.

## Matrix

| Workflow role | Typical practical authority | Default AI mode | Conditions for higher authority | Fallback triggers | Main alignment priority | Evidence strength |
| --- | --- | --- | --- | --- | --- | --- |
| Information summarization | shapes what the user sees first | assist | stable source set, easy source checking, low downstream stakes | unverifiable summary, omitted source context, ambiguous source quality | validation alignment | moderate to strong |
| Problem framing | defines what the organization thinks the issue is | assist | bounded scope, strong human review, low immediate action pressure | narrowing of options too early, hidden assumptions, persuasive reframing | problem alignment | moderate |
| Option generation | expands candidate actions | assist | diverse option generation with structured review and explicit criteria | hallucinated options, duplicated ideas presented as breadth, premature convergence | authority alignment | moderate |
| Ranking or screening | changes which cases receive attention first | assist or tightly governed recommend | measurable criteria, fairness checks, auditable thresholds, independent review | subgroup anomaly, unclear criteria, subjective evaluation pressure | trust alignment | strong in high-stakes domains |
| Recommendation | suggests what should be done | recommend | validated workflow, explicit accountability, clear override rules, domain-specific evidence | drift, instability, unexplained recommendation shifts, weak audit trail | authority alignment | strong for governance logic |
| Approval support | influences human sign-off and exception handling | assist | separation between recommendation and final review, structured checklist, independent evidence | reviewer overload, same-interface validation, persuasive rationale effects | validation alignment | strong |
| External communication | speaks to customers, applicants, vendors, or regulators | assist or tightly governed recommend | grounded sources, narrow scope, clear refusal behavior, monitored templates | policy improvisation, customer commitment risk, outdated knowledge base | policy and knowledge alignment | strong |
| Policy or compliance guidance | represents internal rules or legal/compliance constraints | assist | approved source grounding, strict retrieval boundaries, escalation to humans for ambiguity | conflicting policy sources, missing rule coverage, uncertainty in interpretation | policy and knowledge alignment | strong |
| Action triggering | starts a workflow, ticket, decision path, or transaction | recommend or bounded automate-with-guardrails | low reversibility cost, strong monitoring, clear rollback path, event logging | false positives, exception growth, failed rollback, unclear ownership | authority plus commercial alignment | moderate to strong |
| Autonomous execution | executes decisions or actions with limited review | automate with guardrails only in narrow settings | repeated environment, stable data, bounded objectives, real-time monitoring, rollback, low rights sensitivity | degraded telemetry, changing conditions, rights-sensitive edge cases, policy drift | authority plus fallback design | strong only in low-risk structured settings |

## Interpretation

### 1. Practical authority is often higher than formal authority

If AI sets the first frame, ranks the queue, or produces the rationale that humans see before anything else, its practical authority may already be high even without explicit automation.

### 2. Review architecture matters as much as nominal mode

An "assist" system can still be dangerous if the human review is weak, overloaded, or contaminated by the same conversational interface that generated the output.

### 3. External communication roles deserve the most conservative treatment

Policy-facing, customer-facing, and compliance-facing uses create a special risk because fluent language can be mistaken for an authorized company position.

### 4. Action-triggering roles are often misclassified

Many firms treat workflow triggers as low-risk support, but a trigger can create de facto decisions by moving cases, notifying customers, or changing queues before a human notices.

## Practical Rules

1. If the AI changes what the human notices first, treat the role as higher-authority than ordinary assistance.
2. If the AI speaks for the firm, default to grounded assist rather than open-ended recommendation.
3. If the role affects ranking, screening, or approval, require structured review rather than conversational validation.
4. If rollback is weak or delayed, do not increase authority.
5. If evidence is weak or the task is jagged, prefer calibrated recommendation over automation.

## Sources

- `research/delivery/output/thinktank-report.md`
- `research/operations/revision/governance-memo.md`
- `research/extensions/business-alignment/alignment-framework.md`
- `research/extensions/business-alignment/incidents/implications-and-immediate-company-needs.md`
- Vaccaro, Michelle, Abdullah Almaatouq, and Thomas Malone. Nature Human Behaviour (2024). https://www.nature.com/articles/s41562-024-02024-1
- Agarwal, Nikhil, Alex Moehring, and Alexander Wolitzky. NBER Working Paper 33949 (2025). https://www.nber.org/papers/w33949
- Gans, Joshua. NBER Working Paper 34712 (2026). https://www.nber.org/papers/w34712
