# Part 3: Organizational Design for AI Decision-Making

builds_on: part1-workflow.md, part2-infrastructure.md
research_question: How should roles, authority structures, collaboration routines, and organizational maturity be designed so AI-supported decision systems can be governed responsibly?

## 1. Overview

### 1.1 Position in the broader study

Part 1 defines how decision workflows should operate. Part 2 defines the infrastructure required to support those workflows. Part 3 defines who owns the system, how accountability is assigned, and how organizational design should adapt as AI authority expands.

### 1.2 Research gap

The earlier research argued that accountability should remain explicit and that human override should be visible and operational. It did not yet specify the organizational structures needed to make those principles real. Part 3 fills that gap.

### 1.3 Research question

How should firms design roles, authority, routines, and culture so that AI-supported decisions remain effective, accountable, and adaptable?

### 1.4 Conceptual basis

This document draws on:

- human-AI complementarity
- algorithm aversion and trust calibration
- organizational complements to data-driven decision-making
- governance-first logic for high-stakes domains

## 2. Core Roles

| Role | Primary responsibility |
| --- | --- |
| AI governance committee | approve authority levels, escalation rules, and policy changes |
| Domain decision owner | own final judgment in consequential decisions |
| AI and data engineering | build, deploy, monitor, and maintain systems |
| Legal and compliance | review regulatory and policy implications |
| Fairness and ethics lead | monitor subgroup impact and normative risk |
| Explainability and audit lead | ensure traceability, documentation, and review readiness |

### 2.1 Role relationship

The domain decision owner carries substantive accountability. The governance committee authorizes mode design and transition rules. Engineering owns implementation and monitoring. Compliance, fairness, and audit roles ensure that deployment remains defensible.

### 2.2 Scaling rule

As AI authority rises from assist toward recommend and bounded automation, organizations should increase:

- separation of duties
- review rigor
- monitoring intensity
- auditability
- escalation clarity

## 3. RACI Matrix for Authority Assignment

### 3.1 Summary

| Decision step | Responsible | Accountable | Consulted |
| --- | --- | --- | --- |
| Classify domain | governance committee | governance committee | domain owner |
| Classify decision structure | domain owner and analytics lead | domain owner | governance committee |
| Classify risk level | domain owner and compliance | domain owner | fairness lead |
| Assess scenario condition | monitoring team and domain owner | domain owner | engineering |
| Check evidence strength | analytics lead | governance committee | audit lead |
| Check governance readiness | governance committee | governance committee | compliance and audit |
| Assign lowest justified AI authority | governance committee | governance committee | domain owner |

### 3.2 Interpretation

The RACI logic prevents hidden ownership gaps. The key rule is simple: no high-stakes AI mode should exist without a named accountable owner and an operational override path.

## 4. Organizational Models

### 4.1 Model A: Centralized AI office

Best fit:

- early-stage maturity
- limited number of AI deployments
- need for standardization and tight control

Strengths:

- clear standards
- easier governance consistency
- efficient concentration of expertise

Weaknesses:

- weaker domain fit
- slower response to local context
- risk of central bottlenecks

### 4.2 Model B: Hub-and-spoke

Best fit:

- expanding portfolio of AI use cases
- need to balance domain context with common standards

Strengths:

- better domain alignment
- reusable central standards
- stronger scale potential

Weaknesses:

- coordination overhead
- more complex reporting lines
- possible conflict between central and embedded roles

### 4.3 Model C: Federated

Best fit:

- high organizational maturity
- multiple domains with their own AI operating capability

Strengths:

- strong domain specialization
- faster local decision-making
- flexibility for scenario-sensitive design

Weaknesses:

- risk of governance fragmentation
- harder standard enforcement
- greater cross-domain consistency burden

### 4.4 Transition path

The expected progression is:

1. centralized during early controlled adoption
2. hub-and-spoke during scaling
3. federated only after governance, infrastructure, and domain capability are mature

Organizations should not skip directly to federated operation in high-stakes domains.

## 5. Trust, Algorithm Aversion, and Change Management

### 5.1 Problem definition

Employees do not adopt algorithmic systems mechanically. They may reject them after visible mistakes, over-correct them, or rely on them too heavily. Trust should therefore be treated as an organizational design problem, not a messaging problem.

### 5.2 Trust-building strategies

#### Graduated exposure

Move from assist to recommend gradually, with visible checkpoints and narrow pilots before wider use.

#### Transparency

Explain what the system does, what it does not do, and what signals should trigger skepticism or override.

#### Modifiability

Allow users to challenge or revise outputs where the task type justifies it, rather than forcing blind acceptance.

#### Fair comparison

Compare human and AI performance using consistent criteria so users do not judge machine errors more harshly than human ones.

### 5.3 Training design

Training should differ by audience:

- domain experts need workflow-specific use and override training
- executives need governance and accountability literacy
- engineering teams need domain and regulatory understanding

### 5.4 Change management

Useful mechanisms include:

- champion networks
- shared examples of successful use
- visible review of failures and near misses
- repeated demonstration that fallback actually works

### 5.5 Organizational expression of human-AI complementarity

The organization should assign analytical, repetitive, and monitoring strengths to AI, while keeping ambiguity management, ethical judgment, and accountability with humans.

### 5.6 Organizational complements

