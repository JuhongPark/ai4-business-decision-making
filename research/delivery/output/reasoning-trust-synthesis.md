# From Interpretability to Reasoning Trust: A Practitioner's Path to Verifiable AI in Business Decision-Making

status: draft
date: 2026-03-28
type: synthesis

---

## Part 1: Three Eras of AI Trust

### 1.1 Era 1 — The Interpretability Solution

In the earlier phase of AI deployment, the central problem was simple: AI models were accurate, but people would not use them. A diagnostic AI could outperform physicians on detection rates, but clinicians resisted adoption because they could not see the basis for the model's conclusions. The model said "malignant," and the physician had no way to agree or disagree.

The response was interpretability. Tools like SHAP (SHapley Additive exPlanations) decomposed each prediction into feature-level contributions, making it possible to show which variables drove the model's output. In medical AI collaborations, this was the breakthrough: showing a physician that the model attended to the same tissue characteristics, cell morphologies, and biomarkers that clinical training emphasized turned resistance into informed trust.

This worked because the verification loop was closed:

1. The AI presented **discrete evidence** — individual feature contributions that could be evaluated independently
2. The human expert had **independent domain knowledge** to judge whether the features were diagnostically relevant
3. The verification was **binary** — the model either focused on the right features or it did not
4. The model and the physician operated in the **same ontology** — tissue characteristics, lab values, patient history

Under these conditions, trust was earned through visible evidence and human verification. The expert could inspect the basis, apply their judgment, and make a collaborative decision. Interpretability solved the trust problem for this era.

### 1.2 Era 2 — The LLM Disruption

Large language models arrived and inverted the dynamic. In the SHAP era, the problem was too little trust. In the LLM era, the problem became too much.

LLM outputs do not look like feature attribution plots. They look like consultant memos — fluent, structured, confident, written in the language of business analysis. Where a SHAP explanation required a domain expert to interpret a chart, an LLM output reads as if it has already been interpreted. It presents conclusions, cites evidence, and constructs arguments. It feels pre-verified.

The initial concern was factual accuracy: hallucination, fabrication, citation of non-existent sources. This is a real problem, and fact-checking is important. But fact-checking, while labor-intensive, is ultimately tractable. Given time and access, a human can verify whether a specific claim is true, whether a cited source exists, whether a number is accurate.

The field observation was sobering: even this tractable problem proved too difficult for most organizations. Working across companies attempting to integrate LLMs into business analysis, the pattern was consistent — the effort required to verify basic claims exceeded what busy teams would invest. Fact-checking happened sporadically, if at all.

### 1.3 Era 3 — The Reasoning Gap

The deeper realization emerged from watching what happened when facts were checked. Even when individual facts survived verification, the reasoning connecting those facts to conclusions often did not.

A concrete case made this visceral. An LLM was tasked with producing a marketing strategy analysis at consulting-firm quality. The output was structured, professional, and cited specific data points. One key recommendation: advertising trend cycles had shortened dramatically — to under one week — and the company should pivot to rapid-response marketing.

From the perspective of someone trained at BCG, where analysis directly informs decisions worth tens of billions of won and every link in the analytical chain must justify itself, this analysis had a fundamental flaw that had nothing to do with the facts themselves. The sources supporting the "one-week trend cycle" claim were unattributed blog posts and content published by advertising agencies selling rapid-cycle marketing services. In consulting practice, these sources would never survive the evidence review process. They are sales material, not evidence. The claim might be true, but the evidentiary basis was grossly inadequate for the confidence expressed.

The people receiving this analysis did not catch the problem. The analysis was fluent. The facts were presented confidently. The reasoning appeared logical. And because the output looked like the kind of analysis they expected from experts, they accepted it without scrutinizing the reasoning chain — without checking whether the source quality justified the claim confidence, whether the inference from evidence to conclusion was valid, whether the recommendations conformed to professional analytical standards.

