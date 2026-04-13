# Framework Portability Matrix

status: research_complete
date: 2026-04-13
purpose: For each of the five reasoning verification disciplines, evaluate whether the discipline is portable to each tier, and if so, in what form. The output is a 5×7 discipline-by-tier table plus narrative notes on each row. This is the most direct input to the scale-aware framework revision.

---

## 1. Portability categories

Each cell in the matrix is assigned one of five portability categories:

- **F — Full**: the discipline works as originally defined in the reasoning verification framework, without adaptation.
- **A — Adapted**: the discipline works with tier-specific modification, which the cell describes.
- **S — Substituted**: the discipline is replaced by a different mechanism that produces a comparable function.
- **I — Impossible**: the discipline is structurally infeasible at this tier without external infrastructure.
- **X — Absent**: the discipline is not being performed, even though it is in principle feasible at this tier.

Where a tier has substantial within-tier variance (S2, S4, S5), the cell is split into two values separated by a slash — for example "F / X" at S4 means "Full at substantive S4 firms, Absent at typical S4 firms."

---

## 2. The 5×7 matrix

| Discipline | S7 | S6 | S5 Big | S5 Solo | S4 sub / typ | S3 | S2 AN / AU | S1 |
|---|---|---|---|---|---|---|---|---|
| **Q1 Source quality** | A | A | F | X | F / X | S | F / A | A |
| **Q2 Inferential validity** | A | A | F | X | F / X | F (implicit) | F / A | **I** |
| **Q3 Normative acceptability** | F | F | F | A | F / X | S | A / X | X |
| **Q4 Confidence calibration** | A (leader-dependent) | X | A | X | F / X | X | X | **I** |
| **Q5 Failure mode awareness** | X | A | A | X | F / X | X | F / A | A (uneven) |

Reading the matrix as a whole, three patterns are visible:

1. **Q2 Inferential validity is structurally impossible at S1**, because the same person cannot reliably play advocate (asking for help) and skeptic (challenging the answer) on the same artifact under time pressure. This is the single hardest cell in the matrix and the strongest argument for the public-good thesis.
2. **Q4 Confidence calibration collapses at five tiers** (S6, S3, S2 AI-using, and S1, as well as S4 typical). The common cause is lack of a historical track record to calibrate against. Tiers with long institutional memory (S5 Big Law, S7 committee review with leader cover) can adapt; tiers without memory cannot.
3. **Q3 Normative acceptability is full at S7, S6, S5, and S4 substantive** (because each has an explicit normative body: intergovernmental, constitutional, ethics code, or ethics committee) **but absent at S2 AI-using and S1**. The S2 Character.AI / Clearview / DoNotPay pattern — Q3 failures dominating the S2 incident record — is directly visible in this row.

---

## 3. Discipline-by-discipline analysis

### 3.1 Q1 — Source quality assessment

The discipline asks: does the evidence cited actually support the claim at the confidence level expressed? Would this source survive professional scrutiny?

| Tier | Portability | How it looks in practice |
|---|---|---|
| S7 | **A** | Source review is institutional: named expert pool, peer review, OECD / IPCC / IMF author lists. The discipline exists but is performed at document level, not claim level. |
| S6 | **A** | Procurement documentation records vendor sources; FRIA captures training-data provenance. Not per-decision. The reasoning-erasure failure mode in MuckRock 2025 FOIA tracking is a direct consequence. |
| S5 Big Law | **F** | Cite-check layer is the clearest implementation in the entire taxonomy. Junior associate verifies each citation against Westlaw / Lexis primary source. Fails only when cite-checker treats RAG output as trustworthy. |
| S5 Solo | **X** | No layer. The 1,174+ Charlotin corpus shows 7 of 8 sanctioned cases skipping this discipline. |
| S4 substantive | **F** | Sensitive Uses review cross-checks sources. |
| S4 typical | **X** | Analyst with Copilot has no source check. Deloitte Australia A$440,000 report demonstrates this at a firm with a pre-existing AI policy. |
| S3 | **S** | Substituted by vendor compliance attestations (SOC 2, ISO 42001, model cards). The substitution conflates security with source quality. |
| S2 AI-native | **F** | Evaluation harnesses check source lineage. |
| S2 AI-using | **A** | Where it happens at all, via RAG documentation. Rarely audited at the output level. |
| S1 | **A** | Cross-model second query, browser fact-checker, Perplexity citations. Best-supported discipline at S1 because tool surface exists. |

**Row summary**: Q1 is the most portable discipline in the framework. It survives compression because it can be tooled — a cite-check layer does not require a committee. The S1 tool audit (Bedrock Automated Reasoning, cross-model platforms, Perplexity) shows a real if incomplete implementation surface at the smallest tier.

### 3.2 Q2 — Inferential validity

The discipline asks: does the conclusion follow from the premises? Are there logical gaps, unstated assumptions, or unjustified leaps?

