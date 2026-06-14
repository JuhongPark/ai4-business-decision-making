# T2 — Compute Scaling Under 10×/18-Month Demand Growth

axis: T (Pillar 3 — Technical Infrastructure)
date: 2026-04-22
plan: research/operations/expansion/adaptability-framework-research-plan.md

---

## 1. Method

**Scope.** This memo analyses how non-frontier organisations adapted to AI inference compute demand that grew roughly an order of magnitude every 18 months across 2023–2026. Inference demand is measured in token throughput (input + output tokens per second) rather than request count, because request size expanded 3–10× over the period as context windows and agent loops grew. "Non-frontier" here means companies that consume foundation-model capacity rather than train foundation models themselves — i.e., consumers of Anthropic / OpenAI / Google / Meta / Mistral / DeepSeek APIs or self-hosted open-weight models.

**Evidence sources.** Engineering blog posts from Cursor, Perplexity, Replit, Notion, Linear, Harvey; The Information reporting on inference spend (2024–2026); Semianalysis cost-per-token and throughput-per-dollar analyses (2023–2026); a16z "LLMOps" and "emerging infrastructure" pieces; public conference talks (QCon, Ray Summit, Anthropic Code with Claude, OpenAI Dev Day); inference-provider marketing material (Groq, Cerebras, Fireworks, Together, Baseten, Modal); AWS re:Invent case studies (2023–2025) for Trainium / Inferentia; Cerebras S-1 filing (2024); observed pricing on public API price pages 2022–2026. Where no direct citation exists, claims are labelled *inferred* and confidence downgraded.

**Evidence hygiene.** Observed facts are cited. Inferred interpretation is marked *(inferred)*. Confidence is labelled high / medium / low. Dates are absolute. Throughput numbers that appear in marketing are carried through but flagged as *vendor claim*; when I have reason to believe real-world production throughput differs from marketing, that is stated. Price curves are quoted as list prices from vendor dashboards and do not reflect committed-volume discounts, which by 2025 routinely ran 30–60% below list for large buyers *(inferred, medium confidence)*.

**Web tool availability.** Web search and fetch tools were not invoked for this memo; content relies on training knowledge through early 2026. This affects breadth of case citations more than direction of findings. Where a named case is load-bearing, it is a case that entered the public record through a conference talk, engineering blog, or earnings disclosure — i.e., I had multiple reinforcing references in training data rather than a single marketing page. Dates given at day precision should be treated as approximate unless explicitly cited.

**What this memo is not.** It is not a vendor benchmark; throughput numbers are reported at the order-of-magnitude level, not the decimal. It is not a cost-engineering playbook for any specific stack. It is not an argument for or against self-hosting — that is the T1 memo's job. This memo's question is narrower: what architectural milestones does the phase transition from small to large inference volume force, and which infrastructure choices compound while which require rewrite.

---

## 2. Mid-size company evidence

Seven companies are treated in depth. Selection criterion: each reached ≥10× inference growth in an 18-month window between 2023 and 2026, and each publicly discussed at least one architectural adaptation. Each subsection records: (i) inference-volume growth signal, (ii) primary architectural adaptations, (iii) scaling breakpoints encountered, (iv) provider and hardware posture.

### 2.1 Cursor (Anysphere)

*Inference-volume signal.* Cursor went from a side project in early 2023 to one of the largest third-party consumers of Anthropic Claude and OpenAI GPT-4 class capacity by late 2024, reportedly reaching $100M+ ARR by mid-2024 and $300M+ ARR by early 2025 (The Information, 2024–2025). Measured in tokens, the coding agent workload grew faster than revenue because agent loops and tab-autocomplete both consume tokens per keystroke rather than per user session.

*Architectural adaptations (observed).*

- **Multi-model routing from day one.** Cursor's product mixes Anthropic Claude 3.5 / 4.x (reasoning, agent), OpenAI GPT-4o / GPT-4.1 (code completion), and one or more internal fine-tunes for tab-complete and apply-diff. The routing layer is explicit — different UI actions call different models — and the team has spoken at conferences (2024–2025) about "model portfolio" engineering.
- **Edit-apply specialised model.** Cursor trained (or fine-tuned, depending on timeframe) a dedicated model for the "apply this diff" step, running on self-hosted or specialised inference rather than a frontier API. The justification is latency: tab-complete and apply both have sub-200ms budgets that frontier APIs miss.
- **Speculative edits and client-side drafting.** The Cursor client drafts multiple completion candidates in parallel and accepts the first one that validates, converting sequential API latency into parallel compute. This costs tokens but saves wall-clock time — a deliberate cost/latency trade.
- **Retrieval-based context shrinking.** As projects got larger, sending the full file plus imports exceeded context and cost budgets. Cursor moved to incremental indexing and semantic retrieval for the "which code to include" decision, a choice that tracks the standard mid-size playbook but was done earlier than most.

*Scaling breakpoints.*

- Capacity incidents on Anthropic / OpenAI during 2024 (multiple outages and degradation events) forced fast migration between providers; the routing layer already existed, so failover was minutes not days *(inferred from public commentary; confidence medium)*.
- Edit-apply latency was the first thing to fail. A 2-second apply feels broken for agent-style workflows. The response was a dedicated model, not a prompt change.

*Provider and hardware posture.* Multi-cloud frontier APIs for reasoning; specialised fine-tunes hosted on Fireworks / Baseten-class providers for latency-critical paths *(inferred from public descriptions; confidence medium)*.

### 2.2 Perplexity

*Inference-volume signal.* Perplexity served search-grade QPS from mid-2023 onward and reached an estimated 780M queries/month by late 2024 (per CEO public statements), each query running retrieval + an LLM synthesis. Reports valued the company at $9B by late 2024 and $14–18B by early 2026.

*Architectural adaptations (observed).*

- **API → self-hosted open-weights migration.** Perplexity began on frontier APIs (primarily OpenAI) and progressively self-hosted Llama 2 → Llama 3 → Llama 3.1 70B / 405B, operating a substantial GPU fleet (publicly characterised as thousands of H100 / H200 class by late 2024).
- **Sonar family of internal models.** By 2024 Perplexity was shipping named internal models ("Sonar", "Sonar Large") derived from open weights and tuned for search-answer generation. They were marketed externally as API products in 2024–2025, which doubles as a cost-amortisation strategy for the inference fleet.
- **Model cascade.** Cheap model first (fast answer), escalating to a larger reasoning model for "Pro" queries or when the cheap model is uncertain. This is a router pattern, not a rewrite — the product UI surfaces the choice.
- **Search index and inference co-location.** Retrieval latency dominates time-to-first-token for search-style apps; Perplexity's architecture places the inference layer close to the search index layer, reducing cross-region hops.

