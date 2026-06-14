# M2 — Measurable Indicators of AI-Era Organizational Adaptability

axis: M (Meta — Cross-Pillar Integration)
date: 2026-04-22
plan: research/operations/expansion/adaptability-framework-research-plan.md

---

## 1. Method

Candidate indicators were drawn from three sources: (a) the seven candidates listed in the M2 research prompt, (b) analogues from DORA and SPACE developer-productivity frameworks (GitHub/Microsoft/Victoria University, 2021; DORA 2024), and (c) adjacent benchmark data from Stanford HAI AI Index 2025, McKinsey State of AI March 2025, Menlo Ventures 2024 and December 2025 reports, a16z Enterprise CIO 2025, Ravio Salary Benchmarks 2025 and 2026, JetBrains Developer Ecosystem Survey 2025, Atlassian State of Developer Experience 2025, and Deloitte State of Generative AI 2025. For each candidate, three filters were applied: (i) **construct-concept fit** — does the number actually measure adaptability rather than size, spend, or hype? (ii) **measurement feasibility** — can a mid-market CFO or CTO collect it quarterly without bespoke instrumentation? (iii) **gaming resistance** — how easy is it to move the indicator without moving the underlying capability? Seven candidates were reduced to six retained, one dropped (adaptation-to-overcorrection ratio) and partially re-absorbed into a composite "reversal-adjusted change velocity" sub-metric. Benchmark ranges are labelled `observed`, `estimated`, or `modelled` and carry confidence tiers (high/medium/low). Small/mid/large boundaries are taken at <250 FTE, 250–5,000 FTE, >5,000 FTE — identical to the scale-based track's S2/S3/S4 split for cross-track comparability.

---

## 2. Indicator specification

Six indicators are retained. Each is specified as a precise formula, data source, measurement method, construct risk, gaming risk, industry benchmarks, and reference ranges.

### 2.1 Capability-to-Deployment Lag (CDL)

**Definition.** `CDL = median(days between vendor public release of capability C and first production traffic using C in the organization)` over the last eight capability releases tracked. A "capability" is an externally observable unit — model generation, long context, function calling, vision, reasoning, agent, computer use, multimodal generation. "Production traffic" means real user-facing or revenue-generating inference — explicitly excluding hackathon, internal demo, or staged eval.

**Data-source feasibility.** Internal telemetry (model router logs, feature-flag activation timestamps) cross-referenced with vendor release notes. Feasibility is **high** for engineering-led orgs, **medium** for orgs that outsource AI to SIs, **low** for purely vendor-dependent adopters.

**Measurement method.** Pick a reference capability list (e.g., every quarterly GPT/Claude/Gemini release + one non-model capability per quarter). For each release, record `release_ts` from the vendor and `first_prod_ts` from the gateway that first served paid / customer-facing requests using the new capability. Median the differences; exclude retired capabilities.

**Construct validity concerns.** CDL punishes deliberate non-adoption — an org that correctly waited for a bug-fix release scores *worse*, even though waiting was the right call. Mitigation: report CDL alongside post-deployment incident rate, so "fast and stable" and "fast and broken" look different.

**Known gaming risks.** Shadow deploys to internal tools counted as production; selection bias in which releases enter the list; "flag-flip" deploys with zero traffic but recorded timestamps. Mitigation: require minimum traffic threshold (e.g., ≥1% of relevant route QPS) and a pre-registered capability list.

