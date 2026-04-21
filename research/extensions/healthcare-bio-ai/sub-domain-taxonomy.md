# Healthcare and Bio AI Sub-Domain Taxonomy

status: draft
date: 2026-04-21
purpose: Decompose "healthcare AI" into structurally distinct sub-domains and show that a single domain label collapses heterogeneous decision structures with qualitatively different delegation and verification requirements.

---

## 1. Decomposition method

"Healthcare AI" is treated in the repo's core framework as one of eight domains. That works for the comparative claim in the core (healthcare is governance-first, default ASSIST) but hides the fact that the decisions being made inside healthcare differ more from each other than healthcare-as-a-whole differs from operations or finance.

Sub-domains are carved along four structural axes:

1. **Decision type** — diagnostic classification, risk prediction, resource allocation, molecular-property prediction, payment adjudication, generative output.
2. **Safety-criticality** — direct physical harm possible, indirect (delayed care), no direct patient contact.
3. **Regulatory perimeter** — inside Software as a Medical Device (SaMD), inside drug regulation, inside payer regulation, or outside all three.
4. **Verification chain** — who actually reviews the AI output before it affects a patient, and at what point in the decision chain.

Nine sub-domains emerge. They are not mutually exclusive at the vendor level (Epic and Cerner touch multiple), but they are structurally distinct as decision contexts.

## 2. The nine sub-domains

### HC1 — Diagnostic imaging and pathology AI

**Decision type**: image → finding / flag / worklist-priority.
**Examples**: CT / MRI / X-ray AI (Aidoc, Viz.ai, Qure.ai, Annalise.ai), digital pathology AI (PathAI, Paige, Ibex), retinal imaging (IDx-DR, Optain), mammography AI (iCAD, DeepHealth, Lunit, Vara).
**Regulatory perimeter**: tightly inside FDA SaMD; over 900 AI/ML-enabled medical devices authorised in the US as of late 2025 ([FDA list of authorized AI/ML-enabled devices](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices), A-tier). Radiology is the single largest category.
**Verification chain**: radiologist or pathologist reads the AI output alongside the image; double-read workflows in some institutions; FDA clearance path requires retrospective studies (sometimes prospective).
**What fails when it fails**: false negatives that delay diagnosis (radiology); false positives that cause unnecessary procedures; distribution shift (model trained on one scanner / population fails on another); automation bias (reader defers to AI and misses call).
**Delegation default**: ASSIST to tightly governed RECOMMEND. The framework's risk-level dimension caps authority because the decision is a medical one and the sanction gradient (malpractice) is personal to the reader.
**Differentiator from HC2**: image-based, mostly pre-clearance validated, typically single-decision-point, decision embedded in a specialist workflow with established double-read norms.

### HC2 — Clinical decision support and deterioration prediction

