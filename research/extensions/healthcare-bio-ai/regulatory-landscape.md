# Healthcare and Bio AI Regulatory Landscape

status: draft
date: 2026-04-21
purpose: Comparative survey of healthcare/bio AI regulatory regimes as of April 2026, organised around the nine sub-domains defined in `sub-domain-taxonomy.md`. Identifies structural gaps where deployment outpaces regulation and feeds into framework-application.md.
evidence_tiers: A = primary regulator source; B = credible secondary (specialist press, professional association, academic review); C = inferred; D = speculative (flagged).

---

## 1. Comparative matrix of regimes

| # | Regime | Primary instruments | Current status (Apr 2026) | Scope | Key strength | Key gap | Tier |
|---|---|---|---|---|---|---|---|
| R1 | **US FDA — SaMD / AI-enabled devices** | AI/ML SaMD Action Plan (Jan 2021); Final PCCP guidance (4 Dec 2024); Draft Lifecycle Management guidance (6 Jan 2025); CDS Final Guidance (Sep 2022); GMLP Guiding Principles (N88 Final, Jan 2025) | PCCP in force; lifecycle draft open; 1,451 AI-enabled devices authorised cumulatively by end-2025 (~295 in 2025 alone); 76% are radiology | Pre-market (510(k), De Novo, PMA) + PCCP for post-market adaptive change + labelling + GMLP | First operational adaptive-AI change-plan mechanism; mature device list | LLMs fall outside §520(o)(1)(E) CDS device definition; bias testing not mandated; post-market real-world performance monitoring voluntary | A |
| R2 | **US CMS / HHS — coverage, reimbursement, nondiscrimination** | HHS §1557 Final Rule (26 Apr 2024; effective 5 Jul 2024; PCDST duties from 1 May 2025); CMS MA Final Rule CMS-4201-F (2024); AMA CPT Category III codes 0877T-0880T, 0902T, 0932T (2025); 2026 additions | §1557 in force; CMS-4201-F in force; further MA AI guardrails proposed Dec 2024, partially deferred | Anti-discrimination for any patient care decision-support tool; MA coverage-determination rules; AI-assisted-service reimbursement signalling | First federal duty on covered entities for discriminatory AI output; CPT codes create reimbursement rails | Enforcement mechanisms nascent; PCDST audit processes immature; private commercial insurers outside MA/Medicaid unaffected | A |
| R3 | **EU — AI Act + MDR/IVDR + EMA** | Regulation (EU) 2024/1689 (AI Act, in force 1 Aug 2024); MDR 2017/745 + IVDR 2017/746; EMA Reflection Paper on AI in the Medicinal Product Lifecycle (CHMP/CVMP adopted Sep 2024); MDCG 2025-6 (AI Board) | AI Act phased: GPAI from Aug 2025; Annex III high-risk Aug 2026 scheduled; Article 6(1) / Annex I medical devices Aug 2027 — but the **Digital Omnibus on AI package (proposed 19 Nov 2025)** is widely expected to push medical-device AI deadlines to 2028 | Pre-market conformity assessment via MDR notified body + FRIA + data governance + post-market monitoring + transparency + human oversight + bias/robustness | Broadest horizontal scope; binds provider and deployer; aligns with MDR classification (most AI SaMD → Class IIa/IIb/III = high-risk) | Double burden with MDR capacity bottleneck; LLM/GPAI-to-medical-device translation unclear; Digital Omnibus uncertainty creates compliance whiplash | A |
| R4 | **UK — MHRA + NICE** | MHRA AI Airlock (pilot Apr 2024-Mar 2025; Phase 2 through Spring 2026; £3.6M Phase 3 funding 2026-29); NICE Evidence Standards Framework for Digital Health Technologies (ESF, updated Aug 2022) | Phase 2 reports due Summer 2026; ESF in force but under review for adaptive AI | Regulatory sandbox for AI-as-Medical-Device; evidence standards for clinical effectiveness / economic value; HTA-style NHS adoption gatekeeping | Internationally novel sandbox methodology; NICE ESF integrates value assessment with performance | No binding horizontal AI law (contextual approach); ESF struggles with continuously-learning systems; SME burden high | A |
| R5 | **Japan — PMDA / MHLW** | PMD Act (programs-as-devices); MHLW 2018 Notice on AI oversight; PMDA IDATEN (adaptive-update mechanism); 2025 PMD Act amendments; JIS T 62366-1:2022 | IDATEN operational, expanding 2025-26; SaMD One-Stop Consultation Desk active | Pre-market approval + physician-in-the-loop mandate + lifecycle update mechanism analogous to PCCP | One of earliest adaptive-AI pre-approval systems; clear doctor-accountability doctrine | Conservative approval volume relative to FDA; published AI-device list less transparent than FDA's | B |
| R6 | **South Korea — MFDS** | MFDS AI medical device guidelines (original 2017); world-first Class III AI device approval (JLK JBS-01K, Sep 2018); Generative AI Medical Device Guideline (24 Jan 2025 — claimed world-first); updated AI-SaMD guidance (Nov 2025); Market Immediate Entry fast-track (26 Jan 2026, joint MOHW/MFDS) | Active; generative-AI guideline in force; fast-track operational | Pre-market approval tiered by maturity/risk; generative-AI-specific lifecycle requirements; reimbursement linkage | First national generative-AI medical-device framework; tight alignment with industrial policy | Domestic focus; external-research transparency limited; bias requirements less developed than §1557 | A |
| R7 | **China — NMPA** | NMPA SaMD classification guidance; Key Review Points for AI Medical Devices (2019, revised 2022); Announcement [2025] No. 63 whole-lifecycle regulation (Oct 2025); generative-AI labelling/registration rules (effective 1 Sep 2025) | 126 Class III AI medical devices approved cumulatively by Dec 2024; Special Approval Channel saves ~83 days average review | Pre-market approval by algorithm maturity; SaMD-specific GMP; post-market incident reporting; generative-AI content/labelling controls | Highest Class III AI approval volume globally; integrated industrial policy + regulatory acceleration | Limited external transparency on bias/equity controls; overlap with CAC Deep Synthesis / GenAI rules — enforcement layering unclear | B |
| R8 | **WHO** | *Ethics and governance of AI for health* (Jun 2021); *Guidance on large multi-modal models* (18 Jan 2024, 40+ recommendations); Global Initiative on AI for Health (GI-AI4H, 2023-) | Non-binding guidance; actively cited in LMIC frameworks | Ethics principles; LMM governance; equity and data protection | Only norm-setter with truly global legitimacy; explicit LMM framework earlier than most regulators | Non-binding; implementation relies on member-state adoption; does not address reimbursement or liability | A |
| R9 | **IMDRF** | GMLP Guiding Principles (N88 Final, 27 Jan 2025); Characterization Considerations for Medical Device Software (N81 Final, 2025); earlier SaMD framework (N10, N12, N23) | Active; N88 and N81 adopted 2025 | Pre-market expectations harmonisation; GMLP lifecycle principles; software-risk characterisation | Cross-recognised anchor for FDA / Health Canada / MHRA; supports convergence | Non-binding; trails horizontal law (AI Act); no post-market monitoring requirements | A |
| R10 | **Drug-discovery AI (FDA / EMA)** | FDA CDER/CBER/CDRH *Discussion Paper: Using AI/ML in the Development of Drug and Biological Products* (May 2023; ~800 comments); EMA Reflection Paper (Sep 2024); FDLI commentary (Jul 2025) | Non-binding; no drug-discovery AI product subject to direct pre-market AI regulation; AI regulated indirectly via GxP and study-data integrity | Indirect: GLP/GCP/GMP cover AI as a tool; outputs (drug candidates) regulated via standard IND/NDA/BLA or EMA MAA | Acknowledges AI role across discovery → pharmacovigilance; leaves room for innovation | **Most structurally under-regulated layer in the stack**; no bias, no transparency, no model-card norms for AI-designed molecules | A |
| R11 | **US-EU CDS divide** | FDA CDS Final Guidance (Sep 2022) — 4 criteria under §520(o)(1)(E) for non-device CDS; EU MDR Rule 11 — most decision-supporting software is Class IIa/IIb/III and therefore a device | Stable but interpretations diverge; LLMs usually fail FDA's 4 criteria (particularly criterion 4 — user cannot independently review basis) | Scope of what counts as a regulated device | FDA's 4-criteria test is crisp; EU's Rule 11 is risk-expansive | US leaves many CDS apps unregulated; EU captures almost all — notified-body bottleneck | A |
| R12 | **Health insurance / UM AI** | CMS MA Final Rule CMS-4201-F (2024); CMS proposed MA AI guardrails (Dec 2024, partially deferred); HHS §1557 covers private insurers receiving federal funds; state-level (California AB 3030, NY S.09149) | In force for MA; **largely unregulated for commercial ERISA plans** | Requires individualised medical-necessity review; AI cannot override physician judgment in MA | First federal guardrails on payer-side AI; nondiscrimination hook via §1557 | No federal pre-market review of payer AI; no transparency/registry; commercial and employer plans outside Medicare Advantage face minimal oversight | A |
| R13 | **Liability allocation** | US: state tort law + Federation of State Medical Boards guidance (Apr 2024); American Law Institute *Restatement of the Law of Medical Malpractice* (approved May 2024); EU: AI Liability Directive (stalled; reportedly withdrawn early 2025 but uncertain under Digital Omnibus — D); revised Product Liability Directive 2024/2853 (in force Dec 2024); France: Art. L.1142-1 Code de la santé publique (fault standard) | Evolving; ~14% YoY rise in AI-implicated malpractice claims reported for 2024 | Risk allocation for AI-assisted diagnostic error | EU PLD 2024 expands producer liability and eases evidentiary burden for claimants; ALI Restatement shifts US toward reasonable-care | US state-by-state variation; physicians often absorb residual risk; EU AI Liability Directive stalled | A (US/EU), B (France doctrinal) |

