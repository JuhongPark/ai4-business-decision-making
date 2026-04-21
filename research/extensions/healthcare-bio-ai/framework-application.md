# Framework Application to Healthcare and Bio AI Sub-Domains

status: draft
date: 2026-04-21
purpose: Apply the repo's 6-dimensional delegation framework and 5-discipline reasoning verification (RVCS-1) to each of the nine healthcare/bio AI sub-domains defined in `sub-domain-taxonomy.md`. Record where the framework produces actionable guidance, where it produces coarse guidance that the sub-domain can tolerate, and where it breaks structurally.

This document is the analytic core of the healthcare-bio-ai track. It uses:

- **6-dim delegation framework** from `research/core/taxonomy/category-system.md`: domain × decision structure × risk level × scenario condition × evidence strength × governance readiness, each 1-3, summed 5-15, mapped to ASSIST / RECOMMEND / AUTOMATE bands with three override rules.
- **5-discipline RVCS-1 coding** from the scale-based track and `research/core/framework/reasoning-failure-taxonomy.md`: Q1 source quality, Q2 inferential validity, Q3 normative acceptability, Q4 confidence calibration, Q5 failure mode awareness, each 0-3, summed 0-15.
- **Regulatory perimeter map** from `regulatory-landscape.md` §3 for scoring governance readiness.
- **Incident evidence** from `incident-inventory.md` for testing framework outputs against documented failures.

---

## 1. Scoring convention

For each sub-domain this document records two scores and two analyses.

**Delegation scoring (6 dims, 1-3 each)**:
- Decision structure: 1=unstructured, 2=semi-structured, 3=structured
- Risk level: 1=high (safety/fairness/compliance), 2=medium (revenue/customer), 3=low (operational)
- Scenario condition: 1=edge-case, 2=stress, 3=baseline
- Evidence strength: 1=weak, 2=moderate, 3=strong
- Governance readiness: 1=weak, 2=adequate, 3=strong
- Domain fixed: healthcare = 1 (safety-critical default) — overrideable when sub-domain does not touch patient safety (HC3 operational, HC4 pre-patient, HC9 documentation)

Authority bands: 5-8 ASSIST; 9-11 ASSIST or RECOMMEND; 12-15 RECOMMEND or AUTOMATE WITH GUARDRAILS.

Override rules:
- High risk + weak governance → cap at ASSIST
- Edge-case scenario → cap at ASSIST
- Weak evidence in consequential decision → reduce one level

**RVCS-1 scoring** is applied to a representative "substantive" configuration (best-resourced deployment) and "typical" configuration (modal deployment) to reproduce the scale-based track's S4 substantive / S4 typical distinction within each sub-domain.

The scoring here is indicative and documentary-evidence-grounded; it is not the product of primary empirical coding.

---

## 2. HC1 — Diagnostic imaging and pathology AI

### Delegation scoring

| Dimension | Score | Justification |
|---|---|---|
| Domain (safety prior) | 1 | Patient safety downstream |
| Decision structure | 2 | Semi-structured (image → finding with clinical context) |
| Risk level | 1 | High (diagnostic error → harm) |
| Scenario condition | 2 | Baseline or stress (surge); edge-cases exist (rare findings) |
| Evidence strength | 2 | Moderate; FDA clearance data exists but often retrospective |
| Governance readiness | 3 | Strong — dense SaMD regulation (R1, R3, R5, R6, R7) |
| **Sum** | **11** | ASSIST or RECOMMEND band |

Baseline score 11 places HC1 at the top of the ASSIST-or-RECOMMEND band. No override triggers (risk high but governance strong; scenario is baseline or stress, not edge-case; evidence is moderate not weak). RECOMMEND is justifiable where post-market performance monitoring is operational.

### RVCS-1 scoring

**Substantive configuration** (academic medical centre with imaging AI and double-read workflow):

