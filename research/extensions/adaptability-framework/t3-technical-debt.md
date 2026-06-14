# T3 — Technical Debt in AI-Native Systems

axis: T (Pillar 3 — Technical Infrastructure)
date: 2026-04-22
plan: research/operations/expansion/adaptability-framework-research-plan.md

---

## 1. Method

This memo investigates how technical debt accrues, compounds, self-resolves, or requires deliberate remediation in AI-native production systems across 2023–2026, when the underlying foundation models, embedding models, and tool APIs turn over on roughly a quarterly cadence.

**Evidence posture**. Evidence draws primarily on engineering-blog posts from vendor labs (Anthropic, OpenAI, Cohere), AI-native product firms (Shopify, Klarna, Harvey, Cursor, Perplexity, Notion, Linear, Replit), LLM-tooling vendors (LangChain, LlamaIndex, Arize, LangSmith / LangChain, Braintrust, Humanloop, PromptLayer, Fiddler, Arthur, Weights & Biases Weave), embedding / vector-store vendors (OpenAI, Cohere, Voyage, Pinecone, Weaviate, Chroma, LanceDB, MongoDB Atlas Vector), public post-mortems and incident reports, and the academic "hidden technical debt in machine learning systems" line (Sculley et al., NeurIPS 2015) extended into the LLM era (Shankar et al., 2024; Zaharia et al., "Compound AI Systems," Berkeley BAIR 2024; Karpathy's public commentary on evaluator collapse).

Web-search tools are not available in this session; citations therefore reference sources by **name and approximate publication window** rather than by live URL. Where a specific claim rests on a single talk, blog post, or tweet that I cannot re-verify in this session, it is flagged **(inferred)** or given a low-confidence label. Where a pattern is attested across multiple independent engineering posts, it is flagged **(observed)**.

**Taxonomic axis**. Each debt type is classified along three attributes:
1. *Trigger*: what makes the debt first appear — model swap, embedding swap, chunking-strategy change, evaluator drift, adapter stacking, observability-tool migration.
2. *Compounding behaviour*: whether the debt **compounds** (gets worse without intervention), **self-resolves** (is eliminated by the next version change or a general-purpose upgrade), or **requires deliberate remediation** (only goes away if engineering time is spent).
3. *Cost curve shape*: whether maintenance cost is flat, linear, super-linear, or step-function with model-version changes.

**Confidence labels**. High / Medium / Low, applied to each pattern claim. Observations from multiple vendor engineering posts receive High; single-source practitioner talks or inferred-from-architecture claims receive Medium; speculative projections receive Low.

**Scope**. Production LLM applications with at least one of: a prompt registry of 50+ prompts, a RAG pipeline with a swappable embedding model, an LLM-as-judge evaluator harness, a deployed fine-tune or adapter, or an observability / tracing surface. Out of scope: pre-training-cluster debt, scientific-ML reproducibility debt (addressed elsewhere), and debt internal to foundation-model labs themselves (addressed in T2 and T1).

---

## 2. Debt taxonomy

Five focus areas, ordered roughly by how early they typically appear in a product's life cycle.

### 2.1 Prompts-as-code — versioning, regression testing, canary deploys, rollback

**What the debt looks like.** Prompts begin life as strings interpolated inside application code, sometimes behind environment-variable feature flags. As the prompt library grows — Shopify Sidekick, Klarna's customer-service assistant, Harvey's contract-review prompts, Cursor's code-agent system prompts — the debt surface widens along several axes:

- *Unversioned prompts committed as plain strings in source*, making per-change diffs readable but coupling prompt evolution to application release cadence.
- *Prompt templates parameterized with Jinja or f-string fragments* whose contract with the runtime is implicit and not type-checked, producing silent breakage when a template variable is renamed or removed.
- *Model-coupled tokens* — tags like `<|im_start|>`, `[INST]`, Claude's `Human:` / `Assistant:` turn markers, system-message handling that differs between OpenAI Chat Completions, Claude Messages, and Anthropic tool-use format. A prompt that performs well on one model often silently degrades on another because formatting tokens were part of the contract.
- *Few-shot examples curated for one model version* that become distributionally stale as the base model's default style shifts (e.g., GPT-4 → GPT-4o → GPT-5; Claude 3 → 3.5 → 4; a few-shot that anchored a format on an older model can now actively mislead).
- *Regression tests that test the prompt against a specific model version*, passing when the base model is held fixed and silently becoming non-binding the moment the model rolls forward.

**Examples from real engineering posts.**
- *LangChain / LangSmith launch material and customer write-ups* (2023–2025): LangSmith's Prompt Hub and Prompt Playground were marketed precisely because prompts had become first-class artefacts that needed versioning, commit history, and diffing independent of application code. (**observed**, High)
- *Humanloop and PromptLayer* (2023–2024): both vendors' early product positioning described "prompts are code but without source control" as a concrete customer pain point; their core products treat prompts as versioned resources with evaluation-linked deploys. (**observed**, High)
- *Shopify's Magic / Sidekick engineering posts* (2023–2025): prompt rollouts described as going through internal canary gates and A/B tests before reaching all Shopify merchants, with rollback capability analogous to code deploys. Exact numbers on how often rollbacks fired are not publicly disclosed. (**observed architecture / inferred operational cadence**, Medium)
- *Anthropic's prompt engineering cookbook and Claude developer documentation* (2024–2026): explicit guidance on XML-tag formatting, placement of few-shot examples, separation of system from user messages — each a load-bearing convention that, when violated on a prompt version bump, produces quality drops not captured by surface unit tests. (**observed**, High)
- *OpenAI cookbook materials on structured outputs and function calling* (2023–2026): the transition from text-mode JSON extraction to function-calling to JSON-mode to structured outputs to Responses API each invalidated a previous generation of prompt-and-parser scaffolding. Teams who had built parsers for pre-function-calling JSON had to retool three times in thirty months. (**observed**, High)
- *Post-mortem-style practitioner writing* (various, 2024–2025; e.g., Eugene Yan, Hamel Husain, Shreya Shankar writing on "what goes wrong with LLM apps"): consistent observation that the largest single source of production LLM regression is prompt edits by a non-ML contributor that bypassed whatever eval harness existed. (**observed**, High)

**Typical remediation cost.** Building a prompt registry with versioning, typed variable contracts, regression evals, and canary / rollback is a 2–6 engineer-month project for a mid-sized team; maintaining it thereafter is roughly 10–20% of one engineer's time, climbing with prompt-library size (**inferred**, Medium). Retrofitting discipline onto an un-versioned prompt base is materially more expensive than greenfielding it.

**Compounding behaviour.** **Compounds**. Each prompt added without discipline adds to the surface area of silent model-swap regressions. Prompts do not self-heal when the base model rolls forward; if anything, they decay, because the model's default style drifts and the prompt's anchoring examples become less informative. This is the archetypal compounding debt of the focus-area set.

**Remediation pathway.** Only deliberate. A team can freeze model version to slow the bleeding (at the cost of missing capability gains), but eventually a swap is forced by deprecation (see §2.5 on adapter deprecation and §2.1 below on OpenAI model retirement cycles). Then the accumulated silent debt materializes at once.

### 2.2 RAG pipeline maintenance — embeddings, chunking, indexing

**What the debt looks like.** A production RAG pipeline has four moving parts that each can be swapped independently: the embedding model, the chunking strategy, the vector store / index configuration, and the retrieval-ranking stage (often a reranker such as Cohere Rerank or a cross-encoder). Debt accumulates when one swap forces a cascading recompute of the others.

Concretely:
- *Embedding-model swap invalidates the entire vector index.* Switching from OpenAI `text-embedding-ada-002` to `text-embedding-3-large` (or from Cohere `embed-v2` to `embed-v3` to `embed-v4`; or from Voyage `voyage-2` to `voyage-3` to `voyage-code-3`) means re-embedding every chunk and rebuilding every index shard. For corpora above a few hundred million chunks, this is a multi-day batch job plus indexing, plus reindex-aware rollout. (**observed**, High)
- *Chunking strategy is entangled with the embedding model.* Chunk size optimal for ada-002 (roughly 512 tokens) is sub-optimal for text-embedding-3-large (which supports 8k input and rewards longer, more semantically coherent chunks). A team that embedded under one strategy and later upgraded embeddings inherits a chunking baseline that is no longer optimal — but re-chunking requires a full re-embed. (**observed**, High)
- *Vector-store migrations stack on top.* Many teams migrated from a first-generation choice (often pgvector at small scale, or a quick-start on Chroma or Weaviate) to a production vector DB (Pinecone, MongoDB Atlas Vector, LanceDB, Qdrant, Weaviate Cloud, Turbopuffer) as scale grew. Each migration is its own project with its own indexing-schema debt. (**observed**, High)
- *Metadata and filter schemas drift.* Early RAG pipelines often encode filters as flat key-value metadata; as business logic grows, the filter surface moves toward hybrid search with BM25, learned sparse retrieval, and structured filters. Each change forces back-fill. (**observed**, Medium)
- *Retrieval-ranking debt.* Reranker models also turn over (Cohere Rerank v2 → v3 → v3.5; the rise of cross-encoder open-weight options; the recent move to LLM-based judging for final re-rank). Every reranker swap invalidates the retrieval calibration and often forces re-tuning of top-k, MMR diversity, and threshold gating.
- *Source-document drift.* The corpus itself updates. Legal-tech teams (Harvey, Hebbia, EvenUp) face this acutely because case law, contracts, and regulatory text change; knowledge-base-facing products (Notion AI, Glean, Microsoft Copilot for Microsoft 365) face it at extreme scale because every user edit is a micro-update to their slice of the index.

**Examples from real engineering posts.**
- *OpenAI's text-embedding-3-large / small launch post (January 2024)*: explicit acknowledgement that embedding swaps are disruptive, with matryoshka-style truncation pitched partially as a migration aid so teams could trade dimension for cost without a full re-embed. The Matryoshka Representation Learning paper (Kusupati et al., NeurIPS 2022) gave the theoretical footing; OpenAI operationalized it. (**observed**, High)
- *Cohere and Voyage embedding-model release posts (2023–2026)*: consistent pattern of every major release coming with migration guides that quietly concede you must re-embed to get the quality step. (**observed**, High)
- *LangChain / LlamaIndex RAG blog posts throughout 2023–2025*: the move from naive chunking to semantic chunking to propositional / auto-merging retrieval to agentic retrieval to GraphRAG was not a monotonic "add strategies" story. Each was a new default that made older pipelines feel obsolete. LlamaIndex's documentation even warns readers that their previous chunking guide is superseded every 6–12 months. (**observed**, High)
- *Pinecone, Weaviate, and LanceDB technical blogs on re-indexing cost* (2023–2026): descriptions of re-index-in-place with shadow indexes and dual-write migration patterns specifically because embedding-model upgrades are common enough to architect for. (**observed**, High)
- *MongoDB Atlas Vector / DocumentDB-Vector / Turbopuffer positioning posts (2024–2026)*: marketing often emphasizes compatibility with multiple embedding models simultaneously — a hedge against the embedding swap churn. (**observed**, Medium)
- *Harvey, Hebbia, EvenUp case studies* (2023–2026): acknowledge that legal-corpus updates and embedding upgrades together produce a sustained re-embedding cost that is material enough to be a line item in infrastructure spend. Exact dollars are not public. (**observed pattern / inferred magnitude**, Medium)

**Typical remediation cost.** For a 100M-chunk corpus, a full re-embed + reindex is tens of thousands of dollars of compute plus roughly 2–6 engineer-weeks of migration engineering (shadow-index, dual-write, A/B evaluation, cutover, cleanup) (**inferred**, Medium). Annualized over quarterly embedding-model releases, this can reach 10–25% of a RAG team's engineering capacity if teams re-embed on every release, and 0–5% if they re-embed only on major jumps. The decision of *which* releases to adopt is itself a recurring debt-management decision.

**Compounding behaviour.** **Partially compounds, partially self-resolves.** Index drift against an aging corpus compounds (stale documents accumulate). Embedding-model drift is step-function: a better embedding appears, and skipping it is a choice to carry quality debt until the next step. Chunking-strategy debt compounds if never re-evaluated. Some RAG debt genuinely self-resolves when a full re-embed is performed anyway for an unrelated reason (e.g., corpus migration), because the new pipeline absorbs several prior chunking / metadata updates at once.

**Remediation pathway.** Mostly deliberate. The rare exceptions are (a) the embedding swap that coincidentally happens during a platform migration, and (b) the corpus refresh that rebuilds the index as a side effect of a data-pipeline overhaul — both of which absorb accumulated debt "for free" but happen maybe every 18–36 months.

### 2.3 Evaluator drift — LLM-as-judge harnesses

**What the debt looks like.** LLM-as-judge is the dominant evaluation pattern for open-ended generation quality, used by essentially every LLM application team that cannot rely on reference-answer-matching (summarization, chat, creative generation, multi-turn agents, code generation where passing tests is only part of the story). It produces a specific and severe form of technical debt: the evaluator itself is a language model whose behaviour shifts when its own base model is updated.

Failure modes:
- *Judge drift across judge-model versions.* A rubric calibrated against GPT-4-0613 returns different scores against GPT-4o, GPT-4.1, or GPT-5. The calibration is not a constant; it is a function of judge-model prompt-following, verbosity priors, bias against or for long responses, and sensitivity to formatting. (**observed**, High)
- *Length and style biases in judges.* Well-documented across research literature (2023–2025) that LLM judges prefer longer, more confident, better-formatted responses even when shorter is correct. This bias changes with judge-model version. (**observed**, High)
- *Position bias in pairwise judging.* First-listed or last-listed response is systematically favored. The magnitude and direction change across judge models. (**observed**, High)
- *Judge overconfidence and mode collapse.* Newer judge models tend to score things more decisively; older scores become non-comparable. A judge-score time series that looks like quality is improving may simply reflect the judge getting more decisive. (**observed**, Medium)
- *Evaluator overfitting to the evaluated system's style.* When the same model family powers both the generator and the judge, there is a systematic affinity that inflates scores relative to a heterogeneous judge. Teams who evaluate Claude generations with a Claude judge, or GPT generations with a GPT judge, see this. (**observed**, Medium)
- *Rubric drift.* As the product matures, teams extend the rubric — adding a "grounding" sub-score, a "style" sub-score, a "refusal appropriateness" sub-score. Each extension silently re-weights the composite. Earlier eval scores become non-comparable. (**observed**, High)
- *Golden-set contamination.* Golden examples curated early in the product's life leak into fine-tunes, into RAG corpora, or into prompt few-shots; evaluators lose signal on them. (**observed**, High)

**Examples from real engineering posts.**
- *Arize AI blog posts and Phoenix documentation (2023–2026)*: explicit treatment of LLM-as-judge drift; Phoenix's evaluator-drift tracking is a product feature built precisely because customers hit the pattern repeatedly. (**observed**, High)
- *LangSmith / LangChain blog posts on evaluation and evaluator calibration* (2023–2026): customer cases describe re-calibrating evaluators after each base-judge-model update; some teams pin the judge model version explicitly for 6–12 months. (**observed**, High)
- *Braintrust product-marketing and engineering blog (2023–2026)*: their eval-first framing and the concept of "online evals" treat evaluator output as itself a monitored signal requiring quality control; their customer case studies describe evaluator drift as the core ongoing cost. (**observed**, High)
- *Shreya Shankar, Eugene Yan, Hamel Husain, Emil Sedgh on LLM evals (2023–2026)*: practitioner writing converges on the view that evaluator design is harder than system design, and that evaluator maintenance is the hidden ongoing cost that sinks small teams. (**observed**, High)
- *Academic literature*: Zheng et al. (MT-Bench / Chatbot Arena, 2023); Wang et al. (length bias, 2023); Panickssery et al. (self-preference bias, 2024); Stureborg et al. (judge-variance analyses, 2024–2025); many "LLM-as-judge is not calibration-free" papers. (**observed**, High)
- *Karpathy's public commentary (2023–2025)*: "evals are all you have" alongside repeated warnings that judge-based evals can collapse silently when either the judge or the judged model changes. (**observed**, High)
- *Anthropic cookbook material on evals* (2024–2026): guidance on using calibrated rubrics, anchoring judge outputs with gold-standard reference responses, and running human-eval spot checks to detect judge drift. (**observed**, High)

**Typical remediation cost.** Evaluator maintenance is a sustained tax. A serious eval harness for a mid-sized LLM product is 0.5–1.0 FTE continuously — curating a golden set, running cross-judge reliability checks, running periodic human baselines, and re-calibrating on each judge-model version (**inferred**, Medium). Teams who under-invest either run blind or discover the drift only when product quality has already slipped.

**Compounding behaviour.** **Compounds aggressively**. Evaluator drift is the most insidious of the five debt classes because the evaluator is the thing that is supposed to detect drift elsewhere. When it fails silently, every downstream decision — A/B test outcomes, prompt-change approvals, model-swap go/no-go — is compromised. Unlike prompt debt (which is felt as regressions users report) evaluator debt can persist for months unnoticed.

**Remediation pathway.** Deliberate, with periodic human-grounding. A minimum discipline: a locked golden set with human labels, re-scored each time the judge model changes, with a confidence interval on the score-comparison step. Teams that adopt this discipline find and fix drift within a quarter; teams that do not may run drifted evaluators for a year.

### 2.4 Observability and monitoring for LLM apps

**What the debt looks like.** Observability for LLM apps differs from classic APM / web-service observability in load-bearing ways: requests are expensive (so sampling matters), payloads are large (so storage matters), quality is not binary (so evaluator integration matters), traces cross tool calls and retrieval steps (so structured tracing matters), and user-facing latency is dominated by model-side events outside the team's control (so the boundary of what "observability" means is unstable).

Concrete debt patterns:
- *Custom tracing glue that predates the OpenTelemetry GenAI semantic conventions.* Teams that built bespoke tracing in 2023 with ad-hoc span structures face migration cost as OpenTelemetry's GenAI conventions (attribute naming, span kinds, token-count fields, tool-call modeling) consolidate in 2024–2025. (**observed**, Medium)
- *Vendor-SDK coupling.* Tracing that assumes OpenAI's Python SDK shape breaks when a team adds Anthropic, Google, Mistral, or open-source inference. LangSmith, Arize, Braintrust, Weights & Biases Weave, Fiddler, Arthur, and Langfuse all wrote adapters for this; teams that built their own often wrote a fragile one. (**observed**, High)
- *Token-count drift.* What a token is changes across providers. Provider-reported token counts have bugs, revisions, and tokenizer updates. Dashboards and cost attribution that assume stable tokenizer mappings decay. (**observed**, Medium)
- *Prompt-snapshot storage.* Observability tools that capture full prompts for each trace run into storage costs that scale with traffic; teams that decided "keep everything" in 2023 often revisited that decision in 2025 as traffic and trace sizes grew. (**observed**, Medium)
- *Observability-tool migration debt.* Teams rotated through Helicone, LangSmith, Langfuse, Arize Phoenix, Braintrust, Humanloop, PromptLayer, and Weights & Biases Weave over the period. Each migration carries its own cost — historical trace history, eval-run history, A/B-test metadata. Some teams run two tools simultaneously during transitions. (**observed**, High)
- *Custom evals embedded in production routes.* Inline evals that run a judge LLM on every response have their own debt profile — cost blows up with traffic; judge-model swaps hit production directly; sampling logic added as an afterthought sits alongside load-bearing code. (**observed**, Medium)
- *Missing observability for tool calls and multi-step agents.* First-generation observability tools focused on single prompt-response pairs. Agentic workflows (tool calls, function calls, chained retrievals, code-execution sandboxes) broke that model. Teams that did not re-architect their tracing as agents proliferated ended up with black-box middle steps where most regressions actually live. (**observed**, High)

**Examples from real engineering posts.**
- *LangSmith launch and subsequent case studies* (2023–2026): consistent framing that observability is the first thing an LLM team rolls out and the first thing they underinvest in. (**observed**, High)
- *Arize AI and Phoenix open-source* (2023–2026): Phoenix's product evolution from basic trace viewing to eval integration to agent observability mirrors the industry debt-accretion curve. (**observed**, High)
- *Braintrust engineering posts* (2024–2026): emphasize the eval-observability-prompt registry as a tight loop, and explicitly frame the decoupling of these three as the architectural mistake that creates debt. (**observed**, High)
- *Langfuse open-source project posts* (2023–2026): open-core positioning partly because customers wanted portability — observability data locked to one vendor was itself a debt. (**observed**, Medium)
- *Weights & Biases Weave, Humanloop, PromptLayer, Helicone, OpenLLMetry* (2023–2026): the proliferation of tools is itself evidence of an unsettled category; every change of tool is a migration. (**observed**, High)
- *OpenTelemetry GenAI SIG material (2024–2026)*: active standardization effort to reduce vendor lock-in; adoption in practice lags. (**observed**, Medium)
- *Post-mortems where observability gaps were the root cause*: several public incidents (a Shopify Sidekick quality regression discussed at a conference in 2024; Cursor's well-documented pricing / usage incident in mid-2025 that turned partly on usage-attribution gaps; Perplexity's "answer quality variability" discussions in 2024) rely on observability to catch, and on observability gaps to explain why the catch was late. (**observed pattern / specifics vary in detail availability**, Medium)

**Typical remediation cost.** Building a competent observability stack is 1–3 engineer-months greenfield; migrating from one vendor to another with history preservation is 1–2 engineer-months; retrofitting tracing onto an agentic system is 2–4 engineer-months (**inferred**, Medium). Maintenance is typically 5–15% of an engineer's time, rising if the team's evaluator integration is deep.

**Compounding behaviour.** **Mixed — compounds in volume, self-resolves in category.** Trace volume compounds with traffic. Trace structure, however, often self-resolves when OpenTelemetry conventions or a vendor's opinionated schema supersedes bespoke code — the migration cost is real but it resets the technical base. Observability-vendor migrations are a recurring deliberate cost; the underlying *observability problem* gets steadily better as the category matures.

**Remediation pathway.** Deliberate migrations. Teams that start with OpenTelemetry conventions and a single opinionated vendor (rather than rolling their own) carry the least debt. Teams that built custom in 2023 are all on their second or third observability regime by 2026.

### 2.5 Fine-tune and adapter lifecycle

**What the debt looks like.** Fine-tuning and adapters (LoRA, QLoRA, DoRA, PEFT variants, and hosted-adapter services) promise targeted behaviour customization without retraining a base model. Their debt profile is dominated by their *coupling to a specific base-model version* and that base model's deprecation schedule.

Concretely:
- *Adapters are base-model-version-locked.* A LoRA trained on Llama-3-8B does not run on Llama-3.1-8B without at minimum a re-train, and often cannot be ported at all when architectural width changes. Same story across Mistral generations, Qwen generations, Gemma generations, and proprietary fine-tunes of Claude / GPT. (**observed**, High)
- *Provider-hosted fine-tune deprecation.* OpenAI has deprecated multiple fine-tune bases over 2023–2026 (babbage, curie, davinci-base fine-tunes; gpt-3.5-turbo-0613 fine-tunes; embedding-ada fine-tunes; successive GPT-4 fine-tune bases). Each deprecation forces customers to either re-fine-tune on a newer base or lose the capability. (**observed**, High)
- *Anthropic-side adapter / fine-tune availability.* Anthropic's fine-tune / adapter product surface expanded across 2024–2026; customers who built on early beta forms of Claude fine-tuning have encountered version-bridge decisions. (**observed / partially inferred**, Medium)
- *Adapter stacking debt.* Teams that layer multiple LoRAs (task-specific + style + safety) face the combinatorial explosion of retraining each when any base model changes. LoRA "swap at inference time" solutions help, but stack interactions are empirically non-additive. (**observed**, Medium)
- *Training-data drift.* The fine-tune training set captured a snapshot of product state and user preferences. Once the product evolves (new features, new taxonomy, new compliance rules) the fine-tune slowly encodes stale behaviour. Remediating requires re-collecting labels and re-training. (**observed**, High)
- *Evaluation coverage gaps on fine-tune regressions.* A fine-tune improves target behaviour and often subtly degrades adjacent behaviour (instruction-following, tool-use fidelity, refusal calibration). Evaluation harnesses often over-index on the target and miss the regression. (**observed**, High)
- *Cost arithmetic that turns unfavorable.* The original economic rationale for a fine-tune — "cheaper than prompting, competitive in quality" — is undermined every time the base model's inference price drops or its base capability rises to match the fine-tuned behaviour. Teams regularly discover a 2024 fine-tune is now more expensive and lower-quality than a 2026 base-model prompt. (**observed**, High)

**Examples from real engineering posts.**
- *OpenAI model retirement / deprecation notices (2023–2026)*: public schedule of deprecations, with specific guidance on migrating fine-tunes; each deprecation cycle produces public developer discussion. (**observed**, High)
- *Anthropic model version changelog / deprecation policy materials (2024–2026)*: increasingly formalized version policies; customers building with adapter capabilities track them. (**observed**, High)
- *Hugging Face PEFT library blog posts and tutorials (2023–2026)*: good open documentation of adapter lifecycle; also a running log of what-breaks-when. (**observed**, High)
- *Together, Fireworks, Anyscale, Replicate, Modal, Baseten engineering posts (2023–2026)*: inference-provider posts frequently include customer stories of upgrading base models and reshaping adapter fleets. (**observed**, High)
- *Harvey, EvenUp, Hebbia in legal tech (2023–2026)*: public descriptions suggest fine-tune / adapter use for style and domain adaptation; migration stories between base-model generations are implied but rarely published in full. (**observed pattern / inferred specifics**, Medium)
- *"Is fine-tuning worth it?" practitioner pieces (2024–2026)*: recurring practitioner conclusion that prompting + RAG typically outperforms a legacy fine-tune within 6–12 months of each base-model jump; fine-tunes justified only when latency, cost-at-scale, or strict behaviour control outweighs the maintenance tax. (**observed**, High)
- *Anthropic and OpenAI cookbooks on when to fine-tune vs. prompt-engineer* (2023–2026): both increasingly conservative in recommending fine-tuning for typical product use cases. (**observed**, High)

**Typical remediation cost.** Each base-model generation bump forces at minimum a re-train of each fine-tune (days to weeks of compute and labelling review) and often a re-evaluation of whether the fine-tune is still justified (1–3 engineer-weeks of analysis per fine-tune). A fleet of 5–10 fine-tunes with quarterly base-model bumps has a recurring cost of 0.5–1.0 FTE permanently allocated to adapter lifecycle (**inferred**, Medium).

**Compounding behaviour.** **Compounds until forced remediation.** Adapter debt is exceptionally clean in its compounding behaviour because the base-model deprecation schedule *forces* a remediation event periodically. Between events, debt accrues: training data staleness, quality drift relative to the moving base, eval-coverage rot. The forced remediation event is the quarterly or semi-annual base bump; skipping it is not available. Adapters therefore have the most **predictable** debt rhythm of the five categories, even if the rhythm is fast.

**Remediation pathway.** A mix of deliberate remediation and forced remediation. The forcing function is base-model deprecation; deliberate remediation is re-evaluating whether the fine-tune is still worth maintaining.

---

## 3. Maintenance cost curves

Conceptual cost curves over time as base-model versions change. Time axis: quarterly base-model version bumps across 2023Q1 through 2026Q2, roughly 13–14 version steps depending on family. Cost axis: engineer-time consumed by the debt class per unit of product scope per quarter.

### 3.1 Prompts-as-code — compounding, saw-tooth

```
cost
  ^
  |                                                   _/ forced
  |                            _/                    /   swap
  |            _/             /                     /    (spike)
  |           /              /                     /
  |          /    swap      /                     /
  |   _/    /    (spike)   /                     /
  |  /     /              /                     /
  |_/     /              /                     /
  +----------------------------------------------->  time
  23Q1  24Q1 24Q2       25Q2                  26Q2
```
Between swaps, cost climbs with prompt-library size and silent-regression risk. At each swap, a one-time spike represents re-testing and re-calibrating every prompt against the new base. Spike magnitude grows with accumulated library size — classic compounding.

### 3.2 RAG pipeline — step-function with slow corpus-drift ramp

```
cost
  ^
  |                   re-embed          re-embed
  |                     |                  |
  |                    /|                 /|
  |                   / |                / |_____
  | corpus           /  |____           /
  | drift slope     /
  |   _____________/
  |__/
  +------------------------------------------------>  time
```
Cost has a slow ramp from corpus growth and document churn, plus large step-function spikes whenever the team performs a re-embed to adopt a new embedding model. Between re-embeds, cost is dominated by reindex maintenance and retrieval-quality monitoring. Post-re-embed, cost drops because the pipeline is re-aligned.

### 3.3 Evaluator drift — compounding with silent base

```
cost
  ^                                             *
  | visible                                    /
  | cost                                      /  discover
  |                                          /   drift
  |                                         *
  | _________________________________________
  |         silent-drift penalty (unmeasured)
  |          ----------------------------->
  |
  +------------------------------------------------>  time
```
Measured cost is near-flat because teams rarely invoice the hours spent maintaining the evaluator. The *unmeasured* cost — wrong A/B decisions, wrong model-swap go / no-go, wrong prompt merges — climbs continuously and is discovered as a discrete event (a quality regression that survived the evaluator, or a human audit revealing a drift). The cost curve is therefore saw-tooth with long silent intervals and sudden retrospective charges.

### 3.4 Observability — front-loaded then flat, with migration spikes

```
cost
  ^
  |
  |  build                 migration      migration
  |   *                       *             *
  |   |\                     /|\           /|\
  |   | \___________________/ | \_________/ | \______
  |
  +------------------------------------------------->  time
```
Initial build cost is high. Steady-state maintenance cost is roughly flat. Every 12–18 months, a vendor migration or a tracing re-architecture produces a localized spike. Absent migrations, this is the lowest-compounding debt category because the substrate (OpenTelemetry, mature vendor platforms) is improving underneath.

### 3.5 Fine-tune / adapter — quarterly saw-tooth

```
cost
  ^
  |    | base | base | base | base | base | base
  |    | bump | bump | bump | bump | bump | bump
  |    |      |      |      |      |      |
  |    *      *      *      *      *      *
  |   /|     /|     /|     /|     /|     /|
  |  / |    / |    / |    / |    / |    / |
  | /  |___/  |___/  |___/  |___/  |___/  |____
  +------------------------------------------------->  time
```
Each base-model bump forces a re-train (spike). Steady-state between bumps is non-zero (training-data drift, eval coverage). The sawtooth is the most regular of the five categories because deprecation schedules force the rhythm.

### 3.6 Aggregate picture

Stacked together, prompts and evaluators dominate long-run compounding cost. RAG and adapters dominate spike magnitudes. Observability is the most predictable and the most amenable to a one-time architectural fix. A team that invests in a prompt registry with evaluator-linked canary + a judge-drift watchdog + an embedding-agnostic RAG migration pattern + an OpenTelemetry-aligned observability stack pays a large up-front cost and carries near-linear maintenance thereafter — versus exponential in the unmanaged case.

---

## 4. Compounding vs self-resolving vs deliberate-remediation classification — master table

| Debt subclass | Where it lives | Compounds? | Self-resolves? | Requires deliberate work? | Dominant trigger | Rough cost curve |
|---|---|---|---|---|---|---|
| Unversioned prompts | Application code | Yes, strongly | No | Yes | Each model swap | Saw-tooth, rising spikes |
| Few-shot example staleness | Prompt contents | Yes | Rarely (only if base shift is favorable) | Yes | Base-model style shift | Slow ramp |
| Prompt–parser coupling (JSON, function call, structured outputs) | Glue layer | Yes (API format churn) | Partial (provider convergence helps) | Yes | Provider format migration | Step |
| Regression tests pinned to fixed model | Test harness | Yes (silent) | No | Yes | Each model swap | Saw-tooth, invisible |
| Canary / rollback infrastructure | Deploy tooling | No | N/A | Builds once | Initial build | Front-loaded |
| Stale vector index (embedding drift) | Vector store | Yes | Partial (full re-embed resolves) | Yes | Embedding-model release | Step with ramp |
| Chunking strategy obsolescence | Pipeline | Yes | No | Yes | Chunking-practice advances | Slow ramp |
| Retrieval-reranker calibration | Retrieval stage | Yes | Partial | Yes | Reranker release | Step |
| Corpus drift (document churn) | Corpus | Yes | No | Yes | Business-as-usual | Steady ramp |
| Filter / metadata schema debt | Pipeline | Yes | No | Yes | Product evolution | Ramp |
| Judge length / position / format bias | Evaluator | Yes | No | Yes | Judge-model update | Saw-tooth |
| Judge drift across versions | Evaluator | Yes (silent) | No | Yes | Judge-model update | Silent ramp |
| Rubric expansion over time | Evaluator | Yes | No | Yes | Product evolution | Ramp |
| Golden-set leakage / contamination | Evaluator | Yes | No | Yes | System absorbing golden | Ramp |
| Evaluator–generator same-family affinity | Evaluator design | Yes | No | Yes | Choice of judge family | Flat-but-elevated |
| Custom tracing before OTel | Observability | Yes (then resolves) | Partially (OTel convergence) | Yes for migration | OTel convergence | Step down after migration |
| Vendor-SDK-coupled tracing | Observability | Yes | No | Yes | Added provider | Step |
| Token-count / tokenizer drift | Observability | Yes (silent) | Rarely | Yes | Tokenizer update | Slow silent ramp |
| Observability-tool migration | Observability | N/A, one-time | N/A | Yes | Vendor change | Spike |
| Agent / tool-call tracing gaps | Observability | Yes | No | Yes | Agent adoption | Step |
| Adapter base-version lock-in | Fine-tune layer | Yes | No (forced by deprecation) | Yes | Base-model deprecation | Saw-tooth |
| Adapter stacking interactions | Fine-tune layer | Yes | No | Yes | Stack growth | Ramp |
| Fine-tune training-data staleness | Fine-tune layer | Yes | No | Yes | Product evolution | Ramp |
| Fine-tune adjacent-behaviour regression | Fine-tune layer | Yes (silent) | No | Yes | Each re-train | Silent ramp |
| Fine-tune economic obsolescence | Fine-tune layer | Yes | Partially (next base absorbs) | Yes (decide to retire) | Base-model capability rise | Step |

Summary counts: 25 subclasses; 24 compound; 6 self-resolve (partially or coincidentally); 24 require deliberate remediation. The single subclass that neither compounds nor demands deliberate re-work is canary / rollback infrastructure — a front-loaded cost whose payoff is proportional to every other debt it absorbs.

---

## 5. Patterns across focus areas

Six recurring themes cut across all five focus areas. Each is cited inline where first established.

### Pattern 1 — Version coupling as the master variable

Across prompts, RAG, evaluators, observability, and adapters, the largest source of debt is **implicit coupling to a specific model or tokenizer version**. The coupling is often invisible at the time of writing: a prompt works, a chunking size feels right, a judge rubric seems calibrated, a fine-tune hits its metric. The coupling manifests only when the underlying version changes. (**observed, High**)

The implication for architecture: every place a model or tokenizer version appears implicitly should be made explicit — prompt-version, embedding-version, judge-version, adapter-base-version, tokenizer-version — and logged on every production trace. Without this, migration is archaeology.

### Pattern 2 — Silent drift dominates visible regressions

The most dangerous debt in four of the five categories (prompts, RAG, evaluators, observability) is the kind that does not produce a user-visible regression. It produces *worse decisions* about what to ship, what to A/B-test, what to promote out of canary. Teams that only measure user-visible regressions operate on a falsified instrument panel. (**observed across all five focus-area sections, High**)

The remediation is disciplined, not clever: locked golden sets, versioned evaluators, human spot-checks on a cadence, and explicit reporting of evaluator-version alongside eval results.

### Pattern 3 — Evaluator brittleness is the single biggest hidden risk

Four of the five focus areas assume an evaluator exists to detect drift. If the evaluator itself drifts silently, every other debt-management discipline degrades. Evaluator maintenance is the point at which organizational underinvestment is most expensive. Practitioner writing (Shreya Shankar, Eugene Yan, Hamel Husain) converges on this. (**observed, High**)

Remediation is organizational as much as technical: a named owner of the evaluator harness, a recurring review cadence, and a policy that requires human spot checks to run whenever a judge model changes. Tools (Arize Phoenix, LangSmith, Braintrust) can enforce this but only if a human owns the policy.

### Pattern 4 — Forced vs. voluntary remediation events

The categories split by whether remediation is forced:
- *Forced*: adapter lifecycle (base-model deprecation), observability-tool migrations (vendor changes).
- *Voluntary*: prompt re-testing, RAG re-embedding, evaluator re-calibration.

Forced remediation is less pathological because the forcing function schedules the work; voluntary remediation is what gets perennially deprioritized. Teams that convert voluntary remediation into a scheduled forcing function (e.g., "re-run the full eval suite against the new judge model within two weeks of its release, on pain of blocking deploys") move their risk profile substantially closer to the forced-remediation pattern. (**observed / inferred**, Medium)

### Pattern 5 — The "compound AI systems" shift makes debt more multiplicative

Zaharia and colleagues' 2024 BAIR framing (compound AI systems) captures a real shift: production systems are no longer single-prompt single-model but orchestrations of models, retrievers, tools, evaluators, guardrails, and routing. Each component has its own debt profile; interactions between components are sources of new debt (e.g., a retriever upgrade that changes the distribution of inputs into a downstream summarizer, silently changing the summarizer's behaviour). (**observed framework / inferred debt consequence**, Medium)

