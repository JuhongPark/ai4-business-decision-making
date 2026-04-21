# Healthcare and Bio AI Special Topic — Research Plan

status: wave_1_in_progress
date: 2026-04-21
owner: healthcare-bio-ai extension track
relationship: special topic (not a core thesis track); feeds findings back into core framework where warranted

---

## 1. Why this track exists

The core project catalogues 71 AI governance failures across eight domains. Healthcare is one of those eight domains but is represented in the core by a single minimal case (`research/core/domain-analysis/cases/healthcare-case.md`, FDA-governed SaMD) and a single scenario pack (`research/core/scenario-packs/healthcare-scenarios.md`, three scenarios H1-H3). That coverage is sufficient to support the cross-domain comparative claim in the core framework but insufficient to characterise the actual structure of AI in healthcare, hospitals, and pharma — an ecosystem where AI is deployed across settings as different as sepsis prediction, MRI reconstruction, drug-target discovery, utilization review, and mental-health chatbots.

This track is a **special topic** — a lateral expansion rather than a core thesis track — designed to:

1. Decompose "healthcare AI" into its structurally distinct sub-domains and test whether the repo's frameworks (delegation calibration, reasoning verification, scale-based capacity) hold across them.
2. Map the current (2026) regulatory landscape across jurisdictions and identify where the regulatory perimeter leaves gaps that the delegation framework must cover.
3. Expand the incident evidence base specific to healthcare/bio AI beyond what the core 71-incident inventory supports.
4. Feed revisions back into the core framework only where findings are load-bearing enough to justify it.

**This is not a new core thesis.** The scale-based track (`research/extensions/scale-based/`) and the reasoning trust verification direction remain the load-bearing extensions. Healthcare-bio AI is a cross-cutting test case that sharpens those frameworks where they touch patient safety, pharmaceutical R&D, and payer decisions.

## 2. Framing question

**Does the repo's adaptive framework (6-dim delegation × 5-discipline reasoning verification × 7-tier scale) produce actionable guidance for the structurally distinct sub-domains of healthcare and bio AI, or does healthcare's combination of patient-safety criticality, regulated-profession verification chains, and heterogeneous deployment settings break the framework's assumptions?**

The hypothesis going in is that the framework partially holds but requires three adaptations: (a) a patient-safety override that caps authority below what score bands would otherwise allow; (b) a profession-chain model where verification is explicitly distributed between clinician, hospital system, vendor, and regulator rather than concentrated at one role; (c) a drug-lifecycle model where AI is deployed at stages (pre-clinical, clinical, post-marketing) with qualitatively different evidentiary requirements.

## 3. Scope

### In scope

- **Clinical AI**: diagnostic imaging, pathology, ECG analysis, clinical decision support, sepsis and deterioration prediction, triage
- **Hospital operations AI**: scheduling, bed management, readmission prediction, staffing, revenue-cycle management
- **Pharma/biotech R&D AI**: target discovery, molecule generation, protein structure prediction (AlphaFold ecosystem), clinical trial design and patient matching, drug repurposing
- **Drug safety**: pharmacovigilance, post-market surveillance, adverse event detection
- **Precision medicine**: genomic interpretation, biomarker discovery, companion diagnostics
- **Mental health AI**: chatbots, screening tools, therapy-adjacent tools
- **Patient-facing health AI**: wearables, chronic-disease management apps, symptom checkers, LLM health advice
- **Health insurance / payer AI**: utilization management, prior authorization, claims adjudication, fraud detection
- **Administrative AI in healthcare**: clinical documentation (ambient scribes), coding, billing

### Out of scope (for this track)

- Deep technical comparison of specific models (e.g., benchmark performance of vision transformers on radiology tasks)
- Bioethics theory not directly tied to AI deployment decisions
- Veterinary AI
- Non-AI digital health (telehealth infrastructure per se)
- Wellness-only consumer products without health claims

### Deliberately in scope but treated lightly

- Agentic AI in hospital workflows — referenced where it intersects with delegation authority questions, but not characterised in depth; the agentic-AI governance space is moving too fast to pin down in this cycle
- AI in medical education and continuing medical education — noted in sub-domain taxonomy but not given its own analysis document

## 4. Analytical instruments inherited from the main project

This track uses the same instruments the scale-based track uses, with healthcare-specific adaptations:

- **6-dimensional delegation framework** (`research/core/taxonomy/category-system.md`) — domain × decision structure × risk level × scenario condition × evidence strength × governance readiness. Healthcare defaults to high-risk + safety-critical scenario condition, so the scoring has a strong prior toward ASSIST.
- **5-discipline reasoning verification (RVCS-1)** — Q1 source quality, Q2 inferential validity, Q3 normative acceptability, Q4 confidence calibration, Q5 failure mode awareness.
- **7-tier scale taxonomy (S1–S7)** — adapted here because the healthcare ecosystem has distinctive actor types (solo physician, group practice, academic medical center, national health service, WHO) that map onto S1-S7 but with sub-tier nuances.
- **Evidence grading rubric** — A (primary source / regulatory filing / peer-reviewed paper), B (credible practitioner secondary / major journalism), C (inferred from adjacent evidence), D (speculative; must be flagged).
- **FICS-1 failure incident coding** — applied to the healthcare incident inventory (see `incident-inventory.md`).

