# How Organizations Actually Govern AI: Industry Practice Survey

## Status: research_complete
## Phase: 21 — Adaptive Governance Extension
## Date: 2026-03-10

---

## 1. Purpose

Phases 00-20 built a normative framework (what organizations should do). Phase 21's earlier documents added adaptive governance mechanisms. This document surveys what organizations **actually do** in practice — the real structures, processes, shortcuts, and failures observed across industries in 2024-2026.

The gap between normative frameworks and actual practice is itself a critical finding. Understanding this gap informs how the research framework should be designed for adoption, not just for theoretical completeness.

---

## 2. Big Tech: Divergent Approaches

### Google

**Structure:** Four-pillar framework (Govern, Map, Measure, Manage). Governance teams span ML research, product policy, UX research, public policy, law, human rights, and social sciences. DeepMind operates a separate Frontier Safety Framework with Critical Capability Levels (CCLs).

**What actually happens:** Pre-deployment models undergo comprehensive safety evaluations including bias and toxicity testing. An internal governance assessment platform handles flagged content. Annual Responsible AI Progress Reports (6th edition in February 2025).

**What went wrong:** In February 2024, Gemini's image generation produced historically inaccurate outputs (e.g., racially diverse Nazis). CEO Sundar Pichai called the errors "unacceptable" in an internal memo. This demonstrates that even multi-team governance structures can miss critical failure modes when testing does not cover the full output space.

**Notable opacity:** Google DeepMind's AGI Safety Council has shared very limited information about its mandate and operations.

---

### Microsoft

**Structure:** The most publicly documented governance structure among Big Tech. Natasha Crampton serves as the first Chief Responsible AI Officer, leading the Office of Responsible AI.

**Operational components:**
- Responsible AI Standard as backbone policy
- Frontier Governance Framework for advanced model risk
- Sensitive Uses and Emerging Technologies team providing hands-on counseling for high-impact deployments (healthcare, sciences)
- Distributed community of Responsible AI CVPs, Division Leads, and "Champs" across the organization
- Policy-to-tooling pipeline translating requirements into engineering workflows and dashboards
- Layered safety stack: User Experience > System Messages and Grounding > Safety System > Model
- Pre-deployment oversight including deployment safety process for generative AI systems
- Internal workflow tool centralizing responsible AI requirements

**Assessment:** Microsoft comes closest to the continuous governance infrastructure described in Layer 2 of this research. The layered safety stack and deployment gates are operationally real, not just documented. The 2025 Responsible AI Transparency Report (second annual) provides deep dives on actual review cases.

---

### Meta

**Structure:** Meta **disbanded its dedicated Responsible AI team** in late 2023, first pruning by half, then restructuring remaining members into generative AI and AI infrastructure teams. Part of the "year of efficiency."

**What actually happens now:**
- Engineers building Meta products make their own judgments about risks
- Manual human review happens only for projects involving new risks or where teams explicitly request feedback — not by default
- Meta uses AI to handle up to 90% of all risk assessments by 2025, with LLMs "operating beyond that of human performance for select policy areas"
- Reinforcement learning achieves 10x to 100x data efficiency improvements over supervised fine-tuning for content moderation

**Assessment:** Meta represents the opposite end of the governance spectrum from Microsoft. Governance has been effectively decentralized to individual engineering teams and partially automated. In May 2025, NPR reported that Meta plans to replace humans with AI to assess privacy and societal risks, raising significant concerns about governance adequacy.

**Research implication:** Meta's approach directly challenges this research's assumption that human oversight should be operationally real in high-stakes domains. Meta treats its own AI governance as an automation-eligible task.

---

### Amazon / AWS

**Structure:** Governance primarily visible through AWS-facing tools rather than internal practices.

**Operational components:**
- AWS Well-Architected Responsible AI Lens for development lifecycle
- AI Risk Intelligence (AIRI) solution transforming best practices into automated governance controls
- Amazon SageMaker Data and AI Governance (launched December 2024) with column-level data curation and metadata enforcement