## 2. Structural patterns

### Pattern 1 — Pre-market gating dominates; post-market monitoring is structurally underdeveloped

Across the nine regulator-led regimes (R1-R9), the bulk of regulatory leverage is exerted at the pre-market gate: conformity assessment, 510(k) / De Novo / PMA, Class III approval, CE marking. Post-market surveillance is nominally addressed but operationally shallow. PCCP (FDA R1) and IDATEN (PMDA R5) give adaptive-change pre-authorisation but do not impose real-world performance reporting obligations comparable to pharmacovigilance. The MHRA AI Airlock Phase 1 report (Oct 2025) explicitly flagged this as a finding. WHO 2024 LMM guidance (R8) and IMDRF N88 (R9) recommend continuous monitoring but neither creates a binding post-market telemetry regime.

**Implication for the framework**: the delegation framework's "evidence strength" dimension depends on a kind of evidence — post-deployment real-world performance — that the regulatory ecosystem is not systematically producing. The incident inventory's Pattern 1 (proprietary models deployed at scale before external validation; HBI-01 Epic Sepsis Model, HBI-05 Zech pneumonia, HBI-04 Roberts COVID-imaging) is the direct manifestation.

### Pattern 2 — Drug-discovery AI is structurally under-regulated compared to diagnostic AI

