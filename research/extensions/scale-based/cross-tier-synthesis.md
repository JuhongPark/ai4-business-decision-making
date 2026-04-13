# Cross-Tier Synthesis

status: research_complete
date: 2026-04-13
purpose: Produce the narrative synthesis across the seven tier reports, following Procedures 1-6 defined in the scale-based research plan (§7). This is the document that turns the tier reports plus the comparative matrix, the verification capacity curve, and the framework portability table into a single analytical answer to the project's question about reasoning verification across organisational scales.

---

## 1. Procedure 1 — Dimension gradients

Reading each column of the comparative matrix (§2 of `comparative-matrix.md`) top to bottom produces ten gradient narratives. The gradients do not all move together, which is itself a finding.

**D1 Verification agent identity** — The number of distinct verifiers collapses from dozens at S7 to one at S1, but not monotonically. The fall is fastest between S4 substantive (6-12 reviewers) and S4 typical (1), a within-tier cliff larger than any between-tier difference. The second sharpest fall is between S5 Big Law (3-4) and S5 Solo (1). The "one verifier at the desk" is not an S1 phenomenon — it is the modal configuration at S4 typical, S5 Solo, S3, and S2 AI-using. D1 is the diagnostic dimension for the collapse of the recommend-vs-automate distinction.

**D2 Verification infrastructure** — Non-monotonic. S7 and S4 substantive have dense infrastructure of different kinds; S4 typical is a cliff because the apparatus is built for deployment gating; S3 has no native infrastructure at all (everything rented from vendors); S2 AI-native is lean but purpose-built; S1 is browser + chatbot + one paid review service per quarter. The monotonic reading ("smaller organisation = less infrastructure") is wrong because S4 substantive has more infrastructure than S7 by volume and S2 AI-native has more discipline per dollar than S4 typical.

**D3 Verification incentive structure** — Monotonically weak. At every tier, endogenous incentives to verify are weaker than incentives to ship or comply. Where substantive verification exists, it was forced from outside — regulator, contract, FDA, court order, ministerial veto, chair reputation. The assumption that users want good reasoning does not survive this column. The gradient is not about scale; it is about external compulsion.

**D4 Sanction gradient** — Non-monotonic. The steepest gradient is S5, not S7 or S6, because professional licences create personal liability that committee structures launder at higher tiers. The most dangerous cell in the entire taxonomy is solo licensed professional at S1 — a cell that does not exist in simple scale models because it is the intersection of S5 sanctions and S1 capacity. The gradient is steeper going between S5 Big Law and S5 Solo than between any two successive tier numbers.

**D5 Verification trigger** — Monotonically external. The trigger column exposes the structural collapse of "recommend" into automation. At almost every tier the modal trigger is external pressure, not internal discipline. Where triggers are calendar- or policy-driven (S7 Article IV, S6 inventory, S5 Big Law SOP, S4 substantive intake), verification happens reliably. Where triggers are personal curiosity (S1, S4 typical, S5 Solo), verification happens accidentally. The project's implicit assumption that trained users will initiate verification is contradicted everywhere it is tested.

**D6 Per-decision verification budget** — Non-monotonic but with a clean floor at S1. The mathematical impossibility at S1 (verification floor 30-400 min/day > working day 360-480 min/day) is the load-bearing fact for the public-good argument. Notice that the S4 typical budget (0-3 minutes per Copilot decision) is lower than the S3 partner-review budget (~20 minutes). Budget does not scale with organisational size. It scales with whether the tier's implementation is deployment-gated or case-gated.

**D7 Delegation chain depth** — Monotonically collapsing but with an anomaly at S4. Chain depth falls from 10+ at S7 to 0 at S1. The anomaly: S4's *pre-deployment* chain is one of the longest in the taxonomy, but the *at-use* chain is one of the shortest (1). Committee structures extend the chain upstream but not downstream. S1 is the only tier with structurally zero chain depth.

**D8 Failure mode profile** — Qualitative gradient from social to cognitive. At higher tiers failures are *social* (committee laundering, procurement capture, governance theater). At lower tiers failures are *cognitive* (passive acceptance, sycophantic loops, isolation bias). S2 is anomalous — its dominant failures are *normative* (Q3), not cognitive or social. S3 is the compression tier with a distinctive "some disciplines collapse, others survive implicitly, others are substituted wholesale" fingerprint.

