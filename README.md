# AI for Business Decision-Making

This repository contains a think-tank style research project on how organizations should use AI to assist, recommend, or automate business decisions.

## Current Status

status: submission_ready_v1_plus_extension
current_focus: phase 22 information-structure extension
primary_output: [research/06_output/thinktank-report.md](research/06_output/thinktank-report.md)
summary_output: [research/06_output/executive-summary.md](research/06_output/executive-summary.md)
extension_output: [research/22_information-structure/initial-analysis.md](research/22_information-structure/initial-analysis.md)

## Research Position

The project argues that AI authority should be assigned by category combination rather than by domain label alone.

core_dimensions:
- domain
- decision structure
- risk level
- scenario condition
- AI role
- evidence strength

## Key Outputs

- Final report: [research/06_output/thinktank-report.md](research/06_output/thinktank-report.md)
- Executive summary: [research/06_output/executive-summary.md](research/06_output/executive-summary.md)
- Taxonomy summary: [research/16_taxonomy/summary.md](research/16_taxonomy/summary.md)
- Decision tree: [research/16_taxonomy/decision-tree.md](research/16_taxonomy/decision-tree.md)
- Scoring sheet: [research/16_taxonomy/scoring-sheet.md](research/16_taxonomy/scoring-sheet.md)
- Core tables: [research/19_submission-ready/core-tables.md](research/19_submission-ready/core-tables.md)
- Final validation: [research/19_submission-ready/final-validation.md](research/19_submission-ready/final-validation.md)
- Freeze note: [research/19_submission-ready/freeze-note.md](research/19_submission-ready/freeze-note.md)
- Phase 22 plan: [research/22_information-structure/research-plan.md](research/22_information-structure/research-plan.md)
- Phase 22 analysis: [research/22_information-structure/initial-analysis.md](research/22_information-structure/initial-analysis.md)
- Phase 22 literature scan: [research/22_information-structure/literature-scan.md](research/22_information-structure/literature-scan.md)
- Phase 22 consulting narratives: [research/22_information-structure/consulting-firm-narratives.md](research/22_information-structure/consulting-firm-narratives.md)
- Phase 22 doom narratives: [research/22_information-structure/doom-narratives.md](research/22_information-structure/doom-narratives.md)
- Phase 22 LLM decision paradigm: [research/22_information-structure/llm-decision-paradigm.md](research/22_information-structure/llm-decision-paradigm.md)
- Phase 22 capability ladder: [research/22_information-structure/capability-ladder.md](research/22_information-structure/capability-ladder.md)

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

## Repository Structure

```text
research/
  00_planning/              planning and timeline documents
  01_questions/             research question and scope
  02_literature/            source tracker and reading notes
  03_cases/                 case comparison materials
  04_framework/             evaluation framework
  05_drafting/              section drafts
  06_output/                report outputs
  07_validation/            earlier validation materials
  08_expansion/             expansion and refocus planning
  09_research/              evidence-strengthening notes
  10_domain-analysis/       cross-domain comparison and casebook
  11_scenario-design/       scenario research design
  12_thinktank-program/     3-month research program plan
  13_scenario-packs/        scenario packs for core domains
  15_revision-01/           revision-stage synthesis and review
  16_taxonomy/              category system and usage rules
  18_publication-prep/      publication-grade supporting materials
  19_submission-ready/      finish plan, validation, and freeze
  20_three-part-study/      workflow, infrastructure, and organization extension
  21_adaptive-governance/   adaptive governance and market-timing extension
  22_information-structure/ information shocks and decision-making extension
templates/                  reusable templates
```

## Working Rules

- Write all research content in English.
- Separate evidence from interpretation.
- Label evidence strength when claims differ in confidence.
- Treat the report as a decision-governance study, not as a universal ROI claim.

## Commit Format

Use commit messages in `type: summary` format.

Examples:

- `research: finalize submission-ready version one`
- `docs: replace cycle terminology with revision language`
- `research: formalize ai decision taxonomy and usage rules`
