# Pilot Validation Protocol for the Reasoning Verification Framework

status: active
phase: 2.7
date: 2026-03-28
purpose: Design a rigorous validation plan to test whether the reasoning verification framework detects reasoning failures that existing approaches miss.

## Overview

The framework must be validated before organizational recommendation. Three validation approaches, each testing a different aspect:

1. **Retrospective**: Does the framework catch failures in documented incidents?
2. **Prospective**: Does the framework detect failures in live LLM outputs?
3. **Comparative**: Do practitioners perform better with the framework than without it?

---

## Validation 1: Retrospective — Against Incident Inventory

### Objective
Test whether the reasoning verification framework would have caught reasoning failures in the 71-incident inventory that the delegation framework alone did not.

### Case Selection
Focus on the 8 key LLM incidents where the delegation framework partially caught or missed the failure:

| Incident | Why Delegation Framework Was Insufficient | Expected Reasoning Verification Catch |
|---|---|---|
| Air Canada chatbot | Framework addresses system-level governance, not output-level policy accuracy | Source quality: AI cited non-existent policy. Normative: contradicted actual company rules. |
| Mata v. Avianca | Framework does not verify specific output content | Source quality: fabricated citations (A1). |
| AP Electric | Same pattern as Mata | Source quality: fabricated quotations (A1). |
| Google Bard demo | System was well-resourced; the specific output was wrong | Source quality: factual premise error. Confidence calibration: definitive claim on unverified fact. |
| CNET articles | System had editorial process; specific outputs had errors | Source quality + inferential validity on financial claims. |
| Chicago Sun-Times | Content generated at scale without verification | Source quality: hallucinated non-fiction content. |

(Samsung and DPD excluded: boundary/control failures, not reasoning failures.)

### Method
For each of the 6 applicable cases:
1. Reconstruct the AI output based on documented details (or generate a representative equivalent using current LLMs with similar prompts)
2. Apply the full verification protocol: source quality → inferential validity → normative acceptability → confidence calibration
3. Record which method caught the failure and at which step
4. Assess whether the framework would have prevented harm if applied before action

### Success Criteria
- The framework should catch all 6 cases that the delegation framework missed or only partially flagged
- Each catch should occur through a specific, documented verification step (not vague "this seems wrong")
- The framework should not require domain expertise beyond what was available to the original decision-maker

---

## Validation 2: Prospective — Against Live LLM Outputs

### Objective
Test the framework against fresh AI-generated business analyses where reasoning quality is unknown in advance.

### Task Design

Five business analysis tasks across domains where reasoning quality matters:

| Task | Domain | Why Selected |
|---|---|---|
| Marketing strategy analysis | Marketing | The BCG example domain; tests source quality assessment heavily |
| Competitive positioning analysis | Strategy | Tests inferential validity (analogical reasoning, generalization) |
| Credit risk evaluation | Finance | Tests normative assessment (regulatory compliance, professional standards) |
| Market sizing and projection | Research | Tests confidence calibration (quantitative claims, projection certainty) |
| Supply chain optimization | Operations | Tests scope mismatch (context-specific vs. generic recommendations) |

### Generation Protocol
For each task:
- Write a realistic business prompt (the kind a manager would actually ask)
- Generate analysis from 3 current LLMs (select based on availability; ensure diversity)
- Each output should be 1,000-3,000 words — long enough to contain substantive reasoning
- Do not prompt for specific errors; let natural LLM behavior produce whatever quality it produces

This yields 15 analysis outputs (5 tasks × 3 models).

### Evaluation Protocol
For each of the 15 outputs:

**Framework evaluation** (by the researcher):
1. Apply source quality assessment → record all findings
2. Apply inferential validity assessment → record all findings
3. Apply normative acceptability assessment → record all findings
4. Apply confidence calibration assessment → record all findings
5. Record total time spent per output
6. Classify each finding by failure type (from the taxonomy)

**Expert evaluation** (independent ground truth):
- Recruit one domain expert per task area (5 experts total)
- Each expert reviews the 3 outputs in their domain
- Expert identifies all reasoning issues they detect, using their own professional judgment
- Expert does not see the framework evaluation results

