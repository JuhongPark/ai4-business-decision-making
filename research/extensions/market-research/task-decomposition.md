# Task Decomposition and Failure Mode Mapping: AI Market Research for Product Ideation

status: Phase 2 deliverable
date_created: 2026-04-11
purpose: decompose market research into discrete reasoning tasks, map predicted failure modes against the 25-type taxonomy, and assign initial authority levels using the delegation framework

## Decomposition Method

Market research for product ideation is decomposed into 18 discrete reasoning tasks across 6 stages. Each task is characterized by:

- **Input**: what information the task requires
- **Reasoning type**: the dominant inferential operation
- **Output**: what the task produces
- **Professional competence**: what the professional benchmark requires
- **Predicted failure modes**: which taxonomy failure types are most likely

The decomposition follows the stages identified in the research plan and uses the professional benchmark (professional-benchmark.md) as the quality reference.

## Task Inventory

### Stage 1: Environmental Scanning (3 tasks)

#### Task 1.1: Source Identification and Collection

- **Input**: Industry keywords, market boundaries, geographic scope
- **Reasoning type**: Source identification, relevance filtering
- **Output**: Curated source list with quality assessments
- **Professional competence**: Multiple independent source categories (industry data, customer data, regulatory data). Explicit inclusion/exclusion criteria.
- **Predicted failures**: Inadequate source quality (S3), Selection bias in sources (S5)
- **Delegation score**: Domain 2, Structure 2, Risk 1, Scenario 1, Evidence 2, Governance 2 = **10 (RECOMMEND)**
- **Rationale**: Structured task with low risk. AI excels at breadth of scanning. Human reviews source quality ratings.

#### Task 1.2: Regulatory and Macro Environment Assessment

- **Input**: Policy announcements, regulatory texts, economic indicators
- **Reasoning type**: Normative analysis, temporal awareness
- **Output**: Regulatory landscape summary with compliance implications
- **Professional competence**: Current sources. Correct interpretation of regulatory language. Jurisdiction-specific awareness.
- **Predicted failures**: Outdated sources (S4), Legal norm violation (N1), Temporal confusion (St3)
- **Delegation score**: Domain 2, Structure 2, Risk 3, Scenario 2, Evidence 2, Governance 2 = **13 (RECOMMEND/AUTOMATE)**
- **Override**: High risk (compliance) + moderate governance → cap at **RECOMMEND**
- **Rationale**: Regulatory errors carry compliance risk. AI drafts; human validates legal accuracy.

#### Task 1.3: Signal-Noise Discrimination

- **Input**: Collected sources, trend indicators, anomaly candidates
- **Reasoning type**: Pattern recognition, alternative hypothesis testing
- **Output**: Filtered signal list with stated reasoning for inclusion/exclusion
- **Professional competence**: Distinguish durable signals from noise. Test apparent patterns against alternative explanations.
- **Predicted failures**: Overgeneralization (I3), Confirmation bias amplification (Sy1), Missing counterfactual (I4)
- **Delegation score**: Domain 2, Structure 1, Risk 2, Scenario 2, Evidence 1, Governance 2 = **10 (RECOMMEND)**
- **Override**: Weak evidence → reduce to **ASSIST**
- **Rationale**: Judgment-intensive. AI lacks the contextual knowledge to distinguish signals reliably.

### Stage 2: Trend Identification (3 tasks)

#### Task 2.1: Trend Pattern Recognition

- **Input**: Temporal data series, market indicators, industry reports
- **Reasoning type**: Temporal analysis, pattern recognition
- **Output**: Identified trend patterns with direction, magnitude, and supporting evidence
- **Professional competence**: At least three data points over time. Distinguish acceleration, deceleration, cyclical patterns.
- **Predicted failures**: Overgeneralization (I3), Overconfidence (C1), Anchoring on irrelevant precedent (I5)
- **Delegation score**: Domain 2, Structure 2, Risk 2, Scenario 2, Evidence 2, Governance 2 = **12 (RECOMMEND/AUTOMATE)**
- **Override**: None
- **Rationale**: Quantitative pattern detection is an AI strength. Verification focuses on evidence sufficiency.