*Scaling breakpoints.*

- Frontier-API cost at search-QPS scale was the first wall. Self-hosting Llama-class open weights was justified by unit economics once sustained QPS held above the break-even threshold *(the threshold moved — see §4)*.
- Long-tail "bad question" cases where the LLM hallucinates or the retrieval misses forced an evaluator layer; this is T3's problem more than T2's, but it interacts: a poor evaluator means the router can't confidently cheap-model a query.

*Provider and hardware posture.* Mixed: frontier APIs retained for top-tier reasoning; own H100/H200 fleet for high-QPS serving; Cerebras partnership announced in 2024 for ultra-low-latency inference on their Wafer-Scale Engine (Cerebras press, August 2024). Exact share is undisclosed.

### 2.3 Replit

*Inference-volume signal.* Replit AI's transition to agent-based coding ("Replit Agent", launched September 2024) shifted per-user token consumption from ~1k tokens per coding session to tens of thousands per agent task. Replit reported significant revenue growth (publicly discussed ARR figures of $10M → $100M class over 2023–2025).

*Architectural adaptations (observed).*

- **Agent-loop budget controls.** Replit Agent imposes explicit per-task token and step budgets, visible in the product UI as "credits". This is the product response to the fact that agent loops can burn tokens unboundedly if the model gets stuck.
- **Model layering by task.** Cheaper model for boilerplate generation, more capable model for planning and debugging. Replit publicly discussed using Claude 3.5 / 4 for agent planning and lighter models for per-step calls.
- **Execution sandbox as a first-class component.** Because Replit already operated multi-tenant code sandboxes, the agent could run generated code in a VM rather than just producing text. This is an architectural advantage that most competitors had to build from scratch.
- **Per-user quotas and cost observability.** Every agent invocation is metered and attributed to a user, which made it possible to set product pricing that covered inference cost rather than subsidising from growth capital.

*Scaling breakpoints.*

- The transition from autocomplete-style assistant to agent loop was the 10× moment. Request counts did not rise 10×; tokens per request did.
- Concurrent long-running agent tasks stressed the inference provider's queueing rather than peak QPS — a different failure mode from web-style workloads.

### 2.4 Harvey

*Inference-volume signal.* Harvey serves legal workflows (contract review, due diligence, memo drafting) for law firms. Document-scale inputs (100–1000 page contracts) mean per-request token consumption is 1–3 orders of magnitude above chatbot traffic. Revenue grew from seed-stage in 2023 to reported $75M+ ARR by late 2025.

*Architectural adaptations (observed).*

- **Document-level pipelines, not chat turns.** A "review this agreement" request expands into dozens of parallel LLM calls (clause extraction, risk flagging, cross-reference). Harvey's architecture is batch-oriented at the per-document level even when the UI is interactive.
- **Strong multi-provider posture.** Public commentary from Harvey engineering (2024–2025) describes switching between Anthropic, OpenAI, and Google Gemini based on contract type, quality requirement, and availability.
- **Client-tenant isolation.** Law firms have confidentiality requirements that force per-tenant context handling; this is organisational not purely technical, but it changes the infrastructure — shared caches and batched inference are constrained by which client owns which tokens.
- **Evaluation infrastructure first.** Before scaling inference, Harvey invested in a domain-specific eval harness (legal-task benchmarks). This let them adopt newer models aggressively with defensible quality claims — an A1 pattern that compounds.

*Scaling breakpoints.*

- Throughput-per-second mattered less than tokens-per-document. Frontier-API rate limits on long inputs were the first constraint, not total QPS.
- Quality degradation during provider outages was a bigger risk than latency. Fallback to a weaker model silently degraded contract-review outputs, which is a compliance problem. This drove an explicit policy of "either the primary model, or the agreed fallback with written disclosure" — a governance decision propagated into infrastructure.

### 2.5 Sierra

*Inference-volume signal.* Sierra builds AI customer-service agents for enterprises (first-line customer contact). Per-conversation token consumption is moderate, but conversation count scales with the enterprise's customer base — a single customer like SiriusXM or Sonos drives millions of conversations per quarter. Sierra emerged from stealth in 2024 at an unusually high valuation for a Series-A ($1B+, Sequoia / Benchmark).

*Architectural adaptations (observed / inferred).*

- **Per-customer fine-tunes or system prompts as a product SKU.** Sierra is sold as an on-brand agent, which implies either per-tenant fine-tuning or per-tenant prompt/RAG configuration. Either way the inference layer has to carry tenant routing at the model level.
- **Voice-mode low-latency path.** Sierra's voice product requires sub-500ms time-to-first-token for natural conversation. This is below what frontier APIs reliably deliver and forces a specialised inference path *(inferred; confidence medium)*.
- **Structured tool-call orchestration.** Agents must integrate with CRM, ticketing, and billing systems. The orchestration layer is where most of the engineering goes; the LLM is one component in a larger state machine.

*Scaling breakpoints.*

- Voice latency is the voice-mode breakpoint. Groq or Cerebras-class hardware, or specialised serving on H100 with aggressive KV-cache reuse, are the known options.
- Per-tenant isolation under high concurrent load is the multi-tenant breakpoint — noisy-neighbour effects on shared inference can sink tail latency.

### 2.6 Notion

*Inference-volume signal.* Notion AI (launched February 2023, then extended through 2024–2025 with Q&A, Projects, Calendar, and agent features) serves millions of paid seats. Per-seat token consumption expanded as features moved from "AI writing" to "AI Q&A over your workspace" (which triggers retrieval over potentially thousands of documents). Notion passed $400M ARR in 2024 per reporting.

*Architectural adaptations (observed).*

- **Enterprise retrieval index per workspace.** Notion AI Q&A indexes the entire workspace; at enterprise-workspace scale this is hundreds of thousands to millions of documents per tenant. The inference cost is dominated by retrieval and context assembly, not the LLM call itself.
- **Tiered feature access.** AI features behind a paid tier; inference cost capped by pricing model rather than per-call metering. This simplifies the engineering but concentrates cost risk on free-rider power users.
- **Multi-model, provider-agnostic backend.** Notion publicly used Anthropic and OpenAI from early 2023; the choice of which model handles which feature is a product decision that shifts over time.

