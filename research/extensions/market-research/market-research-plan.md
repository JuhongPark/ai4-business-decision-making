# Research Plan: Reasoning Verification in AI-Autonomous Market Research for Product Ideation

status: draft
scope: extension of core reasoning trust verification framework applied to the market research domain
date_started: 2026-04-10
purpose: investigate how reasoning trust verification methods apply when AI systems autonomously conduct market research and generate product ideas, producing domain-specific failure cases, a verification framework, and practitioner guidance

## Research Background

The core repository established two linked contributions. First, a 6-dimensional delegation framework determining when firms should assign assist, recommend, or automate authority to AI systems in business decisions, grounded in 71 documented governance failures. Second, a reasoning failure taxonomy classifying 25 failure types across six categories (Source, Inferential, Normative, Calibration, Structural, Sycophantic), each with definitions, business examples, detection questions, risk levels, and detectability assessments.

The delegation framework answers **when a human should review AI output**. The reasoning failure taxonomy answers **what that human should look for**. The verification protocols (source quality, inferential validity, normative assessment, confidence calibration) answer **how that human should conduct the review**.

The cross-domain analysis (`research/core/domain-analysis/analysis.md`) classified market research as a domain with assist-level recommended autonomy, weak to moderate evidence strength, and a specific risk that "synthetic fluency can disguise poor inference." This assessment was correct but preliminary. It did not examine the internal reasoning structure of AI-conducted market research or test the verification framework against market-research-specific failure modes.

This extension takes a single applied domain — market research for product ideation — and uses it as a rigorous test environment for the reasoning trust verification framework. The research is motivated by a practical observation: AI systems are increasingly capable of executing the full market research workflow (environmental scanning, trend identification, customer need extraction, competitive mapping, opportunity sizing, and concept generation), but the reasoning quality of these outputs is largely unexamined. Firms are beginning to use AI-generated market intelligence for product decisions without methods to verify whether the underlying analysis meets professional standards.

The researcher's prior consulting experience provides a concrete professional benchmark for what constitutes defensible market research reasoning. This professional standard becomes the evaluation baseline against which AI market research outputs are assessed.

## Research Question

primary_question: How should firms verify the reasoning quality of AI-generated market research and product ideation, and what domain-specific failure modes emerge when AI systems autonomously conduct market analysis?

## Supporting Questions

1. What does professional-grade market research reasoning look like when decomposed into discrete reasoning tasks, and which tasks require which forms of analytical competence?
2. Which of the 25 failure types in the reasoning failure taxonomy are most prevalent when AI systems conduct market research, and do market-research-specific failure modes exist that the current taxonomy does not capture?
3. How accurately can non-expert practitioners detect reasoning failures in AI-generated market research using the verification framework, compared to detection without the framework?
4. What is the cost-benefit profile of AI market research with systematic verification versus AI market research accepted without verification versus traditional human-only market research?
5. Which market research tasks belong at assist, recommend, or automate authority levels, and how do the delegation framework dimensions interact with task-level reasoning quality?
6. How does the information structure of market research (high interpretive burden, low verifiability, fast-changing environment) shape the specific verification requirements?

## Working Argument

AI systems can now execute many of the mechanical steps in market research: scanning sources, summarizing trends, extracting themes from customer data, sizing markets, and generating product concepts. The outputs read like professional analysis. But reading like professional analysis and being professional analysis are different things. Professional market research reasoning requires source discrimination, inferential discipline, normative awareness of industry context, calibrated confidence proportional to evidence quality, structurally sound analytical architecture, and resistance to framing effects. These are precisely the capabilities that the reasoning failure taxonomy was designed to assess.

The central argument is that market research is an especially demanding test domain for reasoning verification because it combines several properties that amplify verification difficulty:

- **Low verifiability**: Market trends, customer needs, and competitive positioning cannot be checked against a definitive reference source the way legal citations or financial figures can. The truth is distributed, ambiguous, and contested.
- **High interpretive burden**: Raw market data requires substantial interpretation before it becomes actionable insight. The gap between data and decision is wide, creating more surface area for inferential failures.
- **Temporal sensitivity**: Market conditions change rapidly. Outdated sources and temporal confusion are structurally more likely than in domains with stable reference data.
- **Sycophancy vulnerability**: Product ideation is inherently aspirational. When a product manager asks AI to explore an opportunity, the system faces strong incentives to confirm the opportunity rather than challenge it. Confirmation bias amplification and question-shaped answers are predictably prevalent.
- **Professional standard ambiguity**: Unlike finance (where regulatory standards define acceptable practice) or healthcare (where clinical evidence hierarchies are established), market research has weaker codified professional standards. This makes professional standard violations harder to detect because the benchmark is less explicit.

