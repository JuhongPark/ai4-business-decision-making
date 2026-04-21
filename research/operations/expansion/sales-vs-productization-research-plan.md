# Sales-vs-Productization Decomposition — Extended Research Plan

status: research_plan
date: 2026-04-21
parent_memo: [`research/extensions/scale-based/sales-vs-productization-decomposition.md`](../../extensions/scale-based/sales-vs-productization-decomposition.md)
parent_track: [`research/extensions/scale-based/`](../../extensions/scale-based/)

---

## 1. Why this plan exists

The `sales-vs-productization-decomposition.md` memo (2026-04-21) decomposed the scale-based track's three-axis tradeoff (speed, resources, verification quality) into two firm-level skills and produced five hypotheses. The memo's evidence base is primarily Wave 3 external literature plus tier-report cross-references. It has named gaps.

This plan identifies those gaps, prioritises six research streams to close them, and specifies the deliverables each stream should produce. The aim is a Wave 4 expansion of the scale-based track that strengthens the decomposition memo from an interpretive layer into a publishable analytical claim.

The plan is deliberately extensive. The scale-based research plan (§4–§5 in `scale-based-reasoning-trust-research-plan.md`) set a precedent for multi-stream Wave-scale investigation. This plan applies the same discipline to the decomposition extension.

---

## 2. Gaps in the current memo

The memo produced in April 2026 has ten identifiable weaknesses, ranked by how strongly each blocks a publishable claim.

### Priority 1 gaps

1. **No empirical distribution across the 2×2 quadrants.** The matrix in §4 names four cells and populates each with case anchors, but offers no estimate of the population share per cell. Without this, the PwC 20%-capture hypothesis (H1) cannot be tested and the "modal firm is lower-right" claim is not quantified.

2. **No Korean / Asian evidence.** The project owner is Korean, the S7 tier report cites Korea AI Basic Act, and the Singapore AI Verify case is a load-bearing S6 exemplar. Yet the decomposition memo's cases are overwhelmingly US (Microsoft, Anthropic, OpenAI, Harvey, Klarna, Humane, etc.) with occasional European references (Cohere, Mistral, UK ATRS). Naver/Kakao/Samsung/LG/SK AI initiatives, Japanese AI startups (Preferred Networks, Sakana AI), Chinese AI deployment patterns are absent. This is a major scope hole.

3. **71-incident dataset not recoded.** The project's anchor evidence base is the 71-incident inventory in `research/extensions/business-alignment/incidents/incident-inventory.md`. The decomposition memo cites a subset of incidents (Nate Inc., Character.AI, Humane, Klarna) but does not systematically recode the full 71 against the two-skill matrix. Doing so would either strengthen the decomposition or reveal incidents that do not fit and need a different analytic frame.

### Priority 2 gaps

4. **Eval engineering as a discipline is underdeveloped.** The memo names LangSmith, Arize, Galileo, Patronus, and the Apple "AI Evaluation Engineer" job title but does not examine the emerging profession systematically. If eval engineering is a bounded productization sub-skill, its labour-market signal (job postings, salary, geography) is one of the most concrete tests of the decomposition.

5. **Regulatory regime × skill interaction is qualitative only.** The memo mentions EU AI Act, FDA CDS, SR 11-7, and Singapore AI Verify, but does not develop the asymmetric effect regulation has on sales skill (compliance-as-sales-instrument creation) vs productization skill (verification infrastructure mandates). A comparative regulatory analysis would make the hypothesis on governance theater (H2) more testable.

6. **Vertical AI / service-as-software thesis is present but thin.** The Menlo "Great Re-Aggregation" thesis, Gil Pignol's vertical-AI-service-as-software framing, and the vertical-AI-TAM projection ($5.1B → $47.1B) are cited once. The decomposition predicts that vertical AI will bifurcate by productization depth (orchestration-only wrappers vs. trained vertical models). This prediction needs to be developed and tested.

### Priority 3 gaps

7. **Pricing-model × verification-affordance linkage is not developed.** The memo notes Salesforce's seat-based reversal and the rise of hybrid pricing but does not link pricing model choice to the decomposition. An outcome-based pricing model implicitly requires productization-grade measurement of outcomes, which is a verification-substance requirement. This is a testable claim the memo does not yet make.