| Discipline | Score / 3 | Notes |
|---|---|---|
| Q1 Source quality | 3 | FDA-cleared device, peer-reviewed validation, known training distribution |
| Q2 Inferential validity | 2 | Reader evaluates; occasional blind-read studies |
| Q3 Normative acceptability | 3 | Within standard practice of care |
| Q4 Confidence calibration | 2 | Vendor-published AUC; less site-specific base rates |
| Q5 Failure mode awareness | 2 | Known shortcuts (Zech hospital-signature case) in literature |
| **Total** | **12 / 15** | Substantive |

**Typical configuration** (community hospital reading AI-flagged studies, solo reader):

| Discipline | Score / 3 | Notes |
|---|---|---|
| Q1 Source quality | 2 | Vendor materials only; no site validation |
| Q2 Inferential validity | 1 | Single reader, time-pressured |
| Q3 Normative acceptability | 3 | Standard practice |
| Q4 Confidence calibration | 1 | No site-specific base rates |
| Q5 Failure mode awareness | 1 | Not universally taught |
| **Total** | **8 / 15** | Typical |

### Framework fit
HC1 is the cleanest fit. Framework outputs match clinical practice norms. Substantive vs typical gap (12 vs 8) maps precisely to the scale-based track's S4 substantive / S4 typical cliff.

### Incident evidence
HBI-04 (Roberts COVID-imaging review), HBI-05 (Zech pneumonia), HBI-07 (Daneshjou dermatology) all manifest at the typical configuration end of Q1, Q4, Q5 scores. No incident evidence supports raising HC1 to AUTOMATE WITH GUARDRAILS; the external-validation failure pattern caps authority at RECOMMEND.

---

## 3. HC2 — Clinical decision support and deterioration prediction

### Delegation scoring

| Dimension | Score | Justification |
|---|---|---|
| Domain (safety prior) | 1 | Patient safety immediate |
| Decision structure | 2 | Semi-structured |
| Risk level | 1 | High |
| Scenario condition | 2 | Baseline; surge increases error rate |
| Evidence strength | 1 | Weak — many deployed CDS tools lack independent validation (HBI-01 Epic Sepsis Model is the archetype) |
| Governance readiness | 2 | Adequate under CDS carve-out; contested regulatory perimeter |
| **Sum** | **9** | ASSIST or RECOMMEND band; weak-evidence override → ASSIST |

Weak-evidence override reduces HC2 by one level: **ASSIST is the framework-mandated default** for CDS deployed without independent validation.

### RVCS-1 scoring

**Substantive configuration** (AMC with AI assurance team evaluating CDS before deployment and monitoring drift):
Q1=3, Q2=2, Q3=3, Q4=2, Q5=2 → 12 / 15

**Typical configuration** (community hospital deploying vendor CDS with vendor-supplied validation materials):
Q1=1, Q2=1, Q3=3, Q4=1, Q5=1 → 7 / 15

### Framework fit
Framework works but the weak-evidence override is load-bearing. The Epic Sepsis Model case (HBI-01) is the canonical framework test: the core scoring without the override would have landed at RECOMMEND; with the override it lands at ASSIST, matching the retrospective judgment of Wong et al.

### Incident evidence
HBI-01 (Epic Sepsis Model), HBI-02 (Epic Deterioration Index), HBI-03 (IBM Watson for Oncology), HBI-08 (pulse oximeter bias), HBI-26 (GPT-4 clinical vignettes bias). Every one of these lines up with the "weak-evidence override → ASSIST" prescription.

### Framework adaptation recommended
The core framework's CDS scoring would benefit from explicitly labelling the CDS carve-out as a governance-readiness factor. "Operates under CDS carve-out + vendor-embedded + no site validation" should automatically set governance readiness = 1 (weak) rather than requiring the scorer to infer it.

---

## 4. HC3 — Hospital operations AI

### Delegation scoring

| Dimension | Score | Justification |
|---|---|---|
| Domain (safety prior) | 2 (relaxed) | Operations; downstream effects possible but mediated |
| Decision structure | 3 | Structured (scheduling, staffing, bed management) |
| Risk level | 3 | Low for pure ops; 2 when routed back to clinical care (readmission-driven discharge) |
| Scenario condition | 3 | Baseline |
| Evidence strength | 2 | Moderate — operational metrics are measurable |
| Governance readiness | 2 | Adequate — operational regs (CoP, HIPAA) cover but AI-specific rules limited |
| **Sum** | **14** | RECOMMEND or AUTOMATE band |

