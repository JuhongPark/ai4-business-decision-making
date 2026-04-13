# 7×10 Comparative Matrix

status: research_complete
date: 2026-04-13
purpose: The primary cross-tier synthesis artefact. Each cell summarises a single tier's answer on a single dimension, drawn directly from the tier reports. Read horizontally for tier profiles; read vertically for dimension gradients.

---

## How to read this document

Every cell contains three elements: **a concise answer**, an **evidence grade** (A–D) inherited from the tier report, and (where available) a **representative RVCS-1 score anchor**. The matrix is not a substitute for the tier reports; it is a compression layer that makes the tier reports comparable at a glance. When any cell requires nuance or a counterexample, the reader is pointed back to the relevant tier report.

The tiers are ordered top to bottom from largest (S7) to smallest (S1) because the most instructive reading is top-down — watching each dimension either hold, adapt, substitute, or collapse as organisational scale shrinks.

---

## D1 — Verification agent identity

| Tier | Who actually verifies the AI's reasoning | Evidence | Anchor |
|---|---|---|---|
| S7 | Layered standing committees and working parties (OECD AIGO, IMF Executive Board, IPCC review editors, UN Scientific Panel 40-member board) — never a single individual | A | OECD AI Capability Indicators: 57 reviewers |
| S6 | Distributed across five roles with distinct legal bases: contracting officers, CAIOs and AI Governance Boards, data-protection / equality officers, supreme audit institutions, the public via FOIA | A | UK ATRS DWP fraud-scoring: 1 case officer + periodic sample |
| S5 Big Law | Four-layer manufactured pipeline: drafting associate, cite-check paralegal, senior associate, partner sign-off | A | Harvey workflow: 3–4 reviewers |
| S5 Solo | The same person who drafted, billed, and signs | A | Sanctioned solo attorneys: 1 reviewer |
| S4 substantive | Sensitive Uses committee, Model Risk Governance, multi-disciplinary review boards, FDA-forced embedded review | A | Microsoft Sensitive Uses: 6–12 reviewers |
| S4 typical | Nominally the apparatus; actually the individual analyst at the desk | B | JPMorgan LLM Suite: 230,000+ daily users, no per-decision checkpoint |
| S3 | One role-compressed individual absorbing the entire verification stack as a side duty — usually CIO, General Counsel, or Chief Privacy Officer | A | IAPP 2024: 17% of orgs have one person responsible |
| S2 AI-native | Small, lean but real safety stack (Anthropic Alignment Science, Frontier Red Team, Responsible Scaling Officer) | A | Anthropic: 15–30 reviewers for capability cycle |
| S2 AI-using | CTO or co-founder with one or two informal reviewers; no separation of requester, verifier, and accountable party | A/B | Harvey internal: 1 reviewer |
| S1 | Verifier, requester, decision-maker, and accountable party converge on one person; N_verifiers = 1 by definition | A | Solo founder shipping landing page: 1 |

**Vertical reading**: The number of distinct verifiers collapses monotonically from dozens (S7) to one (S1), except at S4 where the documented number (one, at the desk) is *lower* than S2 AI-native firms, which keep dedicated alignment teams. The "more apparatus = more verifiers" intuition is wrong — an S4 Copilot user has fewer verifiers per decision than an Anthropic capability evaluation.

---

## D2 — Verification infrastructure

