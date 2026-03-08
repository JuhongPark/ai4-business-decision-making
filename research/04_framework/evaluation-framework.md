# Phase 5: Evaluation Framework

status: completed
phase_goal: Build a practical framework for evaluating when AI should be used in business decision-making and under what conditions it is likely to improve performance.

## Core Principle

AI should be evaluated as a decision-support capability embedded in organizational workflows, incentives, and accountability structures rather than as an isolated technical model.

## Evaluation Dimensions

### 1. Decision Structure

- low: ambiguous, infrequent, weakly measurable decisions
- medium: partially structured decisions with some repeated patterns
- high: repeated, measurable, rules-influenced decisions

### 2. Data Readiness

- low: sparse, noisy, fragmented, or weakly relevant data
- medium: usable data with quality gaps or integration limits
- high: rich historical data with clear feedback loops

### 3. Stakes and External Impact

- low: limited external harm if the recommendation is wrong
- medium: meaningful business cost but limited rights impact
- high: decisions affecting fairness, compliance, access, safety, or reputation

### 4. Degree of AI Autonomy

- low: AI provides signals only
- medium: AI recommends actions that humans approve
- high: AI directly triggers actions with limited human intervention

### 5. Explainability Requirement

- low: limited need for detailed reasoning
- medium: internal explainability needed for management use
- high: explanation needed for legal, ethical, or stakeholder accountability

### 6. Human Oversight Requirement

- low: humans monitor aggregate performance
- medium: humans approve exceptions or sensitive cases
- high: humans retain final authority over decisions

### 7. Governance Requirement

- low: basic monitoring and performance review
- medium: documented controls, auditing, and escalation paths
- high: formal governance, traceability, fairness review, and accountability assignment

## Decision Logic

### Good Fit for AI Support

AI is most likely to improve business decision-making when:

- the decision is frequent and sufficiently structured
- the organization has strong and relevant data
- outcomes can be measured and fed back into the system
- human roles in review and exception handling are clearly defined
- governance is proportional to the stakes of the decision

### Restriction Defaults for High-Stakes Domains

In finance, hiring, and similarly sensitive domains:

- default first to `assist`
- move to `recommend` only when oversight, explainability, and accountability are demonstrably strong
- avoid meaningful automation unless the decision is narrowly bounded, auditable, and supported by strong evidence
- treat weak evidence or unresolved fairness concerns as a reason to restrict deployment rather than expand it

### Weak Fit for AI Automation

AI should not be highly automated when:

- the decision is ambiguous and context-heavy
- data quality is weak or historically biased
- the decision affects rights, fairness, or legitimacy
- objective functions are poorly specified
- the organization cannot explain or govern the system effectively

## Framework Matrix

| Dimension | Favorable Condition | Warning Condition |
| --- | --- | --- |
| Decision structure | repeated and measurable | ambiguous and one-off |
| Data readiness | high-quality and relevant | sparse, biased, or fragmented |
| Stakes | limited harm from error | high external or ethical impact |
| AI autonomy | support with controlled escalation | direct action without review |
| Explainability | sufficient for the use case | opaque in sensitive contexts |
| Human oversight | explicit role design | unclear accountability |
| Governance | active monitoring and audit | weak controls or ownership |

## Evidence Strength Layer

The framework should be applied with an explicit evidence tier:

- strong: regulator-backed, audited, or peer-reviewed support
- moderate: official company documentation and technical disclosures
- weak: reported or secondary evidence without direct primary confirmation

High-impact adoption claims should not rely on weak evidence alone.

## Adoption Modes

### Mode 1: Assist

Use when the decision is complex or high-stakes. AI generates signals, summaries, or forecasts, while humans retain decision authority.

### Mode 2: Recommend

Use when the decision is moderately structured and the organization can review outputs effectively. AI recommends actions, and humans confirm or override.

### Mode 3: Automate with Guardrails

Use when the decision is highly structured, data-rich, low to moderate in harm potential, and easy to monitor. Humans focus on exceptions, audits, and drift detection.

## Framework Implications

- Marketing and operations often fit `recommend` or `automate with guardrails`.
- Finance should default to `assist` or tightly governed `recommend`, with only narrow automation under strong governance and strong evidence.
- Human resources should generally remain `assist` or tightly constrained `recommend`, and restriction is often more appropriate than automation.
- Strategy is usually an `assist` domain because contextual judgment remains central.

## Final Working Proposition

AI-supported decisions are most defensibly useful when the decision environment is structured, the data are reliable, the oversight model is explicit, governance intensity matches decision risk, and the claims supporting deployment are backed by appropriately strong evidence.
