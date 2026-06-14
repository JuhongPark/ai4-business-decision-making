# A2 — Capability-to-Adoption Lag Curves

axis: A (Pillar 1 — AI Usage)
date: 2026-04-22
plan: research/operations/expansion/adaptability-framework-research-plan.md

---

## 1. Method

Evidence was gathered by pairing (i) vendor release artefacts (OpenAI, Anthropic, Google, DeepSeek blog posts, system cards, changelogs) with (ii) enterprise-survey data published between 2023 and early 2026, principally the Menlo Ventures *State of Generative AI in the Enterprise* reports (2023, 2024, 2025), the McKinsey *State of AI* surveys (2024 and March 2025), the Stanford HAI *AI Index* 2025, the a16z *How 100 Enterprise CIOs Are Building and Buying Gen AI in 2025* panel, the Gartner *Hype Cycle for AI* (2024 and 2025), and public vendor case studies (Stripe, Harvey, Klarna, Microsoft Azure, Databricks). For each capability wave, three milestones are attempted: the vendor release date (observed, dated), the first publicly documented enterprise production deploy (observed where a named customer exists, otherwise labelled inferred), and — harder — the point at which "a typical AI-using enterprise" had the capability live in at least one production surface (estimated from survey aggregates). Price-collapse / open-weight-parity dates are taken from public pricing pages and open-weight model release dates. Where no survey instrument directly measures a given capability (true for function calling, computer use, and multimodal generation in 2024–2025), the 50 % number is inferred from proxy questions (e.g., share of enterprises shipping agentic workflows, share shipping RAG, share shipping code generation) and labelled as inferred with a confidence tag. All dates are absolute. All currency figures are USD.

---

## 2. Capability wave table

Columns: Capability | Public-release date | First enterprise production deploy (date + example) | Time to 50 % enterprise adoption (estimate + source) | Time to commoditization (price curve or open-weight parity event)