Diagnostic AI is captured everywhere because it is embedded in a device, which triggers established medical-device regimes. Drug-discovery AI is upstream of a molecule, so it is governed by the molecule's regulatory path (IND / NDA / MAA), and the AI tool itself is invisible to the regulator except through GxP study-data integrity (R10).

The FDA 2023 discussion paper and EMA 2024 reflection paper are explicitly non-binding. There is no analogue to PCCP, GMLP N88, or bias-audit §1557 for an AI tool that nominates a drug candidate. The mismatch is structural: drug-discovery AI's output passes through years of wet-lab and clinical verification, giving regulators a defensible reason to let downstream evidence absorb the risk.

**But** the incident inventory's Pattern 4 (drug-discovery's translation cliff, HBI-18/19/20) shows the downstream verification mechanism is slow and expensive (~years per candidate at Phase 2 readout) and absorbs risk as sunk cost rather than preventing it. For AI-designed proteins, AI-generated synthetic biology, and AI-driven target selection, existing frameworks were not designed to produce upstream evidence.

### Pattern 3 — Utilization-management AI is the least-regulated layer of all

R12 captures what is arguably the most consequential regulatory gap in the taxonomy. The AI that denies care — prior-authorisation algorithms, coverage-decision support, claims triage — is governed in the US only by CMS MA CMS-4201-F (Medicare Advantage only), HHS §1557 (federally-funded entities only), and state insurance codes. Commercial ERISA plans and self-funded employer plans sit outside almost every AI-specific rule. The EU AI Act partially captures this via Annex III point 5(b) ("AI used to evaluate eligibility for essential private services"), but operational application to medical insurance is unclear.

The incident inventory's Pattern 2 (cost-proxy and coverage-gatekeeper substitution, HBI-06 Optum, HBI-09 UnitedHealth nH Predict, HBI-10 Humana, HBI-11 Cigna PxDx) is the direct manifestation.