#### Task 2.2: Trend Trajectory Estimation

- **Input**: Trend patterns, historical analogies, external forecasts
- **Reasoning type**: Predictive inference, analogical reasoning
- **Output**: Trajectory estimates with ranges and key assumptions
- **Professional competence**: Ranges, not point estimates. Assumptions stated. Historical analogies with acknowledged differences.
- **Predicted failures**: False precision (C2), Certainty laundering (C3), Anchoring on irrelevant precedent (I5)
- **Delegation score**: Domain 2, Structure 1, Risk 2, Scenario 2, Evidence 1, Governance 2 = **10 (RECOMMEND)**
- **Override**: Weak evidence → reduce to **ASSIST**
- **Rationale**: Prediction under uncertainty. AI tends toward false precision. Human must validate assumptions.

#### Task 2.3: Trend Significance Assessment

- **Input**: Trend patterns, business context, strategic priorities
- **Reasoning type**: Evaluative judgment, contextualization
- **Output**: Prioritized trend list with business relevance assessment
- **Professional competence**: Connect trends to business implications. Distinguish "interesting" from "actionable."
- **Predicted failures**: Audience-optimized reasoning (Sy4), Question-shaped answers (Sy2), Stakeholder blindness (St4)
- **Delegation score**: Domain 2, Structure 1, Risk 2, Scenario 2, Evidence 1, Governance 2 = **10 (RECOMMEND)**
- **Override**: Weak evidence → reduce to **ASSIST**
- **Rationale**: Strategic judgment task. AI optimizes for user expectation, not business truth.

### Stage 3: Customer Need Extraction (3 tasks)

#### Task 3.1: Customer Feedback Synthesis

- **Input**: Survey data, reviews, interview transcripts, behavioral data
- **Reasoning type**: Qualitative interpretation, theme extraction
- **Output**: Categorized need statements with evidence links
- **Professional competence**: Trace each need to identifiable evidence. Distinguish stated from latent needs. Label inference types.
- **Predicted failures**: Overgeneralization (I3), Inadequate source quality (S3), Fabricated sources (S1)
- **Delegation score**: Domain 2, Structure 1, Risk 2, Scenario 1, Evidence 1, Governance 2 = **9 (ASSIST/RECOMMEND)**
- **Override**: Weak evidence → cap at **ASSIST**
- **Rationale**: Interpretive task where AI-generated "insights" may not trace to real customer evidence.

#### Task 3.2: Latent Need Identification

- **Input**: Behavioral data, contextual observation, JTBD framework
- **Reasoning type**: Abductive inference, creative interpretation
- **Output**: Hypothesized latent needs with supporting reasoning
- **Professional competence**: Label abductive inferences explicitly. Distinguish inference from observation. Apply JTBD causal depth.
- **Predicted failures**: Question-shaped answers (Sy2), Circular reasoning (St1), Non sequitur (I1), False causation (I2)
- **Delegation score**: Domain 2, Structure 1, Risk 2, Scenario 2, Evidence 1, Governance 1 = **9 (ASSIST/RECOMMEND)**
- **Override**: Weak evidence + weak governance → cap at **ASSIST**
- **Rationale**: Highest interpretive burden task. AI excels at generating plausible-sounding latent needs that lack causal grounding.

#### Task 3.3: Need Prioritization

- **Input**: Need statements, market size indicators, strategic fit criteria
- **Reasoning type**: Multi-criteria evaluation, weighting
- **Output**: Prioritized need list with scoring rationale
- **Professional competence**: Explicit criteria. Stated weights. Sensitivity analysis on priorities.
- **Predicted failures**: Uniform confidence (C4), Confirmation bias amplification (Sy1), Stakeholder blindness (St4)
- **Delegation score**: Domain 2, Structure 2, Risk 2, Scenario 1, Evidence 2, Governance 2 = **11 (RECOMMEND)**
- **Override**: None
- **Rationale**: Semi-structured task amenable to AI. Verification focuses on criteria transparency and bias.

