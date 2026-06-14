# T1 — Build vs Rent Decision Framework Under Model Flux

axis: T (Pillar 3 — Technical Infrastructure)
date: 2026-04-22
plan: research/operations/expansion/adaptability-framework-research-plan.md

---

## 1. Method

**Research object**: decisions that determine where inference runs, who owns the weights, and how many providers stand behind production traffic — kept durable under a foundation-model release cadence of 6–12 months across 2024–2026 (GPT-4o → GPT-5 → GPT-5.1; Claude 3 → 3.5 → 4 → 4.5; Llama 3 → 3.1 → 3.2 → 4; DeepSeek V3 → R1 → V3.1; Qwen 2.5 → 3).

**Evidence sourcing**: the corpus for this memo is public — vendor engineering blogs, press releases, analyst commentary, trade press, and one arXiv paper (BloombergGPT). No proprietary switching-cost data was obtainable; all engineering-month and downtime figures are either self-reported by the company, estimated by the cited analyst, or marked inferred. Evidence tiers follow the project's `evidence-tier-method.md`: Tier A regulator / peer-reviewed / audited (very few here), Tier B official company / vendor disclosure, Tier C trade press and analyst commentary.

**Claim discipline**. Observed facts carry a source and a date. Inferred claims are labelled *[inf]*. Confidence is labelled *high / medium / low* when the claim is load-bearing for the decision tree. Negative evidence (what was looked for and not found) is recorded in §6.

**Scope boundary**. Memo covers the four decision axes in the plan — API vs self-host, proprietary vs open-weight, cloud vs on-prem vs hybrid, single vs multi-provider routing. Non-goals: detailed GPU-level procurement, embedding-model lifecycle (that sits in T3), compute scaling curves (T2), and organization-side governance around the decision (O2, scale-based tier analyses).

---

## 2. Case study table — switching events 2024–2026

Fifteen cases in the table. "Switch direction" uses the plan's conventions: *API→self-host*, *API↔multi-provider*, *API→proprietary-model (built own weights)*, *single-cloud→hybrid*, etc. Costs are reported where stated; otherwise marked *not disclosed*.