| Tier | Tools, platforms, committees, workflows | Evidence | Anchor |
|---|---|---|---|
| S7 | Standing committees; expert-comment portals (IPCC); document genealogies; OECD AI Incidents Monitor (29 criteria, 8 dimensions); ITU/ISO/IEC AI Standards Exchange Database (870+ standards); Oxford AIGI hardware verification proposal (future) | A | — |
| S6 | System-level dense: US federal use-case inventory, UK ATRS, EU Annex III registry, Korea high-impact AI register, Singapore AI Verify open-source toolkit. Decision-level sparse: FRIA template (unpublished final), APA reasoned-decision analogy, agency-internal logs not FOIA-readable | A | Singapore AI Verify (12/15 RVCS-1) = high water mark |
| S5 Big Law | Deployment SOPs (DLA Piper "audit the robots"), grounded-tool stack (Harvey, CoCounsel, Thomson Reuters Westlaw Precision), cite-check layer, partner sign-off | A/B | — |
| S5 Solo | General-purpose ChatGPT / Gemini free tier; no SOP, no grounded tool, no reviewer layer | A | — |
| S4 substantive | Rich at deployment layer and at narrow high-touch review programs (Microsoft Sensitive Uses, JPMorgan Model Risk Management with patented bias audit, GE HealthCare FDA-embedded pipeline) | A | Microsoft AETHER + Sensitive Uses |
| S4 typical | Rich at deployment (OneTrust, Credo AI, Fiddler, Arthur AI, ServiceNow); thin or absent at reasoning layer; no industry-standard per-output tool | A/C | — |
| S3 | Vendor compliance artifacts substitute for infrastructure: SOC 2 Type II, ISO 42001 (USD 180–320K), vendor model cards, cyber insurance, compliance automation (Vanta/Sprinto/Drata) | A | Mid-market governance spend is outsourced |
| S2 AI-native | Internal eval harnesses, automated red-teaming (Anthropic Petri), capability evaluation against ASL thresholds, 3–6 month risk reports | A | Anthropic RSP v3.0 |
| S2 AI-using | Browser, GitHub, Slack, Vanta/Sprinto/Drata for SOC 2, Trust Centers for sales | B | — |
| S1 | A browser, two or three chatbots, a search engine, occasionally Perplexity, possibly one paid review service per quarter | B | — |

**Vertical reading**: Infrastructure intensity is non-monotonic. S7 and S4 substantive have dense verification infrastructure of different kinds; S4 typical is a cliff because the apparatus was built for deployment gating rather than reasoning verification. S3 has no native infrastructure at all — everything is rented from vendors. S2 AI-native's infrastructure is lean but purpose-built, scoring almost as high as S4 substantive.

---

## D3 — Verification incentive structure

| Tier | Why they would verify | Evidence | Anchor |
|---|---|---|---|
| S7 | Diplomatic legitimacy (member-state veto power), inter-institutional reputation, scientific independence when chair is named publicly (Bengio) | B | International AI Safety Report 2025 |
| S6 | Civil-service incentives actively oppose per-decision verification (throughput pressure); senior officials face career risk only after scandal; no reward for catching errors early | B | Toeslagenaffaire escalation pattern |
| S5 Big Law | Firm reputation, malpractice exposure, Rule 11 sanctions, partner's personal bar license | A | Partner sign-off ritual |
| S5 Solo | Personal malpractice / bar sanction — high in theory, psychologically distant under time pressure | A | 89.9% of court hallucination cases are solo/small firms |
| S4 substantive | External pressure (FDA, EU AI Act, ISO 42001 procurement), investor rewards for CAIO appointments, D&O insurance scrutiny | A | S&P 500 AI-citing earnings → +13.9% vs +5.7% |
| S4 typical | Deployment-gate incentives are real; user-level incentives are cultural and largely absent | A/B | 66% of employees accept AI output without checking |
| S3 | External (SOC 2, ISO 42001 buyer demand, regulatory pressure); internal governance is symbolic | A | 66% of B2B buyers demand SOC 2 before AI vendor |
| S2 AI-native | Mixed: genuine commitment but fragile under compute competition (Superalignment dissolution) | A | OpenAI Leike "sailing against the wind" |
| S2 AI-using | Negative incentive dominates — verification slows shipping, shipping is existential | B/C | — |
| S1 | Privately costly, privately beneficial; weak except catastrophic tail | C | — |

**Vertical reading**: At every tier, endogenous incentives to verify reasoning are weaker than incentives to ship or comply. Where substantive verification exists, it was forced from outside (regulator, contract, FDA, court order). The project's implicit assumption that "users want good reasoning" does not survive this column.

---

## D4 — Sanction gradient

