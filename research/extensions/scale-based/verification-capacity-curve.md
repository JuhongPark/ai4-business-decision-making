# Verification Capacity Curve

status: research_complete
date: 2026-04-13
purpose: Express the quantitative relationship between organisational scale and the feasible number of reasoning verification steps per decision per person. The curve turns the tier reports' VTI and RVCS-1 data into a single diagnostic artefact and identifies the breakpoint below which the five-discipline framework cannot be performed as a private discipline.

---

## 1. What the curve measures

The curve plots **feasible verification depth per decision** against **organisational scale tier**. Feasible verification depth is measured in three ways: (a) RVCS-1 score as an ordinal expression of the disciplines actually performed, (b) the VTI triple (T_verify/T_total ratio, N_reviewers, N_sources) as a process measure, and (c) a derived step-count ceiling that tells the reader how many of the five framework disciplines can survive at that tier.

The curve is deliberately not a single line. It is a distribution with substantial within-tier variance, and the distribution shape matters more than its mean. Where within-tier variance exceeds between-tier variance (at S4, S5, and S2), the curve shows parallel upper and lower bands labelled *substantive* and *typical*. Where the distribution is tight (S3, S6, S1), a single band is used.

---

## 2. Curve inputs

### 2.1 Observed RVCS-1 anchors

The tier reports produced the following representative RVCS-1 scores:

| Tier | Decision anchor | RVCS-1 / 15 |
|---|---|---|
| S7 substantive | International AI Safety Report 2025 (Bengio) | 12 |
| S7 typical | OECD AI Capability Indicators beta | 9 |
| S6 substantive | Singapore AI Verify Global Assurance Pilot | 12 |
| S6 typical | UK ATRS DWP fraud-scoring; US OMB M-25-21 DHS high-impact | 8 |
| S5 Big Law | Harvey + 4-layer review (AmLaw 50) | 11 |
| S5 Solo | Sanctioned solo attorney filing | 1 |
| S4 substantive | Microsoft AETHER Sensitive Uses program | 14 |
| S4 typical | Meta AI-automated risk review | 5 |
| S3 best | Regional bank composite (implicit partner review) | 7 |
| S3 typical | Mid-tier accounting firm tax workflow | 6 |
| S3 worst | Mid-tier law firm hallucinated filing (Ellis George) | 4 |
| S2 AI-native | Anthropic capability evaluation against ASL-3 | 13 |
| S2 AI-using best | Harvey AI internal memo workflow | 7 |
| S2 AI-using typical | Cursor agentic refactor | 5 |
| S1 licensed professional | Solo attorney AI-assisted brief (sanctioned pattern) | 4 |
| S1 founder | Solo SaaS founder shipping landing page | 0 |
| S1 retail investor | Evaluating AI-generated stock thesis | 0 |

These scores are the raw data for the curve. They are drawn from different decision types and are not perfectly comparable — a Sensitive Uses case is structurally different from a motion in limine. The curve uses them as ordinal anchors, not as cardinal measurements.

### 2.2 Effective attention per decision (VTI-derived)

The effective attention per decision, expressed as T_verify ratio, also varies within tier:

| Tier | Decision type | T_verify / T_total |
|---|---|---|
| S7 | Flagship deliverable (person-years, per-claim minutes) | ~0.6–0.7 for deliverable; tiny per claim |
| S6 | Benefits adjudication | 0.10–0.20 |
| S6 | Regulatory enforcement | 0.40–0.60 |
| S5 Big Law | Brief / memo with cite-check and partner review | 0.20–0.30 |
| S5 Solo | Brief or motion, no review layer | ≈ 0 |
| S4 substantive | Sensitive Uses case | 0.70–0.90 |
| S4 typical | Analyst using Copilot on memo section | 0.00–0.15 |
| S3 | Chatbot output for customer service | ≈ 0.05 |
| S3 | Tax return with partner review | ≈ 0.20 |
| S2 AI-native | Capability evaluation (weeks) | ≈ 0.50 |
| S2 AI-using | Product decision informed by AI | 0.10–0.25 |
| S1 | Routine solo decision | 0.05–0.15 |
| S1 | High-stakes solo decision (flagged) | 0.20–0.40 |

### 2.3 Required attention per full verification (framework baseline)

