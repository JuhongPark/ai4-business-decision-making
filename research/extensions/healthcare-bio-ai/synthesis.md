# Healthcare and Bio AI — Cross-Cutting Synthesis

status: draft
date: 2026-04-21
purpose: Extract load-bearing findings from the track's six preceding documents, state the framework revisions the findings imply, and identify which findings are candidates for promotion into the core thesis versus which stay inside the extension.

This document synthesises:

- `sub-domain-taxonomy.md` — nine structurally distinct sub-domains
- `regulatory-landscape.md` — 13 regulatory regimes with perimeter map
- `incident-inventory.md` — 30-case inventory with four cross-cutting patterns
- `framework-application.md` — 6-dim delegation + 5-discipline RVCS-1 applied sub-domain by sub-domain
- `scale-mapping.md` — sub-domain × tier matrix with hazard-cell identification

It does not introduce new evidence. Every claim here is supported in one of the documents above.

---

## 1. Six load-bearing findings

### Finding 1 — The single "healthcare" label in the core framework collapses qualitatively different decisions

The core framework treats healthcare as one of eight domains with a uniform "governance-first, default ASSIST" prescription. Applying the framework's own scoring to the nine sub-domains of `sub-domain-taxonomy.md` produces delegation scores spanning 5 to 14 — from the bottom of the ASSIST band to the top of the AUTOMATE WITH GUARDRAILS band. Specifically:

- HC7 (mental health / patient-facing) scores 5-6 and sits at the bottom of the ASSIST band with multiple stacked overrides.
- HC3 (hospital operations), HC4 (drug discovery), and HC5 (pharmacovigilance) score 13-14 and cleanly reach the RECOMMEND or AUTOMATE band.
- HC2 (CDS) scores 9 pre-override, 8 post-override — the ASSIST band; HC1 (imaging) scores 11 — the RECOMMEND band.

The spread within the domain is wider than the spread across most of the core framework's eight domains. "Healthcare → ASSIST" is therefore not useful as a default; it underprescribes for HC3-HC5 and overprescribes relative to what is needed as an explicit prescription for HC2, HC7, HC8. The framework revision implied: replace the single healthcare row in `research/core/taxonomy/scoring-sheet.md` with a nine-row sub-domain matrix, or add a sub-domain index that the scorer consults before setting the domain prior.

Evidence grade: **A**. Finding is directly demonstrated by the framework's own scoring applied consistently.

### Finding 2 — Regulatory gap maps directly to incident-pattern concentration

The regulatory perimeter map in `regulatory-landscape.md` §3 identifies four sub-domain × regime cells marked ✗ (structural gap). These are HC4 drug discovery, HC7 patient-facing mental health, HC3 hospital operations (partial), and HC9 administrative documentation (partial).

The healthcare-bio incident inventory's four cross-cutting patterns line up as follows:

- Pattern 1 (proprietary models deployed before external validation) → HC2 and HC1 under the CDS carve-out gap
- Pattern 2 (cost-proxy denial substitution) → HC8 non-MA gap
- Pattern 3 (conversational AI on vulnerable populations) → HC7 wellness-carve-out gap
- Pattern 4 (drug-discovery translation cliff) → HC4 pre-clinical gap

Three of the four incident patterns map 1:1 to regulatory gaps. The fourth (Pattern 1) maps to the CDS-carve-out gap rather than a complete absence of regulation but still reflects regulatory perimeter failure. Regulatory gap is the best single predictor of healthcare-bio AI incident concentration in this corpus.

Evidence grade: **A for mapping, B for causal claim**. The mapping is demonstrated; the causal claim (regulatory gap *causes* incident concentration) would require a controlled comparison the documentary corpus cannot support.

### Finding 3 — The scale-based track's three findings reproduce in healthcare, with one sharpening and one extension

The scale-based track's three findings (infrastructure > headcount; overtrust is the equilibrium; public-good threshold runs through tiers) all reproduce in healthcare. The reproduction is sharper in two ways:

**Sharpening** — the HC2 per-decision verification budget (5-30 seconds at bedside CDS) vs the framework's 10-50 minute protocol produces a one-to-two-orders-of-magnitude gap, wider than the scale-based track's S4 typical gap. Healthcare makes the overtrust-as-equilibrium finding harder to ignore because the budget-requirement mismatch is dramatic at the specific configuration where most CDS deployment happens.

**Extension** — HC7 × S1 patient-direct-use is uniformly below the public-good threshold. The scale-based track identified S1 as uniformly below the threshold for all domains; the healthcare extension sharpens this by naming a specific sub-domain × tier cell (patient in crisis using mental-health chatbot) where no actor configuration inside the cell can produce adequate private reasoning verification. This is the strongest empirical instance of the scale-based track's public-good argument in any domain studied in the repo.

