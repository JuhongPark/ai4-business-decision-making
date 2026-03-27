# Think-Tank Report Draft

title: AI in Business Decision-Making
subtitle: A Scenario-Based Study of Human-AI Collaboration Across High-Stakes and Operational Domains
status: submission_ready_v1

## Introduction

Artificial intelligence is increasingly embedded in business decision processes, but adoption debates remain too broad to guide real institutional design. The central challenge is not whether AI can support decisions in the abstract. The real question is when organizations should use AI to assist, recommend, or automate decisions under different business conditions.

This report argues that AI should be studied by decision role and scenario condition rather than by hype-driven sector generalization. The suitability of AI depends on decision structure, evidence quality, downside risk, and governance burden. As a result, the same domain may tolerate higher AI autonomy under stable conditions but require stronger human control under stress or edge-case conditions.

The central principle of this report is simple: AI authority should be adaptive, not fixed. Organizations need escalation rules for when autonomy can increase and fallback rules for when autonomy must shrink.

This report should be read as a structured decision-governance study. It does not claim to provide universal empirical proof of return on investment across all domains. Its stronger contribution is to identify which category combinations justify which level of AI authority.

## Why Role Matters More Than Hype

The current public conversation often treats AI adoption as a binary choice between use and non-use. That framing is analytically weak. In practice, organizations must decide whether AI should function as an assistive tool, a recommending system, or an automated mechanism with bounded oversight. These roles create different tradeoffs in speed, consistency, explainability, safety, fairness, and accountability.

## Analytical Framework

This study uses three core AI roles:

- `assist`: AI supports human judgment with signals, summaries, or forecasts
- `recommend`: AI suggests actions that humans approve or override
- `automate with guardrails`: AI executes bounded decisions while humans monitor exceptions, audits, and drift

The framework evaluates these roles against decision structure, evidence strength, explainability needs, downside risk, and governance burden.

The report now formalizes this judgment through a six-part category system:

1. domain
2. decision structure
3. risk level
4. scenario condition
5. AI role
6. evidence strength

This taxonomy matters because it prevents the research from collapsing into vague case-by-case reasoning. The right unit of analysis is the category combination, not the domain label alone.

## Decision Matrix

| Domain | Baseline | Stress | Edge Case | Core Rule |
| --- | --- | --- | --- | --- |
| Operations | automate with guardrails | recommend or automate with guardrails | assist | automate only while data quality and routing stability hold |
| Finance | assist or tightly governed recommend | assist | assist | reduce autonomy when drift, subgroup impact, or macro instability rises |
| Healthcare | assist or tightly governed recommend | recommend | assist | reduce autonomy when safety uncertainty or incomplete information rises |

## Domain Recommendation Table

| Domain | Default Role | Escalation Condition | Fallback Trigger |
| --- | --- | --- | --- |
| Strategy | assist | bounded scope and stronger evidence | ambiguity and low measurability |
| Operations | automate with guardrails | stable data and bounded objectives | degraded telemetry or conflicting service goals |
| Finance | assist or tightly governed recommend | strong fairness controls and auditability | drift, subgroup anomaly, macro instability |
| Healthcare | assist or tightly governed recommend | clinician override and validated workflow support | incomplete information, atypical presentation |
| Investment | assist or tightly governed recommend | clear disclosure and suitability controls | suitability ambiguity or disclosure weakness |
| Product | assist or recommend | stable experimentation logic | ambiguous tradeoffs or weak signal quality |
| Marketing | recommend | bounded optimization and privacy controls | short-term optimization bias or privacy conflict |
| Market Research | assist | strong analyst review and transparency | weak sampling or hallucinated synthesis |

## Taxonomy-Based Usage Rules

The research supports seven practical rules.

1. structured plus low-risk plus baseline conditions can justify `recommend` or `automate with guardrails`
2. semi-structured plus medium-risk decisions usually justify `assist` or `recommend`
3. high-risk decisions default to `assist` or tightly governed `recommend`
4. stress conditions increase support value but do not automatically justify more automation
5. edge cases trigger fallback toward `assist`
6. weak evidence reduces allowable autonomy
7. strong evidence is necessary but not sufficient in high-risk domains

