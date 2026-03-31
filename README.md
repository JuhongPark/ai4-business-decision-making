# AI for Business Decision-Making

This research addresses a core question in AI deployment: when should AI systems be granted autonomous decision-making authority, and when must humans retain control? Rather than treating AI delegation as binary (use it or do not), this project builds a 6-dimensional adaptive framework grounded in existing academic literature, regulatory records, and 71 documented AI failure cases that evaluates delegation fitness based on contextual risk, evidence strength, governance maturity, and scenario conditions.

The project originated as a business governance study and has evolved toward the broader alignment problem that underlies it: how to calibrate the boundary between human and AI authority as capabilities change.

Start here for navigation: [research/README.md](research/README.md)

Repository structure note: [research/repository-organization-note.md](research/repository-organization-note.md)

## Current Status

status: submission_ready_plus_extension
current_focus: alignment and interpretability extension
primary_output: [research/delivery/output/thinktank-report.md](research/delivery/output/thinktank-report.md)
summary_output: [research/delivery/output/executive-summary.md](research/delivery/output/executive-summary.md)
extension_output: [research/extensions/information-structure/initial-analysis.md](research/extensions/information-structure/initial-analysis.md)

## The 71-Incident Analysis and 6-Dimensional Framework

### What This Research Did

This project collected **71 documented AI governance failures** (2018–2026) from regulatory actions (FTC, DOJ, EEOC, SEC, CFPB, FDA), court decisions, investigative journalism, and corporate disclosures, then systematically classified them using two established academic taxonomies:

- **General AI incidents** were classified using Amodei et al.'s (2016) Five Concrete Problems in AI Safety — side effects, reward hacking, scalable oversight, safe exploration, and distributional shift.
- **LLM-specific incidents** were classified using Weidinger et al.'s (2022) six risk categories — discrimination/toxicity, information hazards, misinformation, malicious uses, interaction harms, and automation harms.

The analysis revealed that most failures were not caused by technical incapacity. They were caused by **delegation calibration failure** — organizations granted AI more authority than the conditions warranted. Drawing on these failure patterns and existing governance literature (NIST, 2023; Agrawal et al., 2018; Lee and See, 2004), a 6-dimensional adaptive framework was built to evaluate the appropriate level of AI autonomy for a given decision context.

### Key Findings from the Incident Analysis

- **Reward hacking and side effects** dominated general AI failures (Amodei et al., 2016). The problem was objective specification, not model capability. This aligns with Krakovna et al.'s (2020) finding that specification gaming is pervasive.
- **Misinformation (W3)** dominated LLM failures — 70% of LLM incidents involved fluent hallucination (Weidinger et al., 2022).
- **General AI and LLM governance toolkits must differ fundamentally.** General AI requires bias testing, objective review, and human override design. LLM requires output verification outside the chat interface, prompt/data-boundary controls, and brand/policy grounding.
- **Retrospective validation**: When applied against the 20 core incidents, the framework would have recommended a lower authority level in 12/20 cases outright, partially flagged 7/20, and missed 1/20 (an information security risk outside its scope).

### The 6-Dimensional Framework

The framework is a practical evaluation structure with six dimensions, grounded in established research. The core principle — **AI authority should be assigned by category combination, not by domain label alone** — follows from Agrawal, Gans, and Goldfarb's (2018) distinction between prediction and judgment. This positions AI delegation as a calibration problem rather than an adoption problem.

```
preferred_AI_role = domain × decision_structure × risk_level × scenario_condition × evidence_strength × governance_readiness
```

| Dimension | What It Evaluates | Academic Basis |
|-----------|------------------|---------------|
| **Domain** | Business area (strategy, operations, finance, healthcare, investment, product, marketing, market research) | Brynjolfsson, Hitt, and Kim (2011) — data-driven performance depends on organizational practices, not model quality alone |
| **Decision Structure** | Unstructured → semi-structured → structured | Agrawal, Gans, and Goldfarb (2018) — prediction requires separate judgment; structure determines where judgment is needed |
| **Risk Level** | Low (operational) → medium (revenue/customer) → high (fairness/compliance/safety) | NIST AI Risk Management Framework (2023) — governance requirements must be differentiated by risk level |
| **Scenario Condition** | Baseline → stress → edge-case | Amodei et al. (2016) — distributional shift causes AI to fail when deployment conditions differ from training |
| **Evidence Strength** | Weak → moderate → strong | Elhage et al. (2022); Conmy et al. (2023) — without interpretability, evidence strength cannot be objectively assessed |
| **Governance Readiness** | Weak → adequate → strong | Schuett et al. (2023) — institutional structures for responsible AI deployment |