| Tier | What happens when verification fails | Evidence | Anchor |
|---|---|---|---|
| S7 | Diffuse, politically severe but non-legal: legitimacy loss (US withdrawal from 2026 AI Safety Report), competing institution publication, donor fund reallocation | A | Time coverage 2026 |
| S6 | Steepest theoretical gradient, back-loaded: internal review → supreme audit findings → parliamentary hearings → judicial review → regulatory fines (EU AI Act up to EUR 15M / 3% turnover) → royal commission / criminal referral | A | Robodebt Royal Commission |
| S5 Big Law | Firm insurance, Rule 11, firm-level reputational damage; partners have personal exposure | A | Morgan & Morgan $5,000 |
| S5 Solo | Same sanctions as Big Law with zero institutional cushion: personal bar discipline, malpractice, license suspension, fines up to $110K (Brigandi) | A | $145K cumulative Q1 2026 solo sanctions |
| S4 substantive | FDA enforcement, EU AI Act fines up to 7% turnover, class-action, SR 11-7 examination findings | A | AI incidents +56.4% YoY (Stanford HAI 2025) |
| S4 typical | Sanctions attach to the institution regardless of individual verification; absorbed into the apparatus | B | Air Canada chatbot liability |
| S3 | High regulatory exposure, low internal visibility; failures surface through customer complaints, press, or litigation | A | Ellis George / K&L Gates $31,100 |
| S2 AI-native | Investor sanctions immediate (Stability AI); regulatory sanctions rare but rising | A | Stability CEO ouster March 2024 |
| S2 AI-using | Steepest on survival-percentage basis: Clearview $100M+, Character.AI wrongful death litigation, DoNotPay $193K FTC | A | Nate Inc. SEC fraud charges |
| S1 | Bimodal: solo licensed professional faces full S5 gradient; non-licensed face narrow economic/reputational damage only | B/C | Brigandi $110K, Lake disbarment |

**Vertical reading**: Sanction severity does not map cleanly to tier. The steepest gradient is S5, not S7 or S6, because professional licenses create personal liability that committee structures launder at higher tiers. The most dangerous combination in the taxonomy is solo licensed professional at S1: full S5 sanctions with S1 verification capacity.

---

## D5 — Verification trigger

| Tier | What makes verification actually happen | Evidence | Anchor |
|---|---|---|---|
| S7 | Calendar-driven (annual Article IV, Ministerial Council, assessment cycles) and ratification-driven | A | IMF surveillance cycle |
| S6 | Four descending-volume mechanisms: procurement cycle, periodic inventory (M-25-21 / ATRS annual), complaint (FOIA / ombudsman), incident (media / audit). Missing: per-use trigger | A | OECD 2025 |
| S5 Big Law | Firm SOP mandatory at matter opening, cite-check at filing, partner sign-off at client delivery | A | — |
| S5 Solo | Personal curiosity or post-hoc recognition; not standing | A | Sanctioned cases: zero pre-filing trigger |
| S4 substantive | Risk classification threshold, regulator demand, contract counter-party, post-incident review | A | Microsoft Sensitive Uses intake |
| S4 typical | Deployment-side dense; reasoning-side nearly absent; dominant pattern is "no trigger" | A | 66% of employees: no trigger |
| S3 | Customer-driven (SOC 2 demand), vendor renewal, regulatory filing, post-incident | A/B | — |
| S2 AI-native | Capability threshold (Anthropic RSP), board committee briefings, enterprise customer requirement | A | Anthropic ASL-3 May 2025 |
| S2 AI-using | SOC 2 customer ask (~50%), regulated customer (~20%), investor diligence (~15%), public incident (~10%), founder-driven (~5%) | C | Vanta 2025 |
| S1 | Personal curiosity or visible error, not standing; fires less often as AI appears reliable | B | Parasuraman–Manzey 2010 |

