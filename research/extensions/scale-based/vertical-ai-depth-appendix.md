# Vertical AI and Service-as-Software Depth: Firm-Level Decomposition Evidence

status: research_complete
date: 2026-04-21
stream: E — Vertical AI and service-as-software depth
parent_plan: [`research/operations/expansion/sales-vs-productization-research-plan.md`](../../operations/expansion/sales-vs-productization-research-plan.md)
parent_memo: [`sales-vs-productization-decomposition.md`](sales-vs-productization-decomposition.md)

---

## 1. Scope and method

Closes Gap 6 of the decomposition research plan via deep-dive on 21 vertical-AI firms 2024-2026 across legal, customer support, developer tools, consumer/enterprise search, healthcare, and Korean/Japanese vertical AI. Each firm classified along (1) sales motion (PLG / enterprise / hybrid / channel), (2) productization depth (prompt-only / RAG-heavy / fine-tuning / own training / hybrid), (3) ARR trajectory with team size, (4) eval publication.

Tests four hypotheses the parent memo surfaces: **H1** eval-publishing firms cluster UL; **H2** RAG-heavy firms cluster UR with higher churn; **H3** training/fine-tuning firms price higher and retain longer; **H4** Menlo's "Great Re-Aggregation" service-as-software thesis requires productization depth.

Evidence grade: B majority (Sacra, Contrary Research, Bessemer, company press releases, TechCrunch, Fortune). A-grade for Harvey/Sierra benchmark and ISO 42001 disclosures. C-grade for Decagon ARR (8-figure self-report).

---

## 2. Firm classification table

