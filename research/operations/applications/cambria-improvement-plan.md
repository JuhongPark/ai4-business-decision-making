# Research Direction: From Delegation Governance to Alignment and Safety

status: draft
date: 2026-03-27

## Where the Research Stands

This repository started with a practical question: under what conditions should organizations let AI systems assist, recommend, or automate business decisions? The answer took the form of a 6-dimensional scoring framework, 7 decision rules, 3 override constraints, and a 71-incident failure inventory.

During the course of this work, a broader realization emerged. The question "how much authority should this AI system receive?" is not only a business governance question. It is an alignment question. The framework already encodes alignment-relevant structure — risk thresholds, fallback triggers, evidence requirements — but the research has not yet made that connection explicit, and the framework itself exists only as prose. Both of these are limitations worth addressing.

## What the Research Already Contains

| Framework component | What it does | Alignment parallel |
|---|---|---|
| Authority levels (assist / recommend / automate) | Grades how much autonomy AI receives | Delegation spectrum in human oversight research |
| Risk level dimension | Evaluates consequence severity | Catastrophic risk assessment |
| Evidence strength dimension | Rates confidence in the AI system's outputs | Model inspectability — how verifiable is the reasoning? |
| Governance readiness dimension | Checks organizational oversight capacity | Oversight infrastructure and corrigibility |
| Override rules | Hard constraints that cap authority regardless of score | Safety constraints that cannot be optimized away |
| Incident inventory (71 cases) | Catalogs real-world AI deployment failures | Alignment failure modes — specification gaming, distributional shift, oversight collapse |

These parallels are not retrofitted. The framework was built to answer "when should AI be trusted with authority," which is the deployment-side formulation of the alignment problem.

## Open Problems

### 1. The evidence strength ceiling

The framework's weakest dimension is evidence strength. Currently it relies on external proxies: regulatory validation, peer review, company documentation. These tell you whether other people trust the system, not whether the system's internal reasoning supports the decision.

This is where interpretability becomes necessary — not as a theoretical interest, but as a practical requirement. If a lending model scores high on every other dimension but its reasoning cannot be inspected, the framework forces a one-level authority reduction. Mechanistic interpretability (circuit-level model understanding, feature attribution, sparse autoencoders) would allow evidence strength to be grounded in model internals rather than external reputation.

### 2. The framework exists only as prose

The scoring sheet, decision tree, and override rules are documented in markdown. They have never been implemented as executable code. This means:

- The framework cannot be stress-tested against the incident inventory to verify it would have flagged failures before they occurred.
- The interaction between scoring bands and override rules cannot be explored systematically.
- Sensitivity analysis (how much does authority change when one dimension shifts?) is not possible.

### 3. The incident inventory is manually classified

71 incidents are cataloged and split into general-AI and LLM-specific failure types. The classification was done by hand. NLP-based clustering could validate whether the manual groupings hold, discover patterns the manual process missed, and map incident clusters back to framework dimensions.

## Next Steps

### Step 1: Make the alignment connection explicit

The README and research framing should reflect what the research actually is. The project introduction currently reads as a business consulting study. It should state the delegation calibration problem directly: this research addresses when and how much autonomous authority AI systems should receive, evaluated across six contextual dimensions.

Add a section connecting the framework to AI safety and alignment:
- Why delegation calibration is an alignment problem (even well-aligned models should not receive unlimited authority)
- How the evidence strength dimension creates demand for interpretability
- How the incident inventory maps to alignment failure modes

### Step 2: Implement the framework in Python

**`notebooks/authority_scorer.ipynb`**

Implement the scoring sheet and decision tree as working code.

- Encode dimension values: `DecisionStructure` (structured=3, semi=2, unstructured=1), `RiskLevel` (low=3, medium=2, high=1), `ScenarioCondition` (baseline=3, stress=2, edge_case=1), `EvidenceStrength` (strong=3, moderate=2, weak=1), `GovernanceReadiness` (strong=3, partial=2, weak=1).
- Scoring function: sum 5 dimensions (range 5–15) and map to authority bands (5–8 → assist, 9–11 → assist or recommend, 12–13 → recommend, 14–15 → recommend or automate with guardrails).
- Override rules as hard constraints: high-risk + weak governance → cap at assist; edge-case → cap at assist; weak evidence in consequential decisions → reduce one level.
- Demonstrate with real scenarios from the research (high-risk lending, low-risk operations, stress-condition healthcare).
- Visualize dimension scores (radar chart) and authority levels across domain-risk combinations (heatmap).
- Interpretability gap analysis: for scenarios where evidence strength is weak, simulate the effect of raising it by one level through interpretability.

**`notebooks/incident_analysis.ipynb`**

Apply NLP to the 71-incident inventory.

- Parse incident tables from markdown into a structured DataFrame (date, company, business_use, failure_mechanism, consequence, evidence_type).
- TF-IDF vectorize failure mechanisms and consequences.
- K-means clustering (k=4–6) to discover incident groupings and compare against the manually identified failure patterns.
- PCA or t-SNE visualization of the incident space.
- Map each cluster to framework dimensions: which dimension failures would have caught each incident type?
- Map clusters to alignment failure categories: specification gaming, distributional shift, oversight failure, fluent hallucination.

**`scripts/evaluate.py`**

CLI tool for the scoring engine.

- Arguments: --domain, --structure, --risk, --scenario, --evidence, --governance.
- Outputs: authority_level, total_score, active_override_rules, reasoning.
- Supports --format json and --input batch.csv.

### Step 3: Write the interpretability bridge

**`research/extensions/interpretability-bridge.md`**

"Why Mechanistic Interpretability Matters for Delegation Calibration"

1. The evidence strength limitation — external proxies are insufficient for grounding delegation authority.
2. What interpretability enables — mechanistic interpretability, feature attribution, probing, and sparse autoencoders each translate into concrete upgrades to evidence strength evaluation.
3. Concrete scenarios — for lending, clinical support, and hiring, show how authority level changes when interpretability is available vs. absent (using the scoring sheet numerically).
4. Research directions — treating delegation as dynamic policy optimization (RL framing), connecting incident failure modes to alignment science, building interpretability-aware governance instruments.

### Step 4: Directory structure and dependencies

- Create `notebooks/` directory and `requirements.txt` (pandas, numpy, scikit-learn, matplotlib, seaborn).
- Update README repository structure to include new directories.

## Execution Priority

| Order | Step | Effort | Rationale |
|---|---|---|---|
| 1 | Step 1: alignment framing | 1 hour | Makes the research legible for what it already is |
| 2 | Step 2a: authority_scorer.ipynb | 3–4 hours | Validates the framework computationally |
| 3 | Step 2b: incident_analysis.ipynb | 3–4 hours | Tests whether manual incident classification holds under NLP analysis |
| 4 | Step 3: interpretability bridge | 2 hours | Addresses the evidence strength ceiling directly |
| 5 | Step 2c: evaluate.py | 2 hours | Makes the framework usable beyond the notebook |
| 6 | Step 4: structure | 30 min | Cleanup |

## Constraints

- Do not alter existing research content. Add framing and implementations alongside it.
- Do not overstate the alignment connection. This is governance research that borders alignment, not an alignment solution.
- Code must faithfully implement the existing framework logic. No invented scoring rules.
- Incident analysis must preserve source attribution and evidence-type classification.