| Capability | Public release | First enterprise production deploy | Time to 50 % enterprise adoption | Time to commoditization |
|---|---|---|---|---|
| **Function calling** (OpenAI) | 2023-06-13 — `gpt-3.5-turbo-0613`, `gpt-4-0613` (OpenAI blog; InfoQ) | 2023-08–2023-12 — Vercel AI SDK integrations, early Shopify / Klarna tooling, Harvey document-action patterns (inferred from vendor case studies; first public at-scale callout late 2023) | ~12 months (by mid-2024) — observed: 63 % of application developers report gen-AI in production and tool-calling is the dominant integration pattern (TechTarget summary of 2024 developer survey); RAG is the dominant design pattern at 51 % in 2024 (Menlo Ventures 2024), almost all of which uses tool/function calling underneath | **~14 months** — Structured Outputs GA 2024-08-06 with strict JSON-Schema at 100 % adherence (OpenAI); Anthropic tool use GA 2024-05, Gemini function calling GA 2024-05; open-weight equivalents (Llama 3.1 tool-use, Qwen2.5) land by 2024-07–2024-09. By 2024-08 essentially a commodity API primitive across OpenAI, Anthropic, Google, open-weight |
| **Vision (GPT-4V and peers)** | 2023-09-25 — GPT-4V rolled out to ChatGPT Plus / Enterprise; 2023-11-06 — GPT-4 Turbo with Vision API GA (OpenAI; VentureBeat; TechCrunch) | 2023-11–2024-02 — Be My Eyes, insurance claims pilots; 2024-Q1 Shopify / e-commerce product-image workflows (inferred, vendor-curated case studies) | ~18 months (by early 2025) — one-third of enterprises using gen AI report image understanding or generation workloads by McKinsey March 2025; Menlo 2024 flags multimodal as a scale-up category rather than universal | **~24 months** — Gemini 1.5 vision, Claude 3 vision (2024-03), Pixtral, Qwen-VL, Llama 3.2 vision (2024-09) all arrive within 12 months; Gartner projects multimodal share of enterprise apps rising from <10 % (2024) to 80 % (2030), i.e., vision capability becomes ambient rather than distinct |
| **Long context (≥ 200K → 1M tokens)** | 2023-05 — Anthropic Claude 2 100K; 2023-11-06 — GPT-4 Turbo 128K; 2024-02-15 — Gemini 1.5 Pro 1M (private preview); 2024-03 — Claude 3 200K GA; 2025 — Claude Sonnet 4 1M, Gemini 2.5 Pro 2M (Google, Anthropic announcements) | 2024-Q2 — doc-heavy workflows at Harvey (full-case analysis), Klarna support, Thomson Reuters, early Azure deployments | ~12–18 months (by mid-2025) — a16z 2025 panel flags a clear enterprise shift from fine-tuning to long-context "dump the data in" patterns; 50 % of enterprises running RAG at 51 % in 2024 (Menlo 2024) operate against context windows ≥ 128K by 2025 | **~18 months** — Qwen2.5-1M open-weight (2024-11); DeepSeek 128K; by 2025-12 "million-token context" documented as production-ready across Gemini, Claude, Qwen (Introl, Dec 2025). Price per million input tokens on long-context calls falls under $3 on Gemini 2.5 Pro discounted long context |
| **Reasoning (o1-class)** | 2024-09-12 — OpenAI o1-preview, o1-mini (ChatGPT Plus / Team / Azure / GitHub Copilot on day one); 2024-12-05 — o1 full release; 2024-12 — o3 preview; 2025-01–2025-02 — o3-mini GA | 2024-09-12 — GitHub Copilot test integration on release day (Microsoft); 2024-Q4 — Azure OpenAI enterprise tenants; 2025-Q1 Harvey, Cursor, Perplexity Pro deep research | ~9–12 months (mid-2025) — McKinsey March 2025: 23 % of orgs scaling agentic AI + 39 % experimenting, where reasoning models are the foundation; a16z 2025 CIO panel reports GPT-4o as most-deployed and o3 as "generating significant interest" with reasoning models being "more integrated into production"; true 50 % crossover inferred late 2025 | **~4 months** — DeepSeek-R1 (2025-01-20) reaches o1 parity on AIME / MATH at ~70 % lower cost; DeepSeek-R1-Distill-Qwen-32B beats o1-mini; Qwen QwQ (2024-11) and R1 derivatives commoditize reasoning training recipe inside ~5 months of o1-preview |
| **Agents (multi-step tool-using)** | 2023-07 — GPT-4 Code Interpreter / Plugins; 2023-11-06 — OpenAI Assistants API; 2024-H1 — LangGraph, CrewAI, AutoGen; 2024-09 — Salesforce Agentforce; 2024-10 — Anthropic Claude tool-use + computer use; 2025 — ChatGPT Agent mode (merged Operator) | 2024-Q3 — Klarna support assistant (reported public), Harvey vault agents, Cursor agent mode; 2024-12 — Agentforce general availability at Dreamforce customers | **Not yet at 50 %** (as of 2026-04) — Menlo 2024: agentic architectures power 12 % of implementations; Menlo 2025: 16 % of deployments qualify as *true* agents, 57 % use agents for multi-step workflows; a16z 2025: 11 % of agent pilots reach production; McKinsey March 2025: 23 % scaling agentic. 50 % is a forward projection, plausibly 2026-Q3 → 2027 (speculative) | Partial — tool-use primitives are commoditized (function calling GA everywhere); managed agent runtimes (LangGraph Cloud, Anthropic Claude Managed Agents, OpenAI Responses API) still differentiated on observability and governance; open-weight agent harnesses (SmolAgents, browser-use) reach parity on narrow tasks by 2025-Q4 |
| **Computer use** | 2024-10-22 — Anthropic Claude 3.5 Sonnet computer use (research preview API); 2025-01-23 — OpenAI Operator (separate product); 2025-07 — Operator folded into ChatGPT Agent mode; 2026-03 — Claude Computer Use for Pro / Max subscribers via Claude Cowork and Claude Code on macOS | 2025-Q1–Q2 — Replit agent, Cognition Devin enterprise pilots, small-scale BPO pilots (public POCs rather than at-scale production) | **Not yet at 50 %** — no public survey reports crossover; a16z 2025 flags computer use as POC-heavy; Anthropic Managed Agents launch (2026) explicitly targets the "months of infrastructure work" gap keeping enterprises out of production. 50 % crossover is forward projection, ≥ 2027 (speculative) | Not commoditized — DOM / accessibility integration remains a moat; open-weight browser-use agents (Qwen-Agent, WebArena-style) narrow the gap but computer use on arbitrary enterprise software remains bespoke through 2026-Q1 |
| **Inference-time scaling (test-time compute)** | 2024-09-12 — o1 formalizes "thinking" tokens; 2024-12 — o3 scales further; 2025-01-20 — DeepSeek-R1 makes the RL recipe open; 2025-H1 — o3-mini, Claude 3.7 / 4 "extended thinking" modes; 2025-H2 — production `reasoning_effort` / `thinking_budget` parameters across vendors | 2024-Q4 — GitHub Copilot, Cursor, Perplexity Pro use o1 as backend for selective queries; 2025-H1 — Harvey, Bloomberg Terminal AI, Klarna risk triage use reasoning tier for hard queries | ~12–18 months (late 2025 → early 2026) — a16z 2025: reasoning models "more integrated into production"; OpenAI reports 67 % of users have deployed non-frontier (cheaper / faster) models alongside reasoning tiers; majority of large enterprises running gen-AI have *some* reasoning-tier routing by end of 2025 (inferred, medium confidence) | **~4–12 months** — DeepSeek-R1 open-weights the recipe 2025-01; by 2025-Q4 `thinking_budget` parameters are standard; price per reasoning token on o3-mini, Gemini 2.5 Flash Thinking, and Claude 3.7 Sonnet extended thinking all fall within a 2–3× band by 2026-Q1 |
| **Multimodal generation (image / audio / video)** | Image: Midjourney v1 2022-07, DALL-E 2 2022-04, Stable Diffusion 2022-08, DALL-E 3 2023-10, FLUX 2024-08. Audio: ElevenLabs 2023, GPT-4o voice 2024-05, Sesame 2024. Video: Sora demo 2024-02, GA 2024-12; Runway Gen-3 2024-06; Veo 3 2025; Kling 2024 | 2023-Q4 — e-commerce image generation (Shopify Magic, Wayfair); 2024-H2 — marketing asset pipelines; 2025 — Gartner reports 58 % of Fortune 500 marketing suites embed multimodal APIs (Gartner 2025) | ~24–30 months for image (crossover ~2024-Q4 on marketing surfaces, still < 50 % on product / service surfaces as of 2025); video still < 20 % in 2025–2026 | Image: commoditized by 2024-Q4 (SD3, FLUX, SDXL derivatives, Ideogram). Video: partial by 2026-Q1 (Veo 3, Sora 2, Kling, Hunyuan, Wan 2.1 open-weights). Audio: commoditized 2024-H2 with ElevenLabs, Sesame, open-weight TTS (Kokoro, F5-TTS) |