**Implication for the framework**: the delegation framework's "governance readiness" dimension should be scored as WEAK at HC8 regardless of the deploying actor's internal governance maturity, because the external regulatory backstop is absent.

### Pattern 4 — The US-EU CDS divide produces asymmetric innovation and risk

The FDA's four-criteria exemption under §520(o)(1)(E) (R11) effectively excludes most CDS software. Almost all current LLM-based clinical advice tools fail the fourth criterion (user independently reviews basis of recommendation). US regulators respond by treating such tools as unregulated rather than as regulated devices, because enforcement resources do not scale to the output volume. The EU's MDR Rule 11 does the opposite: CDS is presumptively Class IIa+ and thus a device.

The result is that US LLM health tools proliferate outside FDA review while EU tools are choked at the notified-body bottleneck. This is the single most consequential divergence in current global health-AI regulation and has direct implications for where developers incorporate and where patients first encounter LLM clinical advice.

### Pattern 5 — Liability is converging on the clinician, not the developer

Despite AI Act "deployer" vs "provider" framing, EU PLD 2024/2853 expansion, and the ALI Restatement, in practice every jurisdiction with a clear doctrine routes clinical-AI liability back to the treating physician (R13). The US Federation of State Medical Boards (Apr 2024) stated that clinicians, not AI makers, remain responsible for veracity. France's Article L.1142-1 places fault on the healthcare professional unless a defect in a health product can be shown.

This creates a governance paradox: the agent with the least ability to audit the AI (a busy clinician) bears the residual tort risk, while the agent with full epistemic access (the developer) is insulated by medical-device pre-market clearance as a quasi-safe-harbor.

**Implication for the framework**: this pattern is the regulatory manifestation of the scale-based track's finding that the most dangerous cell in the taxonomy is the solo licensed professional — S5 sanction gradient with S1 verification capacity. The regulatory structure institutionalises exactly that mismatch.

### Pattern 6 — Generative AI and LLMs fracture the existing taxonomy

Every framework here was designed for narrow, task-specific AI. LLMs and LMMs fit none of them cleanly. The WHO (R8, Jan 2024 LMM guidance), Korea MFDS (R6, Jan 2025 generative-AI guideline — first in the world by government claim), China NMPA (R7, Sep 2025 generative-AI labelling), EMA (R3, reflection paper Sep 2024), and FDA Digital Health Advisory Committee (Nov 2025 meeting on generative AI for mental health) are each carving extensions rather than recognising LLMs as a new regulatory object.

None mandates upstream model-weight transparency, training-data provenance, or base-model registration independent of the downstream medical-device wrapper. The EU AI Act's GPAI obligations (Art. 51-55) partially fill this gap for the base model but do not harmonise with MDR's device-level scrutiny.

**The next 18-24 months are likely to see the largest substantive regulatory movement precisely on this axis.**

### Pattern 7 — Regulatory capacity, not regulatory intent, is the binding constraint

Across regimes, stated ambition exceeds institutional capacity. EU notified-body bandwidth under MDR is an acknowledged bottleneck that the AI Act will exacerbate; the Digital Omnibus proposals of Nov 2025 are driven partly by this constraint. FDA's AI-device list shows radiology at ~76% of clearances — likely because other modalities lack reviewers fluent in domain + ML. MHRA's Airlock covers small numbers of pilots. The regulators that want to act adaptively (MHRA, PMDA, FDA) are building sandboxes and PCCPs precisely because traditional review throughput cannot keep pace with deployment velocity.

This is the adaptive-governance track's central claim — that regulator capacity is the binding constraint, not regulator intent — reproduced in healthcare with unusual clarity.

## 3. Sub-domain × regime perimeter map

The nine sub-domains from `sub-domain-taxonomy.md` map onto the 13 regimes as follows. Cells marked "✓" indicate substantive regulation; "◐" partial; "✗" gap.