**Decision type**: patient → risk flag / treatment suggestion / alert.
**Examples**: Epic Sepsis Model (ESM), Epic Deterioration Index, Cerner early-warning systems, pharmacy decision support (drug-drug interaction alerts augmented with AI), treatment-recommendation engines (the defunct IBM Watson for Oncology is the canonical cautionary case).
**Regulatory perimeter**: historically outside FDA SaMD under the 21st Century Cures Act clinical decision support (CDS) carve-out if the clinician can independently review the basis; FDA 2022 CDS guidance tightened the carve-out. Vendor-embedded CDS sits in a contested perimeter zone.
**Verification chain**: the attending clinician, nurse, or pharmacist reviews the alert inline during care. Alert fatigue is the dominant failure-adjacent phenomenon.
**What fails when it fails**: Q1 source-quality failure (model trained on biased historical data), Q2 inference-validity failure (proxy outcome diverges from intended outcome — the canonical Epic Sepsis Model case), Q5 failure-mode-awareness failure (reader does not know the model's false-negative rate).
**Delegation default**: ASSIST. RECOMMEND is hard to justify because the decision chain is compressed ("alert appears at bedside → clinician decides in seconds").
**Differentiator from HC1**: non-image, often embedded in EHR, frequently proprietary and non-transparent to the reviewing clinician, regulatory perimeter contested.

### HC3 — Hospital operations AI

**Decision type**: capacity / flow / staffing / resource-allocation.
**Examples**: bed-management AI, OR scheduling, staff rostering, readmission prediction used for discharge planning, revenue-cycle AI, denial-appeal automation.
**Regulatory perimeter**: mostly outside clinical AI regulation. May touch Medicare Conditions of Participation via denial / readmission tied to reimbursement. HIPAA applies to the data side.
**Verification chain**: hospital administrators, operations managers; almost never clinician-reviewed per decision; verification happens at dashboard aggregation level, not per-patient.
**What fails when it fails**: equity failures (readmission models penalising high-socioeconomic-disadvantage populations, flagged in Obermeyer et al. 2019 on commercial risk-prediction bias); false confidence from throughput optimisation; indirect safety effects when discharge timing is AI-influenced.
**Delegation default**: RECOMMEND or AUTOMATE WITH GUARDRAILS for operational decisions where no direct patient-safety harm. ASSIST when the downstream effect routes back to patient care (discharge timing, staffing minimums on safety-critical units).
**Differentiator from HC1-HC2**: primarily economic/logistic rather than clinical; failure mode is slow and population-level rather than fast and patient-level; reviewer is not a licensed clinician.

### HC4 — Drug discovery and R&D AI

**Decision type**: target → molecule → candidate / trial design / patient match.
**Examples**: protein structure prediction (AlphaFold ecosystem, RoseTTAFold), generative molecular design (Insilico Medicine, Exscientia, BenevolentAI, Recursion, Isomorphic Labs), clinical trial patient matching, synthetic control arms, retrosynthesis planning.
**Regulatory perimeter**: **largely unregulated pre-clinically**. The FDA is a late gatekeeper — the IND (Investigational New Drug) filing is the first moment AI-derived molecules meet the regulator. FDA issued a 2023 discussion paper on AI/ML in drug development (A-tier) but substantive regulation is nascent.
**Verification chain**: medicinal chemists, ADMET assay teams, pre-clinical in-vitro and in-vivo experiments are the real verification mechanism. Failure filters out in the wet lab.
**What fails when it fails**: candidate attrition (the vast majority of AI-generated molecules fail downstream validation — e.g. BenevolentAI's high-profile clinical-trial setbacks, C-tier); false targets; reproducibility crises in generative-design benchmarks; target discovery that does not translate to druggable biology.
**Delegation default**: RECOMMEND is acceptable because verification is the wet lab, not the committee. AUTOMATE WITH GUARDRAILS is appropriate for narrow steps (e.g., retrosynthesis search within a defined chemistry).
**Differentiator from HC1-HC3**: pre-patient; verification is downstream physical experimentation, not a clinician-in-the-loop; regulatory perimeter is vastly looser.

### HC5 — Pharmacovigilance and post-market drug safety AI

**Decision type**: signal → adverse-event flag.
**Examples**: FDA FAERS signal detection, EMA EudraVigilance, disproportionality analysis augmented with ML, NLP of social media and EHR for adverse-event surfacing, causality assessment support.
**Regulatory perimeter**: regulated via GVP (Good Pharmacovigilance Practices), ICH E2E. Pharma companies have pharmacovigilance obligations; regulators themselves use AI on their own data.
**Verification chain**: pharma safety teams (Qualified Person for Pharmacovigilance, QPPV, in EU) and regulator signal-management teams; formalised review protocols; long-timescale decisions (weeks to months per signal).
**What fails when it fails**: false-positive signals that trigger label changes without sufficient causality; false negatives that miss emerging harms (the classic failure is Vioxx-era missed signals; AI-era failures are less documented but implied in FDA Sentinel commentary).
**Delegation default**: RECOMMEND. The review protocol is strong; the clinical impact is downstream via label change or market withdrawal, not immediate.
**Differentiator from HC2**: post-market, long timescale, institutionally reviewed; failure is a population-level signal, not a patient-level alert.

### HC6 — Precision medicine and genomics AI

**Decision type**: variant → clinical significance / treatment match.
**Examples**: variant classification (Invitae, Myriad, Foundation Medicine), tumour molecular profiling and treatment match, polygenic risk scores (contested clinical utility), companion diagnostics.
**Regulatory perimeter**: companion diagnostics are FDA-regulated devices. Laboratory-developed tests (LDTs) historically enforced minimally; the FDA's 2024 final rule on LDTs changes this for phase-in (A-tier). Polygenic risk scores sit in a gap.
**Verification chain**: molecular pathologists, genetic counsellors, tumour boards; decision windows are days to weeks.
**What fails when it fails**: Q1 source-quality failure (databases of variant pathogenicity are biased toward populations of European ancestry); Q2 inference-validity failure (polygenic scores optimised in one population do not transfer); Q3 normative-acceptability failure (screening in populations where treatment pathway is absent).
**Delegation default**: ASSIST for novel variant calls; RECOMMEND for well-characterised variants where tumour-board norms exist.
**Differentiator from HC1-HC2**: inference is about the patient's biology rather than their current state; population representativeness is the dominant risk surface; verification chain is specialised (molecular tumour board) and not universal.

### HC7 — Mental health and patient-facing AI

**Decision type**: symptom / message → support response / screening / escalation.
**Examples**: Woebot, Wysa, Replika, Character.AI (not health-positioned but used as such), Koko's 2023 AI experiment, NEDA's Tessa chatbot (2023 eating-disorder incident), symptom checkers (Ada, Babylon).
**Regulatory perimeter**: the **largest and most dangerous regulatory gap** in the taxonomy. Wellness carve-outs keep most conversational mental-health AI outside FDA authority unless it makes diagnostic claims; EU AI Act classifies some as high-risk but enforcement is nascent.
**Verification chain**: **often none at runtime**. A user in distress receives an AI response directly with no clinician review. Escalation paths vary from rigorous (Woebot clinical oversight) to absent (generic LLM chatbots marketed for wellness).
**What fails when it fails**: Q3 normative-acceptability failure (should this be deployed at all in this population?); direct patient harm (the 2024 Character.AI-associated suicide lawsuit is the canonical case); fluent-hallucination safety misinformation; false reassurance delaying clinical help.
**Delegation default**: ASSIST at most, with mandatory human escalation paths. Current practice widely violates this default.
**Differentiator from HC1-HC6**: direct patient contact with no clinician intermediary; regulatory perimeter near-zero for conversational forms; vulnerable-population exposure is the defining feature.

### HC8 — Health insurance / utilization management AI

**Decision type**: claim / authorisation request → approve / deny / flag.
**Examples**: UnitedHealth's nH Predict (the subject of STAT News investigation 2023 and class-action litigation), Cigna's PxDx / PXDX algorithm (ProPublica 2023 investigation), prior-authorisation AI at Humana, Medicare Advantage AI-driven denials, fraud-detection AI across payers.
**Regulatory perimeter**: CMS issued a 2024 final rule stating Medicare Advantage plans cannot use algorithms alone to deny care — decisions must involve clinician review (A-tier, CMS CMS-4201-F). State-level action (California AB 3030) follows. Still underdeveloped relative to SaMD regulation.
**Verification chain**: **structurally conflicted**. The reviewing clinician is employed by the payer and is incentivised to align with the algorithm's denial recommendation. The patient's treating physician has standing to appeal but often lacks access to the algorithm's reasoning.
**What fails when it fails**: overrides Q3 normative-acceptability wholesale (cost minimisation as sole objective); downstream patient harm through delayed or denied care; systematic bias against high-acuity patients.
**Delegation default**: contested. The CMS 2024 rule says not AUTOMATE; current practice at several major insurers went further than the rule would now allow.
**Differentiator from HC1-HC7**: economic rather than clinical decision, but with direct patient consequence; adversarial structure between payer and patient / provider; verification chain is compromised by design.

### HC9 — Administrative and documentation AI

**Decision type**: clinical encounter → note / code / bill.
**Examples**: ambient clinical documentation (Abridge, Nuance DAX, Suki, Microsoft Dragon Copilot), AI-assisted medical coding (3M, optum), claims generation, chart summarisation, RCM automation.
**Regulatory perimeter**: largely outside SaMD because the output is documentation, not a clinical decision. HIPAA covers data. CMS billing rules cover coding accuracy. EHR vendors incorporate ambient AI broadly.
**Verification chain**: clinician reviews and signs the generated note; coding staff review codes; billing goes through revenue cycle.
**What fails when it fails**: fluent-hallucination of clinical content (the ambient-scribe field has documented cases of fabricated findings entering notes, e.g., Vayu 2024 and ongoing vendor evaluations); upcoding risk; liability shift — the signing clinician is legally responsible for content they may not have dictated.
**Delegation default**: RECOMMEND. The default is that the clinician reviews and edits before signing. AUTOMATE is inappropriate because the note enters the legal medical record and has downstream care and billing consequences.
**Differentiator from HC1-HC8**: output is text, not a decision; generative-LLM failure modes dominate (Weidinger W3 misinformation, W5 interaction harms via embedded hallucinations); speed of adoption is extreme (ambient-scribe deployment went from niche in 2022 to mainstream at US academic medical centres by 2025).

## 3. Cross-sub-domain comparison

### 3.1 Delegation-mode defaults

| # | Sub-domain | Delegation default | Rationale |
|---|---|---|---|
| HC1 | Imaging / pathology | ASSIST → tightly governed RECOMMEND | FDA-cleared; specialist reviewer per image; personal malpractice liability |
| HC2 | Clinical decision support | ASSIST | Fast alert loop; alert fatigue undermines review; contested regulatory perimeter |
| HC3 | Hospital operations | RECOMMEND (AUTOMATE for narrow ops) | Population-level, logistic; no per-decision clinician review needed |
| HC4 | Drug discovery and R&D | RECOMMEND → narrow AUTOMATE | Wet-lab verification downstream; pre-patient |
| HC5 | Pharmacovigilance | RECOMMEND | Formal review protocols; long decision timescale |
| HC6 | Precision medicine / genomics | ASSIST → RECOMMEND | Dependent on variant novelty and tumour-board availability |
| HC7 | Mental health / patient-facing | ASSIST (with mandatory escalation) | Vulnerable-population exposure; no clinician intermediary |
| HC8 | Health insurance / utilization | ASSIST (per CMS 2024 rule) | Conflicted verification chain; downstream patient harm; recent regulatory intervention |
| HC9 | Administrative / documentation | RECOMMEND | Clinician signs; output enters legal medical record |

This matrix shows the core framework's "healthcare → default ASSIST" prescription is too coarse. The default differs by sub-domain, and two sub-domains (HC3, HC4) justify RECOMMEND or higher while two others (HC2, HC7) demand strict ASSIST with conditions the current default does not articulate.

### 3.2 Dominant failure-mode profile

| # | Sub-domain | Dominant Amodei-2016 mode | Dominant Weidinger-2022 mode (when LLM-based) |
|---|---|---|---|
| HC1 | Imaging / pathology | Distributional shift | Not primarily LLM |
| HC2 | Clinical decision support | Specification gaming (proxy-outcome drift) | — |
| HC3 | Hospital operations | Scalable oversight failure (population-level equity) | — |
| HC4 | Drug discovery | Distributional shift (in silico → wet lab) | — |
| HC5 | Pharmacovigilance | Side effects (false signals propagating) | — |
| HC6 | Precision medicine | Distributional shift (population representativeness) | — |
| HC7 | Mental health / patient-facing | Oversight failure | Misinformation (W3), interaction harms (W5) |
| HC8 | Insurance / utilization | Specification gaming (cost proxy) + oversight failure | — |
| HC9 | Administrative / documentation | Oversight failure | Misinformation (W3) |

The ambient-scribe sub-domain (HC9) and patient-facing mental-health AI (HC7) are the two sub-domains where LLM-specific failure modes dominate. Every other sub-domain is primarily an Amodei-2016 problem. This matters for framework revision — the reasoning-verification framework's Q1-Q5 instruments were designed with LLM outputs in mind; in HC1-HC6 and HC8 they apply but are not the most natural fit.

### 3.3 Verification chain length

| # | Sub-domain | Per-decision verification chain | Typical time per review |
|---|---|---|---|
| HC1 | Imaging / pathology | 1 reader (radiologist/pathologist); occasional double read | 1-15 min |
| HC2 | Clinical decision support | 1 clinician, inline with care | 5-30 sec |
| HC3 | Hospital operations | Aggregate dashboard review; rarely per-patient | N/A per patient |
| HC4 | Drug discovery | Medicinal chemist → ADMET → in-vivo (chain of months-to-years) | Weeks per candidate |
| HC5 | Pharmacovigilance | Safety scientist → QPPV → regulator | Weeks |
| HC6 | Precision medicine / genomics | Molecular pathologist → tumour board | Days to weeks |
| HC7 | Mental health / patient-facing | **Often zero at runtime** | 0 sec typically |
| HC8 | Insurance / utilization | Payer-employed clinician (conflicted) | Minutes |
| HC9 | Administrative / documentation | Signing clinician edits/signs note | 30 sec - 5 min |

HC7's zero-seconds-at-runtime cell and HC8's conflicted-reviewer cell are the structural analogs of the scale-based track's "verifier compression at S1" finding. These are the healthcare contexts where the five-discipline reasoning verification framework fails the hardest because the verification step the framework assumes simply is not happening.

### 3.4 Regulatory perimeter map

| # | Sub-domain | Primary regulatory perimeter | Gap |
|---|---|---|---|
| HC1 | Imaging / pathology | FDA SaMD (strong) | Post-market drift monitoring weak |
| HC2 | Clinical decision support | 21st Century Cures Act CDS carve-out (contested) | Vendor-embedded CDS often outside FDA |
| HC3 | Hospital operations | Outside clinical AI regulation | Equity-audit requirements emerging but uneven |
| HC4 | Drug discovery / R&D | Late gatekeeping at IND filing | Pre-IND AI largely unregulated |
| HC5 | Pharmacovigilance | GVP, ICH E2E (strong) | AI-specific guidance nascent |
| HC6 | Precision medicine / genomics | FDA LDT rule 2024 phase-in; CDx for accompanying drugs | Polygenic risk scores sit in a perimeter gap |
| HC7 | Mental health / patient-facing | **Wellness carve-out — near-zero** | The largest patient-exposure gap in the taxonomy |
| HC8 | Insurance / utilization | CMS 2024 rule + state law | Commercial payers and Medicaid managed-care less covered |
| HC9 | Administrative / documentation | CMS billing rules; not SaMD | Generative-hallucination risk unaddressed |

The regulatory gap column is the load-bearing conclusion of this taxonomy. Two gaps (HC4 pre-IND drug discovery AI, HC7 wellness-carve-out mental health AI) are structural — the regulatory perimeter was drawn before AI deployment, and the deployment pattern has changed but the perimeter has not.

## 4. Findings emerging from the decomposition

1. **The single "healthcare" label in the core framework collapses decisions with delegation defaults ranging from AUTOMATE to strict ASSIST.** The default-per-sub-domain matrix (§3.1) makes this explicit. The core framework should add a sub-domain axis to its healthcare row or replace the single row with nine.

2. **The worst verification gaps are in the two sub-domains where regulatory perimeter is weakest, not where deployment volume is largest.** HC1 (imaging, highest deployment volume) has strong regulation and a specialist reviewer per decision. HC7 (mental-health chatbots, growing volume) has near-zero regulation and often zero reviewer per interaction. The gap is not a function of volume; it is a function of regulatory history.

3. **LLM-specific failure modes dominate exactly two sub-domains (HC7, HC9), not healthcare AI broadly.** Treating "LLM healthcare risk" as one thing confuses policymaking. The HC7 risk is patient-vulnerability exposure; the HC9 risk is hallucinated content entering the legal medical record. Different interventions follow.

4. **The verification chain at HC8 is conflicted by design.** A payer-employed clinician reviewing an AI recommendation to deny care is not a meaningful verification step in the sense RVCS-1 assumes. The CMS 2024 rule addresses the algorithm-alone failure but not the employment conflict. This is a sub-domain where the framework correctly identifies the problem but the existing regulatory intervention is insufficient.

5. **Drug discovery AI (HC4) is the only sub-domain where AUTOMATE with narrow guardrails is clearly justified.** The verification mechanism is physical experiment, the timescale is months, and candidate attrition is the accepted noise floor. The framework's default of "healthcare → ASSIST" is too conservative here.

These five findings feed into the framework-application document (`framework-application.md`) and the final synthesis (`synthesis.md`).

## 5. Limitations of this decomposition

- The nine sub-domains cover the major cases but omit niches: wearables-only consumer health AI, veterinary AI, environmental health AI, genomic research AI separate from clinical diagnostics. These are either out-of-scope for this track or absorbed into adjacent sub-domains.
- Vendor products often span sub-domains (Epic, Cerner, Oracle Health touch HC2, HC3, HC8, HC9 simultaneously). Sub-domain analysis of vendors would require a second cut.
- The "LLM failure modes dominate HC7 and HC9" finding is current-as-of-2026. Agentic clinical AI, if it diffuses at the pace vendors project, will shift the dominant modes in HC2 and HC3 as well. The taxonomy will need revision within 12-24 months.
- The decomposition treats each sub-domain as independent. In practice HC2 and HC9 interact (ambient-scribe notes feed CDS features); HC4 and HC6 interact (AI-discovered drugs pair with AI-identified biomarkers). Interaction effects are not analysed here.

## 6. Inputs this document provides to downstream documents

- `regulatory-landscape.md` uses the nine-sub-domain frame to organise its gap analysis.
- `incident-inventory.md` tags each incident with its HC1-HC9 sub-domain.
- `framework-application.md` applies the 6-dim delegation framework and 5-discipline reasoning verification sub-domain by sub-domain, using the defaults in §3.1 as baselines.
- `scale-mapping.md` identifies which actor tier (S1-S7) dominates each sub-domain.
- `synthesis.md` extracts cross-sub-domain patterns from §4.
