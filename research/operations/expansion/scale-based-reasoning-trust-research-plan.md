# Research Plan: Reasoning Trust Verification Across Organizational Scales

status: active
date_created: 2026-04-13
date_expanded: 2026-04-13
purpose: Restructure the reasoning trust verification research agenda around organizational scale, from international institutions and governments to solo entrepreneurs, so that the framework can be tested, tailored, and critiqued where verification conditions differ most. This expanded plan adds an explicit comparative analysis framework, shared coding instruments, per-dimension research questions, and a cross-tier synthesis methodology capable of producing publishable findings.

---

## 1. Why Restructure Around Scale

The existing project has a strong framework for *when* AI should be used at different authority levels and a new direction targeting *how* decision-makers should verify AI reasoning. Both lines of work have so far spoken to a generic "business decision-maker" — implicitly a mid-to-large enterprise with some governance apparatus and some human slack for verification.

That generic framing hides the most consequential question a reasoning verification framework must answer: **who actually pays the verification tax, and is paying it feasible at their scale?**

A reasoning verification method that depends on committees, red teams, or dedicated reviewers will be irrelevant to a solo founder and unworkable for a three-person legal clinic. A method that relies on a single individual's attention will fail to bind an international regulatory body whose legitimacy rests on inter-institutional accountability. The same framework must therefore be evaluated, adapted, and in some cases explicitly bounded across scales.

The restructuring is not a rebrand. It forces the framework to meet organizations where they are, rather than assuming a middle tier that hosts only a fraction of real AI-assisted decisions. And — critically for what the user has asked this plan to produce — it turns every observation into a comparative observation, because the research value now comes from cross-tier contrast rather than from any single tier's description.

---

## 2. Preliminary Search Findings

### 2.1 What the literature already covers

| Scale tier | Literature coverage | Representative sources |
| --- | --- | --- |
| International institutions | Thin. Focus is on *compliance* verification between states, not reasoning verification in decision-making. | Oxford AIGI "Verification for International AI Governance" (2025); ITU AI Standards for Global Impact (2025); proposed World Council for Cooperative Intelligence |
| National governments / public sector | Medium. Emphasis on procurement, traceability, and adaptive regulation; little on reasoning inspection by civil servants. | GAO-25-107933; OECD *Governing with AI* (2025); OECD AI Capability Indicators (2025); GSA AI Guide for Government; Deloitte public-sector trends 2026 |
| Regulated industries and legal institutions | Rich but narrow. Focus is overwhelmingly on *hallucination detection* and professional liability, not on end-to-end reasoning verification. | Stanford HAI 2025 (17%+ legal model hallucination); ABA and state bar ethics guidance 2025-2026; 1,174+ documented courtroom incidents (April 2026); Lexology professional-responsibility commentary |
| Large corporations and multinationals | Dense. CAIO playbooks, three-tier governance committees, hub-and-spoke models, SOC 2, ISO 42001. | Microsoft Responsible AI Standard and AETHER; JPMorgan Model Risk Governance; OneTrust committee construction; Deloitte *State of AI in the Enterprise* 2026 |
| Mid-sized and small enterprises (SMEs) | Adoption-focused, governance-thin. Strong data on the adoption gap; very little on verification practice. | OECD *AI adoption by SMEs* (December 2025); ScienceDirect systematic review 2025; PLOS One 2025; TOE–DOI survey (MDPI 2025) |
| Startups and AI-native firms | Covered in this repository. Founder-driven, speed-prioritized, triggered by SOC 2, investor diligence, and incident response. | `research/extensions/adaptive-governance/startup-small-org-governance.md`; CB Insights; Y Combinator safety notes |
| Solo entrepreneurs and one-person businesses | Essentially absent. A handful of practitioner essays reference "verification tax" and responsibility designation, but no empirical or theoretical work. | *FractionalView* essay on the verification tax; *TrueFuture* 2026 small-business AI compliance guide |

### 2.2 Empirical signals that already decompose by scale

A small number of statistics already reveal scale-dependent behavior that the existing reasoning verification direction does not engage with:

- **AI use gap.** OECD 2025: 40% of large firms use AI versus 11.9% of firms with 10-49 employees.
- **Legal-profession gap.** In-house counsel at large corporations report 70% AI adoption; small and mid-sized firms report 22%.
- **Governance capacity gap.** Industry governance teams average 9 people; 17% of organizations have only one person responsible for AI governance.
- **Verification tax concentration.** At solo scale, the same person is the requester, evaluator, and accountable party — there is no division of cognitive labor to absorb verification effort.
- **Hallucination exposure.** 1,174+ judicial incidents involving AI hallucinations have been documented globally as of April 2026, overwhelmingly in smaller firms and pro se contexts where review processes were thinnest.
- **Oversight dissolution.** 66% of employees accept AI output without evaluation (Microsoft, 2025); 91% of executives agree employees overtrust AI (McKinsey, 2024-2025). Neither statistic is currently decomposed by firm size.

### 2.3 The real gap

No existing body of work asks the same reasoning verification question across the full scale spectrum using a consistent analytical lens. Three specific absences are striking:

1. **No comparative verification-capacity theory.** We have adoption-gap data and governance-structure case studies, but no framework that models *how much reasoning verification is feasible per decision per person* as a function of scale.
2. **No solo-scale empirical base.** The one-person business segment is economically significant (~$1.7T) but invisible to AI governance research.
3. **No scale-aware framework transfer.** The existing BCG-style reasoning verification heuristics (source grading, inference checking, normative fit, confidence calibration) were developed for large-team contexts. Nobody has tested whether they survive compression to a solo decision-maker or expansion to an international regulatory body.

These gaps map cleanly onto the project's core conviction: **without a reasoning verification method that is demonstrably feasible at the decision-maker's scale, "assist" and "recommend" modes collapse into de facto automation.** The scale-based restructuring is the way to harden and bound the framework.

---

## 3. Proposed Scale Taxonomy

The plan adopts a seven-tier scale taxonomy. Tiers are ordered by *verification-relevant structural properties*, not headcount alone.

| Tier | Scale | Defining structural property for verification | Illustrative actors |
| --- | --- | --- | --- |
| S7 | International institutions | Verification is a legitimacy problem across sovereign or cross-jurisdictional boundaries | UN, OECD, ITU, IMF, WTO, WHO, ICAO, cross-border standards bodies |
| S6 | National governments and public agencies | Verification is an accountability-to-the-public problem, constrained by procurement law, FOIA, and audit trails | Ministries, central banks, federal/state agencies, GAO-style audit offices |
| S5 | Regulated professions and legal institutions | Verification is a professional-liability problem bound to ethics codes | Law firms, medical practices, accountancies, licensed financial advisers |
| S4 | Large corporations and multinationals | Verification is distributed through governance apparatus | Fortune 500, global banks, Big Tech, pharma majors |
| S3 | Mid-sized enterprises | Verification is compressed into a few role holders | ~250-2,000 employees, regional banks, mid-market industrials, SaaS scale-ups |
| S2 | Small enterprises and startups | Verification is founder- or CTO-driven, ad hoc, incident-triggered | 10-250 employees, most Series A–C companies |
| S1 | Solo entrepreneurs and individual decision-makers | Verification is absorbed entirely by the decision-maker who also owns the outcome | 1-9 person businesses, independent consultants, freelancers, investors, sole practitioners |

**Why this cut.** Each tier has a qualitatively different answer to three questions the reasoning verification framework must address: (a) who performs the verification, (b) what sanction follows if verification is skipped, and (c) what infrastructure supports or obstructs verification. The tiers are cleanest where these three answers co-move. They blur at the boundaries, which is itself a research object — for example, the moment a Y Combinator startup lands a regulated-industry customer, it effectively ascends into S5 verification obligations without possessing S5 infrastructure.

**What it is not.** The taxonomy is not a claim that every organization at a given headcount behaves the same way. It is a *verification structural property* cut: organizations with similar verification burdens, capacities, and sanctions belong to the same tier regardless of label.

---

## 4. Comparative Analysis Framework

This section is the heart of the expanded plan. It defines the set of dimensions along which every tier will be investigated and compared. Without a shared dimension set, tier reports would drift into incomparable narratives. With it, every finding becomes a point in a comparative space.

### 4.1 Ten comparative dimensions