## 5. Deliverables

This track produces one directory under `research/extensions/healthcare-bio-ai/` with the following documents:

| Document | Purpose | Status |
|---|---|---|
| `research-plan.md` (this file) | Plan, scope, procedures, and deliverable manifest | Draft complete |
| `README.md` | Entry point and reading order | Draft complete |
| `sub-domain-taxonomy.md` | Decomposition of healthcare AI into 9 structurally distinct sub-domains with delegation-mode defaults | Planned |
| `regulatory-landscape.md` | Comparative matrix of FDA / EU AI Act / MDR / MHRA / PMDA / MFDS / NMPA / WHO regimes with structural-gap analysis | Planned (external research in progress) |
| `incident-inventory.md` | ~25-35 healthcare-bio AI failure cases coded with FICS-1 and failure-mechanism labels | Planned (external research in progress) |
| `framework-application.md` | 6-dim delegation + 5-discipline verification applied sub-domain by sub-domain | Planned |
| `scale-mapping.md` | Healthcare actors mapped to S1-S7 tiers with verification capacity implications | Planned |
| `synthesis.md` | Load-bearing findings, framework revisions, and connection back to the core thesis | Planned |

## 6. Procedures

The track executes six procedures in sequence, mirroring the scale-based track's method:

1. **Sub-domain decomposition** — define 9 structurally distinct sub-domains; for each, specify (i) the decision being made, (ii) who makes it today, (iii) what kind of AI is deployed, (iv) what fails when it fails.
2. **Regulatory landscape survey** — compile a comparative matrix across 8+ jurisdictions; identify structural gaps where deployment outpaces regulation.
3. **Incident inventory construction** — 25-35 cases with FICS-1 coding; map each to Amodei-2016 and Weidinger-2022 failure modes already used in the core 71-case inventory.
4. **Framework application** — apply the 6-dim delegation framework and 5-discipline reasoning verification to each sub-domain; record where the framework produces clean guidance vs. where it breaks.
5. **Scale mapping** — place representative actors from each sub-domain on the S1-S7 ladder; identify tier × sub-domain cells that are high-exposure with low verification capacity.
6. **Synthesis** — extract 3-5 load-bearing findings; recommend specific framework revisions; flag which findings feed back into core vs. stay within the extension.

## 7. Evidence quality priorities

Because healthcare AI combines high-stakes claims with a noisy evidence base, this track follows three evidence rules:

1. **Regulatory filings and peer-reviewed papers outrank vendor press releases** — always. Vendor claims about clinical performance are C-tier until an independent evaluation appears.
2. **Prospective evaluation outranks retrospective evaluation** — a model that passed retrospective silent-mode evaluation but not prospective real-world evaluation does not get credit for clinical performance.
3. **Incidents with regulatory response outrank incidents reported only in trade press** — the former are A-tier, the latter B or C depending on detail.

## 8. Relationship to other tracks

- **Scale-based track**: healthcare adds depth to the S5 regulated-professions tier (physicians are already the archetype of S5) and to the S4 substantive vs. typical distinction (academic medical centers vs. community hospitals reproduce the S4 cliff in microcosm).
- **Adaptive governance track**: healthcare is one of the most regulation-dense domains, so it tests the adaptive-governance framework's claims about regulator lag more sharply than most sectors.
- **Core 71-incident inventory**: healthcare-specific incidents gathered here supplement but do not replace the core inventory. The core stays at 71; any incidents used in core framework validation must be promoted through the core evidence channel.
- **Reasoning trust verification direction**: healthcare is the cleanest test of whether RVCS-1 scoring produces useful differentiation in a high-stakes domain where clinicians already practise a form of reasoning verification (differential diagnosis, second opinion, M&M conferences).

## 9. Honest limitations going in

- This is a single-cycle special topic, not a multi-wave research programme. Expect breadth over depth — each sub-domain gets a page-level treatment, not the full 15-page treatment the scale-based track gives S5.
- No primary empirical work. No clinician interviews, no hospital site visits, no regulatory FOIA. Evidence base is documentary.
- 2026 regulatory landscape moves fast; specific document citations may be outdated within 6-12 months. This is flagged inline where it matters.
- Korean, Japanese, and Chinese regulatory material is covered but with less depth than US and EU material due to language and access constraints (consistent with the scale-based track's Asia-market appendix practice).
- No depth on agentic AI in clinical workflows; the space is in flux and premature to characterise.

## 10. Success criteria

This track succeeds if, at the end, it can answer four questions clearly:

1. Does the repo's framework produce actionable guidance across the nine healthcare sub-domains, or are there sub-domains where it fails structurally?
2. Where does the regulatory perimeter end, and what does the delegation framework need to cover on its own in those gaps?
3. Which healthcare-specific failure patterns are captured by the existing incident taxonomy (Amodei-2016 + Weidinger-2022) and which require new categories?
4. What is the healthcare-specific verification infrastructure equivalent of the scale-based track's "productization infrastructure" finding?

If the answers to all four can be stated in one paragraph each in `synthesis.md` with evidence-graded support, the track has delivered.