| # | Company | Switch direction | Date | Stated rationale | Switching cost (eng-months / downtime / quality regression) | Source tier |
|---|---|---|---|---|---|---|
| 1 | **Perplexity** | API-multi-provider → in-house model (Sonar, built on Llama 3.3 70B) while retaining API fallback for reasoning and frontier tasks | Announced Feb 11 2025; deprecation of legacy Llama-Sonar aliases Feb 22 2025; `sonar-reasoning` removed Dec 15 2025 | Cost per query, latency for search-grounded answers, control over factuality-and-readability post-training loop (Perplexity claim: Sonar matches GPT-4o / Claude 3.5 Sonnet for user satisfaction while running on internal infrastructure) ([Meet New Sonar](https://www.perplexity.ai/hub/blog/meet-new-sonar); [Sonar Pro blog](https://www.perplexity.ai/hub/blog/introducing-the-sonar-pro-api); [Perplexity Changelog](https://docs.perplexity.ai/changelog/changelog)) | Not disclosed. *[inf, medium]* Roughly multi-quarter effort for a post-training and serving stack; existing model-download path suggests no material downtime | B |
| 2 | **Cursor / Anysphere** | API-multi-provider (OpenAI, Anthropic, Google) → multi-provider plus in-house model (Composer 2, Mar 19 2026) while keeping frontier models for user choice | Composer 2 released Mar 19 2026; Auto-router operational throughout 2024–2026 | Inference economics at billions of completions per day; latency ("4× faster than similarly intelligent models"); reward-signal control for long-horizon coding RL ([Cursor Composer 2 review](https://computertech.co/cursor-composer-2-review/); [Bytebytego on Cursor scale](https://blog.bytebytego.com/p/how-cursor-serves-billions-of-ai); [Contrary Research](https://research.contrary.com/company/cursor)) | Not disclosed. Public reporting describes Composer 2 as pre-trained from initialization on a curated code corpus with multi-round RL; no downtime disclosed; quality regression only for users who prefer Claude or GPT — routing preserves choice | B / C |
| 3 | **Harvey** | Started single-provider (OpenAI) → multi-provider (added Anthropic Claude and Google models alongside OpenAI) | Multi-provider extension announced 2025–2026 | Performance parity no longer held per model generation; enterprise users also consolidating around Claude-side platforms ([Harvey blog — Expanding Model Offerings](https://www.harvey.ai/blog/expanding-harveys-model-offerings); [Harvey Opus 4.6 blog](https://www.harvey.ai/blog/opus-4-6-now-live-in-harvey); [Legal IT Insider, Feb 25 2026](https://legaltechnology.com/2026/02/25/from-market-meltdown-to-strategic-realignment-harvey-and-lexisnexis-chart-diverging-paths-with-anthropic/); [Anthropic customer story — Harvey](https://claude.com/customers/harvey)) | Not disclosed. *[inf, medium]* Harvey reports $190M ARR end-2025 across 1,000+ customers, 60 countries, majority of AmLaw 100 — scale makes migration a product-line decision rather than a single-team project | B |
| 4 | **Klarna** | API (OpenAI) forward push, then partial rollback on the *application* layer (customer service agent), not on the infrastructure choice | Deployment early 2024; public rollback on layoffs-driven CS agent disclosed 2025 | Initial: $40M projected profit lift, resolution time 11 min → 2 min, AI covered ~2/3 of CS chats. Reversal: CEO Siemiatkowski publicly admitted "the AI-driven transition negatively affected service and product quality" and resumed human hiring ([Fast Company](https://www.fastcompany.com/91039401/klarna-ai-virtual-assistant-does-the-work-of-700-humans-after-layoffs); [CX Network on Klarna automation & IPO](https://www.cxnetwork.com/artificial-intelligence/news/klarna-closer-to-ipo-as-ai-and-automation-boost-pays-off); [mlq.ai — Klarna CEO admits AI job cuts went too far](https://mlq.ai/news/klarna-ceo-admits-aggressive-ai-job-cuts-went-too-far-starts-hiring-again-after-us-ipo/)) | Quality regression significant enough to warrant re-hire; dollar figure not disclosed. Infrastructure choice (ChatGPT Enterprise / OpenAI API) was **not** reversed | B / C |
| 5 | **Bloomberg** | Self-host proprietary model (BloombergGPT) — chose build over rent from the outset, not a mid-stream switch | BloombergGPT paper Mar 30 2023; remained internal layer 2023–2026 | Proprietary training data ("we have data we don't want to send out … for internal and sensitive use, in-house models are preferable"), compliance, domain fine-tune on FinPile (369B tokens finance + 345B tokens general) ([Bloomberg press release](https://www.bloomberg.com/company/press/bloomberggpt-50-billion-parameter-llm-tuned-finance/); [arXiv:2303.17564](https://arxiv.org/abs/2303.17564); [InfoQ](https://www.infoq.com/news/2023/04/bloomberg-gpt-ai/); [Belitsoft case summary](https://belitsoft.com/bloomberggpt)) | Reported ~$10M training spend (Medium, corroborated in trade press). *[inf, medium]* Post-GPT-4 arrival, parity gap widened — regulatory / data-moat arguments, not quality, sustained the decision | A (arXiv) / B |
| 6 | **JPMorgan Chase — LLM Suite** | Private-cloud aggregator: multiple provider models delivered through an in-house controlled wrapper | Rolled out summer 2024; ~200,000 onboarded users in 8 months; >230,000 daily users by 2025–2026; American Banker "Innovation of the Year" 2025 | Data privacy, regulatory compliance, internal governance — "in a very safe and secure way … was a principal reason they wanted to build in-house" ([JPMorgan blog](https://www.jpmorganchase.com/about/technology/blog/llmsuite-ab-award); [Digital Banker feature](https://thedigitalbanker.com/jpmorgan-chases-llm-suite-drives-ai-transformation-across-the-enterprise/); [American Banker](https://www.americanbanker.com/news/how-jpmorganchase-democratized-employee-access-to-gen-ai)) | Not disclosed in engineering-month terms. Adoption curve (0 → 200k in 8 months) is Tier-B evidence of low user-facing regression | B |
| 7 | **Morgan Stanley — Wealth / Institutional assistants** | API (Azure OpenAI / GPT-4-class) — stayed API, extended scope rather than insourcing | AI @ MS Assistant rolled out to Wealth advisors Sep 2023; AskResearchGPT rolled out to Institutional Securities Oct 2024 | Productivity on ~100,000 research documents; compliance-reviewed retrieval wrapper rather than a custom model ([CNBC Jun 26 2024](https://www.cnbc.com/2024/06/26/morgan-stanley-openai-powered-assistant-for-wealth-advisors.html); [CNBC Oct 23 2024](https://www.cnbc.com/2024/10/23/morgan-stanley-rolls-out-openai-powered-chatbot-for-wall-street-division.html); [Morgan Stanley press release](https://www.morganstanley.com/press-releases/key-milestone-in-innovation-journey-with-openai); [Celent](https://www.celent.com/en/insights/531525129)) | Not disclosed. No rollback reported through 2025 | B |
| 8 | **Shopify — Sidekick** | API with Shopify-documents RAG → big-bang re-architecture of the agentic loop in spring 2025 while keeping external LLMs for reasoning | Introduced Summer 2024; re-architecture Spring 2025; Sidekick 2 + Agentic Storefronts Dec 2025 | Initial low merchant usage; shifted from reactive to proactive agent; kept "publicly available LLMs like ChatGPT for reasoning" rather than training a proprietary model ([Shopify Engineering](https://shopify.engineering/building-production-ready-agentic-systems); [Stack Overflow blog — every ecommerce hero needs a Sidekick](https://stackoverflow.blog/2026/01/09/every-ecommerce-hero-needs-a-sidekick/); [TheLetterTwo Dec 10 2025](https://thelettertwo.com/2025/12/10/shopify-ai-growth-tools-sidekick-tinker-agentic-storefronts/)) | Not disclosed. Characterized by Shopify engineering as a "big re-architecture shift" | B |
| 9 | **DoorDash, Instacart (+ Uber, OpenTable, Priceline, StubHub, Thumbtack)** | App-on-API: integrate into ChatGPT's agent runtime rather than run their own LLM | Instacart Dec 2025 (first grocery partner); DoorDash Dec 17 2025 | Distribution gain via ChatGPT; end-to-end Instant Checkout; time-to-market — cost of building a rival surface prohibitive ([Bloomberg](https://www.bloomberg.com/news/articles/2025-12-17/doordash-brings-grocery-shopping-to-chatgpt-rivaling-instacart); [Instacart IR](https://investors.instacart.com/news-releases/news-release-details/instacart-app-launches-openai-chatgpt-first-company-offer-new); [Digital Commerce 360](https://www.digitalcommerce360.com/2025/12/19/doordash-app-openai-chatgpt/); [PYMNTS](https://www.pymnts.com/artificial-intelligence-2/2025/doordash-integrates-app-with-openai%E2%80%99s-chatgpt-to-facilitate-grocery-shopping/); [OpenAI Operator intro](https://openai.com/index/introducing-operator/)) | *[inf, medium]* single-digit engineering-months to ship the app definition; revenue dependent on ChatGPT traffic — adaptability cost is vendor lock-in at the distribution layer | B / C |
| 10 | **Notion** | API-multi-provider (GPT-4.1 + Claude 3.7) → central reasoning model orchestrating modular sub-agents (agent platform rebuild for GPT-5 in 2025; Notion 3.2 Jan 2026 added GPT-5.2, Claude Opus 4.5, Gemini 3) | Multi-model added in 2024; agent rebuild around GPT-5 2025; Notion 3.0 Sep 2025; Notion 3.2 Jan 2026 | Multi-step workflows required a re-architecture: "instead of patching their existing stack, Notion rebuilt it with a central reasoning model that coordinates modular sub-agents" ([OpenAI customer story — Notion](https://openai.com/index/notion/); [VentureBeat](https://venturebeat.com/ai/notion-bets-big-on-integrated-llms-adds-gpt-4-1-and-claude-3-7-to-platform); [Notion × Claude partner page](https://www.notion.com/partners/claude)) | Not disclosed. *[inf, high]* The rebuild itself is the switching cost — pre-existing prompt chains did not survive the agentic generation | B |
| 11 | **Palantir AIP** | Model-agnostic multi-provider architecture from the start (OpenAI, Google, Anthropic, xAI, Llama, custom) | AIP GA 2023; supported-LLM catalogue expanded 2024–2026 | Enterprise buyers demand swap / A/B / graceful fallback under provider outage; regulated-customer need for bring-your-own-model ([Palantir AIP overview](https://www.palantir.com/platforms/aip/); [Palantir supported LLMs](https://www.palantir.com/docs/foundry/aip/supported-llms); [Anand blog — AIP 12-layer agentic architecture](https://anandbg.com/blog/palantir-aip-end-to-end-agentic-architecture)) | No rewrite events reported. Model-agnostic wrapper is the switching-cost minimiser — the architectural posture, not a switch | B / C |
| 12 | **Sierra** | Multi-model from launch (OpenAI, Anthropic, Meta) with multi-model orchestration as a hallucination-reduction mechanism | Founded 2023; $100M ARR in 7 quarters; $10B valuation 2025 | Reliability in customer-service agent contexts; vendor redundancy ([Sacra — Sierra](https://sacra.com/c/sierra/); [TechCrunch Nov 21 2025](https://techcrunch.com/2025/11/21/bret-taylors-sierra-reaches-100m-arr-in-under-two-years/); [Sequoia Training Data podcast — Bret Taylor](https://sequoiacap.com/podcast/training-data-bret-taylor/); [webpronews](https://www.webpronews.com/bret-taylors-agentic-bet-sierras-push-to-reshape-enterprise-ai/)) | No switch event; architectural hedge from day one | C |
| 13 | **Block (Cash App)** | API-first → added self-hosted Llama for customer-support workloads | Reported 2024; Meta "future of AI built with Llama" blog | Open weights enabled rapid experimentation and per-use-case customization; customer-data privacy ([Meta AI blog — Built with Llama](https://ai.meta.com/blog/future-of-ai-built-with-llama/)) | Not disclosed; Meta cites 85% cost reductions for some switchers to Llama 3 ([Nova Media Group](https://www.novamediagroup.com/blog/meta-llama-3-open-weight-models-disrupting-enterprise-ai-costs)) — *[inf, low]* figure is vendor-PR quality | B / C |
| 14 | **Goldman Sachs, AT&T, Nomura Holdings** | Added Llama to existing API stack (hybrid) | 2024 ([Meta AI blog](https://ai.meta.com/blog/future-of-ai-built-with-llama/)) | Document review, code generation, customer service — use-case-specific fit beats single-provider quality ceiling | Not disclosed | B |
| 15 | **Mercado Libre** | Built a centralized LLM gateway covering multiple providers for ~50,000 employees and e-commerce recommendation flows | 2024–2025 ([ZenML LLMOps database — Mercado Libre](https://www.zenml.io/llmops-database/building-a-scalable-llm-gateway-for-e-commerce-recommendations)) | Consolidate security, monitoring, billing; provider diversity per use case | Not disclosed | C |

**Dominant direction observed**: *toward multi-provider* for most companies; *toward hybrid API + in-house weights* for the inference-heavy AI-native subset (Perplexity, Cursor); *stay API* for data-light enterprises that bought distribution (DoorDash, Instacart). Pure API→on-prem migration driven by cost alone is not observed in the 2024–2026 corpus; compliance or data-sovereignty drove the self-host side in every Tier-B case (Bloomberg, JPMorgan, Block).

---

## 3. Decision axes

Each axis carries a pros / cons / failure-mode triple. Failure modes are the reason this axis has to survive the 6–12-month turnover — a decision that looks optimal per generation can become the rewrite driver of the next.

### 3.1 API vs self-host

| | Pros | Cons | Failure mode under flux |
|---|---|---|---|
| **API (managed)** | Zero GPU capex; frontier quality on day one; automatic upgrades; per-token elastic cost | Vendor lock-in on prompts, function-call schema, and safety-layer behaviour; outage propagates to your product; token price floor set by provider margin | Prompt-as-code regression when the provider ships a silently different model (well-documented for GPT-4o → GPT-5 and Claude 3.5 → 4 transitions); sunset of named checkpoints (e.g. Perplexity `sonar-reasoning` deprecation Dec 15 2025) forces migration with no negotiated date ([CallSphere GPT-3.5→5 migration post](https://callsphere.ai/blog/upgrading-llm-models-production-gpt35-gpt4-gpt5-migration); [Rajasekar Venkatesan — prompts as technical debt](https://medium.com/@rajasekar-venkatesan/your-prompts-are-technical-debt-a-migration-framework-for-production-llm-systems-942f9668a2c7)) |
| **Self-host (own weights on own or rented GPUs)** | Data never leaves the boundary; deterministic version control; cost per token predictable once break-even passed; RL / fine-tune loop is fully yours | Team-weeks for every model generation; on-call for GPU and serving issues; quality lag behind frontier is the default state, not the exception | Obsolescence — the weights you trained on Llama 3.1 stop being competitive 6 months later; the fine-tune stack has to be redone against the successor model; break-even was computed on old token prices that the managed providers later undercut |

**Break-even heuristic (observed and inferred)**: cost-side break-even sits somewhere around 15–40M tokens/month against 2026 open-weight API prices from DeepSeek / Qwen-class providers ([Swfte AI — open-source savings guide](https://www.swfte.com/blog/open-source-llm-cost-savings-guide); [Phyvant — DeepSeek for enterprise AI buyers](https://phyvant.com/blog/deepseek-enterprise-ai-buyers); [Particula — DeepSeek V4 Qwen 3.5](https://particula.tech/blog/deepseek-v4-qwen-open-source-ai-disruption)). *Confidence: medium.* Below that, managed API is almost certainly cheaper; above it, self-hosting becomes defensible on price alone. Non-price drivers (data sensitivity, latency, capability-specialisation) can override the break-even in either direction.

### 3.2 Proprietary vs open-weight

| | Pros | Cons | Failure mode under flux |
|---|---|---|---|
| **Proprietary weights (OpenAI, Anthropic, Google)** | Frontier capability, richest tool / agent / reasoning features first; mature safety layer; enterprise SLAs | No inspection; no on-prem option for most of the catalogue; price and quality are the vendor's variables | Forced-migration when the specific checkpoint you depended on is retired or behaviourally changed ([GPT-4o retirement & dependency risk](https://jangwook.net/en/blog/en/gpt4o-retirement-model-dependency-risk/)) |
| **Open-weight (Llama, Qwen, DeepSeek, Mistral)** | Inspectable, portable, deployable in regulated environments; customizable via fine-tune; zero marginal token cost once served in-house | Frontier lag (narrowed for reasoning in 2025–2026 — DeepSeek R1, Qwen 3 — but still present for multimodal / agentic); no vendor SLA except via Fireworks / Together / Baseten / Modal; you own the evaluation and safety burden | Ecosystem fragmentation — Llama 3 → 3.1 → 3.2 → 4 meant three fine-tune refreshes in ~18 months; DeepSeek V3 → R1 → V3.1 meant reasoning-pipeline rebuild on release ([Computerworld on DeepSeek V3.1](https://www.computerworld.com/article/4042964/chinas-deepseek-launches-v3-1-raising-stakes-for-enterprise-ai-adoption.html); [InformationWeek on enterprise DeepSeek adoption](https://www.informationweek.com/machine-learning-ai/will-enterprises-adopt-deepseek-)) |

**Adoption signal (observed)**: self-hosted models used by DeepSeek customers rose ~2× in January 2025 alone ([Virtualization Review, Mar 5 2025](https://virtualizationreview.com/Articles/2025/03/05/DeepSeek-Drives-Increase-in-Self-Hosted-Models-Says-Cloud-AI-Report.aspx)); DeepSeek + Qwen combined share rose from ~1% to ~15% of global AI market January 2025 → January 2026 ([Particula](https://particula.tech/blog/deepseek-v4-qwen-open-source-ai-disruption)). The "67% of enterprises deploying open-weights in production" figure ([Programming Helper](https://www.programming-helper.com/tech/deepseek-open-source-ai-models-2026-python-enterprise-adoption)) is Tier-C and should not be treated as verified — *confidence low*.

### 3.3 Cloud vs on-prem vs hybrid

| | Pros | Cons | Failure mode under flux |
|---|---|---|---|
| **Public cloud** (Azure OpenAI, AWS Bedrock, Google Vertex) | Speed to production; catalog breadth; standard compliance posture; per-region availability | Token-price floor; cloud's own capacity constraints (AWS Bedrock reported peak-demand constraints in 2025 ([Xenoss comparison](https://xenoss.io/blog/aws-bedrock-vs-azure-ai-vs-google-vertex-ai); [CloudOptimo](https://www.cloudoptimo.com/blog/amazon-bedrock-vs-azure-openai-vs-google-vertex-ai-an-in-depth-analysis/))); coupling to cloud's identity / networking stack | Provider route deprecation (Azure OpenAI GPT-4o-class → GPT-5 forced endpoint migration); cross-cloud egress penalties if a second provider is added later |
| **On-prem** | Data sovereignty; predictable latency inside the DC; regulated industries (banking, defence, healthcare) often accept no other option | GPU procurement 2024–2026 was the binding constraint; team needs MLOps + GPU ops; hardware cycles misalign with model cycles | You bought H100 capacity for one model family; the next family wants a different shape; model refreshes arrive faster than capital refreshes |
| **Hybrid** (sensitive data on-prem, non-sensitive via API) | Matches regulatory segmentation; allows asymmetric capability — frontier for brainstorm / low-stakes, self-host for regulated | Two pipelines, two eval suites, two safety layers, two on-call rotations; routing logic becomes its own system | Category drift — the set of "non-sensitive" prompts shrinks as agents start chaining tools across data sources; a single agent turn can cross the boundary |

Observed pattern: regulated financial-services firms are the cleanest hybrid exemplars — JPMorgan (LLM Suite, private wrapper over multiple providers), Morgan Stanley (Azure OpenAI inside compliance wrappers), Bloomberg (self-host for internal data, external APIs for analyst-facing brainstorm).

### 3.4 Single vs multi-provider routing

| | Pros | Cons | Failure mode under flux |
|---|---|---|---|
| **Single provider** | One prompt dialect; one safety policy; one eval suite; best-in-class partnership terms (Harvey ↔ OpenAI initial posture, Morgan Stanley ↔ OpenAI, DoorDash / Instacart ↔ ChatGPT) | Outage = product down; price increase = margin compression; checkpoint retirement = forced rewrite; capability gap when rival ships something your provider has not | Harvey's 2025 move from OpenAI-only to OpenAI + Anthropic + Google is the canonical single→multi switch — rationale was capability parity no longer sustained per-generation ([Harvey blog](https://www.harvey.ai/blog/expanding-harveys-model-offerings); [Legal IT Insider](https://legaltechnology.com/2026/02/25/from-market-meltdown-to-strategic-realignment-harvey-and-lexisnexis-chart-diverging-paths-with-anthropic/)) |
| **Multi-provider routing** | Vendor-outage survivability; per-task best-of-N; price arbitrage; negotiating leverage | Engineering mass of the router itself; two eval suites; prompt dialect divergence; skill is scarce | Router becomes a product — Palantir AIP and Sierra have effectively made the router the product. Cursor, Windsurf, Notion ship explicit model pickers. The router is new surface area that must itself adapt to each release |

Observed industry infrastructure for this axis: LiteLLM, Portkey, OpenRouter, AnyModel, any-llm, LLMGateway, Mercado Libre's internal gateway — a 2024–2026 generation of routing abstractions ([LiteLLM](https://docs.litellm.ai/); [Portkey + Cursor](https://portkey.ai/docs/integrations/libraries/cursor); [Mozilla any-llm](https://blog.mozilla.ai/introducing-any-llm-a-unified-api-to-access-any-llm-provider/); [LLMGateway](https://llmgateway.io/)). Their existence is evidence that multi-provider routing is now a category, not a bespoke architecture — *confidence high*.

---

## 4. Architectural decisions — held vs rewrite across GPT-5 / Claude 4

Span: roughly GPT-4o (May 2024) and Claude 3.5 Sonnet (June 2024) → GPT-5 (August 2025), Claude 4 (mid-2025), Claude 4.5 (December 2025), Claude 4.6 / 4.7 (early–mid 2026), GPT-5.1–5.4 and Gemini 2.5 / 3 (late 2025–early 2026). The question: which architecture choices from early 2024 survived the full cycle, which needed rewrite?

### 4.1 Held up (observed)

| Decision | Why it held | Evidence |
|---|---|---|
| **Thin abstraction boundary between prompt layer and model** (Palantir AIP, Sierra, LLM-gateway pattern) | Swap cost falls from product rewrite to adapter rewrite | Palantir AIP supports OpenAI / Google / Anthropic / xAI / Llama behind one interface ([Palantir supported LLMs](https://www.palantir.com/docs/foundry/aip/supported-llms)); Sierra multi-model orchestration shipped at launch ([Sacra — Sierra](https://sacra.com/c/sierra/)) |
| **Retrieval layer decoupled from the model** (Morgan Stanley, JPMorgan LLM Suite, Bloomberg's FinPile wrapper) | Documents, indexes, chunkers outlive the generator | Morgan Stanley AI @ MS Assistant retained the same ~100k-document retrieval base across GPT-4 / GPT-4o / GPT-5 generations ([CNBC](https://www.cnbc.com/2024/06/26/morgan-stanley-openai-powered-assistant-for-wealth-advisors.html); [Celent](https://www.celent.com/en/insights/531525129)) |
| **Model-agnostic evaluator harness** (companies that versioned prompt regressions pre-migration) | GPT-4o → GPT-5 migration costs dropped sharply where eval coverage existed ([LeanLM](https://leanlm.ai/blog/llm-cost-optimization); [Codeant](https://www.codeant.ai/blogs/cost-of-switching-llm-models)); *confidence medium* — this is mostly trade-press inference |
| **Token-metering and billing decoupled from model identity** (Stripe token-meter, LLM gateways) | Pricing can be re-wired in hours rather than weeks on a model change | [Stripe token-meter](https://stripe.com/use-cases/ai); Mercado Libre gateway pattern |
| **Private-cloud aggregator over multiple external providers** (JPMorgan LLM Suite) | The aggregator absorbs the per-release upgrade without product teams noticing | 0 → 200k users in 8 months without a reported migration event ([JPMorgan blog](https://www.jpmorganchase.com/about/technology/blog/llmsuite-ab-award)) |

### 4.2 Required rewrite (observed)

| Decision | Why it broke | Evidence |
|---|---|---|
| **Prompt chains tightly coupled to a specific checkpoint's behaviour** | Behaviour changes under silent updates; "let's think step by step" and similar heuristics actively counterproductive on reasoning-trained models ([SurePrompts 2026](https://sureprompts.com/blog/advanced-prompt-engineering-2026-claude-gpt5-gemini)) | Widely reported across GPT-4o→GPT-5 migration posts ([CallSphere](https://callsphere.ai/blog/upgrading-llm-models-production-gpt35-gpt4-gpt5-migration); [Divyam.AI](https://divyam.ai/blog/hidden-cost-of-llmflation/)) |
| **Fine-tunes on deprecated base models** | Adapters locked to a base-model version that was retired ([GPT-4o retirement risk writeup](https://jangwook.net/en/blog/en/gpt4o-retirement-model-dependency-risk/)) | Tier C; *confidence medium* |
| **Agentic loop designed for a fixed tool-use schema** | Tool-use schemas changed between GPT-4o and GPT-5 (function calling → Responses API / structured-output paradigm); Anthropic's tool schema also evolved | Notion's GPT-5 rebuild is the clearest case — central reasoning model + modular sub-agents, not an incremental patch ([OpenAI customer story — Notion](https://openai.com/index/notion/)) |
| **Single-provider assumptions baked into observability, rate-limiting, cost-attribution** | A second provider exposes the coupling | Implicit in the emergence of LLM-gateway products 2024–2026 |
| **Eval harnesses that used an older model as LLM-as-judge** | Judge drift under generation turnover; re-weighting required (more fully treated in T3) | [Latitude on proprietary-LLM hidden costs](https://latitude.so/blog/proprietary-llms-hidden-costs-watch-for) |

### 4.3 Reported switching cost anchors

Not a controlled study. Each number carries a Tier-C caveat.
- "Migrating to a new provider can consume 20–50% of the original development time, which for startups could mean spending over $100,000 just on re-engineering" ([CodeAnt blog](https://www.codeant.ai/blogs/cost-of-switching-llm-models); *confidence low*).
- "Eight engineer-weeks spent on migrations" per wholesale migration episode ([Divyam.AI](https://divyam.ai/blog/hidden-cost-of-llmflation/); *confidence low*).
- Klarna's CS-agent rollback shows that *quality regression* can be the binding constraint even when engineering cost is small ([mlq.ai](https://mlq.ai/news/klarna-ceo-admits-aggressive-ai-job-cuts-went-too-far-starts-hiring-again-after-us-ipo/)).

**Clearest rewrite driver, observed**: coupling between the product's core loop and a specific model's agentic / tool-use behaviour. Notion's rebuild for GPT-5 is the cleanest example; Shopify Sidekick's spring 2025 re-architecture is the second; Cursor's Composer 2 build is a third where the company decided to absorb the rewrite cost by owning the model. *Confidence high.*

---

## 5. Decision tree

Parameters (the five listed in the plan), and their operational ranges:

- **Size**: Solo / SMB (<$1M ARR), Mid ($1M–$100M ARR), Large ($100M–$1B), Enterprise (>$1B or regulated multinational). Roughly aligns with scale-based track tiers S1–S7 but is independent of it.
- **Regulatory posture**: Unregulated, Light-touch (privacy / consumer), Sectoral (healthcare, finance, legal), Strict (defence, national-security, critical infrastructure).
- **Capability requirement**: Frontier-required (complex reasoning, novel code, multimodal), Mixed (mostly extraction / classification / summarisation with occasional frontier), Commodity (classification, extraction, translation at scale).
- **Latency / cost constraint**: Latency-critical (<1s agent turn, high-concurrency), Cost-critical (margins tight, >10M tokens/day), Relaxed (<1M tokens/day, sub-second latency not required).
- **Data-sensitivity tier**: Public / synthetic, Business-confidential, Regulated PII / PHI, Classified / sovereign.

### 5.1 Top-level branches

**Branch 1 — if regulatory posture is Strict *or* data-sensitivity is Classified/Sovereign**
- Default: on-prem or sovereign-cloud, self-host open-weight (Llama, Mistral, DeepSeek where geopolitics permits, Qwen with regional caveats).
- Route frontier / non-sensitive requests via managed API only through an aggregator with contractual data-isolation (e.g. Azure OpenAI with data-protection terms, AWS Bedrock with custom KMS).
- Rebuild budget: assume 3–6 eng-months per major generation turnover; hardware cycle 18–24 months.
- Canonical exemplars: Bloomberg, JPMorgan LLM Suite pattern, Goldman / AT&T / Nomura hybrid Llama additions.
- Failure mode to watch: category drift in "non-sensitive" as agents chain — budget for continuous classification of prompt boundaries.

**Branch 2 — if regulatory posture is Sectoral and size is Large/Enterprise**
- Default: private-cloud aggregator over multiple proprietary providers (Morgan Stanley, Harvey, JPMorgan pattern).
- Add open-weight self-host *only* for the use cases that need data-isolation or fine-tune specificity (Block Cash App pattern).
- Multi-provider routing is default, not optional — vendor-outage survivability matters for SLA.
- Rebuild budget: ~2–4 eng-months per generation turnover if the retrieval and evaluator layers are clean; double that if prompt chains are tightly coupled.

**Branch 3 — if capability requirement is Frontier-required and size is Mid/Large AI-native**
- Default: multi-provider API with automatic routing; invest in eval harness before invest in router.
- Consider proprietary-model build only when inference volume passes the cost-break-even *and* there is a reward-signal advantage to owning the post-training loop (Perplexity, Cursor pattern) — otherwise the build is likely to trail the frontier.
- Rebuild budget: assume 1–2 generation cycles between "can switch in a week" and "need quarter-long rewrite"; target the former.

**Branch 4 — if capability requirement is Commodity and latency/cost is Cost-critical**
- Default: open-weight model through a managed inference provider (Baseten, Fireworks, Together, Modal, Cerebras, Groq where latency is binding) or via Bedrock / Vertex / Azure on open-weight catalog.
- Self-host only above 15–40M tokens/month break-even *and* with operational maturity to serve at that volume.
- A "send 80% to open-weight, 20% to frontier" routing pattern is the observed 2026 default ([Particula](https://particula.tech/blog/deepseek-v4-qwen-open-source-ai-disruption)).

**Branch 5 — if size is Solo/SMB**
- Default: single managed API; no router; no self-host. Switching cost is absorbed by smallness, not avoided by architecture. The solo tier's adaptability comes from willingness to rewrite, not architectural hedge.
- Exception: if data-sensitivity is Regulated PII/PHI, jump to Branch 1 or Branch 2 immediately — do not pass through a consumer-API tier.

**Branch 6 — if the product is an agentic loop with long-horizon reasoning**
- Default: expect a generation-cycle rewrite. Design the agentic schema to be rebuildable rather than stable — Notion's pattern, not Shopify's first-version pattern.
- Route through multi-provider specifically so the long-horizon agent can be swapped to whichever vendor ships the strongest reasoning per generation.
- Consider model ownership only if reward-signal control is core to the moat (Cursor Composer 2 rationale).

### 5.2 Cross-branch invariants

Three architectural commitments hold in *every* branch and are the lowest-regret decisions observed 2024–2026:
1. **A model-agnostic prompt / response layer** (thin adapter between product logic and whichever model serves the call). Minimum artefact: all prompts stored as versioned assets with their own eval suite.
2. **A retrieval and data-governance layer owned by the company, not the model vendor.** This is load-bearing for regulatory compliance *and* for surviving checkpoint retirement.
3. **An evaluation harness that is not itself backed by a model in the main provider's family** (to prevent judge-drift coupling). *Confidence medium* — the cross-pollution failure mode is documented but the mitigation pattern is under-specified in the public corpus.

### 5.3 Decision-table summary

| If these parameters hold… | Default architecture | Rebuild budget per model generation | Watch-out |
|---|---|---|---|
| Strict reg OR sovereign data | On-prem self-host + API for non-sensitive via compliance wrapper | 3–6 eng-months | Hardware vs model cycle mismatch |
| Sectoral reg + Large/Enterprise | Private-cloud aggregator + multi-provider + selective self-host | 2–4 eng-months | Prompt-chain coupling to one vendor |
| Frontier-required + AI-native scale | Multi-provider API + eval harness + optional own-model for moat | 1–2 eng-months | Trailing the frontier if you build |
| Commodity + cost-critical | Open-weight through managed inference; 80/20 route | 1–2 eng-months | Break-even moves with token price |
| Solo / SMB | Single API; no router | days to weeks, absorbed | Premature multi-provider optimisation |
| Agentic long-horizon | Multi-provider + rebuildable agent schema | Generation cycle (a full rebuild) | Tool-schema drift between vendors |

---

## 6. Open questions and negative evidence

- **Engineering-month data is systematically unavailable at Tier A or Tier B quality.** No audited disclosure (10-K, investor letter, regulator filing) breaks out LLM-migration cost in eng-months for any case above. All numbers in §4.3 are Tier C. This is the single biggest evidence gap in the memo.
- **Perplexity, Cursor, Shopify, Notion, Harvey switching cost details are not disclosed publicly** in a way that permits cross-case comparison. Vendor blogs describe *what* changed, not *at what cost*.
- **Downtime during LLM-layer migrations is rarely reported.** Either it is low enough to be uninteresting or companies do not volunteer it. Klarna's reported quality regression is a rare counter-example and even it is not quantified beyond "negatively affected service and product quality."
- **Open-weight "67% of enterprises in production" and 85% / 86% cost-savings figures** come from vendor PR and trade-press sources; none are independent measurements. Treated as *weak signal, not proof*.
- **No observed case of an enterprise moving from self-host back to pure API in 2024–2026.** Motion is either static or toward self-host or multi-provider; the reverse migration is absent from this corpus. May be a genuine absence; may be reporting bias (rollbacks are not announced). Negative-evidence flag.
- **Azure OpenAI / AWS Bedrock / GCP Vertex selection criteria at Fortune 500 scale** are likely gated by existing cloud commits, not by model quality — but the load-bearing evidence for that claim (procurement documents, RFP responses) is not publicly available.
- **The Mistral / Accenture / sovereign-EU sub-pattern** is under-sampled here and deserves its own follow-up — the memo's case table has no clean EU-regulated self-host exemplar.
- **Latency-bound hardware choice** (Groq, Cerebras, Trainium / Inferentia) is under-covered; T2 (compute scaling) is the correct memo to pick it up.
- **Agentic tool-schema compatibility across provider generations** is the most under-documented load-bearing variable — everything points to it being the dominant rewrite driver, but no public study rigorously quantifies the breakage rate.

---

## 7. Feedback to the three-pillar adaptability frame

1. **T1's load-bearing architectural invariants map cleanly onto O2 role questions.** The "model-agnostic prompt layer" and "eval harness decoupled from provider" from §5.2 both require a role that is distinct from both ML engineer and software engineer — the LLM-gateway / eval-infrastructure engineer. O2's role-lifecycle model should treat this as one of the durable roles, not a transient prompt-engineer-rebrand.
2. **The dominant rewrite driver is agentic tool-schema coupling, not prompt text.** This is directly load-bearing for A1 (foundation-model transition management) and A3 (workflow retooling by domain). The A1 decision-tree should weight "is there an agentic loop in production" as a first-class branch, separate from "is there a prompt chain in production."
3. **The build-vs-rent axis is strongly coupled to the O1 human-AI collaboration model.** Harvey's move from OpenAI-exclusive to multi-provider happened at roughly the same time its AmLaw-100 customer base consolidated around Claude-side platforms — customers' model preferences drove the infrastructure choice. Adaptability at T1 is not purely an engineering decision; it is a downstream effect of customer-side AI usage. The three-pillar frame must not treat T1 as upstream of O1 — the causation runs both ways.
4. **Scale tier effects are sharp.** For Solo / SMB (scale-based S1–S2), the right answer is almost always *no router, one provider, absorb rewrite*. For Enterprise / regulated (S4–S6), the right answer is *aggregator + multi-provider + selective self-host*. The memo's decision tree should be cross-referenced with the scale-based track's `comparative-matrix.md` and `size-speed-resource-tradeoff.md` — the tradeoffs are the same variables viewed from two axes.
5. **Negative evidence is itself a finding.** The near-absence of "self-host → pure API" migrations in 2024–2026 is weak but suggestive evidence that infrastructure commitments are asymmetrically sticky — once a company has built a private pipeline it tends to keep it even when the cost gap closes. If this holds on further investigation, it is a *dynamic-capability hysteresis* argument for M1.
6. **For M2 indicator design**: two measurable T1 indicators belong on the adaptability dashboard — (a) *generation-to-production lag* (days from provider's new-model GA to it serving meaningful production traffic inside the company), (b) *rewrite-to-adapter ratio* (fraction of a model-generation turnover that results in a full rewrite vs a swap of the thin adapter). Both are observable in principle from engineering change logs; in practice, will require voluntary disclosure or case-study partnership.

---

*End of memo.*