**Vertical reading**: The trigger column exposes the structural collapse of "recommend" mode into de facto automation. At almost every tier, the modal trigger is external pressure, not internal discipline. Where triggers are calendar- or policy-driven (S7, S6, S5 Big Law, S4 substantive), verification happens in principle; where triggers are "personal curiosity" (S1, S4 typical, S5 solo), verification happens only accidentally.

---

## D6 — Per-decision verification budget

| Tier | Time / attention / effort available per decision | Evidence | VTI anchor |
|---|---|---|---|
| S7 | Person-years per flagship deliverable but minutes per individual claim; reviewers operate at document level, not claim level | B/C | T_verify/T_total ≈ 0.6–0.7 for deliverable; tiny per claim |
| S6 | Minutes for high-volume benefits adjudication; hours to weeks for regulatory enforcement; weeks to years for rulemaking | C | 0.1–0.2 benefits; 0.4–0.6 enforcement |
| S5 Big Law | 15–30% of associate time on a brief spent verifying | B | 0.20–0.30; 3–4 reviewers; 1 primary source per proposition |
| S5 Solo | Whatever is left after substantive work, typically <5% | B | ≈ 0; 1 reviewer; 0 sources |
| S4 substantive | 70–90% of total decision time spent verifying for a Sensitive Uses case | A | 0.70–0.90; 6–12 reviewers; 10–30 sources |
| S4 typical | 0–3 minutes on a 12–25 minute Copilot-assisted task | B/C | 0–0.15; 1 reviewer; 0–2 sources |
| S3 | 5% for high-volume chatbot output; 20% where implicit professional review is embedded (partner tax reviewer) | B | 0.05–0.20 |
| S2 AI-native | 50% for major capability cycles; near zero for routine product decisions | B | 0.50; 15–30 reviewers |
| S2 AI-using | Near zero for most product decisions | C | 0.05–0.15; 1 reviewer; 0–1 source |
| S1 | 30 sec–5 min routine; 20–30 min flagged high-stakes; floor for complete review (30–400 min/day) exceeds working day (360–480 min/day) | D | 0.05–0.15 routine; 0.20–0.40 high-stakes |

**Vertical reading**: Budget is the single most diagnostic dimension in the matrix. The mathematical impossibility at S1 (verification floor > working day) is the load-bearing fact for the public-good argument. Notice how the S4 typical budget is lower than the S3 partner-review budget: the governance apparatus absorbs budget at the committee level without delivering budget at the desk level.

---

## D7 — Delegation chain depth

| Tier | Number of steps between AI output and final decision | Evidence | Notes |
|---|---|---|---|
| S7 | 10+: model → staff analyst → drafting team → internal review → interdepartmental clearance → management → Executive Board → member-state consultation → standing working party → committee → ministerial endorsement → translation → publication | B | Each handoff loses inferential trace |
| S6 | 7–9: minister → permanent secretary → divisional director → branch chief → case officer → AI tool → vendor foundation model → underlying training data | A | Robodebt: warnings blocked from reaching ministers |
| S5 Big Law | 2–4: drafter → cite-checker → senior associate → partner | A | Each step is a verification opportunity |
| S5 Solo | 0–1: solo practitioner is the chain | A | — |
| S4 substantive | ~10 at deployment gating; 2–12 at Sensitive Uses review | A | Depth concentrated pre-deployment |
| S4 typical | ~10 at deployment gating; **1** at use (the analyst is the chain) | A | Asymmetric: long chain ends at the desk |
| S3 | 1–2 at use; compliance chain runs through vendor attestations | B | — |
| S2 AI-native | Flatter than S4: evaluation → red team → Responsible Scaling Officer → board notification | A | Compressed but real |
| S2 AI-using | 1–2 | B | — |
| S1 | **0**: AI output reaches decision in a single hop | A | Structurally distinct from every other tier |

**Vertical reading**: Chain depth collapses from ~10 at S7 to 0 at S1 but the collapse is not monotonic. S4 is the most diagnostic anomaly: the *pre-deployment* chain is one of the longest in the taxonomy, but the *at-use* chain is one of the shortest (1). Committee structures extend the chain upstream but not downstream. S1 is the only tier where chain depth is structurally zero.

