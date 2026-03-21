# Phase 23: Business-Context AI Alignment Research Focus

status: draft
phase: 23
date: 2026-03-21
source_memo: (private reference, 2026-03-20)
purpose: Translate the personal research-interest memo into a focused repository direction and assess how much of the current research already supports it.

## Why This Note Exists

The source memo clarifies that the long-run interest is not technical frontier-model alignment in the usual sense.

The core interest is how firms can use AI in business decision-making in ways that remain trustworthy, useful, risk-bounded, and governable.

That can be stated more precisely as:

**business-context AI alignment**

This repository has already built much of the conceptual foundation for that direction, but it has usually described the problem as AI authority allocation, decision governance, or adaptive autonomy rather than as alignment.

## Working Definition

Business-context AI alignment studies how organizations align AI-supported decision systems with:

- the real decision context
- the appropriate level of delegated authority
- the risk and harm profile of the domain
- the oversight and accountability structure of the organization
- the need for fallback, legitimacy, and adaptive control over time

The central question is not:

- "Is the model aligned in an abstract technical sense?"

The central question is:

- "Is the organization using AI in a way that keeps decision authority, trust, risk, and governance aligned with the actual business context?"

## Recommended Core Thesis Focus

The sharpest thesis center remains:

**calibrated AI delegation in business decision-making**

More explicitly:

**How should firms calibrate AI authority in business decisions so that human-AI systems remain trustworthy, effective, risk-aware, and governable?**

This is the cleanest bridge between the personal interest memo and the existing repository.

It also keeps the project in a business-facing, organizational, and applied research lane rather than drifting into pure model-safety research.

## Position Of Ethics In This Research

Ethics should be treated as an important contextual layer, but not necessarily as the single primary center of the project.

That means:

- ethics is necessary for understanding the normative logic of delegation
- ethics helps clarify what kinds of harm, unfairness, opacity, manipulation, or legitimacy loss matter
- ethics provides boundary conditions for acceptable business use
- ethics does not need to become the sole framing of the thesis

The practical stance is:

**This project is not primarily a general AI ethics project. It is a business decision and delegation project that must remain ethically literate.**

In this framing, ethics is needed because firms cannot decide how much authority to give AI without some view of:

- what harms are acceptable or unacceptable
- what fairness or rights concerns are triggered
- what kind of explanation is owed to affected people
- when optimization goals diverge from broader organizational or social obligations
- when a technically effective system becomes institutionally or morally unacceptable

So ethics should function as:

- a boundary-setting layer
- an interpretive layer for risk and legitimacy
- a supporting lens for governance and trust calibration

not necessarily as the repository's only or main organizing identity.

## How The Main Interests Collapse Into One Problem

The source memo identifies four attractive subproblems: trust, optimization, risk, and governance.

Ethics sits across these four rather than replacing them as a separate center.

These fit together cleanly if the unifying problem is defined as calibrated delegation.

| Interest area | Business-context alignment interpretation | Main practical question |
| --- | --- | --- |
| Trust | warranted reliance on AI outputs | When should managers trust or distrust the system? |
| Optimization | role allocation between human and AI | What level of delegation produces the best decision process? |
| Risk | failure detection and restriction logic | When should authority be reduced or blocked? |
| Governance | organizational design for control | Who sets, reviews, and revises the delegation rules? |
| Ethics | normative limits and legitimacy conditions | What should never be optimized past, ignored, or delegated away? |

This means the strongest integrative statement is:

**Business-context AI alignment is the problem of assigning and revising AI authority so that trust is calibrated, performance is improved, risks are bounded, and governance remains operationally real.**

Ethics helps determine the acceptable boundaries of that authority rather than replacing delegation as the core research variable.

## How Much The Current Repository Already Covers

The answer is:

**a large share of it is already covered**

The repository is already strongly related to this direction, especially under the language of authority, governance, fallback, and organizational design.

### 1. Strong direct foundation: authority allocation

The early framework and taxonomy already ask the question that the source memo calls "How much should AI be trusted and how much should it be given authority?"

Key files:

- `research/04_framework/framework-summary.md`
- `research/04_framework/evaluation-framework.md`
- `research/16_taxonomy/summary.md`
- `research/16_taxonomy/decision-tree.md`

What is already established:

- AI should be evaluated as part of a workflow, not as an isolated model.
- The correct AI role depends on decision structure, data readiness, risk, evidence, and governance.
- The practical question is when AI should assist, recommend, or automate with guardrails.
- High-stakes domains should default toward lower authority unless stronger evidence and governance are present.

This is already very close to a business-alignment frame.

### 2. Strong direct foundation: adaptive delegation and fallback

The executive summary and the main report already make delegation and authority reduction central.

Key files:

- `research/06_output/executive-summary.md`
- `research/06_output/thinktank-report.md`

What is already established:

- AI authority must be adaptive rather than fixed.
- The key managerial question is how much authority to delegate under specific conditions.
- The second key question is when authority should be reduced again.
- Fallback logic is treated as a core design obligation.

This is effectively an alignment question framed at the system-governance level.

### 3. Very strong foundation: governance

Phases 20 and 21 extend the project from principle into implementation and adaptive governance.

Key files:

- `research/20_three-part-study/research-plan.md`
- `research/20_three-part-study/part2-infrastructure.md`
- `research/20_three-part-study/part3-organization.md`
- `research/21_adaptive-governance/summary.md`

