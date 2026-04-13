# Tier S1 — Solo Entrepreneurs and Individual Decision-Makers

status: research_in_progress
tier: S1
date: 2026-04-13

---

## 1. Tier Definition and Scope

Tier S1 covers any decision context in which the verifier, requester, decision-maker, and accountable party converge on a single individual. It is a structural category, not a headcount band: no division of cognitive labor between the person consuming the AI output and the person who must answer for it.

Sub-populations: **solo founders and one-person SaaS operators** (indie hackers, micro-SaaS, single-member LLCs); **solo licensed professionals** (attorneys, physicians, CPAs/EAs, Registered Investment Advisers, psychologists, dentists); **freelancers and independent consultants** (platform-mediated via Upwork, Fiverr, Toptal, Outlier, MBO Partners; or direct-relationship); **retail investors** making capital-allocation decisions on personal assets — not businesses, but structurally identical: one person, one decision, no review committee.

Not in S1: any organization with a second human who reviews AI output before commitment. The boundary is sharper than it sounds — a 3-person LLC drops into S1 every time the founder works alone on a deliverable the other two never read.

**Sizing.** U.S. solopreneurs are estimated at 29.8M people contributing ~$1.7T to U.S. GDP (~6.8 percent of total activity, 82 percent of U.S. small businesses; Inc. Magazine 2025; CNBC September 2025) [B]. Adjacent: 70M Americans in the 2025 gig economy (~36 percent of workforce); full-time independents doubled from 13.6M (2020) to 27.7M (2024); 36 percent of Carta-tracked 2025 startups were solo-founded; freelancers earned ~$1.3T in 2024–2025; MBO Partners reports 5.6M U.S. independents earning over $100,000/year [B]. Conservative aggregate: at least $2T in U.S. economic activity at S1.

---

## 2. The Research Vacuum

This section is unusual for a tier report. It exists because the absence of literature on this tier is itself the most important finding, and so future readers do not mistake the report's heavy reliance on inferred evidence for analytical sloppiness. It is the literature, not the analyst, that is missing.

**Academic.** A 2023–2026 search across CoT faithfulness, automation bias, appropriate-reliance frameworks, AI overreliance, and AI in legal/health/finance domains returns essentially zero peer-reviewed studies that take the one-person business as a unit of analysis. Schemmer et al. (2023), Goddard et al. (2012), Lyell and Coiera (2017), the Gillespie/KPMG 2025 global trust study (n=48,340), and the Microsoft New Future of Work Report all sample employees inside organizations. None decomposes respondents into a 1-employee bucket.

**Practitioner.** A handful of essays use language like "verification tax," "cognitive escrow," and "judgment debt." The most cited is Fractionalview's 2026 *AI Makes Judgment More Expensive: The Verification Tax* — well argued, but addresses team and organizational dynamics, contains no quantitative claims, and does not engage solo founders. Small-business compliance guides (TrueFuture 2026, NC Bar January 2026) treat verification as a checklist, not a research object.

**Regulatory.** The SEC's Predictive Data Analytics Rule was withdrawn June 17, 2025; no final U.S. SEC rule for investment advisers targets generative AI. Colorado's AI Act (February 1, 2026) and California AB 2013 (January 1, 2026) cover deployers of high-risk AI but enforcement against a one-person LLC is unclear and untested. ABA Formal Opinion 512 (2024) extends Rules 1.1 and 5.3 to AI use, but the supervision-of-nonlawyers framing is awkward when there is no nonlawyer to supervise. None of these instruments models a single-person actor as the central case.

**Incident corpora.** Charlotin AI Hallucination Cases Database: 1,313 documented cases across 33 jurisdictions as of early April 2026 [HIGH]; 784 (~59 percent) pro se; Stanford Cyberlaw October 2025 sample of 114 cases found 89.9 percent involve solo or sub-25-attorney firms [HIGH]. The only large-scale empirical evidence of S1-adjacent failure rates, concentrated in law because courts force disclosure. No analogous corpus exists for solo CPAs, physicians, financial advisers, SaaS founders, or retail investors. Inference: failure rates in those domains are at least comparable; the difference is no adversarial party rechecks the work.