These properties make market research both a high-value test domain for the verification framework and a domain where verification matters most for practitioners who lack the professional training to assess quality independently.

## Conceptual Frame

This extension operates at the intersection of three analytical layers.

### Layer 1: Task Decomposition

Market research for product ideation is decomposed into discrete reasoning tasks. Each task is characterized by its information inputs, reasoning operations, output form, and the professional competence it requires. This decomposition provides the unit of analysis for failure mode mapping.

| Market Research Stage | Primary Reasoning Tasks | Dominant Information Properties |
| --- | --- | --- |
| Environmental scanning | Source identification, relevance filtering, signal-versus-noise discrimination | High volume, low verifiability, mixed quality |
| Trend identification | Pattern recognition, temporal analysis, magnitude estimation | Temporal sensitivity, selection bias risk |
| Customer need extraction | Qualitative interpretation, need hierarchy construction, latent need inference | High interpretive burden, sycophancy vulnerability |
| Competitive mapping | Comparative analysis, capability assessment, strategic inference | Outdated source risk, survivorship bias risk |
| Market sizing and opportunity assessment | Quantitative estimation, assumption construction, sensitivity analysis | False precision risk, overconfidence risk |
| Concept generation and screening | Creative synthesis, feasibility assessment, fit evaluation | Confirmation bias risk, normative blind spots |

### Layer 2: Failure Mode Mapping

Each reasoning task is mapped against the 25-type reasoning failure taxonomy to identify which failure types are most probable, most dangerous, and most detectable at each stage. This mapping produces a domain-specific risk profile that guides verification priority ordering.

### Layer 3: Verification Framework Application

The existing verification methods (source quality assessment, inferential validity checking, normative assessment, confidence calibration) are applied to AI market research outputs. The research tests whether these methods are sufficient for the market research domain or whether domain-specific verification procedures are needed.

## Scope Boundaries

### In scope

- AI-generated market research and product ideation as the test domain for reasoning verification
- Application and extension of the existing 25-type reasoning failure taxonomy to market research outputs
- Empirical testing of AI market research quality using current frontier LLMs on representative market research tasks
- Development of market-research-specific verification checklists and practitioner tools
- Connection to the delegation framework for task-level authority assignment
- Connection to the information structure extension for domain-level information property analysis

### Out of scope

- Building a production-grade AI market research agent (the pipeline is a research instrument, not a product)
- Comprehensive evaluation of AI agent architectures (CrewAI, LangGraph, AutoGPT are referenced for context, not benchmarked)
- General-purpose product management methodology (the focus is on the verification of AI reasoning in market research, not on market research methodology per se)
- Real-time market intelligence systems or competitive monitoring infrastructure
- Consumer-facing product recommendation systems (the focus is on upstream product ideation, not downstream personalization)

## Research Design

### Method

This extension uses an empirically grounded framework development method that combines:

- **Professional benchmark construction**: codifying what constitutes defensible market research reasoning based on consulting practice and methodology literature
- **Task decomposition analysis**: breaking market research into discrete reasoning tasks amenable to individual assessment
- **Empirical failure cataloging**: running AI systems through representative market research scenarios and cataloging reasoning failures using the taxonomy
- **Verification framework testing**: applying existing verification methods to AI market research outputs and assessing detection rates
- **Practitioner simulation**: testing whether non-expert users can apply the verification framework to detect failures that they would otherwise accept

### Unit of Analysis

The primary unit of analysis is the **discrete reasoning task within a market research workflow**. Each task produces a specific output (a source assessment, a trend claim, a need statement, a market size estimate, a concept description) that can be evaluated for reasoning quality using the taxonomy.

The secondary unit is the **compound market research output** — a complete market analysis or product concept brief — evaluated for structural and cross-category failures that emerge only at the integrated level.

### Analytical Sequence

#### Phase 1: Professional Benchmark and Literature Landscape (Weeks 1-3)

Objective: establish what professional-grade market research reasoning looks like and map the relevant literature.

1. Codify the professional reasoning standard for market research based on consulting practice and methodology literature. Define the specific reasoning operations that distinguish professional-grade analysis from amateur analysis at each stage.
2. Survey the literature on AI and innovation, market research methodology, AI agent architectures, and reasoning quality assessment. Map gaps and connections to existing repository literature.
3. Construct a literature mapping table linking each literature cluster to specific research questions and existing repository assets.

Deliverable: professional benchmark memo and literature landscape document.

#### Phase 2: Task Decomposition and Failure Mode Mapping (Weeks 3-5)

