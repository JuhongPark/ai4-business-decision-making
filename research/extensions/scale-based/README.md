# Scale-Based Reasoning Trust Verification Track

status: wave_1_2_3_complete
date: 2026-04-13
owner: scale-based research track

This directory contains the first full pass of the scale-based reasoning trust verification research. It restructures the reasoning verification work around seven organisational scale tiers and produces a cross-tier comparative synthesis.

## Why this track exists

The project's reasoning trust verification direction (2026-03-28) had been speaking to a generic "business decision-maker." That generic framing hid the most consequential question: **who actually pays the verification tax, and is paying it feasible at their scale?** The scale-based track answers that question by decomposing the framework's implicit audience into seven tiers with qualitatively different verification structural properties.

The output is not a ranking of tiers. It is a structural decomposition that shows where the five-discipline reasoning verification framework holds as currently constituted, where it needs adaptation, and where it is structurally infeasible as a private discipline.

## Seven-tier taxonomy

| Tier | Scale | Defining structural property | Representative actors |
|---|---|---|---|
| S7 | International institutions | Verification is a legitimacy problem across sovereign jurisdictions | UN, OECD, ITU, IMF, WHO, World Bank |
| S6 | National governments and public agencies | Verification is an accountability-to-the-public problem | US federal agencies, UK Civil Service, EU member states |
| S5 | Regulated professions and legal institutions | Verification is a professional-liability problem | Law firms, medical practices, accountancies, licensed financial advisers |
| S4 | Large corporations and multinationals | Verification is distributed through governance apparatus | Fortune 500, global banks, Big Tech, pharma majors |
| S3 | Mid-sized enterprises | Verification is compressed into a few role holders | ~250-2,000 employees, regional banks, mid-market industrials, SaaS scale-ups |
| S2 | Small enterprises and startups | Verification is founder- or CTO-driven, ad hoc, incident-triggered | 10-250 employees, most Series A-C companies |
| S1 | Solo entrepreneurs and individual decision-makers | Verification is absorbed entirely by the decision-maker who also owns the outcome | 1-9 person businesses, solo licensed professionals, freelancers, retail investors |

## Recommended reading order

1. [cross-tier-synthesis.md](cross-tier-synthesis.md) — start here. The narrative synthesis that reports the three load-bearing findings and answers the framing question.
2. [comparative-matrix.md](comparative-matrix.md) — the 7×10 comparative matrix (tiers × dimensions). The primary compression artefact.
3. [verification-capacity-curve.md](verification-capacity-curve.md) — the quantitative curve with its breakpoints and public-good threshold.
4. [framework-portability.md](framework-portability.md) — the 5×7 discipline-by-tier portability table with direct implications for framework revision.
5. [size-speed-resource-tradeoff.md](size-speed-resource-tradeoff.md) — supplementary memo on the classical firm-size literature (speed advantage, resource advantage, middle-market squeeze, liability of smallness / newness, ambidexterity). Independent external validation of Finding 1.
6. [sales-vs-productization-decomposition.md](sales-vs-productization-decomposition.md) — supplementary memo decomposing the tradeoff memo's three axes (speed, resources, verification quality) into two firm-level skills: sales skill (sales + investment) and productization skill (product implementation only). Names the verification-claim / verification-substance gap and re-expresses the three load-bearing findings under the decomposition. §14 integrates the six Wave 4 streams below.
7. Wave 4 decomposition appendices (2026-04-21), read alongside the parent memo:
   - [incident-decomposition-recoding.md](incident-decomposition-recoding.md) — Stream B: 20-incident recoding against the 2×2 matrix.
   - [asia-market-decomposition-appendix.md](asia-market-decomposition-appendix.md) — Stream A: Korean / Japanese / Chinese / Singaporean cases.
   - [eval-engineering-profession-appendix.md](eval-engineering-profession-appendix.md) — Stream C: eval engineering as a crystallising productization sub-profession.
   - [regulatory-regime-skill-asymmetry-appendix.md](regulatory-regime-skill-asymmetry-appendix.md) — Stream D: 11 regulatory regimes coded by sales-instrument vs productization-substance asymmetry.
   - [vertical-ai-depth-appendix.md](vertical-ai-depth-appendix.md) — Stream E: 21 vertical-AI firms coded by productization depth.
8. Tier reports, in whatever order best fits the reader's purpose:
   - [s7-international-institutions.md](s7-international-institutions.md)
   - [s6-national-governments.md](s6-national-governments.md)
   - [s5-regulated-professions.md](s5-regulated-professions.md)
   - [s4-large-corporations.md](s4-large-corporations.md)
   - [s3-mid-sized-enterprises.md](s3-mid-sized-enterprises.md)
   - [s2-small-enterprises-startups.md](s2-small-enterprises-startups.md)
   - [s1-solo-entrepreneurs.md](s1-solo-entrepreneurs.md)

