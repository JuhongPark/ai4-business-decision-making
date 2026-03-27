# The Research-Practice Temporal Gap in AI Governance

## Status: research_complete
## Phase: 21 — Adaptive Governance Extension
## Date: 2026-03-10

---

## 1. Problem Statement

AI governance research and AI capability development operate on fundamentally different timescales.

```
Research cycle:     literature → framework → case analysis → validation → publication  (12-24 months)
AI capability:      GPT-4 → Claude 3 → GPT-4o → o1 → Claude 4 → Opus 4.6 → ...     (3-6 month intervals)
Enterprise adoption: PoC → pilot → production → pivot                                 (weeks to months)
Regulatory response: proposal → consultation → enactment → enforcement                (2-5 years)
```

The structural consequence: by the time governance research concludes with domain-specific recommendations, the AI capabilities those recommendations address may have shifted materially. Cases analyzed during research may no longer represent current deployment patterns. The "unstructured = human domain" assumption weakens with each foundation model generation.

This is not a failure of research quality. It is a structural mismatch between evidence production speed and capability advancement speed.

---

## 2. Quantifying the Gap

### Stanford HAI AI Index 2025

- **233 AI-related incidents** reported in 2024, a 56.4% increase over 2023
- **78% of organizations** use AI in operations, yet **only 14%** have enterprise-level governance frameworks
- U.S. federal agencies introduced **59 AI-related regulations** in 2024, double the 2023 count
- U.S. state-level AI laws increased from 1 (2016) to **131** (2024)
- Legislative mentions of AI rose **21.3%** across 75 countries
- **65+ nations** have published national AI strategies
- Standardized responsible AI evaluations remain **rare** among major model developers

### Enterprise Deployment Gap

- A 2024 study found a **42% shortfall** between anticipated and actual AI deployments
- **80%** of enterprises have 50+ generative AI use cases in pipeline, but most have few in production
- **56%** report it takes **6-18 months** to move a GenAI project from intake to production

### Counterintuitive Finding

Organizations with **mature governance frameworks deploy AI 40% faster** and achieve **30% better ROI** than those without. Governance does not slow adoption — governance uncertainty slows adoption. This supports the argument that adaptive governance frameworks, not governance absence, is the answer to the speed gap.

---

## 3. Existing Mechanisms for Closing the Gap

### 3.1 Regulatory Sandboxes

Regulatory sandboxes allow controlled experimentation under relaxed rules, generating evidence that feeds back into governance design.

#### United Kingdom — FCA

- Launched 2016; 7+ cohorts; **166 firms** supported in first seven cohorts
- Moved to "always open" model in 2021 following the Kalifa Review; **630+ applications** since
- **80% of sandbox firms still operating**; sandbox firms **50% more likely to raise funding** and raise **15% more investment** on average
- October 2024: launched **AI Lab** with three components — AI Spotlight (showcasing), AI Input Zone (industry insights), AI Live Testing (real-world testing)
- September 2025: **Supercharged Sandbox** with NVIDIA, providing high-performance computing and enriched datasets
- November 2024 Bank of England/FCA survey: **75% of financial firms already using AI**, with 10% more planning adoption within three years

**Limitation:** Designed for individual firm testing, not systemic governance questions. Does not directly address temporal gap between capability advancement and regulatory response.

#### Singapore — MAS

- Launched 2016; enhanced with **Sandbox Express** (2019) and **Sandbox Plus** (January 2022)
- **19 firms** accepted; **15 graduated** to full licenses
- Testing periods typically **6-9 months** with extensions on case-by-case basis
- July 2024: **SGD 100 million** additional funding for AI in financial services
- **Project MindForge**: industry consortium co-developed AI risk framework (early 2024)
- October 2024: established **Global Finance & Technology Network (GFTN)**
- Summer 2025: broader AI regulatory sandbox went live

#### South Korea

- Financial regulatory sandbox launched **April 1, 2019** under Special Act on Support for Financial Innovation
- Over **200 innovative financial services** received regulatory exemptions
- August 2024: "Roadmap for Improvement of Network Separation in the Financial Sector" permitted financial companies to use AI models on external cloud networks
- **AI Basic Act** passed December 26, 2024, effective **January 22, 2026** — risk-based approach with detailed obligations for high-impact AI (healthcare, biometrics, credit/loan decisions), explicit transparency duties for generative models, mandatory labeling

#### EU AI Act Sandbox Provisions

- **Article 57** requires each Member State to establish at least one AI regulatory sandbox by **August 2, 2026**
- December 2025: Commission launched stakeholder consultation on draft implementing act
- Spain proactive: **AESIA** designated as national authority, already operational with **12 AI providers**
- Several major Member States (Germany, Belgium, France) missed the August 2, 2025 governance deadline
- Significant implementation delays across the EU

