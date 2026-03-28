# Incident Inventory: Alignment Failure Mode Mapping

status: draft
date: 2026-03-27
purpose: Reclassify the incident inventory using alignment failure mode taxonomies from Amodei et al. (2016) and Weidinger et al. (2022), then map each incident to the 6-dimensional framework.

## Method

Each incident from the inventory is classified along two axes:

1. **Alignment failure mode** — using Amodei et al. (2016) for general AI incidents and Weidinger et al. (2022) for LLM-specific incidents
2. **Framework dimension failure** — which of the 5 scored dimensions would have flagged this failure if the framework had been applied before deployment

The question being tested: if the framework had been applied to these deployment contexts, which incidents would it have prevented by recommending a lower authority level?

## Taxonomy Definitions

### Amodei et al. (2016) — Five Concrete Problems

- **Side effects**: Agent achieves its objective but damages the environment in unintended ways
- **Reward hacking**: Agent finds unintended ways to maximize its reward that do not match designer intent
- **Scalable oversight**: Human evaluators cannot effectively monitor agent behavior at scale
- **Safe exploration**: Agent takes catastrophic actions in the course of learning
- **Distributional shift**: Agent behaves poorly when deployment conditions differ from training

### Weidinger et al. (2022) — Six LLM Risk Categories

- **W1 Discrimination and toxicity**: Biased, exclusionary, or harmful content
- **W2 Information hazards**: Privacy leakage, confidential data exposure
- **W3 Misinformation**: Fluent but false content generation
- **W4 Malicious uses**: Social engineering, fraud enablement
- **W5 Interaction harms**: Over-trust, anthropomorphization, manipulation
- **W6 Automation harms**: Job displacement, power concentration

## Part I. General AI Incidents — Alignment Mapping

| Company | Amodei failure mode | Framework dimensions that would have flagged | Would framework have prevented? |
|---|---|---|---|
| Zillow Offers | **Reward hacking** + **distributional shift**. The forecasting model optimized for a metric (home price prediction) that diverged from the business objective (profitable iBuying) when market conditions shifted. | Risk level (high — financial exposure), scenario condition (volatile market = stress/edge-case), evidence strength (forecast models unvalidated for volatile conditions). Score would produce ASSIST or capped RECOMMEND. Zillow operated at AUTOMATE. | **Yes.** The framework would have flagged the mismatch between the authority level exercised (automate) and the appropriate level given high risk + stress conditions. |
| Amazon recruiting | **Side effects** + **reward hacking**. The model optimized for patterns in historical hiring data, which encoded gender bias as a proxy signal. The side effect was systematic discrimination. | Risk level (high — fairness/compliance), evidence strength (weak — historical bias unaudited), governance readiness (weak — no fairness review process). Override rule triggered: high-risk + weak governance → cap at ASSIST. | **Yes.** The override rule alone would have capped authority at ASSIST, preventing automated screening. |
| Uber ATG | **Safe exploration** + **scalable oversight**. A developmental autonomous system was deployed with inadequate safety culture and oversight, and it encountered conditions outside its design envelope. | Risk level (high — safety), governance readiness (weak — NTSB found inadequate safety risk assessment), scenario condition (edge-case — atypical pedestrian crossing). Multiple override triggers. | **Yes.** The framework would have produced ASSIST with multiple override flags. The fundamental failure was deploying at AUTOMATE authority in a high-risk, governance-weak context. |
| Meta housing ads | **Side effects**. The ad delivery algorithm optimized for engagement/conversion, producing discriminatory audience targeting as an unintended side effect. | Risk level (high — fairness, housing access), evidence strength (weak — disparate impact unaudited until DOJ intervention). | **Yes.** High risk + weak evidence → framework would flag for ASSIST. |
| Rite Aid | **Side effects** + **distributional shift**. Facial recognition deployed with poor accuracy across demographics, producing false positives disproportionately affecting certain groups. | Risk level (high — privacy, disproportionate harm), evidence strength (weak — accuracy unvalidated across subgroups), governance readiness (weak — poor safeguards per FTC). | **Yes.** Multiple override triggers would cap at ASSIST. |
| iTutorGroup | **Reward hacking**. Explicit age-based rejection rules were built into the screening system — a direct case of optimizing for a proxy (age) that violates the intended objective (merit-based hiring). | Risk level (high — employment discrimination), decision structure (structured — automated rejection rules). Override rule: high risk. | **Yes.** Even with structured decisions, high risk defaults to ASSIST or tightly governed RECOMMEND. Automated rejection would not be permitted. |
| Workday | **Scalable oversight**. Hiring decisions were delegated to an external vendor's algorithmic system, creating an oversight gap where neither the employer nor the vendor took full accountability. | Risk level (high — employment), governance readiness (weak — outsourced accountability). | **Yes.** High-risk + weak governance override → ASSIST. |
| SafeRent | **Side effects**. Tenant screening algorithm produced disparate impact on protected groups as a side effect of optimizing for risk scoring. | Risk level (high — housing access), evidence strength (weak — disparate impact unaudited). | **Yes.** High risk + weak evidence triggers override. |
| RealPage | **Reward hacking**. Pricing algorithm coordinated rents across competitors, optimizing for revenue in a way that constituted market manipulation — maximizing the specified metric (landlord revenue) at the expense of the intended market function (competitive pricing). | Risk level (high — market manipulation), governance readiness (weak — no competitive impact assessment). | **Yes.** High-risk + weak governance → ASSIST. |
| FloatMe | **Reward hacking** + **side effects**. Deceptive claims about algorithmic underwriting combined with discriminatory outcomes. The system optimized for conversion metrics while producing unfair lending practices. | Risk level (high — lending discrimination), evidence strength (weak — deceptive claims). | **Yes.** Override rules would trigger. |