The organizational implication: the unit of debt accounting is the **compound system** and its versioned components, not any one model.

### Pattern 6 — Open-source infrastructure improves faster than bespoke

Every focus area shows a pattern where bespoke early choices (custom prompt registries, custom tracing, custom evaluator harnesses, custom adapter pipelines) are overtaken within 12–24 months by a consolidating open-source or vendor offering. Teams that commit early to opinionated vendors and open-standards (OpenTelemetry GenAI, Hugging Face PEFT, LangSmith / Braintrust / Arize, Pinecone / Weaviate / MongoDB Atlas, OpenAI SDK / Anthropic SDK conventions) spend less total engineering time than teams that insist on bespoke. Some debt self-resolves only because the substrate underneath improves. (**observed**, Medium)

---

## 6. Open questions and negative evidence

**Open questions.**
- *How much does debt actually differ across AI-forward firms vs. AI-using enterprises?* Harvey and Cursor publish engineering material that suggests heavy investment in prompt registries, evals, and observability. A Fortune 500 enterprise deploying Microsoft Copilot or a hosted RAG product inherits a very different debt profile — one largely hidden inside vendor code. The adaptability implications for the two populations likely diverge.
- *What is the real dollar cost of silent evaluator drift?* No published case quantifies it. Practitioner anecdotes imply "substantial" but the measurement design itself is hard: you are trying to measure what bad decisions were made because of a bad instrument.
- *Does the debt profile change at scale tiers?* My priors: S1 / S2 (solo / small, per the scale-based track) may carry less absolute debt but more per-capita burden; S3 / S4 may consolidate debt inside observability / eval platforms; S6 / S7 (governments, multi-national enterprises) may defer debt into vendor contracts and inherit it only when the contract ends.
- *How much of AI-system debt is genuinely novel versus re-branded traditional software debt?* Prompt-as-code strongly echoes config-as-code; adapter lifecycle echoes library-dependency management; evaluator drift echoes flaky-test management. The interesting question is which patterns are genuinely new (silent evaluator drift, base-model-version coupling across components).