**But**: the Obermeyer racial-bias case (HBI-06) shows HC3's operational decisions (risk stratification for extra care) can mask HC1/HC2 clinical and fairness risks. When the operational decision routes back to clinical care or patient allocation, risk_level should be re-evaluated as 1-2 (high or medium) and scenario condition as 2 (stress), reducing score by 2-3 and landing in ASSIST-or-RECOMMEND.

### RVCS-1 scoring

**Substantive configuration** (large health system with ops-AI governance and bias audits):
Q1=3, Q2=2, Q3=2, Q4=2, Q5=2 → 11 / 15

**Typical configuration** (community hospital deploying vendor readmission model without bias audit):
Q1=2, Q2=1, Q3=1, Q4=1, Q5=1 → 6 / 15

### Framework fit
Framework correctly identifies HC3 as the sub-domain with the highest base delegation authority. But the Obermeyer case shows the framework's discrete risk_level variable is brittle: the Optum Impact Pro model scored as operational under a naive application and only emerged as a high-risk clinical-fairness issue after external research. The framework needs a hook that flags "operational AI that influences patient allocation" as high-risk regardless of administrative positioning.

### Incident evidence
HBI-06 (Optum), HBI-17 (DeepMind-Royal Free), HBI-21 (Olive), HBI-22 (Forward CarePods). Optum is the strongest case that HC3 can slide into HC8-adjacent fairness failures.

### Framework adaptation recommended
Add a "downstream patient-effect test" to HC3 scoring: if the operational AI's output influences patient allocation, priority, timing, or resource access, risk_level defaults to 1-2.

---

## 5. HC4 — Drug discovery and R&D AI

### Delegation scoring

| Dimension | Score | Justification |
|---|---|---|
| Domain (safety prior) | 3 (relaxed) | Pre-patient; wet-lab verification downstream |
| Decision structure | 2 | Semi-structured candidate selection |
| Risk level | 2 | Medium — false candidates absorb R&D spend but do not harm patients |
| Scenario condition | 3 | Baseline |
| Evidence strength | 2 | Moderate — AlphaFold and similar tools have strong benchmark evidence; generative-chemistry less so |
| Governance readiness | 1 | Weak — R10 non-binding; no pre-market AI regulation |
| **Sum** | **13** | RECOMMEND or AUTOMATE band |

No override triggers (risk medium not high; scenario baseline; evidence moderate). HC4 is the only sub-domain where AUTOMATE WITH GUARDRAILS is cleanly justified under framework scoring.

### RVCS-1 scoring

**Substantive configuration** (Big Pharma R&D with wet-lab + ADMET + in-vivo pipeline):
Q1=3, Q2=3, Q3=2, Q4=2, Q5=2 → 12 / 15

**Typical configuration** (early-stage AI-first startup without wet-lab infrastructure):
Q1=2, Q2=2, Q3=1, Q4=1, Q5=1 → 7 / 15

### Framework fit
Framework correctly places HC4 at the top of its authority band. The substantive/typical gap (12 vs 7) is consistent with the scale-based track's findings but here is driven by presence or absence of wet-lab verification infrastructure rather than regulator-facing apparatus.

### Incident evidence
HBI-18 (BenevolentAI BEN-2293), HBI-19 (Exscientia), HBI-20 (Recursion REC-994). These are Phase 2 failures, not AI failures in the framework's sense — the AI's recommendation was acted on and the wet-lab / clinical pipeline was the verification mechanism, which correctly detected lack of efficacy. The economic harm (sunk R&D spend, layoffs) is real but does not land at a patient.

The incidents do identify a framework-adjacent issue: AI candidates at this rate of failure (majority Phase 2 miss) may be producing worse candidates than non-AI selection, which is an economic-efficiency question rather than a safety question. The framework does not score efficiency.