### Summary — General AI

| Amodei failure mode | Count | Incidents |
|---|---|---|
| Reward hacking | 5 | Zillow, iTutorGroup, RealPage, FloatMe, Amazon |
| Side effects | 5 | Amazon, Meta, Rite Aid, SafeRent, FloatMe |
| Scalable oversight | 2 | Uber, Workday |
| Safe exploration | 1 | Uber |
| Distributional shift | 2 | Zillow, Rite Aid |

Most incidents involve reward hacking or side effects — failures in objective specification rather than in model capability. This aligns with Krakovna et al.'s finding that specification gaming is pervasive. The framework addresses these primarily through the risk level dimension and override rules.

**Framework detection rate: 10/10.** Every general AI incident in the inventory would have produced a lower authority recommendation than the level at which the system was actually deployed. The most common pattern is the override rule triggering on high-risk + weak governance or high-risk + weak evidence.

## Part II. LLM-Specific Incidents — Alignment Mapping

| Company | Weidinger category | Amodei mode (if applicable) | Framework dimensions that would have flagged | Would framework have prevented? |
|---|---|---|---|---|
| Air Canada chatbot | **W3 Misinformation** + **W5 Interaction harms**. Fluent policy misstatement led to customer reliance on incorrect information. | Scalable oversight — chatbot operated without effective human review of policy guidance. | Evidence strength (weak — chatbot outputs unverified), governance readiness (weak — no review process for chatbot statements). | **Partially.** Framework would recommend ASSIST for customer-facing policy guidance, but the chatbot was deployed at AUTOMATE. The framework does not specifically address real-time conversational interaction risks. |
| Mata v. Avianca | **W3 Misinformation**. Hallucinated legal cases submitted as real. | Scalable oversight — attorney did not verify AI outputs. | Evidence strength (weak — no verification), decision structure (semi-structured — legal research requires judgment). | **Partially.** Framework would flag weak evidence, but this is an individual professional tool use, not an organizational deployment decision. |
| AP Electric | **W3 Misinformation**. Fabricated quotations in legal briefs. | Scalable oversight. | Same as Mata v. Avianca. | **Partially.** Same limitation. |
| Samsung | **W2 Information hazards**. Confidential code and data leaked through prompts. | Not a decision-delegation failure but an information security failure. | Not directly captured by the framework. This is an information security risk, not a delegation calibration failure. | **No.** The framework does not address data leakage through AI tool use. This is a gap identified in the Weidinger analysis. |
| Google Bard | **W3 Misinformation**. Factual error in promotional material. | Scalable oversight — high-profile demo without adequate fact-checking. | Evidence strength (weak — demo output unverified). | **Partially.** Framework would flag weak evidence but does not address product launch risk management. |
| Google Gemini | **W1 Discrimination and toxicity**. Offensive image generation from overcompensation in content policies. | Side effects — the content safety system produced the opposite of its intended effect. | Risk level (medium-high — reputational, content harm), governance readiness (partial — content policy existed but produced unintended results). | **Partially.** Framework would flag risk but does not specifically model content generation safety. |
| CNET | **W3 Misinformation** + **W6 Automation harms**. AI-generated articles contained errors and plagiarism, published at scale without adequate disclosure. | Scalable oversight — editorial review could not keep pace with AI generation volume. | Evidence strength (weak — AI content unreviewed), governance readiness (weak — no disclosure, no editorial review process). | **Yes.** Framework would recommend ASSIST for content production, not AUTOMATE. Weak evidence + weak governance → override. |
| Chicago Sun-Times | **W3 Misinformation**. Hallucinated book recommendations published as real. | Scalable oversight. | Evidence strength (weak — hallucinated content). | **Partially.** Same limitation as individual tool use cases. |
| DPD chatbot | **W5 Interaction harms**. Prompt-induced rogue behavior in customer-facing chatbot. | Safe exploration — chatbot had no behavioral boundaries for adversarial prompting. | Governance readiness (weak — no adversarial testing), scenario condition (edge-case — adversarial user behavior). | **Partially.** Framework would flag edge-case + weak governance, but does not specifically model adversarial interaction risks. |
| Elegant Enterprise | **W1 Discrimination and toxicity**. AI-generated job ads that excluded workers based on citizenship. | Side effects — the AI optimized for ad content generation without checking for discriminatory language. | Risk level (high — employment discrimination), evidence strength (weak — AI output unreviewed). | **Yes.** High risk + weak evidence → override rules trigger, recommending ASSIST. |