### Metrics

| Metric | Definition | Target |
|---|---|---|
| Detection rate | Framework-identified failures confirmed by expert / Total expert-identified failures | >70% |
| Precision | Framework-identified failures confirmed by expert / Total framework-identified failures | >80% |
| Coverage by type | Detection rate broken down by taxonomy category (A, B, C, D) | Identify which categories are strong vs. weak |
| Time per output | Average time to complete full verification protocol | <30 minutes |
| Cross-model variation | Do different LLMs produce systematically different failure patterns? | Descriptive (no target) |

### Analysis
- Calculate metrics overall and by task/domain
- Identify which failure types the framework detects well vs. poorly
- Identify which verification method (source, inferential, normative, confidence) contributes most to detection
- Compare failure rates across LLMs
- Document any failure types the expert caught that the framework missed entirely → these are framework gaps requiring revision

---

## Validation 3: Comparative — Framework vs. No Framework

### Objective
Test whether the framework improves reasoning evaluation quality compared to unaided human judgment.

### Design
Controlled comparison with two groups:

**Group A (Control)**: Business professionals evaluate AI outputs using their own judgment. No framework provided. Instruction: "Review this AI-generated analysis and identify any problems with the reasoning."

**Group B (Treatment)**: Same professionals, same outputs, but provided with the reasoning verification framework and a 15-minute orientation on how to use it.

### Materials
- 10 AI-generated business analyses, each containing 2-4 planted reasoning failures at known locations and severity levels
- Failures should span all four taxonomy categories (source, inferential, normative, structural)
- Include 2 outputs with no significant failures (to measure false positive rates)
- Each output: 800-1,500 words

### Participants
- Minimum 20 per group (40 total)
- Matched for professional experience level and domain background
- Mix of: junior analysts, mid-level managers, senior managers
- Recruited from organizations currently using LLMs for business analysis

### Measurement

| Metric | Definition |
|---|---|
| Detection rate | Planted failures identified / Total planted failures |
| False positive rate | Non-failures flagged as failures / Total non-failures |
| Detection by category | Detection rate for source (A) vs. inferential (B) vs. normative (C) vs. structural (D) failures |
| Detection by experience | Detection rate by participant seniority level |
| Time spent | Average evaluation time per output |
| Confidence | Self-reported confidence in evaluation (1-5 scale) |

### Hypotheses
1. Group B (framework) will detect significantly more failures than Group A (no framework)
2. The improvement will be largest for source quality (Category A) and normative (Category C) failures, where structured checklists compensate most for lack of training
3. The improvement will be smallest for structural failures (Category D), which require judgment that checklists alone may not provide
4. Group B will take more time per output but will have higher confidence in their assessments
5. The framework will particularly benefit junior analysts, narrowing the gap with senior managers

### Success Criteria
- Group B detection rate is statistically significantly higher than Group A (p < 0.05)
- Group B false positive rate is not significantly higher than Group A (framework should improve detection without generating excessive noise)
- Framework is usable: average time per output does not exceed 30 minutes

---

## Pilot Timeline

| Phase | Duration | Deliverable |
|---|---|---|
| Phase A: Retrospective | 2 weeks | Incident reanalysis report; framework refinements |
| Phase B: Prospective | 3 weeks | 15 LLM outputs evaluated; expert comparison; detection metrics |
| Phase C: Comparative | 4 weeks | Participant recruitment, evaluation sessions, statistical analysis |
| Synthesis | 1 week | Validation summary with framework revisions and readiness assessment |

Total: approximately 10 weeks from initiation.

## Expected Outcomes

1. Validated detection rates for each reasoning failure type
2. Identified framework strengths (failure types it catches reliably) and weaknesses (types it misses)
3. Refined protocol incorporating lessons from all three validation phases
4. Usability data supporting (or questioning) the 30-minute-per-output target
5. Evidence base for recommending the framework to organizations
6. Comparison data showing the value-add of structured verification over unaided judgment