Notes on observed vs. inferred. Release dates (column 2) are observed. First enterprise deploys (column 3) are observed where a named customer is given, inferred where "early 2024 case studies" are cited without a specific customer. 50 % adoption (column 4) is rarely directly measured — it is estimated from Menlo Ventures and McKinsey survey proxies; confidence is labelled in §5. Commoditization (column 5) combines observed open-weight releases with observed price curves; the cutoff threshold ("commoditized") is my judgement, not a survey finding.

---

## 3. Velocity chart

The table below normalizes each wave onto three milestones, measured in months from the public release date. Entries in parentheses are speculative / forward-projected.

| Wave | M1: release → first enterprise deploy | M2: release → ~50 % adoption | M3: release → commoditization |
|---|---:|---:|---:|
| Function calling | ~2–6 months | ~12 months | ~14 months |
| Vision | ~2–5 months | ~18 months | ~24 months |
| Long context (1M tier) | ~3–6 months | ~12–18 months | ~18 months |
| Reasoning (o1-class) | ~0 months (Azure / Copilot same day) | ~9–12 months | ~4 months (open-weight parity via R1) |
| Agents (multi-step) | ~3–9 months | (~24–36 months, speculative) | partial (tool primitives commoditized, runtimes not) |
| Computer use | ~3–6 months (POCs) | (≥ 30 months, speculative) | not commoditized as of 2026-Q1 |
| Inference-time scaling | ~0–3 months | ~12–18 months | ~4–12 months |
| Multimodal generation (image) | ~2–6 months | ~24 months (marketing surfaces) | ~12 months post-SDXL/FLUX |
| Multimodal generation (video) | ~3 months (POC) | (≥ 36 months, speculative) | partial |