These rules make the report usable beyond the three scenario packs because they provide a transfer mechanism across domains.

## Evidence and Claim Discipline

The report distinguishes between:

- governance claims supported by regulatory frameworks, peer-reviewed work, and stronger scenario logic
- design claims supported by official company materials and workflow examples

This distinction matters because high-confidence claims in the report concern governance burden, restriction logic, and fallback design, not universal business impact.

## MIT Research Landscape

MIT research provides a useful bridge between conceptual theory and real organizational implementation. The most relevant MIT work clusters around three units. First, the MIT Center for Collective Intelligence, led by Thomas Malone with major contributions from Abdullah Almaatouq and Michelle Vaccaro, studies when human and AI capabilities combine productively. Their 2024 meta-analysis finds that human-AI combinations are not automatically better than the best standalone performer and are more consistently useful in creative tasks than in decision tasks. For this report, that result matters because it directly weakens any assumption that high-stakes business decisions should move toward more autonomy by default.

Second, MIT Sloan's digital economy research, especially work associated with Erik Brynjolfsson, Danielle Li, and Lindsey Raymond, shows that performance gains depend on organizational complements rather than model capability alone. This line includes both earlier work on data-driven decision-making and later work on generative AI in customer-support settings. The practical implication is that AI value emerges when task structure, worker learning, and workflow design are aligned. This supports the report's emphasis on evidence quality, scenario condition, and governance readiness instead of broad adoption claims.

Third, MIT Sloan research on hiring and organizational implementation deepens the governance argument. Danielle Li's hiring research shows that algorithm design can change both candidate quality and candidate diversity, which means that the design of AI-mediated screening systems is itself a governance choice. Kate Kellogg's work on algorithm use inside organizations shows that transparency and interpretability do not solve adoption problems automatically. Workers may second-guess, over-intervene in, or reshape algorithmic tools in ways that change realized performance. Taken together, the MIT evidence supports a conservative conclusion: organizations should assign AI authority by task type, workflow design, and governance capacity, not by the existence of a technically capable model alone.

MIT System Design and Management adds a related but distinct contribution. Official SDM materials show relevant research on AI commercialization strategy, AI-supported venture capital judgment, AI-assisted cybersecurity product evaluation, and AI accountability questions linked to data ownership and ethical system design. The SDM pattern is less centered on a single faculty research lab and more centered on thesis and applied systems work. That makes SDM especially useful for the implementation-facing side of this report. It reinforces the claim that AI should be designed as part of a larger sociotechnical system involving workflows, infrastructure, stakeholder incentives, and accountability mechanisms rather than treated as a standalone prediction tool.

## Cross-Domain Comparison

The broader field comparison shows that AI readiness is uneven across domains. Operations and marketing are the strongest candidates for bounded automation because their decisions are often repeated, measurable, and feedback-rich. Finance, healthcare, and investment offer high analytical upside but require governance-first deployment because decisions in these domains affect fairness, safety, access, and compliance. Strategy, product, and market research are strongest as augmentation domains where AI supports synthesis rather than replacing judgment.

This distinction should be interpreted carefully. In this report, high-confidence claims about governance burden and restriction logic rely mainly on regulatory and peer-reviewed sources, while some lower-risk domain illustrations rely more heavily on company documentation and technical materials.

## Scenario Methodology

The core research design compares four decision modes within baseline, stress, and edge-case scenarios:

1. human-only
2. AI assist
3. AI recommend
4. AI automate with guardrails

The first implementation focuses on three domains:

- operations
- finance
- healthcare

This mix provides contrast between lower-risk operational decisions and higher-risk regulated or safety-critical decisions.

## Operations Findings

Operations is the strongest automation candidate in the study. Under baseline conditions, automate-with-guardrails is defensible because routing and dispatch decisions are repeated, measurable, and well supported by feedback loops. Under stress conditions, AI remains valuable, but human override becomes more important because local optimization can damage broader service performance. Under edge-case conditions with degraded data or major disruption, the preferred mode falls back toward assist.

