# Healthcare and Bio AI — Scale Tier Mapping

status: draft
date: 2026-04-21
purpose: Place healthcare-bio AI actors on the S1-S7 scale tier taxonomy from the scale-based track, identify sub-domain × tier cells with high exposure and low verification capacity, and test whether the scale-based track's three load-bearing findings (infrastructure > headcount, overtrust as equilibrium, public-good threshold running through tiers) reproduce in healthcare.

This document depends on the scale-based track's framework: see `research/extensions/scale-based/comparative-matrix.md` and `research/extensions/scale-based/cross-tier-synthesis.md`. Readers unfamiliar with S1-S7 should start there.

---

## 1. Mapping the tiers to healthcare actors

### S7 — International institutions
**Healthcare actors**: WHO (ethics and governance of AI for health; LMM guidance 2023, 2024 updates); IMDRF (International Medical Device Regulators Forum); ICH (International Council for Harmonisation of Technical Requirements, including ICH E2E pharmacovigilance, and emerging AI-in-drug-development positions); OECD health working parties; Global Digital Health Partnership; PRAC at EMA touches this tier through its supranational coordination role.
**Verification structure**: Multi-year standing-committee cycles; dozens of reviewers per guidance document; legitimacy across sovereign jurisdictions is the product, not per-decision epistemic verification.
**Representative failure mode**: Guidance laundering — an AI-governance principle becomes "the international consensus" via paraphrase without any individual reviewer having audited its applicability to a specific deployment.
**Healthcare specifics**: WHO's 2024 guidance on large multi-modal models is the archetype; it names principles and harms but is not itself a verification instrument.

### S6 — National governments and public agencies
**Healthcare actors**: FDA (US, Digital Health Center of Excellence, SaMD Action Plan), EMA (EU, reflection paper on AI/ML in drug lifecycle), MHRA (UK, AI Airlock), PMDA (Japan), MFDS (Korea, world-first AI diagnostic approval 2020), NMPA (China); NIH; CMS (utilization AI rule 2024); national health services (NHS England, Korean NHIS, NHS in Scotland); state-level health departments; Veterans Health Administration.
**Verification structure**: Dense formal apparatus (pre-market clearance, post-market surveillance protocols, IDE/IND reviews, HDE, De Novo pathways) but per-deployment inferential capture at the clinician's desk is weak. FDA's premarket process gates whether a device can be sold; it does not verify that a specific clinician in a specific hospital used it appropriately on a specific patient.
**Representative failure mode**: Heavy ex-ante pre-market process + nominal post-market surveillance + reactive response to incidents. The Epic Sepsis Model case is the archetype — the model did not require FDA clearance (CDS carve-out), got deployed at hundreds of hospitals, was evaluated negatively in an external 2021 JAMA Internal Medicine study (Wong et al.), and changes came after publication rather than from regulatory surveillance.
**Healthcare specifics**: The FDA has the densest AI device authorisation record in the world (900+ AI/ML-enabled devices authorised by late 2025). But the authorisation volume has not translated into per-deployment verification at scale. Singapore's AI Verify (cross-domain) and MHRA's AI Airlock (healthcare-specific) are the notable attempts at building deployment-side verification infrastructure.

### S5 — Regulated professions and licensed institutions
**Healthcare actors**: This tier is where the majority of healthcare AI-facing verification happens. Representative cells include:

- **Academic medical centres** (Mass General Brigham, Johns Hopkins, Mayo Clinic, Kaiser Permanente Research, Stanford Health) — institutional AI governance committees; internal validation of external AI models before deployment; some have dedicated AI assurance groups (Duke Institute for Health Innovation, Stanford Center for Artificial Intelligence in Medicine and Imaging)
- **Community hospitals and hospital systems** (HCA, Tenet, Ascension, CommonSpirit) — vendor-selected AI, fewer internal validation resources
- **Specialty practices with high AI touch** (radiology groups, pathology groups, oncology practices)
- **Solo licensed clinicians** — family physicians, solo psychiatrists, solo cardiologists using AI tools directly
- **Pharmacies** (retail and hospital) — dispensing AI and drug-interaction CDS
- **Licensed nurses** — both as primary users of CDS at bedside and as mediated users of hospital operations AI