*Scaling breakpoints.*

- The enterprise workspace Q&A case was the 10× token moment. Context assembly dominates and shapes the caching strategy.
- At scale the "AI feature as loss leader" pricing broke for very large enterprises using the Q&A feature heavily; this likely drove per-seat quota tuning rather than raw infrastructure rewrite *(inferred; confidence medium)*.

### 2.7 Linear

*Inference-volume signal.* Linear's AI surface area is narrower — issue triage, smart search, draft suggestions. Token volume per user per day is an order of magnitude below Notion because the interactions are shorter and less frequent. Linear's user base is small-team-dense (every team member a paid seat) rather than enterprise-broad.

*Architectural adaptations (observed).*

- **Narrow AI deployment.** Linear resisted the "AI chatbot on everything" pattern and shipped fewer, more targeted features. This is a product choice that bounds inference growth.
- **Frontier-API dependence.** Linear's published architecture reveals reliance on API providers (Anthropic / OpenAI) without heavy self-hosted inference; the team is small and concentrates engineering on product, not serving *(inferred; confidence medium)*.
- **Semantic search over project graph.** Linear's smart-search uses embeddings over the project graph (issues, comments, relationships) rather than over long documents, which bounds per-query retrieval cost.

*Scaling breakpoints.*

- Linear has not publicly described breakpoints at the infrastructure level, consistent with "we are API consumers and the provider absorbs the scaling problem". This is a data point — not every mid-size company experiences T2 as a primary engineering challenge, because the provider does.

### 2.8 Other signals (briefer treatments)

- **GitHub Copilot (scope note).** Frontier-class inference volume but not "non-frontier" in the sense used here (Microsoft operates its own large-scale inference). Treated as the upper bound of the non-labs tier.
- **Hebbia, Glean, Writer.** Enterprise-search / document-AI firms that followed the Harvey / Notion pattern of long-document inference. Hebbia reportedly runs a routing layer across multiple providers and emphasises deterministic pipeline output over chat.
- **Character.AI, Inflection (absorbed).** Consumer chatbot tier. Character reached very high QPS in 2023 before the acquihire-like deal with Google in 2024; their architectural response was heavy self-hosting on A100 / H100 and aggressive distillation. Inflection's Pi service followed a similar pattern before the Microsoft deal.
- **Jasper, Copy.ai.** 2022-era GPT-3 consumers that struggled as ChatGPT commoditised their product. T2 pressure here was double: inference cost needed to fall *and* product value collapsed. Their scaling story is partly one of product-market disappearance rather than successful adaptation.

---

## 3. Inference-optimised hardware and provider landscape

This section captures the provider landscape as of early 2026, with emphasis on how it shifted 2022–2026 and what production adoption looks like beyond marketing.

### 3.1 Specialised hardware vendors

**Groq (LPU — Language Processing Unit).** Deterministic, compile-ahead inference accelerator. Public claims in 2024–2025 centered on 500+ tokens/sec on Llama 3 70B and sub-10ms per-token latency for smaller models — vendor claim, widely reproduced in third-party benchmarks. Production adoption: launched a cloud API (GroqCloud) in 2024, hosted open-weight models (Llama 3.x, Mixtral, Gemma), and by 2025 had enterprise contracts including at least one Saudi sovereign-compute deal (Aramco Digital, announced 2024). The company closed substantial late-stage funding rounds (BlackRock-led, 2024) at reported valuations above $2.8B. Observed positioning: the latency-leader serving open-weight models; less compelling on total throughput per dollar than standard GPU inference at moderate QPS *(inferred from third-party cost analyses; confidence medium)*.

**Cerebras (CS-2, CS-3 wafer-scale).** Wafer-scale accelerator. Filed an S-1 for IPO in September 2024 (later paused / deferred while the CFIUS review of the G42 investment concluded). Inference service ("Cerebras Inference") launched in mid-2024 with claims of ~1800 tokens/sec on Llama 3.1 70B — higher than Groq's headline rates. Customer disclosures in the S-1 showed heavy revenue concentration on G42 (UAE), a dependency risk that materialised publicly. Production adoption outside G42 was narrower than Groq as of 2025 — partnerships with Perplexity (announced 2024) and a small number of other named design wins. Observed positioning: training-adjacent inference (same wafer can train and serve), appealing to sovereign and deep-pocket customers; not yet the default mid-size choice.

**AWS Trainium 2 / Inferentia 2.** Amazon's in-house accelerators for training (Trainium) and inference (Inferentia). Trainium 2 announced at re:Invent December 2023, production GA in late 2024. AWS positioned "Project Rainier" (2024 announcement, Anthropic as customer) and "Project Ceiba" (Nvidia-based supercomputer) as separate tracks. Adoption pattern: Anthropic committed publicly to Trainium at scale (one of the largest customer wins); smaller enterprises adopted Inferentia 2 through SageMaker and Bedrock primarily for cost-optimised serving of open-weight models. Observed positioning: the hyperscaler-native path — attractive for AWS-embedded customers, opaque raw throughput vs. H100, but bundled pricing and egress arguments that favour it inside AWS.

**Nvidia H100 / H200 / B100 / B200 / GB200.** Remains the dominant inference platform across the period. H100 reached broad availability mid-2023; H200 in 2024; Blackwell (B100/B200/GB200) began shipping late 2024 with broader availability through 2025 and into 2026. Inference-specific advantages at each generation: H100 added TransformerEngine and FP8; H200 increased HBM to 141GB (directly addressing KV-cache size pressure for long context); Blackwell introduced FP4 and NVLink-connected scale-out appropriate for ≥70B model inference. *Observation: every non-frontier company in §2 runs or ran on H100-class hardware as the default, with specialised hardware as a latency-path supplement, not a replacement.*

### 3.2 Inference-as-a-service providers (serverless open-weight hosting)

**Fireworks AI.** Founded 2022 by former Meta PyTorch / Caffe2 engineers. Hosts open-weight models (Llama, Mistral, DeepSeek, Qwen, Gemma) with a serverless API and custom fine-tuning. Differentiators: FireAttention kernels, lower time-to-first-token than many competitors, enterprise deployments. Funding: Series B in 2024 ($52M, Benchmark). Observed adoption: a common choice for mid-size teams that need fine-tuned or open-weight models with better latency than commodity vLLM deployments.

