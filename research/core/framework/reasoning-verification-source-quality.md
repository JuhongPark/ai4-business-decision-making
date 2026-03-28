# Source Quality Assessment Method for AI Reasoning Verification

status: active
phase: 2.2
purpose: Formalize a systematic method for evaluating whether the sources behind AI-generated reasoning meet professional standards for business decision-making.

## Origin

This method codifies a discipline that consulting firms treat as non-negotiable: verifying that the evidence base justifies the analytical claims being made. At BCG, where analysis directly informed decisions worth tens of billions of won, every consultant was trained to evaluate source credibility before accepting any factual claim in an analytical chain. The skill was instinctive for trained consultants but invisible to outsiders.

The problem: LLMs produce fluent, structured output that reads like professional analysis. When an LLM cites blog posts and vendor marketing material as evidence for strategic claims, untrained users accept the output because it looks credible. A trained consultant would reject the same analysis immediately -- not because the facts are wrong, but because the sources are inadequate for the claims being made.

This method makes that instinct systematic and teachable.

---

## Source Quality Hierarchy

Five levels of source quality for business contexts, ranked by accountability, methodology transparency, and institutional review.

### Level 5 -- Primary Authoritative Sources

- Government statistics (census data, BLS, national statistical offices)
- Regulatory filings and decisions (SEC filings, CFPB orders, court opinions)
- Peer-reviewed academic research in established journals
- Audited financial statements
- Legislative and regulatory text

Criteria: independently verified, legally accountable, methodology transparent, subject to institutional review or legal obligation.

### Level 4 -- Institutional Analytical Sources

- Reports from established research firms (Gartner, IDC, McKinsey Global Institute, Forrester)
- Central bank reports, World Bank data, IMF publications
- Industry association data with documented methodology
- Major consulting firm published research with named methodology

Criteria: institutional reputation at stake, methodology disclosed, track record verifiable, review process exists within the institution.

### Level 3 -- Professional Secondary Sources

- Major business press with editorial standards (Financial Times, Wall Street Journal, Bloomberg, Reuters)
- Company-published data (annual reports, investor presentations, 10-K filings)
- Conference presentations by named experts with institutional affiliation
- Named analyst reports from recognized firms

Criteria: editorial review process exists, author and source identifiable, conflicts of interest discoverable even if not eliminated.

### Level 2 -- Informal Sources

- Blog posts by individuals, including domain experts
- Unattributed industry reports without named methodology
- Conference marketing materials and event summaries
- Social media posts and threads
- Podcast transcripts and interview summaries
- Self-published whitepapers without peer review

Criteria: no institutional review process, accountability is personal not institutional, quality varies widely, no systematic fact-checking or editorial oversight.

### Level 1 -- Unreliable or Non-Verifiable Sources

- Anonymous content without attribution
- Marketing and sales material from vendors with financial interest in the claim
- AI-generated content without source verification
- Sources that cannot be located or verified
- Paywalled or restricted content cited without access evidence
- Circular citations (Source A cites Source B which cites Source A)

Criteria: no accountability, potential or actual financial conflict of interest, cannot be independently checked, may not exist.

### Hierarchy Summary

| Level | Label | Accountability | Review Process | Example |
|---|---|---|---|---|
| 5 | Primary authoritative | Legal/regulatory | Statutory or peer review | SEC filing, peer-reviewed journal |
| 4 | Institutional analytical | Institutional reputation | Internal methodology review | Gartner report, World Bank data |
| 3 | Professional secondary | Editorial/personal | Editorial review | FT article, annual report |
| 2 | Informal | Personal only | None | Blog post, social media |
| 1 | Unreliable/non-verifiable | None | None | Vendor sales material, anonymous content |

---

## Source-Claim Matching Rules

Not every claim requires the same source quality. The required level depends on what kind of claim is being made and what decisions it influences.