#### Sandbox Assessment

| Strength | Limitation |
|----------|-----------|
| Generates real deployment evidence | Individual-firm focus, not systemic |
| Faster than full regulatory cycles | Still requires months to setup and evaluate |
| Creates feedback loop to policy | Evidence may not generalize beyond sandbox conditions |
| Reduces regulatory uncertainty for participants | Limited capacity — cannot test all emerging capabilities |

---

### 3.2 Responsible Scaling Policies (RSP)

The most direct industry response to the speed gap. RSPs define capability thresholds that trigger governance obligations, allowing governance to scale dynamically with AI capability.

#### Anthropic RSP

- v1.0 (September 19, 2023) → v2.0 (October 15, 2024) → v3.0 (February 24, 2026)
- **Jared Kaplan** serves as Responsible Scaling Officer

**AI Safety Levels (ASL):**

| Level | Description | Trigger | Required Safeguards |
|-------|-------------|---------|---------------------|
| ASL-1 | Basic capabilities (e.g., chess bots) | Default | Minimal |
| ASL-2 | Current baseline for all Anthropic models | Default | Industry best practices |
| ASL-3 | CBRN capability threshold — model could meaningfully assist someone with undergraduate STEM background in creating/deploying chemical or biological weapons | Capability evaluation | Enhanced cybersecurity, constitutional classifiers monitoring I/O, jailbreak detection, pre-deployment red teaming, internal access controls, real-time monitoring, rapid response protocols |
| ASL-4+ | Autonomous AI R&D capability | Capability evaluation | Elevated security standards, affirmative safety case identifying and mitigating misalignment risks |

- **ASL-3 protections activated May 2025**
- v2.0 introduced **Capability Thresholds** and **Required Safeguards** as distinct concepts, replacing broad model categories with targeted per-capability safeguards
- AI R&D thresholds disaggregated into two levels: (1) automating entry-level AI research and (2) causing dramatic acceleration in effective scaling
- Minor compliance gaps identified in first year (three-day evaluation delays), deemed "minimal risk"

#### OpenAI Preparedness Framework

- v1.0 (2023) → v2.0 (April 15, 2025)
- Simplified from four capability levels to two: **High** and **Critical**

| Level | Bio/Chem | Cybersecurity | AI Self-Improvement |
|-------|----------|---------------|---------------------|
| High | Meaningful counterfactual help to novices | Removes bottlenecks, automates vulnerability discovery | Equivalent to giving every researcher a highly performant mid-career research engineer assistant |
| Critical | Enables novel vector creation OR independent engineering/synthesis | Zero-days in hardened systems OR end-to-end novel attacks | Superhuman researcher OR generational improvements in 1/5 normal time |

**Notable provisions:**
- CEO or designee makes final deployment decisions
- Safety Advisory Group provides recommendations but "does not have the ability to filibuster"
- **Competitive pressure clause:** If a rival releases equivalent capabilities without comparable safeguards, OpenAI may reduce its own requirements if adjustment does not meaningfully increase overall harm risk

**Major criticisms (Zvi Mowshowitz et al.):** Removal of persuasion tracking; dropping Low/Medium thresholds eliminates granularity; Critical AI Self-Improvement thresholds may be set so high that detection occurs too late; leadership retains unilateral override power; document explicitly disclaims binding commitment.

#### Google DeepMind Frontier Safety Framework

- v1.0 (May 2024) → v2.0 (February 2025) → v3.0 (September 22, 2025)

**Critical Capability Levels (CCLs) across five domains:**
1. Autonomy — systems capable of independent action
2. Biosecurity — biological threat capabilities
3. Cybersecurity — offensive cyber capabilities
4. ML R&D — AI systems that accelerate AI research
5. Harmful Manipulation (new in v3.0) — models with powerful manipulative capabilities in high-stakes contexts

**Governance mechanism:** When a CCL is reached in a misuse risk domain, a **safety case** must be developed and reviewed by an appropriate corporate governance body before deployment. v3.0 expanded misalignment risk coverage to include instrumental reasoning, ML R&D acceleration, and model interference with operator control.

#### RSP Assessment

| Strength | Limitation |
|----------|-----------|
| Governance scales directly with capability | Self-regulated — no external enforcement |
| Threshold-based triggers are adaptive by design | Thresholds may be set too high or too narrowly |
| Updates on shorter cycles than regulation | Competitive pressure clauses weaken commitments |
| Addresses speed gap most directly | Focused on frontier safety risks, not business decision governance |