---

## D8 — Failure mode profile

| Tier | Dominant observed failure patterns | Evidence | Most diagnostic incident |
|---|---|---|---|
| S7 | Committee laundering, false consensus, frozen evidence, non-representativeness, predicted citation contamination (Deloitte pattern) | B/C | Deloitte Australia A$440K fabricated citations |
| S6 | Discriminatory targeting (Toeslagenaffaire), statistical overreach to individuals (Robodebt), reasoning erasure under FOIA, procurement capture, scandal-cycle failure | A | Robodebt + Toeslagenaffaire |
| S5 | Misgrounding (real source cited for proposition it does not contain) dominates fabrication at Big Law; fabrication dominates at Solo | B | 1,174+ Charlotin cases, 7 of 8 coded incidents skip Q1 and Q5 |
| S4 | Decoupling (apparatus and need in different parts of same org), governance theater, approval pile-up → shadow AI, vendor AI blind spot (only 37% govern vendor AI), architectural-substitute reliance | A | Deloitte AU 2025 |
| S3 | Q1 and Q4 collapse first; Q5 weakest; Q2 survives only via pre-existing professional practice; Q3 substituted wholesale by vendor attestation | B | Ellis George / K&L Gates USD 31,100 |
| S2 | Q3 normative failures dominate (Character.AI, Clearview, DoNotPay, Cleo, Workado, Perplexity copyright); Q4 overconfidence (Humane); Q5 resource starvation (Superalignment) | A | Character.AI wrongful death + Texas AG + ban |
| S1 | Passive acceptance of fluent but unfaithful reasoning, citation fabrication, automation complacency drift, sycophantic loop reinforcement, isolation bias; compound: passive acceptance of a sycophantic answer that confirms the actor's prior | B/C | Hancock declaration, Brigandi $110K |

**Vertical reading**: Failure modes cluster by tier: the higher the tier, the more the failure is *social* (committee laundering, procurement capture, governance theater); the lower the tier, the more the failure is *cognitive* (passive acceptance, sycophantic loops, isolation bias). The S2 tier is anomalous — its dominant failure class is *normative* (Q3), not cognitive or social, because S2 firms reach scale before asking "should we do this at all?"

---

## D9 — Substitutes when full verification is infeasible

| Tier | What fills the gap | Evidence | Notes |
|---|---|---|---|
| S7 | Peer-institution deference, delegation to country experts, hedged language, footnote/annex offload, standards-exchange pointer | B | IPCC / IEA cross-citation |
| S6 | Categorical bans (EU AI Act prohibited practices), risk classification triage, pre-deployment testing (AI Verify, AISI), HITL fig leaf, sunset clauses, public consultation as process legitimacy | A | "Heavy ex ante + HITL fig leaf + reactive scandal handling" |
| S5 Big Law | Deployment SOP + grounded-tool stack (Harvey, CoCounsel) + cite-check layer + partner sign-off bottleneck | A/B | Manufactured human-review pipeline |
| S5 Solo | None substantial; insurance partially, which is now narrowing (Verisk exclusion Jan 2026) | A | — |
| S4 substantive | Bounded automation by design (Aladdin Copilot refuses to advise, Goldman mandatory reviewer, Stripe fraud), FDA HITL, insurance, continuous monitoring, architectural narrowing (Bloomberg GPT, Harvey, Aladdin Asimov) | A | AI liability insurance projected $29.7B by 2033 |
| S4 typical | Essentially none at the desk; shadow AI fills the gap | A | GenAI traffic +890% in 2024 |
| S3 | SOC 2 Type II, ISO 42001, vendor model cards, cyber insurance (with narrowing terms), outsourced audits, fast-follower strategy, compliance automation platforms | A | Substitution stack as a whole |
| S2 AI-native | AISI partnerships, model cards, third-party red-teaming, EU GPAI Code participation | B | Cohere hired Joelle Pineau August 2025 |
| S2 AI-using | SOC 2 / ISO 27001 / ISO 42001 badges, Trust Centers, D&O / cyber insurance, indemnity clauses, output throttling, rate-limited access | B | — |
| S1 | Second-model crosscheck, browser fact-checkers, community forums, occasional paid expert review, shrinking insurance | B | Tool audit (Section 7 of S1 report) |