### Framework adaptation recommended
HC4 is the only sub-domain where the framework's output "AUTOMATE WITH GUARDRAILS" requires no qualification for safety. The guardrails are standard drug-development infrastructure (GLP, wet lab, IND).

---

## 6. HC5 — Pharmacovigilance and post-market drug safety

### Delegation scoring

| Dimension | Score | Justification |
|---|---|---|
| Domain (safety prior) | 1 | Patient safety (population-level signal) |
| Decision structure | 2 | Semi-structured (causality assessment) |
| Risk level | 2 | Medium — false signals or missed signals affect population labelling |
| Scenario condition | 3 | Baseline |
| Evidence strength | 2 | Moderate — pharmacovigilance methods well-validated classically; AI-augmented less so |
| Governance readiness | 3 | Strong — GVP / ICH E2E / FDA Sentinel |
| **Sum** | **13** | RECOMMEND or AUTOMATE band |

### RVCS-1 scoring

**Substantive configuration** (Big Pharma global safety team with QPPV, ICH-compliant):
Q1=3, Q2=3, Q3=3, Q4=2, Q5=2 → 13 / 15

**Typical configuration** (mid-cap pharma safety team, automated triage):
Q1=2, Q2=2, Q3=2, Q4=1, Q5=1 → 8 / 15

### Framework fit
Framework produces clean output. Pharmacovigilance is the sub-domain with the highest combined governance readiness and RVCS-1 substantive score in the taxonomy.

### Incident evidence
HBI-27 (Novo Nordisk FDA warning letter). A systemic post-approval-reporting failure tied to AI-augmented case triage is the only healthcare-bio AI incident in this sub-domain. This case raises a question the framework does not address: when AI augments a traditionally strong verification pipeline, does it reduce the verification quality the pipeline was built to produce? The Novo Nordisk warning letter suggests yes — automated invalidation rules removed cases from the reviewed pool before human review.

### Framework adaptation recommended
HC5 is a test case for whether the framework can detect erosion of existing verification infrastructure by AI augmentation. The framework's current scoring treats "governance readiness = strong" as a stable property of the sub-domain. The HBI-27 case suggests governance readiness should be re-evaluated when AI automation enters a previously manual verification step.

---

## 7. HC6 — Precision medicine and genomics

### Delegation scoring

| Dimension | Score | Justification |
|---|---|---|
| Domain (safety prior) | 1 | Patient safety downstream via treatment match |
| Decision structure | 2 | Semi-structured (variant → significance) |
| Risk level | 1 | High (wrong treatment assignment) |
| Scenario condition | 2 | Baseline or edge-case (novel variants) |
| Evidence strength | 2 | Moderate — variant databases biased toward European ancestry (Q1 source-quality issue) |
| Governance readiness | 2 | Adequate — LDT rule phase-in, IVDR; gap for polygenic risk scores |
| **Sum** | **10** | ASSIST or RECOMMEND; weak-evidence override applicable when novel variant |

For well-characterised variants with tumour-board consensus: 10 → RECOMMEND. For novel variants: weak-evidence override → ASSIST.

### RVCS-1 scoring

**Substantive configuration** (academic molecular tumour board):
Q1=3, Q2=3, Q3=3, Q4=2, Q5=2 → 13 / 15

**Typical configuration** (commercial genomics lab without tumour-board review):
Q1=2, Q2=2, Q3=2, Q4=1, Q5=1 → 8 / 15

### Framework fit
Framework works when sub-domain is further decomposed by variant novelty. The framework's current scoring treats HC6 as monolithic; in practice the novel-variant case and the well-characterised-variant case call for different authority levels.

### Incident evidence
HBI-29 (Tempus AI — specification gaming and normative violation). The incident does not primarily concern variant-calling quality but commercial overclaim and data resale. It is not a strong test of HC6 framework fit.

### Framework adaptation recommended
Sub-domain HC6 should be split into HC6a (well-characterised variants with established tumour-board review) and HC6b (novel variants without consensus). This is the only sub-domain where the current single-row scoring is clearly too coarse.