---

### 3.3 Continuous Governance Infrastructure

#### Google Model Cards

- Structured documentation acting as "nutrition labels" for AI models
- Documents: model design, training data, intended uses, evaluation results, performance metrics, bias testing, known limitations
- Maps to EU AI Act documentation requirements for high-risk AI systems
- Serves as baseline for monitoring model drift — MLOps teams detect when retraining or governance review is needed
- Governance operationalized across entire model lifecycle: development, deployment, post-launch monitoring, remediation

#### Microsoft Responsible AI Standard (v2)

- Published June 2022; supplemented by Frontier Governance Framework (May 2024)
- Core requirements: impact assessment (required early in development), data governance, human oversight, ongoing monitoring
- 2024: launched internal workflow tool centralizing responsible AI requirements
- 2025 Transparency Report details overhauled **policy-to-implementation pipeline** using policy teams, technical engineering groups, and automated tools embedding compliance checks into product development workflows

#### IBM AI FactSheets (watsonx.governance)

- Captures: data sources, model intent, build approach, performance metrics, bias testing results, audit trails
- **Automated logging:** monitors model facts throughout lifecycle
- **Continuous monitoring:** real-time monitoring with preset thresholds for drift, quality, and safety on inputs and outputs
- **Audit trail:** complete record from production entry including all changes and performance data
- Exportable for stakeholder review or regulatory audits

#### Continuous Governance Assessment

| Strength | Limitation |
|----------|-----------|
| Embeds governance into development workflow | Requires organizational maturity and tooling investment |
| Real-time monitoring enables rapid response | Documentation quality varies with organizational discipline |
| Creates audit trail for accountability | Model cards and FactSheets describe, they do not constrain |
| Reduces governance-as-afterthought problem | No external enforcement mechanism |

---

### 3.4 Living Evidence and Rapid Review Methods

Borrowed from healthcare evidence-based practice, where clinical evidence also evolves faster than traditional review cycles.

#### Cochrane Living Systematic Reviews

- Continually updated as relevant new evidence becomes available
- During COVID-19: Cochrane published **25 COVID-19 living systematic reviews**
- June 2023 assessment: **half had not been updated**, with only **four updated more than once**
- Maintaining currency was "not feasible for many author teams" due to author-side, editorial, and platform barriers

#### WHO/BMJ Living Guidelines

- BMJ/WHO living guideline on drugs for COVID-19 reached **14th version** (13th update)
- Weekly updates informed drug purchases, mask policy, travel requirements
- **MAGIC Evidence Ecosystem Foundation** provided methodological support
- Technology enablers: AI screening, NLP, ML-based automation, crowdsourcing, FAIR data sharing

#### Adaptation Potential for AI Governance

- A **three-actor model** (producers, intermediaries, users) has been proposed for living evidence in policy
- Particularly valuable when "evidence base is dynamic, emerging quickly, and the policy context is evolving" — direct parallel to AI governance
- Value of living evidence **"yet to be substantively tested in policy-relevant domains such as governance"**
- Key barrier: no consensus on optimal update frequency
- Success depends on sustained funding, methodological capacity, and collaborative structures

#### Living Evidence Assessment

| Strength | Limitation |
|----------|-----------|
| Designed for rapidly evolving evidence bases | Maintaining currency proved difficult even in healthcare |
| Keeps recommendations current | Resource-intensive — requires sustained commitment |
| Technology can partially automate updates | Not yet tested substantively in governance domains |
| Matches the speed gap problem well conceptually | No established methodology for AI governance specifically |

---

### 3.5 Principle-Based vs Rule-Based Regulation

| Dimension | EU AI Act (Rule-Based) | Singapore (Principle-Based) | NIST AI RMF (Technology-Neutral) |
|-----------|----------------------|---------------------------|----------------------------------|
| Nature | Binding law | Voluntary frameworks | Voluntary guidance |
| Approach | Risk-based, prescriptive | Principle-based with testing tools | Technology-neutral, principle-based |
| Enforcement | Fines up to EUR 35M / 7% turnover | Incentive-based adoption | None |
| Scope | Extraterritorial (EU market) | Singapore + international influence | US-focused, globally referenced |
| Adaptability | Slow (legislative amendment) | Moderate (framework updates) | High (voluntary, iterative) |
| GenAI coverage | GPAI provisions (August 2025) | Dedicated GenAI framework (2024) + Agentic AI framework (January 2026) | AI 600-1 supplement |
| Speed gap response | Sandboxes + delegated acts | Rapid framework iterations + AI Verify testing | Iterative updates + playbook approach |

