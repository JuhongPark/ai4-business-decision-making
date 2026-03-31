# Meta-Analysis of 71 AI Governance Failures and the 6-Dimensional Adaptive Delegation Framework

## 1. Research Overview

### 1.1 Research Question

The central question of this research is:

> When should AI systems be granted autonomous decision-making authority, and when must humans retain control?

While prevailing AI adoption discourse remains trapped in a binary framing — "use AI or do not" — this research redefines AI delegation as a **calibration problem**. The core argument is that AI authority must be **adaptively adjusted** according to domain, risk, evidence, and governance conditions.

### 1.2 Methodology

This research takes a meta-analytic approach. Rather than conducting a single case study or industry-specific analysis, it **systematically collects, classifies, and cross-compares 71 real-world AI governance failure cases** to extract failure patterns and construct a framework inductively.

**Data Collection Protocol:**

- **Collection period**: 2018–2026
- **Sources**: Regulatory actions (FTC, DOJ, EEOC, SEC, CFPB, FDA), court decisions and sanctions orders, investigative journalism, corporate disclosures and SEC filings, NTSB investigation reports
- **Inclusion criteria**: An incident is included when at least one of the following holds: (1) clear financial loss, business wind-down, or public product rollback; (2) lawsuit, settlement, sanction, or regulatory action; (3) concrete governance failure with visible customer, worker, or public harm; (4) forced pause, restriction, or redesign of AI deployment; (5) material impact on trust, brand credibility, or internal AI policy
- **Saturation check**: Collection continued until major failure-type categories began to repeat rather than generate genuinely new incident types

**Classification Frameworks:**

Two established academic taxonomies were applied for incident classification:

1. **General AI incidents**: Amodei et al. (2016), Five Concrete Problems in AI Safety
2. **LLM-specific incidents**: Weidinger et al. (2022), Ethical and Social Risks of Harm from Language Models

**Evidence Tiering:**

All claims are labeled according to a 3-tier verification protocol:

- **Tier 1 (confirmed)**: Backed by regulatory or official institutional documentation (CFPB, FTC, SEC, NTSB, court materials)
- **Tier 2 (estimated)**: Company-reported materials, press releases, investor filings
- **Tier 3 (hypothesis)**: Investigative reporting, third-party research findings

---

## 2. The 71-Incident Inventory

### 2.1 General AI Incidents (10 cases)

| Year | Company / Case | Business Use | Dominant Failure Mechanism | Public Consequence | Evidence Type |
|------|----------------|-------------|---------------------------|-------------------|--------------|
| 2021 | Zillow Offers | Home-price forecasting and iBuying | Forecast error plus over-delegation to predictive models in a volatile market | Business wound down, ~$304M inventory write-down, ~25% staff cut | Investor release; SEC filing |
| 2018 | Amazon recruiting tool | Resume screening and hiring ranking | Historical training-data bias and proxy discrimination | Tool scrapped after penalizing resumes with signals associated with women | Reuters reporting |
| 2018 | Uber ATG | Developmental automated driving system | Weak safety culture, poor oversight, automation complacency, brittle real-world handling | Fatal crash in Tempe; NTSB identified operator distraction plus inadequate safety risk assessment | NTSB investigation |
| 2022 | Meta housing ads | Ad-delivery and audience expansion for housing ads | Algorithmic discrimination in ad delivery and lookalike targeting | DOJ settlement required Meta to stop using Special Ad Audience for housing ads | DOJ complaint and settlement |
| 2023 | Rite Aid | Facial recognition for retail surveillance | Poor safeguards, false positives, disproportionate harm | FTC five-year ban on facial-recognition surveillance use | FTC complaint and order |
| 2022–23 | iTutorGroup | Automated applicant screening | Explicit age-based automated rejection rules | EEOC settlement required payment and relief | EEOC suit and settlement |
| 2024 | Workday litigation | Outsourced hiring screening tools | Delegation of hiring functions to algorithmic systems | Court allowed key discrimination claims to proceed under agent theory | Court ruling |
| 2023 | SafeRent | Algorithm-based tenant screening | Potential disparate impact in rental screening | DOJ reinforced that FHA theories apply to algorithmic screening vendors | DOJ statement of interest |
| 2024 | RealPage | Rental pricing software | Algorithmic coordination and data-sharing across competitors | DOJ and states sued for alleged unlawful pricing coordination | DOJ complaint |
| 2024 | FloatMe | Cash-advance eligibility and underwriting | Deceptive claims about algorithmic decisioning plus discriminatory practices | FTC settlement: $3M for refunds, banned deceptive claims | FTC complaint and order |

### 2.2 LLM-Specific Incidents (10 cases)