This is where fact-checking ends and reasoning verification begins. And this is the gap that no existing framework, tool, or methodology addresses.

### 1.4 The Three Questions

When a business decision-maker receives AI-generated reasoning, they face three questions in ascending order of difficulty:

**Question 1: Are the facts correct?** Hard but solvable. Tools exist. Time can be invested. Individual claims can be verified against primary sources.

**Question 2: Is the reasoning valid?** Harder. Even if every fact is correct, the logical chain connecting facts to conclusions may be flawed. Correlation may be presented as causation. Weak evidence may support strong claims. Sources may be inadequate for the confidence expressed. Contextual factors may be ignored.

**Question 3: Can I even tell?** The hardest question, and the one that matters most. If the person receiving AI reasoning does not have a method to assess reasoning quality, then the quality of that reasoning is irrelevant in practice. No one is checking.

The consulting industry solved Question 3 through years of training, institutional culture, and structured analytical frameworks. No equivalent exists for evaluating AI reasoning. As AI reasoning increasingly supplements or replaces human analysis in business decisions, this absence becomes critical.

---

## Part 2: The Delegation Framework — What We Built

### 2.1 The Governance Answer

The first phase of this research produced a structured answer to the question: when should firms use AI to assist, recommend, or automate high-stakes business decisions?

The answer is a 6-dimensional adaptive framework that evaluates delegation fitness based on:

1. **Domain** — what business function the decision belongs to
2. **Decision structure** — how structured vs. unstructured the decision is
3. **Risk level** — how consequential failure would be
4. **Scenario condition** — whether conditions are baseline, stress, or edge-case
5. **AI role** — what level of authority AI is granted (assist, recommend, automate with guardrails)
6. **Evidence strength** — how strong the evidence supporting AI reliability is

The framework produces a score (5-15) mapped to authority bands, with three hard override rules that cap authority when conditions are unfavorable. It was validated against 71 documented real-world AI governance failures.

Details: [taxonomy/taxonomy-summary.md](../../core/taxonomy/taxonomy-summary.md) | [taxonomy/scoring-sheet.md](../../core/taxonomy/scoring-sheet.md) | [taxonomy/decision-tree.md](../../core/taxonomy/decision-tree.md)

### 2.2 The 71 Incidents

The framework is grounded in empirical evidence: 71 documented AI governance failures sourced from regulatory actions (CFPB, FTC, EEOC), court decisions, NTSB investigations, SEC filings, and company disclosures. These include:

- Zillow Offers: $304M loss from over-delegation to pricing models
- Amazon recruiting: gender-biased resume screening from proxy features
- Air Canada chatbot: incorrect policy guidance treated as company speech
- Mata v. Avianca: hallucinated legal citations submitted to federal court
- Google Bard: factual error in public demo erasing $100B+ in market value

Retrospective testing showed the framework would have prevented 12 of 20 key incidents outright by recommending a lower authority level. Seven more were partially flagged. One was missed entirely.

Details: [business-alignment/incidents/incident-inventory.md](../../extensions/business-alignment/incidents/incident-inventory.md) | [business-alignment/incidents/alignment-failure-mapping.md](../../extensions/business-alignment/incidents/alignment-failure-mapping.md)

### 2.3 The Structural Assumption

The framework is sound as a governance instrument. But it contains a hidden dependency: every authority level above "do not use AI" assumes that humans can meaningfully evaluate AI outputs.

- **Assist** assumes the human evaluates the AI's suggestion independently
- **Recommend** assumes the human critically assesses the recommendation before acting
- **Override rules** assume someone can assess evidence strength and governance readiness

This assumption is:

- **Empirically violated**: 66% of employees accept AI output without evaluating accuracy (Microsoft, 2025). 91% of executives say employees overtrust AI (McKinsey, 2024-2025).
- **Technically undermined**: CoT explanations are unfaithful 60-80% of the time (Anthropic, 2025). AI self-explanation cannot be relied upon as a verification mechanism.
- **Practically unsupported**: No verification methodology exists for non-expert business users.