Evidence grade: **A**. The sharpening is demonstrated by RVCS-1 substantive-typical spread data; the extension is demonstrated by the zero-verification-at-runtime structure of HC7 × S1 plus the incident evidence of HBI-14 (Character.AI) and HBI-15 (Replika).

### Finding 4 — Verification-chain adversarial structure at HC8 is a framework-scope gap

RVCS-1 scoring produces Q3 (normative acceptability) scores of 0-1 for HC8 typical configurations because the verification step — clinician review employed by the insurer — has direct financial interest in one outcome. The current framework treats Q3 as a discipline the reviewer can or cannot perform; HC8 demonstrates that the reviewer's positional relationship to the decision outcome affects the discipline's achievability.

This is a framework-scope gap: the reasoning verification framework does not currently model positional conflicts of interest in the verification chain. The four HC8 cases (HBI-06, HBI-09, HBI-10, HBI-11) together form the single strongest multi-case convergence in the incident inventory, and all converge on the same mechanism.

The adjacent sub-domain HC9 shows a different positional issue: the signing clinician is the verifier but is time-pressured to sign AI-generated notes at volumes that preclude line-by-line review. The conflict is not financial but temporal. Either way, the framework's RVCS-1 instrument needs to extend beyond "did the reviewer perform the discipline" to "was the reviewer positionally able to perform the discipline."

Evidence grade: **A for HC8 finding; B for HC9 extension of the finding**. HC8 evidence is strong (regulatory filings, class-action complaints, CMS rulemaking). HC9 evidence is strong on the hallucination side but the temporal-positional claim for signing clinicians rests on deployment observation rather than structured research.

### Finding 5 — The framework correctly prescribes at five of five divergence tests

The framework-application document identifies five sub-domains where framework prescription diverges from observed deployment practice (HC2 Epic Sepsis deployment, HC7 Character.AI, HC8 non-MA Cigna PxDx, HC9 typical rubber-stamp review, HC3 Obermeyer Optum). In each case, correct application of the framework's override rules would have prescribed a lower authority level than what was deployed, matching the retrospective judgment that the deployment was unsafe.

The framework-output correctness rate is 5/5 on divergence tests. The failures in these five cases are framework-enforcement failures at the delegation-decision-maker level, not framework-output failures. This is consistent with the core framework's existing retrospective validation showing 12/20 correct outright + 7/20 partial flags (`research/extensions/business-alignment/incidents/alignment-failure-mapping.md`).

Evidence grade: **A** for the five specific cases. The generalisation beyond these five would require a larger retrospective validation than this track performs.

### Finding 6 — Seven concrete framework revisions emerge from the sub-domain application

The framework-application document identifies seven specific revisions to the core framework that are load-bearing enough to warrant consideration for promotion:

1. HC2 CDS-carve-out + vendor-embedded + no-site-validation → governance_readiness = 1 automatically
2. HC3 downstream-patient-effect test → risk_level ≤ 2 when operational AI influences patient allocation / priority / timing
3. HC5 automation-erodes-review hook → re-evaluate governance_readiness when AI automation enters a previously manual verification step
4. HC6 split into HC6a / HC6b by variant novelty
5. HC7 "infrastructure-dependent tier" designation for sub-domains where private discipline is structurally insufficient
6. HC8 RVCS-1 Q3 extension to test adversarial verification-chain positioning
7. HC9 Q4 calibration cannot be privately supplied; requires vendor-published per-institution audit data

Revisions 5 and 6 are candidates for promotion into the core framework because they name structural insufficiencies, not just healthcare-specific cases. The other five revisions are healthcare-specific and are better recorded as a sub-domain appendix to the core scoring sheet.

Evidence grade: **A** for the revisions themselves; the promotion recommendations are track judgment, not proven.

## 2. Implications for existing extension tracks

### Scale-based track

The healthcare track provides three sharpening contributions:

1. The RVCS-1 substantive-typical spread data per sub-domain (HC7 = 9; HC8 = 7) is the largest within-cell spread observed in any domain studied in the repo. This is direct support for the scale-based track's Finding 1.
2. The HC7 × S1 cell provides a second empirical instance of the scale-based track's public-good threshold argument, complementing the solo-licensed-professional cell originally identified.
3. The sub-domain × tier matrix in `scale-mapping.md` is a candidate for generalisation: if the matrix is useful in healthcare, similar sub-domain-level decomposition may be useful in finance, legal, and government domains.

### Adaptive governance track