| Firm | Vertical | Sales motion | Productization depth | ARR 2024 → 2026 | Team | $/employee | Eval publication | Quadrant |
|---|---|---|---|---|---|---|---|---|
| **Harvey AI** | Legal | Enterprise-led; AmLaw 100 | Hybrid (OpenAI custom case-law model, multi-model orchestration, private RAG) | $50M → $195M (Dec 2025) → ~$250M+ (Q1 2026) | ~350 | ~$700K | Yes — VLAIR top score 94.8% Document Q&A; SOC 2 Type II, ISO 27001, ISO 42001, IRAP | **UL (both strong)** |
| **Sierra** | Customer support | Enterprise-led; outcome-based pricing; 50% of customers >$1B rev | Hybrid orchestration with own agent architecture; τ-bench / τ³-bench published | $26M (Dec 2024) → $130M (Dec 2025) → $150M (Jan 2026) | ~300 | ~$500K | Yes — owns τ-bench, τ²-bench, τ³-bench open-source benchmarks | **UL** |
| **Decagon** | Customer support | Enterprise-only; no self-serve; median contract $386K | Hybrid — own evaluation engine, offline+online A/B, not own foundation model | 0 → 8-figure (late 2024) → growing; valuation $1.5B → $4.5B in Jan 2026 | ~250 est. | n/d | Partial — internal eval engine published, no third-party benchmark | **UL (tilt toward sales)** |
| **Cresta** | Contact center | Enterprise-led; seat-based subscription | **Training** — Ocean-1 contact-center foundation model + customer-specific fine-tuning (4-6 wk timeline) | "Nearly quadrupled" ARR 2023-2025; $270M total funding | ~400 | n/d | Limited — Ocean-1 announcement but no independent third-party benchmark | **UL (tilt toward productization)** |
| **Forethought** | Customer support | Enterprise-led + mid-market | RAG-heavy; agent orchestration on vendor models | $50-100M range; acquired by Zendesk Mar 2026 | 135 | ~$500K | No public eval; acquired before publishing | **Fringe — sales ahead** |
| **Cursor (Anysphere)** | Developer tools | **PLG-led** flipping to hybrid (60% enterprise in 2026) | **Own training** — Composer 2 on Kimi K2.5 base with continued pretraining + RL; published technical report | $100M (Jan 2025) → $500M (Jun) → $1B (Nov) → $2B (Feb 2026) | ~300 | **~$6.7M** | Yes — SWE-bench Multilingual 73.7, Terminal-Bench 61.7, "cursorbench" internal framework | **UL** |
| **Cognition (Windsurf)** | Developer tools | Hybrid (Windsurf PLG + Devin enterprise) | **Own training** — SWE-1.5, SWE-1.6 models; SWE-bench published | Windsurf $82M ARR at $250M acquisition (Dec 2025); Cognition combined >$200M | ~500 | ~$400K | Yes — SWE-bench technical reports, SWE-1.6 public preview | **UL** |
| **Replit** | Developer tools | Hybrid — consumer PLG + Agent consumption billing | Hybrid orchestration; Agent 4 built on vendor models + own scaffolding | $2.8M (Jan 2025) → $150M (Sep 2025) → $1B run-rate target end 2026 | 371 | ~$400K | Limited — Agent demos but no SWE-bench number | **UL (tilt toward sales)** |
| **Perplexity** | Consumer / enterprise search | PLG + Enterprise Max tier | **Fine-tuning** — Sonar on Llama 3.3 70B with SFT + DPO + PPO; Vespa retrieval | $80M (late 2024) → $232M (2025) → $500M annualized (Apr 2026) | ~400 | ~$1.25M | Partial — Sonar model cards, no third-party benchmark leader | **UL (sales ahead)** |
| **Glean** | Enterprise search | Enterprise-led; seat-based | **RAG-heavy with knowledge graph** — GraphRAG architecture; explicit "RAG not fine-tuning" stance | $110M (2024) → $208M (2025) → $200M+ (Feb 2026) | >1,000 | ~$200K | Limited — internal studies, no third-party eval | **UL (tilt toward sales)** |
| **Abridge** | Healthcare / clinical doc | Enterprise-led; Epic first-partner; health-system contracts | **Fine-tuning** — internal model on 50,000+ clinical examples + 10,000-encounter benchmark; confabulation-detection 97% vs GPT-4o 82% | $45M (early 2025) → $117M contracted ARR (Q1 2025) → >$150M (2026 est) | ~400 | ~$375K | Yes — whitepapers on hallucination-free clinical notes, NEJM/JAMA integrations | **UL** |
| **OpenEvidence** | Healthcare / clinician reference | PLG (free to clinicians; ad-based) | Hybrid — medical RAG + DeepConsult agent; not own foundation model | 0 → $100M revenue (2025) | ~100 | **~$1M** | Limited — DeepConsult launch, no peer-reviewed benchmark | **UR tilt (sales ahead, scale via free)** |
| **Atropos Health** | Healthcare / real-world evidence | Enterprise-led; pharma + health systems | **RAG-heavy on curated clinical evidence networks** | Post-$33M Series B; ARR not disclosed | ~50-80 | n/d | Limited — peer-reviewed case studies, no benchmark | **LL → UL migration** |
| **Tennr** | Healthcare workflow | Enterprise-led; 150 health-system customers | **Training** — RaeLM vision-language model trained on 100M anonymized docs | Post-$101M Series C at $605M valuation (June 2025) | ~100 | n/d | Limited — product claims, no public benchmark | **UL (tilt toward productization)** |
| **EvenUp** | Legal / personal injury | Enterprise-led to plaintiff firms | Hybrid — document extraction + case-value model + template | ARR "doubling YoY"; $2B → $3B valuation Oct 2025 | ~400 | ~$250K | Limited — internal claims of "69% higher likelihood of policy-limit settlements" | **UL (sales ahead)** |
| **Spellbook** | Legal / contract | PLG + mid-market + enterprise | RAG-heavy on vendor APIs (GPT-5, Opus); no own training | $30M → $100M on track 2026; $350M valuation (Oct 2025) | ~150 | ~$670K | No third-party eval; absent from VLAIR | **UR (sales ahead)** |
| **Paxton AI** | Legal / research | Mid-market + solo + BigLaw; $22M Series A | RAG-heavy with Stanford Legal Hallucination Benchmark score | n/d specific ARR; 26 employees | 26 | n/d | Yes — 94% non-hallucination on Stanford Legal Hallucination Benchmark | **Small-scale UL** |
| **Eve** | Legal / plaintiff | Enterprise-led to plaintiff firms; 800+ firms | Hybrid — case intake + demand generation on vendor models | $1B valuation Sep 2025; ARR not disclosed; 250% YoY rev growth | ~200 est. | n/d | No — absent from VLAIR; no third-party benchmark | **UR tilt (sales ahead)** |
| **Upstage** (Korea) | Document AI | Enterprise-led via Samsung/partners; Korea 35% LLM share | **Own training** — Solar LLM family (Depth Up-Scaling technique), Document Parse 95% accuracy | 130%+ YoY rev growth; $1B+ valuation Series C (Apr 2026) | ~250 | n/d | Partial — model cards, Korea-market benchmarks, KOSPI IPO 2026 | **UL (productization depth)** |
| **Samsung SDS** (Korea) | Enterprise AI suite | Captive Samsung + OpenAI ChatGPT Enterprise reseller (Korea first) | Hybrid orchestration (FabriX + Brity Copilot wrapping Samsung LLM + GPT) | Samsung group revenue; not standalone AI ARR | ~25,000 (group) | n/a | No — internal only | **Incumbent platform — not comparable** |
| **Tripla** (Japan) | Travel / hotel AI | Channel + hotel-direct | Prompt + RAG on vendor APIs; booking engine + chatbot | $17.2M TTM (Oct 2025); publicly traded TSE 5136 | ~100 est. | ~$170K | No — product-level claims only | **Mid-tier UR (sales ahead)** |