The five disciplines executed at BCG-associate level consume, per the S1 report's estimate, 2–10 minutes each for a single AI-generated memo. A complete five-discipline review is 10–50 minutes per memo. This figure is a floor, not a ceiling, for what the framework currently requires.

### 2.4 Number of reviewers available per decision (from D1)

N_reviewers per decision (S7 → S1, representative values from exemplars):

| Tier | N_reviewers for a typical decision |
|---|---|
| S7 | 50+ over a multi-year cycle; ~3–5 on a given claim |
| S6 | 1–2 routine; 3–8 for regulatory enforcement |
| S5 Big Law | 3–4 |
| S5 Solo | 1 |
| S4 substantive | 6–12 |
| S4 typical | 1 (the analyst) |
| S3 | 1, role-compressed |
| S2 AI-native | 15–30 for capability cycles |
| S2 AI-using | 1–2 |
| S1 | 1 by definition |

---

## 3. Curve construction

The curve's y-axis is **RVCS-1 score per decision** (0–15). The x-axis is the ordered tier sequence S7 → S1. Each tier contributes two values where within-tier variance is large: the *substantive* (top) band and the *typical* (bottom) band.

```
RVCS-1 score (0–15)
15 ┤
14 ┤                                    ●───  S4 substantive (Microsoft AETHER)
13 ┤                                            ●──── S2 AI-native (Anthropic)
12 ┤ ●─S7 substantive                     
11 ┤      ●── S5 Big Law (Harvey+4-layer)
10 ┤                                 
 9 ┤ ●─── S7 typical                      
 8 ┤         ●── S6 typical                
 7 ┤                            ●─── S3 best                 ●── S2 AI-using best
 6 ┤                              ●─── S3 typical
 5 ┤                                     ●── S4 typical (Meta)     ●── S2 AI-using typical
 4 ┤                          ●─── S3 worst / S5 Solo              ●── S1 licensed prof
 3 ┤
 2 ┤                                           
 1 ┤             ●─── S5 Solo sanctioned
 0 ┤                                                                    ●── S1 founder / retail
   └─────────────────────────────────────────────────────────────────────────────
        S7     S6      S5           S4           S3       S2         S1
```

The curve is visibly **bimodal** at S4, S5, S2, and S1, and **unimodal** at S7, S6, and S3. The bimodality is the most important structural feature of the curve: at the three bimodal tiers, a practitioner's access to infrastructure (not their tier) determines where on the curve they sit.

---

## 4. The step-count ceiling

For each tier, the curve yields a ceiling on the number of framework disciplines that can be performed per decision. The ceiling is derived by asking: given the tier's effective attention per decision (T_verify in minutes) and the baseline cost of a full five-discipline review (10–50 minutes), how many disciplines fit?

| Tier | Effective verification attention (min/decision) | Disciplines feasible | Notes |
|---|---|---|---|
| S7 | High absolute (person-years) but small per claim | 5 for flagship, 2–3 per claim | Committee verification, not per-claim |
| S6 substantive | 15–60 per regulatory decision | 4–5 | Singapore AI Verify pilot realises this |
| S6 typical | 2–5 per operational decision | 1–2 | Benefits adjudication: inventory + sampling only |
| S5 Big Law | 20–50 per brief (cite-check + partner review) | 4–5 | The manufactured review pipeline |
| S5 Solo | <5 per brief | 0–1 | Source quality only if anything |
| S4 substantive | 30–120 for Sensitive Uses case | 5 | Budget intentionally high |
| S4 typical | 0–3 for analyst using Copilot | 0–1 | Q1 partial at best |
| S3 | 2–10 per decision with partner review | 1–2 | Q2 implicit only |
| S2 AI-native | 50+ for capability cycles; <5 for product decisions | 5 for evals, 0–1 for product | Bimodal within firm |
| S2 AI-using | 2–8 | 1 | Q5 reactive, Q3 missing |
| S1 | 0.5–5 routine; 20–30 high-stakes | 0–2 | Structural floor |

**The breakpoint** — the tier below which at least one of the five framework disciplines cannot be performed at all — falls between S4 substantive and S4 typical, not between tier numbers. Within S4, the substantive case performs all five; the typical case performs at most one (and usually zero). The same is true at S5 (between Big Law and Solo) and S2 (between AI-native and AI-using product decisions).

**Below the breakpoint** — any decision where the effective verification attention is less than ~10 minutes — fewer than two of the five disciplines are feasible. At S1 for solo founders and retail investors, the number is typically zero. At S5 Solo, it is typically one (a rushed source check that misses misgrounded citations).

