# 3-Part Research Plan: AI-Driven Business Decision-Making

status: draft
scope: extension of phases 01-19

## Research Background

The phase 1-19 research established a governance-centered framework for deciding when firms should use AI to assist, recommend, or automate high-stakes business decisions. It produced a six-axis taxonomy, a seven-step decision sequence, scenario-based domain analysis, and a category-based rule set for assigning AI authority.

This extension translates that framework into an implementation-oriented program. The earlier work answered what level of AI authority is justified. This program asks how that authority should be operationalized in workflows, what infrastructure is required to support it, and which organizational roles should own it.

## Integrated Research Question

How should workflow design, technical and governance infrastructure, and organizational structure be designed so that AI-enabled business decision-making can operate effectively in real institutional settings?

## Part 1: AI Decision Workflows

### Research Question

What role should AI play at each stage of a business decision process, and under what conditions should authority escalate or fall back across stages?

### Core Idea

The assist, recommend, and automate logic from the earlier research should be translated from the domain level to the workflow-step level. The goal is not simply to say that a domain is assist-heavy or automation-friendly. The goal is to specify which steps can tolerate higher autonomy, which steps require stronger human control, and how that changes when conditions deteriorate.

### Main Workstreams

#### 1. Decision stage model

Decompose general business decision-making into seven stages:

| Stage | Purpose | Typical AI contribution |
| --- | --- | --- |
| Problem recognition | detect anomalies, opportunities, or required action | anomaly detection, signal monitoring |
| Information gathering | collect and structure relevant data | ingestion, summarization, normalization |
| Analysis and prediction | estimate likely outcomes | predictive modeling, simulation |
| Alternative generation | produce or search options | optimization, recommendation generation |
| Judgment and selection | choose among tradeoffs | decision support signals |
| Execution | apply the chosen action | workflow triggers, bounded automation |
| Monitoring | track outcomes and detect drift | dashboards, alerts, drift detection |

#### 2. Stage-level AI mode mapping

Assign the appropriate AI mode for each stage under domain and scenario conditions.

Illustrative example for finance credit underwriting:

| Stage | Baseline | Stress | Edge case |
| --- | --- | --- | --- |
| Problem recognition | recommend | assist | assist |
| Information gathering | automate with guardrails | automate with guardrails | assist |
| Analysis and prediction | recommend | assist | assist |
| Alternative generation | assist | assist | assist |
| Judgment and selection | assist | assist | human-only |
| Execution | assist | human-only | human-only |
| Monitoring | automate with guardrails | recommend | assist |

The same mapping should be completed for operations, finance, and healthcare.

#### 3. Escalation and fallback flow design

Implement scenario transition logic in workflow terms:

- escalation conditions: signals that justify higher AI authority
- fallback triggers: signals that require lower AI authority
- human-in-the-loop checkpoints: stages where human review is mandatory

#### 4. Workflow pattern catalog

Define reusable workflow patterns:

- Pattern A: automation-first for structured, low-risk, stable conditions
- Pattern B: recommendation-centric for semi-structured, medium-risk contexts
- Pattern C: assist-centric for high-risk, regulated contexts
- Pattern D: human-led for unstructured or edge-case conditions

### Prior Research Assets to Reuse

| Existing asset | Use in Part 1 |
| --- | --- |
| `16_taxonomy/decision-tree.md` | workflow branching logic |
| `16_taxonomy/decision-rules.md` | authority assignment rules |
| `13_scenario-packs/*` | scenario transitions and examples |
| `04_framework/evaluation-framework.md` | stage-level evaluation criteria |
| `15_revision-01/governance-memo.md` | escalation and fallback principles |

### Deliverables

- domain-specific AI workflow diagrams for operations, finance, and healthcare
- stage-by-stage AI mode mapping tables
- reusable workflow pattern catalog
- escalation and fallback specification

## Part 2: AI Decision Infrastructure

### Research Question

What technical, data, governance, and evidence infrastructure is required to run AI-supported decision workflows reliably?

### Core Idea

The earlier research identified data quality, evidence strength, and governance readiness as determinants of justified AI authority, but it did not specify the infrastructure required to realize those conditions. Part 2 translates governance logic into technical and operational architecture.

### Main Workstreams

#### 1. Data infrastructure

Specify infrastructure for:

- data pipelines for collection, cleaning, and delivery
- data quality controls for accuracy, completeness, and timeliness
- feedback loops connecting outcomes back to models
- real-time versus batch processing choices by scenario and domain

#### 2. AI operations infrastructure

Specify infrastructure for:

- development environments and reproducibility
- model registry and version control
- deployment pipelines and rollback paths
- drift detection and alerting
- A/B testing and controlled rollout
- production performance monitoring

#### 3. Governance infrastructure

Specify infrastructure for:

- audit trails
- explainability tooling
- fairness monitoring
- regulatory response processes
- access control and approval boundaries
- incident management and fallback activation

#### 4. Evidence quality infrastructure

Specify infrastructure for:

- decision logs
- outcome tracking
- independent validation mechanisms
- evidence tier labeling for design claims versus outcome claims