## Three load-bearing findings

From the cross-tier synthesis:

1. **Infrastructure, not headcount, predicts verification quality.** Substantive cases across tiers (Microsoft 14/15, Anthropic 13/15, Singapore AI Verify 12/15, Harvey+review at Big Law 11/15) cluster together. Typical cases across tiers (Meta 5/15, Cursor 5/15, Ellis George 4/15, solo attorney 1/15) also cluster together. Tier is not the unit of analysis; infrastructure is.

2. **The 66%/91% overtrust finding is the predicted equilibrium, not a failing.** At S4 typical the per-decision verification budget (0-3 minutes) is dramatically smaller than the framework's 10-50 minute baseline. A framework that assumes conditions that do not exist predicts its own failure.

3. **The public-good threshold runs through tiers, not between them.** The boundary below which reasoning verification cannot be produced privately is defined by the co-occurrence of infrastructure absence, verifier compression, and external-compulsion failure. The boundary appears *inside* every tier that has internal variance (S4, S5, S2). Only S1 is uniformly below the boundary.

See [sales-vs-productization-decomposition.md](sales-vs-productization-decomposition.md) for the two-skill reinterpretation that sharpens each finding: Finding 1 becomes "*productization* infrastructure predicts verification *substance*, while *sales* infrastructure predicts verification *claims*"; Finding 2 becomes the joint failure of sales narrative × productization shortfall; Finding 3 runs through both skills, converging the AI-liability and scale-based public-good arguments.

## Shared instruments used across tier reports

Every tier report applies the same coding instruments so the findings are comparable:

- **RVCS-1** — Reasoning Verification Coding Scheme. Five 0-3 scores (source quality, inferential validity, normative acceptability, confidence calibration, failure mode awareness) summed to 0-15.
- **VTI** — Verification Tax Instrument. The triple (T_verify/T_total, N_reviewers, N_sources).
- **FICS-1** — Failure Incident Coding Scheme. Eight-field coding of documented incidents (most fully applied at S5).
- **Evidence grading rubric** — A (primary source), B (credible practitioner/secondary), C (inferred), D (speculative, must be flagged).

Details in `research/operations/expansion/scale-based-reasoning-trust-research-plan.md`, §4–§5.

## Status and honest limitations

**This track is Wave 1–3 work only.** The research plan defines a Wave 4 of primary empirical work that has not been done in this cycle:

- **S1 diary study** with 12-30 participants across sub-populations — highest-value missing piece
- **FICS-1 expansion** from 8 coded legal cases to 100+ — most tractable primary empirical work
- **S3 survey** at 20-30 mid-sized enterprises — addresses the weakest evidence base in the taxonomy
- **S7 institutional access work** with OECD AI / ITU / IMF — thinnest documentary evidence

Tier reports vary in evidence strength. S5 (with the 1,174+ Charlotin corpus) is the richest. S4 (with extensive repository material) is a reframing of existing evidence. S3 and S1 rely substantially on C and D grades because the underlying literature is sparse.

Several claims flagged D (speculative) are included where the research gap justifies naming a hypothesis that future primary work can test. The reports say so plainly.

## Upstream research plan

- Plan: [`research/operations/expansion/scale-based-reasoning-trust-research-plan.md`](../../operations/expansion/scale-based-reasoning-trust-research-plan.md)
- Broader reasoning trust direction: [`research/core/planning/research-direction-reasoning-trust.md`](../../core/planning/research-direction-reasoning-trust.md)
- Connection to existing framework: [`research/core/planning/research-direction-review.md`](../../core/planning/research-direction-review.md)

## Connection to the rest of the project

This track is the fourth analytical layer:

1. Delegation calibration framework (Phases 00-20) — *when* to use AI
2. Reasoning trust verification direction (2026-03-28) — *how* to verify AI reasoning
3. Adaptive governance extension (Phase 21) — *how governance stays current*
4. Scale-based restructuring (this track) — *who can verify, with what infrastructure, at their scale*

The three earlier layers assume a generic decision-maker. The scale-based layer decomposes that assumption, bounds the framework, and identifies the infrastructure substitutes needed where the framework is structurally infeasible.

## Recommended next actions for the project

1. **Revise the reasoning verification framework** in `research/core/framework/` with explicit scope notes for each tier, using the framework portability table as the direct input. The revision should not pretend the framework serves S1 as currently constituted — it should say plainly that S1 is infrastructure-dependent.
2. **Prioritise the S1 diary study** as Wave 4's first primary empirical effort. It is the highest-information-gain study in the plan.
3. **Mark the S1 candidate infrastructure proposals** (standardised audit APIs, verification marketplaces, mandatory vendor disclosure) as the project's constructive contribution at the tier where the private framework fails.
4. **Treat the 66% / 91% finding as a boundary condition**, not a rhetorical anchor. Any future iteration of the framework must satisfy it empirically.