---

## 5. The public-good threshold

The curve implies a public-good threshold: the tier below which private verification effort is dominated by externally provided verification infrastructure.

The threshold is not a single tier. It is defined by three conjoint conditions:

1. **Effective verification attention < 10 minutes per decision**, which excludes routine S4 typical, typical S3, S2 AI-using, and nearly all S1.
2. **N_reviewers = 1**, which excludes S1 entirely and the solo fraction of S5.
3. **Zero delegation chain depth**, which applies uniquely to S1.

All three conditions co-occur at S1. Two of three conditions co-occur at S4 typical, S5 Solo, and S2 AI-using routine decisions. One of three conditions applies at S3 and S6 routine.

**Interpretation**: the public-good case is strongest at S1 (all three conditions) and second strongest at S4 typical, S5 Solo, and S2 AI-using (two of three). Where all three conditions apply, reasoning verification cannot be produced privately in the normal operating context. Where two apply, it is marginally possible but rare. Where one applies, it is possible but rare-in-practice.

This is the quantitative backbone of the §4.5 framing question in the research plan. The answer the curve supports is: **reasoning verification is conditionally a public good**. It is not a public good at S7, S6, S5 Big Law, S4 substantive, or S2 AI-native — at those tiers, infrastructure or committee structure makes private verification feasible. It is de facto a public good at S4 typical, S5 Solo, S3, S2 AI-using, and S1 — at those tiers, private verification is nearly impossible without external infrastructure.

---

## 6. Sensitivity and caveats

The curve is a diagnostic artefact, not a measurement. Several caveats are load-bearing.

**Caveat 1 — RVCS-1 is ordinal, not cardinal.** A 14/15 Microsoft Sensitive Uses case is not "twice as good as" a 7/15 Harvey use case. The numbers express ordering and discipline coverage, not absolute verification quality. Readers should not compute means across cells.

**Caveat 2 — The observed anchors are not randomly sampled.** Tier exemplars were selected in the tier reports for diagnostic clarity, not statistical representativeness. A future primary study (diary studies at S1, S3, S4 typical; FICS-1 corpus expansion at S5) would produce a fuller picture.

**Caveat 3 — The within-tier variance is probably underestimated.** The reports focus on documented best and documented worst cases. The mode is probably between the two, not at either bound.

**Caveat 4 — Decision-type heterogeneity.** The same organisation produces different RVCS-1 scores for different decision types. Microsoft's Sensitive Uses case scores 14/15; a Copilot-assisted analyst memo at the same company probably scores much lower. The curve reports organisational capability at the high end of each tier, not average behaviour.

**Caveat 5 — The 10–50 minute baseline is itself estimated.** A future empirical study should time-and-motion the five disciplines at BCG-associate level across domain types (legal brief, audit memo, clinical decision, financial analysis). The baseline is likely different in different domains.

**Caveat 6 — "Framework disciplines feasible" is a necessary but not sufficient condition.** A tier can have the attention budget for 5 disciplines and still perform 0 if the actor is not trained to perform them. The curve does not account for skill, only for capacity.

---

## 7. What the curve is for

Four uses:

1. **Bounding the framework**. The curve tells the reader where the reasoning verification framework, as currently constituted, fails as a private discipline. Those are the tiers where the framework's contribution must be infrastructure design rather than training.
2. **Explaining the 66% / 91% finding**. The Microsoft 2025 and McKinsey 2024-25 statistics are the aggregate of S4 typical, S3, S2 AI-using, and S5 Solo — precisely the tiers where the curve shows fewer than two disciplines are feasible. The statistics are not a cultural failing; they are the predicted equilibrium of a framework that assumes an attention budget those tiers do not have.
3. **Guiding primary empirical work**. The tiers where the curve is flattest (S1, S3) are the tiers where primary fieldwork will yield the largest information gain.
4. **Shaping the policy brief**. A policy audience asking "should regulation require reasoning verification?" can now be answered with a tier-by-tier ceiling — for tiers above the breakpoint, regulation should require a verification protocol; for tiers below, regulation should require disclosure infrastructure the actor can rely on.

The curve is not the final answer. It is the compression layer that makes the seven tier reports comparable and that gives the cross-tier synthesis a quantitative backbone.