### Stage 4: Competitive Mapping (3 tasks)

#### Task 4.1: Competitor Capability Assessment

- **Input**: Public filings, product data, analyst reports, news
- **Reasoning type**: Comparative analysis, information synthesis
- **Output**: Competitor capability profiles with source citations
- **Professional competence**: Current sources. Date all information. Separate demonstrated capability from inferred intent.
- **Predicted failures**: Outdated sources (S4), Survivorship bias (St5), Misrepresented sources (S2)
- **Delegation score**: Domain 2, Structure 2, Risk 1, Scenario 1, Evidence 2, Governance 2 = **10 (RECOMMEND)**
- **Rationale**: Structured data synthesis. AI performs well with verification on source currency.

#### Task 4.2: Competitive White Space Identification

- **Input**: Capability map, need map, market structure
- **Reasoning type**: Gap analysis, strategic inference
- **Output**: Identified gaps in competitive landscape with opportunity assessment
- **Professional competence**: Multi-dimensional comparison. Acknowledge information gaps. Test gap claims against competitive response scenarios.
- **Predicted failures**: Scope mismatch (St2), Stakeholder blindness (St4), Confirmation bias amplification (Sy1)
- **Delegation score**: Domain 2, Structure 1, Risk 2, Scenario 2, Evidence 1, Governance 2 = **10 (RECOMMEND)**
- **Override**: Weak evidence → reduce to **ASSIST**
- **Rationale**: Strategic inference with high interpretive burden. AI-identified "white spaces" may reflect data gaps rather than market gaps.

#### Task 4.3: Competitive Response Prediction

- **Input**: Competitor profiles, strategic history, market dynamics
- **Reasoning type**: Predictive inference, game-theoretic reasoning
- **Output**: Predicted competitive responses to market entry or product launch
- **Professional competence**: Consider multiple response scenarios. Weight by competitor capability and strategic priority. Acknowledge prediction uncertainty.
- **Predicted failures**: Overconfidence (C1), False causation (I2), Anchoring on irrelevant precedent (I5)
- **Delegation score**: Domain 2, Structure 1, Risk 2, Scenario 3, Evidence 1, Governance 2 = **11 (RECOMMEND)**
- **Override**: Edge-case scenario → cap at **ASSIST**
- **Rationale**: Prediction about intentional actors under uncertainty. High failure risk.

### Stage 5: Market Sizing and Opportunity Assessment (3 tasks)

#### Task 5.1: Market Size Estimation

- **Input**: Market data, demographics, analogies, economic indicators
- **Reasoning type**: Quantitative estimation, assumption construction
- **Output**: Market size estimates with assumptions, ranges, and methodology
- **Professional competence**: Explicit assumptions. Multiple estimation methods. Ranges with stated confidence.
- **Predicted failures**: False precision (C2), Overconfidence (C1), Certainty laundering (C3)
- **Delegation score**: Domain 2, Structure 2, Risk 2, Scenario 1, Evidence 2, Governance 2 = **11 (RECOMMEND)**
- **Rationale**: Quantitative task where AI performs well but tends toward false precision. Verification on assumptions.

#### Task 5.2: Willingness-to-Pay Assessment

- **Input**: Survey data, pricing analogies, conjoint analysis results
- **Reasoning type**: Economic inference, analogical reasoning
- **Output**: Price sensitivity analysis with supporting evidence
- **Professional competence**: Methodology stated. Analogies with acknowledged differences. Uncertainty ranges.
- **Predicted failures**: Certainty laundering (C3), Anchoring on irrelevant precedent (I5), Inadequate source quality (S3)
- **Delegation score**: Domain 2, Structure 1, Risk 2, Scenario 2, Evidence 1, Governance 2 = **10 (RECOMMEND)**
- **Override**: Weak evidence → reduce to **ASSIST**
- **Rationale**: Pricing decisions have direct revenue impact. Evidence base is typically thin.

#### Task 5.3: Opportunity Prioritization