**D9 Substitutes** — The most practically valuable gradient. Substitutes are present at every tier but they are risk-transfer mechanisms, not verification mechanisms. They reduce the probability that a failure will be *the actor's responsibility*, not the probability that a failure will *occur*. This distinction is the most important conceptual move of the entire synthesis. Where tiers rely on substitutes (S3's vendor compliance stack, S1's insurance), verification has quietly exited the system.

**D10 Scale-crossing dynamics** — Not smooth. The most consequential scale-crossing dynamic is not gradual tier migration but sudden single-contract transition: S2 → S5 when a 30-person startup lands a regulated customer, S1 → S5 for a licensed solo professional every working day, S4 → S6/S7 when corporate analysis enters government or international policy. These transitions expose actors to higher-tier liability with lower-tier infrastructure. The "legitimacy laundering downward" dynamic at S7 → S6 → S4 is the mirror image — high-tier outputs acquire unjustified bindingness in lower-tier decisions.

**Summary of gradient patterns**: Three of ten dimensions (D3, D5, D6) behave monotonically in the expected direction. Four (D2, D4, D7, D9) have sharp within-tier cliffs larger than between-tier differences. Three (D1, D8, D10) are non-monotonic in ways that expose specific framework gaps. **The taxonomy is not a line; it is a landscape with holes and cliffs, and the holes are where the reasoning verification framework fails.**

---

## 2. Procedure 2 — Tier profiles

Reading each row of the matrix produces a one-paragraph fingerprint per tier.

**S7 International institutions** — The verifier is a named standing committee or working party that operates on multi-year cycles with dozens of reviewers per deliverable, producing high *legitimacy* but only patchy *epistemic structure* verification. Sources, normative fit, and inferential validity are reviewed informally through expert comment; confidence calibration happens only when a named chair (Bengio) accepts the personal reputational cost of cataloguing disagreement; failure mode awareness has no standardised catalog. The dominant failure mode is committee laundering — an AI-derived claim becomes a "broadly shared assessment" through iterated paraphrase even though no individual reviewer audited it. When full verification is infeasible the substitutes are deference to peer institutions, hedged language, and footnote offload. The cross-tier risk is legitimacy laundering downward.

**S6 National governments and public agencies** — The densest formal apparatus in the taxonomy but the weakest per-decision inferential capture. System-level instruments (UK ATRS, US OMB M-25-21 inventories, EU AI Act FRIA, Korea AI Basic Act) produce inventory and impact assessments without reaching the civil servant who actually pastes a citizen file into a generative-AI tool. FOIA captures outputs, not inferential chains. The counterexamples (Toeslagenaffaire, Robodebt) required royal commissions to reconstruct reasoning years after harm. Sanction gradient is theoretically steep but back-loaded — nothing or national scandal. The modal substitute is "heavy ex ante process + HITL fig leaf + reactive scandal handling." Singapore's AI Verify is the outlier best case (12/15 RVCS-1), achieved by building a testing surface the other jurisdictions have not.

**S5 Big Law and its regulated-profession peers** — The tier with the fullest portable framework. A manufactured human review pipeline (deployment SOP + grounded-tool stack + cite-check layer + partner sign-off) substitutes for the absent regulator-issued protocol. When functioning, it produces 11/15 RVCS-1 scores — the highest among non-S4 exemplars. When missing (S5 Solo), the same professional ethics rules produce 1/15 scores and a 1,174+ case incident corpus. The within-tier variation is therefore not a difference in rules but a difference in infrastructure substituted for missing rules. Cross-profession analog applies: academic medical centers vs solo physicians, Big Four vs solo CPAs, bulge-bracket wealth divisions vs solo RIAs all replicate the pattern with sub-tier shading.