## Finance Findings

Finance is a high-value but restriction-heavy AI domain. Under baseline conditions, AI assist and tightly governed recommend can improve consistency and analytical capacity in underwriting and risk review. Under stress conditions, however, fairness exposure, macro uncertainty, and model-risk become more salient. In edge cases involving drift or subgroup impact, the preferred mode returns to assist because governance and accountability requirements dominate speed gains. The main fallback triggers in this domain are subgroup anomalies, drift signals, and unstable macro conditions that make historical patterning less trustworthy.

## Healthcare Findings

Healthcare demonstrates the strongest governance burden in the report. AI can support triage and clinical prioritization, especially under routine conditions or surge pressure. However, the domain remains safety-critical, and edge cases with incomplete information or unusual presentation justify a strong return to clinician-led judgment. The preferred mode is therefore assist or tightly governed recommend, not broad automation. Surge conditions justify stronger recommendation support, not full automation. The main fallback triggers are incomplete information, atypical presentation, and uncertainty about signal reliability.

## Cross-Scenario Findings

Three patterns recur across domains. First, baseline conditions tolerate more AI autonomy than stress or edge-case conditions. Second, stress conditions increase both the value of AI support and the cost of hidden model failure. Third, edge cases reverse the autonomy logic by making human-led judgment more valuable than automated consistency.

The strongest analytical result of the study is that AI autonomy should be scenario-sensitive rather than domain-static. Domain type matters, but scenario conditions decide whether authority should escalate or fall back.

## Governance and Restriction Logic

The report recommends a governance-first approach in high-stakes domains. Organizations should require stronger evidence before deployment, keep accountability clearly assigned, and define explicit fallback rules for stress and edge-case conditions. High-impact adoption claims should rely on regulator-backed, audited, or peer-reviewed evidence whenever possible.

Fallback planning should be treated as a managerial obligation. A system that performs well in baseline conditions but lacks a clear fallback design is not governance-ready.

The report therefore recommends a practical decision sequence:

1. classify the domain
2. classify the decision structure
3. classify the risk level
4. classify the scenario condition
5. check evidence strength
6. check governance readiness
7. assign the lowest justified AI authority

This is a conservative rule by design. If the category combination does not clearly justify greater autonomy, the organization should keep the system at a lower authority level.

## Strategic Recommendations

- Treat AI role selection as a governance decision, not only a technical decision
- Use bounded automation mainly in repeated, measurable, lower-risk environments
- Default to assist or tightly governed recommend in finance and healthcare
- Define escalation triggers and fallback triggers before deployment
- Build fallback logic for stress and edge-case scenarios before scaling autonomy
- Distinguish design claims from outcome claims and label evidence strength explicitly
- Use a category-based decision tree or scoring sheet before assigning AI authority

## Evidence Note

The report draws on mixed evidence types. Stronger evidence supports the claims made about finance, healthcare, investment, governance, and fairness-sensitive decisions. Moderate evidence supports many of the workflow and design examples in operations, marketing, product, and market research. Readers should therefore treat the report primarily as a structured decision-governance study rather than as a universal empirical proof of ROI across all domains.

## Conclusion

The report concludes that AI is most useful when organizations match autonomy level to domain structure, scenario condition, evidence quality, and governance capacity. Its central contribution is not a general claim that AI improves business outcomes everywhere. Its stronger and more defensible contribution is to show how organizations should decide when AI should assist, recommend, or automate, and when authority should be reduced again.

The scope boundary is important. This report does not offer live experimental validation across all domains, nor does it claim that the same autonomy logic should apply unchanged in every organization. The analysis is strongest where governance burden, restriction logic, and fallback design can be grounded in stronger regulatory and conceptual evidence.

The practical conclusion is therefore conservative by design: if a category combination does not clearly justify greater autonomy, organizations should keep AI at a lower authority level.