**Verification structure**: Professional liability is the steepest sanction gradient in the full taxonomy for this tier. Malpractice exposure is personal to the clinician. Hospital accreditation (Joint Commission, DNV) is institutional but translates into personal pressure through credentialing and privileging.
**Representative failure mode**: Within-tier variance is extreme. Academic medical centres with AI assurance teams approach the scale-based track's "S5 Big Law Harvey+review" configuration — strong institutional substitute for missing regulator-issued protocol. Community hospitals without such teams approach the "S5 Solo" configuration — same professional ethics rules, orders-of-magnitude less infrastructure.
**Healthcare specifics**: The solo licensed clinician (S1 × S5 intersection, flagged as the single most dangerous cell in the scale-based track) maps in healthcare to the solo family physician using GPT-based clinical reasoning tools, the solo psychiatrist using AI-assisted note generation, the sole community radiologist reviewing AI-flagged studies. These practitioners face S5 malpractice exposure with S1 verification capacity. The liability mismatch is precisely the scale-based track's diagnosis.

### S4 — Large corporations and multinationals
**Healthcare actors**:

- **Big Pharma** (Pfizer, Novartis, Roche, Merck, J&J, AstraZeneca, Eli Lilly, GSK, Sanofi, AbbVie, Takeda) — well-funded AI/ML groups; internal model validation; dense interaction with regulators
- **Large hospital systems** (HCA Healthcare, Ascension, CommonSpirit, Kaiser Permanente, Providence, Trinity Health) — enterprise IT and analytics teams; Epic / Oracle Health / Cerner enterprise deployments
- **Big Tech in healthcare** (Google Health / DeepMind Health, Microsoft Healthcare, Oracle Health, Amazon Health Services / One Medical / Amazon Pharmacy, Apple Health)
- **EHR vendors at enterprise scale** (Epic Systems, Oracle Health)
- **Imaging AI vendors with broad penetration** (GE Healthcare, Siemens Healthineers, Philips Healthcare — each with AI portfolios integrated into imaging platforms)
- **Large insurers** (UnitedHealth Group + Optum, CVS Health + Aetna, Elevance Health / Anthem, Cigna, Humana) — operate at the intersection of S4 corporate resources and HC8 utilization AI
- **AI-first drug discovery at scale** (Isomorphic Labs as an Alphabet subsidiary; Recursion after Exscientia merger; Insilico Medicine at near-S4 scale)