**Singapore notable:** Published the world's first **Agentic AI governance framework** (January 2026) — directly addressing a capability category that did not exist when most governance frameworks were designed.

**Cross-framework interoperability:** NIST-IMDA crosswalk enables organizations to satisfy multiple frameworks with a single set of processes. ISO/IEC 42001:2023 provides additional convergence point.

---

### 3.6 Real-Options Thinking for AI Governance

Real options theory treats investments as series of contingent choices rather than one-time commitments, valuing managerial flexibility under uncertainty.

**Application to AI governance:**
- Supports phased regulatory approaches rather than all-or-nothing rules
- Emphasizes maintaining optionality — the ability to wait for better information before irreversible commitments
- Particularly valuable when regulatory decisions have long-lasting consequences in rapidly evolving technological landscapes

**Implicit adoption:** The RSP frameworks from Anthropic, OpenAI, and DeepMind implicitly use real-options logic. Capability thresholds act as "exercise points" where governance commitments are triggered. Organizations do not commit to full governance upfront; they commit to trigger-based escalation.

**Limited direct literature** connecting real options theory specifically to AI governance, but the conceptual fit is strong. Fichman (2004) established the framework for IT platform adoption under uncertainty and irreversibility. The sandbox approach is itself a real-options instrument — limited investment to preserve the option of full deployment or withdrawal.

---

### 3.7 Emerging Adaptive Governance Frameworks

#### Adaptive Governance Framework (Gutierrez et al., 2024)

arXiv:2406.04554 — proposes a five-actor model (government, industry, academia, civil society, citizens) with six shared activities (SCUMIA framework):

1. **Share** best practices across stakeholders
2. **Collaborate** on standards and norms
3. **Use** AI systems under governance-aware conditions
4. **Monitor** deployment outcomes and incidents
5. **Inform** stakeholders of changes and findings
6. **Adapt** governance rules based on accumulated evidence

Key mechanisms:
- **Iterative updates** with built-in feedback loops
- **Government Coordinating Committees** with permanent representatives and rotating external experts
- **Central AI Officer** managing cross-sectoral impacts
- **Incident Registries** tracking AI incidents and development trajectories
- **3% of AI spending** allocated to independent governance research
- **Shortened legitimization processes** for regulatory updates

Acknowledged risks: insufficient oversight from rapid iteration, depth sacrificed for speed, regulatory uncertainty, potential regulatory capture.

#### AGILE Index 2025

The AI Governance International Evaluation Index evaluates **40 countries** across 4 pillars, 17 dimensions, and 43 indicators. Top performers embed agile mechanisms — regulatory sandboxes, ethics-by-design frameworks — that translate principles into practice.

#### Council of Europe Framework Convention (2024)

The **first legally binding international treaty** focused on human rights, democracy, and the rule of law in AI use.

---

## 4. Gap Analysis: What Exists vs What Is Needed

| Need | Existing Solution | Maturity | Gap |
|------|-------------------|----------|-----|
| Governance that scales with capability | RSPs (Anthropic, OpenAI, DeepMind) | Moderate — self-regulated, frontier-focused | Not designed for business decision governance |
| Controlled experimentation under relaxed rules | Regulatory sandboxes (FCA, MAS, Korea) | Mature for fintech; early for AI broadly | Individual-firm focus; months-long cycles |
| Governance embedded in development workflow | Model Cards, FactSheets, MS RAI Standard | Moderate — requires organizational discipline | Describes and monitors, does not constrain |
| Continuously updated evidence and recommendations | Living systematic reviews | Early — proven concept, unproven at scale for governance | Not yet tested in governance domains |
| Governance rules that survive capability shifts | Principle-based regulation (Singapore, NIST) | Moderate — growing adoption | Principles alone do not produce specific guidance |
| Staged deployment preserving flexibility | Real-options thinking | Conceptual — limited formal methodology | No established tooling or standard process |
| Multi-stakeholder adaptive governance | Adaptive governance frameworks (Gutierrez et al.) | Early — proposed, not widely implemented | Untested at institutional scale |

---

## 5. Implications for This Research

### What phases 00-20 did well

The research's principle-level findings — adaptive authority, scenario-sensitive governance, escalation/fallback logic — are structurally durable. They do not depend on specific AI capabilities and become more important as capabilities advance.

### What phases 00-20 did not address

1. **No transition conditions:** The research recommends "assist" or "recommend" for specific domains but does not specify measurable conditions under which those recommendations should change
2. **No living evidence protocol:** Recommendations are presented as static conclusions, not as current-best-defaults with update mechanisms
3. **No capability-indexed governance:** The framework does not connect governance requirements to AI capability levels (as RSPs do)
4. **Pre-LLM case base:** All cases predate the foundation model era
5. **No agentic AI coverage:** The 7-stage workflow model assumes human checkpoints between stages