### Scoring and Authority Levels

Each dimension is scored 1–3. Total score maps to three authority levels:

| Score | Authority Level | Description |
|-------|----------------|-------------|
| 5–8 | **ASSIST** | AI provides analysis and drafts; human retains final authority |
| 9–11 | **ASSIST or RECOMMEND** | AI provides structured recommendations; human reviews before action |
| 12–15 | **RECOMMEND or AUTOMATE WITH GUARDRAILS** | AI acts within predefined boundaries; human handles exceptions |

Three **override rules** apply regardless of score:

1. High risk + weak governance → cap at ASSIST (grounded in scalable oversight: Amodei et al., 2016)
2. Edge-case scenario → cap at ASSIST (grounded in distributional shift risk)
3. Weak evidence in consequential decision → reduce one level (grounded in trust calibration: Lee and See, 2004; Bansal et al., 2021)

### Reasoning Verification Extension

The incident analysis revealed that the delegation framework alone does not sufficiently address LLM output quality. Drawing on the failure patterns identified in the 71-case inventory, a reasoning verification framework was built with four complementary methods — source quality assessment, inferential validity, normative assessment, and confidence calibration — integrated into the scoring model through a weakest-link principle and a verification gate.

### Detailed Materials

All components of the 71-incident analysis and 6-dimensional framework can be accessed directly:

**Overview and synthesis:**

| Document | Description |
|----------|------------|
| [framework-overview-document.md](research/delivery/output/framework-overview-document.md) | Full single-document synthesis of the 71-incident analysis, 6-dimensional framework, and reasoning verification extension with all academic references |
| [thinktank-report.md](research/delivery/output/thinktank-report.md) | Final research report |
| [executive-summary.md](research/delivery/output/executive-summary.md) | Executive summary |

**Incident analysis:**

| Document | Description |
|----------|------------|
| [incident-inventory.md](research/extensions/business-alignment/incidents/incident-inventory.md) | Full 71-case inventory with classification, evidence types, and primary source URLs |
| [alignment-failure-mapping.md](research/extensions/business-alignment/incidents/alignment-failure-mapping.md) | Each incident mapped to Amodei et al. (2016) and Weidinger et al. (2022) failure modes, with retrospective framework validation |
| [general-ai-vs-llm-incidents.md](research/extensions/business-alignment/incidents/general-ai-vs-llm-incidents.md) | Comparison of general AI vs. LLM failure mechanisms and governance implications |
| [cross-case-comparison.md](research/core/cases/cross-case-comparison.md) | Cross-case comparison across domains (Upstart, Amazon hiring, UPS ORION) |
| [domain-analysis/analysis.md](research/core/domain-analysis/analysis.md) | 8-domain comparative analysis |

**6-dimensional framework and taxonomy:**

| Document | Description |
|----------|------------|
| [category-system.md](research/core/taxonomy/category-system.md) | Full 6-dimensional category system definition |
| [decision-rules.md](research/core/taxonomy/decision-rules.md) | 7 core decision rules derived from the framework |
| [scoring-sheet.md](research/core/taxonomy/scoring-sheet.md) | Scoring model (5 dimensions × 1–3 scale) with score bands and override rules |
| [decision-tree.md](research/core/taxonomy/decision-tree.md) | 6-step sequential decision tree for practical application |
| [evaluation-framework.md](research/core/framework/evaluation-framework.md) | 7-dimension evaluation framework with adoption mode definitions |

**Reasoning verification:**

| Document | Description |
|----------|------------|
| [reasoning-failure-taxonomy.md](research/core/framework/reasoning-failure-taxonomy.md) | 6 categories × 25 failure types with risk and detectability matrix |
| [reasoning-verification-source-quality.md](research/core/framework/reasoning-verification-source-quality.md) | 5-level source quality hierarchy and assessment protocol |
| [reasoning-verification-inferential-validity.md](research/core/framework/reasoning-verification-inferential-validity.md) | Inference type classification and validity assessment |
| [reasoning-verification-confidence-calibration.md](research/core/framework/reasoning-verification-confidence-calibration.md) | Confidence vs. evidence alignment assessment |
| [reasoning-verification-scoring-integration.md](research/core/framework/reasoning-verification-scoring-integration.md) | Integration with delegation framework (weakest-link and verification gate) |
| [reasoning-verification-pilot-protocol.md](research/core/framework/reasoning-verification-pilot-protocol.md) | 3-phase validation plan (retrospective, prospective, comparative) |