| Year | Company / Case | Business Use | Dominant Failure Mechanism | Public Consequence | Evidence Type |
|------|----------------|-------------|---------------------------|-------------------|--------------|
| 2024 | Air Canada chatbot | Customer policy guidance chatbot | Fluent policy misstatement and customer reliance | Tribunal held Air Canada liable, awarded compensation | Legal practitioner summary |
| 2023 | Mata v. Avianca | Legal research and briefing | Hallucinated cases submitted as real | Court sanctions and $5,000 penalty | Court order |
| 2025 | AP Electric | Legal research and briefing | Fabricated quotations generated through AI | Court sanctioned counsel; warned real case names do not solve LLM reliability | Court order |
| 2023 | Samsung | Internal employee use of ChatGPT | Prompt-based leakage of confidential code and data | Samsung temporarily banned generative AI tools on company devices | TechCrunch reporting |
| 2023 | Google Bard | Conversational search product launch | Hallucinated factual error in product demo | Alphabet shares fell sharply; >$100B market value erased | Reuters reporting |
| 2024 | Google Gemini | Consumer conversational AI product | Overcompensation producing offensive generated outputs | Google paused image generation of people in Gemini | Google blog |
| 2023 | CNET / Red Ventures | AI-generated finance articles | Large-scale content errors, poor disclosure, plagiarism concerns | Corrections required, credibility suffered, partial rollout pause | Futurism reporting |
| 2025 | Chicago Sun-Times | AI-assisted lifestyle content | Hallucinated nonfiction disguised as real recommendations | Retractions, investigation, freelance creator termination | AP reporting |
| 2024 | DPD chatbot | Customer-service chatbot | Prompt-induced rogue behavior and weak brand voice control | DPD disabled the affected AI component | The Guardian reporting |
| 2026 | Elegant Enterprise-Wide Solutions | AI-generated job advertisements | Unlawful content generation in hiring communications | DOJ settlement for AI-generated ads excluding U.S. workers by citizenship | DOJ press release |

### 2.3 Additional Domain Representative Cases (8 domains)

Beyond the 20 incident cases above, in-depth representative cases were analyzed across 8 business domains to provide the foundation for framework construction:

| Domain | Representative Case | Key Lesson |
|--------|-------------------|------------|
| Strategy | Johor Corporation + Microsoft Copilot | AI is useful for information retrieval and synthesis; strategic judgment remains human |
| Operations | UPS ORION route optimization | Structured, repeated decisions are optimal candidates for controlled automation |
| Finance | Upstart AI lending | High-stakes value claims require governance and regulator-visible controls |
| Healthcare | FDA-governed AI medical devices | Lifecycle governance for safety, effectiveness, and transparency is required |
| Investment | SEC-framed robo-advisers | Disclosure requirements and suitability assessment for investor protection |
| Product | Productboard AI feedback synthesis | AI is valuable as synthesis and prioritization tool; final judgment is human |
| Marketing | Netflix personalization | AI automation is effective where strong feedback loops exist |
| Market Research | Qualtrics AI research synthesis | Assist-level autonomy is appropriate for interpretation-led domains |

### 2.4 Additional Domain-Specific Cases

Additional detailed cases across each of the 8 domains complete the 71-case inventory. These include cases from finance (credit underwriting, fraud detection, risk scoring), healthcare (diagnostic support, triage, imaging), hiring (resume screening, interview evaluation), operations (demand forecasting, inventory management, logistics), marketing (targeting, pricing, campaign optimization), and other sectors.

---

## 3. Failure Pattern Analysis

### 3.1 Application of Academic Taxonomies

#### Amodei et al. (2016) — General AI Incident Classification

Amodei et al. identified five concrete problems in AI safety. Applying this taxonomy to general AI incidents in the inventory:

| Failure Mode | Count | Representative Cases |
|-------------|-------|---------------------|
| **Reward hacking** | 5 | Zillow, iTutorGroup, RealPage, FloatMe, Amazon |
| **Side effects** | 5 | Amazon, Meta, Rite Aid, SafeRent, FloatMe |
| **Scalable oversight** | 2 | Uber, Workday |
| **Distributional shift** | 2 | Zillow, Rite Aid |
| **Safe exploration** | 1 | Uber |

**Key finding**: The majority of incidents involve reward hacking or side effects — failures of **objective specification**, not model capability. This aligns with Krakovna et al.'s (2020) finding that specification gaming is pervasive.

#### Weidinger et al. (2022) — LLM Incident Classification

Weidinger et al. identified six categories of LLM risk:

| Weidinger Category | Count | Representative Cases |
|-------------------|-------|---------------------|
| **W3 Misinformation** | 7 | Air Canada, Mata, AP Electric, Bard, CNET, Sun-Times, Elegant |
| **W5 Interaction harms** | 2 | Air Canada, DPD |
| **W1 Discrimination/toxicity** | 2 | Gemini, Elegant |
| **W2 Information hazards** | 1 | Samsung |
| **W6 Automation harms** | 1 | CNET |

**Key finding**: 70% of LLM incidents fall under misinformation (W3). This suggests that "fluent hallucination" — a fundamental LLM characteristic — is the single largest governance risk in business contexts.

### 3.2 Recurring Failure Patterns

#### General AI: Five Recurring Patterns

1. **Objective and optimization failures**: The problem is often not technical sophistication but attaching a model to the wrong business objective or scaling the objective too aggressively (Zillow, RealPage, Amazon).
2. **Historical bias and proxy discrimination**: Automating a decision process often automates the institution's history, not neutral merit (Amazon, iTutorGroup, Meta, Workday, SafeRent).
3. **Safety and real-world brittleness**: Even when perception or control systems are the visible issue, the deeper failure lies in safety culture, operator role design, and escalation structure (Uber).
4. **Accountability does not disappear with vendor involvement**: Outsourcing the system does not dissolve responsibility; delegation to software vendors can still create legal exposure (Workday, SafeRent, RealPage).
5. **Regulation moving from abstract concern to operational intervention**: FTC, DOJ, and EEOC are increasingly willing to intervene at the level of design choices, data use, system deployment, and vendor structure.

#### LLM-Specific: Six Recurring Patterns

1. **Fluent falsehood as business risk**: A wrong answer becomes more dangerous when it is confident, user-facing, embedded in a trusted interface, and treated as actionable guidance (Air Canada, Bard, Sun-Times).
2. **Human review failure inside the same interface**: "Human-in-the-loop" fails when the reviewer does not independently verify claims and treats output as a plausible draft (Mata, AP Electric).
3. **New data-boundary problem**: Useful conversational tools invite employees to paste sensitive material into external systems (Samsung).
4. **Brand voice as alignment problem**: When a conversational agent speaks for the company, reputational harm, liability risk, and customer confusion follow (DPD, Air Canada).
5. **Content-scale risk**: Generative systems can create many errors quickly with misleadingly polished prose (CNET, Sun-Times).
6. **LLM incidents often require withdrawal, not fine-tuning**: When system behavior becomes difficult to bound in production, firms resort to pausing features, shrinking scope, or re-routing workflows (Gemini, Samsung, DPD).

### 3.3 General AI vs. LLM: Governance Toolkits Must Differ

This distinction goes beyond technical classification — it implies that **the governance toolkit itself must be different**:

| Aspect | General AI Governance | LLM Governance |
|--------|----------------------|---------------|
| Core needs | Threshold setting, bias testing, objective review, human override design, vendor accountability | Verification outside the chat interface, prompt/data-boundary controls, brand and policy grounding |
| Risk source | Prediction, scoring, ranking, optimization, surveillance, autonomy | Language-mediated trust, verification failure, policy communication, generated content governance |
| Intervention point | Pre-deployment design and testing | Output verification and real-time control |

---

## 4. The 6-Dimensional Adaptive Delegation Framework

### 4.1 Core Principle

> AI authority should be assigned by **category combination**, not by domain label alone.

This means the question "Can AI be used in finance?" is ill-formed. The correct question is: "For this specific financial decision, at this risk level, under these scenario conditions, with this evidence strength, what level of authority can be granted to AI?"

This approach draws theoretical grounding from established research:

- **Agrawal, Gans, and Goldfarb (2018)**: AI understood as a prediction technology, but prediction alone does not produce action — judgment is separately required. Theoretical basis for the "decision structure" and "AI role" dimensions.
- **Jarrahi (2018)**: Human-AI complementarity is stronger than pure substitution in complex organizations. Justification for defaulting to "assist" and "recommend" over "automate."
- **Dietvorst, Simmons, and Massey (2015)**: Algorithm aversion — people avoid algorithms after observing errors, even when algorithms remain more reliable. Justification for the behavioral trust dimension.
- **NIST (2023) AI Risk Management Framework**: Trustworthiness, risk management, accountability, transparency, and human oversight as core governance components. Direct basis for the "governance readiness" dimension.
- **OECD (2019) AI Principles**: International policy principles supporting accountability and human oversight dimensions.

### 4.2 The Six Dimensions

The framework formula:

```
preferred_AI_role = domain × decision_structure × risk_level × scenario_condition × evidence_strength × governance_readiness
```

#### Dimension 1: Domain

The business area to which the decision belongs. Each domain has distinct regulatory environments, stakeholder structures, and failure impact ranges.