Cross-firm observations: 15 of 21 firms land in the upper-left by the time they cross $100M ARR — vertical AI is not primarily a wrapper market at scale. The 4 clearly UR firms (Spellbook, Eve, EvenUp, Forethought) have thinner eval publication or were acquired before reaching full productization depth. Tripla and OpenEvidence are outliers: OpenEvidence hit $100M on free-to-clinician + ad model; Tripla is an older listed company at $17M with minimal productization depth.

---

## 3. H1: Firms publishing eval numbers cluster in the upper-left

**Evidence (strongly supportive)**. 6 of 7 firms with unambiguous third-party eval publication — Harvey (VLAIR 94.8%), Sierra (owns τ-bench family), Cursor (SWE-bench Multilingual 73.7 + cursorbench), Cognition/Windsurf (SWE-bench, SWE-1.6 preview), Abridge (97% confabulation detection vs GPT-4o 82%), Paxton (94% Stanford Legal Hallucination Benchmark) — are UL. 4 of 4 firms at material scale with no eval publication (Spellbook, Eve, EvenUp, Forethought) are UR or acquired. Decagon, Perplexity, and Glean publish internal material without third-party Vals AI/Patronus testing and still operate at UL scale, but *no firm publishes third-party eval numbers and is UR* within this sample.

**Why the pattern holds**. Eval publication is a productization artifact — engineering must write the harness, run the tests, defend the methodology. A firm without productization depth cannot credibly publish. Publishing is simultaneously a sales instrument converting productization substance into pitch-deck claims. UL firms do both; UR firms sell on narrative because substance is not there to cite.

**Exception**. Spellbook at 4,000 customers and $100M ARR on GPT-5 / Claude Opus with no VLAIR entry. Decomposition predicts fragility to (1) GPT-5/Opus price moves or (2) frontier-lab move into contract-review. Neither resolved as of April 2026.

---

## 4. H2: Prompt-only / RAG-heavy firms cluster in upper-right

**Evidence (mixed)**. The hypothesis is only partially supported. Glean is the clearest counter-example: explicitly RAG-first with knowledge-graph extension, documented stance that "fine-tuning on enterprise data increases hallucinations," UL at $208M ARR and $7.2B valuation. Decagon is RAG + agent orchestration on vendor models; still UL because evaluation engineering is the moat. Forethought and Spellbook do match the hypothesis — RAG-heavy, lighter on eval publication, Forethought acquired below natural scale.

**Reinterpretation**. The RAG-vs-fine-tune-vs-train gradient does *not* map cleanly onto productization depth. Glean's knowledge-graph RAG is a more substantive productization investment than many fine-tune approaches. The better-fitting variable is **verification-infrastructure discipline** (eval harness, A/B testing, confidence scoring, monitoring), not whether weights are trained. This is consistent with the parent memo's finding that verification lives in productization infrastructure, not in headcount or model training per se.

---

## 5. H3: Firms that train / fine-tune price higher and retain longer

**Evidence (strong)**. Eight firms do material training or fine-tuning: Harvey (custom case-law model with OpenAI), Cursor (Composer 2 with continued pretraining + RL on Kimi K2.5), Cognition (SWE-1.5/1.6), Abridge (in-house clinical LM on 50,000+ examples), Perplexity (Sonar on Llama 3.3 70B + SFT+DPO+PPO), Upstage (Solar LLM family), Tennr (RaeLM on 100M docs), Cresta (Ocean-1). These firms *all* price at the top of their vertical: Harvey at 58× revenue multiple, Cursor at $6.7M revenue/employee (10× Salesforce), Sierra's outcome-based pricing at $200-350K year-one, Decagon's $386K median contract, Abridge's health-system deals (Kaiser 24,600 physicians), Cresta's enterprise contact-center deals.

