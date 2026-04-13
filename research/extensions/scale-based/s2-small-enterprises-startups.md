# Tier S2 — Small Enterprises and Startups

status: research_in_progress
tier: S2
date: 2026-04-13

---

## 1. Tier Definition and Scope

Tier S2 covers organizations of ~10-250 employees, late seed through Series C, that build or deploy AI as a central part of their product. The defining structural property is that reasoning verification is **founder- or CTO-driven, ad hoc, and incident-triggered**. No role exists whose only job is verification, no committee exists whose only purpose is review, no budget survives a pricing renegotiation.

S2 is the most volatile tier in the taxonomy because its headcount band conceals two qualitatively different populations: AI-native firms building foundation models, and AI-using firms consuming third-party AI. Both are treated separately in §4 and synthesized in §6. S2 is *not* a scaled-down S4: enterprise governance instruments (committees, model risk management, three-tier boards, CAIOs) cost more annually than most S2 firms spend on their entire engineering function. (A) Source: `research/extensions/adaptive-governance/startup-small-org-governance.md` §8.1.

---

## 2. Core Question Answered

**At what point in the startup lifecycle does reasoning verification become a standing practice, and what triggers the transition from ad-hoc founder judgment to a repeatable verification routine?**

For AI-using startups, verification typically does not become a standing practice until **Series B**, and the trigger is almost never internal. It is one of three external forcing functions: a SOC 2 Type II audit demanded by an enterprise prospect, a first regulated customer that imposes S5 obligations on a firm with no S5 infrastructure, or a public incident severe enough to impose reputational or legal cost. Until then, the verifier *is* the CTO.

For AI-native startups the timeline is different but less so than the public narrative suggests. Anthropic published the RSP at roughly Series C — late by lifecycle, early by capability. OpenAI's Safety and Security Committee was created reactively in mid-2024 after the Superalignment dissolution. Cohere's CAIO hire (Joelle Pineau, August 2025) coincided with its $500M raise and pivot toward regulated industries. Even AI-native firms add structure when commercial pressure or capability thresholds force it.

The transition is **never internally generated**. It is always pulled from the outside by a customer, regulator, investor, or failure. The most important finding for the framework: at S2, verification is an externality cost that someone else has to make visible before the firm pays it. (B)

---

## 3. Comparative Dimensions (D1-D10)

**D1 — Verification agent identity.** AI-using: CTO/co-founder with one or two informal reviewers; no separation between requester, verifier, and accountable party. AI-native: more distributed but still lean — Anthropic's Alignment Science / Frontier Red Team / Responsible Scaling Officer stack with Jared Kaplan as anchor. (A)

