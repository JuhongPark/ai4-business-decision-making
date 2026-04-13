# Tier S6 — National Governments and Public Agencies

status: research_in_progress
tier: S6
date: 2026-04-13

---

## 1. Tier Definition and Scope

Tier S6 covers organizations exercising sovereign or delegated public authority at the national level: federal cabinet departments (US DHS, UK Home Office, Korea MSIT), federal regulatory agencies (SEC, FDA, BaFin), benefits and tax administrations (IRS, Belastingdienst, Services Australia), central banks (Fed, BoE, ECB, BoK), supreme audit institutions (GAO, NAO, ANAO), and national digital service agencies (GDS, Estonia RIA, Singapore GovTech). Decisions bind citizens, allocate public funds, or affect statutory rights, so verification operates as an *accountability-to-the-public problem*. Excluded: subnational governments (S5), supranational institutions (S7), private contractors, and classified national-security systems.

S6 inherits the strongest formal apparatus on paper — administrative procedure law, FOIA, procurement statutes, parliamentary oversight, supreme audit — but those instruments were built to capture *decisions and documents*, not *inferential chains*. The core question is whether that legacy infrastructure can be retrofitted to inspect AI reasoning.

---

## 2. Core Question Answered

**Does existing administrative review infrastructure (impact assessments, procurement review, FOIA audit trails) create a native surface for reasoning verification, or does it only capture outputs while leaving inferential chains invisible?**

**Short answer**: it creates a *partial* native surface — strong on system inventory, procurement documentation, and ex ante impact assessment, weak on per-decision reasoning capture. The administrative state in 2026 has built a dense ex ante regime (UK ATRS, US OMB M-25-21 use-case inventories, EU AI Act FRIA, Korea AI Basic Act high-impact category) but the chain linking a model's output to a civil servant's adopted reasoning is mostly invisible to FOIA and audit. The Dutch Toeslagenaffaire and Australian Robodebt confirm the diagnosis: review caught errors years late, never inspected reasoning, and only surfaced through litigation and royal commissions. **(Grade B)**

The gap is precise. Administrative review captures three of four verification dimensions: source quality via procurement documentation **(B)**, normative fit via fundamental-rights / equality impact assessments **(A, EU AI Act Art. 27)**, and failure-mode awareness via post-deployment monitoring **(A, OMB M-25-21)**. It captures the fourth — inferential validity at the level of a specific decision affecting a specific citizen — only indirectly. FOIA can produce model output and input data, but reproducing the reasoning that justified treating that output as authoritative requires logging few agencies maintain. **(Grade C)**

---

## 3. Comparative Dimensions

### D1 — Verification agent identity

Verification at S6 is distributed across at least five roles, each with distinct legal basis: procurement / contracting officers verifying vendor documentation under FAR / PPN / EU procurement directives **(A)**; Chief AI Officers (CAIOs) and AI Governance Boards mandatory at CFO Act agencies under OMB M-24-10 and the retained M-25-21 **(A)**; data-protection and equality officers under GDPR Art. 35 and EU AI Act Art. 27 **(A)**; supreme audit institutions (GAO, NAO, ANAO, Bundesrechnungshof) performing ex post audits **(A)**; and the public performing reactive verification through FOIA and parliamentary questions **(B)**.

The civil servant who actually pastes a citizen file into an AI tool and adopts its suggestion is rarely the formally accountable agent. This is the central role-confusion at S6: the OECD *Governing with AI* (September 2025) explicitly states that "a human user (which in government means a civil servant) is expected to review, verify and perhaps build on" AI content, but no jurisdiction defines what that per-decision verification must comprise. **(A — OECD 2025)**

### D2 — Verification infrastructure

S6 has the densest verification infrastructure of any tier, but most is *system-level*, not *decision-level*.

System-level instruments **(A)**: US federal AI use case inventory (annual consolidation since 2022; agency `[agency.gov]/ai` pages under M-25-21); UK Algorithmic Transparency Recording Standard (ATRS), mandatory for central government and frontline ALBs since 2024, with Tier-1 plain-language and Tier-2 technical records published centrally; EU Annex III high-risk AI registry, with member-state notification required from August 2026; Korea high-impact AI register under the AI Basic Act effective 22 January 2026; Singapore AI Verify open-source toolkit (generative-AI update 29 May 2025) and the Global AI Assurance Pilot (February 2025).