---

## 8. HC7 — Mental health and patient-facing AI

### Delegation scoring

| Dimension | Score | Justification |
|---|---|---|
| Domain (safety prior) | 1 | Patient safety direct; vulnerable-population exposure |
| Decision structure | 1 | Unstructured (conversational) |
| Risk level | 1 | High (suicide, self-harm, delayed care) |
| Scenario condition | 1-2 | Often edge-case (user in crisis) |
| Evidence strength | 1 | Weak — scarce prospective validation; Tessa HBI-12 is the canonical case |
| Governance readiness | 1 | Weak — wellness carve-out; R12 is the largest gap in the taxonomy |
| **Sum** | **5-6** | ASSIST band |

Multiple overrides stack: high-risk + weak-governance + weak-evidence + edge-case. The framework output is ASSIST with mandatory human escalation paths — a specific sub-band the current framework does not formally define.

### RVCS-1 scoring

**Substantive configuration** (Woebot pre-sunset with FDA Breakthrough designation path and clinical oversight):
Q1=2, Q2=2, Q3=3, Q4=1, Q5=2 → 10 / 15

**Typical configuration** (generic LLM marketed for wellness; Character.AI adjacency):
Q1=1, Q2=0, Q3=0, Q4=0, Q5=0 → 1 / 15

The typical-configuration RVCS-1 score of 1 / 15 is the lowest in the full sub-domain × configuration matrix. It matches the scale-based track's "solo-attorney 1 / 15" case — structurally similar positions produce structurally similar scores.

### Framework fit
The framework produces the correct prescription (strict ASSIST + escalation) but the prescription is not what is happening in deployment. HC7 is the sub-domain where framework output and observed practice diverge most sharply. Character.AI (HBI-14) deployed at volume with a de facto AUTOMATE configuration. The gap is not a framework-output problem; it is a framework-enforcement problem that sits outside the delegation framework proper.

### Incident evidence
HBI-12 (NEDA Tessa), HBI-13 (Koko), HBI-14 (Character.AI), HBI-15 (Replika), HBI-22 (Forward CarePods), HBI-25 (ChatGPT pharmacotherapy), HBI-28 (Kaiser strike), HBI-30 (Woebot sunset). Every one of these is consistent with the framework's prescription of strict ASSIST. HBI-30 (Woebot) is the case that shows what following the framework's prescription costs when the regulatory environment does not support the infrastructure the prescription assumes.

### Framework adaptation recommended
HC7 requires an explicit "infrastructure-dependent tier" designation — the scale-based track's S1 insight applied sub-domain-wise. The framework should recognise that HC7 at S1 patient-direct-use or S2 consumer-facing-platform configurations cannot be made safe by private actor discipline alone. Required infrastructure: platform-level crisis-detection escalation, integrated hotline connections, mandatory disclosure of LLM base model and finetuning, liability allocation to the deployer rather than the patient.

---

## 9. HC8 — Health insurance / utilization management

### Delegation scoring

| Dimension | Score | Justification |
|---|---|---|
| Domain (safety prior) | 1 | Patient safety downstream via denied care |
| Decision structure | 2 | Semi-structured (claim + policy → decision) |
| Risk level | 1 | High |
| Scenario condition | 2 | Baseline |
| Evidence strength | 2 | Moderate; outcome data on denial overturn rates exists (HBI-09 plaintiffs allege 90% overturn on appeal) |
| Governance readiness | 2 | Adequate for Medicare Advantage under CMS-4201-F; WEAK for commercial ERISA plans |
| **Sum** | **10 for MA / 9 for non-MA** | ASSIST or RECOMMEND band |

For non-MA deployments, weak-governance override may apply given consequential-decision criterion: reduce by one level → ASSIST.

### RVCS-1 scoring

**Substantive configuration** (Medicare Advantage payer post-CMS-4201-F with clinician review meaningfully applied):
Q1=2, Q2=2, Q3=2, Q4=2, Q5=2 → 10 / 15