8. **Longitudinal movement across quadrants is not characterised.** The memo is a static snapshot. In practice firms move between quadrants over time — a strong-productization startup may weaken when it scales; a sales-heavy wrapper may acquire productization skill through hires. The movement patterns are unknown and would be highly informative if measured.

9. **Insurance and liability market pricing is absent.** The scale-based track cited Verisk's Jan 2026 AI exclusion for malpractice, AI liability insurance projected at $29.7B by 2033, and related coverage. The decomposition predicts that insurance markets price sales-skill instruments (certifications, disclosures) but not productization substance. D&O and cyber insurance pricing data would test this.

10. **Solo-founder productization ceiling is not bounded.** The memo cites Base44 ($80M exit), Cursor, Bolt, Midjourney, Gumloop as existence proofs but does not identify the productization ceiling below which a solo founder cannot cross. Where does Cursor/Claude Code stop being enough?

---

## 3. Research streams

Six streams address the ten gaps. Each stream has a distinct method, output, and acceptance criterion.

### Stream A — Korean and Asian market decomposition evidence

**Purpose**: Close gap 2 (Korean / Asian evidence). Produce a compact sibling memo that populates the 2×2 matrix with Asia-region cases and evaluates whether the hypotheses hold in a different market structure.

**Method**: External literature synthesis (WebSearch, Korean-language sources translated as needed) plus 2024-2026 Korean AI enterprise filings (DART, Samsung / Naver / Kakao / SK Group / LG / Hyundai AI disclosures), Korea Fair Trade Commission AI-related actions, Japanese AI M&A (SoftBank / Mitsubishi patterns), Chinese AI deployment reports (WAIC, Cyberspace Administration), Singapore AI Verify ecosystem data.

**Acceptance criterion**: At least 15 Asian firm cases coded against the 2×2 matrix; explicit test of whether Korean large-cap AI (Samsung, Naver, Kakao) follows the Microsoft/Salesforce incumbent pattern or a different pattern; identification of at least three Asian-origin cases that strengthen or contradict the memo's hypotheses.

**Deliverable**: `research/extensions/scale-based/asia-market-decomposition-appendix.md` (target 10-15KB).

### Stream B — 71-incident dataset recoding

**Purpose**: Close gap 3 (dataset not recoded). Use the project's anchor evidence base to test whether the decomposition is consistent with the 71-incident distribution.

**Method**: Read `research/extensions/business-alignment/incidents/incident-inventory.md` (the full 71-case inventory) and `alignment-failure-mapping.md`. Code each incident with four labels: (1) sales-skill strength at the firm at time of incident (L/M/H), (2) productization-skill strength (L/M/H), (3) quadrant classification (both strong, sales ahead, product ahead, both weak, or unclassifiable), (4) dominant failure locus (sales narrative, productization substance, both, neither). Cross-tabulate against the existing Amodei / Weidinger classifications.

**Acceptance criterion**: 71 of 71 incidents assigned to quadrants or explicitly marked "unclassifiable" with a reason. Distribution table produced. Surprises and outliers documented.

**Deliverable**: `research/extensions/scale-based/incident-decomposition-recoding.md` (target 15-20KB including the full coding table).

### Stream C — Eval engineering profession data

**Purpose**: Close gap 4 (eval engineering underdeveloped). Treat eval engineering as a labour-market signal of productization-skill formalisation.

**Method**: Systematic review of 2025-2026 job postings from Anthropic, OpenAI, Meta, Google, Microsoft, Apple, Cohere, Mistral, Scale AI, Harvey, Sierra, Decagon, Cursor, Perplexity for titles containing "eval," "evaluation," "red team," "alignment," "safety," "reliability," "model risk." Cross-reference with public salary data (Levels.fyi, Glassdoor, H1B records). Survey 2025-2026 arxiv + industry-blog coverage of eval engineering emergence. Check Korean AI firm job postings for similar roles.

**Acceptance criterion**: At least 100 job postings surveyed; salary/headcount gradient estimated across frontier-lab vs product-layer vs non-AI-native firms; concrete evidence that the discipline is crystallising (or not).

**Deliverable**: `research/extensions/scale-based/eval-engineering-profession-appendix.md` (target 10-12KB).