AI tools do not create performance on their own. Gains depend on workflow redesign, performance measurement, role clarity, and managerial routines that embed the tools into actual decision practice.

## 6. Cross-Functional Collaboration

### 6.1 Collaboration structure

AI decision systems should be run through recurring collaboration among:

- business domain teams
- AI and data teams
- legal and compliance teams
- fairness and audit stakeholders when risk is high

### 6.2 Operating interfaces

#### Domain team to AI and data team

Share decision objectives, contextual constraints, exception patterns, and signs of practical failure.

#### AI and data team to legal and compliance

Share model changes, material risk assumptions, documentation, and governance events.

#### Domain team to legal and compliance

Share downstream impact, complaints, fairness concerns, and evidence of scenario shifts.

### 6.3 Review cadence

Suggested review structure:

- weekly operational review for active systems
- monthly governance review for exceptions, drift, and overrides
- quarterly strategic review for authority level, evidence quality, and policy change

### 6.4 Escalation routes

Escalation paths should be predefined for:

- drift
- subgroup anomalies
- repeated override disagreement
- regulator-facing incidents
- scenario changes requiring fallback

### 6.5 Shared artifacts

Every serious AI decision program should maintain:

- role and responsibility documents
- authority assignment logs
- model and policy change logs
- incident and fallback records
- regular review summaries

## 7. Organizational Maturity Model

### 7.1 Summary table

| Level | Description | Typical AI scope | Typical organization model |
| --- | --- | --- | --- |
| 1 | exploration | assist pilots | project-based or centralized |
| 2 | formalization | assist in production, limited recommend pilots | centralized |
| 3 | scaling | recommend in production, bounded automate pilots | hub-and-spoke |
| 4 | optimization | dynamic mode shifts across scenarios | federated with strong central governance |

### 7.2 Level 1: Exploration

Characteristics:

- small pilot portfolio
- informal practices
- limited AI literacy
- no meaningful automate use

Key priority:

- establish basic governance and role clarity

### 7.3 Level 2: Formalization

Characteristics:

- first production use cases
- documented governance rules
- clearer owner assignments
- limited recommend pilots

Key priority:

- standardize approval, monitoring, and documentation

### 7.4 Level 3: Scaling

Characteristics:

- multiple domains using AI
- center of excellence or equivalent coordination
- regular review cadence
- bounded automate pilots in lower-risk settings

Key priority:

- scale without losing governance consistency

### 7.5 Level 4: Optimization

Characteristics:

- domain-level operating capability
- scenario-sensitive authority management
- strong evidence generation
- mature monitoring and audit systems

Key priority:

- prevent complacency and governance drift

### 7.6 Maturity checklist dimensions

Assess maturity across:

- AI staffing depth
- governance documentation
- workflow ownership
- monitoring and audit practice
- fairness and compliance capability
- domain AI literacy
- cross-functional collaboration quality

## 8. Domain-Specific Organization Guidance

### 8.1 Operations

Recommended design:

- embedded AI engineering support
- strong exception handling protocol
- rapid fallback-to-manual operations plan
- performance-centered review

### 8.2 Finance

Recommended design:

- strong compliance integration
- dedicated fairness oversight
- explicit audit ownership
- independent review of AI-supported recommendations

### 8.3 Healthcare

Recommended design:

- tight clinician and AI team collaboration
- strong safety-first review logic
- external or independent validation where justified
- shortest escalation path for patient-facing risk

### 8.4 Strategy

Recommended design:

- light but explicit AI support
- direct executive engagement
- stronger focus on augmentation than automation

### 8.5 Marketing and product

Recommended design:

- experimentation-friendly culture
- fast feedback loops
- privacy-aware but not paralysis-inducing governance
- strong collaboration between creative, product, and analytics functions

### 8.6 Summary table

| Domain | Typical AI mode | Governance burden | Organizational priority |
| --- | --- | --- | --- |
| Operations | bounded automate | lower | exception handling and monitoring |
| Finance | assist or recommend | high | fairness, compliance, auditability |
| Healthcare | assist or tightly governed recommend | highest | clinician control and safety |
| Strategy | assist | lower | executive interpretation and context |
| Marketing and product | recommend | medium | experimentation and privacy balance |

## 9. Integrated Organizational Principles

### Principle 1

Organization structure should scale with AI autonomy.

### Principle 2

Accountability should be explicit rather than diffusely shared.

### Principle 3

Algorithm aversion should be addressed through design and process, not slogans.

### Principle 4

Maturity should be built gradually; skipping stages creates governance gaps.

### Principle 5

Cross-functional collaboration should be defined by protocol, not goodwill alone.

### Principle 6

Human-AI complementarity should be a design assumption, not a rhetorical claim.

### Principle 7

Technology adoption without organizational embedding rarely produces durable performance gains.

## References

- Jarrahi, M. H. (2018). Artificial Intelligence and the Future of Work: Human-AI Symbiosis in Organizational Decision Making.
- Dietvorst, B. J., Simmons, J. P., and Massey, C. (2015). Algorithm Aversion.
- Brynjolfsson, E., Hitt, L. M., and Kim, H. H. (2011). Strength in Numbers.

This document should be used together with Part 1 and Part 2. Workflow design, infrastructure design, and organizational design are interdependent parts of the same AI decision-governance system.