**S4 Large corporations and multinationals** — The tier where the category error lives. Deployment governance is dense, regulator-forced, well-instrumented, and largely effective at preventing unsafe systems from going live. Per-decision reasoning verification is nearly absent at the analyst's desk, where the 66% overtrust / 91% executive concern finding is actually located. The variance between Microsoft AETHER (14/15) and Meta automated review (5/15) is larger than the variance between S4 and lower tiers. "S4 with governance apparatus" is not a meaningful unit of analysis; what matters is whether the apparatus is case-by-case reasoning review (rare, narrow, high-touch) or deployment gating (common, broad, regulatory). The substantive cases appear endogenously only when an external actor (regulator, court, FDA, contract) forces them.

**S3 Mid-sized enterprises** — The compression tier. A verification facade composed of vendor attestations and the residual judgment of busy domain experts. Q1 source quality and Q4 calibration collapse first because they require dedicated tooling and specialist roles. Q2 inference validity survives only implicitly through pre-existing professional review (loan officers, audit partners). Q3 normative acceptability is substituted wholesale by vendor compliance artifacts (SOC 2, ISO 42001, model cards). Q5 failure mode awareness is the weakest of all. Most mid-sized firms dress like S4 and operate like S2. The tier has the least academic coverage of any — the evidentiary silence is itself a finding.

**S2 Small enterprises and startups** — A two-population split. AI-native firms (Anthropic, OpenAI, Cohere, Mistral) implement strong technical disciplines (Q1, Q2, Q5) because their founders are research-lab alumni. AI-using firms (Harvey, Cursor, hundreds of others) have essentially zero standing verification practice until Series B, when external forcing functions (SOC 2 customer ask, first regulated customer, investor diligence) cluster within ~6 months of the Series B close. The dominant failure mode is Q3 normative acceptability — "should we do this at all?" is the question S2 systematically skips. Character.AI, Clearview, DoNotPay, Cleo, Perplexity, Nate Inc., Workado are all Q3 failures. Reasoning verification is *always* externally pulled; it is never internally generated.

**S1 Solo entrepreneurs and individual decision-makers** — The hardest tier and the one with the least literature. The verifier, requester, decision-maker, and accountable party converge on a single individual. N_reviewers = 1 by definition. Delegation chain depth = 0. The verification floor for a complete five-discipline review (30-400 min/day) exceeds the effective working day. Q2 inferential validity is structurally impossible (same person cannot reliably play advocate and skeptic on the same artifact under time pressure). Q4 confidence calibration is impossible (n=1 track record). Q1 and Q5 are adapted to imperfect tools (cross-model crosscheck, failure catalogs). The most dangerous sub-population in the entire taxonomy is the solo licensed professional — S5 liability with S1 capacity. The S1 research vacuum — $1.7T economic segment, near-zero academic coverage — is itself the central finding.

---

## 3. Procedure 3 — Framework portability

The 5×7 framework portability matrix (see `framework-portability.md`) produces five direct conclusions.

1. **The framework must explicitly bound itself** below S4 substantive and S5 Big Law for the full five-discipline protocol. At S4 typical, S3, S2 AI-using, S1 and (for some disciplines) S6, it produces a subset, and the subset must be labelled.

2. **Q2 Inferential validity is the structurally hardest discipline** because it is impossible at S1 by definition. Any framework claiming to serve S1 must either solve this structurally (externalised second-person review) or declare Q2 out of scope at that tier.

3. **Q4 Confidence calibration collapses at five tiers** (S6, S3, S2 AI-using, S4 typical, S1). The common cause is lack of a historical track record. The framework's implicit assumption that actors can calibrate against their own experience fails wherever experience has not accumulated. Calibration must be supplied externally (vendor-published base rates, evaluated accuracy, AI confidence meters) for those tiers.

4. **Q1 Source quality is the most portable discipline** and the most tool-supportable. A browser extension or cross-model source checker is the highest-return single investment for scaling the framework downward. This is the quickest available win.

5. **Q3 Normative acceptability at S2 AI-using is an incentive problem, not a capacity problem.** The tier could perform Q3 if motivated. The S2 failure record — Character.AI, Clearview, DoNotPay — is not about inability to verify; it is about the tier skipping the question. Framework revision should make "should we do this at all?" a standing artefact, not an optional add-on.