| Tier | Portability | How it looks in practice |
|---|---|---|
| S7 | **A** | Expert reviewer comments serve a weak inference-check function. The International AI Safety Report 2025 explicitly catalogues areas of expert disagreement — a rare S7 implementation that approaches genuine inference verification. |
| S6 | **A** | APA reasoned-decision doctrine (5 USC §706) is the closest analog but was built for human reasoning and applies to AI-informed decisions only by analogy. |
| S5 Big Law | **F** | Senior associate and partner review interrogate the inference chain. This is the highest-fidelity Q2 implementation at any tier. |
| S5 Solo | **X** | No review layer. The inference chain is accepted as drafted. |
| S4 substantive | **F** | Sensitive Uses panels challenge inference chains. |
| S4 typical | **X** | Analyst reads the Copilot output and propagates it without structural inference check. |
| S3 | **F (implicit)** | Survives only because the person reviewing AI work (loan officer, audit partner, clinical lead) already performs inference checking in their non-AI work. The danger is silent failure when AI errors look superficially correct. |
| S2 AI-native | **F** | Adversarial red-teaming against capability thresholds. |
| S2 AI-using | **A** | Ad hoc; test passes as a weak proxy for inference validity. |
| S1 | **I** | **Structurally impossible**. The same person cannot reliably be advocate and skeptic. This is the strongest argument for the public-good thesis. |

**Row summary**: Q2 is the *least* portable discipline. It has a structural floor at S1: without a second person, inference validity cannot be adversarially tested. At S3 it survives only by the accident of pre-existing professional practice, which means it can fail silently when AI produces a plausible-looking but subtly wrong inference. Q2 is the canonical case for "needs a reviewer, or needs infrastructure that acts like one."

### 3.3 Q3 — Normative acceptability

The discipline asks: does the reasoning conform to domain-specific professional standards, ethical norms, and social conventions?

| Tier | Portability | How it looks in practice |
|---|---|---|
| S7 | **F** | The tier's entire raison d'être is normative review. OECD AI Principles, EU AI Act, Council of Europe Framework Convention on AI are explicit normative instruments. |
| S6 | **F** | FRIA under EU AI Act Art. 27; equality and fundamental-rights impact assessments; procurement norms; FOIA and constitutional rights anchors. Strongest implementation at a formal level. |
| S5 Big Law | **F** | Professional ethics codes (ABA Rule 3.3, Rule 11, state bar opinions) are the normative anchor. |
| S5 Solo | **A** | Same rules apply but enforcement falls back on personal judgment; no intermediary between the rule and the decision. |
| S4 substantive | **F** | Ethics review panels (Microsoft AETHER was originally exactly this) operate exactly this discipline. |
| S4 typical | **X** | The individual analyst has no standing norm check on output at the desk. |
| S3 | **S** | Substituted by vendor compliance artifacts (SOC 2, ISO 42001). The substitution conflates process-level norms with output-level norms. |
| S2 AI-native | **A** | Research lab norms at early stage; RSP-style commitments at later stage. |
| S2 AI-using | **X** | The dominant failure mode of the tier. Character.AI, Clearview, DoNotPay, Cleo, Perplexity, Nate Inc., Workado, Evolv — all Q3 failures. "Should we do this at all?" is the question S2 systematically skips. |
| S1 | **X** | No native normative surface. Solo licensed professionals inherit S5 norms but operate without enforcement apparatus. |

**Row summary**: Q3 is the discipline with the steepest gradient. At S7 it is full because tier purpose requires it. At S2 AI-using it is absent because product incentives override it. The S2 row is the most diagnostic: the tier produces the most Q3 failures not because it cannot perform the discipline but because it has an incentive not to.

### 3.4 Q4 — Confidence calibration

The discipline asks: is the expressed certainty proportionate to the strength of the supporting evidence?

| Tier | Portability | How it looks in practice |
|---|---|---|
| S7 | **A (leader-dependent)** | Possible when a named chair explicitly catalogues expert disagreement (Bengio, International AI Safety Report 2025). Absent in ordinary committee outputs where hedged language replaces calibration. |
| S6 | **X** | Aggregate metrics only; no per-decision calibration. |
| S5 Big Law | **A** | Partner-level implicit calibration during sign-off ("would I bet my license on this"); not systematic. |
| S5 Solo | **X** | Zero. The solo practitioner has no track record to calibrate against. |
| S4 substantive | **F** | Frontier red team at Microsoft; Model Risk Management at JPMorgan; FDA-required calibration for medical AI. |
| S4 typical | **X** | No per-decision calibration; users treat AI confidence as given. |
| S3 | **X** | Collapses. Mid-sized firms treat output as binary (correct / wrong), which is the opposite of how the underlying systems behave. |
| S2 AI-native | **X** | Activates late, often never. Requires historical track record which rapid-moving startups do not accumulate before they exit or scale. |
| S2 AI-using | **X** | Absent. |
| S1 | **I** | **Structurally impossible**. A single actor cannot systematically calibrate against a track record that is always n=1. |