| Domain | Default Structure | Default Risk | Default Mode | Rationale |
|--------|------------------|-------------|-------------|-----------|
| Strategy | Unstructured | Med–High | ASSIST | Context-heavy, judgment-intensive |
| Operations | Structured | Low–Med | AUTOMATE WITH GUARDRAILS | Repeated, measurable |
| Finance | Semi-structured | High | ASSIST / tightly governed RECOMMEND | Compliance, audit burden |
| Healthcare | Semi-structured | Very High | ASSIST / tightly governed RECOMMEND | Safety-critical |
| Investment | Semi-structured | High | ASSIST / tightly governed RECOMMEND | Investor protection |
| Product | Semi-structured | Medium | ASSIST / RECOMMEND | Synthesis-heavy tradeoffs |
| Marketing | Structured–Semi | Medium | RECOMMEND | Strong feedback loops |
| Market Research | Unstructured–Semi | Medium | ASSIST | Interpretation-led |

Academic basis: Brynjolfsson, Hitt, and Kim (2011) showed that data-driven decision-making is associated with stronger firm performance, but the effect depends on organizational practices and data quality. This supports the need for domain-specific defaults.

#### Dimension 2: Decision Structure

The degree of structuredness determines the appropriate AI role.

- **Unstructured**: Ambiguous, no precedent, heavily judgment-dependent → default **ASSIST**
- **Semi-structured**: Partially structured with judgment-requiring components → **ASSIST** or **RECOMMEND**
- **Structured**: Repeated, measurable, clear rules → **RECOMMEND** or **AUTOMATE WITH GUARDRAILS**

#### Dimension 3: Risk Level

Evaluates the potential harm range if the decision fails.

- **High risk**: Fairness, compliance, safety (finance, healthcare, hiring) → default **ASSIST**
- **Medium risk**: Revenue, customer relationships → **ASSIST** or **RECOMMEND**
- **Low risk**: Operational, internal impact → **RECOMMEND** or **AUTOMATE WITH GUARDRAILS**

Academic basis: The NIST AI Risk Management Framework (2023) specifies that governance requirements must be differentiated by risk level. This framework directly connects that principle to decision authority levels.

#### Dimension 4: Scenario Condition

The same decision warrants different AI roles depending on conditions.

- **Baseline**: Normal, predictable environment → framework score applies as-is
- **Stress**: Market volatility, operational pressure → assist value increases but automation tolerance decreases
- **Edge-case**: No precedent or extremely rare situation → default **ASSIST**

Academic basis: Amodei et al.'s (2016) "distributional shift" problem explains how AI fails when deployment conditions differ from training conditions. The Zillow Offers case is a textbook example of a forecasting model developed under normal market conditions failing in a volatile market (stress/edge-case).

#### Dimension 5: Evidence Strength

Evaluates the quality and quantity of evidence supporting the AI system's reliability.

- **Strong**: Regulator-verified, audited, peer-reviewed evidence → framework score holds
- **Moderate**: Documented but lacking independent verification → score holds or one-level reduction
- **Weak**: Only reported materials or unverifiable → one-level autonomy reduction

Academic basis: This dimension connects directly to the interpretability debate in AI safety research. According to mechanistic interpretability research by Elhage et al. (2022) and Conmy et al. (2023), when a model's internal reasoning cannot be inspected, evidence strength cannot be objectively assessed. The framework forces a one-level authority reduction in this case.

Furthermore, Vaccaro, Almaatouq, and Malone's (2024) meta-analysis showed that human-AI combinations are more useful in creative tasks than decision tasks. This provides justification for raising evidence strength requirements in high-stakes decision environments.

#### Dimension 6: Governance Readiness

Evaluates whether the organization can responsibly manage the proposed autonomy level.

- **Strong**: Formal governance, traceability, fairness review in place → framework score holds
- **Adequate**: Basic review procedures exist → framework score holds
- **Weak**: Governance absent or nominal → one-level autonomy reduction

Academic basis: Schuett et al. (2023) presented institutional structures for responsible AI deployment. This framework serves as a bridge between technical alignment confidence and operational delegation decisions. De Stefano, Kellogg, Menietti, and Vendraminelli (2022) also showed that worker trust, visibility, and intervention patterns affect the actual performance of algorithmic systems.

### 4.3 Scoring Model

Each dimension is scored 1–3, with the total determining the AI role:

| Dimension | 1 point | 2 points | 3 points |
|-----------|---------|----------|----------|
| Decision Structure | Unstructured | Semi-structured | Structured |
| Risk Level | High | Medium | Low |
| Scenario Stability | Edge-case | Stress | Baseline |
| Evidence Strength | Weak | Moderate | Strong |
| Governance Readiness | Weak | Adequate | Strong |

**Score bands:**