Objective: decompose market research into assessable reasoning tasks and map predicted failure modes.

1. Decompose market research for product ideation into 15-25 discrete reasoning tasks across the six stages identified in the conceptual frame.
2. For each task, identify: required inputs, reasoning operations performed, output form, professional competence required, and predicted failure modes from the taxonomy.
3. Generate a predicted failure frequency matrix mapping the 25 failure types against market research tasks. Identify the hot zones — task-failure-type combinations expected to be most frequent and most dangerous.
4. Apply the delegation framework to each task: score on the relevant dimensions and assign initial authority recommendations.

Deliverable: task decomposition table and failure mode prediction matrix.

#### Phase 3: Empirical Testing (Weeks 5-9)

Objective: run AI systems through representative market research scenarios and catalog actual failures.

1. Design 8-12 market research scenarios spanning the six stages. Include scenarios calibrated to expose specific failure types: scenarios with contested data (to test source discrimination), scenarios requiring counterfactual analysis (to test inferential rigor), scenarios with cultural or regulatory sensitivities (to test normative awareness), scenarios with thin evidence (to test calibration), scenarios with structural complexity (to test analytical architecture), and scenarios framed to invite agreement (to test sycophancy resistance).
2. Execute scenarios using 2-3 frontier LLMs. Collect outputs and apply the full verification protocol.
3. Catalog every detected failure using the taxonomy. Record failure type, severity, stage, detectability, and whether the failure would have been caught by fact-checking alone.
4. Compare predicted failure frequencies (Phase 2) against observed frequencies. Identify surprising results — failures more or less common than predicted, and any failures not captured by the existing taxonomy.
5. Identify candidate new failure types specific to market research if the taxonomy proves insufficient.

Deliverable: empirical failure catalog and analysis report.

#### Phase 4: Verification Framework Development (Weeks 9-12)

Objective: develop market-research-specific verification tools and test their effectiveness.

1. Develop a market-research-specific verification checklist organized by research stage. The checklist adapts the general verification protocol to the specific reasoning tasks and failure patterns observed in Phase 3.
2. Design a practitioner simulation: present AI-generated market research outputs (a mix of outputs with significant reasoning failures and outputs with sound reasoning) to test participants. Measure detection rates with and without the verification checklist.
3. Develop a verification cost estimate: time and effort required to apply the checklist at each stage, compared to the time required to produce the analysis from scratch.
4. Produce authority-level recommendations for each market research task using the delegation framework, now informed by empirical failure data.

Deliverable: market research verification framework, practitioner tool, and authority mapping.

#### Phase 5: Synthesis and Integration (Weeks 12-14)

Objective: connect findings back to the main reasoning trust framework and prepare for publication.

1. Assess whether the existing 25-type taxonomy is sufficient for market research or requires domain-specific extensions. If extensions are needed, propose them with the same format (definition, business example, detection question, risk level, detectability).
2. Update the delegation framework authority recommendations for market research based on empirical evidence.
3. Connect findings to the information structure extension: analyze how market research's information properties (low verifiability, high interpretive burden, temporal sensitivity) create specific verification challenges.
4. Produce a synthesis paper suitable for academic or practitioner publication that demonstrates reasoning verification applied to a concrete domain.

Deliverable: synthesis paper, taxonomy update proposal, and integration memo.

## Literature Mapping

| Literature Cluster | Key Works | Connection to This Extension | Connection to Existing Assets |
| --- | --- | --- | --- |
| AI and innovation | Girotra et al. 2023; Dell'Acqua et al. 2023; Doshi and Hauser 2024; Brynjolfsson et al. 2023 | Establishes empirical baseline for AI performance on creative and analytical business tasks. Girotra finds AI generates more and better ideas; Dell'Acqua finds AI helps on structured tasks but hurts on unstructured ones. Both findings inform which market research tasks are amenable to AI. | Extends the cross-domain analysis in `research/core/domain-analysis/analysis.md` |
| Market research methodology | Kohli and Jaworski 1990; Christensen et al. (JTBD); Cooper (Stage-Gate); Malhotra; Griffin and Hauser 1993 | Defines the professional standard for market research reasoning. These works specify what constitutes rigorous customer need identification, opportunity assessment, and concept development. | Provides the domain-specific professional standard that source quality assessment requires but does not currently define for market research |
| AI agents for research | Park et al. 2023; Shinn et al. 2023 (Reflexion); Yao et al. 2023 (ReAct) | Provides technical context for how AI market research agents are constructed. Multi-step agent architectures introduce compounding failure risks across reasoning chains. | Extends the pipeline validation concept from `research/core/framework/reasoning-verification-pilot-protocol.md` |
| Reasoning quality and CoT faithfulness | Turpin et al. 2024; Lanham et al. 2023; Wei et al. 2022; Barez et al. 2025 | Already surveyed in the literature landscape. Unfaithful CoT in market research means the AI's stated reasoning for a market conclusion may not reflect its actual inference process. | Directly extends the gap identified in `research/core/literature/reasoning-trust-landscape.md` |
| Business intelligence and competitive analysis | Fleisher and Bensoussan; industry analyst methodology | Provides reference standards for how professional competitive analysis is conducted and verified. | Connects to `research/extensions/information-structure/information-structure-plan.md` |