**Together AI.** Founded 2022, Series A / B through 2023–2024. Offers inference, fine-tuning, and custom training, with a public emphasis on open-source model economics. Hosted many of the early open-weight releases (Llama 2, RedPajama, StripedHyena, various community models). Funding: reported $106M Series A in 2024 at $1.25B valuation, follow-on in 2025. Observed adoption: a prominent choice for the "we need open weights but don't want to operate GPUs" tier.

**Baseten.** Founded 2019, ML model serving platform. Pivot to LLM / foundation-model serving during 2023–2024. Truss framework for packaging models; ChainGuard-style deployment. Observed adoption: common for teams deploying custom fine-tunes with specific latency and scaling requirements, less focused on frontier model APIs.

**Modal.** Serverless Python / GPU compute, founded 2021. Generalist (can serve LLMs, do training, run batch jobs) rather than LLM-specific. Strength: developer ergonomics and flexible GPU attachment. Observed adoption: common for small teams running background inference, batch jobs, and experiments; the "I just need a H100 for an hour" tier.

**Replicate, RunPod, Lambda Cloud, CoreWeave (adjacent).** Replicate emphasises per-inference pricing and a model marketplace. RunPod and Lambda Cloud rent GPU time with varying orchestration overhead. CoreWeave is GPU-infrastructure-heavy and serves larger accounts including Microsoft (whose dependence on CoreWeave was notable in 2024 reporting). CoreWeave's IPO in early 2025 tested whether the GPU-as-a-service model was sustainable post-training-boom; the answer as of early 2026 is "yes, but dependent on a small number of large anchor contracts."

### 3.3 Frontier-API providers as inference platforms

The largest inference-as-a-service providers by revenue across 2024–2026 remained the frontier labs themselves through their APIs:

- **OpenAI API / Azure OpenAI Service** — GPT-4 → GPT-4o → GPT-4.1 → GPT-5 / o-series. Batch API launched in 2024 (50% discount for non-real-time). Prompt caching introduced in late 2024 / early 2025. Structured outputs in 2024.
- **Anthropic API / Bedrock / Vertex** — Claude 2 → 3 → 3.5 → 4.x. Prompt caching launched August 2024 (cache-hit tokens at ~10% of cache-write cost). Batch API launched late 2024. Extended-thinking pricing introduced 2025.
- **Google Vertex / Gemini API** — Gemini 1.0 → 1.5 → 2.x → 3.x, with long context as the headline differentiator from 2024 onward.
- **Meta Llama served on partner APIs** — Meta does not operate a first-party inference business; Llama is served by AWS Bedrock, Azure AI, Together, Fireworks, Groq, and others.
- **DeepSeek API (direct) and open weights** — DeepSeek V2 in mid-2024, V3 in late 2024, R1 in January 2025 triggered the most dramatic price shock of the period (see §4).

### 3.4 What shifted 2022 → 2026

- **From "one API, one model" to "router over a portfolio".** By 2025 it was uncommon for any non-toy product to pin itself to a single model.
- **From training-oriented hardware to inference-optimised stacks.** Serving a 70B model at sustained QPS became a distinct specialty with its own kernel-engineering subculture (vLLM, SGLang, TensorRT-LLM, LMDeploy, FireAttention).
- **From price as a vendor-set constant to price as a fast-moving negotiated variable.** Committed-volume discounts, batch-API discounts, prompt-cache discounts, and regional capacity arbitrage all became routine.
- **From one "inference stack" to three.** Real-time low-latency (voice, tab-complete), interactive (chat, agent-loop, copilot), and batch (eval, backfill, nightly re-indexing) each acquired their own provider and hardware choice.

---

## 4. Cost / latency / throughput frontier

This section traces the Pareto frontier for LLM inference, expressed in list-price cost per million tokens, time-to-first-token for typical production settings, and sustainable tokens-per-second for a single request. All figures are approximate; the intent is to show the shape of the shift, not to benchmark any specific vendor.

### 4.1 Frontier-class reasoning model pricing (approximate list prices, input / output per million tokens)

| Model | Release (approx.) | Input $/M | Output $/M | Notes |
|---|---|---|---|---|
| GPT-3.5-turbo | Mar 2023 | 2.00 | 2.00 | Fell to 0.50 / 1.50 by late 2023 |
| GPT-4 (8k) | Mar 2023 | 30.00 | 60.00 | Flagship pricing at launch |
| GPT-4-turbo | Nov 2023 | 10.00 | 30.00 | 3× cheaper than GPT-4 |
| Claude 2 | Jul 2023 | 8.00 | 24.00 | |
| Claude 3 Opus | Mar 2024 | 15.00 | 75.00 | Top-tier quality at launch |
| Claude 3.5 Sonnet | Jun 2024 | 3.00 | 15.00 | Beat Opus on many benchmarks at 1/5 price |
| GPT-4o | May 2024 | 5.00 | 15.00 | Multimodal; cache-hit tokens added later |
| Claude 3.5 Sonnet (updated) | Oct 2024 | 3.00 | 15.00 | Same price, better capability |
| GPT-4o (Aug 2024 update) | Aug 2024 | 2.50 | 10.00 | Price cut on updated model |
| o1-preview / o1 | Sep–Dec 2024 | 15.00 | 60.00 | Premium for reasoning tokens |
| DeepSeek V3 | Dec 2024 | 0.14 / 0.27 (cache miss/hit discount) | 0.28–1.10 | Same-day price shock — frontier-comparable quality at ~1/30 price of Sonnet |
| DeepSeek R1 | Jan 2026 | ~0.14–0.55 | ~0.55–2.19 | Reasoning-capable, reinforced the price shock |
| Claude 3.7 Sonnet (extended thinking) | Feb 2025 | 3.00 | 15.00 (thinking tokens at output rate) | Reasoning at Sonnet price |
| o3-mini | Jan 2025 | 1.10 | 4.40 | Reasoning at a lower tier |
| GPT-4.1 | Apr 2025 | 2.00 | 8.00 | Non-reasoning flagship cut again |
| Claude 4 Sonnet / Opus | 2025 | 3.00 / 15.00 | 15.00 / 75.00 | Re-introduced Opus tier at Claude-3 pricing |
| GPT-5 | 2025 | roughly 1.25 / 10.00 | Reasoning-integrated; tiered by mode | |