**Verification structure**: Governance apparatus is dense and formal (pre-deployment AI review committees, privacy impact assessments, clinical advisory boards). But the scale-based track's finding of "S4 substantive vs S4 typical cliff" reproduces in healthcare:
- **S4 substantive** (e.g., Google Health's internal evaluation protocols for diabetic retinopathy AI, Microsoft AETHER for healthcare AI releases, FDA-facing pharma regulatory affairs) — 6-12 reviewers per significant deployment, multi-stage review
- **S4 typical** (e.g., a community hospital system selecting and deploying Epic's sepsis model with vendor-provided validation materials) — one IT director and one clinical lead sign-off; no internal re-validation

**Representative failure mode**: The UnitedHealth nH Predict case (STAT News 2023 and class-action litigation) is an S4 failure mode: governance apparatus existed but did not prevent AI-driven denial at scale. The apparatus was optimised for compliance, not for per-decision verification of whether the algorithm's recommendation was clinically correct for each patient.
**Healthcare specifics**: The pharma sub-tier has the densest regulatory-facing verification infrastructure in the full taxonomy (pharmacovigilance systems, ICH-compliant clinical trial operations, GMP manufacturing controls). This infrastructure is genuinely high-performing for pre-approval and post-market pharmaceutical risks. Whether it extends to AI used in pharma R&D (HC4) is an open question — the pre-clinical AI-usage pipeline does not sit inside the regulated pharmacovigilance infrastructure.

### S3 — Mid-sized enterprises
**Healthcare actors**:

- **Regional hospital systems and community hospitals** (~500-1500 beds; 2,000-10,000 staff)
- **Regional pharma companies and mid-cap biotechs**
- **Mid-sized health tech** (radiology platforms not at GE / Siemens / Philips scale, EHR vendors serving smaller practices)
- **Specialty pharmacy benefit managers**
- **Medium-sized insurers and provider-sponsored plans**
- **Physician practice management organisations** (PPMs) and MSOs at middle-market scale

**Verification structure**: The compression tier. Clinical AI decisions receive review from a small number of role-holders — a medical director, a CMIO, an IT security lead — who also have operational responsibilities competing for time. No dedicated AI assurance function. Dependence on vendor-supplied validation and compliance artefacts (SOC 2, ISO 42001, 510(k) clearance documents) as substitutes for internal evaluation.
**Representative failure mode**: "Dresses like S4, operates like S2." A community hospital system adopting Epic with full CDS plus a third-party imaging AI behaves administratively like a large healthcare system but verifies like a small one. This matches the scale-based track's finding that S3 substitutes vendor compliance artefacts for internal reasoning-verification discipline.
**Healthcare specifics**: Community hospital systems are the single largest cell by bed count in US healthcare and are the least-studied tier in healthcare AI literature. Peer-reviewed studies of clinical AI skew heavily toward academic medical centres. The community-hospital tier is where deployment volume is highest and verification infrastructure is thinnest — the healthcare analog of the scale-based track's S3 evidentiary silence.

### S2 — Small enterprises and startups
**Healthcare actors**:

- **Digital health startups** (consumer-facing: Noom, Calm, Headspace, Woebot; provider-facing: Abridge, Ambient Healthcare, Suki, Ellipsis Health)
- **Clinical AI startups at Series A-C** (Viz.ai, Aidoc pre-enterprise scale, Notable Health, Hippocratic AI, Caption Health pre-GE acquisition)
- **AI-first drug discovery at startup scale** (BenevolentAI historically, Valence Discovery pre-Recursion acquisition, smaller generative-chemistry platforms)
- **Specialty telehealth and mental-health platforms** (Cerebral, BetterHelp, Talkspace, Hims/Hers health divisions)
- **Clinical trial tech** (Medable, H1, trial patient-matching startups)

**Verification structure**: Two-population split, parallel to the scale-based track's S2:
- **AI-native health startups with research-lab founders** (Hippocratic AI, some AI-first drug discovery) implement strong technical discipline on Q1 source quality, Q2 inferential validity, and Q5 failure mode awareness because the founders are research-lab alumni
- **AI-using health startups** (Cerebral being the archetype pre-DEA controversy, Character.AI being the cross-domain consumer analog) have essentially zero standing verification practice until external forcing functions (HIPAA audit, FDA 510(k) pathway, state licensure board action) cluster within months of the forcing event

**Representative failure mode**: Q3 normative-acceptability failure dominates the failure record at S2 healthcare startups. Cerebral's 2022 DEA investigation (controlled-substance prescribing practices), Nurx telehealth issues, the 2023 NEDA Tessa eating-disorder chatbot incident, Character.AI's 2024 wrongful-death lawsuits tied to mental-health-adjacent usage — every one of these is the sub-population skipping the "should we do this at all?" question, not a capacity problem.
**Healthcare specifics**: The regulated-customer transition (S2 → S5) happens when a digital-health startup lands a hospital-system customer or a major pharmacy customer. The scale-based track's finding that this transition is often a sudden single-contract cliff holds in healthcare with unusual clarity: one hospital system's procurement triggers HIPAA BAAs, SOC 2 certification, clinical advisory board stand-up, and 510(k) pathway consideration within weeks.

### S1 — Solo entrepreneurs and individual decision-makers
**Healthcare actors**:

- **Solo licensed clinicians** (as noted in S5 above, they live at the S1 × S5 intersection)
- **Patients directly using AI** (asking ChatGPT / Claude / Gemini about symptoms, using symptom checkers, using mental-health chatbots, using consumer genetic-testing interpretations)
- **Family caregivers using AI** to interpret a relative's condition
- **Individual research clinicians** using AI literature tools without institutional support
- **Solo medical-device startups** (pre-team)

**Verification structure**: Verifier = requester = decision-maker. N_reviewers = 1 by definition. For patients using health AI, the reviewing party is not medically trained; the framework's verification disciplines (Q1-Q5) are structurally inapplicable without external infrastructure.
**Representative failure mode**: The scale-based track's finding that Q2 inferential validity is structurally impossible at S1 (same person cannot reliably play advocate and skeptic on the same artefact under time pressure) applies with particular force to patients using LLMs for symptom interpretation. Q4 confidence calibration is impossible because the patient has no base rate for "how often is the AI wrong about conditions in my demographic." Q1 is partially supported by cross-model comparison but not by independent clinical review.
**Healthcare specifics**: **The solo licensed clinician is the most dangerous single cell in the healthcare taxonomy** — exactly as the scale-based track identified across all domains. In healthcare this cell has specific populations: the solo family physician in a rural practice using GPT-based clinical-reasoning tools, the solo psychiatrist using AI scribe tools with mental-health content, the solo radiologist at a critical-access hospital reading AI-flagged imaging studies. They carry full S5 malpractice exposure with S1 verification capacity, and healthcare's patient-safety stakes sharpen the hazard relative to other regulated professions.

## 2. Sub-domain × tier matrix

The key analytical move of this document is the **sub-domain × tier cross-product**. Each cell is a specific deployment context with specific verification capacity.

| Sub-domain \ Tier | S7 | S6 | S5 | S4 | S3 | S2 | S1 |
|---|---|---|---|---|---|---|---|
| HC1 Imaging / pathology | IMDRF guidance | FDA / EMA clearance apparatus | Radiology groups, academic vs community | GE / Siemens / Philips; Aidoc, Viz.ai at enterprise | Regional hospital radiology depts | Imaging AI startups | Solo radiologist at critical-access hospital |
| HC2 Clinical decision support | WHO guidance | FDA CDS carve-out; CMS | Clinicians at bedside | Epic, Oracle Health | Community hospital IT | Clinical CDS startups | Solo clinician with AI-driven alerts |
| HC3 Hospital operations | OECD hospital-sector reports | CMS operational rules | CMIOs, CNOs | Large health system enterprise IT | Mid-sized hospital admin | Health ops startups | Clinic owner using ops AI |
| HC4 Drug discovery / R&D | ICH AI-in-drug-development discussions | FDA IND review, EMA scientific advice | Pharma R&D teams with regulatory obligations | Big Pharma, Isomorphic Labs | Mid-cap biotech | AI-first drug discovery startups | Solo academic researcher using AI tools |
| HC5 Pharmacovigilance | ICH E2E; IMDRF | FDA FAERS, EMA EudraVigilance | QPPV, medical-safety officers | Pharma global safety teams | Mid-cap pharma safety | Small pharma PV teams | Individual safety officer |
| HC6 Precision medicine / genomics | Global Alliance for Genomics and Health | FDA CDx, LDT rule | Molecular pathologists, tumour boards | Foundation Medicine, Invitae, Myriad | Regional genetic-counselling practices | Genomics AI startups | Patient using direct-to-consumer genetic AI interpretation |
| HC7 Mental health / patient-facing | WHO LMM guidance | FDA wellness carve-out (gap) | Licensed therapists prescribing AI-adjunct | Calm, Headspace at corporate wellness scale | Mid-sized mental-health platforms | Woebot, Wysa, Replika, Character.AI | Patient directly using chatbot |
| HC8 Insurance / utilization | — | CMS 2024 rule; state AI-in-UM laws | Payer medical directors (conflicted) | UnitedHealth, Cigna, Humana | Regional payers, PBMs | Claims-processing startups | — |
| HC9 Administrative / documentation | — | CMS billing rules | Clinicians signing notes | Microsoft DAX, Abridge enterprise | Mid-sized hospital revenue cycle | Suki, smaller ambient-scribe vendors | Solo clinician dictating |

### High-exposure, low-capacity cells (the hazard cells)

The cells in this matrix vary enormously in combined exposure and verification capacity. The cells with high exposure and low capacity are the hazard zones:

1. **HC1 × S1** — solo radiologist at a critical-access hospital reading AI-flagged imaging studies. Full malpractice exposure, no double read, no peer consultation, vendor provides the AI but no validation for this specific patient population.

2. **HC2 × S3 and HC2 × S1** — community hospital deploying Epic Sepsis Model without internal validation; solo clinician receiving AI alerts without independent review capacity.

3. **HC7 × S1 and HC7 × S2** — patient directly using mental-health chatbot; startup deploying chatbot to patient without clinician-in-loop. Regulatory gap (wellness carve-out) makes this the single most dangerous sub-domain × tier cell across the taxonomy. The scale-based track's S1 solo-entrepreneur hazard compounds with HC7's vulnerable-population exposure.

4. **HC8 × S4** — large insurer deploying utilization-AI at scale. Not low-capacity in the conventional sense, but the verification chain is adversarial by design; capacity exists but is not directed at patient interest.

5. **HC6 × S1** — patient interpreting direct-to-consumer genetic risk assessments with AI assistance. Low literacy and high stakes; population representativeness issues compound.

Five other cells are notable for being surprisingly well-governed:

- **HC1 × S4** with full imaging-AI integration (major AMCs with internal AI assurance) — 12-14/15 RVCS-1 equivalent
- **HC4 × S4** — Big Pharma + AI-first drug discovery with wet-lab verification infrastructure
- **HC5 × S4-S6** — the pharmacovigilance regulatory stack is the cleanest verification infrastructure in the full healthcare taxonomy
- **HC6 × S5** (academic tumour boards) — tumour-board norms predate AI and extend to AI-assisted variant interpretation
- **HC9 × S4 with signing-clinician review** — when the review step functions as designed

## 3. Testing the scale-based track's three findings

### Finding 1 (infrastructure > headcount) in healthcare

The scale-based track's first finding is that substantive verification quality is predicted by infrastructure, not by organisational headcount.

**Healthcare test**: The finding reproduces cleanly.

- A large community hospital system (S3-S4 by headcount) that deploys vendor AI without internal validation (Epic Sepsis Model pre-2022 is the archetype) produces worse verification outcomes than a smaller academic medical centre (also S3-S4 by headcount) with an AI assurance team.
- A solo radiologist at an AMC with a departmental AI assurance workflow (double-read, quarterly drift review, access to a clinical validation subset) has better verification infrastructure than a solo radiologist at a critical-access hospital reading AI-flagged studies alone — same individual clinical skill, very different outcomes.
- Big Pharma pharmacovigilance infrastructure outperforms mid-cap pharma despite similar per-drug regulatory requirements; the difference is instrumentation.

The healthcare-specific infrastructure element that the scale-based track's "productization infrastructure" operationalises is the **clinical validation apparatus**: specific protocols for silent-mode evaluation, prospective validation in the institution's own patient population, drift monitoring, override-rate tracking, and change-management processes for model updates. Where this apparatus exists, verification is substantive; where it does not, verification is a signature on a vendor-supplied checklist.

### Finding 2 (overtrust as equilibrium) in healthcare

The scale-based track's second finding is that the 66% overtrust / 91% executive concern gap is the predicted equilibrium of an assumption mismatch, not a failing.

**Healthcare test**: Reproduces with qualitative strengthening.

The per-decision verification budget at HC2 typical (CDS alert at bedside) is 5-30 seconds. The RVCS-1 five-discipline review at the framework's intended level requires 10-50 minutes. The budget-to-requirement gap in healthcare CDS is one to two orders of magnitude wider than the S4 typical gap in the scale-based track. Alert fatigue — well-documented in the CDS literature — is the corresponding behaviour: clinicians override the majority of AI alerts because they cannot spend 10-50 minutes per alert when they have 30 seconds.

The healthcare-specific implication: **the framework's RVCS-1 protocol is structurally infeasible at HC2 typical deployment conditions**, and this is not a failing of the framework or the clinician but a mismatch between the framework's assumed conditions and the deployment's actual conditions. The HC2 response should be infrastructure — smarter alerts, higher precision before escalating, pre-computed verification artefacts — not clinician training.

### Finding 3 (public-good threshold runs through tiers) in healthcare

The scale-based track's third finding is that the boundary below which reasoning verification cannot be produced privately runs inside tiers, not between them.

**Healthcare test**: Reproduces with an additional healthcare-specific boundary.

- Inside S4: the boundary between AMC with AI assurance and community hospital without it.
- Inside S5: the boundary between Big Law analog (major radiology groups, tumour boards at AMCs) and S5 Solo analog (solo family physician, solo psychiatrist).
- Inside S2: the boundary between AI-native digital health startups with research-lab founders and AI-using mental-health startups with consumer-app founders.

The healthcare-specific additional boundary: **HC7 patient-facing mental health AI at S1 patient use is uniformly below the public-good threshold**. No configuration of patient, platform, or geography produces adequate private reasoning verification for a patient in crisis using a chatbot. This is a structural conclusion: the tier combination (patient = S1 verifier + HC7 vulnerable exposure + regulatory gap) cannot be fixed inside the actor's decision chain. Public infrastructure (platform safety requirements, mandatory escalation protocols, crisis hotline integration, liability allocation) must supply the verification.

This result is the healthcare analog of the scale-based track's S1 finding and converges on the same conclusion through a different mechanism.

## 4. Cross-tier dynamics specific to healthcare

Three scale-crossing dynamics are distinctive to healthcare:

1. **Pharmaceutical R&D → clinical trial → marketed drug** (HC4 S2/S4 → HC5 S4 → S5/S1 patient use). An AI-discovered molecule traverses tiers over a decade. Verification at S4 pre-clinical is wet-lab-based and substantive; verification at S5 clinical-trial is protocol-driven; verification at S1 patient use is pharmacist + prescriber + labelling. Failures at one tier (e.g., AI-introduced bias in pre-clinical target selection) may not surface until a later tier. This is the longest scale-crossing chain in the healthcare taxonomy.

2. **Hospital AI deployment → patient use** (HC2 S4/S3 → S5 clinician → S1 patient). An AI alert fires at S4 enterprise deployment → filters through S3 hospital IT → fires at S5 clinician bedside → affects S1 patient care. The patient is the least-informed actor in the chain.

3. **Consumer health AI → clinician response** (HC7 S1 patient use → S5 clinician emergency room). When a patient's chatbot interaction goes wrong, the S5 clinician inherits the outcome with no visibility into the AI reasoning chain. This mirrors the "legitimacy laundering downward" dynamic the scale-based track identified at S7 → S4, but in a clinical direction.

## 5. Implications for framework revision

Synthesising the scale mapping:

1. The healthcare extension of the framework needs a **sub-domain × tier matrix** rather than a simple tier ranking. The nine sub-domains × seven tiers produce 63 cells; the eight "hazard cells" identified in §2 are candidates for explicit framework exceptions.

2. The framework's **S4 substantive vs S4 typical cliff** is sharper in healthcare than in any other domain the repo has studied, because community hospitals and academic medical centres share the same tier designation but operate with dramatically different infrastructure.

3. The **S1 × S5 solo-licensed-professional cell** has a particular healthcare manifestation that may warrant separate treatment: the solo clinician using generative AI for note generation, clinical reasoning assistance, or patient-facing summarisation is exposed to malpractice without meaningful verification infrastructure.

4. **HC7 × S1 is uniformly below the public-good threshold**. This is the clearest empirical instance of the scale-based track's public-good argument in any domain and should be the citing example when the framework argues for infrastructure-dependent intervention.

5. The scale-based track's **verification capacity curve** should be redrawn in healthcare as a **verification capacity surface** indexed by sub-domain and tier. The curve's S3-S4 breakpoint maintains its qualitative shape in healthcare but the quantitative values and the exact break location differ by sub-domain.

These implications feed into `synthesis.md` as concrete revisions to propose to the core framework.