## Task Decomposition

| Stage | Task | Reasoning Type | Primary Input | Predicted Dominant Failure Types |
| --- | --- | --- | --- | --- |
| Environmental scanning | Identify relevant industry trends | Source identification, relevance filtering | Public data, industry reports, news | Inadequate source quality, selection bias |
| Environmental scanning | Assess regulatory and macro environment | Normative analysis, temporal awareness | Regulatory texts, policy announcements | Outdated sources, normative violations |
| Trend identification | Distinguish durable trends from noise | Temporal analysis, magnitude estimation | Trend data over time | False causation, overconfidence, certainty laundering |
| Trend identification | Estimate trend trajectory | Predictive inference | Historical data, analogies | False precision, anchoring on irrelevant precedent |
| Customer need extraction | Synthesize customer feedback | Qualitative interpretation | Survey data, reviews, interviews | Overgeneralization, confirmation bias amplification |
| Customer need extraction | Identify latent needs | Abductive inference | Behavioral data, contextual observation | Question-shaped answers, circular reasoning |
| Competitive mapping | Map competitor capabilities | Comparative analysis | Public filings, product data, analyst reports | Outdated sources, survivorship bias |
| Competitive mapping | Identify competitive white space | Gap analysis, strategic inference | Capability map, need map | Scope mismatch, stakeholder blindness |
| Market sizing | Estimate addressable market | Quantitative estimation, assumption construction | Market data, analogies, demographics | False precision, overconfidence |
| Market sizing | Assess willingness to pay | Economic inference | Survey data, pricing analogies | Certainty laundering, anchoring on irrelevant precedent |
| Concept generation | Generate product concepts | Creative synthesis | Need map, capability map, trend analysis | Confirmation bias amplification, progressive sycophancy |
| Concept screening | Evaluate concept feasibility | Multi-criteria assessment | Concept descriptions, constraints, market data | Uniform confidence, stakeholder blindness |

## Connection to Existing Assets

| Existing Asset | Path | Use in This Extension |
| --- | --- | --- |
| Reasoning failure taxonomy | `research/core/framework/reasoning-failure-taxonomy.md` | Primary evaluation instrument. The 25 failure types and 6 categories structure the empirical analysis. If market-research-specific failures emerge, taxonomy extensions are proposed in the same format. |
| Delegation framework | `research/core/framework/evaluation-framework.md` | Used to assign authority levels to each market research task based on empirical failure data. Scoring dimensions applied at the task level rather than the domain level. |
| Source quality assessment | `research/core/framework/reasoning-verification-source-quality.md` | Applied directly to AI market research outputs. Tests whether the five-level source quality hierarchy needs domain-specific calibration for trade publications, analyst reports, and customer review data. |
| Inferential validity assessment | `research/core/framework/reasoning-verification-inferential-validity.md` | Applied to the logical structure of AI market research arguments. Market research is expected to be rich in inferential failures because the gap between evidence and conclusion is wide. |
| Confidence calibration assessment | `research/core/framework/reasoning-verification-confidence-calibration.md` | Applied to the certainty levels expressed in AI market analysis. Market research with inherently uncertain inputs should produce appropriately hedged outputs. Calibration failures are expected to be frequent. |
| Scoring system integration | `research/core/framework/reasoning-verification-scoring-integration.md` | The two-component evidence strength model (system-level plus output-level) is tested in the market research domain. |
| Pilot validation protocol | `research/core/framework/reasoning-verification-pilot-protocol.md` | The prospective validation design is adapted for market research scenarios. Phase 3 of this extension executes a domain-specific version of the pilot protocol. |
| Cross-domain analysis | `research/core/domain-analysis/analysis.md` | The market research domain assessment (assist authority, weak-to-moderate evidence) is empirically tested and refined. |
| Literature landscape | `research/core/literature/reasoning-trust-landscape.md` | Extended with AI and innovation, market research methodology, and AI agent literatures. |
| Information structure extension | `research/extensions/information-structure/information-structure-plan.md` | Market research is analyzed as an information-structure case. The seven information variables are assessed for market research data, connecting the failure profile to the argument about why expert intermediaries persist. |
| Delegation-as-alignment memo | `research/extensions/delegation-as-alignment.md` | Market research provides a concrete case for the argument that delegation calibration is an alignment problem. |