Every tier report must answer each of the ten dimensions below. The dimensions were selected because each one is (a) observable at every tier, (b) theoretically load-bearing for reasoning verification, and (c) expected to differ across tiers in a structured way.

**D1 — Verification agent identity.** Who is expected to verify AI reasoning? Are they the same person as the decision-maker, the requester, or the one held accountable? How many verifiers touch one decision?

**D2 — Verification infrastructure.** What tools, platforms, committees, templates, and workflows does the actor have access to? Is there a dedicated red team, an internal platform, a third-party review service, or only a browser and a text editor?

**D3 — Verification incentive structure.** Why would the actor actually verify? What is the expected reward for verification and the expected cost for skipping it? Is verification enforced by external sanctions, internal culture, or neither?

**D4 — Sanction gradient.** What happens when verification fails and a bad AI-sourced claim propagates to a real decision? Sanctions range from reputation loss to civil damages to criminal liability to international legitimacy loss. The gradient is steeper at some tiers than others.

**D5 — Verification trigger.** What event causes verification to happen? Options include: standing policy, risk classification, incident response, customer requirement, regulator demand, personal curiosity, or nothing at all. The *distribution* of triggers across decisions is the diagnostic quantity.

**D6 — Per-decision verification budget.** How much time, attention, and effort is actually available per decision? This is the raw input to the verification tax calculation. Typically measured in minutes of human attention and number of distinct sources consulted per decision.

**D7 — Delegation chain depth.** How many steps exist between the AI's output and the final decision? Each step is a potential site of verification and a potential site of collapse. At S1 the chain depth is zero; at S7 it can be dozens of steps long across committees, working groups, and ratification bodies.

**D8 — Failure mode profile.** What are the dominant failure patterns observed at this tier? At S1 it is probably passive acceptance. At S5 it is misgrounded citation. At S4 it is governance-theater. At S7 it is laundering of AI output through committee language. The profile is a fingerprint.

**D9 — Substitutes when full verification is infeasible.** When verification cannot be performed, what substitutes fill the gap? Examples: insurance, indemnity clauses, secondary model cross-checks, community reputation, delayed publication, narrative hedging, output throttling. These are under-theorized and potentially the most practically valuable finding of the research.

**D10 — Scale-crossing dynamics.** What happens when an organization moves up or down a tier — during rapid growth, acquisition, regulatory reclassification, or existential crisis? Does the verification practice move with it, lag behind, or snap?

### 4.2 Additional structural fields (metadata, not dimensions)

To enable cross-tier aggregation, each tier report records a small set of structural fields:

- **Evidence strength grade** (A/B/C/D) for each dimension based on how much external evidence supports the finding.
- **Source typology** indicating whether the finding is drawn from academic literature, regulatory documents, industry case studies, practitioner testimony, or internal repository work.
- **Known exemplars** — two or three named organizations whose behavior illustrates the tier's typical pattern.
- **Known counterexamples** — one or two named organizations whose behavior contradicts the tier's typical pattern, used to prevent over-generalization.
- **Date currency** — the newest and oldest sources cited, so downstream readers know the temporal window.
- **Open questions** — three to five questions the tier report could not answer and that would require future primary work.

### 4.3 The comparative matrix

When every tier report is complete, the findings fold into a single 7×10 comparative matrix (seven tiers × ten dimensions). The matrix is the primary synthesis artefact. Each cell contains the tier's answer on that dimension with evidence grade attached. Rows read as tier profiles; columns read as dimension gradients across scale.

The matrix enables three kinds of analysis:

1. **Horizontal reading** produces a tier profile — a fingerprint of how reasoning verification actually happens at that scale.
2. **Vertical reading** produces a dimension gradient — how, for example, verification agent identity collapses as scale shrinks.
3. **Diagonal reading** surfaces co-variance — whether dimensions move together in ways that suggest deeper underlying structure (e.g., D6 and D8 probably co-vary inversely: smaller budget, richer failure profile).

### 4.4 The verification capacity curve

From dimensions D6, D7, and D8 the plan constructs a single quantitative artefact called the verification capacity curve. It expresses, for a given tier, the maximum number of BCG-style reasoning verification steps that can be applied per decision per person without breaking the actor's available attention budget.

Curve inputs:

- **Effective attention per decision** (minutes) — estimated from interviews, diary studies, and document traces.
- **Required attention per verification step** (minutes per step) — empirically estimated from the coding scheme defined in §5.
- **Number of reviewers available per decision** — from organizational structure data.
- **Verification discipline compression factor** — a qualitative coefficient for how much verification fidelity is preserved when the actor has less attention than a full BCG-style review demands.

Curve outputs:

- A step-count ceiling per tier that tells the reader how many of the framework's verification disciplines survive at that scale.
- A breakpoint — the tier below which at least one of the five framework disciplines (source quality, inferential validity, normative acceptability, confidence calibration, failure mode awareness) cannot be performed at all.
- A public-good threshold — the tier below which private verification effort is dominated by externally provided verification infrastructure, bearing directly on the framing question in §4.5.

### 4.5 The framing question (revised)

**Is reasoning verification a scale-dependent public good that cannot be privately produced below a certain tier, and if so, what is the infrastructure substitute?**

The expanded version adds the constructive half. If reasoning verification fails as a private discipline below some tier, the research must also propose what replaces it. Candidates already visible in the literature include: third-party verification services, AI-supplied reasoning audits, mandatory disclosure regimes, insurance-backed review, peer networks, and regulatory dashboards. The plan commits to producing at least a candidate design for each tier that falls below the public-good threshold.

---

## 5. Data Collection and Coding Instruments

This section specifies the shared instruments used at every tier so that outputs are comparable. The goal is to prevent drift between tier reports that would make the §4 matrix unreliable.

### 5.1 Reasoning verification coding scheme (RVCS-1)

A shared coding instrument applied to any AI-assisted decision or document found during research. RVCS-1 has five scored fields corresponding to the framework's five verification disciplines:

| Code | Discipline | Scoring rule |
| --- | --- | --- |
| Q1 | Source quality assessment | 0 = no source review, 1 = unfiltered sources accepted, 2 = some source grading, 3 = domain-appropriate source grading applied |
| Q2 | Inferential validity | 0 = none, 1 = surface consistency only, 2 = step-by-step inference check, 3 = adversarial challenge to the inference chain |
| Q3 | Normative acceptability | 0 = none, 1 = generic ethics statement, 2 = domain-specific norm check, 3 = external reference to regulation or professional code |
| Q4 | Confidence calibration | 0 = confidence level is accepted verbatim, 1 = confidence is hedged without mechanism, 2 = confidence is adjusted based on evidence, 3 = explicit calibration against a known base rate or track record |
| Q5 | Failure mode awareness | 0 = not considered, 1 = hallucination mentioned, 2 = multiple failure modes considered, 3 = tier-appropriate failure catalog consulted |

A decision-level RVCS-1 score is the sum of Q1–Q5 (range 0–15). It is deliberately coarse because the downstream use is comparison, not precision measurement. Any tier report that applies RVCS-1 records the scores alongside the raw evidence, so that later coders can re-score.

### 5.2 Verification tax instrument (VTI)

A per-decision time and effort estimator. Four fields:

- **T_total** — minutes spent on the decision, from receipt of AI output to final commitment.
- **T_verify** — minutes of that total spent explicitly on verification, including source lookup, crosschecks, challenge, and calibration.
- **N_reviewers** — number of distinct human reviewers who touched the decision before commitment.
- **N_sources** — number of independent sources consulted to check claims in the AI output.

The verification tax for a decision is reported as the triple (T_verify / T_total, N_reviewers, N_sources). It is designed so that S1 tier reports can populate it from diary entries and S7 tier reports can populate it from document traces of committee deliberations.

### 5.3 Failure incident coding scheme (FICS-1)

A shared scheme for any AI-assisted decision failure found during research. Eight fields:

- Organization and tier
- Year
- Decision domain
- AI tool involved
- Failure class (fabrication, misgrounding, specification gaming, sycophancy, overconfidence, misapplication, other)
- Verification step skipped (by RVCS-1 code)
- Sanction outcome
- Public disclosure level

FICS-1 is applied to the 1,174+ documented legal-AI hallucination cases at S5 and to any other failure corpus the research surfaces. The S5 legal incident coding is expected to generate the richest FICS-1 dataset and will anchor cross-tier comparison.

### 5.4 Exemplar case template

A fixed-length template for each named exemplar in a tier report:

- One-paragraph description of the organization and the AI-assisted decision context
- RVCS-1 score for a representative recent decision
- VTI triple for that decision
- One paragraph on what this exemplar illustrates about the tier
- Three primary sources supporting the description

Every tier report produces two to three exemplar cases. Cross-tier comparison pulls exemplar cases side by side.

### 5.5 Evidence grading rubric

For every claim in a tier report, an evidence grade is assigned:

- **A** — direct empirical evidence from a primary source (regulator report, peer-reviewed study, audited document, named interview).
- **B** — indirect but credible evidence from practitioner reporting or secondary analysis by a reputable outlet.
- **C** — inferred from adjacent evidence, consistent with but not directly supported by primary sources.
- **D** — speculative extrapolation. Permitted only where the report explicitly flags it and justifies why extrapolation is better than silence.

No cell in the §4.3 comparative matrix is allowed to be populated from D-grade evidence without an accompanying note saying so.

---

## 6. Tier-Specific Research Plans

Each tier has its own plan below. The plans reuse the §4 comparative dimensions and the §5 instruments so that outputs are comparable. Every tier plan has the same shape: question, method, exemplars, deliverable, risks.

### 6.1 Tier S7 — International institutions

- **Question**: When an international body adopts an AI-generated assessment (trade dispute analysis, pandemic risk forecast, climate policy brief), what reasoning verification discipline is actually applied before it enters a resolution, communiqué, or binding instrument?
- **Primary method**: document genealogy of three AI-informed international deliverables from raw model output to final publication, coded with RVCS-1 and VTI.
- **Candidate exemplars**: OECD AI Capability Indicators 2025-2026 workstream; ITU AI Standards for Global Impact initiative; WHO pandemic AI-assisted analysis; IMF GenAI use cases in Article IV consultations.
- **Deliverable**: `research/extensions/scale-based/s7-international-institutions.md`
- **Key risks**: institutional access likely unavailable for interviews; reliance on public documents risks cherry-picking.

### 6.2 Tier S6 — National governments and public agencies

- **Question**: Does existing administrative review infrastructure (impact assessments, procurement review, FOIA audit trails) create a native surface for reasoning verification, or does it only capture outputs while leaving inferential chains invisible?
- **Primary method**: systematic review of GAO, NAO, OECD, and ENISA reports on AI use in government 2024-2026, plus comparative policy mapping of three jurisdictions (US federal, EU member state, Singapore).
- **Candidate exemplars**: US federal AI inventory and IT Dashboard; UK AI Safety Institute evaluation workflow; Singapore IMDA AI Verify toolkit; Estonia x-road and Kratt AI-enabled services; Korea AI Basic Act implementation.
- **Deliverable**: `research/extensions/scale-based/s6-national-governments.md`
- **Key risks**: government reporting is uneven in depth; public-facing documents may overstate rigor.

### 6.3 Tier S5 — Regulated professions and legal institutions

- **Question**: Do the existing professional ethics rules actually define a reasoning verification method, or do they delegate it to individual judgment, and how does the answer differ between large and small firms within the same profession?
- **Primary method**: incident corpus analysis of documented legal-AI hallucination cases (targeting a sample of ~100) coded with FICS-1; ethics rule synthesis for law, medicine, accounting, and licensed financial advice; comparative analysis across firm sizes within the profession.
- **Candidate exemplars**: *Mata v. Avianca* case and comparables; ABA Formal Opinion 512; AICPA SAS 145 on risk assessment; FDA CDRH Good Machine Learning Practice; Korea FSC AI-finance review guidance.
- **Deliverable**: `research/extensions/scale-based/s5-regulated-professions.md`
- **Key risks**: incident corpus is built from public aggregators of uncertain completeness; non-legal professions have weaker public incident records.

### 6.4 Tier S4 — Large corporations and multinationals