| Score Range | Recommended AI Role | Description |
|-------------|-------------------|-------------|
| 5–8 | **ASSIST** | Uncertainty, risk, or weak evidence dominates |
| 9–11 | **ASSIST or RECOMMEND** | Partial structure, moderate confidence |
| 12–13 | **RECOMMEND** | Structured, stable, lower-risk, evidence-backed |
| 14–15 | **RECOMMEND or AUTOMATE WITH GUARDRAILS** | Optimal conditions only |

### 4.4 Override Rules

Three safety rules that apply regardless of score:

1. **Override 1**: High risk + weak governance → **cap at ASSIST**
2. **Override 2**: Edge-case scenario → **cap at ASSIST**
3. **Override 3**: Weak evidence in consequential decision → **reduce one autonomy level**

Academic basis:
- Override 1 is an operational answer to Amodei et al.'s (2016) "scalable oversight" problem. Granting high authority with insufficient oversight produces the kind of disasters seen in Uber ATG and Workday.
- Override 2 is the operational application of the distributional shift problem. The Zillow case demonstrates this clearly.
- Override 3 is grounded in trust calibration research by Lee and See (2004) and Bansal et al. (2021). Appropriate reliance is the correspondence between trust and actual trustworthiness — when evidence is weak, there is no basis for high trust.

### 4.5 Sequential Decision Tree

A 6-step procedure for practical application:

```
1. Identify the Domain
   → Operations / product / strategy / high-stakes?

2. Classify Decision Structure
   → If unstructured → default ASSIST

3. Classify Risk Level
   → If high-risk → default ASSIST or tightly governed RECOMMEND

4. Classify Scenario Condition
   → If edge-case → default ASSIST

5. Check Evidence Strength
   → If weak → reduce autonomy one level

6. Check Governance Readiness
   → If not ready → reduce autonomy one level
```

### 4.6 Three AI Role Modes

| Mode | Description | Human Role | Suitable Environment |
|------|------------|-----------|---------------------|
| **ASSIST** | AI provides analysis, synthesis, drafts. Human retains final authority | Decision-maker | Complex, high-risk decisions. Strategy, finance, healthcare |
| **RECOMMEND** | AI provides structured recommendations. Human reviews before action | Reviewer / approver | Moderate structure. Evidence-based but requiring human judgment |
| **AUTOMATE WITH GUARDRAILS** | AI acts directly within predefined boundaries. Escalates to human on anomaly | Supervisor / exception handler | Highly structured, data-rich, low–medium harm potential, easy to monitor |

Academic basis: This 3-level model operationalizes the scalable oversight concept from Amodei et al. (2016). In response to Bowman et al.'s (2022) question — "How do we maintain human oversight as AI systems become more capable?" — the framework answers by **constraining autonomy to what can be meaningfully overseen**.

---

## 5. Framework Validation: Retrospective Application Against the Incident Inventory

### 5.1 General AI: 10/10 Detection (100%)

If the framework had been applied before deployment, all 10 general AI incidents would have received a **lower authority recommendation** than the level at which the system was actually operated.

| Case | Actual Level | Framework Recommendation | Primary Trigger |
|------|-------------|------------------------|----------------|
| Zillow | AUTOMATE | ASSIST or capped RECOMMEND | High risk + stress/edge-case conditions |
| Amazon hiring | AUTOMATE | ASSIST | High risk + weak governance (Override 1) |
| Uber ATG | AUTOMATE | ASSIST (multiple overrides) | High risk + weak governance + edge-case |
| Meta housing ads | AUTOMATE | ASSIST | High risk + weak evidence |
| Rite Aid | AUTOMATE | ASSIST (multiple overrides) | High risk + weak evidence + weak governance |
| iTutorGroup | AUTOMATE | ASSIST / tightly governed RECOMMEND | High risk (Override 1) |
| Workday | AUTOMATE | ASSIST | High risk + weak governance (Override 1) |
| SafeRent | AUTOMATE | ASSIST | High risk + weak evidence (Override 3) |
| RealPage | AUTOMATE | ASSIST | High risk + weak governance (Override 1) |
| FloatMe | AUTOMATE | ASSIST | Multiple override triggers |

### 5.2 LLM-Specific: 4/10 Full, 5/10 Partial, 1/10 Not Captured

| Detection Level | Count | Cases | Limitation |
|----------------|-------|-------|-----------|
| Full prevention | 4 | Air Canada, CNET, Elegant Enterprise, (some enterprise deployments) | Organizational delegation decisions |
| Partial flagging | 5 | Mata, AP Electric, Bard, Gemini, DPD, Sun-Times | Individual professional tool use or product launch risk management |
| Not captured | 1 | Samsung | Information security risk outside framework scope |