- **Input**: Market sizes, WTP estimates, competitive landscape, strategic fit
- **Reasoning type**: Multi-criteria evaluation with weighted scoring
- **Output**: Ranked opportunity list with decision rationale
- **Professional competence**: Explicit criteria and weights. Sensitivity analysis. Acknowledgment of estimation uncertainty propagation.
- **Predicted failures**: Uniform confidence (C4), Composition fallacy (I6), Progressive sycophancy (Sy3)
- **Delegation score**: Domain 2, Structure 2, Risk 2, Scenario 1, Evidence 2, Governance 2 = **11 (RECOMMEND)**
- **Rationale**: Structured evaluation. Risk is in the confidence expressed over uncertain inputs.

### Stage 6: Concept Generation and Screening (3 tasks)

#### Task 6.1: Product Concept Generation

- **Input**: Need map, capability map, trend analysis, opportunity assessment
- **Reasoning type**: Creative synthesis, divergent thinking
- **Output**: Product concept descriptions with need-concept traceability
- **Professional competence**: Trace concepts to identified needs. Generate diverse concepts, not variations on a theme. Include non-obvious combinations.
- **Predicted failures**: Confirmation bias amplification (Sy1), Progressive sycophancy (Sy3), Audience-optimized reasoning (Sy4)
- **Delegation score**: Domain 2, Structure 1, Risk 2, Scenario 2, Evidence 1, Governance 1 = **9 (ASSIST/RECOMMEND)**
- **Override**: Weak governance → cap at **ASSIST**
- **Rationale**: Creative task where sycophancy is most dangerous. AI confirms existing hypotheses rather than generating genuinely novel concepts.

#### Task 6.2: Concept Feasibility Assessment

- **Input**: Concept descriptions, technical constraints, market data, financial models
- **Reasoning type**: Multi-criteria assessment, constraint checking
- **Output**: Feasibility evaluations with explicit criteria and identified risks
- **Professional competence**: Stated criteria. Technical, market, and financial dimensions. Identified showstoppers.
- **Predicted failures**: Stakeholder blindness (St4), Scope mismatch (St2), Overconfidence (C1)
- **Delegation score**: Domain 2, Structure 2, Risk 2, Scenario 1, Evidence 2, Governance 2 = **11 (RECOMMEND)**
- **Rationale**: Structured evaluation amenable to AI with human review on constraint completeness.

#### Task 6.3: Concept Screening and Ranking

- **Input**: Feasibility evaluations, strategic fit, opportunity sizes
- **Reasoning type**: Comparative evaluation, decision framing
- **Output**: Ranked concept list with go/no-go recommendations
- **Professional competence**: Disconfirmation testing. Framing resistance. Clear separation of evidence-based assessment from judgment calls.
- **Predicted failures**: Progressive sycophancy (Sy3), Question-shaped answers (Sy2), Uniform confidence (C4)
- **Delegation score**: Domain 2, Structure 1, Risk 3, Scenario 2, Evidence 1, Governance 2 = **11 (RECOMMEND)**
- **Override**: High risk + weak evidence → cap at **ASSIST**
- **Rationale**: Go/no-go decisions with significant resource implications. AI recommendation must be independently verified.

## Failure Mode Prediction Matrix

### Predicted Frequency by Category and Stage

| Stage | Source | Inferential | Normative | Calibration | Structural | Sycophantic | Total Hot Zones |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Environmental scanning | HIGH | Medium | Medium | Low | Low | Medium | 2 |
| Trend identification | Medium | HIGH | Low | HIGH | Medium | Medium | 3 |
| Customer need extraction | Medium | HIGH | Low | Medium | Medium | HIGH | 3 |
| Competitive mapping | HIGH | Medium | Low | Medium | HIGH | Medium | 3 |
| Market sizing | Medium | Medium | Low | HIGH | Medium | Medium | 2 |
| Concept generation | Low | Medium | Medium | Medium | Medium | HIGH | 2 |

### Top 10 Predicted Hot Zones (Task-Failure Combinations)