| Claim Type | Minimum Source Level | Rationale |
|---|---|---|
| Factual assertion used in strategic decision | Level 4+ | Strategic decisions require institutional-grade evidence. A market size estimate driving a resource allocation decision cannot rest on a blog post. |
| Quantitative projection used in financial modeling | Level 4+ | Any specific number entering a financial model needs a source with documented methodology. Unattributed numbers are unacceptable. |
| Causal claim driving strategy change | Level 4+ | Claims that X causes Y in a market context require research-grade evidence. Correlation from informal sources does not justify causal inference. |
| Trend claim influencing resource allocation | Level 3+ | Claims about shifting customer preferences or market direction require credible reporting at minimum. A single blog post is not sufficient. |
| Regulatory or legal claim | Level 5 | Any claim about what a regulation requires or what the law says must cite the actual regulation, statute, or court decision. Summaries and interpretations are not substitutes. |
| Industry benchmark or best practice claim | Level 3+ | Claims about what leading companies do or what constitutes standard practice need identifiable sources with editorial or institutional review. |
| Anecdotal illustration | Level 2+ | A single company example used as illustration, not evidence, can use informal sources if explicitly labeled as anecdote. |
| Background context | Level 2+ | General orientation material (definitions, historical context) can use informal sources if the claims are non-controversial and not load-bearing for the analysis. |

### Critical Rule

If a claim type requires Level 4+ and the actual source is Level 2 or below, the claim is not merely weakly sourced -- it is unsupported. The gap between what the source provides and what the claim requires is too large for the claim to be used in decision-making.

---

## Assessment Protocol

A step-by-step process for evaluating source quality in AI-generated analysis. Apply this to any AI output that will inform a business decision.

### Step 1: Source Identification

For each factual claim in the AI output:

- Can the claim be traced to a specific, named source?
- If no source is cited, flag the claim as **ungrounded**. An ungrounded claim is not necessarily false, but it cannot be evaluated for quality.
- If a source is cited, can it be located and accessed? A citation that cannot be verified is functionally equivalent to no citation.

Practical test: copy the citation into a search engine. Can you find the original source? Does it say what the AI claims it says?

### Step 2: Source Level Classification

For each cited source, classify it on the five-level hierarchy.

Key caution: AI may cite a source accurately but misrepresent which level it belongs to. Common patterns:

- Presenting a blog post as if it were a research finding
- Citing a vendor whitepaper as if it were an independent industry report
- Referencing a press release as if it were investigative journalism
- Treating a conference marketing summary as if it were an expert presentation

The classification must be based on what the source actually is, not how the AI presents it.

### Step 3: Source-Claim Match Evaluation

For each factual claim, compare the source level to the minimum required for that claim type using the matching rules above.

Produce a match assessment:

- **Adequate**: source level meets or exceeds the minimum for the claim type
- **Marginal**: source level is one level below the minimum (acceptable only for non-critical claims)
- **Inadequate**: source level is two or more levels below the minimum

### Step 4: Source Independence Check

When the AI cites multiple sources to support a claim, verify independence:

- Do the sources trace back to the same original data or publication?
- Does the AI present a single source's finding as if it were a consensus across multiple independent sources?
- Are the "multiple sources" actually multiple articles reporting on the same underlying study?

A claim supported by three articles all citing the same Gartner report is supported by one source, not three.

### Step 5: Conflict of Interest Screen

For each source, evaluate whether the source has a financial or institutional interest in the claim being true:

- Vendor-published research about the vendor's own market segment is not independent evidence
- Industry association data may reflect advocacy positions, not neutral measurement
- Consulting firm research may be structured to create demand for consulting services
- Company-published performance data is self-reported and not independently verified

A conflicted source is not automatically wrong, but it cannot serve as the sole basis for a claim. Conflicted sources require corroboration from independent sources at the same or higher level.

### Step 6: Currency Check

Evaluate whether the source is current enough for the claim being made:

- Market size and growth data: generally requires data from within the past 2 years
- Regulatory claims: must reflect current law, not superseded versions
- Technology trend claims: data older than 2-3 years may be obsolete
- Consumer behavior claims: preferences shift; data should be recent unless the claim is about long-term patterns
- Economic data: depends on the claim; GDP figures from 5 years ago do not support claims about current economic conditions

A source that was Level 4 when published may effectively drop to Level 2 if it is too old for the claim being made.

---

## Output Format

The source quality assessment produces a structured report. Use the following template.

### Source Quality Assessment Report

**Analysis evaluated**: [title or description of the AI-generated output]
**Date of assessment**: [date]
**Assessor**: [name]

**Claim inventory**:
- Total factual claims identified: [n]
- Claims with cited sources: [n]
- Ungrounded claims (no source identifiable): [n]

**Source quality distribution**:
- Level 5 sources: [n]
- Level 4 sources: [n]
- Level 3 sources: [n]
- Level 2 sources: [n]
- Level 1 sources: [n]
- Sources not locatable: [n]

**Source-claim match results**:
- Adequate matches: [n]
- Marginal matches: [n]
- Inadequate matches: [n]

**Flags**:
- Independence concerns: [list]
- Conflict of interest concerns: [list]
- Currency concerns: [list]

**Overall source quality rating**:

| Rating | Criteria |
|---|---|
| Strong | All critical claims adequately sourced at Level 3+. No inadequate matches on strategic claims. No unresolved conflict of interest on key sources. |
| Adequate | Minor gaps on non-critical claims. All strategic claims sourced at Level 3+. Any marginal matches are on supporting rather than load-bearing claims. |
| Weak | One or more critical claims sourced below minimum level. Strategic claims rely on Level 2 sources. Independence or conflict of interest concerns on key claims. |
| Unacceptable | Strategic or decision-driving claims based on Level 1-2 sources. Multiple ungrounded claims. Sources cannot be verified. |

**Specific recommendations**: [which claims need better sourcing, what level of source would be required, whether the analysis can be used as-is or needs remediation]

---

## Worked Example: The Marketing Strategy Analysis

This example applies the full protocol to the scenario that motivated this method -- an LLM-generated marketing strategy analysis that recommended rapid-response marketing based on shortened advertising trend cycles.

### The AI Output (Reconstructed)

An LLM was asked to produce a marketing strategy analysis in the style of a top-tier consulting firm. Among its key claims:

1. "Advertising trend cycles have shortened dramatically, now averaging under one week in duration."
2. "Companies that adopt rapid-response marketing see 40% higher engagement rates."
3. "The shift toward micro-trends is driven by social media algorithm changes and declining consumer attention spans."
4. "Leading brands are already restructuring their marketing operations around weekly creative cycles."
5. "The traditional quarterly campaign planning model is obsolete for digital-first brands."

The analysis recommended that the company pivot to rapid-response marketing with weekly creative cycles, requiring significant restructuring of the marketing team and a budget reallocation of approximately 30% of the annual marketing spend.

### Step 1: Source Identification

| Claim | Source Cited | Locatable |
|---|---|---|
| Trend cycles under one week | "Industry analysis" from an ad agency blog | Yes, but it is a promotional blog post |
| 40% higher engagement | An ad tech vendor's case study | Yes, but it is sales material |
| Social media algorithm driving micro-trends | No specific source cited | No -- ungrounded |
| Leading brands restructuring to weekly cycles | Unnamed "industry experts" | No -- ungrounded |
| Quarterly planning obsolete | A marketing conference recap article | Yes, but it is a summary of panel opinions |

Result: 2 ungrounded claims, 3 claims with locatable sources.

### Step 2: Source Level Classification