**Typical configuration** (commercial ERISA payer with PxDx-style 1.2-second clinician review):
Q1=1, Q2=0, Q3=0, Q4=1, Q5=1 → 3 / 15

Q3 score of 0 in typical configuration reflects structural conflict: the verification step is not directed at clinical correctness; it is directed at approval throughput.

### Framework fit
The framework produces reasonable prescriptions but the RVCS-1 scoring is where HC8 diverges. The Q3 = 0 result for typical configuration is a **verification-chain-is-adversarial** finding that the existing reasoning-verification framework was not designed to capture. The CMS 2024 rule partially addresses the Q3 failure by requiring individual review but does not address the employment-incentive conflict that makes the review low-quality.

### Incident evidence
HBI-06 (Optum), HBI-09 (UnitedHealth nH Predict), HBI-10 (Humana), HBI-11 (Cigna PxDx). All four cases converge on the same pattern: AI recommendation → conflicted review → denial → harm downstream. This is the cleanest multi-case convergence in the incident inventory.

### Framework adaptation recommended
RVCS-1 Q3 (normative acceptability) should be expanded to explicitly test for adversarial verification-chain positioning. A verification step where the reviewer has direct financial interest in one outcome does not count as Q3-satisfying verification at current framework scoring.

---

## 10. HC9 — Administrative and documentation AI

### Delegation scoring

| Dimension | Score | Justification |
|---|---|---|
| Domain (safety prior) | 2 (relaxed) | Not a clinical decision; but note enters legal medical record |
| Decision structure | 2 | Semi-structured |
| Risk level | 2 | Medium — hallucinated content can enter record; billing accuracy risk |
| Scenario condition | 3 | Baseline |
| Evidence strength | 2 | Moderate — ambient-scribe evaluation literature emerging |
| Governance readiness | 1 | Weak — HIPAA and CMS billing rules do not address generative hallucination |
| **Sum** | **12** | RECOMMEND band |

Weak-governance + consequential-decision may trigger override if hallucination rate in deployment is high; current evaluations (HBI-23 ~1.4% rate) suggest override is warranted for high-stakes patient types. For general encounters: RECOMMEND with signing clinician review.

### RVCS-1 scoring

**Substantive configuration** (AMC ambient-scribe pilot with structured pre-sign review process):
Q1=2, Q2=2, Q3=2, Q4=1, Q5=2 → 9 / 15

**Typical configuration** (community hospital or solo clinician using ambient scribe without dedicated review time):
Q1=1, Q2=1, Q3=1, Q4=0, Q5=1 → 4 / 15

### Framework fit
Framework correctly identifies RECOMMEND as the default. But the "signing clinician reviews and edits before signing" assumption on which RECOMMEND depends is precisely the step that fails under typical deployment time pressures. The RVCS-1 typical score of 4 / 15 is consistent with the Permanente pilot (HBI-24) documented misdiagnoses.

### Incident evidence
HBI-23 (Whisper hallucinations), HBI-24 (Permanente pilot). Both cases validate the framework's concern that typical-configuration review is structurally insufficient.

### Framework adaptation recommended
HC9's RVCS-1 Q4 score is 0-1 across configurations because signing clinicians do not have a base rate for how often an ambient-scribe note diverges from what they dictated. The framework should recognise that Q4 at HC9 typical cannot be supplied by the clinician privately — it requires vendor-published per-institution audit data.

---

## 11. Cross-sub-domain synthesis

### Delegation output matrix