**Key lesson**: The framework is strong against **organizational delegation failures** but requires supplementary governance for **individual-level tool use** and **information security risks**.

### 5.3 Overall Detection Rate

Across all 20 incidents:
- **12/20 (60%) full prevention**: Framework would have recommended a lower authority level before deployment
- **7/20 (35%) partial flagging**: Framework identifies risk but does not fully prevent
- **1/20 (5%) not captured**: Risk falls outside framework scope

---

## 6. Reasoning Verification Framework (Extension)

One key finding from the 71-incident analysis is that the delegation framework alone does not sufficiently address LLM **output quality** problems. Accordingly, a reasoning verification framework integrating four complementary methods was additionally developed.

### 6.1 Reasoning Failure Taxonomy: 6 Categories × 25 Types

| Category | Types | Representative Types | Risk Level |
|----------|-------|---------------------|-----------|
| **Source Failures** | 5 | Fabricated sources, misrepresented sources, inadequate source quality, outdated sources, selection bias | Critical–High |
| **Inferential Failures** | 8 | Non sequitur, false causation, overgeneralization, missing counterfactual, anchoring on irrelevant precedent | High |
| **Normative Failures** | 4 | Legal norm violation, professional standard violation, ethical boundary crossing, cultural insensitivity | High–Critical |
| **Calibration Failures** | 4 | Overconfidence, false precision, certainty laundering, uniform confidence | High |
| **Structural Failures** | 6 | Circular reasoning, scope mismatch, temporal confusion, stakeholder blindness, survivorship bias | Medium–High |
| **Sycophantic Failures** | 4 | Confirmation bias amplification, question-shaped answers, progressive sycophancy, audience-optimized reasoning | High |

### 6.2 Four Verification Methods

1. **Source Quality Assessment**: Evaluates each claim's source against a 5-level quality hierarchy — from Level 5 (primary authoritative) to Level 1 (unreliable/non-verifiable).
2. **Inferential Validity Assessment**: Applies type-specific checklists for deductive, inductive, abductive, and analogical reasoning, plus a reverse test ("What would have to be true for this to be wrong?").
3. **Normative Assessment**: Checks compliance against legal, professional, ethical, and social standards.
4. **Confidence Calibration Assessment**: Evaluates alignment between expressed confidence level and evidence strength.

### 6.3 Integration with the Delegation Framework

Reasoning verification results are integrated through two mechanisms:

**Mechanism 1: Extended Evidence Strength (weakest-link principle)**
- Component A: System-level evidence (existing framework evidence strength)
- Component B: Output quality (pass/fail across all 4 verification checks)
- Combined score = min(A, B)

**Mechanism 2: Verification Gate**

| Status | Condition | Effect |
|--------|-----------|--------|
| Not verified | No verification applied | Default to **ASSIST** regardless of score |
| Verified with issues | Moderate severity issues | Framework score applies with one-level reduction |
| Verified and passed | All checks passed or low severity only | Framework score applies normally |

---

## 7. Cross-Domain Analysis Results

### 7.1 Eight-Domain Comparison

| Domain | Primary AI Role | Main Value | Main Risk | Recommended Autonomy | Evidence Strength |
|--------|----------------|-----------|-----------|---------------------|------------------|
| Strategy | Synthesis, forecasting, simulation | Broader signal processing | False confidence, weak transferability | ASSIST | Moderate |
| Operations | Optimization, prediction, control | Measurable efficiency | Brittle models, local optimization | AUTOMATE WITH GUARDRAILS | Moderate |
| Finance | Classification, anomaly detection, recommendation | Faster, more consistent risk evaluation | Fairness, compliance, model risk | ASSIST or tightly governed RECOMMEND | Strong |
| Healthcare | Prediction, classification, clinical decision support | Earlier detection, workflow efficiency | Patient safety, bias, liability | ASSIST or tightly governed RECOMMEND | Strong |
| Investment | Recommendation, optimization, pattern detection | Scalable advisory support | Conflicts of interest, investor harm | ASSIST or tightly governed RECOMMEND | Strong |
| Product | Synthesis, clustering, experimentation support | Faster learning loops | Proxy metrics, user misread | ASSIST or RECOMMEND | Moderate |
| Marketing | Prediction, recommendation, experimentation | Conversion efficiency, retention | Privacy, bias, short-term optimization | RECOMMEND or AUTOMATE WITH GUARDRAILS | Moderate |
| Market Research | Clustering, synthesis, summarization | Faster analysis of large datasets | Hallucinated insights, false patterns | ASSIST | Weak–Moderate |

### 7.2 Domain Fitness Classification

**Best candidates for automation:**
- Operations, Marketing — repeated, measurable decisions with clear feedback loops

