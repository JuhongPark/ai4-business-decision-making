# Eval Engineering as an Emerging Productization Sub-Skill

status: research_complete
date: 2026-04-21
purpose: Stream C deliverable of the sales-vs-productization research plan. Tests whether "eval engineering" is crystallising as a distinct labour-market-visible profession in 2025-2026 and, if so, what its emergence tells us about the decomposition's claim that productization skill is separable from sales skill.
parent_memo: [`sales-vs-productization-decomposition.md`](sales-vs-productization-decomposition.md)
research_plan: [`../../operations/expansion/sales-vs-productization-research-plan.md`](../../operations/expansion/sales-vs-productization-research-plan.md)

---

## 1. Bottom line

Eval engineering is crystallising as a profession, but unevenly. In 2025-2026 it has acquired the three markers of a named profession — dedicated titles at major firms, a distinct tooling market of $100M+ funded venture-backed pure-plays, and a shared curriculum with named teachers and a forthcoming O'Reilly textbook. It has not yet acquired stable title standardisation, salary comparability across firms, or a certification regime matched to the underlying engineering content.

This is the most concrete available evidence that productization skill is decomposable into nameable sub-skills with their own labour markets. A skill that generates a dedicated Maven course, a dedicated O'Reilly textbook, 50+ students per frontier firm, and $100M+ of category venture capital is not an abstract analytical construct; it is a job.

---

## 2. Marker 1 — Dedicated job titles at frontier labs and major firms

**Anthropic** has an explicit "Research Engineer, Model Evaluations" Greenhouse listing whose mandate is "leading the design and architecture of Anthropic's evaluation platform, implementing high-throughput evaluation pipelines for production training." Separately, Anthropic runs the Frontier Red Team with four distinct sub-titles: Research Engineer FRT (Autonomy), Research Scientist FRT (Cyber), Research Scientist FRT (Emerging Risks), and Red Team Engineer, Safeguards. Anthropic has grown from ~1,100 (mid-2025) to ~4,585-4,954 (Feb-Mar 2026), with Frontier Red Team and Safeguards both aggressively hiring.

**OpenAI** has an explicit "Research Engineer, Frontier Evals and Environments" posting (San Francisco) — a named team whose charter is building "model environments to measure and steer models." OpenAI is targeting 8,000 FTE by end-2026, up from ~4,500 early-2026.

**Apple** lists "AI Evaluation Engineer, Siri Core Modeling" (Nov 3, 2025 posting) plus four separate Siri-specific quality-engineering roles: ML Engineer Siri AI Quality Engineering; Software Engineer Siri AI Quality Engineering; Senior Software Engineer Siri AI Data and Privacy Quality Engineering; Lead Software Engineer in Test, Siri AI Quality Engineering. This is the thickest public evidence of a sub-discipline: Apple treats Siri evaluation as an entire engineering sub-organisation.

**Meta** hires "Research Engineer, Language - Generative AI" with evaluation named as a distinct skill requirement and runs the GenAI Trust and Safety red team (Ivan Evtimov as tech lead for Llama 3 / Code Llama red team; Aaron Grattafiori as AI Red Teaming lead).

**Google DeepMind** has roughly 87 active postings in April 2026 across Mountain View, London, and Zurich including specific alignment/safety engineering roles.

**Harvey AI** has "Software Engineer, AI Platform" with a named Evaluation Infrastructure sub-mandate: "the shared eval tooling and frameworks that let every team across Harvey measure and improve AI quality systematically."

### Title variance is itself evidence of youth

"AI Evaluation Engineer" (Apple), "Research Engineer, Model Evaluations" (Anthropic), "Research Engineer, Frontier Evals and Environments" (OpenAI), "Red Team Engineer, Safeguards" (Anthropic), "Software Engineer, AI Platform (Evaluation Infrastructure)" (Harvey), "Machine Learning Engineer, Siri AI Quality Engineering" (Apple) are all the same craft under different titles. The title dispersion is evidence that the discipline is young; the craft convergence across firms, visible in the shared curriculum and shared tooling stack, is evidence that it *is* a discipline.

---

## 3. Marker 2 — A distinct commercial tooling market