**D2 — Verification infrastructure.** AI-using: browser, GitHub, Slack, occasional spot-checks. Compliance automation (Vanta, Sprinto, Drata) appears at SOC 2 but covers security not reasoning; AI-specific platforms (Credo AI, Holistic AI) are priced for enterprises. AI-native: internal eval harnesses, automated red-teaming (Anthropic's Petri), capability evaluations against published thresholds, risk reports every 3-6 months. The infrastructure gap between AI-native and AI-using S2 firms is larger than the gap between AI-using S2 and a 5-person consultancy. (A/C)

**D3 — Verification incentive structure.** AI-using: negative incentive dominates; verification slows shipping and shipping is existential. AI-native: mixed — genuine commitment at Anthropic, but fragile under resource competition. OpenAI's Superalignment team dissolved May 2024 after Jan Leike and Ilya Sutskever left; Leike publicly noted they had been "sailing against the wind" for compute. (A)

**D4 — Sanction gradient.** AI-using: steepest in the seven-tier scale on a survival-percentage basis. Clearview AI's $100M+ aggregate GDPR fines halted EU operations. Character.AI faced wrongful death lawsuits, a Texas AG investigation, banned under-18 users November 2025, and entered mediation with Google January 2026. DoNotPay paid $193K plus advertising restrictions. AI-native: regulatory sanctions rare; investor sanctions immediate — Stability AI's board forced CEO Emad Mostaque out March 2024 with Lightspeed and Coatue as the de facto governance instrument. (A)

**D5 — Verification trigger.** Among AI-using firms, illustrative C-grade inferred shares: SOC 2 ~50%, regulated customer ~20%, investor diligence ~15%, public incident ~10%, founder-driven ~5%. **Founder-driven verification is the smallest category by far.** AI-native triggers: capability thresholds (Anthropic RSP), board committee briefings (OpenAI), enterprise customer requirements (Cohere), EU AI Act GPAI obligations (Mistral). Anthropic's RSP v1.0 (September 2023) is the only proactive case. (A)

**D6 — Per-decision verification budget.** AI-using: near-zero per product or content decision; T_verify/T_total ≈ (0.05-0.15, 1, 0-1). (C) AI-native: variance across decision types is diagnostic — routine deployment in minutes, capability evaluations in weeks, major releases through formal committee review at OpenAI under chair Zico Kolter. (B)

**D7 — Delegation chain depth.** AI-using: typically 1-2. AI-native: deeper but compressed — Anthropic's chain runs evaluation → red-team → Responsible Scaling Officer → board notification; OpenAI's Safety and Security Committee has explicit veto over major releases. Both flatter than S4 banks or S6 agencies. (A)

**D8 — Failure mode profile.** AI-using: passive acceptance, incident-triggered pseudo-governance, compliance theater, founder bottleneck. (B/C) AI-native: resource starvation (Superalignment), investor capture (Stability), structural restructuring (OpenAI), self-policing with limited external check — Anthropic's LTBT currently elects 1 of 5 directors, rising to 2/5 in July 2026 and 3/5 in November 2026; whether trustees use the growing authority is untested. (A/B)

**D9 — Substitutes.** AI-using: SOC 2 / ISO 27001 / ISO 42001 badges, Trust Centers, D&O and cyber insurance, indemnity clauses, output throttling, rate-limited access. AI-native: AISI partnerships, model cards and risk reports, third-party red-teaming, EU GPAI Code participation. Richer substitutes than Population B has access to, but still substitutes. (B)

**D10 — Scale-crossing dynamics.** Two dynamics: (i) S2 → S4 by acquisition or rapid scaling — a $500M+ round (Cohere August 2025), IPO, or acquisition forces governance rebuild within 6-12 months; the Pineau hire is a textbook S2→S4 marker. (ii) S2 → S5 by single contract — one enterprise sale to a regulated buyer reclassifies a 30-person startup into S5 verification obligations overnight while it retains S2 capacity. The most consequential scale-crossing dynamic, and the one most poorly handled by existing frameworks. (A/B)

---

## 4. Two-Population Split

The S2 headcount band conceals two populations whose verification realities are almost incommensurable.

### 4.1 Population A — AI-native startups

| Property | Pattern |
| --- | --- |
| Headcount / funding | 100-1,500 / Series B onward, many at multi-billion valuations |
| Verification innovation | High — RSP, LTBT, Safety and Security Committees, ASL standards |
| Per-decision budget | Low for routine output; weeks of structured eval for capability thresholds |
| External oversight | AISI partnerships, EU GPAI Code, voluntary disclosures |
| Sanction gradient | Investor-driven primarily; regulatory secondary |
| Failure mode | Resource starvation of safety teams, investor capture, restructuring |

Representative firms: Anthropic, OpenAI (in pre-2022 form), Cohere, Mistral, Stability AI (collapsed). Perhaps a dozen firms globally matter for capability frontier governance. Unrepresentative by count but disproportionately important because their decisions cascade through the S2 ecosystem.

### 4.2 Population B — AI-using startups

| Property | Pattern |
| --- | --- |
| Headcount / funding | 10-250 / pre-seed through Series C |
| Verification innovation | None — borrowed from SOC 2 and security compliance |
| Per-decision budget | Near zero |
| External oversight | Customers, auditors, occasional regulators |
| Sanction gradient | Existential per fine or lawsuit |
| Failure mode | Passive acceptance, founder bottleneck, compliance theater, incident-triggered governance |

Representative firms: Harvey AI, Cursor (Anysphere), Windsurf, Glean, Decagon, Sierra, hundreds of others. Y Combinator's 2025 batches concentrated nearly 50% of cohorts in agentic AI, showing production AI is shipping faster than governance frameworks can reach it. (B) Source: CB Insights coverage of YC Summer 2025.

### 4.3 What the split means

The two populations need different framework offerings. Population A needs scaffolding around capability evaluation, RSP-style commitments, and external red-teaming. Population B needs a *minimum viable verification routine* — structurally analogous to SOC 2 (a CTO can operationalize it without headcount) but specific to reasoning. Treating S2 as a single tier risks misapplying either pattern to the other.

---

## 5. Exemplar Cases

### 5.1 Anthropic (AI-native, frontier model builder)

Delaware PBC, ~1,200 employees, post-Series E. Most structured AI safety governance among AI-native startups: LTBT, RSP v3.0 (effective February 24, 2026), and ASL standards inspired by biosafety levels.

**Representative decision**: capability evaluation against an ASL-3 threshold for a frontier model release in 2025-2026.

**RVCS-1: 13/15.** Q1=3 (domain-appropriate evaluation, internal/external sources). Q2=3 (Frontier Red Team adversarial challenge, pre-deployment red-teaming). Q3=3 (RSP commitments mapped to NIST and EU GPAI Code). Q4=2 (adjusted against prior models and external benchmarks but not a known historical base rate). Q5=2 (cyber, CBRN, model autonomy catalogued internally but not against an external tier-appropriate catalog).

**VTI**: T_verify/T_total ≈ 0.50, N_reviewers ≈ 15-30, N_sources ≈ 20+ for a major capability cycle. Anthropic's safety team competes for compute with product teams (the same dynamic that broke Superalignment), but the budget is by far the highest in S2. (B)

**What this illustrates**: structured reasoning verification is *possible* at S2 scale only when verification is a corporate purpose rather than an obligation, capability evaluations are tied to public commitments, and the revenue model can absorb the cost. Anthropic is proof of existence, not a template for Population B.

Sources: [RSP v3.0](https://anthropic.com/responsible-scaling-policy/rsp-v3-0); [GovAI analysis](https://www.governance.ai/analysis/anthropics-rsp-v3-0-how-it-works-whats-changed-and-some-reflections); [LTBT](https://www.anthropic.com/news/the-long-term-benefit-trust).

### 5.2 Harvey AI (AI-using-and-building, legal vertical)

Founded 2022, valued at $11B in March 2026 after a $200M raise co-led by GIC and Sequoia. 50%+ of AmLaw 100 and 1,000+ customers in 60 countries. SOC 2 Type II, GDPR, ISO 27001. In March 2026 launched expanded enterprise governance controls: admin dashboards, Usage and Query History APIs, structured external request approval flows.

**Representative decision**: a senior associate at an AmLaw 100 firm uses Harvey to draft a memo on a novel point of securities law; Harvey returns a draft with citations.

**RVCS-1: 7/15** (for the step *as performed*, not what Harvey nominally enables). Q1=2 (citations to retrieval database), Q2=1 (internally consistent, no adversarial check; user expected to verify), Q3=1 (generic ethics statements, no per-output normative check), Q4=1 (disclaimers but no calibration against a known hallucination rate), Q5=2 (hallucination acknowledged in documentation; no per-decision failure catalog).

**VTI**: T_verify/T_total ≈ 0.10-0.25, N_reviewers = 1, N_sources = 2-5. The associate checks a handful of cited cases and ships to the partner. (C)

**What this illustrates**: a hybrid firm can build excellent governance *infrastructure* and still produce mid-range per-decision RVCS-1 scores, because verification ultimately depends on what the user does, not what the platform enables. Harvey's controls are structured for the buyer (AmLaw compliance) rather than the actual user (the associate at 11 PM on a deadline). Dominant pattern across AI-using S2 firms selling into regulated industries.

Sources: [Harvey governance controls — Blockchain.News, March 2026](https://blockchain.news/news/harvey-ai-enterprise-governance-controls-legal); [Harvey $11B — CNBC](https://www.cnbc.com/2026/03/25/legal-ai-startup-harvey-raises-200-million-at-11-billion-valuation.html).

### 5.3 Cursor / Anysphere (AI-using, code generation)

AI code editor, multi-billion-dollar valuation by 2026. Holds SOC 2; Windsurf leads in compliance breadth (SOC 2, HIPAA, FedRAMP, ITAR). Hundreds of thousands of developers whose verification obligations cascade upward from their employers.

**Representative decision**: an engineer at a 30-person Series A startup uses Cursor's agentic mode to refactor a payment-processing module; Cursor produces a multi-file diff.

**RVCS-1: 5/15.** Q1=1 (training data trusted implicitly), Q2=2 (reads diff, runs tests; empirical not adversarial), Q3=0 (no norm check on regulatory alignment for payment processing), Q4=1 (tests hedge but no calibration against Cursor's historical accuracy), Q5=1 (hallucination acknowledged informally, not catalogued).

**VTI**: T_verify/T_total ≈ 0.15-0.25, N_reviewers = 1-2 with code review, N_sources = 0-1. MIT/METR: experienced developers accept only ~44% of AI completions and spend ~9% of development time correcting AI output. (B)

**What this illustrates**: at the boundary between AI-using and AI-built-in, reasoning verification collapses into testing. The developer verifies whether the code runs, not the AI's reasoning. Q3 is essentially impossible to score above 0 for code agents because no native surface exists where regulatory reasoning enters the workflow. The framework needs separate treatment for code-generating AI.

Sources: [Cursor vs Windsurf 2026 — NxCode](https://www.nxcode.io/resources/news/windsurf-vs-cursor-2026-ai-ide-comparison).

---

## 6. The Lifecycle-Stage Model

The central analytical contribution. Maps the five verification disciplines against startup stages. **Standing** = named owner, documented routine, default invocation. **Ad hoc** = only when the founder or CTO remembers. **Absent** = not happening.

### 6.1 Population B (AI-using startups)

| Stage | Headcount | Q1 Source | Q2 Inference | Q3 Norm | Q4 Calibration | Q5 Failure |
| --- | --- | --- | --- | --- | --- | --- |
| Founding / Pre-seed | 1-5 | Absent | Ad hoc | Absent | Absent | Absent |
| Seed | 5-15 | Absent | Ad hoc | Absent | Absent | Ad hoc |
| Series A | 15-40 | Ad hoc | Ad hoc | Absent | Absent | Ad hoc |
| Series B | 40-100 | Ad hoc → Standing | Ad hoc | Ad hoc | Absent | Ad hoc → Standing |
| Series C | 100-250 | Standing | Ad hoc → Standing | Standing (regulated buyers) | Ad hoc | Standing |
| Late-stage | 250+ | Standing | Standing | Standing | Standing | Standing |

(B/C) Inferred from `startup-small-org-governance.md` §3.4, SOC 2 / ISO 42001 cost data, VC diligence data, and the failure cases.

The transition from ad hoc to standing practice is concentrated at the **Series B inflection point** — where SOC 2 Type II becomes a revenue gate, the first regulated customer typically arrives, and investors begin demanding AI ethics diligence. Before Series B, the only standing practices are inherited from security compliance, not native AI verification.

The disciplines do not activate together. Observed order: (1) Q5 failure mode awareness — first, during incident response; (2) Q1 source quality — second, driven by SOC 2 audit trails; (3) Q3 normative acceptability — third, driven by regulated customer requirements; (4) Q2 inferential validity — fourth, often only after a customer-visible mistake; (5) Q4 confidence calibration — last, frequently never reached at S2.

The lateness of Q4 is the most consequential finding. Calibration requires comparing AI output to a historical track record, which requires shipping enough decisions systematically enough to generate one. Most S2 firms do not run long enough or systematically enough to develop calibrated confidence before they exit to acquisition or scale into S4.

### 6.2 Population A (AI-native startups)

| Stage | Headcount | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- | --- |
| Pre-seed (research lab) | 5-20 | Standing (research norms) | Standing (research norms) | Ad hoc | Ad hoc | Standing |
| Seed → Series A | 20-100 | Standing | Standing | Ad hoc → Standing | Ad hoc | Standing |
| Series B+ | 100-500 | Standing | Standing | Standing | Ad hoc → Standing | Standing |
| Frontier deployment | 500-1,500 | Standing (with external review) | Standing | Standing (RSP-style) | Standing (capability evals) | Standing (frontier red team) |

(B) Anthropic research lab origins; comparable at Cohere and Mistral; OpenAI's pre-2022 governance.

AI-native startups inherit research-laboratory norms about source quality and inferential validity from day one because their founders are typically academic AI researchers. The disciplines that activate later are Q3 (what counts as an acceptable model release) and Q4 (capability metrics worth calibrating). The activation order is reversed from Population B.

### 6.3 The lifecycle gap

At every funding stage, the two populations operate at qualitatively different verification levels. A Population B Series A firm with 30 people may have *zero* disciplines as standing practice; a Population A research-lab-stage firm with 30 people will typically have *three or four*. The headcount band conceals a verification chasm the framework must explicitly address.

---

## 7. Transition Triggers

Listed in approximate order of prevalence among Population B firms.

**SOC 2 Type II customer requirement** (late Series A - Series B). ~83% of enterprise buyers now require SOC 2 (Vanta 2025). SOC 2 does not test reasoning, but the audit creates standing practices around access control, change management, and incident response that can be repurposed for reasoning verification with marginal effort. (A)

**First regulated-industry customer** (often Series A-B). A sale to a financial institution, healthcare provider, or government agency imposes vendor risk management on model bias, training data provenance, hallucination rates, and human-in-the-loop controls. Forces the firm to articulate verification practices in writing for the first time, often surfacing the absence of any. (B)

**Series B investor diligence**. 68% of VC firms now include AI ethics in due diligence (PitchBook 2026, cited in `governance-trend-analysis.md` §3.4 — graded B). Forces founders to commit governance investment as a use of funds or accept a valuation discount. (B)

**First public incident** (any stage). The Character.AI sequence (Setzer suicide → Texas AG investigation → minor ban → mediation) is canonical. Whether the response becomes standing practice or theater depends on whether the incident produced lasting revenue damage. (A)

**EU AI Act exposure**. Prohibited practices (February 2025), GPAI obligations (August 2025), high-risk system obligations (originally August 2026, proposed delay to December 2027/August 2028 under the Digital Omnibus on AI). Forces risk-tier classification and documentation that approximates verification artifacts. (A)

**First AI ethics or governance hire** (Series B or later). Rare. McKinsey July 2024: 13% hired AI compliance specialists and only 6% hired AI ethics specialists in the past year. (B)

**Capability threshold (Population A only).** Anthropic's RSP commits to ASL-level safeguards before training or deploying corresponding models; ASL-3 was activated May 2025. (A)

**Clustering observation**: Population B triggers cluster temporally around the Series B raise. SOC 2, first regulated customer, investor diligence, and often the first incident all tend to land within ~6 months of the Series B close. They are not independent events distributed uniformly; they cluster.

---

## 8. Counterexamples and Governance Collapse Cases

**Stability AI (Population A collapse).** CEO Emad Mostaque resigned March 2024 after months of pressure from Coatue and Lightspeed; their board members then resigned. Three of five original Stable Diffusion researchers had already left; the company was burning ~$8M/month against a failed $4B raise. Interim co-CEOs ran the firm until Prem Akkaraju (former Weta Digital) became permanent CEO June 2024. (A) Without internal governance structure, investor power became the de facto mechanism. Research-lab verification practices collapsed when the research team itself collapsed.

**Humane (Population B collapse, hardware variant).** Humane AI Pin launched April 2024 with widespread negative reviews — reliability, overheating, battery, and use-case validation failures. By February 2025 Humane sold to HP for $116M (against a sought $750M-1B in May 2024) and shut down its servers, bricking devices on 10 days' notice. (A) The "ship without verification" mode in extreme form: no structured pre-launch reasoning verification on the AI Pin's user-experience claims. Q5 absent, compounded by Q4 (founders believed their own demos).

**Character.AI (Population B governance vacuum).** Lawsuits filed October 2024 (Megan Garcia case after the suicide of her 14-year-old son) and 2025 (13-year-old Colorado girl). Texas AG investigation November 2024. Banned under-18 open-ended conversations effective November 24, 2025. Mediation with Google on wrongful death lawsuits January 2026. (A) The clearest Q3 failure at S2 scale. Engagement-maximization design in companion chatbots had no observable normative check until lawsuits and regulators forced one.

**Pattern.** Each case shows the same structural feature: governance was absent until an external party forced its creation, and by then the cost was existential. The cases differ in whether the external party was an investor, the market, or a regulator/litigant. **Governance at S2 is reactive.** This is the central failure mode the framework must address.

---

## 9. Known Failures and Incidents

| Year | Firm | Failure class | Q skipped | Sanction |
| --- | --- | --- | --- | --- |
| 2024 | DoNotPay | Misapplication, fabrication | Q1, Q2, Q3 | $193K FTC, advertising restriction |
| 2024 | Clearview AI | Misapplication (data protection) | Q3 | $100M+ GDPR, EU operations halted |
| 2024 | Character.AI | Specification gaming | Q3, Q5 | Wrongful death lawsuits, Texas AG |
| 2024 | Stability AI | Governance failure | Q3, Q4, Q5 | CEO ouster, board reset |
| 2024 | Nate Inc. | Fabrication (AI-washing) | Q3 | SEC fraud charges, $42M raise misrepresented |
| 2024 | Humane AI Pin | Overconfidence | Q4, Q5 | Sold for $116M; product shutdown |
| 2024 | Perplexity AI | Misapplication (copyright) | Q3 | NYT, Yomiuri ($14.7M), Amazon C&D |
| 2024 | Cleo AI | Misapplication (consumer protection) | Q3 | $17M FTC settlement |
| 2024 | Workado | Fabrication (false claims) | Q1, Q4 | FTC settlement |
| 2024 | Evolv Technologies | Overconfidence | Q4 | FTC ban on unsubstantiated claims |
| 2024 | OpenAI Superalignment | Resource starvation | Q5 (org) | Talent loss, public trust damage |
| 2025 | Character.AI (second death) | As above | Q3, Q5 | Compounded litigation |

(A) case sources cited in `startup-small-org-governance.md` §9; (B) FICS-1 mapping is inferred.

The corpus is dominated by Q3 (normative acceptability) failures — the discipline that asks "should we do this at all?" Q4 is second most common. Q1 and Q2 failures appear in the more technical incidents but are less frequent, suggesting **most S2 incidents are not technical reasoning failures but normative reasoning failures**.

---

## 10. Open Questions

1. **Actual VTI distribution at S2.** Triples here are inferred from qualitative evidence; a diary study at 5-10 Population B firms would close the gap.
2. **Geographic generality.** Evidence is heavily US/EU-weighted. Korea's AI Basic Act (force January 2026) and Asian/Latin American S2 patterns are unstudied.
3. **S2 firms that never raise Series B.** The lifecycle model assumes a venture-funded path. Bootstrapped and profitable indie SaaS firms may never face the SOC 2 trigger.
4. **Stability of the 68% VC AI ethics diligence figure.** Widely reproduced but methodology unclear. Primary-source check needed.
5. **Population A → S4 transition.** Anthropic's 2/5 LTBT board control in July 2026 and 3/5 in November 2026 is a natural experiment, as is Cohere's post-Pineau pivot.
6. **Q5 and incident frequency.** Collapse cases all show Q5 absence before incident, but Q5 may be a consequence rather than a cause of prevention.
7. **Do code-generation tools collapse Q3 to zero by structural design?** The Cursor exemplar suggests yes; if true, this category needs separate framework treatment.
8. **Reasoning verification as a distinct discipline.** Startups talk about "responsible AI" broadly but rarely isolate reasoning verification specifically. This report reconstructed it from adjacent governance and compliance evidence rather than native S2 practice. The absence is itself a finding.

---

## 11. Sources

**Primary repository sources**
- `research/extensions/adaptive-governance/startup-small-org-governance.md`
- `research/extensions/adaptive-governance/governance-trend-analysis.md`
- `research/extensions/market-research/ai-adoption-barriers-verified-findings.md`
- `research/operations/expansion/scale-based-reasoning-trust-research-plan.md`

**Anthropic / OpenAI / Cohere / Stability / Mistral**
- [Anthropic RSP v3.0 (effective Feb 24, 2026)](https://anthropic.com/responsible-scaling-policy/rsp-v3-0)
- [Anthropic LTBT](https://www.anthropic.com/news/the-long-term-benefit-trust); [GovAI RSP v3.0 analysis](https://www.governance.ai/analysis/anthropics-rsp-v3-0-how-it-works-whats-changed-and-some-reflections); [Activating ASL-3, May 2025](https://www.anthropic.com/news/activating-asl3-protections)
- [LTBT — Harvard Law CorpGov](https://corpgov.law.harvard.edu/2023/10/28/anthropic-long-term-benefit-trust/); [LTBT critique — EA Forum](https://forum.effectivealtruism.org/posts/JARcd9wKraDeuaFu5/maybe-anthropic-s-long-term-benefit-trust-is-powerless)
- [OpenAI Safety and Security Committee](https://openai.com/index/openai-board-forms-safety-and-security-committee/); [Safety practices update](https://openai.com/index/update-on-safety-and-security-practices/); [Kolter — AP via WRIC](https://www.wric.com/news/u-s-world/ap-who-is-zico-kolter-a-professor-leads-openai-safety-panel-with-power-to-halt-unsafe-ai-releases/); [Superalignment dissolution — CNBC](https://www.cnbc.com/2024/05/17/openai-superalignment-sutskever-leike.html)
- [Cohere hires Pineau as CAIO — TechCrunch, August 2025](https://techcrunch.com/2025/08/14/cohere-hires-long-time-meta-research-head-joelle-pineau-as-its-chief-ai-officer/); [Stability AI CEO resigns — TechCrunch, March 2024](https://techcrunch.com/2024/03/22/stability-ai-ceo-resigns-because-youre-not-going-to-beat-centralized-ai-with-more-centralized-ai/); [Mistral and EU AI Code of Practice](https://euperspectives.eu/2025/07/mistral-and-openai-back-eu-ai-code-of-practice/)

**Harvey, Cursor, YC, compliance**
- [Harvey governance controls — Blockchain.News, March 2026](https://blockchain.news/news/harvey-ai-enterprise-governance-controls-legal); [Harvey $11B — CNBC, March 2026](https://www.cnbc.com/2026/03/25/legal-ai-startup-harvey-raises-200-million-at-11-billion-valuation.html)
- [Cursor vs Windsurf 2026 — NxCode](https://www.nxcode.io/resources/news/windsurf-vs-cursor-2026-ai-ide-comparison); [YC Summer 2025 — CB Insights](https://www.cbinsights.com/research/y-combinator-summer2025/)
- [SOC 2 for AI startups — Comp AI](https://trycomp.ai/soc-2-for-ai-companies); [ISO 42001 for startups — Workstreet](https://www.workstreet.com/blog/iso-42001-for-startups); [ISO 42001 timeline — Elevate](https://elevateconsult.com/insights/iso-42001-certification-timeline-budget-for-founders/)

**Failure / collapse cases**
- [Character.AI lawsuits — SMVLC](https://socialmediavictims.org/character-ai-lawsuits/); [Character.AI bans minors — NBC](https://www.nbcnews.com/tech/tech-news/characterai-bans-minors-response-megan-garcia-parent-suing-company-rcna240985); [Character.AI / Google settle — CNN, January 2026](https://www.cnn.com/2026/01/07/business/character-ai-google-settle-teen-suicide-lawsuit)
- [Humane AI Pin discontinued — TechCrunch, February 2025](https://techcrunch.com/2025/02/18/humanes-ai-pin-is-dead-as-hp-buys-startups-assets-for-116m/); [Clearview AI Dutch fine — TechCrunch](https://techcrunch.com/2024/09/03/clearview-ai-hit-with-its-largest-gdpr-fine-yet-as-dutch-regulator-considers-holding-execs-personally-liable/)
- [FTC DoNotPay order](https://www.ftc.gov/news-events/news/press-releases/2025/02/ftc-finalizes-order-donotpay-prohibits-deceptive-ai-lawyer-claims-imposes-monetary-relief-requires); [FTC Operation AI Comply — Benesch](https://www.beneschlaw.com/insight/one-year-in-ftcs-operation-ai-comply-continues-under-new-administration-signaling-enduring-enforcement-focus/)

**VC / baselines**
- [VC responsible AI tools — Project Liberty](https://www.projectliberty.io/news/venture-capital-tools-for-responsible-and-impactful-investment-in-ai/); [PitchBook 2026 US VC Outlook](https://pitchbook.com/news/reports/2026-us-venture-capital-outlook)
- Stanford RegLab — Hallucinating Law (via `ai-adoption-barriers-verified-findings.md`); MIT/METR 2025 AI code acceptance study (via 2026 IDE benchmarking coverage)