- **Question**: Do the three-tier committee structures that large corporations deploy actually produce reasoning verification, or do they produce deployment gating while the actual verification collapses at individual desks?
- **Primary method**: reframe existing repository material (`caio-governance-construction.md`, `industry-practice-survey.md`, `governance-trend-analysis.md`) through the §4 dimension set; contrastive case pair of one substantive and one performative verification structure.
- **Candidate exemplars**: Microsoft AETHER; JPMorgan Model Risk Governance; Unilever decision-mesh; Siemens responsible AI council; Samsung SDS governance lifecycle.
- **Counterexamples**: Meta disbanding its RAI team and automating 90% of risk assessment; Stability AI's governance collapse.
- **Deliverable**: `research/extensions/scale-based/s4-large-corporations.md`
- **Key risks**: repository material is recent and rich, so the risk is confirmation bias when reframing.

### 6.5 Tier S3 — Mid-sized enterprises

- **Question**: Mid-sized firms have the verification need of S4 and the verification capacity of S2. Which verification disciplines survive the compression, which collapse, and what substitutes fill the gap?
- **Primary method**: literature synthesis using TOE–DOI studies (MDPI, PLOS One, tandfonline 2024-2025); structured case search in Harvard Business Review, BCG, McKinsey outputs for mid-sized firm AI adoption; targeted web research for named mid-sized exemplars.
- **Candidate exemplars**: FAIGMOE midsize GenAI framework; Katch AI deployment at mid-market German industrials; mid-tier accounting firms adopting Thomson Reuters CoCounsel at firm rather than enterprise tier.
- **Deliverable**: `research/extensions/scale-based/s3-mid-sized-enterprises.md`
- **Key risks**: mid-sized firms are the least documented tier in both academic and practitioner literature; dependence on inferred evidence will push several dimensions into C-grade.

### 6.6 Tier S2 — Small enterprises and startups

- **Question**: At what point in the startup lifecycle does reasoning verification become a standing practice, and what triggers the transition?
- **Primary method**: reframe existing repository material (`startup-small-org-governance.md`, `adoption-barrier-implications.md`, Anthropic/OpenAI governance sections); event trace of 3-5 publicly documented startup AI incidents; targeted research on SOC 2, ISO 42001, and VC diligence pressure.
- **Candidate exemplars**: Anthropic Long-Term Benefit Trust and RSP; Harvey AI legal workflow verification; Cursor / Windsurf code-generation audit patterns; Stability AI governance collapse as counterexample.
- **Deliverable**: `research/extensions/scale-based/s2-small-enterprises-startups.md`
- **Key risks**: startup behavior changes quickly; findings may age within months.

### 6.7 Tier S1 — Solo entrepreneurs and individual decision-makers

- **Question**: Is reasoning verification even possible when the verifier, requester, decision-maker, and accountable party are the same individual, or does the framework need a substantively different offering at this tier?
- **Primary method**: literature-based scan for practitioner accounts; tool audit cataloguing verification tools actually accessible to an S1 user (browser-based fact checkers, second-model crosschecks, community review surfaces, paid services); design outline for a future diary study and think-aloud protocol; careful use of existing survey data where it touches solo operators.
- **Candidate exemplars**: solo attorneys citing AI tools in court filings; independent financial advisers using AI research copilots; solo medical practitioners using AI intake tools; one-person SaaS founders using AI product decisions; retail investors using AI trade ideation.
- **Deliverable**: `research/extensions/scale-based/s1-solo-entrepreneurs.md`
- **Key risks**: literature is essentially empty; the tier report will rely more than any other on inferred and extrapolated evidence, and must say so clearly.

---

## 7. Cross-Tier Synthesis Methodology

The cross-tier synthesis is the single most valuable output of the plan. Without it, the seven tier reports are just seven disconnected case sets. This section defines how the synthesis is produced so that it can be replicated or challenged later.

### 7.1 Synthesis inputs

1. The seven tier reports, each populated against the §4 dimensions and §5 instruments.
2. The 7×10 comparative matrix assembled from the tier reports.
3. The verification tax instrument outputs for each tier, feeding the §4.4 capacity curve.
4. The failure incident corpus from S5 (and any smaller corpora from other tiers), coded with FICS-1.
5. Existing repository material from the adaptive-governance, delegation, and reasoning-trust workstreams.

### 7.2 Synthesis procedures

**Procedure 1 — Dimension gradients.** For each of the ten dimensions, read the column of the matrix top to bottom (S7 to S1) and write a short narrative describing the gradient. Flag where the gradient is monotonic, where it inverts, and where it is discontinuous. Monotonic gradients suggest scale laws; inversions and discontinuities suggest tier-specific structural factors worth investigating.