The healthcare track confirms the adaptive-governance track's central thesis that regulator capacity, not regulator intent, is the binding constraint. FDA's radiology-heavy AI-device list (~76% of clearances), EU MDR notified-body bottleneck, and MHRA's small Airlock pilot volumes together form the cleanest capacity-constraint evidence in any domain studied. The EU Digital Omnibus (proposed Nov 2025) is the adaptive-governance track's "regulator acts adaptively when overwhelmed" pattern in operation.

### Business alignment / core 71-case incident track

The healthcare-bio inventory's 30 cases are not promoted into the core 71-count. But four cases are strong candidates for promotion in a future update cycle:

- HBI-01 Epic Sepsis Model (archetype of healthcare proprietary-model failure under CDS carve-out)
- HBI-06 Optum Impact Pro (clearest cross-domain algorithmic-bias case with Science publication backing)
- HBI-09 UnitedHealth nH Predict (class action with multi-year docket; HC8 pattern archetype)
- HBI-14 Character.AI teen suicide (HC7 pattern archetype with Jan 2026 settlement)

These are flagged to the core-update process; the promotion decision is not made here.

## 3. What this track does not answer

Four questions remain open after this track:

1. **Does the framework's RVCS-1 protocol produce different scores when applied to healthcare by clinicians versus by documentary analysts?** This track's scoring is documentary-analyst-produced. Clinician coding may surface disciplines the documentary record understates (Q2 inferential validity comes to mind).
2. **Does the HC7 × S1 public-good finding generalise beyond mental health?** The argument is that vulnerable-population + zero-runtime-verification + regulatory-gap co-occurrence produces structural insufficiency. Other sub-domain × tier cells may reproduce the co-occurrence pattern (HC2 × S1 solo clinician using generative AI for clinical reasoning; HC6 × S1 patient interpreting direct-to-consumer genomics). Primary empirical work is needed.
3. **What is the drug-discovery-AI equivalent of the scale-based track's "productization infrastructure"?** The track identifies that wet-lab verification is the mechanism, but does not decompose what features of a wet-lab pipeline convert AI-hypothesis into AI-evidence. This is a candidate topic for a future extension.
4. **How does the framework handle agentic clinical AI?** This track deliberately set agentic AI aside because the space is in flux. Within 12-24 months this will become a required sub-domain in its own right.

## 4. Recommended next actions

Three are internal to this track; five are for the broader project.

**Internal to this track**:
1. If track is revisited in a second cycle, prioritise primary empirical work on HC2 × S3 community hospital deployments — the highest-volume, least-studied tier × sub-domain cell.
2. Expand the incident inventory from 30 to 50-60 cases with emphasis on Asian jurisdictions.
3. Produce a one-page "healthcare cheat sheet" under `research/delivery/` if the main framework document ships — a condensed version of the sub-domain-taxonomy for decision-maker use.

**For the broader project**:
1. Consider promoting the seven framework revisions in Finding 6 (specifically revisions 5 and 6) into the core taxonomy. Requires a revision cycle of `research/core/taxonomy/`.
2. Reference the HC7 × S1 case in the scale-based track's S1 report as a second empirical instance of the public-good threshold argument.
3. Reference the HC8 adversarial-verification-chain finding in the reasoning-verification track's Q3 normative-acceptability documentation as a framework-scope clarification.
4. Flag the four incident cases (HBI-01, HBI-06, HBI-09, HBI-14) to the core-update process as promotion candidates.
5. The sub-domain × tier matrix approach used in `scale-mapping.md` §2 may be useful as a general analytical template; consider writing a short standalone memo on when the approach is worth the overhead.

## 5. Connection back to the project's central claim

The project's central claim is that AI authority should be adaptive, not fixed, and should be calibrated by six dimensions. This track's findings sharpen the "adaptive" part in a specific way: **within a single domain, authority should be further calibrated by sub-domain**, because the six dimensions themselves take different values across healthcare's nine sub-domains.

The sub-domain level is not a new dimension. It is a refinement of how the existing domain dimension is scored. The revision is small in conceptual terms but has large implications for how the framework is used in practice in high-stakes sectors.

The track does not propose a new framework for healthcare AI. It confirms that the existing framework is portable to healthcare with specific sub-domain-level refinements and explicit acknowledgement of where private-discipline verification is structurally insufficient (HC7 × S1). The bigger revision — framework recognition that some sub-domain × tier cells require public-good infrastructure rather than private practice — is the healthcare-specific instance of the scale-based track's broader argument.

The healthcare-bio AI track is therefore best understood as a stress test of the framework in its most demanding sector. The framework passes the stress test with the seven revisions flagged.
