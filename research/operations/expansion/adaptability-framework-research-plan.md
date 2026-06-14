# AI-Era Organizational Adaptability — Research Plan

status: research_plan
date: 2026-04-22
purpose: Evolve the author's original "AI-based business decision making" frame into a research program on **organizational adaptability under continuous AI-driven change**. Preserve the three-pillar decomposition (AI usage × organization × technical infrastructure) but reposition decision-making as a sub-function of a higher-order adaptability meta-capability. Produce a self-contained plan that can be executed as research prompts in parallel across assistants and sessions.

---

## 1. Anchor — the author's original research frame

This section is a **first-person declaration** of the frame the author brought into the program, preserved here so that every downstream artifact can trace its lineage.

**Root thesis**: AI-based business decision making requires *both* a technical foundation and an organizational structure. The interest was shaped by consulting work (BCG) where traditional problem-solving repeatedly encountered opportunities that AI-supported decision making could have addressed but was not yet equipped to.

**Two anchor questions — stated together, never separated**
- *Engineering*: **"How is the technical infrastructure for an AI-based decision-making system designed and built?"**
- *Managerial*: **"What operational and governance structures are required for it to function effectively in an organization?"**

**The three-pillar decomposition** (the author's own extension of the two anchor questions)
1. **AI usage framework** — how AI is actually employed inside a decision process
2. **Organizational structure** — how humans should be arranged, which roles, which workflows, which governance
3. **Technical infrastructure** — datacenter / cloud / AI serving architecture / data-plane design

**Academic scaffolding (MIT SDM, 2026–2027)**
- Quantitative base: Introduction to Probability, Fundamentals of Statistics, Modern Mathematical Statistics
- AI & systems: The Analytics Edge, Foundations of Systems I–III, Intro to System Dynamics
- Economics & organization: Economic Analysis for Business Decisions, Business and Operations Analytics, AI / Decision Making / Society, People / Teams / Organizations
- Thesis aim: how AI-based decision infrastructures are adopted and used within organizations

This original frame is the **declared prior** of this plan. Everything that follows is an evolution of it, not a replacement.

---

## 2. Frame evolution — from decision making to adaptability

**The problem the original frame does not fully capture**: the AI environment changes on a monthly cadence. Foundation models, tool surfaces, cost curves, and agent capabilities turn over faster than most decision systems are designed to re-equilibrate. "Building a decision system" assumes a stable target; building it *while the target moves* is a different research object.

**The evolution**
- *From*: AI-based decision making (a static function — inputs, model, governance, output)
- *To*: Continuous adaptability under AI-driven flux (a dynamic meta-capability — sense change, reconfigure the three pillars, redeploy, repeat)
- *Preserved*: the two anchor questions, the three-pillar decomposition, the MIT SDM systems-thinking posture, the dual engineering-managerial framing
- *Newly introduced*: dynamic capabilities (Teece), absorptive capacity (Cohen & Levinthal), ambidextrous organization (O'Reilly & Tushman), organizational learning (Senge, Argyris), resilience engineering (Hollnagel), real options theory for infrastructure decisions, system dynamics (Sterman) applied cross-pillar

**Decision making is not abandoned — it is relocated.** In the adaptability frame, decision making is the *instantaneous output* of a three-pillar system that itself must be continuously redesigned. The research question shifts from "how do we decide well" to "how do we keep the decision-making system fit under change."

**The evolved core question**
> How should the three pillars — AI usage, organization, and technical infrastructure — be jointly reconfigured, on what cadence, by what triggers, with what measurement, so that a knowledge-work organization remains productive amid monthly-scale AI capability turnover?

---

## 3. Research streams and prompts

Eleven prompts in four axes. Each prompt is self-contained so that it can be executed independently in a different assistant, session, or analyst. Each returns an artifact that feeds the final integrative memo.

Time window for all prompts: **2022–2026** primary evidence, with forward-looking extrapolation where explicitly labelled. Geography: global, with emphasis on US, EU, and East Asia.

Evidence posture: cite concrete cases, dates, dollar figures, or engineering-month estimates where possible. Label speculation as speculation. Separate what is *observed* from what is *inferred*.

---

### Axis A — Pillar 1: AI Usage Framework (adaptability lens)

**A1. Foundation model transition management**

> Research how production organizations managed foundation model transitions across 2022–2026 (GPT-3.5 → GPT-4 → GPT-4o → GPT-5; Claude 2 → 3 → 3.5 → 4; Gemini; Llama generations). For at least 10 case studies, extract:
> (a) the trigger that caused a switch of primary LLM,
> (b) the testing / validation pipeline design that gated the switch,
> (c) the switching cost expressed in engineering-months,
> (d) who held decision authority (CTO, product lead, ops lead, risk / compliance),
> (e) failures encountered during or after the switch.
> Synthesize a decision framework — *when to swap* vs. *when to stay* — calibrated to application criticality, regulatory posture, and the capability gap between models. Output: a decision tree plus a calibrated case table.

**A2. Capability-to-adoption lag curves**

> Quantify the lag between a new AI capability's public release and its enterprise production adoption for 2022–2026. For each major capability wave — function calling, vision, long context, reasoning (o1-class), agents, computer use, inference-time scaling, multimodal generation — measure:
> (a) release → first public enterprise production deploy,
> (b) release → 50% enterprise adoption,
> (c) release → commoditization (price collapse or open-weight parity).
> Source: vendor case studies, Stripe / a16z / OpenAI public data, enterprise surveys (IDC, Gartner, S&P), public financial disclosures. Output: a capability-adoption velocity chart and a discussion of accelerators and decelerators (compliance, integration surface, change management, ROI visibility).

**A3. Workflow retooling patterns across knowledge-work domains**

> Identify the organizational patterns by which knowledge-work domains rebuilt their daily workflows as AI capabilities shifted. Target domains:
> - Legal (contract review, due diligence)
> - Medical (clinical documentation, imaging)
> - Finance (equity research, compliance, underwriting)
> - Software engineering (coding agents, code review, test generation)
> - Consulting and knowledge services (analysis, decks, memos)
> For each domain across 2023–2026: (a) how workflows were redesigned, (b) big-bang migration vs. continuous integration approach, (c) role of AI champions, centers of excellence, or external vendors, (d) retooling velocity and rework cost. Extract patterns that transfer across domains and patterns that are domain-locked.

---

### Axis O — Pillar 2: Organizational Structure (adaptability lens)

**O1. Human-AI collaboration model evolution at AI-forward firms**

> Trace how leading AI-native and AI-forward organizations restructured human-AI collaboration across 2023–2026. Candidate firms:
> Shopify, Klarna, Stripe, Palantir, Anthropic, OpenAI, Perplexity, Cognition, Harvey, Sierra, Cursor, Replit, McKinsey QuantumBlack, Bain, BCG X.
> For each: team composition shifts, reporting structure changes, hiring profile shifts, promotion criteria changes, layoffs attributed to AI, founder / CEO public positioning.
> Identify which collaboration models proved resilient across capability shifts versus which required frequent redesign. Distinguish substantive restructuring from public-relations restructuring.

**O2. Role redefinition cycles and triggers**

> Research how often, and under what triggers, organizations formally redefine roles in response to AI change. Triggers to track:
> capability release, price collapse (10× cost drop), competitor move, board / investor pressure, cost-cutting initiative, regulatory change.
> Produce concrete examples 2023–2026 of roles:
> (a) created — AI ops, model evaluator, prompt engineer, forward-deployed engineer, AI product manager, chief AI officer, etc.
> (b) eliminated or consolidated,
> (c) merged or redefined without being formally renamed.
> Distinguish structural change from rebranding. Output: a role-life-cycle model for AI-era knowledge work, with typical durations from creation to obsolescence.

**O3. Organizational learning velocity under tool flux**

> Investigate which knowledge-management and internal-learning systems *survive* when AI tools turn over every three months. Evidence to gather: internal documentation practices, training program cadence, prompt / playbook library maintenance cost, cross-team learning mechanisms (guilds, AMAs, internal forums), onboarding velocity for AI tools. Connect findings to:
> - Senge's learning organization,
> - Cohen & Levinthal's absorptive capacity,
> - Argyris's single-loop vs double-loop learning,
> - March's exploration-exploitation,
> - Nonaka's tacit-explicit knowledge spiral.
> Identify what *breaks* when tooling changes (stale documentation, abandoned prompt libraries, skill atrophy) and which structures are tooling-invariant. Output: a maturity model for AI-era organizational learning.

---

### Axis T — Pillar 3: Technical Infrastructure (adaptability lens)

**T1. Build vs. rent decision framework under model flux**

> Build a decision framework for AI infrastructure choices — API vs. self-hosted, proprietary vs. open-weight (Llama, Qwen, DeepSeek, Mistral), cloud vs. on-prem vs. hybrid, single-provider vs. multi-provider routing — that remains valid when the underlying model generation turns over every 6–12 months.
> For 2024–2026, document: (a) 10+ case studies of companies that switched strategies and their stated rationale, (b) total cost of switching (engineering-months, downtime, quality regression), (c) which architectural decisions held up through GPT-5 / Claude 4 releases and which required rewrite.
> Output: a decision tree parameterized by company size, regulatory posture, capability requirement, latency / cost constraint, and data-sensitivity tier.

**T2. Compute scaling under 10×/18-month demand growth**

> Analyze how non-frontier organizations adapted to AI inference compute growing roughly 10× every 18 months across 2023–2026. Subjects:
> (a) mid-size AI product companies (Notion, Linear, Cursor, Replit, Perplexity, Harvey, Sierra) scaling inference,
> (b) emergence of inference-optimized providers and hardware (Groq, Cerebras, AWS Trainium / Inferentia, Fireworks, Together, Baseten, Modal),
> (c) cost / latency / throughput frontier curves and how they shifted,
> (d) multi-provider routing and fallback strategies under incident and price-shock conditions.
> Identify what breaks at 10k QPS that worked at 100 QPS, and which architectural decisions compound versus require rewrite. Output: scaling-phase transition map with architectural milestones.

**T3. Technical debt in AI-native systems**

> Investigate technical debt patterns in AI systems when the underlying model / API changes quarterly across 2023–2026. Focus areas:
> (a) prompts-as-code — versioning, regression testing, canary deploys, rollback,
> (b) RAG pipeline maintenance as embedding models and chunking strategies evolve,
> (c) evaluator drift — how LLM-as-judge setups degrade and require reweighting,
> (d) observability and monitoring for LLM apps (Arize, LangSmith, Braintrust, custom),
> (e) fine-tune / adapter lifecycle and its interaction with base-model version changes.
> Sources: engineering blogs from Anthropic, OpenAI, Shopify, Klarna, Harvey, LangChain / LlamaIndex users, post-mortems.
> Output: a taxonomy of AI-system technical debt by whether it compounds, self-resolves, or resolves only through deliberate remediation — with maintenance-cost curves.

---

### Axis M — Meta: Cross-Pillar Integration

**M1. Systems-dynamics map of the three-pillar adaptability problem**

> Apply MIT SDM / system dynamics framing to the three-pillar adaptability challenge (AI usage × organization × technical infrastructure). Construct:
> (a) causal loop diagram of reinforcing and balancing feedback between pillars,
> (b) delays that produce organizational pathologies — e.g., infrastructure built for last year's model, team structure outliving the capability shift that created it,
> (c) stocks and flows — talent, tooling, data assets, capability debt, trust debt,
> (d) identifiable leverage points in the sense of Meadows.
> Connect to: Teece's dynamic capabilities, O'Reilly–Tushman ambidextrous organization, Hollnagel's resilience engineering, Beer's viable system model, Christensen's disruption theory.
> Output: a testable system-dynamics model of three-pillar coupling under AI flux, with named feedback loops and proposed interventions.

**M2. Measurable indicators of AI-era organizational adaptability**

> Design measurable indicators of AI-era adaptability and benchmark them across published cases 2023–2026. Candidate indicators:
> - capability-to-deployment lag (days from public release to production integration)
> - model-switching cost (engineer-days per major swap)
> - role redefinition frequency (formal role changes per 1000 FTE per year)
> - technical-debt accrual rate in AI subsystems (story points, backlog growth)
> - revenue share from AI capabilities released < 6 months ago
> - time-to-workflow-redesign after capability shock
> - adaptation-to-overcorrection ratio (changes that were reversed within 12 months)
> For each indicator: data-source feasibility, measurement method, industry benchmarks, construct validity, and known gaming risks.
> Output: a 5–7-indicator adaptability dashboard specification with reference ranges for small / mid / large organizations.

---

## 4. Execution notes

**Parallelization**: each prompt is independent and self-contained. They can be run in parallel in different assistants, sessions, or by different analysts. No prompt depends on the output of another at the fact-gathering stage. Integration happens only at the memo-synthesis stage.

**Output shape per prompt**: a standalone memo with (i) method, (ii) evidence table, (iii) pattern findings, (iv) open questions, (v) how the finding feeds the three-pillar adaptability frame.

**Evidence hygiene**:
- separate *observed* facts (with citation) from *inferred* interpretation;
- label confidence where claims differ in strength (high / medium / low or weak / moderate / strong);
- record negative evidence (what was looked for but not found) — it is load-bearing for this frame;
- convert relative dates to absolute dates (e.g., "last year" → "2025").

**Language**: English throughout. No emojis.

**Final integrative artifact**: after all eleven prompts produce their memos, a single synthesis memo will stitch them into the three-pillar adaptability framework and tie back to the MIT SDM coursework structure in Section 1. That synthesis memo is the candidate for promotion from `research/operations/expansion/` to `research/extensions/adaptability-framework/` as a new extension track parallel to `scale-based/` and `healthcare-bio-ai/`.

**Relation to adjacent tracks**:
- *Reasoning trust verification*: re-positioned as a Pillar 1 sub-capability — "trust-calibrated AI usage is a prerequisite for safely swapping models under the A1 framework."
- *Scale-based decomposition*: adaptability varies by scale tier — S7 international firms adapt by capital and coordination, S1 solo operators adapt by speed and tool choice. Prompts should report scale-tier effects where visible.
- *Healthcare and bio AI*: regulated domains are a stress test of the adaptability frame — the O3 learning-velocity and T3 technical-debt analyses should specifically include regulated-domain cases.
- *Kaggle × freelance talent-market restructuring* (prior plan): re-categorized as an **empirical case data feeder** to M1 and M2, supplying top-end (Kaggle) and mass-market (freelance) talent-market adaptation signals rather than being pursued as an independent track.

**Scope guardrails**:
- do not pursue prescriptive "best practice" claims without a mechanism argument;
- do not collapse the three pillars into one another — their coupling is the research object, not a bug to be engineered away;
- do not abandon the anchor questions from Section 1 — every prompt must ultimately feed back to the engineering question or the managerial question (or, in the case of M1 / M2, to both).

---

## 5. First-pass priority ordering (suggested, not fixed)

If prompts must be executed sequentially rather than in parallel, suggested ordering:

1. A2 (capability-adoption lag curves) — calibrates the clock the rest of the plan runs on
2. T1 (build vs. rent) — defines the infrastructure decision surface
3. O2 (role redefinition cycles) — defines the organizational decision surface
4. A1 (model transition management) — operationalizes A2 into a decision framework
5. T3 (technical debt) — quantifies the cost of infrastructure decisions from T1
6. O1 (human-AI collaboration evolution) — enriches O2 with firm-level patterns
7. A3 (workflow retooling by domain) — tests A1 / A2 patterns across domains
8. T2 (compute scaling) — scenario stress test for T1 / T3
9. O3 (organizational learning velocity) — integrates O1 / O2 into learning theory
10. M1 (systems-dynamics map) — first synthesis pass
11. M2 (adaptability indicators) — turns the synthesis into measurement

Priority is not prescriptive. If a collaborator picks up an individual prompt, they can run it without blocking on any other.