**Procedure 2 — Tier profiles.** For each tier, read the row and write a one-paragraph fingerprint: the verifier, their infrastructure, their incentive, their dominant failure, and their substitutes. Tier profiles are the text form of the verification-capacity curve.

**Procedure 3 — Framework portability matrix.** For each of the five reasoning verification disciplines (source quality, inference validity, normative acceptability, confidence calibration, failure mode awareness), evaluate whether the discipline is (a) fully portable across the tier, (b) portable with tier-specific adaptation, (c) impossible at this tier without infrastructure, or (d) structurally incoherent at this tier. Output is a 5×7 discipline-by-tier table.

**Procedure 4 — Failure mode map.** Combine the FICS-1 outputs with the tier profiles. For each failure class (fabrication, misgrounding, specification gaming, sycophancy, overconfidence, misapplication), identify which tiers are most exposed and why. The output is a ranked failure vulnerability list per tier plus a cross-tier matrix of which failure classes concentrate where.

**Procedure 5 — Scale-crossing dynamics.** Identify three transitions: S2→S4 (fast growth), S4→S5 or S4→S6 (regulatory escalation), S1→S2 (first hire). For each transition, describe what verification practice change should occur, what actually happens, and what governance friction results. This is the most practically relevant synthesis output for policy audiences.

**Procedure 6 — Answer to the framing question.** Given the capacity curve, the portability matrix, and the failure map, produce a first explicit answer to the §4.5 framing question. The answer takes one of three forms: yes (reasoning verification is a public good below tier X), no (verification is private at all tiers with tier-specific adaptation), or conditional (verification is private above tier X and infrastructure-dependent below it). Every form of answer must be accompanied by the evidence base and the confidence level.

### 7.3 Synthesis outputs

- **`research/extensions/scale-based/cross-tier-synthesis.md`** — the narrative synthesis document containing Procedures 1-6.
- **`research/extensions/scale-based/comparative-matrix.md`** — the 7×10 comparative matrix with evidence grades.
- **`research/extensions/scale-based/verification-capacity-curve.md`** — the quantitative curve with its inputs, assumptions, and sensitivity notes.
- **`research/extensions/scale-based/framework-portability.md`** — the 5×7 discipline-by-tier portability table.
- **`research/extensions/scale-based/README.md`** — the track navigation guide so that the synthesis can be read in isolation.

---

## 8. Deliverables

### 8.1 Research artefacts

1. **Seven tier-specific reports**, one per scale tier, each answering its tier-specific question from §6 and populating the §4 dimensions.
2. **Cross-tier comparative matrix**, the 7×10 table described in §4.3.
3. **Verification capacity curve**, the quantitative artefact described in §4.4.
4. **Framework portability matrix**, the 5×7 table described in §7.2 Procedure 3.
5. **Cross-tier synthesis narrative**, the document produced by §7 Procedures 1-6.
6. **Scale-aware framework revision** — an update to the reasoning verification framework in `research/core/framework/` with explicit scope notes for each tier.
7. **Updated MEMORY.md index entry** so future conversations can find this track.

### 8.2 Publishable outputs

- **Paper candidate 1**: *The Verification Tax Across Organizational Scales: Who Actually Pays for Reasoning Verification in AI-Assisted Decisions*. Target venues: CHI, CSCW, FAccT.
- **Paper candidate 2**: *The Legal Profession's Reasoning Verification Crisis: A Firm-Size Analysis of AI Hallucination Incidents*. Target venues: Stanford HAI, Harvard Law Review online.
- **Paper candidate 3**: *Solo Founders and the Verification Floor: An Empirical Account of One-Person Reasoning Verification*. Target venues: ICIS, HICSS, Academy of Management Discoveries.
- **Policy brief**: *A Scale-Aware Reasoning Verification Framework for AI-Assisted Business Decisions*. Target audience: OECD AI, NIST, Singapore IMDA.

### 8.3 What the plan explicitly does not claim

- It does not claim that a single framework will serve all seven tiers. The cross-scale synthesis may conclude that the framework is structurally infeasible at S1 and must be replaced by infrastructure rather than discipline.
- It does not claim comprehensive coverage of every sub-industry within a tier.
- It does not commit to resolving the framing question in §4.5 definitively. The honest answer may be "we do not yet know" and the plan is prepared to report that outcome.
- It does not promise primary fieldwork at tiers S5, S6, or S7 in this research cycle. Those tiers rely on document, incident, and literature analysis.