Without reasoning verification capability, the distinction between "assist" and "automate" collapses in practice. The AI assists, the human rubber-stamps, and the effective authority is higher than the framework intended.

This is not a flaw in the framework. It is the gap that the next phase of research fills. The framework provides the **when** of AI delegation. Reasoning verification provides the **how** of human evaluation.

Details: [drafting/narrative-bridge-structural-assumption.md](../../core/drafting/narrative-bridge-structural-assumption.md)

---

## Part 3: The Alignment Depth — Why This Is Not Just Governance

### 3.1 Delegation Calibration as an Alignment Problem

The delegation question is not merely operational. It is an alignment problem.

Traditional AI alignment asks: does the model pursue objectives aligned with human values? This research asks the complementary question: even if we solve technical alignment perfectly, how much autonomous authority should a given AI system receive in a given context?

A model that is value-aligned in the technical sense may still produce harmful outcomes if deployed at an inappropriate authority level — if it automates decisions it should only recommend, or if it operates in conditions outside its validated envelope. Technical alignment determines whether the system can be trusted in principle. Delegation calibration determines whether it should be trusted in practice.

The 71 incidents demonstrate this concretely. Most failures were not cases of technically misaligned AI. They were cases of correctly functioning systems deployed at the wrong authority level, in the wrong conditions, without adequate verification.

Details: [extensions/delegation-as-alignment.md](../../extensions/delegation-as-alignment.md)

### 3.2 From SHAP to the Evidence Strength Ceiling

The interpretability bridge connects directly to the professional arc. The same researcher who used SHAP to solve the Era 1 trust problem now confronts why that approach cannot solve Era 3.

SHAP provided partial **process trust** — showing which inputs mattered. It worked because the evidence was discrete, the expert was independent, and verification was binary.

LLM reasoning breaks all three conditions:

| Condition | SHAP Era | LLM Era |
|---|---|---|
| Evidence type | Discrete feature contributions | Continuous narrative chain |
| Expert baseline | Physician has independent knowledge | User often lacks domain expertise (that is why they asked the AI) |
| Verification type | Binary (right features or not) | Spectrum (degrees of soundness, relevance, source quality) |

The existing framework's evidence strength dimension captures performance trust (does the system work?) and purpose trust (was it designed for this?), following Lee and See (2004). It does not capture process trust (do we understand how it reaches its conclusions?).

For traditional ML, SHAP and feature attribution could partially close this gap. For LLM reasoning, the gap requires fundamentally different methods: not feature-level inspection but argumentative-level verification — source quality, inferential validity, normative acceptability, confidence calibration.

Details: [extensions/interpretability-bridge.md](../../extensions/interpretability-bridge.md) | [drafting/narrative-bridge-shap-to-llm.md](../../core/drafting/narrative-bridge-shap-to-llm.md)

### 3.3 The Rubber Stamp Problem

The 6-layer business-context alignment framework identifies the mechanism through which passive acceptance operates:

**Layer 4 — Validation alignment**: When AI generates an output and a human reviews it in the same interface, under time pressure, without an independent baseline, the "review" becomes symbolic. The human checks whether the output seems reasonable, not whether the reasoning is sound. Generation and validation collapse into a single act.

This is the rubber-stamp problem. It is not a character flaw of lazy employees. It is a structural consequence of workflow design. When the AI output is fluent, structured, and arrives pre-formatted as a professional memo, the cognitive default is acceptance. Rejecting or significantly modifying the output requires more effort than accepting it — and requires a method for assessing reasoning quality that most users do not have.

The verification framework addresses this directly: it converts symbolic review into substantive review by providing a structured protocol that the reviewer applies before the output is accepted.

Details: [extensions/business-alignment/alignment-framework.md](../../extensions/business-alignment/alignment-framework.md)

---

## Part 4: Why It Gets Worse — Information Structure and Decision Capability