**High-value but high-risk:**
- Finance, Healthcare, Investment — governance-first domains where evidence quality, compliance exposure, and explainability are critical

**Best augmentation (assist) domains:**
- Strategy, Product, Market Research — AI as synthesis and insight-support tool, not autonomous decision engine

---

## 8. Connection to AI Safety and Alignment Research

### 8.1 Delegation Calibration Is an Alignment Problem

Traditional AI alignment research focuses on whether models behave as intended (value alignment, reward specification). This research addresses a complementary question: **even if a model is well-aligned, should it be granted autonomous authority in a given context?**

The 6-dimensional framework provides a **governance layer that translates technical alignment confidence into operational delegation decisions**.

### 8.2 The Role of Interpretability

The "evidence strength" dimension directly depends on model interpretability:

- **High interpretability** → evidence strength is verifiable → higher AI authority is justified
- **Low interpretability** → evidence strength is opaque → human override required regardless of performance

This creates a concrete demand signal for mechanistic interpretability research (Elhage et al., 2022; Conmy et al., 2023).

### 8.3 From Incidents to Alignment Failure Modes

The 71-incident inventory maps to the following alignment failure modes:

- **Specification gaming** — AI optimized for proxy metrics rather than intended objectives (Krakovna et al., 2020)
- **Distributional shift** — model deployed outside training conditions
- **Oversight failure** — human-in-the-loop was nominal, not effective
- **Fluent hallucination** — confidently wrong generated outputs

---

## 9. Limitations and Open Research Questions

### 9.1 Framework Scope Limitations

1. **Individual-level tool use**: The framework evaluates organizational delegation policy, not individual professional AI tool use patterns (the Mata v. Avianca pattern).
2. **Information security risks**: Data leakage through prompts (the Samsung pattern) is an information security problem, not a delegation calibration failure, and falls outside framework scope.
3. **Static evaluation**: The current framework evaluates authority levels statically. How authority levels should adjust in real-time as model confidence and environmental conditions change remains unresolved.

### 9.2 Open Research Questions

1. **Quantifying evidence strength**: Can interpretability methods (feature attribution, probing, circuit analysis) provide objective evidence-strength scores, replacing subjective expert judgment?
2. **Dynamic delegation**: How should authority levels adjust in real-time as model confidence and environmental conditions change?
3. **Cross-domain transfer**: Do failure patterns in one domain (e.g., lending) predict governance needs in another (e.g., hiring)? The incident data suggests partial transferability but needs rigorous validation.
4. **Interpretability-authority tradeoff**: Is there a formal relationship between model interpretability depth and maximum safe authority level? Can this be expressed as a constraint?
5. **Scalable oversight bottleneck**: The framework assumes human oversight is available at the "assist" and "recommend" levels, but this assumption may not hold at scale. How should the framework account for oversight capacity constraints?

---

## 10. Core Conclusions

### 10.1 Central Argument

> **AI authority must be adaptive — not fixed.**

The most important organizational decision is not whether to adopt AI but **how much authority to delegate to AI under specific conditions**. The second most important decision is **when to reduce that authority**.

### 10.2 Key Lessons from the 71-Incident Analysis

1. **Most AI failures originate from delegation calibration failure, not technical capability gaps.** The systems did not lack sophistication — they were granted more authority than conditions warranted.

2. **The same AI capability can create value or cause failure depending on context design.** Prediction, ranking, and optimization are not inherently beneficial. Their outcomes depend on training data, objective choice, workflow integration, and the ability of humans to intervene appropriately.

3. **High-stakes decisions should default to assist or tightly governed recommend.** Predictive capability alone does not justify high-stakes delegation. Human review, accountability, and evidence quality are threshold conditions.

4. **General AI and LLM governance toolkits must differ fundamentally.** Traditional AI's objective specification and bias testing versus LLM's output verification and data-boundary control require separate governance architectures.

5. **The framework's override rules are the most powerful protective mechanism.** Mandatory downward adjustments for high risk + weak governance, edge-case scenarios, and weak evidence would have prevented the majority of incidents in advance.

---

## References

### Academic Literature and Theoretical Foundations