Decision-level instruments are sparser: the FRIA template required by EU AI Act Art. 27(5), unpublished in final form as of early 2026 **(B)**; the US APA reasoned-decision requirement (5 USC §706), applied to AI-informed decisions only by analogy **(C)**; agency-internal audit logs not designed to be FOIA-readable **(C — MuckRock's May 2025 finding that only one of more than a dozen FOIA requests for agency AI tooling produced a substantive response within four months)**.

### D3 — Verification incentive structure

Civil-service incentives actively work against thorough per-decision verification. Frontline officers are rewarded for caseload throughput; verifying an AI suggestion is unmeasured and unbillable. The Toeslagenaffaire showed that tax officers escalated risk flags upward without training or incentive to question the algorithmic basis **(B — Dutch parliamentary inquiry)**. Senior officials face career and political risk if high-profile failures emerge, which explains the recent wave of CAIO appointments **(B — OECD 2025)**. There is no positive reward for catching errors before harm: Services Australia executives knew the Robodebt income-averaging assumption was contested but proceeded for political reasons; the Royal Commission's criminal referrals are the only material counter-incentive **(A)**. The result funds elaborate ex ante review and disincentivises per-decision review.

### D4 — Sanction gradient

S6 has the steepest theoretical sanction gradient of any tier, but it is back-loaded. Available sanctions, softest to hardest **(A unless noted)**: internal performance review and CAIO escalation **(B)**; supreme audit institution findings (GAO recommendations, NAO value-for-money judgements) — non-binding but politically costly; parliamentary or congressional hearings **(B)**; judicial review under APA / UK judicial review / EU Charter Art. 47, which can quash decisions; sectoral regulatory enforcement (data protection, equality, banking supervision); EU AI Act administrative fines up to EUR 15 million or 3 percent of global turnover for FRIA non-compliance applicable to public bodies under member-state implementation **(A — EU AI Act Art. 99)**; royal commission, criminal referral, or political resignation (Robodebt and Toeslagenaffaire both reached this level).

The gap is the absence of routine low-severity per-decision sanctions. Either nothing happens, or it becomes a national scandal. There is no S6 equivalent of a private-firm internal warning followed by a corrective action plan, because civil-service due-process protections slow day-to-day discipline and political consequences make scandalous failures career-ending.

### D5 — Verification trigger

S6 verification is triggered by four mechanisms in descending volume **(A)**: procurement-cycle (every acquisition above a statutory threshold forces vendor documentation review); periodic-inventory (annual update under M-25-21, ATRS, or equivalent); complaint (FOIA, ombudsman, parliamentary question, ECHR application); incident (media, judicial finding, audit finding). Crucially missing: a *per-use* trigger. A civil servant who pastes a citizen file into a generative-AI tool and adopts the suggested response triggers no verification mechanism unless they self-flag or the use later becomes the subject of a complaint. The OECD 2025 report identifies this as the central operational gap in public-sector AI governance. **(A — OECD 2025)**

### D6 — Per-decision verification budget

The per-decision budget is structurally low for high-volume operational decisions (benefits eligibility: minutes per case, with shared standard procedures) and high for high-visibility policy decisions (regulatory enforcement: hours to weeks; rulemaking: weeks to years). Because the cost is essentially salaried civil-servant time, the upper bound on depth is set by political attention rather than by money. A decision affecting one obscure firm gets less verification than the same decision applied to a politically salient population. **(C — inferred from workload data)**

VTI estimates **(C)**: high-volume benefits adjudication with AI assistance — T_verify / T_total ≈ 0.1 to 0.2, N_reviewers ≈ 1 case officer, N_sources ≈ 2 to 4. Regulatory enforcement — T_verify / T_total ≈ 0.4 to 0.6, N_reviewers ≈ 3 to 8 across legal / technical / economic divisions, N_sources often 10+.

### D7 — Delegation chain depth

S6 has the deepest delegation chain of any tier surveyed so far. A typical chain for an AI-informed eligibility decision runs: minister → permanent secretary → divisional director → branch chief → case officer → AI tool (vendor model + agency config) → vendor's foundation-model provider → underlying training data and infrastructure provider. Seven to nine links. Each can deflect accountability. The Robodebt Royal Commission found the income-averaging methodology was repeatedly flagged by officers and lawyers but blocked from reaching ministers, and ministers later denied awareness. The chain itself becomes a reasoning-verification failure mode, distinct from any technical model failure. **(A — Robodebt Royal Commission)**

The vendor link is increasingly important because three cloud providers now hold 60+ percent of public-sector cloud and AI provision globally **(A — NAO *Government's Approach to Technology Suppliers*, January 2025)**. This creates a verification chokepoint: agencies cannot inspect underlying models, and procurement-law verification stops at contractual representations.

### D8 — Failure mode profile

S6 failures cluster in five patterns: **discriminatory targeting** — model uses protected characteristics or proxies to flag disfavoured groups (Toeslagenaffaire's use of dual nationality as a fraud risk feature) **(A)**; **statistical overreach to individuals** — population-level patterns applied to individual cases without legal basis (Robodebt income averaging) **(A)**; **reasoning erasure under FOIA** — audit trails record only the final decision, so a citizen requesting the basis cannot see the AI's contribution **(C — MuckRock 2025)**; **procurement capture** — agency depends on a single vendor whose model it cannot inspect or replace **(B — NAO 2025)**; **scandal-cycle failure** — review activates only after national scandal, by which point harm is irreversible **(A)**.

A sixth emerging mode is *generative drift in policy drafting*: civil servants using UK Redbox / Humphrey, US generative pilots, or Bürokratt may inherit hallucinated citations into briefings. No published cabinet-level incident as of April 2026, but foreseeable. **(D — speculative)**

### D9 — Substitutes when full verification is infeasible

When per-decision verification is infeasible, S6 substitutes are: categorical bans (EU AI Act prohibited practices, in force February 2025) **(A)**; risk classification triage (NIST AI RMF, EU AI Act, Korea AI Basic Act) **(A)**; pre-deployment testing batteries (Singapore AI Verify, UK AISI frontier-model evaluations, US AI Safety Institute, status uncertain post-January 2025) **(A)**; human-in-the-loop requirements (EU AI Act Art. 14, OMB M-25-21 minimum practices, UK Cabinet Office Humphrey guidance), often rhetorical **(B)**; sunset and review clauses **(A)**; public consultation as process legitimacy substitute for reasoning verification **(C)**. The dominant substitute pattern is: heavy ex ante process + human-in-the-loop fig leaf + reactive scandal handling.

### D10 — Scale-crossing dynamics

**Downward** to S5 / S4 / S3: federal procurement and AI standards reshape what state agencies, NGOs, and contractors can deploy. M-25-21 cascades through grant conditions; EU AI Act high-risk classifications cascade through national implementing law to municipalities and SMEs **(A)**. **Upward** to S7: national governments coordinate at OECD, G7 Hiroshima Process, Council of Europe, UN; standards adopted at S7 become anchors S6 governments implement. The Council of Europe Framework Convention on AI (signature open September 2024) is one example **(A)**. **Sideways**: EU AI Act extraterritoriality, Korea's foreign-representative requirement, and Singapore's Global AI Assurance Pilot push partial convergence **(B)**. **Vendor-mediated**: the same three cloud and foundation-model providers serve dozens of S6 agencies; a failure in one jurisdiction can be a known weakness everywhere, but vendor NDAs typically prevent agencies from sharing findings with peers — the most under-appreciated cross-scale dynamic at S6 **(C)**.

---

## 4. Exemplar Cases

### Exemplar 1 — UK Algorithmic Transparency Recording Standard (ATRS) deployment

The UK's ATRS, mandatory for central government departments and frontline ALBs since 2024, requires a Tier-1 plain-language record and a Tier-2 technical record for any algorithmic tool with significant influence on a decision-making process with public effect. By mid-2025 the central register held 26 records from central departments and 10 from devolved and local government. **(A — Data in Government Blog 8 May 2025; gov.uk ATRS Hub)** Representative case: Department for Work and Pensions advanced analytics for fraud risk scoring.

RVCS-1 (representative DWP fraud risk-scoring entry): Q1 Source quality 2 (vendor and dataset documented; model internals limited); Q2 Inferential validity 1 (technical methodology described, per-decision reasoning not captured); Q3 Normative acceptability 2 (equality impact assessment public); Q4 Confidence calibration 1 (aggregate metrics only); Q5 Failure mode awareness 2 (incident reporting and review schedule recorded). **Total: 8 / 15.**

VTI (single fraud-flag decision): T_verify / T_total ≈ 0.15; N_reviewers = 1 case officer (periodic supervisor sample); N_sources = 3 to 5. **(C)**

Comment: the world's most ambitious system-level transparency instrument, but 8/15 shows even best-in-class S6 transparency captures inputs and outputs without per-decision reasoning capture.

### Exemplar 2 — Singapore AI Verify Foundation Global Assurance Pilot

Launched February 2025, the Global AI Assurance Pilot pairs deploying organisations (including Singapore public agencies and partner jurisdictions) with independent testers to validate generative-AI applications against AI Verify's eleven principles (transparency, explainability, robustness, fairness, accountability, human agency, and others). The Foundation has nine premier members (AWS, Dell, Google, IBM, IMDA, Microsoft, Red Hat, Resaro, Salesforce) and 180+ general members. **(A — IMDA 29 May 2025; AI Verify Foundation)** Representative case: a generative AI policy-drafting assistant used by a Singapore ministry.

RVCS-1 (representative pilot): Q1 Source quality 3 (third-party verified data lineage); Q2 Inferential validity 2 (process-level, not per-decision); Q3 Normative acceptability 2 (principles include fairness, thresholds deployer-set); Q4 Confidence calibration 2 (standardised but context-dependent); Q5 Failure mode awareness 3 (red-team and adversarial testing required). **Total: 12 / 15.**

VTI (the pilot itself): T_verify / T_total ≈ 0.7; N_reviewers = 2 to 4 (deployer + independent tester team); N_sources = 6 to 10. **(C)**

Comment: closest current S6 instrument to structured reasoning verification, scoring 12/15, but operates at application level not per-decision, and depends on voluntary participation.

### Exemplar 3 — US OMB M-25-21 federal high-impact AI minimum practices

OMB Memorandum M-25-21 (3 April 2025) replaced M-24-10 and shifted federal AI policy toward a pro-innovation posture while retaining a `high-impact AI` category requiring minimum risk-management practices. CFO Act agencies must designate a CAIO, convene an AI Governance Board, maintain an updated AI use case inventory, and apply minimum practices to high-impact uses. Pre-existing high-impact uses must comply by 3 April 2026 or be discontinued. **(A — OMB M-25-21; White House 7 April 2025)** Representative case: a DHS high-impact screening assistance tool flagged in the agency's published inventory.

RVCS-1 (representative DHS high-impact tool): Q1 Source quality 2 (vendor and procurement record; foundation-model details limited); Q2 Inferential validity 1 (system-level evaluation; per-decision reasoning not captured); Q3 Normative acceptability 2 (privacy and civil-liberties review preserved); Q4 Confidence calibration 1 (use-case-level performance only); Q5 Failure mode awareness 2 (CAIO / governance board escalation channel). **Total: 8 / 15.**

VTI (single screening decision): T_verify / T_total ≈ 0.1; N_reviewers = 1 to 2; N_sources = 3 to 6. **(C)**

Comment: the most consequential current US federal framework, but the matching 8/15 score with ATRS suggests the structural reasoning-verification gap is policy-design-shaped, not country-shaped.

---

## 5. Counterexamples

**Dutch Toeslagenaffaire (childcare benefits scandal)**: Between 2013 and 2019, the Dutch Tax and Customs Administration used machine-learning fraud risk models that incorporated dual nationality as a feature and disproportionately flagged families with Caribbean and Surinamese heritage. Approximately 26,000 families (estimates up to 35,000) were ordered to repay childcare benefits at EUR 20,000 to 60,000 per family; more than 2,000 children were placed in state care as a downstream consequence. The scandal forced the resignation of the Rutte cabinet in January 2021. The parliamentary inquiry confirmed that no routine administrative review caught the discriminatory model design — the issue surfaced through investigative journalism and litigation, and the reasoning chain from feature selection to risk score to enforcement action was not visible to FOIA-style requests in any actionable form. **(A — Dutch parliamentary inquiry, NJCM litigation record, Lighthouse Reports)**

**Australian Robodebt scheme**: From July 2016 to November 2019, Services Australia ran an automated Online Compliance Intervention scheme that calculated debts by averaging ATO annual income data across fortnightly Centrelink reporting periods — statistically and legally invalid. Debt notices were issued to 433,000 individuals; AUD 746 million was wrongfully recovered before class action and government write-offs totalling AUD 1.75 billion. The Royal Commission (July 2023) called Robodebt `a costly failure of public administration` and referred individuals for prosecution, finding that internal warnings from officers and lawyers had been suppressed and that ministers later denied awareness. Standard administrative review entirely failed; only a royal commission with statutory powers reconstructed the reasoning chain. **(A — Royal Commission Final Report July 2023)**

Both confirm that existing administrative infrastructure does not natively capture inferential chains. System-level documentation existed in some form, but the model's actual reasoning — feature weights, decision thresholds, propagation of statistical assumptions to individual files — was reconstructed only after years of harm and only by extraordinary investigatory bodies. A milder counterexample is the **US `AI Bill of Rights`** (October 2022 White House blueprint, never converted into binding regulation, effectively superseded by EO 14179 and OMB M-25-21), showing how S6 verification ambitions can evaporate across administration changes. **(A)**

---

## 6. Known Failures / Incidents

Beyond the two counterexamples:

- **France CNAF allocations familiales risk scoring (ongoing)**: family-allowance fund's risk-scoring algorithm criticised by La Quadrature du Net and Amnesty International for disproportionately targeting low-income and disabled claimants; Conseil d'État litigation unresolved as of early 2026. **(B)**
- **Spain VioGen domestic-violence risk scoring**: police use of the VioGen tool linked in journalism and academic critique to under-classification of victims who later experienced lethal violence; reform ongoing. **(B)**
- **US IRS audit selection algorithm**: long-standing concern that algorithmic selection disproportionately audited Earned Income Tax Credit recipients; partially addressed by internal review 2023-2024. **(B — Stanford IPL)**
- **UK Home Office visa streaming tool**: withdrawn August 2020 after Joint Council for the Welfare of Immigrants legal challenge alleging racial discrimination in visa triage. **(A)**
- **MuckRock FOIA tracking, May 2025**: of more than a dozen FOIA requests filed in January 2025 about agency AI tooling, only one (US Consumer Product Safety Commission) had produced a substantive response by May 2025 — illustrating the FOIA-AI gap empirically. **(B)**

---

## 7. Open Questions

1. **Per-decision logging standards**: no jurisdiction has yet defined a minimum logging schema that would let a citizen FOIA-request `the AI-generated content that influenced this specific decision`. At what tier should it be regulated — national procurement, EU AI Office implementing regulation, ISO?
2. **CAIO role definition**: the Chief AI Officer role exists in US federal practice but substantive responsibilities, sanction powers, and verification accountabilities remain underdefined. Operations role, compliance role, or quasi-judicial reasoning auditor?
3. **Vendor model inspection rights**: can procurement law compel access to vendor model internals for verification without destroying vendor viability? Singapore's testing sandbox and EU AI Act Art. 92 evaluation-access provisions are two routes.
4. **Generative drift in policy drafting**: Redbox / Humphrey, US generative pilots, and Bürokratt are now embedded in brief-drafting workflows. What is the empirical incidence of hallucinated citations surviving into final ministerial decisions?
5. **Cross-jurisdictional reasoning equivalence**: when a multinational vendor's same model informs decisions in 20 S6 jurisdictions, do divergent verification standards create inconsistency, or defence in depth?
6. **Central bank verification**: central banks now use generative AI for code translation, research drafting, and market monitoring (Fed Governor Waller February 2026; ECB; BoE econdat). Should monetary-policy-adjacent uses receive a regime distinct from general civil-service use?
7. **What replaces the US AI Safety Institute?**: AISI's status under the post-January 2025 administration is unclear; UK rebranded its institute to AI Security Institute in February 2025. Is the institutional verification anchor migrating from federal labs to national-security-coded bodies?

---

## 8. Sources

### Primary

- US GAO, [GAO-25-107933 *Federal AI Efforts Guided by Requirements and Advisory Groups*](https://www.gao.gov/products/gao-25-107933), September 2025
- US GAO, [GAO-25-107653 *Generative AI Use and Management at Federal Agencies*](https://www.gao.gov/assets/gao-25-107653-highlights.pdf)
- OMB, [M-25-21 *Accelerating Federal Use of AI*](https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf), 3 April 2025
- Federal Register, [EO 14179 *Removing Barriers to American Leadership in AI*](https://www.federalregister.gov/documents/2025/01/31/2025-02172/removing-barriers-to-american-leadership-in-artificial-intelligence), 23 January 2025
- ombegov, [2025 Federal Agency AI Use Case Inventory](https://github.com/ombegov/2025-Federal-Agency-AI-Use-Case-Inventory)
- OECD, [*Governing with Artificial Intelligence*](https://www.oecd.org/en/publications/governing-with-artificial-intelligence_795de142-en/full-report.html), September 2025
- OECD.AI, [Algorithmic Transparency in the Public Sector](https://wp.oecd.ai/app/uploads/2025/05/algorithmic-transparency-in-the-public-sector.pdf), May 2025
- European Commission, [AI Act overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai); EU AI Act, [Article 27 FRIA](https://artificialintelligenceact.eu/article/27/)
- UK GOV.UK, [ATRS Hub](https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub); [Making ATRS mandatory](https://dataingovernment.blog.gov.uk/2025/05/08/making-the-algorithmic-transparency-recording-standard-atrs-mandatory-across-government/), 8 May 2025
- UK NAO, [*Use of AI in Government*](https://www.nao.org.uk/wp-content/uploads/2024/03/use-of-artificial-intelligence-in-government.pdf), March 2024; [*Government's Approach to Technology Suppliers*](https://www.nao.org.uk/wp-content/uploads/2025/01/governments-approach-to-technology-suppliers-addressing-the-challenges.pdf), January 2025
- UK AISI, [Our 2025 year in review](https://www.aisi.gov.uk/blog/our-2025-year-in-review)
- IMDA Singapore, [New Model AI Governance Framework for Agentic AI](https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2026/new-model-ai-governance-framework-for-agentic-ai), 22 January 2026; [AI Verify Foundation](https://aiverifyfoundation.sg/what-is-ai-verify/)
- Korea, [Framework Act on AI Development and Trust](https://law.go.kr/lsInfoP.do?lsiSeq=268543&lsId=014820&urlMode=engLsInfoR&viewCls=engLsInfoR&efYd=20260122); CSET Georgetown, [translation](https://cset.georgetown.edu/wp-content/uploads/t0625_south_korea_ai_law_EN.pdf)
- Estonia RIA, [Bürokratt](https://www.ria.ee/en/state-information-system/personal-services/burokratt)
- Federal Reserve, [Waller on operationalizing AI at the Fed](https://www.federalreserve.gov/newsevents/speech/waller20260224a.htm), 24 February 2026; [Barr on AI and innovation](https://www.federalreserve.gov/newsevents/speech/barr20251111a.htm), 11 November 2025

### Counterexamples

- [Dutch childcare benefits scandal (Wikipedia)](https://en.wikipedia.org/wiki/Dutch_childcare_benefits_scandal); Lighthouse Reports, [The Algorithm Addiction](https://www.lighthousereports.com/investigation/the-algorithm-addiction/)
- Royal Commission into the Robodebt Scheme, [Report](https://robodebt.royalcommission.gov.au/publications/report), July 2023; [Government Response](https://www.pmc.gov.au/sites/default/files/resource/download/gov-response-royal-commission-robodebt-scheme.pdf), November 2023

### Secondary

- Akin, [GAO on Federal Generative AI](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/gao-issues-report-on-generative-ai-use-and-management-at-federal-agencies); FedScoop, [AI requirements racking up](https://fedscoop.com/ai-requirements-are-racking-up-across-government-gao-says/)
- Global Government Forum, [Meet Humphrey](https://www.globalgovernmentforum.com/yes-civil-servant-meet-humphrey-the-governments-ai-package-for-officials/)
- MuckRock, [Federal agencies on FOIA AI](https://www.muckrock.com/news/archives/2025/may/07/how-federal-agencies-responded-to-our-requests-about-ai-use-in-foia/), 7 May 2025
- Cooley, [Korea AI Basic Act key takeaways](https://www.cooley.com/news/insight/2026/2026-01-27-south-koreas-ai-basic-act-overview-and-key-takeaways); IAPP, [Analyzing Korea's Framework Act](https://iapp.org/news/a/analyzing-south-korea-s-framework-act-on-the-development-of-ai)
- Future of Privacy Forum, [AI Verify Explained](https://fpf.org/blog/ai-verify-singapores-ai-governance-testing-initiative-explained/)

### Repository cross-references

- `research/extensions/adaptive-governance/ai-governance-landscape-2026.md`
- `research/extensions/adaptive-governance/governance-trend-analysis.md`
- `research/extensions/adaptive-governance/industry-practice-survey.md`