| Sub-domain | R1 FDA SaMD | R2 HHS/CMS | R3 EU AI Act/MDR | R10 Drug-dev AI | R11 CDS divide | R12 UM AI | R13 Liability |
|---|---|---|---|---|---|---|---|
| HC1 Imaging / pathology | ✓ (strong) | ◐ (§1557 bias) | ✓ (high-risk) | — | — | — | ✓ (strong; physician bears) |
| HC2 Clinical decision support | ◐ (CDS carve-out) | ◐ | ✓ (Rule 11) | — | ✓ (divide) | — | ✓ (physician bears) |
| HC3 Hospital operations | ✗ | ◐ (bias only) | ◐ (some Annex III employment uses) | — | — | ◐ (readmission → denial) | ◐ (institution) |
| HC4 Drug discovery / R&D | ✗ | ✗ | ✗ | ◐ (non-binding) | — | — | ✗ |
| HC5 Pharmacovigilance | ✗ (drug, not device) | — | ✓ (GVP) | ◐ | — | — | ◐ (sponsor) |
| HC6 Precision medicine / genomics | ◐ (LDT rule phase-in) | ◐ | ✓ (IVDR high-risk) | — | ◐ | — | ◐ (laboratory) |
| HC7 Mental health / patient-facing | ✗ (wellness gap) | ✗ | ◐ (Annex III in some cases) | — | ✓ (CDS exemption) | — | ✗ (platform) |
| HC8 Insurance / UM | ✗ | ✓ (MA only) | ◐ (Annex III 5(b)) | — | — | ✓ (MA; state) | ◐ |
| HC9 Administrative / documentation | ✗ | ✗ | ◐ (fluctuating) | — | ✓ (CDS exemption) | — | ✓ (signing clinician) |

**Structural gaps (✗ rows)**:

- **HC4** is the single most regulation-sparse row.
- **HC7** has the most dangerous ✗ pattern given direct patient-exposure risk.
- **HC3** and **HC9** have ✗ patterns that are acceptable only under assumptions (the output does not reach the patient without clinician review) that the incident inventory shows do not always hold.

## 4. Implications for the delegation framework

The regulatory map feeds into the 6-dimensional delegation framework's "governance readiness" dimension. Synthesising:

1. **HC1 imaging/pathology** scores STRONG on governance readiness — dense pre-market regime, multi-jurisdictional convergence (R1, R3, R5, R6, R7, R9), and mature liability doctrine.
2. **HC2 CDS** scores ADEQUATE at best, WEAK under the FDA CDS carve-out — even for vendor-embedded CDS that reaches every patient.
3. **HC3 hospital operations** scores ADEQUATE for direct-ops uses, WEAK when operational decisions have patient-care downstream (readmission → discharge timing).
4. **HC4 drug discovery** scores WEAK at the AI-tool layer, strong at the downstream drug layer. This is the only sub-domain where the framework's "governance readiness" dimension requires split scoring.
5. **HC5 pharmacovigilance** scores STRONG under GVP / ICH E2E — the strongest sub-domain in the taxonomy.
6. **HC6 precision medicine / genomics** scores ADEQUATE under LDT phase-in and IVDR; polygenic risk scores sit in a perimeter gap.
7. **HC7 mental health / patient-facing** scores WEAK — the largest regulatory gap in the taxonomy.
8. **HC8 insurance / UM** scores ADEQUATE for Medicare Advantage only; WEAK everywhere else.
9. **HC9 administrative / documentation** scores WEAK — billing-rule coverage does not reach generative-hallucination risk.

The framework's default "healthcare → ASSIST" rule is too coarse because governance readiness varies from STRONG (HC1, HC5) to WEAK (HC4 AI layer, HC7, HC8 non-MA, HC9). The sub-domain × tier matrix in `scale-mapping.md` and the framework-application document use this split scoring.

## 5. Sources

Primary sources (A-tier) are hyperlinked inline in §1. Full source list:

- [FDA PCCP Final Guidance (Dec 2024)](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence)
- [FDA — AI-Enabled Medical Devices list](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-enabled-medical-devices)
- [FDA — CDS Software FAQs (4-criteria test)](https://www.fda.gov/medical-devices/software-medical-device-samd/clinical-decision-support-software-frequently-asked-questions-faqs)
- [FDA — Digital Health Center of Excellence](https://www.fda.gov/medical-devices/digital-health-center-excellence)
- [FDA/CDER — Using AI/ML in Drug & Biological Product Development (discussion paper, 2023)](https://www.fda.gov/media/165743/download)
- [Federal Register — HHS Section 1557 Final Rule (2024)](https://www.federalregister.gov/documents/2024/05/06/2024-08711/nondiscrimination-in-health-programs-and-activities)
- [CMS — 2024 Medicare Advantage Final Rule (CMS-4201-F)](https://www.cms.gov/newsroom/fact-sheets/2024-medicare-advantage-and-part-d-final-rule-cms-4201-f)
- [AMA — CPT codes for AI-enabled health services](https://www.ama-assn.org/practice-management/cpt/cpt-codes-offer-language-report-ai-enabled-health-services)
- [EMA — Reflection Paper on AI in the Medicinal Product Lifecycle (final, Sep 2024)](https://www.ema.europa.eu/en/news/reflection-paper-use-artificial-intelligence-lifecycle-medicines)
- [EU AI Act — Article 6 classification](https://artificialintelligenceact.eu/article/6/)
- [MDCG 2025-6 — Medical Devices Joint AI Board](https://health.ec.europa.eu/document/download/b78a17d7-e3cd-4943-851d-e02a2f22bbb4_en)
- [Sidley — EU Digital Omnibus Implications for MedTech (Dec 2025)](https://www.sidley.com/en/insights/newsupdates/2025/12/eu-digital-omnibus-implications-for-medtech-companies)
- [MHRA — AI Airlock collection](https://www.gov.uk/government/collections/ai-airlock-the-regulatory-sandbox-for-aiamd)
- [MHRA AI Airlock Sandbox Pilot Programme Report (Oct 2025)](https://assets.publishing.service.gov.uk/media/68ee1fb88427701993d5e02c/AI_Airlock_Sandbox_Programme_Report_Final.pdf)
- [NICE — Evidence Standards Framework for digital health technologies](https://www.nice.org.uk/corporate/ecd7)
- [PMDA — Report on AI-based SaMD](https://www.pmda.go.jp/files/000266100.pdf)
- [MFDS — Medical Devices (English)](https://www.mfds.go.kr/eng/brd/m_40/view.do?seq=72627)
- [Korean Journal of Radiology — MFDS LLM/LMM guideline overview](https://kjronline.org/DOIx.php?id=10.3348/kjr.2025.0257)
- [NMPA Announcement [2025] No. 63 — whole-lifecycle regulation](https://english.nmpa.gov.cn/2025-10/14/c_1138492.htm)
- [Nature npj Digital Medicine — China AI medical device regulation](https://www.nature.com/articles/s41746-024-01254-x)
- [WHO — Ethics and governance of AI for health: LMM guidance (2024)](https://www.who.int/publications/i/item/9789240084759)
- [WHO — Ethics and governance of AI for health (2021)](https://www.who.int/publications/i/item/9789240029200)
- [IMDRF — AI/ML working group](https://www.imdrf.org/working-groups/artificial-intelligencemachine-learning-enabled)
- [IMDRF GMLP N88 Final (Jan 2025)](https://www.imdrf.org/sites/default/files/2025-01/IMDRF_AIML%20WG_GMLP_N88%20Final_0.pdf)
- [Milbank Quarterly — AI and Liability in Medicine](https://www.milbank.org/quarterly/articles/artificial-intelligence-and-liability-in-medicine-balancing-safety-and-innovation/)
- [Bird & Bird — France AI liability under revised PLD 2024](https://www.twobirds.com/en/insights/2026/france/ai-liability-in-light-of-the-new-2024-pld-expanded-liability-challenging-defences-and-new-evidentiar)
- [Norton Rose Fulbright — CMS on MA AI coverage decisions](https://www.nortonrosefulbright.com/en/knowledge/publications/644bd9a2/cms-clarifies-medicare-advantage-organizations-use-of-ai-and-algorithms-in-coverage-decisions)

## 6. Confidence and limitations

- **D-tier flag**: The status of the EU AI Liability Directive under the Digital Omnibus (proposed 19 Nov 2025) is uncertain as of April 2026. Widely reported as withdrawn in early 2025 but the Digital Omnibus may revive elements. Any citation in a published paper should be verified at time of writing.
- **D-tier flag**: The research agent's prompt framing of the *médecin traitant* doctrine as an AI-specific liability doctrine is imprecise. French AI-liability allocation rests on Article L.1142-1 Code de la santé publique and PLD 2024, not on a named doctrine about general practitioners.
- **B-tier flag**: 2026 CPT AI-augmented code categories are reported by AMA commentary and industry press; the AMA code-book text was not directly fetched for this draft.
- **B-tier flag**: The NMPA cumulative count of 126 Class III AI devices by December 2024 is from literature review rather than direct regulator bulletin.
- The 18-24 month LLM regulatory-movement forecast in Pattern 6 is a C-tier projection.
- Coverage of African, Latin American, and smaller Asian jurisdictions is out of scope. WHO LMM guidance is the primary global-south-facing document available.