### Required extensions

1. **Layer 2 — Transition Conditions:** Define measurable graduation criteria for when AI authority can escalate or must fall back, indexed to capability and evidence rather than fixed domain labels
2. **Layer 3 — Living Evidence Protocol:** Define update triggers, review cadence, and version management for recommendations that evolve with the evidence base
3. **Agentic AI governance extension:** Address continuous AI workflows without discrete human checkpoints
4. **Capability-indexed governance mapping:** Connect the assist/recommend/automate framework to observable AI capability indicators

---

## Sources

### Regulatory Sandboxes
- FCA Regulatory Sandbox: https://www.fca.org.uk/firms/innovation/regulatory-sandbox
- FCA AI Lab: https://www.fca.org.uk/firms/innovation/ai-lab
- FCA AI Update (PDF): https://www.fca.org.uk/publication/corporate/ai-update.pdf
- MAS Regulatory Sandbox: https://www.mas.gov.sg/development/fintech/regulatory-sandbox
- MAS Sandbox Plus: https://www.mas.gov.sg/development/fintech/sandbox-plus
- Korea Financial Regulatory Sandbox: https://sandbox.fintech.or.kr/financial/overview.do?lang=en
- Korea AI Basic Act: https://beaumont-capitalmarkets.co.uk/featured_item/south-korea-ai-basic-act-financial-regulations/
- EU AI Act Article 57: https://artificialintelligenceact.eu/article/57/
- EU AI Act Member State Overview: https://artificialintelligenceact.eu/ai-regulatory-sandbox-approaches-eu-member-state-overview/

### Responsible Scaling Policies
- Anthropic RSP: https://www.anthropic.com/responsible-scaling-policy
- Anthropic RSP v3.0 (PDF): https://www-cdn.anthropic.com/e670587677525f28df69b59e5fb4c22cc5461a17.pdf
- Anthropic ASL-3 Report: https://www.anthropic.com/activating-asl3-report
- OpenAI Preparedness Framework v2 Analysis: https://thezvi.substack.com/p/openai-preparedness-framework-20
- DeepMind FSF v3: https://deepmind.google/blog/strengthening-our-frontier-safety-framework/

### Continuous Governance
- Google Model Cards: https://modelcards.withgoogle.com/
- Google Responsible AI Progress Report 2025 (PDF): https://ai.google/static/documents/ai-responsibility-update-published-february-2025.pdf
- Microsoft Responsible AI Standard v2 (PDF): https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Microsoft-Responsible-AI-Standard-General-Requirements.pdf
- Microsoft 2025 Responsible AI Transparency Report: https://www.microsoft.com/en-us/corporate-responsibility/responsible-ai-transparency-report/
- IBM watsonx.governance: https://www.ibm.com/products/watsonx-governance

### Living Evidence
- Cochrane Living Systematic Reviews: https://community.cochrane.org/review-development/resources/living-systematic-reviews
- Cochrane COVID-19 Living Reviews Assessment: https://pubmed.ncbi.nlm.nih.gov/40656451/
- Living Evidence and Adaptive Policy: https://health-policy-systems.biomedcentral.com/articles/10.1186/s12961-023-01085-4
- Nature — Decision Makers Need Constantly Updated Evidence Synthesis: https://www.nature.com/articles/d41586-021-03690-1

### Principle-Based Regulation
- Singapore AI Governance: https://www.imda.gov.sg/about-imda/emerging-technologies-and-research/artificial-intelligence
- Singapore Agentic AI Framework: https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf
- NIST AI RMF 1.0: https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf
- AI Governance Frameworks Comparison: https://www.lumenova.ai/blog/ai-governance-frameworks-nist-rmf-vs-eu-ai-act-vs-internal/

### Adaptive Governance
- Gutierrez et al. (2024) Adaptive Governance: https://arxiv.org/html/2406.04554v1
- Stanford HAI AI Index 2025: https://hai.stanford.edu/ai-index/2025-ai-index-report
- AGILE Index 2025: https://arxiv.org/abs/2507.11546
- Council of Europe Framework Convention on AI (2024)
- WEF Agile AI Governance: https://www.weforum.org/stories/2025/10/measurement-momentum-agile-governance-ai/

### Real Options
- CGO Real Options for Regulatory Decisions: https://www.thecgo.org/research/real-options-analysis-could-help-improve-regulatory-decisions/
- Fichman (2004) Real Options and IT Platform Adoption, Information Systems Research