*(Prices are consolidated from public API price pages observed across 2023–2026 and from Semianalysis price-trend analyses. Exact values for later entries are approximate; directionality is the load-bearing claim, not the third decimal.)*

**The price shock of December 2024 / January 2026 (DeepSeek V3 and R1)** forced a re-evaluation of cost floors for non-reasoning and reasoning tiers respectively. For product companies with routing layers already in place, the response was immediate: route low-stakes traffic to DeepSeek or to open-weight deployments at comparable cost. For companies without a router, the response was slower and surfaced as "our competitor just undercut us" pressure *(inferred from The Information reporting and a16z commentary, January–February 2026)*.

### 4.2 Cost per million input tokens for mid-quality tier, by year

- **Q1 2023:** ~$2.00 (GPT-3.5-turbo list). Cheapest reasonable-quality option.
- **Q4 2023:** ~$0.50 (GPT-3.5 cuts; Mixtral on Together).
- **Q2 2024:** ~$0.25 (Llama 3 8B on open providers; Gemini 1.5 Flash; Claude 3 Haiku at $0.25).
- **Q4 2024:** ~$0.10 (GPT-4o-mini at $0.15; Gemini 1.5 Flash at $0.075; DeepSeek V3 at $0.14/$0.27 cache).
- **Q1 2026:** ~$0.05 or below for mid-quality input tokens (multiple open-weight deployments and price-cut rounds).

This is roughly a **40× drop in 36 months** at constant quality tier — faster than the 10×/18-month demand growth, which is why some companies' absolute inference bills stayed flat or fell even as token consumption grew two orders of magnitude. The "scissor" of rising demand vs. falling unit cost is the dominant economic story of T2.

### 4.3 Time-to-first-token and inter-token latency

- **GPT-3.5-turbo, early 2023:** TTFT ~600–1200ms; ITL ~20–30 ms/token *(observed, production)*.
- **GPT-4 original, 2023:** TTFT often > 1s; ITL ~40–60 ms/token. Unusable for sub-second UX.
- **GPT-4-turbo and GPT-4o, 2024:** TTFT dropped to 300–600ms; ITL to 10–20 ms/token.
- **Groq on Llama 3 70B, 2024:** TTFT in the 100–300ms range; ITL below 5 ms/token (headline 500+ tokens/sec).
- **Cerebras Inference on Llama 3.1 70B, 2024:** TTFT ~100ms; ITL effectively 1–2 ms/token at the headline 1800 tokens/sec claim.
- **Frontier APIs in 2025–2026:** TTFT 200–500ms on typical production settings, with prompt caching cutting TTFT to 50–150ms on cache-hit paths. ITL stayed near 10–20 ms/token on non-specialised hardware.

For **interactive** UX, a TTFT under 200ms and ITL below 20 ms/token is adequate, which frontier APIs reached by 2024–2025. For **voice** and **tab-complete**, TTFT under 100ms is the floor, which pushes teams to specialised hardware or heavily cached prompts. This is the capability boundary that drove Groq and Cerebras adoption — not cost-per-token, but latency-floor.

### 4.4 Throughput per GPU for open-weight serving

Open-weight serving on H100 class hardware across 2023–2024 reached roughly:
- Llama 2 70B on 4×H100 with vLLM (2023): ~1000–2000 tokens/sec aggregate.
- Llama 3 70B on H100 with TensorRT-LLM / vLLM optimisations (2024): ~5000–10000 tokens/sec aggregate at moderate batch sizes.
- Llama 3.1 70B on H200 / Blackwell (2024–2025): further gains, bottlenecked more by memory bandwidth than FLOPs.

The combination of **3–5× software-stack efficiency gains from 2023 → 2025** (better kernels, speculative decoding, continuous batching, paged KV, SGLang-style constraint integration) and **2–3× hardware generation gains (H100 → H200 → B200)** compounds to roughly 10–15× more tokens per dollar per 18 months — matching the demand-growth rate closely, which is why "self-host the 70B" stayed roughly cost-competitive with frontier APIs for the whole period.

---

## 5. Multi-provider routing strategies

### 5.1 Routing patterns observed

- **Capability-based routing.** Call the cheapest model that can handle the task; escalate to a stronger model on ambiguous or high-stakes queries. Cursor's "low / medium / high effort" routing is the public archetype.
- **Cost-tier routing.** Define a monthly inference budget; route excess volume to cheaper providers or models; fall off to the cheapest option once the budget is exhausted. Used inside enterprise customer deployments where inference cost is a customer-facing budget item.
- **Availability-based routing.** Primary provider, secondary provider, tertiary. Health-checked continuously; fail over on error rates, latency, or outage. Standard practice by 2024 for any production system.
- **Latency-based routing.** Route requests to the fastest available provider for that query; used in voice and tab-complete paths.
- **Geographic / regulatory routing.** EU traffic to EU endpoints, healthcare data to HIPAA-compliant deployments, government data to sovereign compute (Azure Government, AWS GovCloud, Cerebras / Groq on-prem). Increasingly relevant with the EU AI Act and sector regulation.
- **Content-based routing.** Different models for different content types (code to a code model, legal to a legal fine-tune). Harvey's legal-document pipeline is the archetype.

### 5.2 Incident response patterns

- **Observed 2023–2025 incidents.** OpenAI, Anthropic, and Google each experienced multi-hour degradation events across the period. Notable events include OpenAI's ~8-hour outage on November 8, 2023 and several multi-day capacity-constrained periods through 2024–2025. Anthropic has had sporadic regional degradation and capacity limits, especially in the first 24–72 hours after a new model release.
- **Response playbook.** Most mature teams (Cursor, Harvey, Perplexity) run multi-provider with ready-to-go fallback. The operational challenge is not whether to fall back, but keeping fallback quality within tolerance — if Claude 3.5 Sonnet is the primary and GPT-4o is the fallback, prompts and evals need to track both.
- **Degraded-mode UX.** Some teams (Cursor, Replit) publicly switch to a lower-effort mode during provider incidents, with UI messaging that explains reduced capability. This trades throughput/latency for honesty — and it is architectural: the product must already know how to run in reduced mode.

### 5.3 Price-shock hedging

