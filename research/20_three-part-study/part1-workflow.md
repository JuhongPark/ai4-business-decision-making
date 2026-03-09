# Part 1: AI Decision Workflows

builds_on: phases 01-19
research_question: What role should AI play at each stage of business decision-making, and under what conditions should authority shift across stages?

## 1. Overview

### 1.1 Purpose

This document translates the existing assist, recommend, and automate framework into workflow-level operating guidance. The earlier research established which domains and scenarios justify different levels of AI authority. Part 1 asks a more operational question: at which step of a decision process should AI assist, recommend, automate, or step back?

The main claim is that AI mode should be assigned at the intersection of domain, stage, and scenario condition. A domain-level label is too coarse for implementation. Within the same domain, information gathering may tolerate automation while judgment and selection still require human control.

### 1.2 Link to Prior Research

| Existing asset | Use in Part 1 |
| --- | --- |
| six-axis taxonomy | classify workflow conditions |
| decision tree | assign initial authority level |
| scenario packs | define baseline, stress, and edge-case transitions |
| governance memo | convert escalation and fallback logic into workflow rules |
| evaluation framework | define stage-level quality criteria |

## 2. Decision Stage Model

### 2.1 Seven stages

| Stage | Name | Core activity |
| --- | --- | --- |
| S1 | Problem recognition | detect anomalies, opportunities, or triggers for action |
| S2 | Information gathering | collect, normalize, and structure relevant information |
| S3 | Analysis and prediction | estimate outcomes and diagnose likely patterns |
| S4 | Alternative generation | produce candidate actions or optimized options |
| S5 | Judgment and selection | choose among tradeoffs and accept accountability |
| S6 | Execution | carry out the chosen action |
| S7 | Monitoring | track outcomes, drift, and feedback signals |

### 2.2 Stage definitions

#### S1: Problem recognition

AI is often useful for anomaly detection, signal scanning, and threshold-based alerts. Human judgment remains necessary to decide whether the detected signal actually warrants managerial action.

#### S2: Information gathering

This is a strong candidate for automation because collection, structuring, and summarization are often repetitive and measurable. Human review is still needed when relevance, sufficiency, or missing context becomes uncertain.

#### S3: Analysis and prediction

AI can add strong value through predictive modeling, simulation, and pattern recognition. Human oversight is needed to evaluate whether the model assumptions remain appropriate and whether non-modeled qualitative factors matter.

#### S4: Alternative generation

AI is useful for optimization, search, and option generation. Human decision-makers remain important for judging feasibility, strategic fit, and value conflicts that optimization logic may not capture.

#### S5: Judgment and selection

This is the most conservative stage. In high-risk domains, AI should usually remain assistive because this stage concentrates accountability, ethical tradeoffs, and cross-stakeholder consequences.

#### S6: Execution

Execution can support bounded automation in structured and lower-risk settings, but only when rollback and exception handling are operationally real rather than nominal.

#### S7: Monitoring

This is another strong automation candidate. AI can monitor outcomes, detect drift, and surface subgroup anomalies continuously. Humans remain necessary to decide how to respond to the signals and when to trigger fallback.

### 2.3 Cross-stage relationship

The seven stages are usually sequential but not strictly linear. Workflow design should support:

- iteration from analysis back to data gathering
- parallel handling of data preparation and analysis
- feedback loops from monitoring back to problem recognition
- stage skipping in urgent but controlled situations

## 3. Domain-by-Stage Mapping

Part 1 focuses on three core domains:

- operations dispatch and routing
- finance credit underwriting
- healthcare triage

### 3.1 Operations

Operations is the most automation-tolerant domain in the study because decisions are repeated, measurable, and feedback-rich.

#### Baseline

| Stage | Mode | Rationale |
| --- | --- | --- |
| S1 | automate with guardrails | threshold-based anomaly detection is stable |
| S2 | automate with guardrails | telemetry and routing data are structured |
| S3 | automate with guardrails | optimization models are reliable in stable conditions |
| S4 | automate with guardrails | search space is large and well-defined |
| S5 | recommend | managers should still approve costly or unusual changes |
| S6 | automate with guardrails | route changes can be executed automatically |
| S7 | automate with guardrails | performance monitoring benefits from continuous automation |