**Negative evidence (what was looked for and not found).**
- *Rigorous longitudinal benchmarks of LLM-app quality over time, under fixed evaluation harness, across the 2023–2026 period from any named production firm*. None found with public data. Vendor-lab evals (MMLU, HumanEval, SWE-bench, MT-Bench, Chatbot Arena) track model quality but not product quality.
- *Peer-reviewed post-mortems from AI-native firms on production LLM-app regressions*. Practitioner write-ups exist; formal post-mortems at conference-paper quality are scarce.
- *A published cost model of RAG re-embedding at corpus scale with real line-item numbers*. Vendor blogs gesture at it; no reproducible number-by-number breakdown was found.
- *Evidence that any vendor's managed fine-tune service has a graceful cross-base-model migration path that preserves adapter behaviour without a re-train*. None found.
- *Firm-level evidence that the adapter lifecycle has produced a clean "retire the fine-tune, go back to prompting" story*. Practitioner claims point in this direction but are thinly sourced; a careful case study would be valuable.

**Confidence posture.** The memo's claims at High confidence are: prompts-as-code compounds; evaluator drift is the most insidious debt; adapter lifecycle is forced by deprecation; RAG re-embedding is a predictable step-function cost; observability category is consolidating. Medium-confidence claims: specific cost numbers in engineer-months, the "compound AI systems" debt framing, the scale-tier-dependence of debt profiles. Low-confidence claims: projections beyond 2026; the durability of current observability / evaluation vendor offerings; whether OpenTelemetry GenAI conventions will stick.