**Assessment:** Amazon's governance is productized — they sell governance tools rather than publicly demonstrating internal governance practices. Limited visibility into how Alexa, retail algorithms, or logistics AI are governed internally.

---

### Apple

**Structure:** The most opaque among Big Tech. Privacy serves as the primary governance mechanism.

**What actually happens:**
- On-device processing as governance-by-architecture — Apple Foundation Models run locally
- Guideline 5.1.2(i) (November 2025) made third-party AI a regulated category for the first time, requiring clear disclosure and explicit user permission for data sharing
- Very little public information about internal governance committees or review processes

**Assessment:** Apple governs through architectural constraints (on-device processing, data minimization) rather than organizational processes. This is a fundamentally different model from the committee-based governance this research assumes.

---

### Big Tech Pattern Summary

| Company | Governance Model | Transparency | Distinctive Feature |
|---------|-----------------|--------------|---------------------|
| Google | Multi-team review with safety evaluations | Moderate (annual reports) | Separate frontier safety for DeepMind |
| Microsoft | Centralized office with distributed champions | High (transparency reports) | Policy-to-tooling pipeline |
| Meta | Decentralized to engineering + AI-automated review | Low | Governance itself treated as automation-eligible |
| Amazon | Productized (sells governance tools) | Low (internal practices opaque) | Governance-as-service |
| Apple | Architecture-based (on-device, privacy-first) | Very low | Governance through design constraints |

---

## 3. Financial Services: The Most Mature Governance

Financial services has the most developed AI governance practice, driven by decades of model risk management regulation (SR 11-7, SS1/23).

### JPMorgan Chase

**Scale:** $18 billion technology budget for 2025; ~$1.3 billion dedicated to AI capabilities in 2024.

**Structure:**
- Explainable AI Center of Excellence
- Dedicated firm-wide Model Risk Governance function
- AI governance committee overseeing development and deployment of all models
- Multi-tiered governance model integrating legal, compliance, cybersecurity, and data ethics into every AI initiative
- AI Model Risk Management Framework (introduced 2024) aligned with EU AI Act and NIST AI RMF
- Patented algorithmic bias evaluation framework specifically for auditing lending risk models for disparate impact

**Deployed systems:**
- LOXM: AI trading execution trained on billions of past trades
- COiN (Contract Intelligence): Analyzes payment documents for fraud before fund release

**Assessment:** JPMorgan represents the closest real-world implementation to this research's framework. Multi-tiered governance, bias auditing, regulatory alignment, and domain-specific risk management mirror the Phase 04 evaluation framework. Their patented bias evaluation framework directly addresses fairness concerns central to the finance domain analysis.

---

### Goldman Sachs

**Structure:**
- GS AI Platform offering multiple AI models with Goldman's guardrails
- ~10,000 employees with access to the GS AI Assistant with governance controls, including mandatory human reviewer for chatbot responses
- "AI Champions" program: team within each business group finding effective use cases, forming "connective tissue" across the firm
- Model Risk Management (MRM) teams co-develop control frameworks with data scientists
- API-first governance framework with authentication, authorization, and data protection

**Notable shift:** In 2025, Goldman reduced AI budgets by 15% and shifted focus to explainable AI (XAI), aiming for 92% model transparency.

**Assessment:** Goldman's AI Champions program mirrors the hub-and-spoke organizational model described in Phase 20 Part 3. The mandatory human reviewer for chatbot responses is a concrete implementation of the "recommend" mode with human approval. The shift toward XAI reflects growing recognition that explainability is a governance prerequisite, not just a regulatory checkbox.

---

### BlackRock

**Structure:**
- Aladdin platform (hosted on Microsoft Azure) processes across public and private markets
- Aladdin Copilot: Generative AI assistant with built-in guardrails — will not give investment advice or respond outside platform boundaries; includes content filtering and hallucination mitigation
- Asimov (announced June 2025): AI research platform scanning research notes, filings, and emails for portfolio insights
- Auto Commentary: AI synthesizing portfolio analytics, CIO outlooks, and client preferences