---

## 9. Sequencing

### Wave 1 — Foundation (this session, complete)

- Expanded plan with comparative framework, instruments, and tier plans.
- Directory structure for `research/extensions/scale-based/`.
- Initial literature scan for each tier.

### Wave 2 — Parallel tier research (this session)

- Seven tier reports produced in parallel using the §4 dimensions and §5 instruments.
- Each report anchors its findings in at least two exemplars and grades its evidence.
- Reports written to `research/extensions/scale-based/s{N}-*.md`.

### Wave 3 — Synthesis (this session)

- Comparative matrix assembled from tier reports.
- Verification capacity curve computed from dimensions D6, D7, D8.
- Framework portability matrix computed.
- Synthesis narrative written.
- Track README and commit.

### Wave 4 — Future work (beyond this session)

- Primary empirical at S1: diary study + think-aloud protocol with solo founders, licensed professionals, and retail investors.
- Primary empirical at S5: expand FICS-1 coding to 300+ legal incidents and run practitioner interviews across firm sizes.
- Primary empirical at S3: survey mid-sized enterprises with a decision-diary instrument.
- Institutional access work at S7: direct outreach to OECD AI, ITU, IMF for interview access.
- Framework revision and paper drafting.

---

## 10. Risk Register

| Risk | Likelihood | Severity | Mitigation |
| --- | --- | --- | --- |
| Tier drift — reports lose comparability | Medium | High | Enforce §4 dimensions and §5 instruments as hard requirements for every tier report |
| Over-reliance on grade-C evidence at S1, S3, S7 | High | Medium | Explicitly grade each cell in the comparative matrix; flag C and D cells in the synthesis |
| Confirmation bias when reframing existing repository material (S2, S4) | Medium | Medium | Include counterexamples in each reframed tier report; contrastive case pairs at S4 |
| Legal incident corpus is non-exhaustive | High | Low | Treat the corpus as a large but non-random sample; note generalizability limits |
| Framing question resists resolution | Medium | Low | Plan accepts "we do not yet know" as a valid outcome, with caveat that the plan commits to a tentative answer with stated confidence |
| Rapid landscape change (startup and professional practice) | High | Medium | Date-stamp every tier report; treat findings as a 2025-2026 snapshot |
| Scope creep in synthesis | Medium | Medium | Synthesis procedures 1-6 are fixed; no new procedures without explicit plan revision |

---

## 11. Connection to the Existing Project

This plan does not replace existing workstreams. It re-weights them and adds a fourth layer:

- The delegation calibration framework (Phases 00-20) remains the authority-assignment layer and continues to define *when* to use AI.
- The reasoning trust verification direction (2026-03-28) remains the quality-assessment layer and continues to define *how* to verify AI reasoning.
- The adaptive governance extension (Phase 21) remains the currency layer and continues to define *how governance stays up to date*.
- The scale-based restructuring adds the fourth layer: *who can actually perform verification, and with what infrastructure, at their scale*.

Existing documents already map onto the plan:

- `caio-governance-construction.md` → S4 material, ready to reframe
- `startup-small-org-governance.md` → S2 material, ready to reframe
- `industry-practice-survey.md` → S3-S4 material, needs decomposition
- `speed-gap-analysis.md` and `adaptive-governance-summary.md` → cross-cutting context for S4-S7
- `reasoning-trust-landscape.md` and the `core/framework/` documents → the framework to be scale-tested

The novel contributions are S1, S5, S6, and S7, plus the cross-scale synthesis.

---

## 12. Immediate Next Steps (in-session execution)

1. Launch parallel tier research, one agent per tier (S1-S7), with each agent producing its tier report against the §4 dimensions and §5 instruments.
2. Assemble the 7×10 comparative matrix and verification capacity curve from the tier reports.
3. Produce the cross-tier synthesis narrative.
4. Create the track README and update MEMORY.md pointer.
5. Commit the whole track in one commit: `research: scale-based reasoning trust verification — 7 tier reports plus synthesis`.