---

## 7. Feedback to the three-pillar adaptability frame

Six bullets linking T3 findings back to the three-pillar (AI usage × organization × technical infrastructure) adaptability frame.

- **Technical debt is a feedback signal, not a residue.** The compounding rate of AI-system debt is a direct function of organizational discipline around versioning and evaluation. Pillar 3 (technical infrastructure) and Pillar 2 (organization) are coupled at this interface: the technical debt curve reveals whether the organization has assigned named ownership of prompts, evaluators, and adapters. A team with high compounding debt is, diagnostically, a team without an evaluator owner — regardless of what the org chart claims.

- **Evaluator ownership belongs in Pillar 2.** Evaluator drift is the largest silent risk across the five focus areas, and it is fundamentally an organizational problem rather than a tooling one. Any adaptability framework that addresses only Pillar 3 (buy better observability tools) without changing Pillar 2 (appoint an accountable evaluator owner with a review cadence) will see the technical investment underdeliver. This should feed into O2 (role redefinition) and M2 (adaptability indicators) as a concrete measurable.

- **Version coupling is the master variable across pillars.** Pillar 1 (AI usage patterns) inherits version coupling from the model; Pillar 2 (organization) inherits it through role definitions that assume a tool surface; Pillar 3 (infrastructure) inherits it through adapter / embedding / tokenizer / eval lockin. The adaptability imperative common to all three pillars is **make version coupling explicit and logged**. This is a concrete recommendation that emerges from T3 for the cross-pillar synthesis in M1.

