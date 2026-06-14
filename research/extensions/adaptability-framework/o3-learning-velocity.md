# O3 — Organizational Learning Velocity Under Tool Flux

axis: O (Pillar 2 — Organizational Structure)
date: 2026-04-22
plan: research/operations/expansion/adaptability-framework-research-plan.md

---

## 1. Method

**Question.** When AI tools turn over on a roughly three-month cadence — new model generations, new tool surfaces (function calling, vision, long context, computer use, agents), deprecated endpoints, renamed SDKs, shifting pricing — which internal learning systems keep producing useful knowledge, and which decay into archaeology?

**Evidence posture.** This memo was produced under *training-knowledge-only conditions* for this session (no live web retrieval). Claims are labelled:
- **O** — observed (public engineering blog, practitioner podcast, survey, regulatory filing, public announcement)
- **I** — inferred (pattern extended from observed cases, or derived from first principles)
- Confidence: **high / medium / low** on each pattern claim
- Absolute dates are preserved (e.g., "2024-10") rather than relative ("last year")

**Sources leaned on.** Public engineering blogs (Shopify, GitHub, Stripe, Anthropic, OpenAI, Klarna, Intercom, Zendesk, Harvey, Palantir); practitioner writing on KM (Lenny's Newsletter, a16z portfolio posts, McKinsey / BCG X playbooks, MIT Sloan Management Review, HBR); academic organizational learning literature (Senge 1990; Cohen & Levinthal 1990; Argyris 1977/1991; March 1991; Nonaka 1994); and regulated-domain trade publications (NEJM AI editorials, Law.com, AICPA / FINRA guidance). Healthcare / legal / finance cases are flagged because of their asymmetric stakes under Section 6.

**Boundary.** This memo is about *learning systems*, not performance outcomes. A firm can have exquisite documentation and still miss a model transition; it can also ship 40% Copilot-authored code with barely any formal training program (GitHub 2024). The memo isolates the *learning scaffolding* and asks which parts of it survive tool flux.

---

## 2. Evidence table — observed learning-system practices

Ten rows plus four regulated-domain rows. Each column is a lever that tool flux stresses. Sources are inline-cited; uncertain datapoints are marked **I** with a confidence tag.

| # | Firm / setting | Documentation cadence | Training program cadence | Prompt / playbook library maintenance | Cross-team learning (guilds, AMAs, forums) | AI-tool onboarding time-to-productivity | Source / note |
|---|----------------|-----------------------|--------------------------|---------------------------------------|---------------------------------------------|-----------------------------------------|---------------|
| 1 | **Shopify** | Living `dev.shopify` internal wiki; public "AI usage is table stakes" memo (Tobi Lütke, 2025-04) mandates AI literacy as a performance dimension | Continuous; AI literacy embedded in onboarding and review cycles (**O**, 2025) | Internal prompt / playbook libraries maintained by Ops and a cross-functional enablement team (**I**, medium) | Internal Slack channels, merchant-facing demo Fridays; "Shopify Magic" product team doubles as internal guild (**O**) | Claimed ~days for generic tools, weeks for domain-specific (Magic, Sidekick) (**I**, medium) | Lütke memo 2025-04; Shopify engineering blog |
| 2 | **Klarna** | Public disclosure of AI customer-service agent handling 2.3M conversations in first month (2024-02); later 2024-09 partial reversal hiring human agents back | Retrained CS ops after partial reversal; training cadence accelerated post-incident (**O**) | Prompt library initially owned by a small AI team; maintenance cost cited publicly as a reason for the partial reversal (**O**, medium — exact figure not disclosed) | Earnings-call disclosure became the main cross-team learning surface (unusual) | Fast for tool rollout, slow for quality recovery (**I**, high confidence the reversal happened; low on internal mechanics) | Klarna press release 2024-02; Bloomberg coverage 2024-09 |
| 3 | **Intercom / Fin AI** | Product changelog tightly versioned; "resolution rate" metric publicly reported and updated quarterly (**O**) | Customer-facing: continuous webinars; internal: Fin Eval team documents regressions each release (**I**, medium) | Playbooks (resolution paths) are *data assets*, not static prompts; maintained via conversation-log replay (**O**) | Public podcast circuit (Des Traynor et al.) acts as external learning surface; doubles as internal alignment device (**O**) | Fin onboarding ~weeks at mid-market; longer at enterprise (**I**, medium) | Intercom blog; Traynor podcast 2024 |
| 4 | **Zendesk** | Post-Klaviyo-era KB; tool churn well documented after 2023 AI Copilot launch and 2024 pricing-model controversy (outcome-based pricing) (**O**) | Partner-led training for enterprise; internal CX enablement team (**O**) | Multi-tenant prompt infrastructure; customer-configurable means each tenant maintains a library fragment — maintenance is partially externalized (**I**, medium) | Partner Slack, Community Discourse forum (**O**) | Long — pricing/config complexity dominates over model complexity (**I**, medium) | Zendesk blog 2024; TechCrunch coverage 2024-09 |
| 5 | **GitHub (Copilot)** | Copilot docs versioned with product; 2024 "Copilot Workspace" launch forced re-doc (**O**) | GitHub Universe annual + monthly "Copilot for Business" webinars; bootcamp programs for enterprise customers (**O**) | Few internal "prompts" — Copilot's learning surface is the model + editor integration, not a prompt library (**O**, high) | Internal "AI guild" since at least 2022; cross-pollinates with Azure AI team (**I**, medium) | Individual developer: hours. Enterprise rollout: 3–9 months for policy, security, and SSO (**O** at the enterprise end from ChangeLog 2024 ep.) | GitHub blog; ChangeLog podcast 2024 |
| 6 | **Stripe** | Rigorous internal engineering docs; Stripe Press culture of written memos carries into AI projects (**O**) | 2023-2024 rolled out internal LLM tools for docs search, support triage; training framed as "Stripe operating principles" rather than tool-specific (**I**, medium) | Prompt library lives as code in a monorepo; versioned with tests (**I**, medium, extending Stripe's general engineering culture) | Classic Stripe "Sessions" and internal tech-talk cadence; AI adaptations continue it (**O**) | Fast for core engineers (days); slow for sales / support tooling (weeks–months) (**I**, medium) | Stripe engineering blog; John Collison interviews 2024 |
| 7 | **Anthropic** | Public — Claude's system prompt published (2024-08 onward), model cards, Responsible Scaling Policy updates (**O**) | Internal: strong norm of written memos; structured onboarding for Applied / policy / research tracks (**I**, medium) | Prompt engineering treated as first-class skill; maintained playbooks around tool use, agent design, constitutional AI methods (**O**, inferred from published materials) | Strong "Internal AMA" + written-memo culture; public comms (blog, papers) double as internal alignment (**I**, high) | Fast for generic usage; model-behavior internalization takes longer (**I**, medium) | Anthropic blog; Amodei public interviews 2024 |
| 8 | **OpenAI** | Spec docs (Model Spec 2024-05, updated 2025) publicly published; internal docs leak-prone but visible through them (**O**) | Continuous; Dev Day (2023, 2024) functions as external training event, internal dogfooding precedes it (**O**) | Playbook library: OpenAI Cookbook (GitHub, public) is also a de facto internal reference (**O**, high) | Internal AMAs; Research/Applied division separation creates a guild-like friction surface (**I**, medium) | Applied teams: weeks. Research-to-product translation: often slower than capability arrival (**I**, medium) | OpenAI Model Spec 2024-05; Cookbook repo |
| 9 | **Deloitte / Accenture / BCG X (consulting CoE model)** | Central AI CoE publishes quarterly or monthly practitioner playbooks; internal "AI Academy" type programs (BCG Henderson, Deloitte AI Academy, Accenture LearnVantage) (**O**) | Quarterly cycles; mandatory certifications; "AI fluency" as a competency tier (**O**) | Playbook libraries built to scale across hundreds of engagements; central governance + local adaptation (**O**) | Cross-office guilds; internal conferences; partner-level AI leads (**O**) | Onboarding: week-long bootcamp + shadow engagement; ~30–60 days to billable AI-augmented work (**I**, medium; varies by firm) | BCG / Deloitte / Accenture public materials 2024-2025 |
| 10 | **McKinsey (QuantumBlack + Lilli)** | Internal "Lilli" assistant onboarded 2023-2024 on McKinsey's proprietary knowledge base (~100k documents); version-controlled (**O**) | Lilli itself is a training lever; analysts onboard by using it on real work (**O**) | Prompt library embedded in Lilli's product surface; central team maintains (**I**, medium) | QuantumBlack internal network; firm-wide AI forum (**I**, medium) | Analyst onboarding to Lilli: days; to full AI-augmented consulting output: months (**I**, medium) | McKinsey public posts on Lilli 2023-2024 |
| 11 | **Harvey (legal AI, vertical)** | Customer-specific workspaces; docs / training tied to each law-firm deployment (**O**, from public case studies with Allen & Overy, PwC, A&M) | Firm-embedded training sprints; Harvey Labs team works on-site (**O**) | Prompt / workflow library per firm; maintenance partially by Harvey, partially by law-firm innovation team (**I**, medium) | Harvey-run customer council; firm-level internal AI committees (**I**, medium) | 2-3 months to measurable partner-hour savings per firm (**I**, medium) | Harvey case studies 2023-2024 |
| 12 | **Epic Systems / hospital deployments (healthcare)** | Epic AI features (ambient notes, inbox draft replies) gated by per-site governance committees; docs maintained by site IT + Epic (**O**) | Site-led training; CMIO / CNIO role is the training lever (**O**) | Prompt customization limited; Epic controls most of the prompt surface, sites control configuration (**I**, high) | ACMIO network; KLAS user groups; AMIA conferences as external learning surface (**O**) | Ambient scribe onboarding: 2-6 weeks per physician for stable usage patterns (**I**, medium, from Kaiser / Permanente / UCSD public statements 2024) | NEJM AI 2024; KLAS 2024 reports |
| 13 | **Big Four audit AI (finance / audit)** | Heavily governed; documentation tied to audit-quality standards and PCAOB oversight (**O**) | Annual mandatory AI training; cadence slower than tech firms due to compliance overhead (**O**) | Playbook library versioned with methodology releases; maintenance cost high because of documentation-for-auditor requirements (**I**, high confidence that cost is high; medium on the exact mechanism) | Internal AI practice leadership councils; external AICPA working groups (**O**) | New-hire onboarding: weeks on tool literacy, months on methodology integration (**I**, medium) | AICPA AI guidance 2024-2025; PCAOB remarks 2024 |
| 14 | **FINRA-regulated broker-dealers (finance)** | Model Risk Management (MRM, SR 11-7 lineage) documentation extended to LLMs; often quarterly reviews (**O**) | Compliance-led training; MRM teams embedded as "second line" (**O**) | Prompt / system-prompt libraries subject to MRM; change control mandatory (**O**) | Internal AI governance councils; industry working groups (SIFMA, ISDA AI initiatives) (**O**) | Slow — weeks to months for any production-facing AI tool to complete MRM cycle (**I**, high) | SR 11-7 (2011 origin); FINRA 2024 AI notices |

Sources flagged **I** are inferences — they extend a publicly known firm practice to the specific learning lever without direct disclosure. They are kept at medium confidence unless explicitly marked high.

---

## 3. What breaks under tool flux — categorized failure modes

Each failure mode is described with its mechanism, an observed or inferred example, and what *re-*breaks each time tools turn over (the recurrence cost).

### 3.1 Stale documentation (high confidence, high recurrence)
- *Mechanism*: documentation writes lag tool changes. When a model is deprecated or an SDK method is renamed, examples and code snippets inside internal wikis go stale in days, not quarters.
- *Observed*: OpenAI SDK migrations (Python v0 → v1 in 2023, and subsequent Responses API vs. Chat Completions duality in 2024–2025) broke every internal tutorial that had hard-coded `openai.ChatCompletion.create(...)` across thousands of enterprise repos (**O**, observed through public migration guides and mass engineering-blog chatter).
- *Recurrence*: every SDK version bump.

### 3.2 Abandoned prompt libraries (high confidence, high recurrence)
- *Mechanism*: prompts written for an older model (GPT-3.5, Claude 2) exploit that model's quirks. New models ignore or misinterpret them; the library becomes a liability.
- *Observed*: widespread reports on practitioner Discords (LangChain, LlamaIndex communities, 2023-2024) of "prompt graveyards" accumulated during the GPT-3.5 → GPT-4 → GPT-4o transition. Klarna's 2024-09 reversal likely implicates a variant (**I**, medium).
- *Recurrence*: each major model generation; worse when a firm has multiple applications with copy-pasted prompt patterns.

### 3.3 Eval drift (medium-high confidence)
- *Mechanism*: eval sets calibrated against old model failures lose discriminative power when models improve; LLM-as-judge setups inherit judge-model biases that drift under judge upgrades.
- *Observed*: Anthropic, OpenAI, and multiple vendor blogs (Braintrust 2024, LangSmith 2024) publicly discuss evaluator drift as a first-class problem. Harvey's published 2024 eval posts emphasize periodic eval re-calibration (**O**).
- *Recurrence*: continuous. Arguably the largest silent cost center.

### 3.4 Skill atrophy (medium confidence)
- *Mechanism*: when AI tools produce first drafts, humans stop practicing the underlying skill; when the tool then underperforms (new model regression, outage, regulatory restriction), the human capability has eroded.
- *Observed / debated*: 2023-2025 studies on "cognitive offloading" (Gerlich 2025 among others) and anecdotal engineering reports of juniors who can't read unfamiliar code without Copilot (**O**, widely discussed; mechanism contested). Not yet proven at organizational scale.
- *Recurrence*: accumulates over years rather than quarters; but any single model regression exposes the gap.

### 3.5 Orphaned integrations (high confidence)
- *Mechanism*: one-off custom integrations (bespoke prompts inside a Zapier flow, an old function-calling schema, a retired vendor plug-in) survive because no one owns them; they break silently when upstream APIs change.
- *Observed*: OpenAI Plugins (2023-Q2) to GPTs (2023-Q4) to Assistants v1 (2024) to Responses API (2024-Q4) — each transition orphaned integrations built on the predecessor (**O**).
- *Recurrence*: each platform-level turnover; compounds with time-since-last-audit.

### 3.6 Onboarding lag at model turnover (medium confidence)
- *Mechanism*: new hires onboarded on the previous tool stack; by the time they are productive, the stack has moved.
- *Observed*: Shopify Lütke memo (2025-04) explicitly aims to compress this loop by making AI literacy a continuous requirement rather than an onboarding milestone (**O**, interpreted).
- *Recurrence*: each quarterly intake cohort.

### 3.7 Playbook fossilization (medium confidence)
- *Mechanism*: a successful playbook (e.g., Klarna's AI CS resolution flow) becomes policy; subsequent context shifts (new model, new regulation, new customer mix) do not trigger revision.
- *Observed*: Klarna's 2024-02 to 2024-09 arc is the canonical example (**O**). Many consulting-CoE playbooks carry the same risk (**I**, medium).
- *Recurrence*: episodic; tied to governance cadence rather than tool cadence.

### 3.8 Guild decay (medium-low confidence)
- *Mechanism*: internal guilds / CoPs staffed by early AI champions disband or lose seniority once the novelty passes; institutional memory scatters.
- *Observed*: generic pattern in OL literature (Wenger on communities of practice, 1998); specific AI-era disbandments are not yet publicly catalogued at scale (**I**, low-medium).
- *Recurrence*: slow; primarily tied to internal mobility and reorgs.

---

## 4. What survives — tooling-invariant structures

These are the practices that, across the evidence table and failure modes, keep producing usable knowledge regardless of whether the underlying tool turns over in three months or twelve.

### 4.1 Written-memo culture (high confidence)
- *Why tooling-invariant*: memos capture reasoning about the problem, not syntax of the tool. A Stripe or Anthropic memo arguing *why* a prompt should do X survives even when the prompt itself is obsolete.
- *Examples*: Stripe operating principles; Anthropic internal memo culture (inferred from public writing output); Amazon's six-pager tradition extended to AI use cases (**O / I**).
- *Stress test passed*: memo archives remain useful after a model generation; prompt archives often do not.

### 4.2 Evaluation harnesses as the durable artifact (high confidence)
- *Why tooling-invariant*: the eval set (inputs, expected behaviors, rubrics) encodes *what the organization cares about*. New models and prompts are plugged into the same harness. The harness is more durable than what it tests.
- *Examples*: Harvey's published eval approach (2024); Anthropic / OpenAI internal eval suites; enterprise Braintrust / LangSmith customers (**O**).
- *Caveat*: evals themselves drift (Section 3.3), but the *harness* and the *rubric philosophy* survive; the test cases inside require refresh.

### 4.3 Learning in public (medium-high confidence)
- *Why tooling-invariant*: external blog posts, podcast appearances, and conference talks double as *forcing functions for internal clarity*. The act of publishing externalizes tacit knowledge at a cadence the tools can't outpace.
- *Examples*: Anthropic's alignment papers; Stripe Press; Intercom's Traynor podcast; Shopify's public commentary; the OpenAI Cookbook (**O**).
- *Mechanism*: Nonaka's tacit-to-explicit step is executed as a side effect of external communication.

### 4.4 Eval-as-onboarding (medium confidence)
- *Why tooling-invariant*: new hires who learn the evals — even before they learn the current prompts — inherit the firm's quality bar. When tools turn over, the hire is already aligned to "what good looks like" independent of the obsolete tool.
- *Examples*: Harvey customer-firm onboarding; inferred at Anthropic/OpenAI applied teams; McKinsey Lilli as a learning surface (**I**, medium).
- *Mechanism*: Cohen-Levinthal absorptive capacity is effectively pre-loaded at day one.

### 4.5 Guilds keyed to *problem domain*, not *tool* (medium-high confidence)
- *Why tooling-invariant*: a "customer-support AI" guild outlives the specific model it started with; a "GPT-4 guild" dies when GPT-4 dies.
- *Examples*: Epic's CMIO / CNIO networks (decades-stable, adapts to ambient-scribe era); Big Four AI practice councils keyed to *audit domain* (**O**); Shopify's merchant-success enablement teams (**I**, medium).

### 4.6 Change-logs and "what-changed" rituals (high confidence)
- *Why tooling-invariant*: a disciplined weekly or monthly write-up of what changed externally (new model, deprecated endpoint, new capability) plus what the firm did about it accumulates as a *diff log* across the tool-flux timeline.
- *Examples*: Anthropic, OpenAI, and many mid-size AI companies maintain internal changelogs. Intercom, Shopify, and Stripe's product release notes play the same role externally (**O / I**).
- *Mechanism*: Argyris double-loop learning — the log is where assumptions about the tool landscape get surfaced and revised.

### 4.7 A role that owns "AI fluency of the firm" (medium confidence)
- *Why tooling-invariant*: the *role* — Chief AI Officer, Head of AI Enablement, AI Practice Partner — persists across tool generations even as its specific agenda rotates. The absence of such an owner correlates with library abandonment and stale docs.
- *Examples*: Accenture CAIO (from 2023); Deloitte AI leadership; Palantir FDE role (forward-deployed engineer, an older construct now applied to AI); McKinsey's QuantumBlack leadership (**O**).

### 4.8 Continuous training *cadence*, not fixed curricula (medium-high confidence)
- *Why tooling-invariant*: organizations that fix a curriculum (say, a 2023 "ChatGPT for marketers" course) ossify. Organizations that fix a *cadence* (monthly AI fluency update, quarterly certification refresh) keep content fluid.
- *Examples*: Shopify's continuous model (2025); consulting CoEs' quarterly certification cycles; Microsoft's annual mandatory AI training modules (**O / I**).

---

## 5. Theoretical mapping

For each framework, 2-4 bullets on what AI-era tool flux stresses or validates.

### 5.1 Senge — learning organization (five disciplines: systems thinking, personal mastery, mental models, shared vision, team learning)
- *Validation*: systems thinking is elevated from discipline to survival requirement. Firms that do not see the whole stack (model × prompt × eval × workflow × user) are the ones whose prompt libraries are abandoned.
- *Stress*: "personal mastery" is destabilized when the tool that enabled the mastery disappears. The mastery target becomes a moving object — mastery shifts from "knowing this tool deeply" to "knowing how to re-learn tools quickly."
- *Practical implication*: team learning rituals (guilds, AMAs) that focus on *meta-skills* (how we learn) beat those that focus on *current tool tricks*.
- *Evidence link*: Section 4.5 (problem-domain guilds) and 4.8 (continuous cadence) are the Senge-aligned survivors.

### 5.2 Cohen & Levinthal — absorptive capacity
- *Validation*: firms with prior investment in related knowledge (ML engineering, data science, software rigor) absorb each new model capability faster. Absorptive capacity compounds, consistent with the 1990 thesis.
- *Stress*: the *boundaries* of "related knowledge" shift each quarter. Prior ML expertise helps with evals but may not help with agent orchestration or multimodal UX. Absorptive capacity is now a portfolio, not a monolith.
- *Mechanism*: the firm's "R&D intensity" analogue is *eval-engineering intensity*. Firms that invest in evals, telemetry, and written reflection have more absorptive bandwidth.
- *Evidence link*: Sections 4.2 (eval harness) and 4.4 (eval-as-onboarding).

### 5.3 Argyris — single-loop vs double-loop learning
- *Validation*: the distinction is sharpened. Updating a prompt when an output is wrong is single-loop; revisiting whether the *task should be AI-done at all* is double-loop. Klarna's 2024-02 to 2024-09 arc is a canonical case of double-loop learning being forced by external results.
- *Stress*: tool flux tempts firms into continuous single-loop adjustment (rewrite the prompt, swap the model) and starves the double-loop review.
- *Practical implication*: organizational designs that schedule double-loop reviews (quarterly "should we still be doing this?" sessions) survive better than those that only handle escalations.
- *Evidence link*: Section 3.7 (playbook fossilization) is a double-loop failure; Section 4.6 (change-log rituals) is a double-loop survivor.

### 5.4 March — exploration vs. exploitation (1991)
- *Validation*: the exploration-exploitation tradeoff is sharpened to a weekly decision. Exploring new models costs engineering-weeks; exploiting the known-good stack risks obsolescence.
- *Stress*: under tool flux, "exploitation" has a shorter half-life than ever. Classic March equilibria assume exploitation is relatively stable; the AI era makes exploitation a decaying asset.
- *Stress*: ambidextrous designs (O'Reilly-Tushman) must separate *exploration teams* (evaluators, research engineering) from *exploitation teams* (productionizers) so that exploration is not starved by on-call pressure.
- *Evidence link*: Section 4.7 (AI fluency ownership) is the structural mechanism; consulting CoE model (Row 9) is the practical example.

### 5.5 Nonaka — SECI / tacit-explicit knowledge spiral (socialization, externalization, combination, internalization)
- *Validation*: "learning in public" (Section 4.3) is a textbook Nonaka externalization move at organizational scale.
- *Stress*: socialization (tacit-to-tacit via co-work) is disrupted when the tool that enabled co-work changes quarterly. A pair-programming ritual built around Copilot 2023 is a different ritual from one built around agentic Copilot 2024.
- *Observation*: AMAs and guilds are the externalization and combination loops that survive; the socialization loop is the most fragile under flux.
- *Practical implication*: firms should treat Nonaka's socialization step as a *designed* activity, not an emergent one, because the tools won't do it for them.
- *Evidence link*: Section 3.8 (guild decay) is a socialization failure; Section 4.3 (learning in public) is externalization-as-survivor.

---

## 6. Maturity model — AI-era organizational learning

Five levels. Criteria are *observable* — an outside reviewer or auditor could score them without privileged access beyond typical KM artifacts (wikis, run-books, training records, retro docs).

### Level 1 — Ad hoc
- No owner of AI learning; individual contributors experiment.
- Prompts shared via Slack screenshots or DMs.
- No written onboarding for AI tools; "ask the one person who figured it out."
- No eval harness; judgements made per-output.
- Documentation is written once at launch, never updated.
- *Failure signature*: every tool turnover produces a visible productivity regression; nobody can say why the old flow worked.

### Level 2 — Reactive
- One champion or small team curates a prompt library.
- Training happens ad hoc, usually in response to incidents.
- Documentation updated when something breaks badly enough to force it.
- Evals exist but are not versioned; they drift silently.
- Internal forum / Slack channel exists; activity follows incidents.
- *Failure signature*: library becomes stale between incidents; the champion burns out or moves on and the library dies.

### Level 3 — Structured
- Named role or team owns AI enablement (CoE, AI fluency lead, or AIO).
- Prompt / playbook library is versioned, reviewed quarterly.
- Training has a fixed cadence (e.g., monthly webinars, quarterly certifications).
- Eval harnesses exist, are run on each change, and are refreshed on a schedule.
- Cross-team guild meets on a regular cadence with minutes archived.
- Onboarding includes a standardized AI-tools module; time-to-productivity is measured.
- *Survival under flux*: withstands model generation changes; still bruised by capability-level shifts (e.g., arrival of agents, computer use).

### Level 4 — Adaptive
- Eval harness is treated as the durable artifact; prompts and models are plugged in and out.
- Documentation is continuous — every tool change triggers a diff log and owner-assigned updates.
- Change-log ritual is scheduled (weekly or biweekly) with named owners.
- Training cadence tracks the tool flux clock rather than an annual HR cycle.
- Double-loop retrospectives scheduled (quarterly) — "should we still be doing this at all?"
- Guilds are keyed to problem domain (customer support, legal research) rather than specific tools.
- Onboarding begins with eval walkthrough, then tool walkthrough (eval-as-onboarding).
- *Survival under flux*: handles capability-level shifts; stressed only by paradigm shifts (non-LLM world, regulatory shock).

### Level 5 — Anti-fragile
- Every tool change is treated as a learning trigger; the organization *gets better* from flux rather than merely surviving it.
- "Learning in public" is a stated expectation — external blog posts, conference talks, podcast appearances per team per quarter.
- Double-loop reviews drive the roadmap, not just the operations cadence.
- Exploration team and exploitation team are structurally separated (ambidextrous); rotation between them is deliberate and tracked.
- Skill atrophy actively monitored (periodic "AI-free drills" to keep fundamentals alive).
- Regulated-domain variants maintain MRM-equivalent governance without sacrificing velocity — the MRM process itself is continuously refined based on near-miss telemetry.
- *Survival under flux*: handles paradigm shifts by design; the scaffolding converts novelty into institutional advantage.

**Diagnostic hint.** The level of a firm is most reliably identified by asking *"what happened the last time a model deprecation email arrived?"* Level 1 firms did not notice. Level 2 had a fire drill. Level 3 followed a runbook. Level 4 updated a diff log and kept going. Level 5 wrote a public post-mortem that competitors learned from.

---

## 7. Open questions and negative evidence

### 7.1 Negative evidence — what was looked for but not found
- **Regulated-domain "anti-fragile" cases.** Healthcare and finance cases cluster at Levels 2-3. No clear Level 5 example surfaced in the training window — governance overhead keeps velocity structurally lower. *Open*: whether "anti-fragile under regulation" is possible or whether it is a category error.
- **Empirical cost curves for prompt library maintenance.** Practitioners discuss the cost qualitatively (Klarna's reversal, LangChain community chatter); rigorous time-study data is rare. *Open*: what does it cost per 1000 prompts per model generation?
- **Skill atrophy measured longitudinally.** The 2023-2025 literature is mostly cross-sectional or anecdotal. *Open*: does atrophy in one dimension (writing drafts) free attention for other dimensions (judgement, integration), or is it net negative?

### 7.2 Regulated-domain specifics

**Healthcare.** Ambient documentation (Nuance DAX, Abridge, Suki, Ambience Healthcare, Kaiser's Permanente deployments) is the current flagship. Learning velocity is *clinician-paced*, not tool-paced — physician adoption studies suggest 2-6 weeks per physician to reach stable usage and trust calibration. The CMIO / CNIO network and AMIA conferences are the durable learning surfaces. *Specific stress*: tool flux is buffered by FDA guidance cycles and EHR vendor release trains, but this buffering introduces its own lag — hospitals on year-old models when startups are on month-old models.

**Legal.** Harvey, Hebbia, Spellbook, Paxton — firm-embedded deployment means learning happens inside each law firm's innovation committee and associate training program. Failure mode: solo attorneys and mid-size firms lack the structure; they bounce between tools with no scaffolding. Bar association CLEs are beginning to add AI competency hours (NY 2023 forward), which functions as a minimum training floor.

**Finance.** SR 11-7-style Model Risk Management is being extended to LLMs. NIST AI RMF and ISO 42001 references are increasingly cited. Learning velocity is governance-paced — a new LLM feature cannot enter production until MRM review completes, which can be weeks or months. *Paradoxically*, this mechanical lag may protect against failure modes 3.1 and 3.2 because documentation and eval harnesses are mandatory. Regulated finance may end up scoring higher on Section 6 criteria *because* the regulation forces Level 3 baseline behaviors.

### 7.3 Contested claims held at low confidence
- Whether "anti-fragile" in Level 5 is a meaningful category or aspirational marketing language.
- Whether skill atrophy matters at the firm level over a 5-10 year horizon or is absorbed by role redesign (connects to O2).
- Whether the consulting-CoE model is a durable learning pattern or a transient outcome of a particular talent market (2023-2026).

---

## 8. Feedback to the three-pillar adaptability frame

- **Pillar 2 is the pillar most sensitive to ritual and cadence design.** Pillar 1 (AI usage) and Pillar 3 (infrastructure) can be re-architected; Pillar 2 learning systems can only be *cultivated* over multi-quarter horizons. This asymmetry should propagate to M1's loop diagram as a long-delay stock.
- **The eval harness is a bridge artifact across pillars.** It lives in Pillar 3 (infrastructure), encodes Pillar 2 judgment (what "good" means), and gates Pillar 1 decisions (which model to use). Three-pillar coupling is tightest here. M1 should model evals as a shared stock.
- **"Learning in public" is an under-theorized adaptability lever.** It converts Pillar 2 tacit knowledge to Pillar 1 shared standards and Pillar 3 documented patterns in a single move. Candidate for inclusion in M2 as an observable indicator (publication cadence per team per quarter).
- **Regulated domains invert the velocity-quality tradeoff.** They are structurally slower but may be structurally more durable. The frame should be explicit that "faster" is not always "more adaptable."
- **Role ownership and ritual cadence are the load-bearing survivors**, not any specific training content. This aligns with O2's role-redefinition findings: the *role* (CAIO, AI enablement lead, eval engineer) outlives any one tool generation.
- **Candidate indicators for M2 derived from this memo**: (a) median age of top-100 prompts in internal library, (b) eval-refresh cadence in days, (c) onboarding time-to-productivity for the *current* flagship AI tool, (d) double-loop retro frequency, (e) public publication cadence per AI-adjacent team, (f) guild lifespan.