What is already established:

- escalation and fallback flows
- infrastructure required to make governance operational
- organizational roles for accountability and approval
- transition conditions for authority increase or decrease
- living-evidence logic for keeping governance current

This is one of the strongest parts of the repository and maps directly to the governance branch of the source memo.

### 4. Partial but meaningful foundation: trust calibration

Trust is present in the repository, but it is not yet the named center of gravity.

Key files:

- `research/05_drafting/introduction.md`
- `research/20_three-part-study/research-plan.md`
- `research/20_three-part-study/part3-organization.md`
- `research/22_information-structure/research-plan.md`
- `research/22_information-structure/initial-analysis.md`

What is already established:

- overreliance is named as a risk
- trust calibration appears as an explicit concern
- AI introduces reliability and oversight problems
- organizations need clear authority and override structures because technical capability alone does not justify reliance

What is not yet fully established:

- a dedicated trust-calibration framework
- a direct model of over-reliance vs under-reliance in business settings
- a clean measurement concept for miscalibrated delegation

### 5. Partial but meaningful foundation: optimization

Optimization is covered indirectly through authority mode selection, workflow design, and scenario-sensitive role assignment.

Key files:

- `research/04_framework/evaluation-framework.md`
- `research/16_taxonomy/decision-tree.md`
- `research/18_publication-prep/domain-recommendation-table.md`
- `research/22_information-structure/llm-decision-paradigm.md`

What is already established:

- different decision settings justify different human-AI role splits
- the same domain can justify more or less authority depending on conditions
- repeated, measurable decisions are better candidates for stronger delegation
- many business gains depend on role design, not model capability alone

What is not yet fully established:

- an explicit optimization objective for the human-AI split
- comparative testing of alternative delegation designs
- a formal account of when the best mode is assist vs recommend vs bounded automation beyond rule-based guidance

### 6. Present as a supporting layer: ethics

Ethics is already present in the repository, but mostly through applied governance language rather than through standalone ethical theory.

Key files:

- `research/04_framework/evaluation-framework.md`
- `research/16_taxonomy/decision-tree.md`
- `research/06_output/thinktank-report.md`
- `research/21_adaptive-governance/summary.md`

What is already established:

- fairness, safety, compliance, access, and investor-protection concerns are treated as reasons to restrict authority
- high-stakes decisions require stronger explainability, accountability, and fallback logic
- legitimacy and responsibility remain important even when technical capability improves
- firms should not treat optimization or speed as sufficient justification for deployment

What is not yet fully established:

- a short statement of the ethical logic underlying the framework
- a direct explanation of how ethics differs from but supports governance
- a clean account of why this project needs ethical literacy without turning into a general moral-philosophy project

## Coverage Assessment By Interest Area

| Interest area from source memo | Coverage in current repository | Assessment |
| --- | --- | --- |
| Trust | present but not yet central | partial |
| Optimization | present through authority logic and workflow design | partial to moderate |
| Risk | deeply embedded in restriction logic, evidence rules, and fallback design | strong |
| Governance | deeply embedded in the project's core contribution | very strong |
| Ethics | present mainly through fairness, legitimacy, accountability, and rights-sensitive restriction logic | partial but necessary |

## Overall Verdict

**Yes. The current research is already substantially related to the new direction.**

More precisely:

- the repository already functions as a study of business-context AI alignment
- it does so under the vocabulary of authority allocation, governance readiness, escalation, fallback, and organizational design
- the strongest existing bridge is the question of how much authority to delegate to AI under different business conditions

So the new direction does not require discarding the current work.

It mainly requires:

1. changing the top-level framing
2. making trust calibration more explicit
3. treating delegation quality as the main alignment variable
4. making the ethics layer explicit as a supporting boundary condition rather than leaving it implicit

## What Is Still Missing If The Project Is Repositioned As AI Alignment

If the project is explicitly repositioned as business-context AI alignment, the biggest gaps are:

1. a direct positioning note explaining how this differs from frontier-model or technical alignment research
2. a dedicated trust-calibration memo covering over-reliance, under-reliance, and calibrated delegation
3. a clearer concept of miscalibrated delegation as the key business failure mode
4. a stronger account of objective misalignment inside firms, where local model targets can diverge from broader organizational goals
5. a more explicit evaluation logic for when human-AI role allocation is actually optimal rather than merely acceptable
6. a short ethics-context note explaining the moral and legitimacy boundaries relevant to business AI delegation

## Suggested Near-Term Research Question

If one question should lead the next phase, it should be:

**Under what conditions does AI delegation in business decision-making remain calibrated rather than becoming over-trusting, under-trusting, under-governed, or misaligned with organizational goals?**

That question preserves the current repository's strengths while bringing the project closer to the source memo's long-run identity.

## Recommended Next Documents

The cleanest next additions would be:

1. a positioning memo on business-context AI alignment versus technical AI alignment
2. a trust-calibration memo for business decision systems
3. a miscalibrated-delegation framework linking trust, optimization, risk, and governance
4. an ethics-context memo clarifying the role of fairness, legitimacy, accountability, and acceptable harm in business AI delegation

Those four would make the repository's existing contribution easier to describe as an alignment research program without forcing a restart.