#### 5. Domain-specific infrastructure requirements

Differentiate requirements across:

- low-risk domains such as operations and marketing
- high-risk domains such as finance and healthcare
- augmentation-heavy domains such as strategy and product

### Prior Research Assets to Reuse

| Existing asset | Use in Part 2 |
| --- | --- |
| `08_expansion/evidence-tier-method.md` | evidence system design |
| `18_publication-prep/evidence-register.md` | evidence management reference |
| `04_framework/evaluation-framework.md` | translate evaluation dimensions into infrastructure requirements |
| `02_literature/reading-notes/nist2023.md` | governance reference standard |
| `02_literature/reading-notes/eeoc2023.md` | fairness monitoring requirements |
| `02_literature/reading-notes/fda2025aimd.md` | healthcare infrastructure requirements |
| `02_literature/reading-notes/sec2017robo.md` | investment-domain infrastructure requirements |

### Deliverables

- four-layer reference architecture for AI decision systems
- domain-specific infrastructure requirement matrix
- infrastructure maturity checklist
- infrastructure gap analysis framework

## Part 3: Organizational Design for AI Decision-Making

### Research Question

How should roles, authority structures, and organizational culture be designed so that AI-supported decision systems can be governed and operated responsibly?

### Core Idea

The earlier research argued that accountability should remain explicit and that human override should be operational, not symbolic. Part 3 extends those principles into concrete organizational design.

### Main Workstreams

#### 1. Core role definitions

Define the core operating roles for AI decision systems:

- AI governance committee
- domain decision owner
- AI and data engineering
- legal and compliance
- fairness and ethics lead
- explainability and audit lead

#### 2. Authority structure

Translate the seven-step decision sequence into responsibility assignments:

- who classifies the domain
- who classifies decision structure and risk
- who assesses scenario condition
- who verifies evidence and governance readiness
- who approves the final AI authority level

#### 3. Organization model types

Compare three models:

- centralized AI office
- hub-and-spoke model with a center of excellence
- federated model with domain-level autonomy and light central oversight

#### 4. Trust and adoption design

Translate algorithm aversion and human-AI complementarity into operating practices:

- staged adoption from assist to recommend
- explicit transparency and override rules
- training and calibration for domain experts
- failure review and learning mechanisms

#### 5. Cross-functional collaboration

Specify operating interfaces among:

- business domain teams
- AI and data teams
- legal and compliance teams

Define meeting cadence, escalation routes, and shared artifacts.

#### 6. Organizational maturity model

Define an organizational path from exploration to formalization, scaling, and optimization, with role, governance, and autonomy requirements at each stage.

### Prior Research Assets to Reuse

| Existing asset | Use in Part 3 |
| --- | --- |
| `15_revision-01/governance-memo.md` | translate governance principles into roles and responsibilities |
| `16_taxonomy/decision-tree.md` | authority assignment sequence |
| `02_literature/reading-notes/jarrahi2018.md` | human-AI complementarity implications |
| `02_literature/reading-notes/dietvorst2015.md` | algorithm aversion and trust calibration |
| `02_literature/reading-notes/brynjolfsson2011.md` | organizational complements for decision performance |
| `10_domain-analysis/analysis.md` | domain-specific operating differences |

### Deliverables

- role definitions and RACI matrix
- organizational model comparison
- AI organization maturity model
- cross-functional collaboration protocol
- change management and training guidelines

## Integrated Architecture

The three parts should be treated as one operating system:

1. Part 1 defines how decisions flow.
2. Part 2 defines what infrastructure supports those flows.
3. Part 3 defines who owns, governs, and improves the system.

This creates an integrated implementation guide rather than three disconnected analyses.

## Recommended Sequence

### Phase A: Part 1 first

Translate the existing taxonomy and scenario packs into step-level workflow logic.

1. finalize the seven-stage decision model
2. complete stage-by-stage mappings for operations, finance, and healthcare
3. specify escalation and fallback flows
4. finalize reusable workflow patterns

### Phase B: Part 2 next

Derive infrastructure requirements from the workflows.

1. map infrastructure needs by workflow stage
2. define the four-layer reference architecture
3. create domain-specific infrastructure matrices
4. define maturity checkpoints

### Phase C: Part 3 next

Define who runs and governs the workflows and infrastructure.

1. define roles and responsibilities
2. compare organization models
3. define maturity stages
4. define change-management and training requirements

### Phase D: Integration

Combine all three parts into an implementation guide.

1. integrate domain-specific workflow, infrastructure, and organization guidance
2. create adoption roadmaps by firm maturity and domain type
3. consolidate into a final report

## Additional Literature Directions

| Part | Additional topic | Likely source types |
| --- | --- | --- |
| Part 1 | business process management, human-in-the-loop workflow design | journal articles, technical white papers |
| Part 2 | MLOps maturity, production AI architecture, governance tooling | technical docs, industry reports |
| Part 3 | AI center of excellence design, organizational change, decision governance | management research, consulting reports |
| Shared | AI governance implementation case studies | regulator materials, audit reports, company disclosures |