## Core Propositions

1. AI market research outputs exhibit systematically different failure profiles than other AI business analysis domains. The combination of low verifiability, high interpretive burden, and sycophancy vulnerability produces higher rates of calibration failures and sycophantic failures than domains with more structured evidence bases.
2. The dominant source failure in market research is not fabrication but inadequate source quality and selection bias. The AI cites real sources that are insufficient for the confidence level of the claims they support. This mirrors the pattern identified in the taxonomy where marketing analysis drew on blog posts from agencies selling the services being recommended.
3. The verification framework significantly improves non-expert detection of reasoning failures in AI market research. Practitioners using the structured verification checklist detect more failures, and more important failures, than practitioners evaluating the same outputs without the checklist. The improvement is largest for inferential and calibration failures, which are invisible to fact-checking alone.
4. Most market research tasks require assist-level authority rather than recommend or automate. Empirical failure rates will show that the interpretive burden exceeds what current AI systems handle reliably, and the verification cost for recommend-level authority is prohibitive for all but the most structured tasks such as environmental scanning.
5. Sycophantic failures are the most prevalent and least detected category in AI market research for product ideation. Product ideation contexts create strong framing effects, and AI systems systematically reinforce these frames rather than challenging them.
6. The cost-benefit of AI market research depends critically on whether verification is applied. The value proposition is strongest for the scanning and sizing stages and weakest for the interpretation and concept generation stages.
7. Market research exposes a structural limitation in the current verification framework: the absence of a creative adequacy assessment. The existing framework evaluates whether reasoning is sound but does not evaluate whether the analysis is strategically useful — whether it identifies non-obvious opportunities, challenges conventional thinking, or generates genuinely novel product concepts.

## Expected Outputs

- a professional benchmark for market research reasoning quality, grounded in consulting practice and methodology literature
- a task-level decomposition of market research for product ideation into discrete, assessable reasoning tasks
- an empirical catalog of reasoning failures in AI-generated market research, classified using the 25-type taxonomy
- a failure frequency matrix showing which failure types dominate at each market research stage
- a market-research-specific verification checklist adapted from the general verification protocol
- authority-level recommendations for each market research task using the delegation framework
- a practitioner detection rate analysis comparing verification framework versus unassisted evaluation
- a cost-benefit comparison of AI market research with verification, without verification, and traditional methods
- a synthesis paper connecting market research findings to the broader reasoning trust framework
- any proposed taxonomy extensions for market-research-specific failure types not captured by the existing 25 types

## Deliverables

- `research/extensions/market-research/market-research-plan.md`
- `research/extensions/market-research/professional-benchmark.md`
- `research/extensions/market-research/literature-landscape.md`
- `research/extensions/market-research/task-decomposition.md`
- `research/extensions/market-research/empirical-failure-catalog.md`
- `research/extensions/market-research/verification-checklist.md`
- `research/extensions/market-research/authority-mapping.md`
- `research/extensions/market-research/practitioner-detection-analysis.md`
- `research/extensions/market-research/synthesis.md`

## Anticipated Contribution

This extension makes three contributions to the broader research project.

First, it provides the first **domain-specific empirical test** of the reasoning verification framework. The core framework was designed at a general level and validated against historical incidents. This extension tests whether the framework works when applied systematically to a single domain with its own professional standards, information properties, and failure patterns. If the framework succeeds, it demonstrates domain portability. If it requires adaptation, the specific adaptations inform how the framework should be extended for other domains.

Second, it connects the **reasoning trust** and **information structure** threads of the research. The information structure extension argues that information democratization increases interpretive burden while decreasing access advantages. Market research is an acute case of this dynamic: AI systems democratize access to market data, but the interpretive burden of converting that data into defensible product decisions remains high. The verification framework is the mechanism that addresses interpretive burden — it provides a structured method for assessing whether the interpretation, not just the data, is sound.

Third, it produces **practitioner-facing output**. The core framework and taxonomy are analytical tools designed for researchers and governance specialists. The market-research-specific verification checklist is designed for product managers, marketing directors, and innovation teams — practitioners who use AI market research outputs daily and currently have no structured method for evaluating quality. This bridges the gap identified in the literature landscape: no existing framework connects reasoning quality assessment to the business decision-maker who must evaluate an AI recommendation in their daily work.