**Assessment:** BlackRock's Aladdin Copilot demonstrates bounded automation in practice. The explicit refusal to give investment advice (even though it technically could) is a deliberate governance constraint — the system operates in "assist" mode for high-stakes investment decisions while automating lower-risk information synthesis. This aligns directly with this research's recommendation for investment domain governance.

---

### Stripe

**Deployed system:** World's first AI foundation model for payments (2025), trained on tens of billions of transactions with hundreds of signals per payment. Uses self-supervised learning rather than explicit fraud labeling.

**Results:**
- 64% increase in detection of card-testing attacks on large businesses
- $6 billion in legitimate declined transactions recovered in 2024
- 17% reduction in dispute rates even as industry-wide fraud increased 15%
- Processed $1.4 trillion in 2024 (up 36% YoY)

**Assessment:** Stripe represents automate-with-guardrails in a medium-risk domain (payment fraud). The system makes autonomous decisions (block/allow transactions) with monitoring and exception handling. This works because the decision is structured, repeated, measurable, and has strong feedback loops — exactly the conditions this research identifies as suitable for bounded automation.

---

### Banking Model Risk Management (SR 11-7)

SR 11-7's four pillars (validation, documentation, governance, monitoring) are now evolving to account for AI-specific requirements:
- Model drift monitoring required alongside traditional validation
- Explainability requirements for ML models — regulators push back on pure black-box approaches
- Third-party/vendor model risk: banks must demonstrate oversight of external AI services
- Generative AI monitoring must capture hallucinations, factual reliability, and adversarial performance
- SEC Division of Examinations identified AI governance as an examination priority for 2025

**Assessment:** Banking regulation already enforces many of the governance conditions this research recommends. The evolution of SR 11-7 to cover AI-specific risks (drift, explainability, third-party risk, hallucination) provides Tier 1 evidence that regulators are moving toward the kind of continuous governance this research advocates.

---

### Ant Group / Alipay

- R&D spending of RMB 23.45 billion (10.7% YoY increase) focused on AI
- AI systems processed 7.25 million health insurance claims in 2024 (55% YoY increase)
- Collaborated with OpenAI, Google, and Microsoft on two international industry standards for GenAI security and validation
- Governance significantly shaped by regulatory enforcement: $985 million fine from PBOC in 2023 for corporate governance, consumer protection, and money-laundering violations

**Assessment:** Ant Group demonstrates enforcement-driven governance. The $985 million fine created a strong incentive structure that voluntary frameworks lack. Their subsequent investment in AI governance and international standards collaboration suggests that enforcement can be an effective catalyst for governance maturation.

---

## 4. Healthcare: Governance by Regulation and Clinical Culture

### Hospital AI Governance Structures

- ~75% of large health systems now have AI governance committees as of 2024-2025
- Hospitals using Epic had ~90% AI usage in 2024 vs ~50% for other EHR systems

**Mayo Clinic:** Uses an "enablement-oriented" approach called "stewardship" rather than governance. Staff see the data and AI team as enablers, not gatekeepers. User groups are responsible for getting data ready; business and clinical stakeholders are data stewards.

**Cleveland Clinic:** Uses interdisciplinary teams meeting monthly to review AI performance and make real-time adjustments. Building AI tools from the ground up rather than purchasing off-the-shelf. Faster feedback cycles than most health systems.

**Cedars-Sinai:** Launched an AI Council in 2023 to oversee governance and ethical deployment across departments.

**Assessment:** Healthcare governance is deeply shaped by clinical culture. Mayo Clinic's "stewardship" framing is notable — governance succeeds when it is perceived as enablement rather than constraint. This aligns with the finding that mature governance accelerates deployment rather than slowing it.

---

### EHR Platform AI