| Source | Actual Level | How AI Presented It |
|---|---|---|
| Ad agency blog post | Level 2 (informal, promotional) | As "industry analysis" implying Level 4 |
| Ad tech vendor case study | Level 1 (vendor with financial interest in the claim) | As "research" implying Level 4 |
| Marketing conference recap | Level 2 (informal summary, no editorial review) | As expert consensus implying Level 3-4 |

### Step 3: Source-Claim Match Evaluation

| Claim | Claim Type | Required Level | Actual Level | Match |
|---|---|---|---|---|
| Trend cycles under one week | Factual assertion used in strategic decision | Level 4+ | Level 2 | **Inadequate** |
| 40% higher engagement | Quantitative projection used in financial modeling | Level 4+ | Level 1 | **Inadequate** |
| Social media algorithm driving micro-trends | Causal claim driving strategy change | Level 4+ | Ungrounded | **Inadequate** |
| Leading brands restructuring | Industry benchmark claim | Level 3+ | Ungrounded | **Inadequate** |
| Quarterly planning obsolete | Trend claim influencing resource allocation | Level 3+ | Level 2 | **Inadequate** |

Result: 0 adequate, 0 marginal, 5 inadequate.

### Step 4: Source Independence Check

The two locatable sources (ad agency blog and ad tech vendor case study) are not independent. Both come from companies that sell rapid-cycle marketing services. They have a shared financial incentive for the claim to be true.

### Step 5: Conflict of Interest Screen

- The ad agency blog is written by a company that sells rapid-response marketing services. Their business model depends on companies believing trend cycles are shortening.
- The ad tech vendor case study is sales material. The vendor profits from the marketing approach being recommended.
- Both sources fail the independence test. Neither is a disinterested observer of the trend they describe.

### Step 6: Currency Check

The sources cited are recent, so currency is not the issue in this case. The problem is level, not age.

### Assessment Report

**Analysis evaluated**: LLM-generated marketing strategy analysis recommending rapid-response marketing pivot
**Date of assessment**: [date of review]
**Assessor**: [reviewer]

**Claim inventory**:
- Total factual claims identified: 5
- Claims with cited sources: 3
- Ungrounded claims: 2

**Source quality distribution**:
- Level 5 sources: 0
- Level 4 sources: 0
- Level 3 sources: 0
- Level 2 sources: 2
- Level 1 sources: 1
- Sources not locatable: 0

**Source-claim match results**:
- Adequate matches: 0
- Marginal matches: 0
- Inadequate matches: 5

**Flags**:
- Independence concerns: Both cited sources have financial interest in the claim. Not independent.
- Conflict of interest concerns: Ad agency blog and ad tech vendor case study are both from entities that profit from the recommended strategy.
- Currency concerns: None (sources are recent).

**Overall source quality rating**: **Unacceptable**

All five claims driving the strategic recommendation are either ungrounded or sourced from Level 1-2 sources. The sources that do exist have direct financial conflicts of interest. No claim in this analysis meets the minimum source quality for the type of claim being made.

**Specific recommendations**:
- This analysis should not be used for the proposed budget reallocation decision in its current form.
- The trend cycle claim requires institutional research data (Level 4+), such as a documented study from a research firm with transparent methodology measuring actual campaign cycle lengths across a representative sample.
- The engagement rate claim requires independent empirical evidence, not vendor self-reporting. A peer-reviewed study or institutional research report would be the minimum acceptable source.
- The causal claim about social media algorithms requires research-grade evidence establishing the causal mechanism, not assumed reasoning.
- Before any resource allocation decision, the core claims must be re-sourced with Level 4+ evidence or the strategic recommendation must be withdrawn.

### What This Example Demonstrates

A trained BCG consultant would reject this analysis in minutes. Not because the facts are provably false -- some of the claims might even be directionally correct. The rejection is based on source quality: the evidence base is categorically inadequate for the decisions being recommended.

The protocol makes this judgment systematic. Without it, the analysis looks professional, reads fluently, and feels authoritative. With it, the gap between claimed authority and actual evidence quality becomes visible and specific.