ASCII shape — months on the horizontal axis, waves stacked.

```
0       6       12      18      24      30      36+
|-------|-------|-------|-------|-------|-------|----->
Function       D-----50=====C                                  (12 / 14 mo)
Reasoning    D C-----50                                        (9 / 4 mo, C before 50)
Long context   D-------50---C                                  (12 / 18 mo)
Inference-t.  D---C-----50                                     (~9 / ~6 mo)
Vision          D---------50---C                               (18 / 24 mo)
Image-gen      D-------------50--C                             (24 / ~12 mo post-SDXL)
Agents         D-------------------(50?)                       (50 projected 30-36 mo)
Computer use    D---------------------(50?)                    (50 projected >= 30 mo)
Video-gen      D--------------------------(50?)                (50 projected >= 36 mo)

D = first enterprise deploy   50 = ~50% adoption   C = commoditization
```

Prose description of the shape. Three distinct curve families are visible. (i) A **fast track** — function calling, reasoning, inference-time scaling, long context — where first deploy happens within 0–6 months, 50 % crossover within ~12 months, and commoditization within ~4–18 months. These are capabilities that are *additive to an existing API surface*: developers add a parameter or a new endpoint, and in some cases (reasoning, inference-time scaling) commoditization actually arrives *before* 50 % adoption because open-weight parity (DeepSeek-R1) destroys price before the typical enterprise has caught up. (ii) A **medium track** — vision, image generation — where first deploy is fast but 50 % adoption and commoditization both take 18–24 months because the capability touches new content pipelines, brand / legal review, and in regulated domains IP provenance. (iii) A **slow track** — agents, computer use, video generation — where first deploy is fast (3–9 months) but 50 % adoption is projected beyond 30 months, because the capability requires destabilizing existing workflows, integrating with legacy enterprise software surfaces, and establishing new governance. The slow-track waves are the ones where Anthropic (Claude Managed Agents, 2026) and OpenAI (Responses API, ChatGPT Agent, 2025) are now explicitly pricing *operational complexity* rather than model capability.

---

## 4. Accelerators and decelerators

### Accelerators (short M1–M2 lag, early commoditization)

- **Additivity to existing API surface** — function calling, long context, reasoning: a developer changes a parameter or swaps an endpoint and keeps the rest of the application. Rework cost is bounded in engineer-days, not months.
- **Day-one hyperscaler availability** — o1, o3, Structured Outputs all shipped on Azure OpenAI Service, AWS Bedrock, Google Vertex on or near release day; GitHub Copilot integrated o1 same-day. Enterprise procurement friction collapses because the vendor is already approved.
- **Compliance-light** — the capability does not change the *class* of content produced. Function calling calls existing internal APIs; reasoning models produce the same text the old models did, only better. No new DPIA, no new IP posture, no new content-safety pipeline.
- **ROI visible in weeks** — cost-per-query reductions (reasoning routing), accuracy lifts on structured extraction (Structured Outputs 40 % → 100 % schema adherence), and latency improvements show up in dashboards within one sprint.
- **Open-weight pressure** — reasoning commoditization in 4 months is the extreme case: DeepSeek-R1 released 2025-01-20 at ~70 % lower cost forced every closed-weight vendor to ship `reasoning_effort` / `thinking_budget` parameters and price cuts within two quarters. Open-weight pressure acts as a *deceleration-killer* for laggards who can now rent reasoning capability at commodity prices rather than wait for frontier licensing.
- **Developer-tool adjacency** — capabilities that land first in developer surfaces (Cursor, GitHub Copilot, Replit, Perplexity) propagate into enterprise through the already-approved developer stack rather than through a formal procurement cycle.