| Firm | Latest funding | Total raised | Employees | Revenue / ARR |
|---|---|---|---|---|
| LangChain / LangSmith | $100M Series B mid-2025 at $1.1B valuation | — | — | $12-16M ARR (est.) |
| Arize AI | $70M Series C (Feb 2025) | $131M | 135 | $5-25M (est.) |
| Galileo | $45M Series B | $68.1M | 153 (Feb 2026) | +834% since early 2024 |
| Braintrust | $80M Series B at $800M valuation (Feb 2026) | — | — | — |
| Patronus AI | $17M Series A (May 2024) | $40.1M | 34 | — |
| Langfuse | acquired by ClickHouse (Jan 2026) as part of $400M Series D | — | — | — |
| Humanloop | sunsetting Sep 2025 | — | — | Failed |
| Scale AI SEAL / Scale Labs | Scale Labs launched Mar 2026 as expanded SEAL; 15 new benchmarks + 450 evals across 50+ models in 2025 | — | — | — |

LangChain reports that **89% of organisations surveyed have implemented some form of agent observability** and **52% have built out evals**; among teams with agents in production, 94% have observability and 71.5% have full tracing. This is the cleanest single indicator that eval engineering has moved from niche to standard practice.

Gartner forecasts LLM observability investment will grow from 15% of GenAI deployments today to **50% by 2028**. Overall observability market: $14.2B by 2028 (Gartner); AI-specific observability: $10.7B by 2033 at 22.5% CAGR.

---

## 4. Marker 3 — A shared curriculum with named teachers and a textbook