These are the task-failure combinations expected to be most frequent and most dangerous:

| Rank | Task | Failure Type | Risk | Detectability | Why This Is a Hot Zone |
| --- | --- | --- | --- | --- | --- |
| 1 | 3.2 Latent need identification | Question-shaped answers (Sy2) | High | Hard | AI restates the user's hypothesis as a discovered need. Appears insightful; is circular. |
| 2 | 6.1 Concept generation | Progressive sycophancy (Sy3) | High | Hard | AI generates concepts that progressively align with user preference signals. Diversity collapses. |
| 3 | 5.1 Market size estimation | False precision (C2) | High | Moderate | AI produces precise-looking estimates ($4.2B) from uncertain inputs. Precision implies rigor that doesn't exist. |
| 4 | 2.2 Trend trajectory estimation | Certainty laundering (C3) | High | Hard | Uncertain inputs become definitive outputs through multi-step processing. Each step strips uncertainty markers. |
| 5 | 1.1 Source identification | Selection bias in sources (S5) | High | Moderate | AI selects sources that support the emerging narrative rather than sources that test it. |
| 6 | 3.1 Feedback synthesis | Overgeneralization (I3) | High | Moderate | AI generalizes from thin evidence to broad customer claims. "Customers want X" from limited signals. |
| 7 | 4.2 White space identification | Scope mismatch (St2) | High | Hard | AI identifies "gaps" that reflect data availability, not market reality. |
| 8 | 6.3 Concept screening | Uniform confidence (C4) | Moderate | Hard | All concepts receive similar-strength recommendations. Differentiation is insufficient. |
| 9 | 2.3 Trend significance | Audience-optimized reasoning (Sy4) | High | Hard | AI emphasizes trends that align with the user's industry or strategic interests. |
| 10 | 4.3 Competitive response | Overconfidence (C1) | High | Moderate | AI predicts competitive moves with certainty that exceeds the available evidence. |

## Authority Level Summary

| Authority Level | Tasks | Count | Percentage |
| --- | --- | --- | --- |
| ASSIST (after overrides) | 1.3, 2.2, 2.3, 3.1, 3.2, 4.2, 4.3, 5.2, 6.1, 6.3 | 10 | 56% |
| RECOMMEND | 1.1, 1.2, 2.1, 3.3, 4.1, 5.1, 5.3, 6.2 | 8 | 44% |
| AUTOMATE WITH GUARDRAILS | (none) | 0 | 0% |

**Key finding**: 56% of market research tasks require ASSIST-level authority after override rules are applied, even though raw scores would place several at RECOMMEND or AUTOMATE levels. The override rules — particularly weak evidence and edge-case scenario — drive most reductions.

**No market research task qualifies for automation.** Even the most structured tasks (source collection, market size estimation) require human verification due to the domain's inherent low verifiability and high interpretive burden.

## Verification Priority Ordering

Based on the failure mode prediction, verification effort should be prioritized:

1. **Sycophantic failures in customer need extraction and concept generation** — highest combined risk and lowest detectability. These failures make AI market research confirm what the user already believes rather than testing it.

2. **Calibration failures in market sizing and trend estimation** — high risk with moderate detectability. These failures make uncertain conclusions look precise and reliable.

3. **Source failures in environmental scanning and competitive mapping** — high risk with moderate detectability. These failures undermine the evidence base for all downstream analysis.

4. **Inferential failures in trend identification and need extraction** — high risk with moderate detectability. These failures produce conclusions that do not follow from the evidence.

5. **Structural failures in competitive mapping and concept screening** — moderate to high risk with hard detectability. These failures produce analyses that are internally consistent but framed incorrectly.

## Connection to Phase 3

This task decomposition and failure mode prediction matrix provide the basis for Phase 3 (Empirical Testing). The predicted hot zones guide scenario design: each scenario should be calibrated to expose specific predicted failure types, and observed failure frequencies will be compared against these predictions to identify surprises — failures that are more or less common than predicted, and failures not captured by the existing taxonomy.