### Decelerators (long M1–M2 lag, slow or absent commoditization)

- **Compliance-heavy workflow change** — computer use lets a model drive production systems; agents take multi-step actions with potentially destructive consequences. Every such deployment triggers a new risk review, new audit-trail requirements, new human-in-the-loop thresholds. Anthropic Claude Managed Agents (2026) explicitly names "months of infrastructure work" (governance, observability) as the blocker, not model skill.
- **Integration surface complexity** — computer use requires DOM or accessibility-tree integration with heterogeneous internal software; video generation requires asset-review pipelines and rights management. The integration engineering is bespoke per enterprise and does not benefit from commoditized foundation models.
- **Destabilizing to existing roles** — agents and computer use substitute for human labour in a way function calling did not, which triggers change-management, union, and role-redefinition processes (see axis O). Menlo 2024 / 2025 shows a plateau around 16 % "true agent" deployments despite capability availability.
- **ROI visibility delayed** — agentic and computer-use ROI depends on end-to-end workflow redesign, not a single API call. a16z 2025 CIO panel reports 11 % pilot-to-production conversion for agents — the rest stall at "we cannot attribute the savings to the agent."
- **Brand / content-provenance risk** — image and especially video generation face IP, deepfake, and brand-safety concerns that marketing and legal teams resolve slowly. Even commoditized image generation stalls at marketing-asset surfaces (~58 % of Fortune 500 suites, Gartner 2025) rather than penetrating product surfaces.
- **Governance and audit scarcity** — survey evidence (a16z 2025) consistently names integration, governance, and change management (not model skill) as the top barriers. Capabilities that require new observability, logging, or audit structures pay a deceleration tax roughly proportional to how novel that structure is.

Meta-pattern: the accelerators share the property that the capability is **additive and compliance-light**; the decelerators share the property that the capability is **destabilizing or compliance-heavy**. The M1 lag (release → first deploy) is almost invariant across waves (roughly 0–6 months once a credible vendor ships). The M2 lag (release → 50 %) is where accelerators vs. decelerators diverge by a factor of 3–5×.

---

## 5. Pattern findings