- **Hamel Husain + Shreya Shankar Maven course "AI Evals For Engineers and PMs"** — 4,500+ students from 500+ companies (50+ each from Google, Microsoft, OpenAI, Meta, Amazon); course-reader mailing list exceeds 25,000.
- **Shreya Shankar's companion textbook** (O'Reilly, Spring 2026) — the first commercial textbook dedicated to LLM evaluation engineering as a craft.
- **Chip Huyen, *AI Engineering* (O'Reilly, 2025)** — dedicates a major chapter to evaluation including LLM-as-judge; "most read book on O'Reilly since release."
- **NeurIPS 2025 dedicated LLM-Eval workshop** — "Evaluating the Evolving LLM Lifecycle: Benchmarks, Emergent Abilities, and Scaling." Parallel ICML/ACL eval workshops continue.
- **Open-source eval frameworks dominant**: lm-evaluation-harness (EleutherAI, 5,000+ citations); HELM (Stanford); LMSYS Chatbot Arena / LMArena; Anthropic Bloom (Dec 2025) and Petri (Oct 2025, Petri 2.0 2026) — Petri built on UK AISI Inspect framework, demonstrating explicit government-lab-to-private-lab tooling portability.
- **A named essay genre**: Arjun Balaji's widely shared formulation "2023: prompt engineering / 2024: context engineering / 2025: tool use, memory, evals / 2026: grug delete waste token." "The Death of Prompt Engineering, And How Evals Are Rising in Its Place" (Medium, March 2026) explicitly frames the professional succession.

---

## 5. Title × firm × count × salary × location

| Firm | Titles observed | Approx. count | Compensation band | Location |
|---|---|---|---|---|
| Anthropic | Research Engineer Model Evaluations; Research Engineer FRT (Autonomy); Research Scientist FRT (Cyber); Research Scientist FRT (Emerging Risks); Red Team Engineer Safeguards; ML Systems Engineer Safeguards | ~15-30+ across FRT + Evaluations teams | ML Systems Engineer Safeguards base $315-340K; Research Engineer up to $690K TC; median Research Scientist $746K; max $1.05M | SF primary; NYC, Seattle; London (some) |
| OpenAI | Research Engineer Frontier Evals and Environments; Research Engineer Applied AI Engineering; safety-track roles | ~10-20 est. | SWE L2-L6: $249K-$1.24M; median $630K; Research Scientist median $1.56M | SF primary |
| Apple | AI Evaluation Engineer Siri Core Modeling; ML Engineer Siri AI QE; SWE Siri AI QE; Senior SWE Siri AI Data and Privacy QE; Lead SWE in Test Siri AI QE | ~5+ distinct active Siri-side postings | Not disclosed publicly | Cupertino; Seattle |
| Google DeepMind | Research Engineer (evaluation-adjacent); alignment/policy roles; safety engineers | 87 total DeepMind active postings Apr 2026; safety subset ~10+ | Not specifically tracked | Mountain View, London, Zurich |
| Meta AI / GenAI T&S | Research Engineer Language GenAI; Red Teaming Research Scientist; AI Red Team lead | Team known from Llama 3/4 red team disclosures; ~10+ | Mid-level $130-150K base; TC at top tier $350K+ | Menlo Park; NYC |
| Microsoft | AETHER review roles; Responsible AI roles; Azure AI eval engineers | Not concentrated in one title | — | Redmond primary |
| Harvey AI | SWE AI Platform (Evaluation Infrastructure) | Multiple postings Mar 2026 | Not public | SF, NYC |
| Scale AI / Scale Labs | SEAL researchers/engineers; benchmark engineers | Team scaled through 2025 despite company 14% RIF; 450 evals across 50+ models | — | SF |
| Patronus / Arize / Galileo | Full headcount is evaluation-adjacent | 34 / 135 / 153 | — | SF, NYC |
| JPMorgan | Model Risk Governance Associates; ML Center of Excellence (200+) | MLCOE 200+; MRG subset | Not publicly itemised | NYC, London |

**Salary observations**: Eval-engineer-adjacent roles at frontier labs are not discounted relative to generic Research / ML Engineer — $315K minimum for Safeguards ML Systems Engineer and up to $690K for Research Engineer at Anthropic suggests the market prices evaluation work at par with frontier research engineering.

---

## 6. Geographic distribution

- **Bay Area**: Anthropic, OpenAI, Scale AI, Harvey, Patronus, Arize, Galileo, Braintrust, LangChain, Decagon all primary. SF is the dominant city.
- **NYC**: Anthropic, Harvey, JPMorgan MRG, Decagon.
- **Seattle**: Anthropic, Apple.
- **Cupertino**: Apple's AI Evaluation Engineer Siri Core Modeling role is Cupertino-based.
- **London**: Google DeepMind; JPMorgan; Anthropic. UK AISI supplies the public-sector evaluation-engineering base whose tooling (Inspect framework) Anthropic's Petri builds on.
- **Zurich**: Google DeepMind; Anthropic Zurich indirectly visible.
- **Singapore**: AI Verify Foundation is a government-sponsored eval-engineering hub; Singapore AISI partners with Korea AISI on multi-turn agent evaluation testing (January 2026 joint test).
- **Seoul**: Korea AISI partnered with Scale AI in October 2025. National AI Research Lab (NAIRL) had 39 papers/4 spotlights at NeurIPS 2025. KAIST will launch a standalone College of AI in 2026 with a dedicated department for AI ethics, policy, and governance.

---

## 7. Korean and Asian signals (cross-check with Stream A)

- No public Korean job postings surfaced under exact titles "AI Evaluation Engineer" or equivalent at Samsung, Naver, Kakao, LG AI Research, Upstage, Rebellions, or FuriosaAI as of April 2026.
- LG AI Research is active in the global benchmark space but treats eval as a research-scientist function rather than an engineering sub-organisation.
- Naver and Kakao are focused on agentic product launches (Naver AI shopping agent Q1 2026; AI national secretary with the Ministry of the Interior and Safety March 2026), which creates agentic-eval demand but no public structural evidence of a named eval engineering team.
- Korea AISI was launched as the evaluation-engineering public good and is the only major Korean entity with a public "AI safety assessment" mandate. Its partnership with Scale AI (Oct 2025) and joint multi-turn agent test with Singapore AISI (Jan 2026) are the strongest signals.
- Academic base: KAIST, SNU, Yonsei, POSTECH all contributed to the ACL 2025 "triple threat" alliance with Stanford + AWS + University of Michigan on LLM red teaming, representation-level alignment, and agentic-system defense. REPBEND (latent-space alignment) was the headline technical contribution.

**Read**: Korean eval engineering is emerging via the state (Korea AISI) and the academy (SNU/KAIST/Yonsei/POSTECH) rather than via firm job postings. The profession there is closer to Stream D's regulatory-driven model than to the Bay Area labour-market model. **The productization skill can crystallise either through labour market or through regulatory compulsion, depending on the jurisdiction** — a significant data point for the decomposition.

---

## 8. The boundary — where eval ends and research begins

Several firms surface a clear internal distinction:

- **Anthropic's Frontier Red Team** (Research Engineer / Research Scientist titles) is explicitly framed as research, housed inside the Policy organisation. Its sibling team Safeguards has a separate Red Team Engineer title — not Research Engineer — framed as engineering.
- **OpenAI's Frontier Evals and Environments** is a Research Engineer role, explicitly research-adjacent; its "eval-driven development" posture merges the two.
- **Apple's Siri AI Quality Engineering** is unambiguously engineering: SWE, Lead SWE in Test, ML Engineer, Senior SWE titles; no Research prefix. The Apple instance is the cleanest case of eval engineering existing as pure productization, distinct from research.
- **Meta's GenAI Trust and Safety Red Team** is hybrid — "Red Teaming Research Scientist" is the title Evtimov carries.

**Synthesis**: The boundary is clearest at product-layer firms (Apple, Harvey, Decagon) where eval is treated as QA/reliability engineering, and fuzziest at frontier labs (Anthropic, OpenAI, DeepMind) where eval is co-located with research because the eval itself is often a research artifact (new benchmark, new auditing agent). This confirms the parent memo's §2 intuition that evaluation infrastructure is a productization output when deployed on a model someone else trained, and a research output when co-developed with the model. The same activity can be either depending on the location in the value chain.

---

## 9. Surprises

1. **Apple is further along than frontier labs** on title differentiation. Apple has five distinct Siri-side evaluation/QE titles; Anthropic and OpenAI have one explicit "Evaluations" title each, supplemented by ambiguous "Research Engineer" titles on adjacent teams. Product-layer scale and regulated-industry exposure force earlier title differentiation than frontier-research status does.
2. **Humanloop, an early eval-tooling pioneer, is sunsetting in September 2025** — the eval-tooling market has consolidated around a smaller number of well-funded players rather than fragmenting into many specialists.
3. **Langfuse was acquired into ClickHouse at a $15B Series D valuation** (January 2026) — AI-observability is being absorbed into general observability / data-infrastructure plays.
4. **Braintrust's $80M Series B at $800M valuation** (Feb 2026) is the strongest late-stage signal that investors price standalone eval tooling as a venture category.
5. **JPMorgan MLCOE 200+ ML specialists plus MRG** is SR 11-7-driven rather than AI-native but represents more eval-adjacent headcount than any single AI-tooling vendor.
6. **Scale AI cut 200 FTE + 500 contractors in July 2025 but then launched Scale Labs in March 2026** — even under cost pressure, frontier firms restructure the evaluation function rather than cut it.
7. **The eval course economy is larger than any single firm's eval headcount**: Husain/Shankar trained 4,500 students from 500 companies. Cross-firm homogenisation via a single curriculum is unusual for a young discipline and suggests the profession is forming bottom-up from practitioners as much as top-down from firm mandates.
8. **There is no "eval engineer" certification** equivalent to ISO 42001 or IAPP AIGP for the productization-substance side. IAPP AIGP (v2.1.0 Feb 2026; US median $151,800) is a governance-professional credential, not an engineering credential. This gap is consistent with the parent memo's verification-claim / verification-substance split: certifications are sales-instruments, and the evaluation-engineering craft has no sales-instrument certification yet.
9. **AI liability insurance underwriters are beginning to require evaluation attestations**: Armilla AI (Lloyd's-backed, $25M/policy) explicitly "moves from questionnaires to evidence-based external evaluation and continuous monitoring." Munich Re aiSure product already requires evaluation-grade performance data. Verisk's January 2026 malpractice AI exclusion creates a pull for SME-serving evaluation attestations that the small-firm supplier base is not yet positioned to produce. Deloitte projects AI insurance premiums at $4.7B by 2032, 80% annual rate.

---

## 10. Bearing on the decomposition memo

**Confirmation 1** — Eval engineering is a labour-market-visible profession. Dedicated titles, named teachers, a textbook, 50+ students per frontier firm, $100M+ of category venture capital. Productization skill is decomposable into nameable sub-skills with their own labour markets.

**Confirmation 2** — The profession is concentrated where productization skill is independent of sales skill. Apple's Siri evaluation-engineering stack (five engineering titles accountable for Siri quality, not Siri sales) is the clearest case. The Apple case supports H1 and H3 in the parent memo: frontier labs (productization-native) and heavily productized product-layer firms (Harvey, Decagon) carry thicker eval engineering than wrapper firms.

**Confirmation 3** — The Korean / Asian case is a natural experiment in which productization skill crystallises through state-sponsored infrastructure rather than firm-level labour markets. Korea AISI + KAIST / SNU / Yonsei / POSTECH + scheduled 2026 College of AI produce the evaluation-engineering base that Samsung / Naver / Kakao / LG do not yet produce internally at the job-posting level. Consistent with Finding 3 reformulation: in Korea the verification-substance public good is being produced by the state, not privately. A similar pattern holds in Singapore (AI Verify as government-built modular verification stack) and the UK (AISI Inspect, which Anthropic's Petri extends).

**Sharpening** — The verification-substance ≠ verification-claims split is now backed by a distinct labour market. The eval engineer builds substance; the AIGP-certified governance professional (IAPP $151,800 median) publishes claims. Different salary bands, different career ladders, different employers in many cases. The decomposition hypothesis is rendered as organisational design.

**Caveat / partial counterexample** — At frontier labs evaluation is not fully separable from research. The FRT Cyber Research Scientist title, the Meta Red Teaming Research Scientist title, and the OpenAI Frontier Evals Research Engineer title all point at a hybrid activity. In those firms, evaluation is still joint with research, not yet a pure productization function.

---

## 11. Limits of this stream

- Exact headcount per firm is not public at any frontier lab; totals are inferred from aggregate Greenhouse/LinkedIn posting counts and company-wide growth disclosures.
- Firm-level ARR for eval-tooling firms is partly private (Patronus, Galileo, Braintrust specific revenue figures undisclosed); LangChain's $12-16M figure is an analyst estimate.
- Salary data for "eval engineer" specifically is absent from H1B and Levels.fyi — the closest bands come from parent Research Engineer / ML Engineer / Software Engineer titles at the same firms.
- Korean-language job boards (Saramin, JobKorea) were not directly searched; English-language coverage is partial.
- This synthesis cannot rule out a lab that deliberately does NOT have eval engineers — among named firms, Cohere and Mistral did not surface a clear eval-engineering hiring signal in public data, but absence is not evidence of absence.

---

## 12. Sources

- [Anthropic Research Engineer Model Evaluations](https://job-boards.greenhouse.io/anthropic/jobs/4990535008)
- [Anthropic Frontier Red Team postings](https://job-boards.greenhouse.io/anthropic/)
- [OpenAI Frontier Evals and Environments](https://openai.com/careers/search/)
- [Apple AI Evaluation Engineer Siri Core Modeling](https://jobs.apple.com/en-us/search?product=siri-SIRI)
- [Arize Series C](https://arize.com/blog/arize-ai-raises-70m-series-c-to-build-the-gold-standard-for-ai-evaluation-observability/)
- [Galileo Series B](https://www.prnewswire.com/news-releases/galileo-raises-45m-series-b-funding-to-bring-evaluation-intelligence-to-generative-ai-teams-everywhere-302276383.html)
- [Braintrust Series B Feb 2026](https://siliconangle.com/2026/02/17/braintrust-lands-80m-series-b-funding-round-become-observability-layer-ai/)
- [LangChain State of Agent Engineering](https://www.langchain.com/state-of-agent-engineering)
- [Husain + Shankar AI Evals course](https://maven.com/parlance-labs/evals)
- [Korea AI Safety Institute](https://www.aisi.re.kr/eng/contents/22)
- [Scale-Korea AISI partnership](https://scale.com/blog/korea-ai-safety-institute-partnership)
- [Armilla AI Liability Insurance](https://www.armilla.ai/)
- [Anthropic Petri 2.0](https://alignment.anthropic.com/2026/petri-v2/)
- [Verisk AI exclusions Jan 2026](https://www.independentagent.com/vu_resource/verisk-to-roll-out-new-general-liability-exclusions-for-generative-ai-exposures/)
- [Gartner LLM observability 2028 forecast](https://www.gartner.com/en/newsroom/press-releases/2026-03-30-gartner-predicts-by-2028-explainable-ai-will-drive-llm-observability-investments-to-50-percent-for-secure-genai-deployment)
- [IAPP AIGP 2026](https://iapp.org/certify/aigp)