**Framework portability conclusion**: The framework is most transferable where infrastructure already exists and least transferable where the actor operates alone. The recommended revision is to bound the full protocol to S4 substantive / S5 Big Law / S2 AI-native / S7 deliverable-scale, produce a compressed protocol for S3 / S2 AI-using / S6 typical / S4 typical, and define S1 as an infrastructure-dependent tier whose framework contribution is the design of that infrastructure rather than the training of the actor.

---

## 4. Procedure 4 — Failure mode map

Combining FICS-1 outputs (from S5) with tier failure profiles (D8) produces a ranked failure vulnerability per tier and a cross-tier matrix of where each failure class concentrates.

| Failure class | Most vulnerable tier(s) | Mechanism |
|---|---|---|
| **Fabrication** (non-existent sources) | S5 Solo, S1 licensed, S3 small-firm | General-purpose ChatGPT without source check; Levidow/Mata, Lake, Brigandi, Massachusetts $2K |
| **Misgrounding** (real source, wrong proposition) | S5 Big Law, S4 substantive, S3 | More professionally dangerous because it survives cursory review; predicted to rise faster than fabrication |
| **Specification gaming** | S2 AI-using (engagement maximisation) | Character.AI companion bots; Nate Inc. AI-washing |
| **Sycophancy** | S1, S4 typical | Isolation bias + time pressure + single-model interaction; UNU 2025 finds 58% sycophantic, 78.5% persistence |
| **Overconfidence** | S2 Humane, S1 founder, S7 without named chair | No calibration surface; Humane AI Pin demos |
| **Misapplication** (using AI where it doesn't fit) | S6 benefits adjudication, S2 AI-using regulated | Toeslagenaffaire, Robodebt, Cleo, Perplexity copyright |
| **Committee laundering** | S7, S4 deployment | Iterated paraphrase removes inferential trace |
| **Governance theater** | S4 typical, S3 | Apparatus present, discipline absent |
| **Reasoning erasure under FOIA** | S6 | MuckRock 2025 empirical finding |
| **Legitimacy laundering downward** | S7 → S6 → S4 flow | Non-binding international norms become binding national law |

**Pattern across failure modes**: The failure mode profile is a function of **tier structural property**, not tier size. Social failures (committee laundering, governance theater, reasoning erasure) happen where apparatus exists. Cognitive failures (passive acceptance, sycophancy, isolation bias) happen where the actor is alone. Normative failures (specification gaming, misapplication) happen where product incentives override ethics. Each tier has a dominant failure class and the framework revision must address each explicitly.

---

## 5. Procedure 5 — Scale-crossing dynamics

Three transitions deserve explicit treatment.

### 5.1 S2 → S5 by single contract

A 30-person Series A startup sells to a regulated-industry customer. The sale creates instant S5 verification obligations — professional liability, ethics-code adherence, per-decision audit trails, human-in-the-loop requirements — while the startup retains S2 infrastructure (CTO-driven, no compliance function, no cite-checkers). The startup cannot simultaneously build S5 infrastructure and hit its quarterly revenue target. The usual coping patterns: offload verification onto the customer's compliance function, narrow the product to a bounded automation box (Aladdin-style), or accept structural risk until the next funding round. None performs actual reasoning verification. This transition is the most consequential scale-crossing dynamic in the taxonomy because it is the most common and the most poorly handled.

**Framework implication**: The framework needs an explicit "S2→S5 crossing kit" — a minimum viable verification protocol a startup can deploy in 30 days to satisfy an S5 customer's due diligence without destroying its velocity. The kit should be designed to be outgrown as the startup scales.

### 5.2 S4 deployment → S6 or S7 use

A corporate analysis, a market forecast, or a risk assessment produced inside an S4 organisation is cited in a government filing or an OECD / IMF / WTO deliverable. The committee structure at the higher tier treats the S4 output as a trusted source and does not re-verify. The S4 output was produced with apparatus-level deployment governance but no per-decision reasoning verification. The result is a paper trail of officially legitimate but epistemically unverified claims flowing upward.

**Framework implication**: S6 and S7 verification procedures need an explicit "imported-reasoning" category with a rule like: any AI-informed claim entering from a lower tier must be re-verified, not accepted as authoritative. This rule does not exist in OECD, UN, or IMF procedures as of April 2026.

### 5.3 S1 / S5 Solo → first hire

The most consequential positive transition. A solo founder hires a contractor, or a solo attorney hires a paralegal. Instantly, a second person can read AI output before commitment. The structural impossibility of Q2 at S1 disappears the moment a second person enters the workflow, even if their formal role is not verification. This is the single highest-impact behavioural recommendation the framework can make at S1: if you cannot pay the verification tax privately, find a second set of eyes by any mechanism.

**Framework implication**: S1 framework guidance should include a "second-eyes" minimum — a rotating peer, a paid reviewer, a partner, a community critique — as a standing practice, not an optional add-on. The second person does not need to be a domain expert to break the advocate-skeptic collapse.

---

## 6. Procedure 6 — Answer to the framing question

**Is reasoning verification a scale-dependent public good that cannot be privately produced below a certain tier, and if so, what is the infrastructure substitute?**

The synthesis supports a **conditional yes** answer.

**Conditional yes**: Reasoning verification is private at tiers where at least one of three conditions is met — infrastructure exists (S4 substantive, S5 Big Law, S7 committee), a dedicated verifier exists (S2 AI-native, S3 partner-review), or external compulsion forces it (regulated finance, FDA-supervised health). Reasoning verification is structurally impossible or effectively absent at tiers where none of the three holds — S1 (all three absent), S4 typical and S2 AI-using and S5 Solo (two of three absent), S3 and S6 typical (one of three absent).

**The public-good threshold** runs between "at least one of the three conditions is present" and "none is present." It does not run between tier numbers. It runs through each tier according to local configuration. A Microsoft Sensitive Uses case is above the threshold; a Copilot-assisted memo inside Microsoft is below it. A Big Law cite-checked brief is above; a solo attorney's unverified filing is below. An Anthropic capability evaluation is above; a Cursor code refactor is below.

**The infrastructure substitute** — what replaces private verification where it fails — has three candidate forms (developed in more detail in the S1 tier report §8):

1. **Standardised reasoning audit APIs** — a public-good verification service that any S1 actor can call against any AI output. Technically feasible (Amazon Bedrock Automated Reasoning demonstrates formal verification at up to 99% accuracy on bounded policy domains; Patronus Percival and TRAIL demonstrate trace-level evaluation). Missing: unified standard, regulatory mandate, non-engineer UX. Feasibility: B.

2. **Verification marketplaces** — two-sided platforms where S1 actors post AI outputs and credentialed reviewers bid to verify them. Draws on the 5.6M U.S. independents earning >$100K. Handles credentialing, payment, and reputation. Feasibility: C, primarily because S1 actors currently do not pay for verification.

3. **Mandatory vendor disclosure** — regulatory action requiring AI vendors to expose confidence scores with calibration samples, sources actually retrieved, known failure modes for prompt class, and refuse/escalate conditions. Would travel with output as metadata. Precedent: FDA CDS guidance January 2026. Feasibility: B technical, D regulatory.

**A complete answer uses all three at different decision stakes** — automated audits at low-stakes high-volume decisions, human marketplaces at the middle, vendor disclosure as a regulatory floor. The S1 offering should be a triage rule, not a single tool.

**What the synthesis does not claim** — and the project commits not to claim without further evidence:

- That the conditional-yes answer is the final answer. Further primary fieldwork (S1 diary study, FICS-1 corpus expansion, S3 survey) could sharpen or revise it.
- That the three infrastructure candidates will work. They are candidate designs, not proven solutions. Feasibility grades are ordinal confidence estimates.
- That the framework can be "rescued" below the threshold by training alone. The structural impossibility at S1 for Q2 and Q4 means training cannot close the gap; infrastructure must.

---

## 7. Three load-bearing findings

Across the six synthesis procedures, three findings emerge as load-bearing for the project's next steps. They are the findings most likely to survive revision and most consequential for the framework's future.

### Finding 1 — Infrastructure, not headcount, predicts verification quality

The RVCS-1 scores of substantive cases across tiers (Microsoft 14/15, Anthropic 13/15, International AI Safety Report 12/15, Singapore AI Verify 12/15, Harvey workflow at Big Law 11/15) are more similar to each other than to the typical cases at the same tiers. The scores of typical and worst cases across tiers (Meta 5/15, Cursor 5/15, Ellis George 4/15, S5 Solo 1/15, S1 founder 0/15) are also more similar to each other than to the substantive cases at the same tiers. The determinant is **whether infrastructure is present to implement the framework**, not the size of the organisation.

**Implication**: The framework should be organised around infrastructure classes, not tier numbers. An Anthropic research-lab startup of 30 people performs reasoning verification better than a Meta team of 300 on the same question, because Anthropic has a purpose-built eval harness and Meta outsourced the function to an AI. Any framework claiming scale relevance must make this distinction clear.

### Finding 2 — The 66%/91% finding is the predicted equilibrium, not a failure

The Microsoft 2025 finding (66% of employees accept AI output without evaluation) and the McKinsey 2024-25 finding (91% of executives agree employees overtrust AI) are not a cultural failing. They are exactly what the verification capacity curve predicts at S4 typical: a per-decision verification budget of 0-3 minutes against a framework that requires 10-50 minutes, with chain depth 1 and no per-decision trigger. The framework currently assumes conditions that do not exist in the tier that houses most of the employees those statistics describe.

**Implication**: A framework that continues to assume meaningful human oversight at the desk level without infrastructure, training, or compulsion is predicting its own failure. The project should stop treating the 66% / 91% finding as a rhetorical anchor and start treating it as an empirical boundary condition that the next framework iteration must satisfy.

### Finding 3 — The public-good threshold runs through tiers, not between them

The threshold below which reasoning verification cannot be produced as a private discipline is not a line between S3 and S2 or between S2 and S1. It is a conditional boundary defined by the co-occurrence of infrastructure absence, verifier compression, and external compulsion failure. The boundary appears inside every tier that has any internal variance. The only tier where the boundary uniformly applies is S1 (because delegation chain depth is structurally zero).

**Implication**: Scale-aware framework design must address the conditional boundary, not the ordinal tier. The framework's scope statement should read: "where at least one of {infrastructure, dedicated verifier, external compulsion} is present, the full protocol applies; where none is present, the framework's contribution is infrastructure design." This is the cleanest bound the synthesis supports.

---

## 8. What the synthesis leaves for Wave 4 work

The synthesis is a compression of tier report material, not a substitute for primary fieldwork. Four pieces of work remain for future research cycles.

1. **S1 diary study** with 12-30 participants across the four sub-populations, instrumented with RVCS-1 and VTI, to replace the current D-grade estimates with empirical data.

2. **FICS-1 expansion** of the legal incident corpus from 8 cases to 100+ cases, coded for firm size, failure class, sanction outcome, and RVCS-1 step skipped, to convert the legal sub-tier from a qualitative anchor to a quantitative benchmark.

3. **S3 survey** at 20-30 mid-sized enterprises with a decision-diary instrument to replace the inferred compression pattern with empirical evidence.

4. **S7 institutional access work** with OECD AI, ITU, IMF to close the thinnest evidence gap in the taxonomy.

None of these is in scope for this cycle. The synthesis records the gap honestly and identifies the primary empirical work that would close it.

---

## 9. Link to the broader project

The scale-based track is the fourth analytical layer of the project:

1. Delegation calibration framework (Phases 00-20) — *when* to use AI
2. Reasoning trust verification direction (2026-03-28) — *how* to verify AI reasoning
3. Adaptive governance extension (Phase 21) — *how governance stays current*
4. Scale-based restructuring (this track) — *who can verify, with what infrastructure, at their scale*

The three earlier layers assume a generic decision-maker. The scale-based layer decomposes that assumption and identifies where the framework holds, where it needs adaptation, and where it is structurally infeasible. The synthesis document is the formal statement of that decomposition.

**Recommended next step for the project**: revise the reasoning verification framework in `research/core/framework/` with explicit scope notes for each tier, using the portability matrix as the direct input, and mark the S1 candidate infrastructure proposals (audit APIs, marketplaces, mandatory disclosure) as the project's constructive contribution at that tier. The revision should not pretend the framework serves S1 as currently constituted — it should say plainly that S1 is infrastructure-dependent and point to the three candidates as the project's first-draft answer.