**Row summary**: Q4 is the hardest discipline to transport downward. It survives only where institutional memory exists (S5 Big Law partners, S4 substantive MRG, S7 leader-driven). It collapses everywhere else. The finding has a direct design implication: Q4 at S1, S2, S3, and S4 typical needs an externally supplied base-rate surface (vendor-published calibration data, AI confidence meters grounded in evaluated accuracy), not a discipline inside the actor's head.

### 3.5 Q5 — Failure mode awareness

The discipline asks: what are the known patterns of AI reasoning failure, and does this output exhibit any of them?

| Tier | Portability | How it looks in practice |
|---|---|---|
| S7 | **X** | No standardised AI failure catalog that a working party is required to consult. OECD AI Incidents Monitor is a reporting surface, not a pre-decision checklist. |
| S6 | **A** | Post-deployment monitoring in some agencies; red-teaming at AISI and Singapore. Uneven and jurisdiction-dependent. |
| S5 Big Law | **A** | Post-Mata internal training at major firms; not consulted per decision. |
| S5 Solo | **X** | Absent in sanctioned cases. |
| S4 substantive | **F** | Frontier red teams, adversarial testing, incident review. |
| S4 typical | **X** | Not performed at the desk. |
| S3 | **X** | Weakest discipline at S3; no incident playbooks, no red team, no after-action review. Failures surface as customer complaints. |
| S2 AI-native | **F** | First discipline to activate (reactively, after Mata / Character.AI / Stability collapse). |
| S2 AI-using | **A** | Reactive; activated by first public incident. |
| S1 | **A (uneven)** | Some S1 actors use failure catalogs; most do not. Q5 is unexpectedly the second-most portable discipline at S1 because failure catalogs (NC Bar January 2026 guide, TrueFuture 2026) are cheap to distribute. |

**Row summary**: Q5 is counterintuitively the discipline most amenable to cheap distribution. A failure catalog is a document; distributing documents scales. The S5 Big Law post-Mata training wave and the NC Bar / ABA Opinion 512 guidance show that Q5 can be moved downward with modest investment. The tier reports show it collapses most severely at S3 — the tier that has neither the dedicated capacity of S4 nor the urgency of S2.

---

## 4. Column-level readings (tier fingerprints)

Reading the matrix vertically produces a tier fingerprint — a one-line answer to "which disciplines does this tier perform."

- **S7**: Q3 full, Q1/Q2/Q4 adapted, Q5 absent. Profile: strong normative review, weak failure-mode discipline.
- **S6**: Q3 full, Q1/Q2/Q5 adapted, Q4 absent. Profile: normative anchor intact, calibration gone.
- **S5 Big Law**: Q1/Q2/Q3 full, Q4/Q5 adapted. Profile: the tier with the fullest portable framework.
- **S5 Solo**: only Q3 adapted, rest absent. Profile: same rules as Big Law, none of the infrastructure.
- **S4 substantive**: all five full. Profile: the tier with substantive implementation of the complete framework.
- **S4 typical**: all five absent. Profile: apparatus present, discipline absent — the governance theater case.
- **S3**: Q2 implicit full, Q1/Q3 substituted by vendor compliance, Q4/Q5 absent. Profile: the compression tier — disciplines survive where pre-existing practice carries them, collapse where they require dedicated investment.
- **S2 AI-native**: Q1/Q2/Q5 full, Q3 adapted, Q4 absent. Profile: technical disciplines strong, normative review late, calibration missing.
- **S2 AI-using**: Q1/Q2 adapted, Q5 adapted, Q3/Q4 absent. Profile: the Q3 failure tier.
- **S1**: Q1/Q5 adapted, Q3 absent, Q2/Q4 structurally impossible. Profile: fewer than half the framework disciplines are portable.

---

## 5. What the portability matrix implies for framework revision

Five direct implications for the scale-aware framework revision:

1. **The framework must explicitly bound itself below S4 substantive and S5 Big Law for the full five-discipline protocol.** At other tiers, the framework produces a subset, and the subset must be labelled clearly.

2. **Q2 and Q4 are the two disciplines most in need of infrastructure support.** Q2 because it is structurally impossible at S1; Q4 because it is absent at five tiers. Any infrastructure the framework recommends should target these two first.

3. **Q1 is the most portable discipline and the most tool-supportable.** A lightweight Q1 tool (browser extension, cross-model source checker, mandatory citation verifier) is the highest-return investment for scaling the framework downward.

4. **Q3 at S2 AI-using is an incentive problem, not a capacity problem.** The tier could perform Q3 if motivated. Framework revision should address the motivational gap explicitly — make "should we do this at all?" part of the standard artefact, not an optional add-on.

5. **Q5 is portable through documentation.** Distribute a versioned failure catalog with each model release; S3, S2 AI-using, and S1 can consume it at near-zero cost. This is the cheapest cross-tier improvement available.

These five implications are the direct inputs to the framework revision document that the scale-based research plan commits to producing as an artefact of the synthesis.