**Literature and sources:**

| Document | Description |
|----------|------------|
| [literature-review-summary.md](research/core/literature/literature-review-summary.md) | Core literature review: 6 themes from foundational sources |
| [sources.md](research/core/literature/sources.md) | Master source tracker with full citations and links |

## Key Outputs

- Final report: [research/delivery/output/thinktank-report.md](research/delivery/output/thinktank-report.md)
- Executive summary: [research/delivery/output/executive-summary.md](research/delivery/output/executive-summary.md)
- Taxonomy summary: [research/core/taxonomy/taxonomy-summary.md](research/core/taxonomy/taxonomy-summary.md)
- Decision tree: [research/core/taxonomy/decision-tree.md](research/core/taxonomy/decision-tree.md)
- Scoring sheet: [research/core/taxonomy/scoring-sheet.md](research/core/taxonomy/scoring-sheet.md)
- Core tables: [research/delivery/submission-ready/core-tables.md](research/delivery/submission-ready/core-tables.md)
- Final validation: [research/delivery/submission-ready/submission-ready-validation.md](research/delivery/submission-ready/submission-ready-validation.md)
- Freeze note: [research/delivery/submission-ready/freeze-note.md](research/delivery/submission-ready/freeze-note.md)
- Information-structure plan: [research/extensions/information-structure/information-structure-plan.md](research/extensions/information-structure/information-structure-plan.md)
- Information-structure analysis: [research/extensions/information-structure/initial-analysis.md](research/extensions/information-structure/initial-analysis.md)
- Information-structure literature scan: [research/extensions/information-structure/literature-scan.md](research/extensions/information-structure/literature-scan.md)
- Consulting narratives: [research/extensions/information-structure/consulting-firm-narratives.md](research/extensions/information-structure/consulting-firm-narratives.md)
- Doom narratives: [research/extensions/information-structure/doom-narratives.md](research/extensions/information-structure/doom-narratives.md)
- LLM decision paradigm: [research/extensions/information-structure/llm-decision-paradigm.md](research/extensions/information-structure/llm-decision-paradigm.md)
- Capability ladder: [research/extensions/information-structure/capability-ladder.md](research/extensions/information-structure/capability-ladder.md)

## Navigation Model

The repository is now grouped by document role rather than by a flat list of topic folders:

- `research/core/`: foundational research, source synthesis, framework design, taxonomy, and scenario work
- `research/delivery/`: reader-facing outputs, publication materials, and submission-ready packages
- `research/operations/`: revision notes, expansion planning, and program-management artifacts
- `research/extensions/`: follow-on research tracks that extend the core thesis

Zone guides:

- [research/core/README.md](research/core/README.md)
- [research/delivery/README.md](research/delivery/README.md)
- [research/operations/README.md](research/operations/README.md)
- [research/extensions/README.md](research/extensions/README.md)

## Main Finding

The central conclusion of the research is:

`AI authority should be adaptive, not fixed.`

Organizations should decide AI authority by evaluating:

1. what domain the decision belongs to
2. how structured the decision is
3. how risky failure would be
4. whether conditions are baseline, stress, or edge-case
5. how strong the supporting evidence is
6. whether governance is strong enough for the proposed autonomy level

## Connection to AI Safety and Alignment

This project sits at the intersection of AI governance and alignment research.

### Why Delegation Calibration Is an Alignment Problem

Traditional AI alignment focuses on ensuring models behave as intended (value alignment, reward specification). This research addresses a complementary question: even if a model is well-aligned, should it be granted autonomous authority in a given context? The 6-dimensional framework provides the governance layer that translates technical alignment confidence into operational delegation decisions.

### The Role of Interpretability

The "evidence strength" dimension in the framework directly depends on model interpretability. When a model's internal reasoning cannot be inspected, evidence strength cannot be objectively assessed — and the framework forces a one-level reduction in allowable authority. This creates a concrete demand for mechanistic interpretability: organizations cannot responsibly delegate decisions to AI systems they cannot inspect.

- **High interpretability** — evidence strength is verifiable — higher AI authority is justified
- **Low interpretability** — evidence strength is opaque — human override required regardless of performance