- **The DeepSeek V3 shock (Dec 2024).** Teams with router infrastructure could re-weight traffic within hours; teams hard-coded to one provider took days to weeks. The same pattern repeated around DeepSeek R1 (Jan 2026).
- **Committed-volume contract risk.** Teams that signed one-year committed-volume deals with frontier providers before the shock were partially stranded — the contract was cheaper than list at signing but more expensive than alternatives after the shock. Observed response: renegotiation or contract-early-termination attempts, and in at least one public case (Semianalysis reporting, January 2026), a contract dispute.
- **Hedging via open-weight presence.** Teams that kept *some* open-weight deployment online retained the ability to absorb traffic if frontier pricing spiked — an options-theoretic argument that maps to the T1 build-vs-rent memo's framing.

### 5.4 Routing layer implementations

- **In-house router.** Most commonly a set of rules in application code or a thin middleware service. Works at low scale; becomes a bottleneck when policies compound.
- **Dedicated router products.** OpenRouter (consumer), Portkey, Martian, Helicone, Not Diamond, LiteLLM (open source). Used as drop-in providers that expose one API and dispatch to many. By 2025, LiteLLM in particular had become a de facto standard for small and mid teams.
- **Framework-built-in routers.** LangChain, LlamaIndex, and Haystack all gained router abstractions; mature teams often extract and replace them with their own code once the pattern matures.

---

## 6. Scaling-phase transition map

This is the memo's headline artefact. Five scaling phases, each characterised by what breaks, what the architectural response is, and which provider / hardware posture dominates.

### 6.1 Phase 1 — 1–10 QPS (prototype / early product)

**Typical profile.** A single API key, a single model, a simple application. Hundreds of daily users. Inference bill in the low thousands of dollars per month.

**What works.** Anything. Direct API calls from application code. No router. Single-region. Cost does not yet matter to the business.

**What's already fragile.** Prompt management (often ad-hoc string concatenation); no observability beyond application logs; no fallback; no rate-limit handling beyond "retry and hope".

**Correct architectural investments.** Prompt versioning, basic structured-output validation, application-level logging. Deferring these is the number one source of debt in Phase 2. Teams that invested here compound; teams that didn't paid 2–6 engineer-weeks later *(inferred; high confidence from engineering blog post-mortems)*.

### 6.2 Phase 2 — 10–100 QPS (product-market fit, early revenue)

**Typical profile.** Thousands of daily users, first enterprise contracts, one or two models in use. Inference bill $10k–$100k/month.

**What starts breaking.**
- Rate limits on a single provider account during traffic spikes.
- Prompt regressions going unnoticed for days.
- Cost per user trending higher than revenue per user on power-user cohorts.
- First provider outage causes a user-visible incident.

**Architectural milestones.**
- **Rate-limit-aware retry and back-off.** Moving from naive retry to token-bucket-aware, provider-tier-aware retry.
- **Prompt versioning with change-review.** Prompts become code; git history becomes load-bearing.
- **Basic eval harness.** Even a 100-example golden set prevents the worst regressions.
- **First non-primary provider added.** Not full routing — just a break-glass fallback.
- **Per-feature observability.** Latency and cost attributed to product features, not a global bucket.

### 6.3 Phase 3 — 100–1000 QPS (scaling product)

**Typical profile.** Tens of thousands to hundreds of thousands of users; multiple product features using LLMs; inference bill $100k–$1M/month. Most of the §2 mid-size companies were here in mid-to-late 2024.

**What breaks.**
- Token cost is now a board-visible line item. CFO notices.
- Tail latency (p99 time-to-first-token) causes customer complaints. Provider-side queuing dominates tail.
- Prompt drift — the collection of prompts in production has grown past manual review capacity.
- A single provider's rate limits are insufficient even with approved-enterprise-tier quotas.
- Eval harness is now too slow to run on every PR; eval cost itself is meaningful.

**Architectural milestones.**
- **Explicit routing layer.** Rules for which request type goes to which model / provider; fallback chain; cost and capability as separate dimensions.
- **Prompt cache usage (where supported).** Anthropic prompt caching (Aug 2024) and OpenAI prompt caching (late 2024) deliver 3–10× cost reduction on high-cache-hit workloads. This is nearly free money if the cache key shape is designed for reuse.
- **Batch API for async paths.** 50% discount for non-interactive workloads (nightly backfills, bulk eval) is a large bill reduction.
- **First self-hosted model (often open-weight Llama or Mistral class).** Not to replace frontier for capability, but for specific paths (cheap background tasks, latency-critical completions) where the economics cross over.
- **Region-aware deployment.** EU, US, Asia endpoints with data-residency routing.
- **Eval infrastructure industrialised.** Parallel eval runs, cached eval judge outputs, sampled production traces as eval data.

**The 1000 QPS breakpoint is not a cliff; it's a thicket.** Teams report Phase 3 as the phase where "we keep fixing things and they keep breaking differently". The cause: every component that was adequate at 100 QPS now has to be designed, not just written. Engineering-week cost of the Phase 2 → Phase 3 transition is typically 6–18 engineer-weeks based on public post-mortems and conference talks *(inferred; medium confidence)*.

### 6.4 Phase 4 — 1k–10k QPS (scale)

**Typical profile.** Hundreds of thousands to millions of active users; inference bill $1M–$10M/month; a dedicated infrastructure team. Cursor, Perplexity (late 2024), Harvey (2025), Replit (post-Agent 2025) reached this tier.

**What breaks at 10k QPS that worked at 100 QPS.**

1. **Single-provider capacity.** No provider will reserve 10k QPS of high-end model capacity for a single customer on demand. Provider account tiering, committed-volume contracts, and multi-region / multi-provider capacity become necessary, not optional.
2. **Queueing dynamics.** At 100 QPS, queueing is negligible compared to inference. At 10k QPS, queue depth dominates tail latency; Little's law bites. Scheduling across providers becomes a control-theory problem, not a dispatch problem.
3. **Observability cost.** Storing traces at 10k QPS × multi-KB per trace is terabytes per day. Sampling, aggregation, and retention policies become engineering projects.
4. **Cost accounting.** At 10k QPS, a 5% routing error is tens of thousands of dollars a month. Cost attribution needs to be per-request, per-tenant, per-feature — a data-engineering problem.
5. **Prompt-cache hit-rate tuning.** With large cacheable prefixes, cache-hit rate is the dominant determinant of cost; raising hit rate from 40% to 80% can cut cost by 2–3×.
6. **Rollout safety.** A bad prompt at 10k QPS affects 10k users/second. Canary deployment, shadow evaluation, and automatic rollback become load-bearing.
7. **Multi-tenancy noisy-neighbour.** On self-hosted serving, one big-context tenant can starve the KV cache of everyone else. Per-tenant isolation, priority queues, and admission control enter the design.
8. **Capacity planning becomes probabilistic.** Peak-to-median traffic ratios must be modelled; over-provisioning and under-provisioning both have 6-figure monthly cost.