**Industry benchmarks (2023–2026).**
- Cursor: GPT-4 Turbo release (2023-11-06) → integrated within 24 h [observed, high confidence]. Cursor reached $100M ARR in ~12 months and hit $2B ARR by 2026-02, with model-refresh turnaround typically <72 h ([TechCrunch 2026-03-02](https://techcrunch.com/2026/03/02/cursor-has-reportedly-surpassed-2b-in-annualized-revenue/)).
- Harvey: Claude 3.5 Sonnet release (2024-06-20) → production rollout ~3–4 weeks [estimated from reported growth cadence, medium confidence]. Harvey grew from $50M ARR end-2024 to $195M ARR end-2025 ([Sacra](https://sacra.com/c/harvey/)).
- Enterprise median: Stanford AI Index 2025 records a shift from 35% enterprise AI implementation in 2023 to 67% in 2025, but reaching production remains slow — "nearly two-thirds of respondents say their organizations have not yet begun scaling AI across the enterprise" ([McKinsey State of AI March 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)). This implies a typical enterprise CDL of **90–180 days** for a new model generation, **180–360 days** for a new modality (e.g., agents, computer use) [estimated, medium confidence].

**Reference ranges (days, lower is more adaptive).**

| Org size | Green / adaptive | Yellow / watch | Red / lagging |
|---|---|---|---|
| Small (<250 FTE) | ≤ 14 | 15–45 | > 45 |
| Mid (250–5,000) | ≤ 30 | 31–90 | > 90 |
| Large (>5,000) | ≤ 60 | 61–180 | > 180 |

### 2.2 Model-Switching Cost (MSC)

**Definition.** `MSC = engineer-days spent to cut over a primary LLM between two major model generations, from cut-over decision to steady-state production`, measured for the single largest inference route. Includes: prompt re-engineering, eval re-baselining, canary deploy, rollback preparedness, guardrail re-tuning. Excludes: ambient work continuing during the migration.

**Data-source feasibility.** Internal Jira / Linear story points converted to days, plus a post-migration retrospective. Feasibility **high** for orgs that run migration as a named project, **low** when migration is diffused across many teams.

**Measurement method.** Define the "primary route" as the inference path with the largest share of paid-or-customer-facing token volume. Tag every story / task linked to the migration with a migration label; sum engineer-days; divide by one. Record both planned and actual engineer-days; the ratio is a secondary indicator of estimation discipline.

**Construct validity concerns.** MSC reflects *accumulated architectural coupling* at least as much as it reflects current adaptability — a greenfield startup will always beat a ten-year-old codebase. Mitigation: report MSC per 10,000 lines of AI-adjacent code, or per unique prompt in production, rather than absolute engineer-days.

**Known gaming risks.** (a) Skipping eval rebaseline to post a low number — visible later as incident rate. (b) Migrating only the trivial route and calling it done. (c) "Routing switch" pretending to be a migration (model A still serves 95% of traffic). Mitigation: require traffic-share validation (≥80% of the route on the new model for ≥14 days) before counting the migration closed.

**Known gaming risks — structural.** a16z reports "as companies invest the time and resources into building guardrails and prompting for agentic workflows, they're more hesitant to switch to other models" ([a16z Enterprise 2025](https://a16z.com/ai-enterprise-2025/)). Menlo Ventures finds that "only 11% of teams report changing model providers in the past year, but 66% upgraded to newer models from their existing vendor" ([Menlo 2025 State of Gen AI](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/)). This means MSC is measurable mostly on *within-vendor version upgrades*; *cross-vendor* MSC is a different and much rarer event, and both should be tracked.

**Industry benchmarks.**
- Third-party reports for enterprise cross-provider migrations put cost at "tens of thousands to over a hundred thousand dollars" in development, with timelines "months" ([Vertesia LLM obsolescence 2025](https://vertesiahq.com/blog/your-model-has-been-retired-now-what)). At a US loaded rate of ~$1,500/engineer-day, that implies roughly 30–70 engineer-days for a mid-complexity migration [estimated, medium].
- Anthropic Claude 3 Haiku deprecation (retirement 2026-04-19) forced forced cutovers on all production users of that model; replacement Haiku 4.5 cost 4× more per token ([Abhs.in migration guide](https://www.abhs.in/blog/claude-3-haiku-deprecation-april-2026-migration-guide)). Forced migrations consistently cost more engineer-days than elective ones because the deadline removes the option to batch with other work [observed, high].
- Within-vendor upgrades (e.g., Claude 3 → 3.5, GPT-4 → GPT-4o) typically cost 5–15 engineer-days for small / mid product teams according to engineering-blog post-mortems [estimated, medium].

**Reference ranges (engineer-days for a within-vendor major upgrade on the primary route; cross-vendor typically 2–4× higher).**

| Org size | Green | Yellow | Red |
|---|---|---|---|
| Small | ≤ 3 | 4–10 | > 10 |
| Mid | ≤ 10 | 11–30 | > 30 |
| Large | ≤ 30 | 31–90 | > 90 |

### 2.3 Role Redefinition Frequency (RRF)

**Definition.** `RRF = formal role changes attributable to AI in the last 12 months per 1,000 FTE`. A "formal role change" is a documented change to role title, role description, level band, reporting line, or primary job cluster. "Attributable to AI" requires a written rationale citing AI capability or AI workflow redesign — not a generic reorg.

**Data-source feasibility.** HRIS (Workday / BambooHR / Rippling), plus a coded AI-rationale tag. Feasibility **high** with a clean HRIS and a role-change workflow; **medium** without structured change tagging.

**Measurement method.** Pull all role changes in the period; hand-code or LLM-code the rationale field against an "AI attribution" rubric; divide AI-attributed count by (average FTE over period / 1,000). Report separately: roles *created*, roles *eliminated*, roles *redefined without rename*.

**Construct validity concerns.** (a) Rebranding (call everyone a "Prompt Engineer" one quarter, retitle them all "AI Engineer" the next) inflates RRF without real structural change. (b) RRF conflates "we are redesigning thoughtfully" with "we keep flip-flopping." Mitigation: pair RRF with a 12-month role-reversal sub-metric — how many of this year's role changes were reverted or re-reverted within 12 months.

**Known gaming risks.** Title inflation, shell roles created during hiring freezes (Shopify's "prove AI can't do it" memo created pressure to rename open requisitions rather than close them; [Fortune 2025-04-10](https://fortune.com/2025/04/10/shopify-ceo-ai-will-kill-jobs-other-ceos-just-wont-admit-it/)), and under-counting of quiet consolidations (roles merged without rename).

**Industry benchmarks.**
- Ravio reports AI-specific job titles grew from 0.32% of all roles in 2024 to 2.17% in early 2025, with AI/ML hires up 88% in 2025 ([Ravio 2025 tech jobs report](https://ravio.com/tech-jobs-report-2025)).
- Chief AI Officer adoption in Fortune 500: ~11% in 2023 → ~26% in 2024 → projected ~40% by end of 2026 ([Findem](https://www.findem.ai/blog/insights-chief-ai-officer), [Fortune 2024-08-12](https://fortune.com/2024/08/12/chief-ai-officer-not-so-fast-say-experts/)).
- Amazon: announced ~14,000 corporate-job cuts in October 2025 with potential to reach 30,000, framed explicitly as AI-driven restructuring ([CNBC 2025-06-17](https://www.cnbc.com/2025/06/17/ai-amazon-workforce-jassy.html)). Across a 350,000 corporate headcount that implies an AI-attributable RRF in the range 40–85 per 1,000 FTE in 2025 [observed, high].
- Klarna: workforce cut from 5,500 to 3,400 (2022–2024) on AI rationale, followed by partial rehiring in 2025 ([Tech.co](https://tech.co/news/klarna-reverses-ai-overhaul)). RRF peaked in 2024 at an exceptional rate, then reversed — a clear illustration of the reversal risk the sub-metric is designed to catch.

**Reference ranges (changes per 1,000 FTE per 12 months).**

| Org size | Green (healthy adaptation) | Yellow | Red (thrash or stagnation) |
|---|---|---|---|
| Small | 30–150 | 150–300 or 10–30 | >300 or <10 |
| Mid | 20–80 | 80–160 or 8–20 | >160 or <8 |
| Large | 10–40 | 40–80 or 3–10 | >80 or <3 |

Green is an *interval*, not a ceiling — **too little** role change under monthly-cadence AI turnover is as adaptability-risky as too much. This is the indicator's most important design choice.

### 2.4 AI-Subsystem Technical-Debt Accrual Rate (TDAR)

**Definition.** `TDAR = (net growth in AI-subsystem technical-debt backlog story points per quarter) / (AI-subsystem engineering capacity story points per quarter)`. "AI subsystem" covers prompts-as-code, RAG pipelines, evaluator harnesses, observability, fine-tune / adapter lifecycle, router / fallback logic. TDAR > 1 means debt is being added faster than capacity could close it even if capacity were entirely redirected to debt. TDAR < 0 means net paydown.

**Data-source feasibility.** Engineering tracker (Jira / Linear / Shortcut) with a "tech-debt" label convention and an AI-subsystem component tag. Feasibility **medium** — most shops don't discipline the debt label. Feasibility **high** in orgs that run an explicit debt register, as recommended by Databricks and Kong for LLM systems ([Databricks](https://www.databricks.com/blog/hidden-technical-debt-genai-systems), [Kong 2025](https://konghq.com/blog/learning-center/reducing-technical-debt)).

**Measurement method.** Sum story points added with the debt label in AI-subsystem components, subtract points closed with the same label, divide by capacity available to the AI-subsystem team. Normalize quarterly. Report both raw TDAR and the fraction of debt that is *model-version-coupled* (prompts / evals / guardrails pinned to a specific model version) — this is the debt that explodes at the next deprecation.

**Construct validity concerns.** (a) Orgs that don't tag debt score artificially clean. (b) Recent research identifies three LLM-specific SATD categories (Model-Stack Workaround, Model-Dependency, Performance-Optimization) accounting for 18% of classified debt — generic debt trackers miss these ([arXiv 2601.06266](https://arxiv.org/html/2601.06266v1)). Mitigation: require the debt taxonomy to include these three, or TDAR will systematically under-read.

**Known gaming risks.** Stop labelling; relabel debt as "tech investment"; close-and-reopen shuffles. Mitigation: audit a random sample of closed debt tickets per quarter for actual code change; compare backlog age distribution over time (gaming shows up as a sudden compression of the distribution without corresponding merge commits).

**Industry benchmarks.**
- No published industry-wide TDAR figures exist — this is a coverage gap.
- DORA 2024 notes AI tooling correlates with *worse* software-delivery stability, implying debt is accruing faster than it is being retired in the aggregate ([DORA 2024 report](https://dora.dev/research/2024/dora-report/), [InfoQ 2024-11](https://www.infoq.com/news/2024/11/2024-dora-report/)). Individual productivity up, organizational throughput flat or worse — classic debt accrual pattern [observed, medium confidence that DORA is pointing at debt specifically; the report frames it as quality/stability].
- The "TODO: Fix the Mess Gemini Created" study (arXiv 2601.07786) observes a statistically large rise in GenAI-induced self-admitted technical debt in 2024–2025 codebases [observed, medium].

**Reference ranges (ratio, lower is better; ≤0 is net paydown).**

| Org size | Green | Yellow | Red |
|---|---|---|---|
| Small | ≤ 0.2 | 0.2–0.6 | > 0.6 |
| Mid | ≤ 0.3 | 0.3–0.8 | > 0.8 |
| Large | ≤ 0.4 | 0.4–1.0 | > 1.0 |

### 2.5 Recent-Capability Revenue Share (RCRS)

**Definition.** `RCRS = revenue in the last full quarter attributable to AI capabilities first exposed to customers within the preceding 180 days / total revenue in the last full quarter`. For AI-native firms, this tests whether new capability is a growth engine. For incumbents, it tests whether new capability is translating to P&L, not just to demos.

**Data-source feasibility.** Finance + product analytics joined at the SKU / feature-flag level. Feasibility **high** for product-led orgs with feature-flag-level billing; **medium** for SaaS with coarse SKU structure; **low** for services businesses where AI is embedded in delivery but not separately billed. Services-heavy orgs should instead report *AI-attributable win rate* on new deals.

**Measurement method.** Tag each revenue SKU with a "first-exposed" date, roll up revenue per SKU, divide the <180-day cohort by total. Rebuild the cohort each quarter. Report both RCRS and a 180-to-360-day "maturing cohort" share — the ratio of those two signals whether new capabilities are durable or faddish.

**Construct validity concerns.** (a) The indicator punishes mature AI products that derive revenue from a capability >180 days old but still growing. (b) Creative SKU-splitting can re-brand old capability as new. Mitigation: pair with a 12-month retention number on each SKU, so a "new" product built on an old capability is visibly under-retaining.

**Known gaming risks.** Releasing cosmetic variants of an existing capability with a new SKU; bundling old capability into a new-labeled package; aggressive sales comp on the tagged SKU class. Mitigation: independent product-marketing signoff on the "first-exposed" tag; audit trail from release notes.

**Industry benchmarks.**
- Cursor's trajectory ($0 → $100M ARR in 12 months; $1B → $2B ARR in 3 months, 2025-11 to 2026-02) suggests RCRS >50% sustained for 18 months during its scale-up phase ([TechCrunch 2026-03-02](https://techcrunch.com/2026/03/02/cursor-has-reportedly-surpassed-2b-in-annualized-revenue/)). This is an extreme outlier.
- Harvey: 4× ARR growth 2024, 3.9× in 2025 — on any reasonable capability-refresh cadence RCRS runs 40–70% [estimated, medium].
- ServiceNow Now Assist: >$600M ACV Q4-2025, more than doubled YoY ([earnings call]). On a ~$10B revenue base, RCRS ~6% for that specific line — typical of an incumbent's AI-new-revenue intensity [observed, high for ServiceNow; generalization low-medium].
- Menlo Ventures reports enterprise gen AI spend at $37B in 2025, up from $11.5B in 2024 ([Menlo 2025](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/)). Spend growth is not the same as *recent-capability revenue share*, but the 3.2× YoY increase indicates the market-wide supply of fresh-capability revenue opportunity.

**Reference ranges (% of revenue).**

| Org size / posture | Green (AI-native) | Green (AI-forward incumbent) | Red (stagnant) |
|---|---|---|---|
| Small | ≥ 40 | ≥ 10 | < 2 |
| Mid | ≥ 25 | ≥ 6 | < 1 |
| Large | ≥ 12 | ≥ 3 | < 0.3 |

### 2.6 Time-to-Workflow-Redesign After Capability Shock (TWR)

**Definition.** `TWR = median days from a pre-registered capability-shock event to the first production deployment of a redesigned workflow that materially changes a human task bundle`. Pre-registered shocks are a published watch-list, e.g., "a new model cuts cost of our primary inference path by ≥50%," "a new agent capability makes a currently-manual step autonomously executable to ≥90% reliability," "a major compliance rule changes." "Materially changes a task bundle" requires a documented change in the SOP, a retrained owning team, and at least 50% of the relevant workflow volume running on the new design.

**Data-source feasibility.** Requires an explicit shock watch-list maintained by a workflow-design owner (typically a CoE or a Chief AI Officer function). Feasibility **medium** — most orgs don't pre-register shocks, so TWR has to be reconstructed retrospectively. Feasibility **high** for firms with an AI Council / CAIO operating-review cadence.

**Measurement method.** Each quarter, review the watch-list for shocks that occurred; for each, record the shock timestamp and the first-deploy timestamp of the redesigned workflow (not the first *plan*, but the first *deploy with volume*); median the deltas. Report separately by shock class (model-capability, cost, agentic, regulatory) — they have different expected latencies.

**Construct validity concerns.** TWR captures a mix of detection lag, decision lag, and execution lag. Slow TWR could indicate poor sensing (no one noticed), poor decision rights (everyone noticed, no one decided), or poor execution capacity (decided, can't ship). Mitigation: pair with a breakdown of the three latencies; it is diagnostically useful to know *where* the time is going.

**Known gaming risks.** Cherry-picking shocks (only counting the ones you responded to fast); redefining "materially changes" downward; counting internal SOP update as deploy. Mitigation: pre-registered watch-list, external verification of deploy (at least 50% traffic threshold, per CDL logic).

**Industry benchmarks.**
- Klarna's customer-service workflow redesign post-GPT-4 (2023–2024): shock event (GPT-4 general availability, 2023-03) → claimed "AI assistant handling 2/3 of chats" (announced 2024-02) — ~330 days; partial reversal in 2025 implies effective sustained redesign took longer [observed on the first-deploy date, high; sustainability lower].
- Shopify's "AI-first hiring" workflow change: OpenAI o1 release (2024-09) was one trigger; internal memo and policy change dated 2025-04 — approximately 210 days for the managerial workflow redesign ([Fortune 2025-04-10](https://fortune.com/2025/04/10/shopify-ceo-ai-will-kill-jobs-other-ceos-just-wont-admit-it/)) [observed, medium].
- Harvey's workflow retooling cadence: typical cycle 30–60 days for a new capability to land in the customer product, per growth-trajectory reconstruction [estimated, medium].
- Enterprise median: Stanford AI Index 2025 / McKinsey 2025 imply a typical enterprise TWR of **6–12 months** for a significant capability shock, closer to 12–18 months for workflow redesigns touching regulated or cross-functional processes [estimated, medium].

**Reference ranges (days for a non-regulated primary workflow; regulated workflows typically 2–3× higher).**

| Org size | Green | Yellow | Red |
|---|---|---|---|
| Small | ≤ 30 | 31–90 | > 90 |
| Mid | ≤ 90 | 91–180 | > 180 |
| Large | ≤ 180 | 181–360 | > 360 |

### 2.7 Dropped candidate: adaptation-to-overcorrection ratio

The seventh candidate — "adaptation-to-overcorrection ratio (changes that were reversed within 12 months)" — was not retained as a top-level indicator, for three reasons. (i) **Too-easy gaming**: reversals can be recoded as "new initiatives" at minimal cost; the indicator moves while nothing changes. (ii) **Signal confounding**: a low ratio is *not* inherently good — it may mean the org refuses to reverse bad calls, which is itself a failure mode (Klarna went ~14 months before partially reversing its AI-replacement strategy). (iii) **Construct redundancy**: the useful signal is already captured as a sub-metric in RRF (12-month role-reversal rate) and as a pairing metric in RCRS (new-SKU 12-month retention). It is re-absorbed rather than tracked twice.

---

## 3. Dashboard specification

| # | Indicator | Unit | Target (mid-size) | Warning | Critical | Update cadence | Owner |
|---|---|---|---|---|---|---|---|
| 1 | Capability-to-Deployment Lag (CDL) | days (median) | ≤ 30 | 31–90 | > 90 | Monthly | Head of Platform / AI Infrastructure |
| 2 | Model-Switching Cost (MSC) | engineer-days per within-vendor upgrade | ≤ 10 | 11–30 | > 30 | Per migration + rolling 4-quarter median | Head of Platform |
| 3 | Role Redefinition Frequency (RRF) | AI-attributed role changes per 1,000 FTE per 12 months | 20–80 (band, not ceiling) | outside band toward 80–160 or 8–20 | >160 or <8 | Quarterly | CHRO / Chief People Officer (co-owned with CAIO if present) |
| 4 | AI-Subsystem Tech-Debt Accrual Rate (TDAR) | points-added net / capacity per quarter | ≤ 0.3 | 0.3–0.8 | > 0.8 | Quarterly | VP Engineering / AI Platform Lead |
| 5 | Recent-Capability Revenue Share (RCRS) | % of last-quarter revenue from <180-day capabilities | ≥ 6 (incumbent) / ≥ 25 (AI-native) | half of target | ≤ 1 | Quarterly | CFO + CPO joint |
| 6 | Time-to-Workflow-Redesign (TWR) | days from pre-registered shock to ≥50% deploy | ≤ 90 | 91–180 | > 180 | Per shock + rolling 4-shock median | CAIO or AI Council Chair |

Design notes:
- RRF is the only indicator whose green zone is a **band** rather than a ceiling. This is deliberate and load-bearing; see §2.3.
- TDAR warning triggers a *remediation sprint allocation rule*, not an individual performance flag — it is a system-level indicator.
- Every indicator has one owner by role, not by person; ownership follows the role even through reorgs (which is relevant given RRF).
- Three indicators (CDL, MSC, TWR) are latency indicators; three (RRF, TDAR, RCRS) are stock/flow indicators. A healthy dashboard shows movement on both families; movement on only latency indicators while stock/flow indicators stagnate is a red flag for "motion without adaptation."

---

## 4. Composite adaptability score (optional)

A single composite is offered with heavy caveats: **the value of these indicators is in reading them jointly, not in collapsing them.** That said, for executive-summary purposes, the following weighting is defensible:

```
ADAPT = 0.20 * score(CDL)
      + 0.15 * score(MSC)
      + 0.15 * score(RRF)
      + 0.20 * score(TDAR)
      + 0.15 * score(RCRS)
      + 0.15 * score(TWR)
```

where `score(X)` is a 0-100 mapping with 100 at the green threshold, 50 at the yellow/red boundary, 0 at 2× the red threshold, clipped.

Caveats, which should always travel with the composite:
- **Over-compression risk.** The composite will mask the "motion without adaptation" pathology (latency indicators green, stock/flow indicators red averages to "fine").
- **Weighting fragility.** The weights above are ordinal (roughly equal) not defended empirically — no public dataset exists to fit them against a business outcome.
- **Goodhart risk.** Once the composite is an OKR target, sub-indicators will be gamed to the composite rather than to adaptability ([Goodhart's law literature applied to AI metrics, 2025](https://jellyfish.co/blog/goodharts-law-in-software-engineering-and-how-to-avoid-gaming-your-metrics/)).
- **Scale-tier sensitivity.** Weights should be re-tuned by scale tier; small firms rely more on CDL+RCRS, large firms more on TDAR+RRF.

Recommendation: publish the six-indicator board; *discourage* the composite for internal management review; allow the composite only for external disclosure or cross-org benchmarking where a single number is unavoidable.

---

## 5. Benchmark table — published cases 2023–2026

Values labelled `obs` are directly observable from the cited source. `est` are estimated from adjacent public data. `—` means not estimable from public sources.

| Case | Period | CDL (days) | MSC (eng-days) | RRF (per 1k FTE) | TDAR | RCRS (%) | TWR (days) |
|---|---|---|---|---|---|---|---|
| Cursor | 2023–2026 | ~1 (obs, high) | ~2 (est, medium) | — | — | ~60 (est, medium) | ~7 (est, medium) |
| Harvey | 2023–2026 | ~30 (est, medium) | ~10 (est, medium) | — | — | ~50 (est, medium) | ~45 (est, medium) |
| Sierra | 2024–2026 | ~14 (est, medium) | ~5 (est, low) | — | — | ~70 (est, medium) | ~30 (est, medium) |
| Klarna | 2023–2025 | ~45 (est, medium) | — | ~380 in 2024, reversed ~70 in 2025 (obs, high) | — | — | ~330 initial, reversal later (obs, high) |
| Shopify | 2024–2025 | ~60 (est, medium) | — | ~40 est, with hiring-freeze mechanism (obs, high) | — | ~3 (est, low) | ~210 (obs, medium) |
| Amazon | 2024–2025 | ~120 (est, medium) | — | ~40–85 in 2025, cut wave (obs, high) | — | — | — |
| Duolingo | 2023–2025 | ~90 (est, medium) | — | ~20 (est, medium) | — | ~4 (est, low) | ~120 (est, medium) |
| Anthropic-as-customer of itself | 2024–2026 | ~1 (obs, high) | ~1 (est, high) | — | — | — | — |
| McKinsey / BCG (consulting incumbents) | 2023–2026 | ~180 (est, low) | — | ~30 (est, low) | — | ~5 (est, low) | ~270 (est, low) |
| ServiceNow | 2024–2025 | ~90 (est, medium) | — | — | — | ~6 (obs, medium; Now Assist ACV) | — |
| Fortune-500 median | 2024–2026 | ~180 (est, medium; from [Stanford AI Index 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report)) | ~30 (est, medium; from Vertesia / DORA) | ~15 (est, low) | ~0.6 (est, low) | ~2 (est, low) | ~330 (est, medium) |

Observations from the table:
- **Strongest benchmark coverage** is on RRF and TWR — high-confidence observations are public for Klarna, Amazon, Shopify, and Duolingo from mainstream business press and CEO memos.
- **Weakest benchmark coverage** is on TDAR — no public case study gives a usable numerator and denominator. Every number in the TDAR column is left blank, which is the honest state of the literature as of 2026-04-22.
- **Cursor is a meaningful outlier** across CDL, MSC, and RCRS — an AI-native firm built around rapid model-turnover absorption. It is arguably the best living proof-of-concept that the six indicators *can* all be green simultaneously, at least at small scale and for ~30 months.

---

## 6. Validation plan

The dashboard should be piloted as follows before being promoted to management-review status.

**Pilot duration.** Two quarters (≈180 days). This is long enough to see one or two capability shocks on 2023–2026 cadence, short enough to avoid ossifying a draft instrument.

**Pilot org profile.** Target one small (<250 FTE), one mid (250–5,000 FTE), one large (>5,000 FTE). Ideally, at least one pilot participant is in a regulated domain (financial services or healthcare) so the regulated-workflow TWR multiplier can be calibrated rather than assumed.

**Instrumentation checklist.**
1. CDL — gateway logs tagged with model version + per-release first-traffic marker.
2. MSC — a migration-project Jira label + a post-migration retrospective form.
3. RRF — HRIS role-change workflow amended with an "AI attribution" field and a 12-month-reversal check.
4. TDAR — debt label discipline in AI-subsystem components, incorporating the three LLM-specific SATD categories.
5. RCRS — revenue tagging at SKU / feature-flag level with "first-exposed" date.
6. TWR — a pre-registered capability-shock watch-list and a per-shock timestamp log.

**Gates and exit criteria.**
- Month 1: indicators instrumented, baseline numbers recorded.
- Month 3: first quarterly review; reference ranges re-checked against pilot data; indicator weights (if composite is being tested) adjusted.
- Month 6: management-review adoption decision; dashboard either promoted, iterated, or retired.

**Failure modes to watch.**
- "Dashboard theater" — the dashboard is populated but decisions don't change. Mitigation: require two decisions per quarter to cite a dashboard indicator in the meeting notes, or the dashboard is downgraded.
- "Metric flight to the measurable" — TDAR (hardest to measure) gets dropped, CDL (easiest) gets over-weighted. Mitigation: none of the six indicators may be removed during the pilot; only the composite weighting is adjustable.
- "Regulated-domain mis-specification" — healthcare / financial-services pilots fail the TWR green threshold by a factor of 3 and are marked "red" despite acting appropriately. Mitigation: regulated-domain TWR has a separate scale; do not fit healthcare to the generic bands.

---

## 7. Open questions and negative evidence

Open questions:
- Does the RRF band hold across non-US labour markets? EU and Japan exhibit lower baseline role churn; the band may need downshifting to (10–40, 40–80, …) for mid-sized orgs in those markets.
- Is TDAR the right normalization? Capacity is endogenous (orgs under-investing in AI capacity will always look good on TDAR). An alternative — `TDAR' = debt growth / AI-subsystem revenue` — might be more robust but is harder to source.
- Does CDL meaningfully measure adaptability above a floor (say ≤7 days)? Below that floor, CDL differences mostly reflect gateway architecture, not adaptability posture.
- Is there a cross-tier interaction — do S2/S3 firms that hit green on all six indicators convert to S4/S5 faster than peers? Testing this requires a longitudinal dataset that does not yet exist.

Negative evidence (looked for, not found):
- No public benchmark gives a per-org engineer-day migration-cost figure broken down by route and by cross-vendor vs. within-vendor. This is sensitive and competitively signalling, which is why it stays private.
- No public data exists on TDAR at a usable granularity. Academic studies on LLM-induced SATD (arXiv 2601.06266, 2601.07786) point at the qualitative shape but do not give organization-level rates.
- No published study links any of these six indicators to downstream financial outcomes (revenue growth, margin, market share) with the rigor needed to ground the composite weights. This is the biggest gap.
- CDL data for regulated industries (healthcare, finance, legal) is consistently missing from the press-cycle cases; the available figures over-represent consumer-software and product-led firms.

---

## 8. Feedback to the three-pillar adaptability frame

- **Indicators partition cleanly onto the three pillars.** CDL and MSC are Pillar 1 (AI usage) measurements. RRF is a Pillar 2 (organization) measurement. TDAR is a Pillar 3 (technical infrastructure) measurement. RCRS and TWR are cross-pillar — they require all three pillars to have moved coherently before they can register as green. The frame survives the measurement-design exercise: the three pillars are separable at the indicator level, and their coupling is visible at the cross-pillar indicators.
- **The "motion without adaptation" pathology is detectable in the dashboard.** An org with green CDL (fast deploys), green MSC (fast swaps), red RRF (no role change), red TDAR (debt piling up), and red TWR (no workflow redesign) is doing tool adoption without organizational or infrastructural follow-through. This is the most common failure mode in the McKinsey "78% adoption, 1% mature" gap. The dashboard surfaces it explicitly.
- **Scale tier is first-class, not a footnote.** Reference ranges differ by scale tier because adaptability mechanisms differ — small firms adapt by speed and tool choice (CDL, RCRS), large firms adapt by capital and coordination (TDAR, RRF). The scale-based track's claim that adaptability mechanisms are tier-specific is supported by the indicator design.
- **Regulated-domain handling is not optional.** Five of the six indicators need a regulated-domain multiplier, and TWR needs a separate scale. The healthcare-bio-ai track and the adaptability dashboard should share a single "regulated-domain adjustment" specification; maintaining two copies will cause drift.
- **The indicators are diagnostic, not prescriptive.** Where an indicator goes red, the dashboard signals *where* to look but does not tell you *what* to do. The three-pillar frame, the M1 system-dynamics map, and the track-level domain memos (A1, A2, O2, T1, T3) are required to convert diagnosis to action. The dashboard is the thermometer, not the medicine.
- **Reversal is a first-class signal.** The design choice to embed reversal tracking inside RRF and RCRS rather than as its own indicator rebalances the frame away from "change velocity" and toward "change durability." A firm that moves fast and reverses less is not merely faster than one that moves fast and reverses often; the adaptability-as-meta-capability claim depends on durability being measurable. These six indicators make it so.