### 4.1 Five Information Shocks

The information structure analysis reveals that the current AI trust problem is the fifth iteration of a recurring pattern. Each major information shock lowers costs but raises new scarcities:

| Shock | What Became Cheap | What Became Scarce |
|---|---|---|
| Public internet | Information access | Attention, filtering |
| Search engines | Information retrieval | Question formulation |
| Enterprise analytics | Data tooling | Metric selection, interpretation |
| Social media | Visibility, distribution | Signal-to-noise filtering |
| AI/LLMs | Interpretation, analysis | Trust calibration, reasoning verification |

Each wave follows the same sequence: costs drop, usage expands, verification becomes the bottleneck, failures accumulate, and eventually organizations build the verification capability they should have built earlier. The lag between adoption and verification capability is measured in years.

This research aims to shorten that lag for AI reasoning.

Details: [extensions/information-structure/initial-analysis.md](../../extensions/information-structure/initial-analysis.md)

### 4.2 Where LLMs Actually Help (and Where They Do Not)

The LLM decision paradigm analysis positions LLMs within the lineage of Herbert Simon's bounded rationality. LLMs do not eliminate bounded rationality — they alter it by reducing the cost of searching, summarizing, and reframing.

LLMs are most valuable in the **pre-optimization zone**: problem articulation, information synthesis, option generation, tradeoff surfacing, cross-functional translation, iterative reframing. They are least reliable at autonomous judgment under ambiguity.

Critically, the DeLLMa research shows that unscaffolded LLM reasoning degrades with complexity. Trustworthiness is a property of the model-plus-scaffold system, not the model alone. An LLM producing strategy analysis without a verification scaffold is operating in exactly the conditions where its reasoning is least reliable.

Details: [extensions/information-structure/llm-decision-paradigm.md](../../extensions/information-structure/llm-decision-paradigm.md)

### 4.3 The Capability Ladder

Business decision-making is a 7-level stack, and AI replacement potential decreases as you ascend:

| Level | Capability | AI Replacement Potential |
|---|---|---|
| 1 | Retrieval and basic synthesis | Very high |
| 2 | Option expansion and first-pass analysis | High |
| 3 | Structured sub-decisions | Moderate-high (with guardrails) |
| 4 | Problem framing and translation | Moderate (assistance) |
| 5 | Judgment under ambiguity | Limited |
| 6 | Legitimacy and accountability | Low |
| 7 | Constitutional choice (where AI may have authority) | Very low |

The irony: the levels where AI reasoning is weakest are exactly the levels where reasoning verification matters most. At Level 1, verification is fact-checking. At Level 5, verification requires assessing whether the reasoning appropriately weighs uncertainty, norms, and context. The organizational trend is toward higher-level usage, which means the reasoning verification gap is widening.

Details: [extensions/information-structure/capability-ladder.md](../../extensions/information-structure/capability-ladder.md)

### 4.4 Why Consulting-Grade Verification Matters More Than Ever

The information structure analysis shows that consulting firms persisted through every information shock because they provide what cheap information cannot: problem framing, signal filtering, cross-functional translation, organizational legitimacy.

The core consulting skill underneath all of these is reasoning verification — the trained ability to assess source credibility, check inferential validity, evaluate normative compliance, and calibrate confidence against evidence. This skill was developed through years of institutional practice: junior consultants learn it from senior partners who scrutinize every analytical chain.

No equivalent training exists for evaluating AI reasoning. The reasoning verification framework aims to externalize this skill — to make it systematic, teachable, and applicable by people who did not spend years in professional training learning to scrutinize analytical chains.

Details: [drafting/narrative-bridge-information-structure.md](../../core/drafting/narrative-bridge-information-structure.md)

---

## Part 5: The Reasoning Verification Framework

### 5.1 What Must Be Verified

The framework addresses four dimensions of reasoning quality, each with a dedicated assessment method:

| Dimension | Core Question | Method |
|---|---|---|
| **Source quality** | Does the evidence cited actually support the claim at the confidence level expressed? | 5-level source credibility scale + source-claim proportionality check |
| **Inferential validity** | Does the conclusion follow from the premises? | Inference type classification + type-specific validity checks + reverse test |
| **Normative acceptability** | Does the reasoning conform to applicable professional, legal, ethical, and social standards? | Professional review test + domain-specific normative checks |
| **Confidence calibration** | Is the expressed certainty proportionate to the evidence strength? | Confidence-evidence alignment matrix + hedge test |

### 5.2 Reasoning Failure Taxonomy

The framework identifies 18 failure types across four categories:

**Category A — Source-level failures** (5 types): fabrication, misrepresentation, quality mismatch, selection bias, temporal decay

**Category B — Inferential failures** (7 types): correlation-causation conflation, unjustified generalization, missing premises, false dichotomy, scope mismatch, confidence-evidence gap, circular reasoning

**Category C — Normative failures** (4 types): professional standard violation, ethical norm violation, regulatory non-compliance, social convention deviation

**Category D — Structural failures** (4 types): sycophantic alignment, prompt anchoring, coherence without validity, premature convergence

Each type is defined by mechanism, business manifestation, detection difficulty, and primary verification method.

Details: [framework/reasoning-failure-taxonomy.md](../../core/framework/reasoning-failure-taxonomy.md)

### 5.3 Source Quality Assessment

The source quality method formalizes the instinct that a trained consultant applies when evaluating evidence:

**5-level credibility scale:**
- Level 5: Authoritative primary source (SEC filings, government statistics, peer-reviewed trials)
- Level 4: Qualified institutional source (major research institutions, established data providers)
- Level 3: Qualified professional source (named analysts, professional journals, trade publications with editorial standards)
- Level 2: Unverified secondary source (blog posts, aggregator sites, news without primary citations)
- Level 1: Commercially motivated source (vendor white papers, sponsored content, advertising agency reports)

**Core rule**: High-stakes claims require Level 4-5 sources. Any conclusion-driving claim resting on Level 1 sources only is flagged as inadequate.

Details: [framework/reasoning-verification-source-quality.md](../../core/framework/reasoning-verification-source-quality.md)

### 5.4 Inferential Validity Assessment

The inferential validity method decomposes reasoning into steps, classifies each by inference type (deductive, inductive, abductive, analogical), and applies type-specific validity checks.

The most powerful single tool is the **reverse test**: "What would have to be true for this conclusion to be wrong?" If the AI output does not address plausible failure conditions, the reasoning has unexamined vulnerabilities.

Details: [framework/reasoning-verification-inferential-validity.md](../../core/framework/reasoning-verification-inferential-validity.md)

### 5.5 Normative Acceptability Assessment

The normative assessment checks whether AI reasoning conforms to applicable standards across four domains: legal/regulatory, professional standards, ethical principles, and social conventions.

The core tool is the **professional review test**: "If a licensed professional in this domain reviewed this reasoning, what would they flag?" This does not require access to the professional — it requires asking whether the analysis would survive expert scrutiny.

Details: [framework/reasoning-verification-normative-assessment.md](../../core/framework/reasoning-verification-normative-assessment.md)

### 5.6 Confidence Calibration Assessment

The confidence calibration method detects when AI-expressed certainty exceeds evidence strength. It maps expressed confidence (linguistic markers, quantitative precision) against actual evidence strength (source quality assessment) and flags misalignments.

The **hedge test** detects selective calibration: AI that hedges peripheral claims while stating core claims without qualification, creating a false impression of intellectual rigor.

Details: [framework/reasoning-verification-confidence-calibration.md](../../core/framework/reasoning-verification-confidence-calibration.md)

### 5.7 Integration with the Delegation Framework

Reasoning verification integrates into the existing scoring system through two mechanisms:

**Extended evidence strength**: The evidence strength dimension becomes a two-component score — system-level validation (existing) and output-level reasoning quality (new). The combined score equals the minimum of the two components (weakest-link principle). A well-validated system producing flawed reasoning on a specific output receives a weak evidence score for that decision.

**Verification gate**: Before the scoring sheet applies to a specific decision, a prerequisite check: has the AI output been verified? If not, the decision defaults to ASSIST regardless of framework score. This operationalizes the finding that nominal oversight without actual verification is functionally equivalent to no oversight.

Details: [framework/reasoning-verification-scoring-integration.md](../../core/framework/reasoning-verification-scoring-integration.md)

### 5.8 Validation Design

The framework will be validated through three approaches:

1. **Retrospective**: Apply the framework to 6 documented LLM incidents the delegation framework missed or only partially caught. Test whether specific verification steps would have caught each failure.
2. **Prospective**: Generate 15 fresh LLM business analyses (5 tasks × 3 models), apply the framework, and compare findings against independent expert review. Target: >70% detection rate, <30 minutes per output.
3. **Comparative**: Test whether practitioners using the framework detect more reasoning failures than those without it. Controlled comparison with planted failures across all taxonomy categories.

Details: [framework/reasoning-verification-pilot-protocol.md](../../core/framework/reasoning-verification-pilot-protocol.md)

---

## Part 6: The Conviction

### 6.1 Not Blind Trust, Not Rejection

People will not stop using AI for business decisions. Nor should they. AI reasoning, when sound, synthesizes information at scale, identifies patterns humans miss, and accelerates analysis dramatically.

But the path to beneficial AI adoption cannot be blind trust. The SHAP era taught a clear lesson: trust follows from visible evidence and human verification. The LLM era disrupted this by producing outputs that feel verified when they are not.

The evidence is stark:
- 66% of employees accept AI output without evaluating accuracy
- 91% of executives say employees overtrust AI
- CoT explanations are unfaithful 60-80% of the time
- ~58% of LLM responses exhibit sycophantic tendencies
- Once sycophancy triggers, it persists in 78.5% of subsequent interactions
- Larger, more capable models produce less faithful reasoning

The trend lines are adverse. As models become more fluent, more personalized, and more confident, the gap between perceived trustworthiness and actual trustworthiness widens.

### 6.2 Informed Trust Through Verifiable Reasoning

The answer is not to reject AI reasoning. The answer is to build the verification capability that makes informed trust possible.

This research provides:

1. **A governance framework** (the 6-dimensional delegation system) that tells organizations when and at what authority level to use AI
2. **A verification methodology** (the reasoning verification framework) that tells individual decision-makers how to assess whether specific AI reasoning deserves trust
3. **An integration mechanism** (the extended evidence strength and verification gate) that connects governance-level delegation decisions to instance-level reasoning assessment

Together, these form a complete system. The governance framework without verification is a set of rules that organizations nominally follow while employees rubber-stamp AI outputs. Verification without governance is individual effort without organizational structure. Both are needed.

### 6.3 The Path Forward

When organizations can assess AI reasoning quality with the same rigor that a trained consultant applies to human analysis, they can:

- **Deploy AI confidently** where reasoning meets professional standards
- **Intervene precisely** where specific reasoning failures are identified, rather than accepting or rejecting wholesale
- **Build institutional competence** in AI-augmented decision-making that improves over time
- **Maintain human judgment** capabilities that deteriorate under passive acceptance
- **Protect their decisions, stakeholders, and integrity** from the consequences of unchecked AI reasoning

This is how we use AI well. Not by trusting blindly, not by rejecting reflexively, but by building the institutional and methodological capacity to verify reasoning — and thereby earning the confidence to act on it.

---

## Document Map

This synthesis draws on and connects the following research assets:

### Core Framework
- [taxonomy/taxonomy-summary.md](../../core/taxonomy/taxonomy-summary.md) — 6-dimensional category system
- [taxonomy/scoring-sheet.md](../../core/taxonomy/scoring-sheet.md) — scoring instrument and override rules
- [taxonomy/decision-tree.md](../../core/taxonomy/decision-tree.md) — sequential decision procedure
- [framework/evaluation-framework.md](../../core/framework/evaluation-framework.md) — 7-dimension evaluation framework

### Empirical Evidence
- [business-alignment/incidents/incident-inventory.md](../../extensions/business-alignment/incidents/incident-inventory.md) — 71 documented incidents
- [business-alignment/incidents/alignment-failure-mapping.md](../../extensions/business-alignment/incidents/alignment-failure-mapping.md) — retrospective framework test
- [core/evidence/evidence-strengthening.md](../../core/evidence/evidence-strengthening.md) — evidence upgrade documentation
- [core/scenario-packs/cross-scenario-synthesis.md](../../core/scenario-packs/cross-scenario-synthesis.md) — cross-scenario findings

### Alignment Extensions
- [extensions/delegation-as-alignment.md](../../extensions/delegation-as-alignment.md) — delegation as alignment argument
- [extensions/interpretability-bridge.md](../../extensions/interpretability-bridge.md) — interpretability and evidence strength
- [extensions/alignment-literature-bridge.md](../../extensions/alignment-literature-bridge.md) — literature validation and gap identification
- [extensions/business-alignment/alignment-framework.md](../../extensions/business-alignment/alignment-framework.md) — 6-layer business-context alignment

### Information Structure
- [extensions/information-structure/initial-analysis.md](../../extensions/information-structure/initial-analysis.md) — five information shocks
- [extensions/information-structure/llm-decision-paradigm.md](../../extensions/information-structure/llm-decision-paradigm.md) — LLM decision capabilities
- [extensions/information-structure/capability-ladder.md](../../extensions/information-structure/capability-ladder.md) — 7-level capability stack

### Reasoning Verification Framework (new)
- [framework/reasoning-failure-taxonomy.md](../../core/framework/reasoning-failure-taxonomy.md) — 18 failure types
- [framework/reasoning-verification-source-quality.md](../../core/framework/reasoning-verification-source-quality.md) — source assessment method
- [framework/reasoning-verification-inferential-validity.md](../../core/framework/reasoning-verification-inferential-validity.md) — inferential validity method
- [framework/reasoning-verification-normative-assessment.md](../../core/framework/reasoning-verification-normative-assessment.md) — normative assessment method
- [framework/reasoning-verification-confidence-calibration.md](../../core/framework/reasoning-verification-confidence-calibration.md) — confidence calibration method
- [framework/reasoning-verification-scoring-integration.md](../../core/framework/reasoning-verification-scoring-integration.md) — framework integration
- [framework/reasoning-verification-pilot-protocol.md](../../core/framework/reasoning-verification-pilot-protocol.md) — validation design

### Narrative Bridges
- [drafting/narrative-bridge-three-eras.md](../../core/drafting/narrative-bridge-three-eras.md) — three-era framing
- [drafting/narrative-bridge-incidents-reframed.md](../../core/drafting/narrative-bridge-incidents-reframed.md) — incidents as reasoning acceptance failures
- [drafting/narrative-bridge-structural-assumption.md](../../core/drafting/narrative-bridge-structural-assumption.md) — framework's hidden verification dependency
- [drafting/narrative-bridge-shap-to-llm.md](../../core/drafting/narrative-bridge-shap-to-llm.md) — SHAP to LLM professional arc
- [drafting/narrative-bridge-information-structure.md](../../core/drafting/narrative-bridge-information-structure.md) — information structure and field observation

### Literature
- [literature/reasoning-trust-landscape.md](../../core/literature/reasoning-trust-landscape.md) — existing research landscape survey
- [planning/research-direction-reasoning-trust.md](../../core/planning/research-direction-reasoning-trust.md) — research direction statement
- [planning/research-direction-review.md](../../core/planning/research-direction-review.md) — direction review against existing work