**Why the vacuum exists.** S1 actors are statistically inconvenient (too small for establishment surveys, too dispersed for convenience samples), own their own outcomes (failures absorbed privately, never entering public datasets), and the AI governance literature inherited its analytical apparatus from organizational behavior research — which assumes hierarchies, committees, and reviewers, all absent at S1.

**Why it matters.** The solo-founder economy is ~$1.7T in the U.S. alone. The S1 verification-failure rate is plausibly the highest in the taxonomy, with consequences absorbed silently by individuals with no institutional cushion. A framework that does not take a position on this tier is implicitly conceding the most exposed population to AI vendor defaults. Most claims in this report are graded C (inferred) or D (speculative) — the honest reflection of a vacuum, not a flaw. The report maps the outline so primary fieldwork can target it.

---

## 3. Core Question Answered

**Question.** Is reasoning verification even possible when the verifier, requester, decision-maker, and accountable party are the same individual, or does the framework need a substantively different offering at this tier?

**Answer.** Reasoning verification as currently formulated — a five-discipline review (source quality, inferential validity, normative acceptability, confidence calibration, failure mode awareness) — is **not feasible** as a private discipline at S1 for the typical decision. The same person cannot reliably play advocate (asking the AI for help) and skeptic (challenging the AI's reasoning) on the same artifact under time pressure, and S1 actors operate under permanent time pressure. The framework needs a substantively different offering: partly behavioral (a radically compressed routine) and partly infrastructural (verification as a public good or third-party service).

Three convergent lines of evidence. First, the HITL literature (Goddard et al. 2012; Parasuraman et al. 1993; Lyell and Coiera 2017; Bahner et al. 2008) establishes that automation bias and complacency cannot be eliminated by training, scale with verification complexity, and worsen when reliability appears high — the S1 actor combines all three at maximum intensity. Second, the legal-profession failure record shows that actors with the strongest professional incentive to verify — solo and small-firm attorneys facing sanctions — fail at high rates anyway. Third, the CoT faithfulness literature (Chen et al. 2025; Lanham et al. 2023; Mancoridis et al. 2025; Korbak et al. 2025) shows the surface signals an S1 actor would rely on (apparent confidence, fluent reasoning, plausible citations) are systematically uninformative about whether the underlying reasoning is sound. There is no compensating institutional mechanism at S1 to absorb the residual error.

---

## 4. Comparative Dimensions (D1-D10)

**D1 — Verification agent identity.** Verifier, requester, decision-maker, and accountable party are the same individual. N_verifiers = 1 by definition. Closest substitute is a community thread on Reddit/HN/X — asynchronous, unreliable, not commitment-bearing. **[A]**

**D2 — Verification infrastructure.** A browser, two or three chatbots, a search engine, possibly Perplexity, occasionally a paid review service. No internal platform, no committee, no template library, no red team, no vetted-corpus retrieval. **[B]**

**D3 — Verification incentive structure.** Privately costly (attention), privately beneficial (better decisions). External incentives are weak except for solo licensed professionals. The incentive curve is slack except at the catastrophic-failure tail, which actors systematically underestimate. **[C]**

**D4 — Sanction gradient.** Heterogeneous and bimodal. For solo licensed professionals identical to S5 (court sanctions, bar discipline, malpractice, license suspension, IRS penalties) but verification capacity is S1 — the most dangerous combination in the taxonomy (Section 6.2). For non-licensed S1 actors restricted to direct economic loss and narrow reputational damage. **[B for licensed, C for non-licensed]**

**D5 — Verification trigger.** Almost always personal curiosity or visible error, not standing policy. Dominant pattern: actor notices something off and rechecks. Parasuraman and Manzey (2010) suggest this trigger fires less often as model performance becomes familiar. **[B by analogy]**

**D6 — Per-decision verification budget.** No empirical S1 measurement. Inference: 30 sec–5 min routine; 20–30 min for flagged high-stakes. **VTI (routine):** T_verify/T_total ≈ 0.05–0.15; N_reviewers = 1; N_sources = 0–2. **(High-stakes):** T_verify/T_total ≈ 0.20–0.40; N_sources = 1–4. **[D]**

**D7 — Delegation chain depth.** Zero. AI output reaches the decision in a single hop. Structurally distinct from all other tiers. **[A]**

**D8 — Failure mode profile.** (a) **passive acceptance** of fluent but unfaithful reasoning (Korbak et al. 2025); (b) **citation fabrication** (the Charlotin pattern); (c) **automation complacency drift** (Parasuraman and Manzey 2010); (d) **sycophantic loop reinforcement** — framings echoed back and treated as confirmation (UNU 2025: 58 percent sycophantic, 78.5 percent persistence); (e) **isolation bias** — actor anchors on the AI's first-pass framing. The compound — passive acceptance of a sycophantic answer that confirms the actor's prior — is the worst. **[B/C]**

**D9 — Substitutes.** Ranked: (a) second-model query; (b) corroborating-source search; (c) community forum post; (d) paid expert review; (e) professional liability insurance; (f) deferral; (g) outsourcing. Sections 7–8 develop. **[B]**

**D10 — Scale-crossing dynamics.** Hiring a first contractor immediately redistributes verification — the second person can read AI output before commitment even in an unrelated role. Reverse: an S2 actor slides back to S1 when a contractor leaves or the founder works alone on a weekend deliverable. Same legal entity can be S1 on Monday and S2 on Tuesday. **[C]**

---

## 5. The Verification Tax at S1

The verification tax is the unifying lens. Adapted from Fractionalview's 2026 essay and the HITL literature: AI does not eliminate the cognitive cost of judgment; it concentrates and externalizes that cost from producing a draft to accepting one. At higher tiers the tax is paid by reviewers, committees, or compliance functions whose job is to absorb it. **At S1 it is paid by the same person who would otherwise be writing the deliverable, billing the client, or shipping the feature.**

**Time concentration.** The five disciplines executed on an AI memo each consume 2–10 min at BCG-associate-minimal level. A complete review is 10–50 min/memo. Across a typical S1 workday (3–8 AI-assisted decisions) the verification floor is 30–400 min/day against an effective working day of 360–480 min. The upper bound exceeds the day. Complete verification is impossible at S1 for a non-trivial decision rate; the actor must triage. **[D]**

**Attention concentration.** Unlike time, attention is not fungible. The cognitive switching cost between "asking for help" and "challenging the answer" is high. The S1 actor performs both roles on the same artifact, often in the same minute. Higher tiers route the artifact across roles. **[B]**

**Accountability concentration.** A reviewer at S4 clearing an AI output bears responsibility distributed across reviewer, author, manager, committee. An S1 actor bears 100 percent. Structural, not psychological. **[A]**

**Decision-quality compounding.** Decisions at S1 feed each other. A miscoded tax position becomes next year's filing; a flawed strategic memo becomes the next investor pitch; a hallucinated citation becomes the foundation for an entire brief. Skipped verification propagates. **[C]**

**The Fractionalview blind spot.** The essay treats the verification tax as an organizational design problem solvable by clearer decision principles, escalation paths, accountability designation. Those tools are unavailable at S1 by definition. The S1 version is not "redesign your decision flow" but "the decision flow has only one node." If the tax cannot be paid privately, the framework either fails at S1 or externalizes verification to infrastructure (Section 8) — stop treating verification as a discipline inside the actor's head; treat it as a service or a public good.

---

## 6. Sub-Population Cases

### 6.1 — Solo founders and one-person SaaS

Solo SaaS founders use AI across the product lifecycle: ideation, market research, code generation, customer support, marketing copy, pricing, investor updates. 36 percent of Carta-tracked 2025 startups were solo-founded, up from 31 percent in 2024 [B]. Practitioner accounts (DEV.to, Indie Hackers, Hacker News 2025–2026): code generation is verified by running tests — the only S1 surface with an automated forcing function; marketing and copy outputs are not verified at all in most cases; strategic and pricing outputs are sometimes second-model-checked, rarely by primary research. The "expert trap" (Development Corporate 2026): domain knowledge can amplify rather than dampen overreliance by making the actor pattern-match AI output to plausible analogs. METR's 2025 RCT: AI assistance produced a 19 percent slowdown in experienced open-source developers; the Webapper SaaS Hallucinations roundup documents shipped features that crashed because AI library calls did not exist. **[B/C]**

**Representative VTI (S1 founder shipping a marketing landing page):** T_total ≈ 25 min, T_verify ≈ 2 min, N_sources = 0. **RVCS-1: 0/15.** **[D]**

### 6.2 — Solo licensed professionals (attorney, physician, CPA, financial adviser)

The most dangerous sub-population in the entire taxonomy: S5 liability exposure with S1 verification capacity. Sanctions span court orders, bar discipline, malpractice, license suspension, IRS penalties, criminal liability in extreme tax cases.

**Solo attorneys.** Charlotin: 1,313 cases as of early April 2026, growing 5–6/day; 784 pro se (~59 percent); Stanford Cyberlaw October 2025 sample of 114 cases: 89.9 percent involve solo/sub-25-attorney firms [HIGH]. Brigandi (*Couvrette v. Wisnovsky*, D. Or., April 4, 2026): $96,000 direct ($110,200+ total) for 23 fabricated citations and 8 invented quotations [HIGH]. *Whiting v. City of Athens* (6th Cir., March 13, 2026): $15,000 each plus double costs and appellee fees for 24+ fabricated citations [HIGH]. Q1 2026: $145,000 cumulative on solo/small-firm attorneys [B]. Oregon Court of Appeals tariff (December 2025): $500/citation, $1,000/quotation [B]. Verisk AI exclusion endorsements January 1, 2026 [HIGH]. ABA Formal Opinion 512 (2024) confirms Rule 1.1 competence extends to AI. Failure concentrates at the smallest firm sizes despite the strongest formal incentive to verify.

**Solo physicians.** No public corpus, but liability literature is converging (The Doctors Company Q4 2025; Medical Economics; McCune Wright July 2025): blind AI acceptance does not transfer liability to the vendor [B]. Many U.S. malpractice insurers now include AI exclusions or require AI-training certifications [B]. The evolving standard of care means a solo physician risks both negligence for *using* AI without verification and negligence for *not* using it when it would have helped.

**Solo CPAs / EAs.** The IRS treats AI-assisted errors as preparer responsibility — no safe harbor (Accounting Solutions Ltd. 2025; Tax Executive 2025) [B]. ~50 percent error rates for complex AI tax advice [B]. Pattern: client AI'ed their own correct return, then demanded amendments matching the AI's hallucinations.

**Solo financial advisers.** AI has no fiduciary duty (CNBC April 2026) [B]; the adviser who relies on it does. SEC 2026 examination priorities highlight AI risk controls; the withdrawn Predictive Data Analytics Rule leaves the Investment Advisers Act of 1940 duty of care in force [HIGH]. The solo RIA bears full fiduciary risk with no compliance officer or peer reviewer.

**The danger compound.** Highest D4 (steep), lowest D6 (minimal). Structurally unstable. Law is the only domain where failures surface publicly because courts have an adversarial process; in medicine, accounting, and financial advice they accumulate silently — as consulting failures did until Christopher Rudge read a Deloitte report and recognized a fabricated book citation. **Representative VTI (solo attorney filing an AI-assisted brief):** T_total ≈ 240 min, T_verify ≈ 25 min (Westlaw citation spot-check only, no inference review). **RVCS-1: 4/15** — the level at which sanctioned attorneys were operating. **[C]**

### 6.3 — Freelancers and independent consultants

Freelancers occupy a middle position: client accountability without licensure, reputation accountability without bar discipline, contractual accountability without statutory liability. ~70M Americans in the 2025 gig economy; 5.6M U.S. independents earned over $100,000 (MBO Partners) [B]. Upwork's 2026 ChatGPT integration routes ChatGPT users to expert freelancers — treating the freelancer as the verification surface for the client's AI tasks [B], inverting the problem so the freelancer is hired to verify the client's AI work even as the freelancer uses their own. Both layers unverified. Practitioner accounts (FreelanceMVP, Fueler.io, Asrify, Hacker News 2024–2026): triage by client stakes; reputation systems sanction outcome quality not process quality; community verification is informal and not commitment-bearing. **[C]**

**Representative VTI (freelance consultant delivering an AI-assisted strategy memo):** T_total ≈ 180 min, T_verify ≈ 15 min, N_sources = 1. **RVCS-1: 3/15.** **[D]**

### 6.4 — Retail investors

Retail investors are the largest S1 sub-population by headcount and capital deployed. SEC Press Release 2025-144 (December 2025) charged three purported crypto platforms and four investment clubs with a $14M scheme luring retail investors with "AI-generated investment tips" via WhatsApp [HIGH]. AI-driven fraud surged 456 percent in 2025 versus 2024, global losses exceeding $10.7B [B]. Earlier Delphia and Global Predictions actions (March 2024; $225,000 and $175,000) targeted "AI-washing" by registered advisers [HIGH]. The SEC Cyber and Emerging Technologies Unit (CETU, early 2025) is enforcement-focused, not verification-infrastructure-focused.

Retail investors use ChatGPT, Claude, and Gemini for ticker research, options screening, and investment thesis generation. None of these models has live market data without explicit tool use, none has fiduciary duty, none is liable. Wall Street Prep 2026 and Deepvest's *When AI Sounds Smart But Gets the Numbers Wrong* (WealthManagement March 2026) both show general LLMs underperforming a junior analyst; ChatGPT 5.2 returned a Bitcoin ROE of -7.93 percent versus actual +27.82 percent in one test [MEDIUM]. The CFA Institute's 2025 position: "in high-stakes fields like finance, AI should be used to support decision design, not to make the final decision" [HIGH] — voluntary, not binding on retail investors.

**Representative VTI (retail investor evaluating an AI-generated stock thesis):** T_total ≈ 30 min, T_verify ≈ 4 min, N_sources = 1–2. **RVCS-1: 0/15.** **[D]**

---

## 7. Tool Audit — What S1 Users Actually Have Access To

Tools available in April 2026, mapped to the five disciplines (Q1 source quality, Q2 inferential validity, Q3 normative acceptability, Q4 confidence calibration, Q5 failure mode awareness).

1. **Manual second-model crosscheck** — same question to a different chatbot. Q1 + Q2 weakly. Most-used; shared training-data bias limits effectiveness. **[B]**
2. **Multi-model verification platforms** (CrossCheck.ai, Platilus, getcrosscheck.ai). Q1 + Q2 + Q4. Emerging 2025–2026; untested at scale. **[B]**
3. **Browser-based fact checkers** (Perplexity, You.com, Google AI Overviews, Bing Copilot). Q1 + Q2 weakly. Citations may still be hallucinated. **[B]**
4. **Amazon Bedrock Guardrails Automated Reasoning checks** — formal verification, up to 99 percent accuracy on bounded policy domains. Q2 + Q3. GA August 2025; NL test Q&A November 2025. Requires user to formalize policy in advance. Out of reach for typical solo founder; accessible to technical micro-SaaS. First commercial product bringing formal-logic verification to a non-research audience. **[HIGH capability; C accessibility]**
5. **Community review** (Reddit, Hacker News, Stack Overflow, X, Discord, Indie Hackers). Q1–Q5 sometimes. Reddit's March 2026 human-verification rollout signals bot dilution. Not commitment-bearing. **[B]**
6. **Paid one-off expert review** (UpCounsel, JustAnswer, Clarity.fm, Maven, Intro) — $50–$500/consultation. All five disciplines. Used only for high-stakes decisions. **[B]**
7. **Professional liability insurance** (Verisk, Hiscox, Next, Embroker). Substitutes by absorbing residual risk. Verisk's AI exclusion endorsements (January 1, 2026) *narrow* coverage. Insurance is moving away from AI risk. **[HIGH]**
8. **Domain-specific verified databases** (Westlaw, Lexis, Bloomberg, FactSet, UpToDate, PubMed) — $50–$30,000+/year. Q1 gold standard, Q5. Licensed solo professionals subscribe; founders, freelancers, retail investors cannot afford them. **[B]**
9. **Vendor-supplied verification features** (ChatGPT browsing, Claude Citations, Gemini Deep Research, NotebookLM). Q1 + Q2 weakly. Improved citation honesty but no inferential-chain validation. Mancoridis et al. 2025 Potemkin: sourced answers can still fabricate conceptual coherence. **[B]**
10. **Output-evaluation tools** (Patronus Percival, Galileo, Arize Phoenix, Langfuse, Braintrust). Q2, Q5. Target developers building AI agents, not S1 actors verifying their own output. Percival is the closest non-expert reasoning verifier; still requires SDK instrumentation. **[HIGH capability; D accessibility]**
11. **Structured prompting templates** (red-team-yourself prompts). Q2 sometimes, Q5. Cheapest forcing function; sycophancy contamination — the model's red team is still the model. **[C]**

**Cross-reading.** Decent Q1; thin Q2 (only Bedrock at a high standard, largely inaccessible); almost no Q3; almost no Q4; patchy Q5. **The five disciplines are not equally available at S1.** This unevenness should drive any S1-specific offering.

---

## 8. Candidate Infrastructure for a Scale-Public-Good Answer

If reasoning verification is infeasible as a private discipline at S1, what infrastructure could replace it? Three primary candidates, ordered by feasibility.

**Candidate 1 — Standard AI reasoning audit APIs as a public good.** A standardized verification API any vendor implements and any S1 actor can call. Takes AI-generated text plus an optional source set; returns source quality grades, inferential validity flags, normative-acceptability flags against a published rubric, confidence calibration warnings, failure mode catalog hits. *Could work because* Amazon Bedrock Guardrails Automated Reasoning checks (GA August 2025) demonstrates formal logic verification at near-99 percent accuracy on bounded policy domains [HIGH]; Patronus TRAIL, Galileo, and Arize Phoenix demonstrate trace-level automated reasoning evaluation is tractable; multi-model platforms demonstrate consumer-facing divergence UX. Missing: unified API standard, regulatory mandate, non-engineer UX. *Might not because* TRAIL shows even frontier-model joint accuracy below 12 percent on multi-step agent error localization [HIGH]; reasoning verification is harder than policy compliance; naive deployment would hand S1 actors false security. **Feasibility: B.**

**Candidate 2 — Third-party verification marketplaces.** A two-sided marketplace where S1 actors post AI outputs and credentialed reviewers (domain experts, retired licensed professionals, paralegals, junior consultants) bid to verify them. Priced per claim or memo. The marketplace handles credentialing, payment, reputation. Reviewers apply the five-discipline framework. *Could work because* Upwork's 2026 ChatGPT integration already routes users to expert freelancers [B]; Outlier-style platforms already pay freelancers to evaluate AI output for vendor training and the mechanics could be redirected; the reviewer pool is large (5.6M U.S. independents earning >$100,000); the marketplace generates a public reputation surface absorbing the accountability burden the lone S1 actor cannot. *Might not because* domain mismatches are likely, reviewer sycophancy is a risk under satisfaction-based pricing, and the model assumes S1 actors will pay for verification — which they currently do not. **Feasibility: C.**

**Candidate 3 — Mandatory AI vendor disclosure.** Regulatory action requiring vendors to expose what S1 actors need: a standardized confidence score with calibration sample, sources actually retrieved (not plausible citations), known failure modes for the prompt class, refuse/escalate conditions. Travels with the output as metadata, like a nutrition label. *Could work because* FDA's January 2026 CDS guidance requires "clinician-reviewable logic" [HIGH] — a domain precedent; EU AI Act Article 14 can support this; Australian DTA's December 2025 Policy v2.0 imposed disclosure-style obligations on contractors [HIGH]. *Might not because* the CoT faithfulness debate (Chen et al. 2025: 25 percent CoT mention rate; reward-hack admission < 2 percent) shows vendors cannot reliably introspect their own models [HIGH]; solo actors are not a constituency that drives U.S. AI rulemaking. **Feasibility: B technical, D regulatory.**

**Briefly noted.** Peer-reviewed community surfaces (Community-Notes-style; Reddit's March 2026 human verification is a precondition); insurance-backed verification (Verisk exclusions point the *opposite* way — niche at best); regulatory dashboards analogous to Investor.gov (politically dependent).

**Cross-cutting principle.** The candidates differ on who pays the verification tax: vendors (C3), reviewers (C2), automated systems (C1). A complete answer probably uses all three at different decision stakes — formal audits at the bottom (low stakes, high volume), human marketplaces in the middle, vendor-mandated disclosure as a regulatory floor. The S1 offering should be a triage rule, not a single tool.

---

## 9. Known Failures / Incidents

(Section 6.2 catalogues the legal-profession incidents; this section adds non-legal cases.)

- **Hancock declaration.** *Kohls v. Ellison*, D. Minn., January 10, 2025. Stanford Social Media Lab founding director used GPT-4o + Google Scholar to assemble an expert declaration; two articles fabricated, one miscited; declaration struck. The world's leading misinformation scholar failed to detect AI-generated misinformation in his own field. **[HIGH]**
- **SEC v. crypto investment clubs.** Press Release 2025-144, December 2025. $14M scheme using "AI-generated investment tips" via WhatsApp. Retail investors' acceptance of unverifiable AI tips on faith is the structural S1 failure. **[HIGH]**
- **Delphia and Global Predictions.** SEC Press Release 2024-36, March 2024. $225,000 and $175,000 settlements for AI-washing — illustrative of how hard it is for retail investors to detect false AI capability claims. **[HIGH]**
- **Verisk AI exclusion** (January 1, 2026): insurance industry's first explicit signal that solo professionals' AI risks are being priced out of standard coverage. **[HIGH]**
- **Inferred-only.** Solo medical practice (no public corpus; inferred from Goddard et al. 2012 RR 1.26 plus malpractice exclusion trends) **[D]**. Solo SaaS founders shipping code with hallucinated library calls; failures surface only after deploy (Webapper 2025–2026; METR 19 percent slowdown) **[C]**.
- **Substack expert hallucination.** A former news executive whose Substack contained 15 of 53 posts with fabricated quotes attributed to real people who confirmed they never made the statements. **[B]**

---

## 10. Open Questions

1. What is the actual per-decision verification budget at S1 in minutes? No diary study exists. A protocol with 30–50 solo actors across the four sub-populations is the highest-value first study.
2. What is the empirical RVCS-1 score distribution at S1? Illustrative scores here are extrapolated.
3. At what compound rate does insurance withdrawal cascade across solo licensed professions? Verisk may be the first signal.
4. Does multi-model crosscheck actually work, or does shared training-data bias collapse the divergence signal?
5. Have solo CPAs, physicians, and advisers changed their AI use after the Verisk exclusion?
6. Do retail investors using AI-generated analysis underperform self-directed investors? Brokerage data could settle this.
7. Is a verification marketplace economically viable, and at what price point would an S1 actor pay for verification of one memo?
8. How much does the failure rate fall when an S1 actor adopts a single forcing function?
9. What is the legal exposure of an S1 actor relying on AI when a regulator cannot prove vendor negligence? Open as of April 2026.
10. Does the framing of "verification tax" actually shift S1 behavior?
11. Is the right unit of analysis the individual or the decision? The same person may be S1 for one decision and S2 for the next.
12. What does an S1-native verification UX look like? No product targets this user.

---

## 11. Sources

**Academic / lab.** Chen et al. (Anthropic) arXiv 2505.05410, 2025; Lanham et al. (Anthropic) arXiv 2307.13702, 2023; Korbak et al. arXiv 2507.11473, 2025; Mancoridis, Weeks, Vafa, Mullainathan, *Potemkin Understanding in LLMs*, ICML 2025; Goddard, Roudsari, Wyatt, JAMIA 19(1), 2012; Lyell, Coiera, JAMIA 24(2), 2017; Parasuraman, Manzey, Human Factors 52(3), 2010; Bahner, Hüper, Manzey, IJHCS 66(9), 2008; Schemmer et al., IUI 2023; Gillespie, Lockey et al., *Trust, attitudes and use of AI: global study 2025*, Melbourne/KPMG (n=48,340).

**Legal.** Charlotin, damiencharlotin.com/hallucinations; Stanford Cyberlaw party-type analysis, October 2025; *Couvrette v. Wisnovsky* D. Or. April 4, 2026 (Brigandi); *Whiting v. City of Athens* 6th Cir. March 13, 2026; *Kohls v. Ellison* D. Minn. January 10, 2025 (Hancock); ABA Formal Opinion 512, 2024; Oregon Court of Appeals tariff schedule, December 2025.

**Regulatory.** SEC Press Releases 2025-144 and 2024-36; SEC 2026 Examination Priorities; FINRA 2026 Annual Regulatory Oversight Report; Verisk AI exclusion endorsements (January 1, 2026); FDA CDS guidance update, January 2026; Australian DTA Policy v2.0, December 15, 2025; Colorado AI Act; California AB 2013.

**Practitioner / trade press.** Fractionalview *Verification Tax* 2026; TrueFuture *Small Business AI Compliance Guide* 2026; NC Bar *Beyond the Ban* January 2026; The Doctors Company *AI on Trial* Q4 2025; Medical Economics 2025; Accounting Solutions Ltd 2025; Tax Executive 2025; Webapper *SaaS AI Hallucinations* 2025–2026; Development Corporate *The Expert Trap* 2026; Wall Street Prep 2026 benchmark; Deepvest WealthManagement March 2026; CFA Institute *AI in Asset Management 2025*; NexLaw, The Ethics Reporter, Sterne Kessler hallucination-sanction reporting.

**Tools / products.** AWS Bedrock Guardrails Automated Reasoning checks (August/November 2025); Patronus TRAIL and Percival 2025; CrossCheck.ai, Platilus, getcrosscheck.ai 2025–2026; CompanionLink April 2026; Reddit human-verification rollout March 2026; Upwork ChatGPT integration (PYMNTS 2026); Outlier AI 2026.

**Sizing.** Inc. Magazine 2025; CNBC September 22, 2025; HRStacks 2026; MBO Partners 2025; Carta 2025.

**Project context.** `research/operations/expansion/scale-based-reasoning-trust-research-plan.md`; `research/core/literature/online-discourse-deep-dive-2026-04.md`; `research/core/literature/reasoning-trust-landscape.md`.

---

*Cells graded D are speculative extrapolations included because the gap justifies them; future primary fieldwork should challenge them. The report's reliance on inferred and adjacent evidence reflects the documented research vacuum at S1, not analytical sloppiness, and is itself the most important finding the report delivers.*