**Epic:**
- Cosmos Medical Event Transformer (CoMET): Foundation models pre-trained on 118 million patients and 151 billion medical events, matching or outperforming task-specific models across 78 clinical tasks
- Launchpad: Structured program for deploying generative AI workflows with governance
- AI Trust and Assurance Suite: Enables local validation and continuous monitoring for performance, bias, and unintended consequences

**Assessment:** Epic's platform demonstrates governance-embedded-in-infrastructure. The AI Trust and Assurance Suite operationalizes Layer 2's continuous monitoring concept within a clinical context. Local validation capability allows hospitals to verify AI performance against their own patient population — addressing the population shift regression trigger.

---

### FDA Landscape

- Over 1,250 AI-enabled medical devices authorized as of July 2025 (up from 950 in August 2024)
- 295 FDA clearances in 2025 alone
- Predetermined Change Control Plans (PCCPs): Final guidance allowing manufacturers to update AI-enabled devices without new marketing applications for covered changes
- January 2025 draft guidance on lifecycle management emphasizing continuous monitoring
- Two new cross-agency councils in 2025: External Policy Council (principles for regulated products) and Internal Use Council (FDA's own AI usage)

**Assessment:** PCCPs are the regulatory equivalent of Layer 2 transition conditions — they define pre-approved change boundaries, allowing AI to evolve within governed constraints without requiring fresh regulatory approval for each update. This is the most mature example of adaptive governance in regulated practice.

---

## 5. Enterprise Governance Platforms and Team Structure

### Tools Actually Used

| Platform | Adoption | Key Governance Feature |
|----------|----------|----------------------|
| DataRobot | 1,000+ organizations | Agent Workforce Platform with built-in evaluation and guardrails |
| Domino Data Lab | Enterprise focused | Governance automation and evidence collection for compliance |
| H2O.ai | 20,000+ organizations | On-premises air-gapped installations for regulated industries |
| MLflow | Most widely adopted open-source | Experiment tracking, model registry |
| Weights and Biases | AI-native companies | Experiment tracking and model monitoring |

### Enterprise Platform AI Governance

**ServiceNow:** Positioning as "AI platform at the core of orchestrating, governing, and scaling enterprise AI." AI Control Tower is the highest-interest product because customers worry about control with agentic AI. Acquired Data.World for data catalog/governance.

**Salesforce:** Agentforce 3 with Command Center for AI agent control; Agent2Agent protocol support.

**Assessment:** The emergence of agentic AI is creating demand for governance-as-platform. ServiceNow's AI Control Tower directly addresses the agentic AI governance gap identified in Phase 21. Companies are looking for centralized visibility into autonomous AI agents operating across their systems.

---

### What AI Governance Teams Actually Look Like

IAPP 2024 survey (670+ respondents from 45 countries):
- Average AI governance team: **~9 people**
- **17% of organizations** have only 1 person responsible for AI governance
- **Privacy function** most commonly responsible for AI governance, followed by legal/compliance and security
- **69% of chief privacy officers** have acquired additional responsibility for AI governance
- **55% of privacy professionals** work in functions with AI governance responsibilities
- Only **28%** have formally defined oversight roles
- Only **59%** have dedicated governance roles despite 75% having AI usage policies

**Assessment:** The typical AI governance team is remarkably small relative to AI engineering teams. Privacy officers are absorbing AI governance by default, not by design. This creates a governance capability gap — privacy expertise does not automatically translate to AI governance expertise (fairness, drift monitoring, explainability). The research's Phase 20 Part 3 organizational design recommendations assume dedicated governance roles that most organizations do not have.

---

## 6. Consulting Firms: What They See vs What They Recommend

### The Reality Gap

- **McKinsey:** 88% of companies use AI in at least one function, but only 39% see impact on EBIT (usually less than 5%)
- **BCG:** 60% generate no material value despite investments; only 5% create substantial value at scale
- Nearly two-thirds of firms remain in experimentation (32%) or piloting (30%); only 31% scaling enterprise-wide
- 62% experimenting with AI agents, but fewer than 10% deploying at scale

### The Deloitte Failure (2025)

A defining governance failure case: Deloitte used GPT-4o to produce a $290,000 (AUD $440,000) report for Australia's Department of Employment and Workplace Relations. A University of Sydney researcher discovered fabricated academic citations and non-existent court references. Deloitte admitted its internal review and QA processes had failed. The firm had not disclosed AI usage until after errors were discovered.

**Significance:** This is a governance failure at the recommend/automate boundary in a professional services context. The AI generated content (automate), it was reviewed (recommend gate), but the review process failed to catch fabricated evidence. This directly illustrates the research's warning that governance mechanisms must be operationally real, not just documented.

**Additional irony:** Deloitte had previously blocked internal access to ChatGPT and developed its own tool with stringent security validation — demonstrating that governance policies and governance execution can diverge sharply.

---

## 7. Government and Public Sector

### US Federal AI Governance (Policy Oscillation)

**Biden era (2024):** M-24-10 and M-24-18 required detailed AI governance. After December 1, 2024, agencies had to stop using AI systems without required safeguards. Agencies reported 1,700+ AI use cases, with 227 identified as rights-impacting or safety-impacting. 206 high-impact use cases received one-year extensions.

**Trump era (2025):** M-25-21 and M-25-22 focused on "removing existing policies" to "facilitate rapid, responsible adoption." Agencies must designate Chief AI Officers within 60 days and convene governance boards within 90 days. Compliance deadline extended to April 15, 2026. December 2025 executive order on "Eliminating State Law Obstruction of National AI Policy."

**Assessment:** US federal AI governance demonstrates the challenge of governance stability under political change. Research frameworks that depend on stable regulatory direction face the risk that regulatory direction itself oscillates. This reinforces the argument for principle-based rather than rule-based governance — principles survive political transitions better than specific rules.

---

### UK AI Security Institute (AISI)

- Renamed from AI Safety Institute in February 2025
- 100+ technical staff including alumni from OpenAI, Google DeepMind, Oxford
- $66 million/year funding with priority access to over $1.5 billion in compute
- Tested 16 models including at least 3 frontier models ahead of public launch
- End-to-end biosecurity red-teaming with OpenAI and Anthropic found dozens of vulnerabilities
- Open-source tools: Inspect, InspectSandbox, InspectCyber, ControlArena — used globally

**Assessment:** AISI represents the most technically capable government AI governance body. Its pre-deployment testing capability and open-source tooling create a feedback loop between frontier AI development and governance. The biosecurity red-teaming results provide Tier 1 evidence for capability-specific governance requirements.

---

### Singapore IMDA

- Model AI Governance Framework for Generative AI (May 2024): Nine proposed dimensions, endorsed by 70+ respondents
- Global AI Assurance Pilot (February 2025): Codifying norms for technical AI testing
- AI Safety Red Teaming Challenge Evaluation Report 2025
- Draft addendum on Securing Agentic AI (open for feedback October-December 2025)

**Assessment:** Singapore continues to lead in iterative, principle-based governance. The Agentic AI governance framework (January 2026) directly addresses the gap this research identified in Phase 21. Singapore's approach — publish framework, gather feedback, iterate — is the closest governmental analog to the living evidence protocol.

---

## 8. Cross-Industry Patterns

### Organizational Structure Reality

- No consensus: 36% centralized, 36% federated, 29% hybrid
- Hub-and-spoke (hybrid) emerging as most effective in practice
- 40%+ of Fortune 500 expected to have a CAIO role by 2026 (26% had one in 2025, up from 11% in 2023)
- Companies with a CAIO report stronger AI ROI
- EU AI Act compliance expected to consume 40-50% of CAIO time

### What Companies Actually Skip

| Governance Practice | Adoption Rate | Gap |
|--------------------|--------------|-----|
| AI usage policies | 75% | Policy exists on paper |
| Dedicated governance roles | 59% | Many are part-time or absorbed by privacy |
| Incorporate governance into AI workflow | 34% | Two-thirds build without governance integration |
| Address bias in AI models | 32% | Most do not actively audit for fairness |
| Formally defined oversight roles | 28% | Most governance is informal |
| Board-level AI governance oversight | 17% | AI governance rarely reaches the board |
| Incident response playbooks for AI | 54% | Nearly half have no AI incident plan |

### Documented Governance Failures (2024-2025)

| Case | Domain | What Happened | Root Cause |
|------|--------|---------------|------------|
| Deloitte Australia | Professional services | Fabricated citations in $290K government report | Review process failed to verify AI-generated references |
| Air Canada | Customer service | Chatbot gave incorrect bereavement fare information; airline ordered to pay damages | No human review of chatbot responses in sensitive context |
| Google Gemini | Image generation | Historically inaccurate outputs (racially diverse Nazis) | Testing did not cover full output space for historical prompts |
| NYC MyCity chatbot | Government services | Falsely claimed business owners could take workers' tips | No domain expert review of AI-generated legal guidance |
| Major insurer (unnamed) | Healthcare insurance | AI algorithm denied elderly patient coverage; 90% error rate on human review | Automated denial without adequate clinical review |
| Major HR vendor (unnamed) | Hiring | AI hiring tool systematically screened out applicants by age | No adverse impact testing before deployment |
| Italy AI fine | Data protection | EUR 15 million fine for processing personal data without safeguards during training | Training data governance absent |

### The Paradox: Governance Enables Speed

- Organizations with mature governance frameworks deploy AI **40% faster** and achieve **30% better ROI**
- Companies with a CAIO report stronger AI ROI
- Yet **42% of companies abandoned most AI initiatives** in 2025 (up from 17% in 2024)
- MIT 2025 report: **95% of generative AI pilots** at companies are failing
- Top obstacles: data quality (43%), technical maturity (43%), skills shortage (35%)

**Interpretation:** Governance does not cause the 95% pilot failure rate. Poor data quality, insufficient technical capability, and skills gaps cause failure. Governance actually helps organizations avoid investing in doomed projects and focus on viable ones. The perception that governance slows innovation is empirically wrong — governance uncertainty slows innovation.

---

## 9. Comparison: Research Framework vs Industry Practice

### Where Practice Matches the Framework

| Research Recommendation | Industry Practice Example |
|------------------------|--------------------------|
| Assist mode for high-stakes domains | BlackRock Aladdin Copilot refuses to give investment advice |
| Multi-tiered governance for finance | JPMorgan's layered governance integrating legal, compliance, cybersecurity, and data ethics |
| Human override must be operational | Goldman Sachs mandatory human reviewer for AI chatbot responses |
| Automate with guardrails for structured, measurable decisions | Stripe's payment fraud foundation model with monitoring |
| Governance embedded in development workflow | Microsoft's policy-to-tooling pipeline |
| Hub-and-spoke organizational model | Goldman Sachs AI Champions program |
| Continuous monitoring for drift and fairness | Epic AI Trust and Assurance Suite |
| Regulatory sandboxes for controlled experimentation | FCA AI Lab, MAS Sandbox, PCCPs |

### Where Practice Diverges from the Framework

| Research Assumption | Industry Reality | Gap |
|--------------------|-----------------|-----|
| Organizations have dedicated governance teams | Average team is 9 people; 17% have 1 person | Governance capacity much thinner than assumed |
| Human oversight is operationally real | Meta automates 90% of risk assessments with AI | Some companies automate governance itself |
| Governance committees review high-stakes deployments | Only 28% have formally defined oversight roles | Most governance is informal and undocumented |
| Fairness auditing is standard practice | Only 32% address bias in AI models | Most companies do not audit for fairness |
| Board provides AI governance oversight | Only 17% of boards oversee AI governance | Governance rarely reaches executive level |
| Incident response is planned | Only 54% have AI incident playbooks | Nearly half have no response plan |
| Evidence quality is tracked | No widespread practice of evidence tier classification | Companies do not classify their evidence |
| Framework review is systematic | Governance often absorbed by privacy or legal as side duty | No dedicated framework maintenance |
| Agentic AI has human checkpoints | Agentic AI governance is just emerging (Singapore January 2026) | Most organizations have no agentic AI governance |

---

## 10. Implications for This Research

### What the research gets right

1. **The core distinction matters.** assist/recommend/automate is visible in real practice — BlackRock's Copilot (assist for investment), Goldman's reviewer requirement (recommend with human approval), Stripe's fraud model (automate with guardrails).

2. **Financial services leads governance maturity.** Banking model risk management (SR 11-7) creates the most rigorous governance environment, confirming the research's emphasis on finance as a governance-first domain.

3. **Governance enables, not impedes.** The empirical finding that mature governance correlates with faster deployment and better ROI validates the research's position.

4. **Regulatory enforcement drives adoption.** Ant Group's $985 million fine and subsequent governance investment shows that enforcement works where voluntary frameworks may not.

### What the research should update

1. **Governance capacity assumptions are too optimistic.** The framework assumes dedicated governance teams, formal oversight roles, and systematic review processes. Most organizations have none of these. The framework needs a lightweight governance track for resource-constrained organizations.

2. **Meta's model challenges core assumptions.** The research assumes human oversight must be operationally real. Meta is automating governance itself. The framework should explicitly address and evaluate AI-governed-AI as a design pattern, even if to reject it for high-stakes domains.

3. **Architecture-based governance is underrepresented.** Apple's on-device processing approach governs through design constraints rather than organizational processes. The framework should recognize governance-by-architecture as a complementary mechanism.

4. **Agentic AI governance is urgent.** ServiceNow's AI Control Tower and Singapore's Agentic AI framework show that industry and government are already responding to agentic AI. The framework's current 7-stage workflow model needs an agentic AI extension.

5. **Political risk to governance stability.** US federal AI governance oscillation between administrations shows that regulatory-dependent governance claims face political risk. The framework should distinguish between governance mechanisms that are regulation-dependent versus those that are organization-internal and more stable.

---

## Sources

### Big Tech
- Google Responsible AI 2024 Report and February 2025 Progress Report
- Microsoft 2025 Responsible AI Transparency Report
- Meta Oversight Board September 2024 Report; NPR May 2025 reporting
- Amazon AWS Responsible AI documentation; SageMaker governance launch
- Apple Guideline 5.1.2(i) November 2025

### Financial Services
- JPMorgan Chase technology and AI governance disclosures
- Goldman Sachs AI platform and Champions program documentation
- BlackRock Aladdin Copilot and Asimov announcements
- Stripe 2025 State of AI and Fraud report
- Ant Group 2024 Sustainability Report
- SR 11-7 and model risk management evolution literature

### Healthcare
- Mayo Clinic AI governance approach (MIT Sloan Review)
- Cleveland Clinic AI strategy reporting
- Epic CoMET and AI Trust and Assurance Suite documentation
- FDA AI-enabled device tracker and PCCP guidance

### Enterprise and Governance Teams
- IAPP AI Governance in Practice Report 2024
- IAPP AI Governance Profession Report 2025
- ServiceNow AI Control Tower reporting
- DataRobot, Domino, H2O.ai platform documentation

### Consulting and Failures
- McKinsey State of AI 2025
- BCG AI adoption and value analysis
- Deloitte Australia AI governance failure (Fortune, Computerworld)
- Air Canada chatbot case; NYC MyCity chatbot; Google Gemini incident

### Government
- OMB M-24-10, M-24-18, M-25-21, M-25-22
- UK AISI 2025 Year in Review
- Singapore IMDA GenAI and Agentic AI frameworks
- EU AI Act implementation timeline and AI Pact

### Cross-Industry Statistics
- Stanford HAI AI Index 2025
- EY 2025 AI governance survey
- MIT 2025 GenAI pilot failure report
- Fortune 500 AI governance adoption data