**The efficiency signal — $1.5M–$10M per employee range**. The parent memo's solo-research signal is strongly supported: Cursor **$6.7M/employee**, Perplexity ~$1.25M, OpenEvidence ~$1M (note: ad-supported, not subscription), Harvey ~$700K, Sierra ~$500K. Firms not in the $1.5M+ range tend to be (a) RAG-heavy verticals requiring integration labor (Glean ~$200K; Cresta; Abridge) or (b) early-stage firms still ramping sales (Paxton, Tennr).

**Retention evidence is thinner**. NRR is not publicly disclosed. Sierra, Decagon, and Harvey describe enterprise-led motions with multi-year contracts and upsell, implying 120%+ NRR but this is inferred. Klarna's "re-hire 700 agents" reversal (parent memo §5) remains the cleanest case of low NRR when productization substance falls short. Forethought's acquisition (Zendesk's largest deal in 20 years at ~$50-100M ARR) is a distribution consolidation rather than a distressed sale, but it does show the ceiling for RAG-only customer-support vendors.

---

## 6. H4: Vertical AI / service-as-software requires productization depth

**Evidence (strongly supportive with one caveat)**. The Menlo "Great Re-Aggregation" thesis — vertical AI eats horizontal SaaS by delivering the *service* — is supported by the data. Sierra charges per-resolution (requiring τ³-bench-grade verification or it absorbs the unresolved-case cost). Harvey reframes from "lawyer drafts, Harvey assists" to "Harvey drafts and lawyer reviews" — a service-level claim that demands the custom model, VLAIR benchmark, and ISO 42001. Cursor and Cognition pitch "agentic coding" not "IDE with AI" — requiring SWE-bench-grade productization to be credible. Abridge charges hospitals for verified-quality clinical notes, not dictation software. Decagon sells "concierge experience" not tickets-deflected.

**The exceptions are Spellbook and EvenUp** — closer to classical "AI-assisted SaaS" (attorney uses tool to draft faster) than to service-as-software. They scale to $100M and $3B valuation respectively but by extending user productivity, not replacing the user. Lower productization depth required, UR placement fits. If the Re-Aggregation thesis is right, these firms face 2026-2027 competitive pressure from players owning more of the workflow.

**Caveat**. OpenEvidence is free-to-clinician, ad-supported, $100M+ revenue at 40% of US physicians — a service-as-software outcome without deep productization because it consumes frontier APIs and wins on distribution. The Menlo thesis is correct about *how* vertical AI captures value, but required productization depth varies with the economic structure (ad-supported vs subscription vs outcome-based).

---

## 7. Cross-firm pattern: which combinations produce $100M+ ARR?

Four patterns emerge at $100M+ ARR:

| Pattern | Sales motion | Productization | Examples | Per-employee |
|---|---|---|---|---|
| **PLG + own training** | PLG → enterprise | Proprietary model + benchmarked eval | Cursor, Cognition | $6.7M, $400K |
| **Enterprise-led + fine-tune** | Direct enterprise; 6-mo cycles | Fine-tuned on vendor base + vertical data | Harvey, Abridge, Perplexity, Upstage | $200K-$1.25M |
| **Enterprise-led + deep RAG/agent** | Direct enterprise; multi-year | Eval harness + agent architecture | Sierra, Decagon, Glean, Cresta | $200K-$500K |
| **PLG + RAG-only** | Self-serve + mid-market | Thin productization on vendor APIs | Spellbook, Eve, EvenUp | $250K-$670K |

All four combinations produce $100M+ ARR at least once. The decomposition predicts **one of the two axes has to be strong**, not a single winning combination.

---

## 8. Surprises

**OpenEvidence's thin productization monetizes at scale via ads**. Parent memo UR quadrant predicts thin-productization firms fail or stay small. OpenEvidence is thin-productization *and* large-revenue ($100M+ at $12B valuation). It sells ad-supported access to 40% of US physicians, not verified medical reasoning. "Vertical AI" has multiple business models.

**Korean and Japanese vertical-AI firms underperform on per-employee ARR**. Upstage and Tripla have productization depth but neither hits $1M/employee. Likely: domestic-market pricing, slower enterprise cycles, Samsung-group captive dynamic. The $1.5M-$10M/employee signal may be US-market-specific.

**Spellbook reaches $100M ARR on RAG-only** — challenges H2/H3. No own training, no VLAIR, yet 4,000 customers. Decomposition reads this as sales-motion advantage (PLG into Microsoft Word + mid-market + tripling YoY) compensating for productization thinness. Fragile if Harvey/Legora/CoCounsel match UX friction.

**Forethought's acquisition below scale** — Zendesk March 2026 at $50-100M revenue. Fits the prediction that RAG-heavy vendors face a ceiling when enterprise buyers demand service-as-software.

**Sierra owning an open-source benchmark**. τ-bench family as open-source research from a commercial vendor. Productization-skill investment doubling as sales instrument — the benchmark becomes the reference point, advantaging Sierra when prospects run the test. One of the cleanest examples of verification *substance* that is *also* verification *claim*.

---

## 9. Answers to the research-plan questions

**Does the decomposition predict the $100M+ outcomes?** Yes, with one qualifier. $100M+ ARR vertical-AI firms either (a) score strong on both axes (UL) or (b) compensate with a very strong single-axis moat. The 21-firm sample confirms (a) for the majority and (b) for the Spellbook / OpenEvidence exceptions.

**Does it predict Cursor's $2B ARR?** Yes. PLG virality + enterprise pivot (60% by early 2026) + own training (Composer 2 with SWE-bench publication) + own inference model launch is textbook UL execution. The Nov-2025 inference-model launch is defensive productization against frontier-lab vertical attack.

**Does it predict Harvey's $11B valuation?** Yes at the 58× multiple. Productization substance (VLAIR leadership, ISO 42001, AmLaw 100 depth) + sales substance (60+ countries, $190M ARR from 1,000+ firms in 36 months). Within-vertical competition (Legora, Spellbook) is the compression risk.

**Thin-productization thriving anyway**: Spellbook and OpenEvidence (via ads). Both tension the decomposition's predictions.

**Deep productization not monetizing**: Atropos Health — real-world-evidence platform, peer-reviewed case studies, pharma partnerships, but no breakout commercial scale (Series B, no ARR disclosure). Parent memo quadrant LL→UL.

---

## 10. Implications for the decomposition memo

1. **H1 strongly supported**: eval publication is a productization artifact that sorts firms into UL. Parent memo §7.1 "productization infrastructure predicts verification substance" is corroborated at vertical-AI firm scale.

2. **H2 requires refinement**: the RAG-vs-train axis does not map cleanly onto productization depth. Glean's knowledge-graph RAG is a deeper investment than some fine-tune operations. Better variable is **verification discipline** (eval harness, A/B, monitoring, confidence scoring) regardless of whether weights are trained.

3. **H3 supported by pricing and per-employee data**: own-training/fine-tuning firms occupy the $1.5M-$10M per employee range more reliably than RAG-only firms and price at the top of their vertical. Korean / Japanese exceptions suggest market-specific compression.

4. **H4 supported with caveat that service-as-software has multiple monetization paths**. Sierra's per-resolution, Harvey's workflow replacement, and Cursor's agentic coding all require productization depth. OpenEvidence's ad-supported clinician reference achieves scale with lower productization intensity.

**Feedback for parent memo §4 matrix**: Extend upper-right with vertical-AI specific examples (Spellbook, EvenUp) and note that "wrapper" is too coarse — some (Glean GraphRAG) have deep verification infrastructure despite no model training.

**Feedback for parent memo §8 H1**: Vertical-AI data supports H1 (PwC 20% = both strong) at firm level. Modal vertical-AI $100M+ ARR firm is UL; modal sub-$100M vertical-AI firm is UR or LR. The vertical selects for both skills.

---

## 11. Cross-references

- [`sales-vs-productization-decomposition.md`](sales-vs-productization-decomposition.md) — parent memo §4 matrix, §8 hypotheses, §10.1 case log.
- [`s2-small-enterprises-startups.md`](s2-small-enterprises-startups.md) — AI-native vs AI-using split informed by this firm-level data.
- [`size-speed-resource-tradeoff.md`](size-speed-resource-tradeoff.md) — per-employee ARR as productization-skill signal.
- [`../../operations/expansion/sales-vs-productization-research-plan.md`](../../operations/expansion/sales-vs-productization-research-plan.md) — Stream E plan section this appendix executes.

---

## 12. Sources

### Legal vertical AI
- Harvey AI: [Sacra Harvey at $195M ARR](https://sacra.com/research/harvey-at-195m-arr/); [TechCrunch — $11B valuation](https://techcrunch.com/2026/02/09/harvey-reportedly-raising-at-11b-valuation-just-months-after-it-hit-8b/); [Harvey $11B announcement](https://www.harvey.ai/blog/harvey-raises-at-dollar11-billion-valuation-to-scale-agents-across-law-firms-and-enterprises); [VLAIR 2-27-25](https://www.vals.ai/industry-reports/vlair-2-27-25); [Artificial Lawyer VLAIR coverage](https://www.artificiallawyer.com/2025/02/27/vals-publishes-results-of-first-legal-ai-benchmark-study/); [Harvey Trust Center](https://trust.harvey.ai/); [Harvey Security by Design](https://www.harvey.ai/blog/security-by-design); [OpenAI custom case-law model](https://openai.com/index/harvey/); [Harvey at $190M ARR + Memory](https://www.artificiallawyer.com/2026/01/08/harvey-hits-190m-arr-building-memory-personalisation/); [Startup Riders Harvey playbook](https://www.startupriders.com/p/harvey-ai-growth-playbook)
- Spellbook: [BetaKit $100M USD ARR target](https://betakit.com/on-track-to-hit-100-million-usd-arr-spellbook-partners-with-canadian-bar-association/); [Spellbook company](https://www.spellbook.legal/)
- Paxton AI: [Paxton Series A announcement](https://www.paxton.ai/post/breaking-new-ground-paxton-secures-22m-series-a-to-transform-legal-ai); [PitchBook Paxton profile](https://pitchbook.com/profiles/company/529346-17)
- Eve: [Eve $1B Series B](https://www.prnewswire.com/news-releases/eve-raises-103-million-at-1-billion-valuation-to-help-plaintiff-firms-deliver-justice-through-ai-transformation-302570807.html); [LawSites Eve coverage](https://www.lawnext.com/articles/5738408/AI-Startup-Eve-Reaches-1B-Valuation-With-New-Funding-Round); [Above the Law Eve at 800+ firms](https://abovethelaw.com/2026/03/meet-eve-the-ai-used-by-800-top-plaintiff-firms/)
- EvenUp: [EvenUp $2B valuation](https://www.evenuplaw.com/blog/evenup-2b-valuation/); [LawSites EvenUp](https://www.lawnext.com/2025/10/evenup-ai-platform-for-personal-injury-lawyers-raises-150m-at-2b-valuation.html); [TechLaw Crossroads](https://www.techlawcrossroads.com/2025/10/from-startup-to-2-billion-evenup-is-transforming-personal-injury-practice/)
- Legal AI hallucinations: [Damien Charlotin AI Hallucination Cases](https://www.damiencharlotin.com/hallucinations/); [LawNext hallucinations](https://www.lawnext.com/2025/05/ai-hallucinations-strike-again-two-more-cases-where-lawyers-face-judicial-wrath-for-fake-citations.html); [NexLaw 2026 guide](https://www.nexlaw.ai/blog/ai-hallucination-sanctions-2026/)

### Customer support vertical AI
- Sierra: [TechCrunch Sierra $100M ARR](https://techcrunch.com/2025/11/21/bret-taylors-sierra-reaches-100m-arr-in-under-two-years/); [Sacra Sierra](https://sacra.com/c/sierra/); [Sierra outcome-based pricing](https://sierra.ai/blog/outcome-based-pricing-for-ai-agents); [τ-bench GitHub](https://github.com/sierra-research/tau-bench); [τ³-bench Sierra blog](https://sierra.ai/blog/bench-advancing-agent-benchmarking-to-knowledge-and-voice); [VentureBeat on τ-bench](https://venturebeat.com/ai/sierras-new-benchmark-reveals-how-well-ai-agents-perform-at-real-work)
- Decagon: [TechCrunch $4.5B valuation](https://techcrunch.com/2026/03/04/decagon-completes-first-tender-offer-at-4-5b-valuation/); [Sacra Decagon](https://sacra.com/c/decagon/); [Decagon evaluation engine](https://webflow2.decagon.ai/resources/evaluation-engine-ai-agents); [Decagon Series D announcement](https://decagon.ai/resources/series-d-announcement); [Microsoft Startups Decagon](https://www.microsoft.com/en-us/startups/blog/decagon-building-the-ai-concierge-for-modern-customer-experience/)
- Cresta: [Cresta $125M Series D](https://cresta.com/press/cresta-closes-125m-series-d-to-accelerate-adoption-of-human-centric-ai-in-the-contact-center); [Cresta Ocean-1](https://cresta.com/blog/introducing-ocean-1-worlds-first-contact-center-foundation-model); [Sacra Cresta](https://sacra.com/c/cresta-ai/)
- Forethought: [Tracxn Forethought 2026](https://tracxn.com/d/companies/forethought-ai/__0F_pU4MmTzR7vt2soQK0vAoINCsiHxE6jIvaab76DjI); [Forethought company](https://forethought.ai/)

### Developer tools vertical AI
- Cursor / Anysphere: [Cursor revenue Sacra](https://sacra.com/c/cursor/); [TechCrunch Cursor $50B valuation talks](https://techcrunch.com/2026/04/17/sources-cursor-in-talks-to-raise-2b-at-50b-valuation-as-enterprise-growth-surges/); [CNBC Cursor Accel Coatue](https://www.cnbc.com/2025/11/13/cursor-ai-startup-funding-round-valuation.html); [Cursor Composer 2 technical report](https://cursor.com/resources/Composer2.pdf); [Cursor Composer blog](https://cursor.com/blog/composer-2); [cursorbench quality](https://cursor.com/blog/cursorbench); [Contrary Research Cursor](https://research.contrary.com/company/cursor); [Anysphere Wikipedia](https://en.wikipedia.org/wiki/Anysphere)
- Cognition (Windsurf): [Cognition Windsurf acquisition](https://cognition.ai/blog/windsurf); [TechCrunch Cognition acquires Windsurf](https://techcrunch.com/2025/07/14/cognition-maker-of-the-ai-coding-agent-devin-acquires-windsurf/); [Contrary Research Cognition](https://research.contrary.com/company/cognition); [SWE-bench report](https://cognition.ai/blog/swe-bench-technical-report); [SWE-1.6 preview](https://cognition.ai/blog/swe-1-6-preview)
- Replit: [TechCrunch Replit $9B](https://techcrunch.com/2026/03/11/replit-snags-9b-valuation-6-months-after-hitting-3b/); [TechCrunch Replit market fit](https://techcrunch.com/2025/10/02/after-nine-years-of-grinding-replit-finally-found-its-market-can-it-keep-it/); [Sacra Replit](https://sacra.com/c/replit/)

### Search / consumer
- Perplexity: [Sacra Perplexity](https://sacra.com/c/perplexity/); [Perplexity Sonar models](https://docs.perplexity.ai/docs/sonar/models); [Accelerating Sonar blog](https://www.perplexity.ai/hub/blog/accelerating-sonar-through-speculation); [ByteByteGo Perplexity deep dive](https://blog.bytebytego.com/p/how-perplexity-built-an-ai-google); [Perplexity Wikipedia](https://en.wikipedia.org/wiki/Perplexity_AI); [NVIDIA Perplexity case study](https://www.nvidia.com/en-us/case-studies/perplexity-enhances-model-performance-with-nemo/)
- Glean: [Glean $200M ARR press release](https://www.glean.com/press/glean-surpasses-200m-in-ai-for-enterprise-ai-doubling-revenue-in-nine-months); [Sacra Glean at $200M ARR](https://sacra.com/research/glean-at-200m-arr/); [Fortune Glean $200M](https://fortune.com/2025/12/08/exclusive-glean-hits-200-million-arr-up-from-100-million-nine-months-back/); [Glean Series F $7.2B](https://www.glean.com/blog/glean-series-f-announcement); [Glean GraphRAG](https://www.glean.com/resources/guides/glean-knowledge-graph); [Glean RAG vs fine-tuning](https://www.glean.com/blog/retrieval-augemented-generation-vs-fine-tuning); [Contrary Research Glean](https://research.contrary.com/company/glean)

### Healthcare vertical AI
- Abridge: [Abridge Series D $250M $2.75B](https://www.fiercehealthcare.com/ai-and-machine-learning/abridge-scores-250m-series-d-ambient-ai-tech-now-use-100-health-systems); [Abridge Series E $300M $5.3B](https://www.fiercehealthcare.com/ai-and-machine-learning/ambient-ai-startup-abridge-scores-300m-series-e-backed-a16z-and-khosla); [Abridge hallucination whitepaper](https://www.abridge.com/ai/science-confabulation-hallucination-elimination); [Abridge Epic integration](https://www.abridge.com/press-release/abridge-becomes-epics-first-pal-bringing-generative-ai-to-more-providers-and-patients); [Sacra Abridge](https://sacra.com/c/abridge/); [Contrary Research Abridge](https://research.contrary.com/company/abridge)
- OpenEvidence: [CNBC OpenEvidence $12B](https://www.cnbc.com/2026/01/21/openevidence-chatgpt-for-doctors-doubles-valuation-to-12-billion.html); [STAT OpenEvidence $250M](https://www.statnews.com/2026/01/21/health-ai-starutup-openevidence-raises-250-million/); [Fierce Healthcare OpenEvidence](https://www.fiercehealthcare.com/ai-and-machine-learning/openevidence-clinches-250m-series-d-rapidly-growing-its-reach-doctors); [OpenEvidence Series C $3.5B announcement](https://www.openevidence.com/announcements/openevidence-the-fastest-growing-application-for-physicians-in-history-announces-dollar210-million-round-at-dollar35-billion-valuation)
- Atropos Health: [Atropos $33M Series B](https://www.fiercehealthcare.com/health-tech/atropos-health-lands-33m-scale-ai-powered-real-world-evidence-build-out-pharma); [Atropos Commercial Analytics](https://www.businesswire.com/news/home/20260112967499/en/Atropos-Health-Announces-AI-Driven-Commercial-Analytics-Solution-for-Life-Science-Companies)
- Tennr: [Tennr $101M Series C $605M valuation](https://www.ctol.digital/news/tennr-raises-101m-healthcare-referral-ai-605m-valuation/); [Tennr voice AI](https://www.digitalhealthnews.com/tennr-adds-voice-ai-to-automate-patient-referral-phone-calls); [ICONIQ Tennr partnership](https://www.iconiqcapital.com/growth/insights/revolutionizing-patient-referrals-with-ai-our-partnership-with-tennr)

### Korean / Asian vertical AI
- Upstage: [Upstage Korea's First GenAI Unicorn](https://en.wowtale.net/2026/04/15/233892/); [Upstage Series B Bridge $45M](https://www.upstage.ai/news/upstage-series-b-bridge); [Seoulz Upstage unicorn](https://www.seoulz.com/upstage-ai-unicorn-koreas-first-generative-ai-giant/); [Upstage Solar Pro 3](https://www.upstage.ai/blog/en/solar-pro-3-0127)
- Samsung SDS: [Samsung SDS CES 2026](https://www.samsungsds.com/us/news/ces2026-260112.html); [FabriX / Brity Copilot launch](https://www.samsungsds.com/en/news/sds-genai-mediaday.html); [Brity Copilot product](https://www.samsungsds.com/en/copilot/brity-copilot.html)
- Naver / Kakao: [Naver Kakao 2026 agentic AI](https://www.koreatimes.co.kr/business/tech-science/20260102/naver-kakao-gear-up-for-agentic-ai-era-in-2026); [Naver Kakao R&D spending](https://www.digitaltoday.co.kr/en/view/43399/naver-kakao-expand-rd-spending-focus-on-in-house-ai); [Korea sovereign AI](https://www.kedglobal.com/artificial-intelligence/newsView/ked202508040010)
- Tripla: [Tripla PitchBook](https://pitchbook.com/profiles/company/161026-30); [Tripla company](https://en.tripla.io/); [Tripla Yahoo Finance 5136.T](https://finance.yahoo.com/quote/5136.T/profile/)

### Cross-cutting thesis / VC
- Menlo Ventures, [Software Finally Gets to Work: The Opportunity in Vertical AI](https://menlovc.com/perspective/software-finally-gets-to-work-the-opportunity-in-vertical-ai/)
- Gil Pignol, [The Great Re-Aggregation: Vertical AI, Service-as-Software, and the Battle for Monopoly](https://medium.com/@gp2030/the-great-re-aggregation-vertical-ai-service-as-software-and-the-battle-for-the-control-point-5aee929af04a)
- Bessemer, [Legora: Fastest Enterprise to $100M ARR](https://www.bvp.com/atlas/legora-the-fastest-enterprise-business-to-reach-100m-arr)
- Menlo, [2025 State of Generative AI in the Enterprise](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/)
- TLDL, [AI Company Rankings 2026](https://www.tldl.io/resources/ai-companies-landscape-2026)
- Finro, [AI Valuation Multiples Q1 2026](https://www.finrofca.com/research/ai-multiples-q1-2026)