#### Stress

| Stage | Mode | Rationale |
| --- | --- | --- |
| S1 | automate with guardrails | surge detection remains highly measurable |
| S2 | automate with guardrails | collection remains stable |
| S3 | recommend | model reliability falls under unusual load |
| S4 | recommend | options still useful but require human plausibility check |
| S5 | assist | tradeoffs among cost, service, and customer priority intensify |
| S6 | recommend | execution should require confirmation |
| S7 | automate with guardrails | continuous monitoring remains valuable |

#### Edge case

| Stage | Mode | Rationale |
| --- | --- | --- |
| S1 | assist | data degradation itself may be the main signal |
| S2 | assist | substitute data and manual checks become necessary |
| S3 | assist | prediction quality becomes uncertain |
| S4 | assist | human experience should dominate recovery options |
| S5 | human-only | low-confidence data should not drive final choice |
| S6 | assist | execution may need manual control |
| S7 | assist | monitoring remains useful but should not be fully trusted |

### 3.2 Finance

Finance is a high-value but governance-heavy domain. Fairness, drift, model risk, and legal accountability constrain autonomy.

#### Baseline

| Stage | Mode | Rationale |
| --- | --- | --- |
| S1 | recommend | AI can surface likely review candidates |
| S2 | automate with guardrails | document gathering and normalization are structured |
| S3 | recommend | scoring and risk modeling are useful but need review |
| S4 | assist | alternatives should be framed, not chosen autonomously |
| S5 | assist | consequential judgment should remain human-led |
| S6 | assist | execution requires accountable approval |
| S7 | automate with guardrails | monitoring can be automated with subgroup checks |

#### Stress

| Stage | Mode | Rationale |
| --- | --- | --- |
| S1 | assist | macro instability increases ambiguity |
| S2 | automate with guardrails | data collection still benefits from automation |
| S3 | assist | historical relationships may weaken |
| S4 | assist | option framing remains useful but constrained |
| S5 | assist | human judgment becomes more central |
| S6 | human-only | execution should remain tightly controlled |
| S7 | recommend | automated monitoring is useful, but escalation should be more active |

#### Edge case

| Stage | Mode | Rationale |
| --- | --- | --- |
| S1 | assist | anomaly detection can help surface fairness or drift issues |
| S2 | assist | data quality itself may be contested |
| S3 | assist | model outputs should be treated as weak signals |
| S4 | assist | alternatives are useful only as structured prompts |
| S5 | human-only | fairness and accountability dominate |
| S6 | human-only | direct execution by AI is not justified |
| S7 | assist | monitoring remains valuable but should not auto-authorize actions |

### 3.3 Healthcare

Healthcare carries the strongest safety burden. AI is valuable as support, but patient safety and atypical presentation keep autonomy low.

#### Baseline

| Stage | Mode | Rationale |
| --- | --- | --- |
| S1 | recommend | AI can flag likely urgency or prioritization needs |
| S2 | assist | information is partly structured but often incomplete |
| S3 | recommend | triage scoring can help under routine conditions |
| S4 | assist | care options should be framed, not autonomously chosen |
| S5 | assist | final judgment should remain clinician-led |
| S6 | assist | execution should preserve clinician confirmation |
| S7 | recommend | monitoring can support escalation and quality review |

#### Stress

| Stage | Mode | Rationale |
| --- | --- | --- |
| S1 | recommend | surge detection and queue prioritization become valuable |
| S2 | assist | intake remains messy under pressure |
| S3 | recommend | stronger support is justified if clinician override is active |
| S4 | assist | option framing remains support-only |
| S5 | assist | high-stakes choice still belongs to clinicians |
| S6 | assist | execution requires accountable human confirmation |
| S7 | recommend | monitoring helps identify overloaded or deteriorating cases |

#### Edge case

| Stage | Mode | Rationale |
| --- | --- | --- |
| S1 | assist | AI may flag unusual patterns but should not frame the case alone |
| S2 | assist | atypical patients create information ambiguity |
| S3 | assist | model generalization is least reliable here |
| S4 | assist | AI can provide reference patterns only |
| S5 | human-only | clinician judgment is indispensable |
| S6 | human-only | execution should stay fully human-directed |
| S7 | assist | monitoring remains useful as a secondary signal |