- Agrawal, A., Gans, J., and Goldfarb, A. (2018). Prediction, Judgment and Complexity: A Theory of Decision Making and Artificial Intelligence. *NBER Working Paper 24243*.
- Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J., and Mané, D. (2016). Concrete Problems in AI Safety. *arXiv:1606.06565*.
- Bansal, G., Wu, T., Zhou, J., Fok, R., Nushi, B., Kamar, E., Ribeiro, M. T., and Weld, D. S. (2021). Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance. *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems*.
- Bowman, S. R., Hyun, J., Perez, E., Chen, A., Pettit, C., Heiner, S., Lukosuite, K., Askell, A., Jones, A., Chen, A., et al. (2022). Measuring Progress on Scalable Oversight for Large Language Models. *arXiv:2211.03540*.
- Brynjolfsson, E., Hitt, L. M., and Kim, H. H. (2011). Strength in Numbers: How Does Data-Driven Decisionmaking Affect Firm Performance? *ICIS 2011 Proceedings*.
- Brynjolfsson, E., Li, D., and Raymond, L. R. (2023). Generative AI at Work. *NBER Working Paper 31161*.
- Conmy, A., Mavor-Parker, A. N., Lynch, A., Heimersheim, S., and Garriga-Alonso, A. (2023). Towards Automated Circuit Discovery for Mechanistic Interpretability. *NeurIPS 2023*.
- De Stefano, V., Kellogg, K. C., Menietti, M., and Vendraminelli, L. (2022). The Tapestry of Work: A Comprehensive Framework for Understanding the Experience of Work in the Age of AI. *SSRN Working Paper*.
- Dietvorst, B. J., Simmons, J. P., and Massey, C. (2015). Algorithm Aversion: People Erroneously Avoid Algorithms After Seeing Them Err. *Journal of Experimental Psychology: General*, 144(1), 114–126.
- Elhage, N., Nanda, N., Olsson, C., Henighan, T., Joseph, N., Mann, B., Askell, A., Bai, Y., Chen, A., Conerly, T., et al. (2022). A Mathematical Framework for Transformer Circuits. *Transformer Circuits Thread*.
- Jarrahi, M. H. (2018). Artificial Intelligence and the Future of Work: Human-AI Symbiosis in Organizational Decision Making. *Business Horizons*, 61(4), 577–586.
- Krakovna, V., Uesato, J., Mikulik, V., Rahtz, M., Everitt, T., Kumar, R., Kenton, Z., Leike, J., and Legg, S. (2020). Specification Gaming: The Flip Side of AI Ingenuity. *DeepMind Blog*.
- Lee, J. D., and See, K. A. (2004). Trust in Automation: Designing for Appropriate Reliance. *Human Factors*, 46(1), 50–80.
- Li, D., Raymond, L. R., and Bergman, P. (2020). Hiring as Exploration. *NBER Working Paper 27736*.
- Schuett, J., Dreksler, N., Anderljung, M., McCaffary, D., Heim, L., Bluemke, E., and Garfinkel, B. (2023). Towards Best Practices in AGI Safety and Governance. *arXiv:2305.07153*.
- Vaccaro, M., Almaatouq, A., and Malone, T. W. (2024). When Combinations of Humans and AI Are Useful: A Systematic Review and Meta-Analysis. *Nature Human Behaviour*.
- Weidinger, L., Mellor, J., Rauh, M., Griffin, C., Uesato, J., Huang, P.-S., Cheng, M., Glaese, M., Balle, B., Kasirzadeh, A., et al. (2022). Ethical and Social Risks of Harm from Language Models. *arXiv:2112.04359*.

### Governance Frameworks and Regulatory Documents

- NIST. (2023). AI Risk Management Framework 1.0.
- OECD. (2019). OECD AI Principles.
- U.S. Equal Employment Opportunity Commission. (2023). Assessing Adverse Impact in Software, Algorithms, and Artificial Intelligence Used in Employment Selection Procedures Under Title VII.
- Consumer Financial Protection Bureau. (2020–2024). Upstart no-action letter materials and termination order.
- U.S. Food and Drug Administration. (2025). Artificial Intelligence in Software as a Medical Device.
- U.S. Securities and Exchange Commission. (2017). Investor Bulletin: Robo-Advisers.

### Incident Case Primary Sources

- Zillow investor release and SEC filing (2021)
- NTSB Tempe investigation — Uber ATG (2018)
- DOJ complaint and settlement — Meta housing ads (2022)
- FTC complaint and order — Rite Aid (2023)
- EEOC suit and settlement — iTutorGroup (2022–2023)
- Court ruling — Mobley v. Workday (2024)
- DOJ statement of interest — SafeRent (2023)
- DOJ complaint — RealPage (2024)
- FTC complaint and order — FloatMe (2024)
- Tribunal decision — Air Canada chatbot (2024)
- Court order — Mata v. Avianca (2023)
- Court order — AP Electric sanctions (2025)
- Samsung internal ban reporting — TechCrunch (2023)
- Google Bard demo error — Reuters (2023)
- Google Gemini image generation pause — Google Blog (2024)
- CNET AI content rollout — Futurism (2023)
- Fake summer reading list — AP (2025)
- DPD chatbot incident — The Guardian (2024)
- DOJ settlement — Elegant Enterprise-Wide Solutions (2026)