| Sub-domain | Substantive score | Typical score | Prescription (substantive) | Prescription (typical) |
|---|---|---|---|---|
| HC1 Imaging | 11 | 11 | RECOMMEND | ASSIST (evidence) |
| HC2 CDS | 9 | 9 | ASSIST (override) | ASSIST (override) |
| HC3 Ops | 14 | 14 | AUTOMATE W/GUARDRAILS; ASSIST if patient-routed | RECOMMEND; ASSIST if patient-routed |
| HC4 Drug discovery | 13 | 13 | AUTOMATE W/GUARDRAILS | RECOMMEND (weaker wet-lab capacity) |
| HC5 Pharmacovigilance | 13 | 13 | AUTOMATE W/GUARDRAILS | RECOMMEND (automation-erodes-review concern) |
| HC6 Genomics | 10 | 10 | RECOMMEND for characterised; ASSIST for novel | ASSIST |
| HC7 Mental health | 5-6 | 5-6 | ASSIST + escalation | ASSIST + escalation (but deployment often at AUTOMATE) |
| HC8 UM | 10 (MA) / 9 (non-MA) | 10 / 9 | ASSIST or RECOMMEND | ASSIST |
| HC9 Documentation | 12 | 12 | RECOMMEND | RECOMMEND (but review quality undermines) |

### RVCS-1 substantive-typical spread

| Sub-domain | Substantive | Typical | Spread |
|---|---|---|---|
| HC1 Imaging | 12 | 8 | 4 |
| HC2 CDS | 12 | 7 | 5 |
| HC3 Ops | 11 | 6 | 5 |
| HC4 Drug discovery | 12 | 7 | 5 |
| HC5 Pharmacovigilance | 13 | 8 | 5 |
| HC6 Genomics | 13 | 8 | 5 |
| HC7 Mental health | 10 | 1 | **9** |
| HC8 UM | 10 | 3 | **7** |
| HC9 Documentation | 9 | 4 | 5 |

**The HC7 and HC8 spreads (9 and 7 respectively) are the largest in the full taxonomy** — larger than the scale-based track's cross-tier spread for most dimensions. This reproduces the scale-based track's Finding 1 (infrastructure > headcount) in healthcare with unusual clarity: the sub-domains with the largest gaps between substantive and typical are the sub-domains where typical deployments most closely resemble what the scale-based track calls "S1 solo" configurations.

### Framework-output divergence from observed deployment

Five sub-domains show framework-prescription vs deployment-reality divergence:

1. **HC2** — framework says ASSIST under weak-evidence override; Epic deployed at scale pre-2022 at RECOMMEND-or-higher de facto (HBI-01, HBI-02).
2. **HC7** — framework says ASSIST + escalation; Character.AI, Replika, generic LLM mental-health usage deployed at de facto AUTOMATE (HBI-14, HBI-15).
3. **HC8 non-MA** — framework says ASSIST; Cigna PxDx-style deployments at de facto AUTOMATE pre-CMS-4201-F (HBI-11).
4. **HC9 typical** — framework says RECOMMEND with real review; deployment pressures push toward rubber-stamp (HBI-23, HBI-24).
5. **HC3 when patient-routed** — framework says ASSIST-or-RECOMMEND; Optum Impact Pro-style deployments at RECOMMEND-or-higher (HBI-06).

These five divergences are the framework's empirical pass-or-fail tests. The framework would have correctly predicted the failure in each case if its override rules had been applied; the failures are not framework-output failures but framework-enforcement failures that sit at the delegation-decision-maker level.

### Framework adaptations recommended from the nine sub-domain applications

1. **HC2** — explicitly code CDS-carve-out + vendor-embedded + no-site-validation as governance_readiness = 1 (not 2).
2. **HC3** — add a downstream-patient-effect test: operational AI that influences patient allocation / priority / timing defaults to risk_level ≤ 2.
3. **HC5** — flag that automation of previously manual verification steps should trigger re-evaluation of governance_readiness even when the parent regime scores strong.
4. **HC6** — split into HC6a well-characterised and HC6b novel variants; different authority bands apply.
5. **HC7** — introduce "infrastructure-dependent tier" designation for sub-domains where private actor discipline is structurally insufficient; HC7 × S1-S2 is the first explicit instance.
6. **HC8** — expand RVCS-1 Q3 to test for adversarial verification-chain positioning (employment-incentive conflict).
7. **HC9** — recognise that Q4 confidence calibration at HC9 typical cannot be supplied privately; requires vendor-published per-institution audit.

These seven revisions are the concrete framework output of this track and feed into `synthesis.md`.
