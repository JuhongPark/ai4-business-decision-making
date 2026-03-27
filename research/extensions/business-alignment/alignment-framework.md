# Business-Context AI Alignment Framework

status: draft
date: 2026-03-25
purpose: define a usable analytical framework for studying alignment in business AI systems without drifting into abstract model-alignment framing

## Why This Note Exists

The repository already argues that firms should assign AI authority adaptively rather than treat AI adoption as a binary question.

What has been missing is a dedicated framework that explains what "alignment" means in business settings.

This note proposes that:

**business-context AI alignment is the problem of keeping AI-supported decision systems aligned with the real business problem, the right level of delegated authority, the right validation structure, and the real accountability conditions of deployment.**

This keeps the project in a business-facing governance lane while giving it a clearer conceptual center.

## Working Definition

Business-context AI alignment asks:

- whether the firm is using AI for the right kind of problem
- whether the AI has the right amount of practical authority
- whether human reliance is calibrated rather than naive
- whether review and verification are substantively reliable
- whether the system stays inside approved policy and knowledge boundaries
- whether the system is deployable under real legal, contractual, and market conditions

The central question is not:

- "Is the model aligned in a general technical sense?"

The central question is:

- "Is the organization using AI in a way that keeps authority, trust, validation, and accountability aligned with the actual business context?"

## Scope Boundary

This framework is not a full theory of frontier-model alignment.

It is a framework for studying alignment in firms, especially where AI enters workflows that affect:

- decisions
- recommendations
- gatekeeping
- customer or employee communication
- action triggering

## Evidence Base

### 1. Human-AI performance depends on delegation design

Evidence strength: strong

- Vaccaro, Almaatouq, and Malone's 2024 meta-analysis found that human-AI combinations performed worse on average than the better of human alone or AI alone, with decision tasks associated with performance losses and creation tasks showing more promise.
- Dell'Acqua et al.'s 2025 field experiment at Procter & Gamble found that individuals with AI matched the performance of teams without AI and reduced functional silos, suggesting that AI changes how expertise is combined rather than merely speeding up isolated tasks.
- Agarwal, Moehring, and Wolitzky's 2025 NBER paper shows that the design of disclosure and selective automation policies matters because people under-respond to AI predictions and reduce effort when AI is highly confident.

Interpretation:

These sources jointly support the claim that the main business design variable is not adoption alone but division of labor, disclosure design, and selective delegation.

### 2. Trust calibration is a first-order business variable

Evidence strength: strong

- Gans's 2026 NBER paper models "Artificial Jagged Intelligence" as uneven local reliability across nearby tasks and shows that value depends on learning where the model works rather than relying on coarse average quality signals.
- The repository's incident synthesis shows that firms repeatedly fail when they trust fluent outputs without independent validation or give models de facto authority through framing, option generation, or rationale production.

Interpretation:

Trust should be treated as an operational design issue, not a soft cultural concern. Firms need ways to map local reliability and identify where users are likely to over-trust or under-trust.

### 3. Governance has become more concrete and organizational

Evidence strength: moderate to strong

- Engel and Duske's 2025 AMCIS paper develops a RACI matrix for AI governance and argues that effective governance combines centralized accountability with decentralized specialized roles.
- The repository's adaptive-governance work already provides escalation, fallback, infrastructure, and living-evidence logic.

Interpretation:

Alignment in firms cannot be reduced to principles alone. It has to be translated into ownership, checkpoints, escalation paths, and organizational architecture.

### 4. Policy-facing and customer-facing systems create a distinct alignment problem

Evidence strength: strong within the repository's incident logic, plus moderate external institutional support

- The repository's incident analysis argues that LLMs create communication and policy risk because they speak fluently, explain persuasively, and can be mistaken for an authoritative company representative.
- Current public procurement and supplier-governance materials increasingly require documented trustworthy AI controls, which implies that policy-sensitive systems are expected to operate within explicit governance boundaries rather than as free-form assistants.

Interpretation:

When the AI represents company policy, customer commitments, hiring logic, or compliance guidance, the alignment problem becomes sharper. The issue is no longer only prediction quality. It is whether the system is authorized to speak and act within real organizational boundaries.

## The Framework

This framework has six layers.

### Layer 1: Problem Alignment

Question:

Is the firm handing AI a problem that is appropriate for AI support at the current level of maturity?

Main failure mode:

- giving AI work that is too ambiguous, too subjective, too high-stakes, or too policy-sensitive for the current workflow design

What to evaluate:

- task structure
- stakes
- reversibility of error
- dependence on tacit knowledge
- personalization requirements

### Layer 2: Authority Alignment

Question:

What practical authority does the AI gain in the workflow?

This includes more than explicit automation. It also includes de facto authority through:

- first-pass framing
- ranking or screening
- rationale generation
- approval support
- action triggering

Main failure mode:

- the organization says the human is still in charge, but the workflow gives the model meaningful influence before the human intervenes

### Layer 3: Trust Alignment

Question:

Are users relying on the AI in the right places and for the right reasons?

Main failure mode:

- reliance based on fluency, confidence cues, convenience, or interface sequence rather than demonstrated local reliability

What to evaluate:

- where the model is reliable
- where it is jagged or unstable
- how users interpret confidence and explanation
- whether task structure encourages over-trust or under-trust

### Layer 4: Validation Alignment

Question:

Does the review architecture actually test the output?

Main failure mode:

- symbolic human oversight that fails because generation and validation happen inside the same interface or under the same framing pressure

What to evaluate:

- separation of generation and review
- independent evidence checks
- reviewer expertise
- rationale governance
- escalation and stop conditions

### Layer 5: Policy and Knowledge Alignment

Question:

Is the system constrained to approved policy and knowledge when it acts as a representative of the firm?

Main failure mode:

- the system improvises company policy, customer commitments, legal logic, or HR guidance

What to evaluate:

- grounded access to approved sources
- narrow response scope
- update and change-management process
- explicit refusal and escalation behavior
- logging and auditability

### Layer 6: Commercial Alignment

Question:

Can the system be deployed, sold, approved, and scaled under real institutional conditions?

Main failure mode:

- the system appears technically impressive but cannot pass procurement, regulatory, insurance, or internal governance gates

What to evaluate:

- documentation readiness
- procurement readiness
- assurance and certification needs
- contractual and supplier requirements
- monitoring and evidence collection

## Practical Reading Rule

The six layers should be read as connected rather than separate.

Inference from the evidence:

- problem alignment determines whether AI should enter the workflow at all
- authority alignment determines how much influence it receives
- trust and validation alignment determine whether humans can govern that influence in practice
- policy and knowledge alignment determine whether the system can safely represent the firm
- commercial alignment determines whether the system is institutionally deployable

## Main Research Implications

### 1. Alignment should be studied at the workflow level

The most useful unit of analysis is not the model in isolation. It is the workflow role the model plays.

### 2. Miscalibrated delegation is a better central risk concept than "AI error" alone

Many of the most important business failures will come from badly assigned authority, weak review design, and policy drift rather than from raw model capability alone.

### 3. Policy-facing systems deserve separate treatment

Customer-facing, policy-facing, compliance-facing, and HR-facing systems should not be treated as ordinary chatbot deployments.

### 4. Commercial deployment is part of alignment

If governance, documentation, and assurance determine whether the system can be sold or approved, then commercial deployability is part of the alignment problem rather than an external business issue.

## Sources

- Vaccaro, Michelle, Abdullah Almaatouq, and Thomas Malone. "When combinations of humans and AI are useful: A systematic review and meta-analysis." Nature Human Behaviour, published October 28, 2024. https://www.nature.com/articles/s41562-024-02024-1
- Dell'Acqua, Fabrizio et al. "The Cybernetic Teammate: A Field Experiment on Generative AI Reshaping Teamwork and Expertise." NBER Working Paper 33641, April 2025. https://www.nber.org/papers/w33641
- Agarwal, Nikhil, Alex Moehring, and Alexander Wolitzky. "Designing Human-AI Collaboration: A Sufficient-Statistic Approach." NBER Working Paper 33949, June 2025. https://www.nber.org/papers/w33949
- Gans, Joshua. "A Model of Artificial Jagged Intelligence." NBER Working Paper 34712, January 2026. https://www.nber.org/papers/w34712
- Engel, Sarah, and Kira Duske. "AI Governance in Large-Scale Organizations: Who is Responsible for What?" AMCIS 2025 Proceedings, August 15, 2025. https://aisel.aisnet.org/amcis2025/is_leader/is_leader/1/
- `research/extensions/business-alignment/research-focus.md`
- `research/extensions/business-alignment/incidents/implications-and-immediate-company-needs.md`
- `research/delivery/output/thinktank-report.md`