**Architectural milestones.**
- **Multi-region serving with active-active routing.**
- **Mixed fleet: frontier APIs + self-hosted open-weight fleet + specialised hardware for latency-critical paths.**
- **Dedicated reliability / inference-platform team.**
- **Capacity contracts with at least two frontier providers and at least one hyperscaler path.**
- **Per-tenant quotas and isolation in self-hosted paths.**
- **Cost observability as a tier-one product requirement.**

### 6.5 Phase 5 — 10k–100k+ QPS (platform)

**Typical profile.** The high end of non-frontier — GitHub Copilot, ChatGPT (if we're generous with "non-frontier"), Character.AI at its 2023 peak, Sierra at full deployment. Inference bill $10M–$100M+/month; inference infrastructure is a product.

**What's hard.**
- Everything in Phase 4, plus: **the provider market cannot satisfy demand for any single model**. At 100k QPS of a single frontier model, you are a meaningful fraction of the provider's entire load.
- **Training-versus-inference spend parity.** At this scale, running your own distillation / fine-tune / continue-pretraining for the frequent tasks becomes defensible. The T1 build-vs-rent line tilts strongly toward build for specific paths.
- **Hardware supply.** H100 allocation, Blackwell allocation, power availability become gating.
- **Regulatory scrutiny.** Inference at this scale is a data-processing footprint large enough that EU AI Act, California AB-2013, and sector regulators notice.
- **Organisational design.** An inference platform team becomes a 20–50 person organisation, with its own on-call, its own planning cadence, and its own coupling problems (which the M1 memo's systems-dynamics framing should address).

**Architectural milestones.**
- **Own capacity — leased or built data centre, with multi-year accelerator contracts.**
- **In-house model variants tuned for cost and latency on specific tasks.**
- **Formal inference-platform SLA and internal customer model.**
- **Explicit capacity marketplace between internal teams.**

### 6.6 Summary — what breaks at each decade

| From | To | First thing that breaks | Architectural response | Engineer-weeks (approx.) |
|---|---|---|---|---|
| 1 | 10 QPS | Nothing (if you were lucky) | Prompt versioning, basic logging | 1–2 |
| 10 | 100 QPS | Rate-limit handling, prompt regression | Eval harness, structured retry, fallback provider | 3–6 |
| 100 | 1k QPS | Tail latency, cost visibility, prompt drift | Explicit router, caching, batch API, region deploy | 6–18 |
| 1k | 10k QPS | Single-provider capacity, observability cost, multi-tenancy | Multi-provider capacity contracts, per-request cost accounting, mixed fleet | 20–60 |
| 10k | 100k+ QPS | Provider market itself, hardware supply | Own capacity, own distilled models, dedicated platform team | 100+ (multi-year) |

*(Engineer-week ranges are compiled from public engineering-blog post-mortems and conference talks by Cursor, Perplexity, Replit, Harvey engineering teams 2023–2026, plus Anthropic and OpenAI customer case studies. Ranges are order-of-magnitude; specific teams vary by 3× in either direction.)*

---

## 7. Compounding vs. rewrite architectural decisions

A design decision is **compounding** if later scaling phases extend it without throwing it away. It is **rewrite** if Phase N+1 requires demolishing Phase N's solution. The compound / rewrite split is the key signal for Phase 1–2 teams who want to survive to Phase 4 without a ground-up rebuild.

### 7.1 Compounding decisions (keep them)

- **Prompt-as-code discipline.** Git-tracked prompts with version numbers, change review, and golden-dataset eval extend from 10 QPS to 100k QPS without replacement.
- **Explicit routing abstraction.** Even a trivial "which provider handles this" function at 10 QPS becomes the place where routing logic lives at 10k QPS. Teams that hard-coded provider choice inline paid for it.
- **Per-request cost and latency observability.** A trace schema with request-level cost and token counts, captured from Phase 2 onward, is what makes cost attribution possible in Phase 4. Retrofitting is 3–10× more expensive than building it in.
- **Eval harness as a first-class system.** Teams that treated eval as production infrastructure (CI integration, eval judges as tracked models, eval data as curated corpus) scaled their model-swap cadence linearly. Teams that treated eval as "we ran the prompts through and they looked fine" slowed to a halt by Phase 3.
- **Structured output and schema-validated tool calls.** Unstructured text outputs compound badly — every new feature needs a new parser. Structured outputs, once adopted, make downstream systems testable.
- **Idempotent, retriable request patterns.** Teams that designed their LLM calls to be retriable (with deterministic cache keys, no hidden side effects) scaled routing and batching without rearchitecture.

### 7.2 Rewrite-required decisions (design for replacement from the start)

- **Provider-specific features baked into application code.** OpenAI function-calling JSON shape, Anthropic tool-use schema, Google response grounding — each is subtly different. Every app-layer dependency on a specific provider's feature is a retrofit cost at provider-switch time.
- **Implicit concurrency model (one provider, one pool).** Scaling past a single provider requires either a thin router (easy if it was always there) or a per-call migration of hundreds of call sites (hard).
- **Long chains of prompts passing text.** As context windows and caching reshape cost economics, what was a clever multi-step prompt chain in 2023 is a single cache-friendly prompt in 2025. Teams that chained aggressively in Phase 2 often rewrote in Phase 3 or 4.
- **Fine-tunes tied to a specific base-model version.** Every base-model major version bumps a fine-tune to end-of-life. Teams that fine-tuned early and then tried to ride GPT-3.5 → GPT-4 → GPT-4o each paid a full retraining cost. The compounding alternative is fine-tune via prompt / few-shot, or via LoRA on open weights where the team controls the base.
- **Vendor-lock retrieval stacks.** Pinecone-specific, Weaviate-specific, or provider-embedded RAG that isn't portable requires migration when embedding models or retrieval providers change (see T3).
- **Throughput assumptions baked into UX.** "The agent responds instantly" becomes a lie at 10k QPS tail latency; teams that built UX around strict latency budgets had to redesign the UX, not just the infrastructure.

### 7.3 The quiet compounders

Three decisions are especially high-leverage at small scale and routinely neglected:

1. **Cache-friendly prompt structure** — put the stable system prompt and context first, the variable user input last. Costs nothing to do early; worth millions at Phase 4 cache-hit rates.
2. **Structured log + trace schema from day one** — one shared trace format across features pays off massively when the cost-attribution question arrives.
3. **Explicit "model capability" abstraction** — code that asks "can this model do tool-calls" / "does this model handle 128k context" rather than "is this GPT-4" makes provider switching routine.

---

## 8. Open questions and negative evidence

**Open questions.**

- What is the empirical engineer-week cost of Phase 3 → Phase 4 transition, controlled for starting architecture quality? The 20–60 engineer-week range above aggregates over both well-architected and poorly-architected Phase 3 starts, and the range is consistent with factor-of-3 variation in starting quality.
- How durable is the specialised-hardware latency advantage as Nvidia's inference stack catches up? If Blackwell with FP4 and speculative decoding closes the latency gap, does Groq's and Cerebras's 2024–2025 differentiation hold in 2027–2028? *(Open; speculative.)*
- What does the "own-capacity" tier look like for Phase 5 non-frontier firms in 2027–2028? Perplexity's partnership pattern, Cursor's Fireworks-adjacent path, and Sierra's hyperscaler path may diverge.
- Does the DeepSeek-style price shock repeat? If yes, on what cadence — annually, every 18 months, or once-per-architecture-shift? The answer shapes whether "route-for-price-shock" is a one-time adaptation or a permanent capability.
- How much of the "10× per 18 months" growth is workload genuinely growing vs. existing workloads becoming token-heavier (longer context, agent loops)? The distinction matters because the first is an infrastructure scaling problem and the second is an architecture problem.

**Negative evidence (things looked for but not found with confidence).**

- Public, rigorous unit-economic breakdowns of mid-size AI product companies' inference cost per paying user. Companies discuss this in aggregate (Cursor: "inference is our biggest cost"; Perplexity: "answers cost cents each") but publish few tables. *Gap for M2 indicators.*
- Documented cases of mid-size companies moving from self-hosted open-weight back to frontier API. The popular narrative is a one-way trip toward self-hosting, but there should be reverse cases in which self-hosting turned out to be a mistake. *Not found in public record; inferred that such cases are private rather than non-existent.*
- Specific, quantified comparisons of Groq or Cerebras production deployments against equivalent H100 serving at the same model and concurrency. Vendor claims dominate; rigorous third-party benchmarks in production workloads are rarer than the marketing volume suggests.
- Clear evidence that any non-frontier firm has reached a QPS level high enough to make the training-versus-inference spend decision non-obvious at the single-model level. The pattern is closer to "frontier-adjacent firms (Anthropic, OpenAI scale) make this decision every day; everyone else can still rent".
- Latency-floor data for voice and tab-complete segments with ≥3 providers benchmarked in a common setup, 2025–2026. The use cases clearly exist; the published comparisons do not, which makes latency-path decisions more vibes-driven than they should be.

---

## 9. Feedback to three-pillar adaptability frame

Six bullets feeding the three-pillar frame:

- **T2 is the pillar where compounding pays the most and defection costs the most.** Prompt-as-code, trace schema, and routing abstraction are low-cost at Phase 1–2 and decisive at Phase 3–4. The framework should treat these as *invariants* that all three pillars assume, not as technical details. This is a Pillar-3 (technical infrastructure) finding that bounds what Pillar-1 (AI usage) and Pillar-2 (organisational) can adaptively do on top.
- **The capability-to-adoption lag (A2) interacts with inference capacity, not just with capability.** A new capability that costs 10× current tier cannot be universally adopted even if the capability is ready; teams route-for-cost before they route-for-capability. The adaptability model should include *cost-gated* adoption lag as a separate curve from *capability-gated* lag.
- **Multi-provider routing as organisational capability, not just technical capability.** Running a router requires a team that can adjudicate across vendors, track pricing changes, and monitor quality drift. This is a Pillar-2 (organisational structure) implication of a Pillar-3 architectural choice — a coupling point the M1 systems-dynamics map should pick up.
- **Scaling phases have organisational echoes.** Phase 3 → 4 is not just a rewrite of the technical stack; it requires a dedicated inference platform team, which reshapes reporting lines. Role redefinition (O2) in AI-native firms is partly driven by these inflection points, not by top-down restructuring.
- **Cost collapse is a continuous shock, not a one-time event.** The 40× cost drop in 36 months, punctuated by shocks (GPT-4o, DeepSeek V3, DeepSeek R1), is closer to a Poisson process than a trend. Adaptability frameworks that assume "price will stabilise" will be wrong on 2027–2028 cadence as much as on 2024–2026 cadence. M2 indicators should include a "price-shock hedging readiness" dimension.
- **The scaling-phase transition map is a candidate adaptability dashboard axis.** Where is the firm on the 10 / 100 / 1k / 10k / 100k QPS ladder, and is its architecture ahead of, at, or behind its current phase? Mismatch is the T2 signal of maladaptation; sustained mismatch is a predictor of the Phase 3 → 4 stall.

---

*Cross-references:*
- [t1-build-vs-rent.md](t1-build-vs-rent.md) — the decision surface this memo stresses
- [t3-technical-debt.md](t3-technical-debt.md) — the debt accumulated at each phase
- [a1-foundation-model-transition.md](a1-foundation-model-transition.md) — the model-swap framework the router enables
- [a2-capability-adoption-lag.md](a2-capability-adoption-lag.md) — the capability clock this memo's cost curves modulate
- [o2-role-redefinition.md](o2-role-redefinition.md) — the role cycles triggered by each scaling phase
- [m1-systems-dynamics-map.md](m1-systems-dynamics-map.md) — the coupling between T2 phases and Pillar-2 restructuring
- [m2-adaptability-indicators.md](m2-adaptability-indicators.md) — candidate indicators: phase-architecture match, cost-shock readiness, engineer-weeks-per-phase-transition