### Stream D — Regulatory regime × skill interaction

**Purpose**: Close gap 5 (regulation is qualitative). Produce a comparative analysis of how each major regulatory regime asymmetrically affects sales skill vs productization skill.

**Method**: Compare EU AI Act (high-risk classification, FRIA, GPAI Code of Practice), US sectoral (FDA CDS guidance, SR 11-7, SEC AI-disclosure enforcement, FTC Operation AI Comply), Korea AI Basic Act, UK ATRS + AISI, Japan AI Guidelines, Singapore AI Verify, China Generative AI Measures. For each regime, identify (1) the compliance artifacts it creates that sales skill produces (filings, disclosures, certifications), (2) the verification infrastructure it mandates that productization skill produces (testing, red-teaming, monitoring), (3) the sanctioning gradient and who absorbs cost.

**Acceptance criterion**: 7 regulatory regimes compared in a table; asymmetric-effect hypothesis tested; at least one surprise identified (regime that uniquely forces productization substance or uniquely rewards sales theatre).

**Deliverable**: `research/extensions/scale-based/regulatory-regime-skill-asymmetry-appendix.md` (target 12-15KB).

### Stream E — Vertical AI and service-as-software depth

**Purpose**: Close gap 6 (vertical AI thin). Develop the prediction that vertical AI will bifurcate by productization depth.

**Method**: Deep-dive on 10-15 named vertical-AI firms (Harvey, Sierra, Decagon, Cursor, Perplexity, Glean, Cresta, Replit, Abridge, Atropos Health, Tennr, EvenUp, Eve, Spellbook, Paxton). For each, classify sales motion (PLG / enterprise / channel / hybrid), productization depth (prompt-only / RAG-heavy / fine-tuning / training), ARR trajectory, and whether they publish eval numbers. Test whether firms that publish eval numbers concentrate in one quadrant.

**Acceptance criterion**: 12+ firms classified; productization-depth × sales-motion cross-tab; clear articulation of whether "vertical AI as service-as-software" favours strong productization, strong sales, or both.

**Deliverable**: `research/extensions/scale-based/vertical-ai-depth-appendix.md` (target 12-15KB).

### Stream F — Quantitative quadrant distribution

**Purpose**: Close gap 1 (no empirical distribution). Use available public data to estimate the population share in each of the four quadrants for the AI company universe.

**Method**: Combine (a) Crunchbase / PitchBook summary statistics on AI-labeled startups by funding stage, (b) Stanford HAI Index 2025 data on AI adoption by firm size and sector, (c) Menlo Ventures enterprise spend distribution, (d) MIT State of AI 2025 on pilot success/failure, (e) PwC 2026 top-20% finding, (f) Stack Overflow 2025 developer survey data on AI tool usage by firm size. Produce a best-estimate distribution with wide uncertainty bands, honest about the indirectness of the estimate.

**Acceptance criterion**: Distribution estimate with explicit uncertainty; test of H1 (PwC 20% = both skills); identification of which cells the data cannot reach (e.g., sales-weak / productization-strong is hard to observe because these firms are pre-commercial).

**Deliverable**: A quantitative section added to the main decomposition memo (`sales-vs-productization-decomposition.md` §10.3 or as a new §14). No separate appendix; the finding should be near the hypothesis it tests.

---

## 4. Stream dependency graph

Streams A, B, C, D, E, F are independent in data collection but share synthesis dependencies:

```
Stream A (Asia) ─┐
Stream B (71-incident recoding) ─┤
Stream C (eval engineering) ─────┼──> Memo update (§ to be inserted)
Stream D (regulatory) ───────────┤
Stream E (vertical AI) ──────────┤
Stream F (quadrant distribution) ┘
```

All six streams feed the memo update and a decision about whether any stream's findings warrant a standalone sibling memo vs an appendix section.

---

## 5. Execution order for this cycle

The user-requested cycle is "research, organise, verify, update, commit." The execution order is:

1. **Run all six streams in parallel.** Streams A-F are independent and can run as parallel Agent tasks. They produce working outputs in independent files.

2. **Synthesise across streams.** Identify which streams strengthen the memo's hypotheses, which weaken them, and which surface genuinely new findings.

