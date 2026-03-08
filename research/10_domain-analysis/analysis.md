# Phase 10: Cross-Domain Analysis

status: completed
scope: strategy, operations, finance, healthcare, investment, product, marketing, market research
method: common framework using decision type, AI role, value, risk, recommended autonomy, evidence strength, and research priority

## Cross-Domain Comparison

| Field | Typical Decisions | Primary AI Role | Main Value | Main Risk | Recommended Autonomy | Evidence Strength | Research Priority |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Strategy | scenario analysis, competitive sensing, portfolio prioritization | synthesis, forecasting, simulation support | broader signal processing and option generation | false confidence, weak transferability, opaque reasoning | assist | moderate | medium |
| Operations | routing, scheduling, maintenance, inventory, demand forecasting | optimization, prediction, control support | measurable efficiency and responsiveness | brittle models, local optimization, bad upstream data | automate with guardrails | moderate | medium |
| Finance | underwriting, fraud detection, risk scoring, cash forecasting | classification, anomaly detection, recommendation support | faster and more consistent risk evaluation | fairness, compliance, model-risk, explainability failures | assist or tightly governed recommend | strong | high |
| Healthcare | diagnosis support, triage, imaging, documentation, care pathway support | prediction, classification, clinical decision support | earlier detection, workflow efficiency, support for clinical judgment | patient safety, bias, liability, transparency, validation failure | assist or tightly governed recommend | strong | high |
| Investment | portfolio allocation, robo-advice, surveillance, risk profiling | recommendation, optimization, pattern detection | scalable advisory support and faster monitoring | conflicts of interest, investor harm, suitability concerns, fraud amplification | assist or tightly governed recommend | strong | high |
| Product | roadmap prioritization, feature discovery, experimentation, user feedback synthesis | synthesis, clustering, experimentation support | faster learning loops and prioritization support | proxy metrics, user misread, overfitting to noisy signals | assist or recommend | moderate | medium |
| Marketing | targeting, segmentation, personalization, pricing, campaign optimization | prediction, recommendation, experimentation support | conversion efficiency, retention, personalization at scale | privacy, bias, short-term optimization, manipulation concerns | recommend or automate with guardrails | moderate | medium |
| Market Research | survey coding, insight extraction, segmentation, trend detection | clustering, synthesis, summarization, signal detection | faster analysis of large qualitative and quantitative datasets | hallucinated insights, weak sampling assumptions, false patterns | assist | weak to moderate | medium |

## Field-by-Field Interpretation

### Strategy

Strategy is a weak automation domain and a strong augmentation domain. AI can improve scanning, pattern aggregation, and scenario support, but strategic decisions remain context-heavy and payoff-sensitive. The main danger is not only error but unwarranted managerial confidence in synthetic coherence.

### Operations

Operations is one of the strongest candidates for controlled automation because decisions are often repeated, measurable, and bounded by operational objectives. The main caveat is that local optimization can degrade broader system performance when data quality or constraints are incomplete.

### Finance

Finance remains a high-value but high-risk domain. AI is useful for pattern detection, fraud monitoring, underwriting support, and forecasting, but these decisions often affect access, fairness, and compliance. Strong governance and explicit accountability are required before firms move beyond recommendation support.

### Healthcare

Healthcare combines high analytical upside with very high consequence risk. FDA materials on AI-enabled medical devices and software as a medical device make clear that safety, effectiveness, transparency, and lifecycle evidence are central. This domain should default to assist or tightly governed recommend, not broad automation.

### Investment

Investment decisions are analytically attractive for AI because they involve high data volume and repeatable advisory processes. At the same time, SEC and Investor.gov materials show that automated investment advice raises suitability, disclosure, conflict-of-interest, and investor-protection issues. This is a governance-heavy domain, not an automation-first domain.

### Product

Product management is a strong synthesis domain. AI can help summarize feedback, identify themes, support experimentation, and accelerate discovery work. However, product decisions often depend on ambiguous user needs, strategic judgment, and organizational tradeoffs, so AI should usually remain assist or recommend rather than operate autonomously.

### Marketing

Marketing is one of the strongest commercial domains for AI because it supports repeated targeting, experimentation, and personalization decisions. Still, privacy, bias, and metric gaming remain important risks. Guardrailed automation may be justified in tightly bounded cases, but firms should avoid optimizing only for short-term conversion.

### Market Research

Market research benefits from AI through coding, summarization, clustering, and trend detection across large datasets. However, this is also a domain where synthetic fluency can disguise poor inference. AI should help analysts work faster, not replace research design, sampling logic, or interpretive judgment.

## Synthesis

### Best Immediate Fit

- operations
- marketing

These fields are the strongest candidates for controlled automation or recommendation because they often involve repeated, measurable decisions with clearer feedback loops.

### Best High-Value but High-Risk Fit

- finance
- healthcare
- investment

These domains may produce major value from AI, but they should be treated as governance-first domains. Evidence quality, compliance exposure, and explainability requirements are too important for casual deployment.

### Best Augmentation Domains

- strategy
- product
- market research

These areas benefit most from AI as a synthesis and insight-support tool rather than an autonomous decision engine.

## Final Interpretation

The broad field comparison reinforces the core logic of the research: AI readiness is not determined by enthusiasm or technical capability alone. It is determined by the structure of the decision, the quality of evidence available, the severity of downside risk, and the organization’s ability to govern the system responsibly.