### Summary — LLM Incidents

| Weidinger category | Count | Incidents |
|---|---|---|
| W3 Misinformation | 7 | Air Canada, Mata, AP Electric, Google Bard, CNET, Sun-Times, Elegant Enterprise |
| W5 Interaction harms | 2 | Air Canada, DPD |
| W2 Information hazards | 1 | Samsung |
| W1 Discrimination/toxicity | 2 | Google Gemini, Elegant Enterprise |
| W6 Automation harms | 1 | CNET |

**Framework detection rate: 4/10 full, 5/10 partial, 1/10 not captured.** The framework is less effective for LLM incidents because many involve individual professional tool use (Mata, AP Electric, Sun-Times) rather than organizational delegation decisions, and because information security risks (Samsung) fall outside the framework's scope.

## Cross-Cutting Findings

### 1. The framework is strongest against organizational delegation failures

All 10 general AI incidents and 2 LLM incidents (CNET, Elegant Enterprise) involve organizational decisions to deploy AI at an authority level higher than the framework would recommend. The override rules — particularly high-risk + weak governance and high-risk + weak evidence — catch the majority of cases.

### 2. The framework does not address individual professional tool use

Five LLM incidents (Mata, AP Electric, Samsung, Google Bard, Sun-Times) involve individuals using AI tools in their professional work. The framework evaluates organizational delegation policy, not individual usage patterns. This is a scope boundary, not a flaw — but it is worth acknowledging.

### 3. Specification gaming (reward hacking) is the most common general AI failure

5 of 10 general AI incidents involve reward hacking. The framework addresses this indirectly through risk level and override rules, but does not explicitly assess objective specification quality. Adding a pre-delegation checklist based on Amodei et al.'s five problems would strengthen this.

### 4. Misinformation dominates LLM failures

7 of 10 LLM incidents involve misinformation (W3). The framework's evidence strength dimension captures part of this risk, but it does not distinguish between "evidence about the system's reliability" and "evidence that a specific output is factually correct." For LLM deployments, output verification is a distinct requirement that the framework does not model.

### 5. The framework would have prevented 12 of 20 incidents outright

If applied before deployment, the framework would have recommended a lower authority level in 12 cases, partially flagged risk in 7 cases, and missed 1 case entirely (Samsung data leakage). This suggests the framework captures the majority of deployment-phase governance failures but needs supplementation for LLM-specific and individual-use-level risks.