3. **Verify memo consistency.** Update the main memo with a new section (§14 or equivalent) summarising cross-stream findings. Add forward-references in §8 (hypotheses) to the streams that tested them. Keep the original hypotheses as written — do not retroactively change the April 21 memo; add the updates as additions.

4. **Update cross-references.** If any stream produces a standalone appendix, add it to `scale-based/README.md` recommended reading list and to the `size-speed-resource-tradeoff.md` / `cross-tier-synthesis.md` sibling-reference notes.

5. **Run language policy check.** All outputs must be in English per the repository policy.

6. **Commit in logical slices.** One commit for the research plan document. One commit for each stream appendix. One commit for the main memo update. One final synthesis commit that closes the cycle.

---

## 6. Evidence grading and honest limitations

This plan inherits the scale-based track's evidence grading (A primary, B practitioner/secondary, C inferred, D speculative). The expected evidence mix per stream:

| Stream | Expected grade distribution | Why |
|---|---|---|
| A (Asia) | B/C majority | Korean / Japanese primary sources exist but are not always translated; Chinese regulatory filings are partial |
| B (71-incident recoding) | A/B majority | The underlying inventory is already A-graded; coding introduces some C where the firm's skill balance at time of incident is not documented |
| C (eval engineering) | B majority | Job postings are primary but transient; salary data is B at best |
| D (regulatory) | A majority | Regulatory texts are primary |
| E (vertical AI) | B majority | Private-company data is practitioner-level |
| F (quadrant distribution) | C/D majority | The underlying data is not collected for this purpose; any distribution estimate is indirect |

The plan expects the memo update to contain at least one D-graded claim where the data does not permit a stronger statement. This is a feature, not a bug — the scale-based track has established a practice of flagging speculative claims explicitly rather than silently upgrading them.

---

## 7. What this plan deliberately does not include

- **Primary interviews or surveys.** Out of scope for this cycle. The scale-based Wave 4 plan already names the S1 diary study, FICS-1 corpus expansion, S3 survey, and S7 institutional access as future primary work; decomposition-specific interviews would be an additional Wave.
- **Longitudinal tracking of individual firms.** Gap 8 is acknowledged but not addressed in this plan. A longitudinal study would need 2-3 years of observation and a different methodology.
- **Building new empirical datasets.** The plan uses existing public data and existing repository evidence only.
- **Insurance market pricing analysis (Gap 9) and solo-founder productization ceiling (Gap 10).** These are flagged as Priority 3 and deferred — their evidence base is likely to require primary data collection beyond this cycle's scope.

---

## 8. Success criteria

The expanded cycle succeeds if:

1. The main memo has a new summary section that cites primary data from at least four of the six streams.
2. At least one hypothesis (H1-H5) is meaningfully strengthened or weakened by cross-stream evidence.
3. At least one stream surfaces a finding that does *not* fit the decomposition — the memo explicitly acknowledges it.
4. The asia-market, regulatory, and vertical-ai appendices are independently useful as related-work material for the three paper candidates.
5. The language-policy check passes without manual cleanup.

Failure modes to avoid:

- **Confirmation bias**: every stream "confirms" the decomposition. If that happens, the streams have been under-challenged.
- **Overclaim**: the memo update promotes C/D-graded claims to confident assertions.
- **Scope drift**: the streams turn into unrelated tier-report expansions. Each stream must end by updating the main memo.

---

## 9. Cross-references

- [`research/extensions/scale-based/sales-vs-productization-decomposition.md`](../../extensions/scale-based/sales-vs-productization-decomposition.md) — the memo this plan expands
- [`research/extensions/scale-based/size-speed-resource-tradeoff.md`](../../extensions/scale-based/size-speed-resource-tradeoff.md) — the parent memo on the three-axis framing
- [`research/extensions/scale-based/cross-tier-synthesis.md`](../../extensions/scale-based/cross-tier-synthesis.md) — the three load-bearing findings the decomposition reinterprets
- [`research/extensions/business-alignment/incidents/incident-inventory.md`](../../extensions/business-alignment/incidents/incident-inventory.md) — the 71-incident base for Stream B
- [`research/operations/expansion/scale-based-reasoning-trust-research-plan.md`](scale-based-reasoning-trust-research-plan.md) — the precedent for multi-stream Wave planning