### From Incident Analysis to Alignment Failure Modes

The incident inventory catalogs 71 real-world AI governance failures — cases where delegation calibration was wrong. These map to alignment failure modes:

- Specification gaming — AI optimized for proxy metrics rather than intended objectives
- Distribution shift — model deployed outside training conditions
- Oversight failure — human-in-the-loop was nominal, not effective
- Fluent hallucination — generated outputs that are confidently wrong

## Methodology

- **Incident analysis**: 71 documented AI governance failures sourced from regulatory actions, court decisions, investigative journalism, and company disclosures (2018-2026)
- **Framework development**: Iterative taxonomy construction with cross-domain validation across finance, healthcare, hiring, marketing, and operations
- **Evidence tiering**: All claims labeled as confirmed, estimated, or hypothesis following a 3-tier verification protocol
- **Failure mode mapping**: Each incident classified by dominant failure mechanism and mapped to alignment failure categories

## Related Work in AI Alignment

This adaptive authority framework connects to several active research threads:

- **Scalable oversight** (Amodei et al., 2016; Bowman et al., 2022) — How to maintain human oversight as AI systems become more capable. The framework's graduated authority levels operationalize this principle by constraining autonomy to what can be meaningfully overseen.
- **Mechanistic interpretability** (Elhage et al., 2022; Conmy et al., 2023) — Understanding model internals to verify decision quality. The evidence strength dimension creates a concrete demand signal for interpretability research.
- **Trust calibration** (Lee and See, 2004; Bansal et al., 2021) — Appropriate reliance as the correspondence between trust and actual trustworthiness. The scoring dimensions are proxies for trustworthiness, and the override rules enforce calibration floors.
- **Specification gaming** (Krakovna et al., 2020) — How AI systems exploit gaps between intended and specified objectives. The framework's graduated authority levels directly manage this risk surface: a system that games its specification at the "assist" level produces a suggestion a human can reject, while the same failure at "automate" level takes action before intervention is possible.
- **AI governance frameworks** (Schuett et al., 2023) — Institutional structures for responsible AI deployment. The framework bridges technical alignment confidence and operational delegation decisions.

## Open Research Questions

This framework raises several questions that remain open:

1. **Quantifying evidence strength** — Can interpretability methods (feature attribution, probing, circuit analysis) provide objective evidence-strength scores, replacing subjective expert judgment?
2. **Dynamic delegation** — The current framework evaluates authority statically. How should authority levels adjust in real-time as model confidence and environmental conditions change?
3. **Cross-domain transfer** — Do failure patterns in one domain (e.g., lending) predict governance needs in another (e.g., hiring)? The incident data suggests partial transferability but needs rigorous validation.
4. **Interpretability-authority tradeoff** — Is there a formal relationship between model interpretability depth and maximum safe authority level? Can this be expressed as a constraint?
5. **Scalable oversight bottleneck** — The framework assumes human oversight is available at the "assist" and "recommend" levels, but this assumption may not hold at scale. How should the framework account for oversight capacity constraints?

## Repository Structure

```text
research/
  README.md                   navigation guide for the research workspace
  core/                       foundational research and analytical building blocks
    planning/                 project scope, sequencing, and timeline documents
    questions/                research question and scope definition
    literature/               source tracker and reading notes
    cases/                    case comparison materials
    framework/                evaluation framework
    drafting/                 section drafts
    evidence/                 evidence-strengthening notes
    domain-analysis/          cross-domain comparison and casebook
    scenario-design/          scenario research design
    scenario-packs/           scenario packs for core domains
    taxonomy/                 category system and usage rules
  delivery/                   reader-facing outputs and publication packages
    output/                   main report outputs
    publication-prep/         publication-grade supporting materials
    submission-ready/         finish plan, validation, and freeze materials
    validation/               earlier validation materials
  operations/                 revision, application, and planning materials
    applications/             application prep materials and submission notes
    thinktank-program/        3-month research program plan
    revision/                 revision-stage synthesis and review
    expansion/                expansion and refocus planning
  extensions/                 follow-on research tracks built on the core thesis
    three-part-study/         workflow, infrastructure, and organization extension
    adaptive-governance/      adaptive governance and market-timing extension
    information-structure/    information shocks and decision-making extension
    business-alignment/       business-context alignment research
    delegation-as-alignment.md  delegation calibration as alignment problem
    interpretability-bridge.md  interpretability and delegation calibration
templates/                    reusable templates
```