### 3.4 Cross-domain pattern

Three patterns recur:

- S2 and S7 are usually the strongest candidates for higher automation.
- S5 is the most restrictive stage across all high-stakes domains.
- As scenarios deteriorate from baseline to stress to edge case, authority shifts downward faster in finance and healthcare than in operations.

## 4. Escalation and Fallback Flow Design

### 4.1 Definitions

- escalation: a controlled increase in AI authority when evidence, stability, and governance justify it
- fallback: a controlled reduction in AI authority when conditions deteriorate or confidence drops

### 4.2 Domain rules

#### Operations

Escalation toward automation is justified when telemetry is stable, routing constraints are clear, and exception rates remain low. Fallback should be triggered by degraded telemetry, route conflicts, infrastructure outages, or repeated service failures.

#### Finance

Escalation toward recommend is justified only when fairness monitoring, auditability, and subgroup stability are strong. Fallback should be triggered by macro instability, drift, subgroup anomalies, or documentation weaknesses.

#### Healthcare

Escalation toward stronger recommendation support is justified only under validated workflows with real clinician override. Fallback should be triggered by incomplete information, atypical cases, or any uncertainty about clinical safety.

### 4.3 Scenario transition protocol

For worsening conditions:

1. detect a scenario shift
2. validate whether the signal is real
3. lower authority to the next justified mode
4. route the case to the required human checkpoint
5. log the transition and monitor outcomes

For recovery conditions:

1. verify that stability has actually returned
2. confirm evidence and governance readiness
3. restore authority gradually rather than instantly
4. continue enhanced monitoring during recovery

Healthcare requires a special caution rule: surge conditions can justify stronger recommendation support, but not broad automation.

## 5. Workflow Pattern Catalog

### 5.1 Pattern A: Automation-first

Best fit:

- structured tasks
- low-risk conditions
- dense feedback loops
- stable baseline environments

Typical domains:

- dispatch
- routing
- repetitive operations optimization

Default shape:

- S2, S3, S4, S6, S7 can support higher automation
- S5 usually remains recommend rather than fully automated

### 5.2 Pattern B: Recommendation-centric

Best fit:

- semi-structured tasks
- medium-risk consequences
- meaningful but incomplete measurability

Typical domains:

- marketing optimization
- product experimentation
- pricing or campaign support

Default shape:

- AI structures options and surfaces likely choices
- humans approve actions and review non-routine exceptions

### 5.3 Pattern C: Assist-centric

Best fit:

- high-risk or regulated tasks
- fairness, safety, or legal exposure
- strong need for accountable review

Typical domains:

- finance
- healthcare
- sensitive HR decisions

Default shape:

- AI gathers, scores, and highlights
- human judgment remains central at S4 to S6

### 5.4 Pattern D: Human-led

Best fit:

- unstructured decisions
- weak evidence
- atypical or novel conditions

Typical domains:

- crisis strategy
- edge-case adjudication
- high-ambiguity stakeholder tradeoffs

Default shape:

- AI serves as a synthesis tool only
- humans own framing, selection, and execution

## 6. Integrated Workflow Design Principles

### Principle 1

Assign AI mode by domain x stage x scenario combination, not by domain label alone.

### Principle 2

Design fallback before deployment. A workflow without operational fallback is not governance-ready.

### Principle 3

Escalation should scale with evidence quality and governance readiness, not with technical ambition.

### Principle 4

Workflows must support dynamic scenario shifts rather than static authority assignments.

### Principle 5

Judgment and selection should be designed most conservatively because accountability concentrates there.

### Principle 6

Information gathering and monitoring are often the best first candidates for higher automation.

## Appendix: Working Definitions

- assist: AI provides signals, summaries, or forecasts while humans retain decision authority
- recommend: AI proposes actions that humans approve or reject
- automate with guardrails: AI acts within bounded limits while humans monitor exceptions, audit logs, and rollback mechanisms
- baseline: ordinary and stable operating conditions
- stress: elevated pressure, unusual demand, or degraded stability
- edge case: out-of-distribution, ambiguous, or confidence-deficient condition