1. [**high**] **M1 (release → first enterprise deploy) is roughly capability-independent and short** — 0–6 months across all eight waves 2023–2025, often 0–3 months when the vendor ships simultaneously on hyperscaler partners and developer tools. This is a saturated curve: enterprises who *can* deploy do so essentially immediately.
2. [**high**] **M2 (release → 50 % adoption) fans out by a factor of 3–5×** between additive / compliance-light capabilities (~12 months) and destabilizing / compliance-heavy capabilities (30+ months, speculative for agents, computer use, video).
3. [**high**] **Reasoning commoditized faster than it was adopted.** DeepSeek-R1 (2025-01, ~4 months after o1-preview) achieved o1 parity at ~70 % lower cost before the median enterprise had deployed reasoning at all. This is the first wave where M3 < M2 — commoditization beats adoption. Implication for the adaptability frame: enterprises who waited were rewarded; enterprises who rushed paid a premium.
4. [**medium**] **Open-weight pressure is the strongest decelerator-killer and the strongest commoditization accelerator.** Function calling, reasoning, and long context all had open-weight parity within 4–18 months. Computer use and video have not (yet) — which correlates with their slow 50 % curves, though the direction of causation is unclear.
5. [**medium**] **Compliance-light additive features dominate the accelerator profile**, as evidenced by Structured Outputs (a lexical tightening of existing function calling) reaching essentially universal production adoption in under a year, while computer use (capable of driving real systems) stalled at POC for 18+ months.
6. [**medium**] **The M1–M2 gap is the canonical "capability-to-adoption lag."** Measured as calendar days between first enterprise deploy and 50 % enterprise deploy, it ranges from ~6 months (function calling, reasoning) to plausibly 24+ months (agents, computer use). This gap is a candidate adaptability indicator for M2 (see §7).
7. [**low**] **Multimodal generation bifurcates** by end surface. Image generation commoditized quickly and was broadly adopted on marketing surfaces, but penetrated product surfaces slowly — enterprise data on this split is poor because surveys do not consistently distinguish "marketing use" from "product use." Video is too early for any confident finding.
8. [**low**] **There is no visible moat in capability-timing alone.** Every frontier capability was matched within 4–18 months by at least one close follower (Anthropic matching OpenAI on tool use inside 11 months, Google matching on long context inside 3 months, DeepSeek matching on reasoning inside 4 months). The moats that remain are governance, workflow integration, and brand trust — none of which are measured by capability release dates.

---

## 6. Open questions and negative evidence

- **What was looked for but not found.** No enterprise survey 2022–2026 directly measures capability-by-capability adoption with monthly granularity. Menlo Ventures, a16z, and McKinsey publish annual snapshots that aggregate across capabilities (e.g., "agentic AI scaling at 23 %") without decomposing function calling vs. agents vs. computer use. The 50 % numbers above are triangulated estimates, not direct observations.
- **Regional and industry decomposition is thin.** US / EU enterprise samples dominate published surveys. East Asia (China, Japan, Korea) adoption of reasoning models under export-control constraints is under-observed. Regulated industries (healthcare, finance, legal) likely show longer M2 lags than the aggregate but the empirical base is sparse — see extension tracks `scale-based/s5-regulated-professions.md` and `healthcare-bio-ai/`.
- **The "50 % adoption" threshold is itself under-specified.** Surveys alternately measure "has deployed in at least one production surface" (high), "has made it available to at least 50 % of employees" (medium), and "majority of workflows touch the capability" (low). The table collapses these into one number, which is a methodological caveat not a finding.
- **Computer use and video generation are too recent for credible 50 % estimates.** Projections are flagged as speculative.
- **Causation is not cleanly separated from correlation** between "compliance-heavy" and "slow adoption." It could be that heavy compliance causes slow adoption, or that low-perceived-ROI causes both the slow deployment and the relaxed compliance scrutiny. The current memo treats this as a pattern to test in A3 (workflow retooling) and O2 (role redefinition), not as a proven mechanism.
- **Pricing data is noisy.** List prices are observed but actual enterprise commit prices are not; the "commoditization" column uses list prices, which overstates the effective price collapse for enterprises with committed-use discounts.

---

## 7. Feedback to three-pillar adaptability frame

