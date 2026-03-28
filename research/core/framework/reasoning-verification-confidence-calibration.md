# Confidence Calibration Assessment Method

status: active
phase: 2.5
date: 2026-03-28
purpose: Method for detecting when AI-expressed confidence exceeds the strength of supporting evidence.

## The Problem

LLMs produce outputs that systematically over-express confidence. A market projection based on a single analyst blog post is stated with the same linguistic certainty as one based on government statistics. Hedging language, when present, is often cosmetic — it creates an impression of intellectual rigor without actually reducing the confidence of the claims.

This method helps practitioners detect the gap between expressed confidence and warranted confidence.

---

## Step 1: Identify Key Claims

Select the 3-5 most important claims in the AI output — the claims that, if wrong, would change the decision. These are typically:

- The central conclusion or recommendation
- The primary evidence cited to support it
- Key assumptions about market conditions, competitive dynamics, or timing
- Quantitative projections or estimates

## Step 2: Rate Expressed Confidence

For each claim, assess the confidence level expressed in the text:

| Expressed Confidence | Linguistic Markers | Quantitative Indicators |
|---|---|---|
| **High** | "will," "clearly," "definitely," "without question," "the data shows" | Precise single-point estimates ("$50B by 2028"), definitive timelines |
| **Medium** | "likely," "suggests," "indicates," "the evidence points to" | Ranges ("$40-60B"), qualified timelines ("within 2-3 years") |
| **Low** | "may," "could," "one possibility," "preliminary evidence suggests" | Wide ranges, explicit uncertainty acknowledgment, multiple scenarios |

## Step 3: Rate Evidence Strength

For each claim, assess the actual strength of the supporting evidence (using the source quality assessment):

| Evidence Strength | Criteria |
|---|---|
| **Strong** | Multiple Level 4-5 sources converging on the same finding; well-established in the relevant field |
| **Moderate** | Level 3-4 sources with some convergence; reasonable basis but not definitive |
| **Weak** | Level 1-2 sources, single source, no convergence, or no source cited |

## Step 4: Check Alignment

Map expressed confidence against evidence strength:

| | Strong Evidence | Moderate Evidence | Weak Evidence |
|---|---|---|---|
| **High confidence** | Well-calibrated | Over-confident | Severely over-confident |
| **Medium confidence** | Under-confident (rare) | Well-calibrated | Over-confident |
| **Low confidence** | Under-confident | Under-confident (rare) | Well-calibrated |

Flag all cells in the "over-confident" zone.

## Step 5: The Hedge Test

Remove all hedging language from the AI output. Read the bare claims.

Ask:
- Does removing hedges change the meaning? If not, the hedges were cosmetic.
- Are the bare claims defensible at their stated confidence level?
- Is hedging applied uniformly, or only to peripheral claims while core claims remain unhedged?

**Selective calibration** is the most deceptive pattern: the AI hedges minor points ("adoption timelines may vary") while stating critical claims without qualification ("the market will reach $300B"). This creates an impression of intellectual honesty while the load-bearing claims remain over-stated.

## Step 6: Assessment

| Rating | Criteria |
|---|---|
| **Well-calibrated** | Expressed confidence matches evidence strength across key claims. Uncertainties acknowledged where appropriate. |
| **Over-confident** | One or more key claims expressed with higher confidence than evidence warrants. Specify which claims and what confidence level is warranted. |
| **Selectively calibrated** | Peripheral claims are hedged but core claims are over-stated. The overall impression of rigor is misleading. |

---

## Worked Example

**AI output**: "The enterprise AI market will reach $300B by 2027, driven by widespread adoption across all major industries. Healthcare and financial services will lead adoption, with manufacturing following closely. While adoption timelines may vary by region, the overall trajectory is clear."

**Step 1 — Key claims**:
1. Market will reach $300B by 2027
2. Driven by widespread adoption across all major industries
3. Healthcare and financial services will lead
4. Manufacturing will follow closely

**Step 2 — Expressed confidence**:
1. High ("will reach" — definitive, single-point estimate)
2. High ("widespread adoption across all" — universal claim)
3. Medium-High ("will lead")
4. Medium ("following closely")

**Step 3 — Evidence strength** (hypothetical source check):
1. Source: two vendor-published reports and one analyst blog post → Weak (Level 1-2 sources)
2. No source cited → Very weak
3. One industry survey from a consulting firm → Moderate (Level 4)
4. No source cited → Very weak

**Step 4 — Alignment check**:
1. High confidence + Weak evidence → **Severely over-confident**
2. High confidence + Very weak evidence → **Severely over-confident**
3. Medium-High confidence + Moderate evidence → Borderline acceptable
4. Medium confidence + Very weak evidence → **Over-confident**

**Step 5 — Hedge test**:
The only hedge is "adoption timelines may vary by region" — a peripheral qualifier. The core claims (market size, universal adoption, sector leadership) are all stated without qualification. This is **selective calibration**.

**Step 6 — Assessment**: Over-confident. The $300B projection and "widespread adoption" claims require significant downgrade. Warranted statement: "Analyst estimates for the enterprise AI market range from $X to $Y by 2027, with healthcare and financial services showing strongest adoption signals based on [specific survey]. Manufacturing adoption remains uncertain."
