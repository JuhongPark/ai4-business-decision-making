# Practitioner Validation Study Protocol

status: ready for IRB/ethics review
date_created: 2026-04-11

## Study Design

**Type**: Within-subjects controlled experiment
**Participants**: 20-30 business practitioners (product managers, marketing directors, business analysts)
**Inclusion criteria**: 2+ years in business role using AI tools; no formal market research training
**Duration**: 2-hour session per participant

## Conditions

Each participant evaluates 12 AI-generated market research outputs (4 per condition, counterbalanced):

| Condition | Tool | Description |
| --- | --- | --- |
| A: Unassisted | None | Read output, assess quality, make decision |
| B: Verification suite | Prototype 2 | Source quality + calibration + sycophancy reports provided |
| C: Full workflow | Prototype 4 | Complete workflow system with countermeasures active |

## Materials

### AI Market Research Outputs (12 total)

6 outputs with planted reasoning failures (2 per category):
- 2 with source quality failures (vendor blog as quantitative evidence, fabricated survey)
- 2 with calibration failures (precise estimates from uncertain data, no ranges)
- 2 with sycophantic failures (hypothesis confirmation, no alternatives, no counter-evidence)

6 outputs with sound reasoning:
- Professional-grade sources, calibrated confidence, balanced analysis
- Include counter-evidence, multiple alternatives, appropriate uncertainty

All outputs formatted identically to eliminate surface-quality cues.

### Measurement Instruments

**Detection accuracy** (per output):
- "Does this analysis contain significant reasoning problems?" (Yes/No)
- If Yes: "Describe the problem you identified" (free text, coded against taxonomy)
- Scored as: correct detection, missed failure, false alarm

**Decision quality** (per output):
- "Based on this analysis, would you recommend proceeding with this product concept?" (Yes/No/Need more info)
- Coded against: ground truth (flawed outputs should elicit No or Need more info)

**Confidence** (per output):
- "How confident are you in your assessment?" (1-7 Likert)

**Time** (per output):
- Measured from output presentation to final response

**Post-session questionnaire**:
- "Which condition helped you most in evaluating the outputs?" (A/B/C)
- "Would you use this tool in your daily work?" (1-7 Likert)
- "What would need to change for you to use this tool regularly?" (free text)
- System Usability Scale (SUS) for Conditions B and C

## Procedure

1. **Briefing** (10 min): Explain the study. No information about failure types or detection rates.
2. **Practice** (10 min): One practice output per condition (not scored).
3. **Condition A** (20 min): 4 outputs, unassisted evaluation.
4. **Condition B** (30 min): 4 outputs with verification suite reports.
5. **Condition C** (35 min): 4 outputs with full workflow system.
6. **Questionnaire** (15 min): Post-session survey.

Order of conditions is fixed (A→B→C) to simulate the learning curve. Output assignment to conditions is counterbalanced across participants using a Latin square design.

## Analysis Plan

### Primary analysis
- Detection rate by condition: McNemar's test for paired proportions
- Expected: A (25%) < B (55%) < C (75%)

### Secondary analyses
- False alarm rate by condition
- Decision quality by condition (% correct go/no-go decisions)
- Time by condition (median minutes per output)
- Confidence calibration: correlation between participant confidence and actual accuracy

### Effect size targets
- Detection rate improvement B vs A: Cohen's h ≥ 0.5 (medium effect)
- Detection rate improvement C vs A: Cohen's h ≥ 0.8 (large effect)

### Sample size justification
- For McNemar's test with medium effect (h=0.5), alpha=0.05, power=0.80: n=26
- Target: 30 participants (allowing for 15% attrition)

## Ethical Considerations

- Participants are evaluating AI outputs, not being evaluated themselves
- No deception: participants know some outputs may contain failures
- Compensation: appropriate for 2-hour commitment
- Data: anonymized, no personally identifiable information retained
- Consent: written informed consent before participation