- **Pillar 1 (AI Usage)** — the M1–M2 gap is the defining clock of Pillar 1. A team whose capability-to-deploy lag exceeds the commoditization time window pays a structural premium (they paid for leading capability and got commodity quality). The A2 evidence argues for a Pillar-1 posture of "deploy fast on additive capabilities, stage deployment on destabilizing capabilities" — the classical split aligns with the accelerator / decelerator profile in §4.
- **Pillar 2 (Organization)** — the M2 lag is dominated by governance, change management, and integration — organizational variables, not Pillar-1 capability. This is evidence that *organizational* adaptability is load-bearing for *AI-usage* adaptability: the slow waves (agents, computer use) are slow not because the model cannot but because the organization cannot. Feeds directly into O1, O2, O3.
- **Pillar 3 (Infrastructure)** — reasoning and long-context commoditization within 4–18 months suggests that infrastructure decisions (build vs. rent, single vs. multi-provider) should be parameterized on a ≤ 12-month horizon for frontier capability and a ≤ 4-month horizon once an open-weight equivalent has shipped. Infrastructure bets on a *specific* frontier model for a *specific* capability have a half-life measured in quarters, not years (feeds T1).
- **M1 (systems dynamics)** — the capability-adoption lag acts as a delay in the feedback loop between model release and organizational redesign. Short M1 combined with long M2 creates an accumulating "capability debt" — organizations know a capability exists but cannot deploy it at scale. This debt compounds across waves and is a candidate stock variable in the system-dynamics map.
- **M2 (indicators)** — **capability-to-deployment lag** (days from public release to production integration) is already listed as a candidate indicator in the plan. A2 additionally suggests two refinements: (i) report the M1 / M2 / M3 triple rather than a single number, because they decompose into different organizational causes; (ii) report the M3 − M2 gap (commoditization minus 50 %-adoption) as a *regret indicator* — negative values mean the organization paid frontier prices to deploy a capability that became commodity before they reached scale.
- **Cross-track relevance** — the slow-track waves (agents, computer use) are precisely the ones where reasoning trust verification, scale-tier differences, and regulated-domain constraints bind hardest. A2 is evidence that the other extension tracks (`scale-based/`, `healthcare-bio-ai/`, reasoning trust) matter *most* for the waves that have not yet reached 50 % and *least* for the waves that have already commoditized. Resource allocation across extensions should follow this asymmetry.

---

### Sources

- OpenAI, "Function calling and other API updates," 2023-06-13.
- InfoQ, "OpenAI Announces Function Calling," 2023-06.
- OpenAI, "GPT-4V(ision) system card," 2023-09-25.
- VentureBeat, "OpenAI makes GPT-4 Turbo with Vision generally available through its API," 2023-11.
- TechCrunch, "As OpenAI's multimodal API launches broadly, research shows it's still flawed," 2023-11-06.
- Anthropic, "Introducing the next generation of Claude" (Claude 3 family, 200K context), 2024-03.
- Google, "Introducing Gemini 1.5, Google's next-generation AI model," 2024-02-15.
- OpenAI, "Introducing OpenAI o1," 2024-09-12.
- Microsoft Azure Blog, "Introducing o1: OpenAI's new reasoning model series for developers and enterprises on Azure," 2024-09-12.
- OpenAI, "Introducing Structured Outputs in the API," 2024-08-06.
- Anthropic, "Introducing computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku," 2024-10-22.
- OpenAI, Operator launch, 2025-01-23; integration into ChatGPT Agent, 2025-07.
- DeepSeek, "DeepSeek-R1" release, 2025-01-20; Hugging Face model card.
- Menlo Ventures, "2023 / 2024 / 2025 State of Generative AI in the Enterprise" reports.
- a16z, "How 100 Enterprise CIOs Are Building and Buying Gen AI in 2025."
- McKinsey QuantumBlack, "The State of AI" (2024, March 2025).
- Stanford HAI, "2025 AI Index Report."
- Gartner, "Hype Cycle for AI 2024, 2025"; "Hype Cycle for GenAI 2025"; multimodal-enterprise projection (2025-07).
- Stripe, "Indexing the AI Economy"; Sessions 2025 announcements; Agentic Commerce Protocol launch.
- Harvey, company timeline via Contrary Research, LawNext, Wikipedia (Allen & Overy 2023-02, Paul Weiss 2023, A&L Goodbody 2024-02, Ashurst 2024-06, Microsoft Azure 2024-05, Mirage acquisition 2024-04).
- Anthropic, "Claude Managed Agents" platform announcement, 2026.

All release dates are observed against primary sources. All adoption percentages are as reported by named surveys. Judgements about "commoditization" (column 5 of §2) are the author's synthesis from price pages, open-weight release dates, and vendor API parity; they are not survey findings.
