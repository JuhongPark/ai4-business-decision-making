# AI for Business Decision-Making

This research addresses a core question in AI deployment: when should AI systems be granted autonomous decision-making authority, and when must humans retain control? Rather than treating AI delegation as binary (use it or do not), this project develops a 6-dimensional adaptive framework that evaluates delegation fitness based on contextual risk, evidence strength, governance maturity, and scenario conditions — grounded in 71 real-world AI failure cases.

The project originated as a business governance study and has evolved toward the broader alignment problem that underlies it: how to calibrate the boundary between human and AI authority as capabilities change.

Start here for navigation: [research/README.md](research/README.md)

Repository structure note: [research/repository-organization-note.md](research/repository-organization-note.md)

## Current Status

status: submission_ready_plus_extension
current_focus: alignment and interpretability extension
primary_output: [research/delivery/output/thinktank-report.md](research/delivery/output/thinktank-report.md)
summary_output: [research/delivery/output/executive-summary.md](research/delivery/output/executive-summary.md)
extension_output: [research/extensions/information-structure/initial-analysis.md](research/extensions/information-structure/initial-analysis.md)

## Research Position

The project argues that AI authority should be assigned by category combination rather than by domain label alone. This positions AI delegation as a calibration problem rather than an adoption problem.

core_dimensions:
- domain
- decision structure
- risk level
- scenario condition
- AI role
- evidence strength

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
    interpretability-bridge.md  interpretability and delegation calibration
templates/                    reusable templates
```

