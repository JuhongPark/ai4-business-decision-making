# Phase 3: Business Application Mapping

status: completed
phase_goal: Map where AI is used in business decision-making and identify which decision environments are most suitable for AI support.

## Mapping Logic

This phase uses the literature review to compare business functions on five criteria:

1. Decision type
2. Role of AI
3. Expected business value
4. Main risks
5. Required human oversight

## Application Map

| Business Function | Typical Decisions | AI Role | Expected Value | Main Risks | Oversight Level |
| --- | --- | --- | --- | --- | --- |
| Strategy | scenario analysis, market sensing, resource allocation support | pattern detection, forecasting, simulation support | improved signal detection and planning support | weak explainability, false confidence, poor transfer across contexts | high |
| Marketing | customer segmentation, churn prediction, pricing, recommendation | prediction, personalization, optimization | revenue growth, targeting efficiency, customer retention | bias in targeting, privacy concerns, overfitting to short-term metrics | medium |
| Finance | credit scoring, fraud detection, risk estimation, cash forecasting | classification, anomaly detection, forecasting | faster risk assessment and better consistency | unfair decisions, regulatory exposure, opaque model logic | high |
| Operations | demand forecasting, inventory planning, scheduling, maintenance | forecasting, optimization, automation support | efficiency, lower waste, improved responsiveness | brittle models, bad upstream data, local optimization problems | medium |
| Human Resources | resume screening, attrition prediction, workforce planning | ranking, prediction, pattern recognition | faster screening and workforce insight | discrimination risk, legal exposure, low transparency | high |

## Cross-Function Observations

### Observation 1: AI is strongest where decisions are frequent, structured, and data-rich

Marketing, finance, and operations appear to be the most mature application areas because they often involve repeated decisions, measurable outcomes, and large historical datasets.

### Observation 2: Oversight requirements increase when decisions affect rights, fairness, or organizational legitimacy

Finance and human resources require stronger oversight because decisions in these areas can directly affect access, opportunity, compliance, and reputational risk.

### Observation 3: Strategy remains an augmentation domain rather than an automation domain

Strategic decisions are less structured, more contextual, and more exposed to external uncertainty. AI may help with signal processing and scenario support, but final judgment remains highly managerial.

### Observation 4: Local optimization can conflict with broader business goals

In marketing and operations, AI can improve narrow metrics while harming longer-term customer trust, resilience, or cross-functional coordination. This means performance should be evaluated beyond single-model accuracy.

## Priority Areas for Case Analysis

Based on the mapping, the strongest case candidates should come from:

1. Marketing and personalization
2. Finance and risk assessment
3. Operations and supply chain forecasting
4. Human resources screening or talent analytics

These areas provide stronger visibility into both value creation and risk exposure than strategy alone.

## Implications for Phase 4

The case analysis should compare functions with different oversight needs. A useful design is to include at least one relatively structured domain and one higher-risk domain so the study can compare not only performance but also accountability demands.