---

## Integration with the Delegation Framework

Source quality assessment connects to the existing evaluation framework through the evidence strength dimension.

### Mapping to Evidence Strength Scores

The evidence strength dimension in the scoring sheet uses a 1-3 scale. Source quality assessment provides the operational definition for how to assign that score when evaluating AI-generated analysis.

| Source Quality Rating | Evidence Strength Score | Effect |
|---|---|---|
| Strong | 3 (strong) | Supports the current evidence strength rating. No adjustment needed. |
| Adequate | 2-3 (moderate to strong) | Minor gaps exist but are not decision-critical. No change to the delegation mode. |
| Weak | 1-2 (weak to moderate) | Critical claims are under-sourced. Triggers override rule 3: reduce authority one level. An analysis scored as `recommend` drops to `assist`. |
| Unacceptable | 1 (weak) | Strategic claims based on Level 1-2 sources. The analysis should not be used for the decision regardless of other scores. |

### Override Rule Integration

The scoring sheet defines override rule 3: "any weak evidence base in a consequential decision: reduce one autonomy level." Source quality assessment provides the concrete test for when this override applies.

An AI-generated analysis with:
- **Strong or adequate** source quality: the evidence strength score stands as assigned
- **Weak** source quality: the override fires, reducing the delegation mode by one level
- **Unacceptable** source quality: the analysis is not fit for use, independent of the delegation framework score

### Practical Sequence

When evaluating whether to delegate a decision to AI-generated analysis:

1. Score the decision using the existing scoring sheet (decision structure, risk level, scenario stability, evidence strength, governance readiness)
2. Apply the source quality assessment protocol to the AI-generated analysis
3. If source quality is weak, apply override rule 3 before determining the delegation mode
4. If source quality is unacceptable, stop -- the analysis needs remediation before the delegation question is relevant

---

## Application Guidance

### When to Apply This Protocol

Apply the full six-step protocol when:

- The AI-generated analysis will inform a resource allocation decision
- The analysis contains quantitative claims that will enter financial models
- The analysis makes causal claims that would change strategic direction
- The decision stakes are medium or high on the evaluation framework
- The analysis will be presented to senior leadership or external stakeholders

Apply an abbreviated check (Steps 1-3 only) when:

- The analysis is used for background context or orientation
- The claims are non-controversial and widely established
- The decision is low-stakes and reversible
- The analysis is one input among many, not the primary basis for a decision

### Common AI Source Quality Failures

Based on observed patterns, these are the most frequent source quality problems in AI-generated business analysis:

1. **Level inflation**: AI presents Level 2 sources as if they were Level 4. Blog posts become "industry analysis." Vendor whitepapers become "research." The presentation implies institutional authority that the source does not possess.

2. **Phantom consensus**: AI cites multiple sources that all trace back to the same original claim or data point, creating an appearance of independent confirmation that does not exist.

3. **Confidence-source mismatch**: AI expresses high confidence in claims supported by low-quality sources. The fluency and structure of the output implies a certainty that the evidence does not warrant.

4. **Fabricated citations**: AI cites sources that do not exist. This is a known LLM failure mode. Any citation must be verified as real before the source level can be assessed.

5. **Temporal mismatch**: AI uses outdated sources to support claims about current conditions without noting the time gap.

6. **Conflict of interest concealment**: AI cites a source without noting that the source has a financial interest in the claim being true. The user sees "according to a study by X" without knowing that X sells the product being studied.

### Training Value

This protocol is designed to be teachable. A business professional without consulting training can apply it by working through the six steps sequentially. With practice, the assessment becomes faster and more intuitive -- approaching the instinctive evaluation that trained consultants perform automatically.

The goal is not to make every business professional a source quality expert. The goal is to provide a structured method that prevents the most damaging failure mode: accepting AI-generated strategic analysis at face value because the output looks professional.