**Vertical reading**: The substitutes column is the most practically valuable column in the matrix. It is where the honest answer lives. Substitutes are *risk transfer* mechanisms, not *verification* mechanisms — they reduce the probability that a failure will be *the actor's responsibility*, not the probability that a failure will *occur*. This distinction is the crucial conceptual move for the framework.

---

## D10 — Scale-crossing dynamics

| Tier | What happens at tier boundaries | Evidence | Most consequential |
|---|---|---|---|
| S7 | Rare inter-tier movement; the consequential dynamic is *downward propagation* (S7 → S6 → S4 → S3 via legitimacy laundering). Weak-evidence S7 claims become binding national law with lighter scrutiny | C | 47 OECD AI Principles adherents |
| S6 | Downward to S5/S4/S3 via grants and cascading law; upward to S7 via coordination; sideways via extraterritoriality; vendor-mediated convergence via the three-cloud chokepoint | A | Three cloud providers = 60%+ public-sector cloud |
| S5 | S5 Solo is a special case — same profession, same rules, dramatically different infrastructure | A/B | Big Law vs Solo: 11/15 vs 1/15 |
| S4 | Upward into S6/S7 requires court-grade evidence the deployment-gating model is not built for; downward into S3 collapses when CAIO loses budget (GM 8-month CAIO dissolution); acquisition integration is the most diagnostic event | B/C | GM CAIO dissolved within 8 months |
| S3 | 250→2,000 employee band spans nearly an order of magnitude; internal sub-pattern boundary probably exists around 800–1,000 employees where dedicated AI governance becomes economical | C | No empirical study |
| S2 | Two dynamics: S2 → S4 via acquisition or rapid scaling (Cohere / Pineau hire); **S2 → S5 via single contract** — one enterprise sale reclassifies a 30-person startup into S5 verification obligations overnight | A/B | **Most consequential scale-crossing dynamic** |
| S1 | Hiring a first contractor redistributes verification instantly; reverse: S2 slides back to S1 on weekend work. Same legal entity can be S1 on Monday and S2 on Tuesday | C | Structural instability |

**Vertical reading**: The most important scale-crossing dynamic is **not** gradual tier migration — it is the sudden single-contract transition (S2 → S5, S1 → S5 for licensed solo professionals). These transitions expose actors to higher-tier liability without giving them higher-tier infrastructure. The framework must have an explicit story for these moments.

---

## Summary: what the matrix shows

Three patterns are visible reading the full matrix:

1. **Variance within tier exceeds variance across tier** at S4, S5, and S2. Microsoft (14/15) and Meta (5/15) are both S4. Big Law (11/15) and solo attorney (1/15) are both S5. Anthropic (13/15) and Cursor (5/15) are both S2. "Tier" is not a meaningful unit of analysis on its own — infrastructure is.

2. **Infrastructure, not headcount, predicts RVCS-1 scores.** S4 substantive (Microsoft, JPMorgan MRG) scores similarly to S2 AI-native (Anthropic). S4 typical scores similarly to S3 and S2 AI-using. S5 Solo scores similarly to S1.

3. **The reasoning verification framework's five disciplines are not equally portable.** Q2 Inferential validity and Q4 Confidence calibration fail first as scale shrinks (the former by structural impossibility at S1, the latter by lack of track record at S2–S3). Q1 Source quality survives across tiers when infrastructure is present. Q3 Normative acceptability is the dominant failure mode at S2 — the "should we do this at all?" question is the one startups systematically skip. Q5 Failure mode awareness is the weakest discipline at every tier except where regulatory pressure forces it.

These three patterns are the inputs to the cross-tier synthesis narrative, the framework portability table, and the verification capacity curve.