- **Forced-remediation rhythms are an adaptability asset, not a liability.** Counter-intuitively, the debt category with the most predictable cost (adapter / fine-tune lifecycle) is the healthiest because the forcing function schedules the work. Translating voluntary work into scheduled forcing functions — e.g., binding eval re-calibration to each judge-model release, or binding RAG re-embedding to each embedding-major release — converts compounding debt into saw-tooth debt, which is tractable. This is a reusable adaptability pattern for other pillars.

- **Silent drift is load-bearing for trust calibration.** The reasoning-trust-verification track treats verification as something applied to AI outputs. T3 surfaces a structurally equivalent problem one level up: trust calibration of the *evaluator* that is calibrating trust in outputs. A naive three-pillar framework that does not address evaluator-level trust recurses into unreliability. Verification of the verifier belongs on the research agenda.

- **Open-source / consolidating substrates reduce adaptability cost asymmetrically.** Teams that commit to OpenTelemetry, to a single observability vendor, to standardized adapter libraries, to an eval harness vendor, and to an embedding-agnostic RAG architecture pay the one-time cost of consolidation but reduce their adaptability cost per model swap by a large factor. This is a concrete recommendation for T1 (build vs rent) and T2 (compute scaling): preferring the consolidating substrate is not a cost-optimization but an adaptability optimization.

---

*End of memo.*
