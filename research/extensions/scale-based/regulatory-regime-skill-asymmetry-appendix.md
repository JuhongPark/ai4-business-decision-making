# Regulatory Regime × Skill Asymmetry: A Comparative Analysis

status: research_complete
date: 2026-04-21
purpose: Stream D deliverable of the sales-vs-productization research plan. Tests whether major AI regulatory regimes asymmetrically tax sales skill (production of compliance artifacts — filings, disclosures, certifications) versus productization skill (production of verification substance — testing, red-teaming, monitoring, per-decision logs). Compares 7 regimes and tests 5 hypotheses (H1-H5) from the parent memo.
parent_memo: [`sales-vs-productization-decomposition.md`](sales-vs-productization-decomposition.md)
research_plan: [`../../operations/expansion/sales-vs-productization-research-plan.md`](../../operations/expansion/sales-vs-productization-research-plan.md)

---

## 1. Framing

The parent memo's core claim is that verification quality splits into verification *substance* (productization output) and verification *claims* (sales output), and that the two can diverge. Regulation is the exogenous forcing function that closes or widens this gap. A regime that only mandates artifacts (disclosures, self-attestations, labels) rewards sales skill. A regime that mandates verification infrastructure (testing, red-team budgets, monitoring logs, per-decision audit trails) rewards productization skill. Most regimes do both; the question is the ratio and where penalties actually land.

For each regime I code: sales-instrument artifacts required, productization substance mandated, sanctioning gradient (who gets fined, how much, how often in 2025-2026), and an asymmetry verdict (sales-heavy, productization-heavy, balanced).

---

## 2. Comparison table

| Regime | Sales-instrument artifacts (S) | Productization substance mandated (P) | Sanctioning gradient 2025-2026 (G) | Asymmetry verdict (A) |
|---|---|---|---|---|
| **EU AI Act** (Reg 2024/1689) | CE marking, EU database registration, declaration of conformity, model cards (Annex XII), summaries of training content, incident reports, FRIA documentation, GPAI transparency docs | Conformity assessment (Annex VI self + Annex VII notified-body for remote biometrics), quality management system, risk management system, post-market monitoring plan, data governance, logging, human oversight, cybersecurity, serious-incident 15-day (2-day widespread) reporting | Penalty regime active Aug 2, 2025: up to €35M/7% (prohibited), €15M/3% (high-risk obligations, GPAI), €7.5M/1% (misinformation to authority). AI Office full GPAI fine power begins Aug 2, 2026. No headline fines yet; Commission opened investigation into Meta (Jan 2026) for WhatsApp Business API AI-access restrictions | **Balanced, leaning productization for high-risk; sales-heavy at GPAI layer via voluntary Code of Practice** |
| **US FDA CDS + SaMD** | 510(k) submission, De Novo, PMA dossiers, labeling, transparency documentation for non-device CDS (Jan 6 2026 guidance) | Pre-market clinical validation, predetermined change control plan (PCCP), quality system regulation (QSR / 21 CFR 820), real-world performance monitoring | Enforcement discretion expanded Jan 2026; FDA has authorized 1,000+ AI/ML medical devices by 2025; enforcement via warning letters and clearance denial rather than fines | **Productization-heavy** (when regulated as a device); Jan 2026 CDS guidance *reduces* scope by excluding clinically-appropriate single-recommendation CDS |
| **US Fed SR 11-7 (MRM)** | Model inventory, validation reports, audit reports, ongoing monitoring reports, governance policy documents | Independent validation (three-pillar: conceptual soundness, ongoing monitoring, outcomes analysis); effective challenge; development-independent validators | Not a fine regime; supervisory criticism and Matters Requiring Attention (MRAs); 58.8% of banks say regulatory clarity is biggest barrier to AI MRM. OCC/FDIC Oct 2025 proposed rulemaking to constrain MRA issuance | **Productization-heavy** for in-scope models (fraud, credit, capital); sales-layer disclosures minimal because supervisor is direct consumer |
| **US SEC "AI washing"** | 10-K/10-Q disclosures, investor-facing claims, marketing materials, Form ADV representations | No direct productization mandate; indirect via "substantiation" requirement for public claims | Presto (Jan 2025, public-company first); Delphia $225K + Global Predictions $175K (Mar 2024); Nate Inc. founder criminal fraud (Apr 2025, $42M raise). All penalties aimed at disclosure fraud | **Sales-instrument regime** — targets misrepresentation of AI capabilities, not AI system defects |
| **US FTC Operation AI Comply** | Advertising claims, substantiation files, consent-order attestations | No direct productization mandate; Section 5 unfair/deceptive frames AI-product malfunction as deceptive claim | At least a dozen cases in 2025: Rytr (consent order set aside Feb 2026), DoNotPay $193K, Workado (98%→53% accuracy order), Cleo, Rite Aid (facial recognition, 5-yr ban). Rite Aid 2024 ban signals FTC will tackle underlying product defect when tied to a deceptive claim | **Sales-instrument regime, with productization hook via deception frame** — the Rite Aid exception proves the rule |
| **US NIST AI RMF** | RMF Profiles, Govern/Map/Measure/Manage documentation, attestation to alignment | Full lifecycle risk management; measurable testing in Measure function; Mar 2025 update added GenAI/LLM threat categories (poisoning, evasion, extraction) | Voluntary. Adoption is referenced by CFPB, FDA, SEC, FTC, EEOC. No direct fines. Federal procurement signal via OMB M-25-21 | **Balanced framework; used as sales instrument ("NIST-aligned") in marketing** — the "aligned-with" badge is the dominant consumed output |
| **US OMB M-25-21** | Compliance plan, annual AI use-case inventory (CSV, public), AI impact assessment, generative AI policy | Minimum risk-management practices for high-impact/rights-impacting AI; pre-deployment testing; ongoing monitoring; impact assessment | Applies only to federal agencies. Non-compliance risk is internal / budget. 56 agency submissions, 3,611 use cases in 2025 consolidation. Creates vendor pressure through procurement rather than direct penalty | **Balanced; procurement-channel amplifier** — the inventory requirement creates a sales-artifact surface that vendors absorb |
| **Korea AI Basic Act** (2024-25) | High-impact-AI pre-assessment record, transparency notice to users, AI-generated content label, domestic-representative appointment | Risk-management plan, explanation plan for AI outputs (key criteria, training-data overview), fundamental-rights impact assessment efforts | Effective Jan 22, 2026. Max admin fine ₩30M (~US$21K) for failure to appoint domestic representative. One-year grace period: enforcement suspended except for severe human-rights violations. Very low sanctioning gradient | **Sales-instrument regime** — explanation/transparency/labelling duties are producible by compliance function; no mandated test harness; penalties de minimis |
| **UK ATRS + AISI** | Algorithmic Transparency Records published on gov.uk (125+ records by 2025) for public-sector use; voluntary in private sector | AISI performs pre-deployment evaluation of frontier models (30+ models tested since Nov 2023); results are voluntary inputs, not mandates | ATRS mandatory for central gov depts + in-scope ALBs (May 2025); no fines — non-publication is a transparency failure, not a statutory breach. AISI operates as research org, not regulator | **Bifurcated: sales-instrument at ATRS (disclosure regime), productization-heavy at AISI (but non-binding)** |
| **Japan AI Guidelines + Promotion Act** | Non-binding guidelines (METI/MIC v1.01 Mar 2025). Promotion Act (May 28, 2025): advice, information requests, "name and shame" disclosure | No productization mandates; three-tier structure (foundational values, 10 principles, checklists) leaves technical substance to voluntary action | **No fines, no penalties.** Enforcement is publication of non-compliance. Implementation June 4, 2025; full effect Sep 2025 | **Sales-instrument regime by construction** — explicit innovation-first stance; productization entirely optional |
| **Singapore AI Verify + GAAP + Project Moonshot** | AI Verify assurance reports, Moonshot benchmark outputs, GAAP (Global AI Assurance Pilot Feb 2025) case studies | **AI Verify technical testing framework**; Project Moonshot (open-source LLM red-team/benchmark toolkit); 16 testers × 17 companies in GAAP; Testing Starter Kit (2025) formalises hallucination, undesirable-content, data-disclosure, adversarial-prompt tests | No fines regime. IMDA operates model-governance as *infrastructure provision* — the state builds the testing surface that private firms use | **Productization-heavy, uniquely so** — the government built the productization substrate as public good |
| **China Generative AI Measures (CAC)** | Security assessment application, model filing (439 services filed by Jun 30, 2025), explicit + implicit content labelling (Mar 2025 measures, effective Sep 1, 2025), training-data attestation, real-name registration of users | Content-review pipeline, training-data compliance, security assessment (specifics non-public), algorithmic recommendation filings | Licensing is binding: unfiled services cannot be offered for public-opinion purposes. Removal of DeepSeek from app stores in select Korean/Taiwan markets (2025) shows licensing as a gating tool. Penalties under PIPL/DSL for data violations | **Sales-instrument regime wearing productization clothes** — the "productization" mandated is content-review machinery, not capability verification; filing is licensing, not evaluation |

---

## 3. Hypothesis tests

### H1 — EU AI Act forces productization substance for high-risk systems but allows sales-instrument compliance at GPAI

**Verdict: Largely supported, with caveat.**

Articles 9-15 (risk management, data governance, technical documentation, automatic logging, human oversight, cybersecurity) are engineering mandates — a compliance team cannot produce Art 12 logs or Art 15 adversarial-robustness evidence without productization headcount. Articles 72-73 (post-market monitoring + 15-day serious-incident reporting) require production telemetry. This forces productization work.

But the notified-body gate is narrow: the conformity-assessment route for most Annex III categories is *internal* (Annex VI) — the provider self-attests via its own quality management system. Only remote biometric identification triggers mandatory third-party assessment (Annex VII). Article 27 FRIA is closer to a sales-instrument duty, and it is a *deployer* obligation (public-service bodies, credit-scoring, life/health-insurance risk), not a provider one.

The GPAI layer is sales-instrument-shaped: Article 53 requires documentation, a training-content summary, and a copyright policy — these are documents. The voluntary GPAI Code of Practice (Jul 10, 2025), signed by 26 providers including Microsoft, Google, OpenAI, Anthropic (Meta declined), is an explicit sales-instrument: adherence reduces administrative burden and is "a relevant factor when setting fines." The Safety-and-Security chapter applies only to systemic-risk models (>10^25 FLOP), a group of 5-15 firms that already have productization infrastructure for other reasons. Sanctioning has not yet tested either side: penalty regime active since Aug 2, 2025, GPAI enforcement from Aug 2, 2026, no headline fine as of Apr 2026.

**H1 conclusion**: Supported for Annex III high-risk providers. Weakened at GPAI where compliance is producible as documents via the voluntary Code — a paradigmatic sales-instrument wrapping around a productization regime.

### H2 — US SEC/FTC enforcement targets sales-instrument failures

**Verdict: Strongly supported.**

Every SEC AI-washing action to date is a disclosure case: Delphia and Global Predictions (Mar 2024, $225K + $175K) for Form ADV misstatements; Presto Automation (Jan 2025) for 10-K/investor claims that understated human-and-third-party involvement; Nate Inc. (Apr 2025) for fraudulent capital-raise claims. In every case the violation is misalignment between claim and substance, not the substance itself. The SEC has not charged a company for its AI producing bad outputs; it has charged companies for saying the AI produced outputs it did not.

FTC Operation AI Comply follows the same pattern: Rytr (consent order set aside Feb 2026), DoNotPay ($193K), Workado (98% vs FTC-measured 53% accuracy), Cleo, and the business-opportunity cases all hinge on Section 5 deception. The Rite Aid 2024 facial-recognition 5-year ban is the exception that proves the rule: the unfair-practice ground was productization defect *tied to* a misrepresentation of accuracy. Without the claim, there would have been no action.

The producer role for compliance is legal/IR/marketing, not engineering. An SEC/FTC-safe firm can ship a defective AI if disclosures accurately describe the defect. The only productization incentive this creates is *downward*: understate capabilities.

**H2 conclusion**: Supported without caveat. US SEC/FTC in 2025-2026 treat the claim-substance gap as the primary wrongdoing, not the substance itself.

### H3 — Korean AI Basic Act and Japanese Guidelines are principally sales-instrument regimes

**Verdict: Supported for Japan, largely supported for Korea.**

Japan is the clearest sales-instrument regime of the seven. The METI/MIC Guidelines (v1.01, Mar 2025) are non-binding (values + 10 principles + checklists). The AI Promotion Act (May 28, 2025; full effect Sep 2025) adds statutory force but no fines — only "advice, information requests, name and shame." The law's design goal is "most AI-friendly country." A compliance team can produce every required artifact; the productization-substance delta between a compliant Japanese AI firm and a non-compliant one is near zero.

Korea is a more mixed case. The AI Basic Act (promulgated Jan 21, 2025, effective Jan 22, 2026) imposes productization-adjacent duties: risk management plan, explanation plan for AI outputs (including key criteria and training-data overview), and "efforts" toward fundamental-rights impact assessments. But: (a) the plan is a document, not an audit; (b) "efforts" is a weak standard; (c) the maximum administrative fine for the cleanest violation (failure to appoint a domestic representative under Article 36) is ₩30M (~US$21K); (d) the one-year grace period (until Jan 2027) suspends enforcement except for severe human-rights violations. ITIF's Sep 2025 analysis calls the domestic-rep requirement a "weak link" that imposes market-access friction on foreign providers without producing verification. Both Korea and Japan impose generative-AI labelling duties — these are UX + metadata changes, not verification engineering. China's Mar 2025 labelling measures (effective Sep 1, 2025) are stricter on this axis.

**H3 conclusion**: Supported. The sanctioning gradient in both regimes is so shallow that compliance is producible by legal teams.

### H4 — Singapore AI Verify is uniquely productization-focused because the government built the testing surface

**Verdict: Strongly supported. This is the regime-level surprise.**

Singapore did what no other government did: it built the productization substrate as a public good. Project Moonshot (launched May 2024) is open-source, integrates into CI/CD pipelines, and combines benchmarks + red-team attacks + a UI. AI Verify Foundation and MLCommons signed an MOI on shared safety benchmarks. The Global AI Assurance Pilot (Feb 2025) paired 16 testers with 17 companies across 10 sectors and produced a Testing Starter Kit formalising hallucination, undesirable-content, data-disclosure, and adversarial-prompt tests.

This inverts the usual regulator-vendor relationship. In every other regime, regulators set requirements and private vendors produce compliance tooling (OneTrust, Credo AI, Fiddler, Holistic AI). In Singapore the regulator *ships the tooling*. There are no fines; the regime is entirely voluntary. What it creates is a productization-substance surface private firms can consume — an asymmetric subsidy to productization skill, not a penalty for its absence.

Caveat: the GAAP key finding — that GenAI risks are "context-dependent (specific to industry, use case, culture, language, and organisation)" — admits that even a government-built testing surface does not solve contextualisation. Subject-matter experts are still needed lifecycle-wide.

**H4 conclusion**: Strongly supported. Productization infrastructure can be provided as a public good, not only as a private-firm output. Moonshot is the first working form of the S1 tier report's three infrastructure proposals.

### H5 — Chinese regime is a sales-instrument regime disguised as productization

**Verdict: Supported, with precision.**

The 2023 Interim Measures require a security assessment for services with "public opinion attributes or social mobilization capabilities." Filings: 117 by Mar 2024, 302 by Dec 2024, 346 by Mar 2025, 439 services + 233 algorithmic applications by Jun 2025. The filing is productization-adjacent, but review content is weighted toward *content-risk* (what the model will say about sensitive topics), not *capability-risk* (whether it performs its stated task).

The Mar 2025 Labelling Measures (effective Sep 1, 2025) require explicit + implicit labelling of AI-generated text, audio, images, video, and virtual scenes. Implicit labels sit in file metadata. This is enforceable productization work, but verification-of-provenance rather than verification-of-capability. A model that produces misleading but well-labelled outputs complies; a model that produces accurate but unlabelled outputs does not.

The real productization work mandated — content-moderation pipelines — is narrower than the EU/FDA/SR 11-7 stack. Penalties are *gating* rather than *fining*: unfiled services cannot operate; the 2025 removal of DeepSeek from South Korea and Taiwan app stores shows licensing as cross-jurisdiction leverage. PIPL/DSL provide data-violation fines, but no generative-AI-specific fine schedule comparable to EU AI Act 7% global turnover.

**H5 conclusion**: Supported with refinement. The regime is not pure sales-instrument — content moderation is real engineering — but its productization surface verifies *content conformity*, not *capability*.

---

## 4. Surprises

**Singapore is the most productization-forcing regime and it is entirely voluntary.** Textbook ordering would put the EU AI Act ahead of Singapore on productization depth. The 2025-2026 picture reverses this: AI Verify + Moonshot + GAAP are open-source, production-deployable artefacts. The EU AI Act's templates (FRIA questionnaires, GPAI summary templates) are documentation scaffolds, not testing frameworks. AISI evaluations are deeper than any EU AI Act pre-market test, but they are research outputs for government consumption, not productization inputs for industry. Productization-forcing regulation does not correlate with sanctioning severity.

**The FDA Jan 6, 2026 CDS guidance *reduced* productization requirements.** The revised CDS + General Wellness guidance loosens scope by extending enforcement discretion to CDS that provides a single clinically-appropriate recommendation with transparent/clinician-reviewable logic. AI-enabled CDS that previously would have required 510(k) clearance now falls outside device regulation, needing only documentation of inputs, logic, and outputs — a sales-instrument duty rather than a productization one. Radiology image analysis remains in-scope, but much of the CDS surface has moved out. This is an AI-specific regulator moving *away from* productization-forcing substance.

**SR 11-7 is the most quietly productization-heavy US regime and the banking sector wants it more prescriptive, not less.** SR 11-7 has never been updated for AI (SR 21-8 extended it to BSA/AML in 2021). Its three-pillar structure plus independent validation plus effective challenge is nonetheless the deepest productization mandate of any US regime. The BPI Oct 2025 OSTP comment and CBA Oct 2025 RFI response both argue SR 11-7 needs *updating for AI*, not displacement. 58.8% of surveyed banks say clearer regulatory guidance on AI is the single biggest barrier to advancing MRM. This is the opposite of every other regime's complaint pattern — a 2011 supervisory letter is the regime banks rely on for productization discipline.

---

## 5. Implications for the decomposition memo

**Which regimes force firms into the upper-right quadrant (sales ahead of product)?** Japan AI Promotion Act and Korea AI Basic Act allow compliance through documents (impact assessments, explanation plans, labelling, domestic-rep appointment) without productization substance. A firm in those markets can be compliant with high sales/investment skill and low productization skill. US SEC and FTC create the upper-right incentive through a different route: the safest position is to underclaim capabilities, which favours legal/IR skill over productization investment. Investment in verification infrastructure only pays off if it can be claimed, but claiming creates disclosure liability — a perverse productization-investment disincentive.

**Which regimes force firms into the upper-left quadrant (both skills strong)?** EU AI Act Annex III + FDA SaMD-regulated device + Fed SR 11-7 for in-scope banking models create the binding dual forcing function: technical documentation + CE declaration (sales-instrument) *plus* quality management system, risk management, and production monitoring (productization). A firm cannot comply with Annex III via documents alone and cannot sell without the documents either. But the forcing function is narrow — Annex III categories only, regulated devices only, in-scope banking models only. Outside these bright lines, firms can revert to upper-right.

**Public-good threshold gains two regime data points.** Singapore AI Verify is the existence proof that productization infrastructure can be a public good — Moonshot + GAAP are consumable by S1/S2/S3 firms that could not privately produce the same substrate. This lowers the productization-skill floor. The Korean domestic-representative requirement is the inverse: a sales-adjacent public-good problem the state *introduces* without providing a productization-side subsidy; ITIF's Sep 2025 analysis notes it raises effective entry cost for foreign providers.

**The claim-substance gap is a regulatory-design choice.** Regimes that regulate claims (SEC, FTC, Korea, Japan, UK ATRS) allow the gap to persist. Regimes that regulate substance (EU AI Act high-risk, FDA device, SR 11-7, Singapore AI Verify) narrow the gap — either by forcing substance to match claims (EU, FDA, SR 11-7) or by subsidising substance production (Singapore). The parent memo's §7.1 re-statement — "productization infrastructure predicts verification substance; sales infrastructure predicts verification claims" — can be extended: regulatory regime type is the exogenous variable that determines which skill the binding constraint lands on.

---

## 6. Limitations and evidence grading

Primary sources (regulation text, regulator releases) are A-grade across EU AI Act, FDA CDS, SEC releases, FTC releases, OMB M-25-21, UK gov.uk ATRS, Singapore AI Verify, and Japan METI. B-grade for Korea AI Basic Act (act text + FPF/Cooley/Debevoise/ITIF analyses), FTC and SR 11-7 (regulator source + practitioner commentary), and China CAC (translations + White & Case/Hogan Lovells/Reed Smith).

Honest limitations: (1) Fine data is incomplete — EU AI Office has not published a consolidated fine registry; CAC enforcement is partial; Korean AI Basic Act enforcement is suspended until Jan 2027. (2) The sales/productization coding is mine, not regulatory self-classification; reasonable people could re-shade some cells. (3) "Producer-role" analysis is structural — the claim that a Korean explanation plan is producible by a legal team without engineering input is inferred from act text and secondary analyses, not from survey evidence of how Korean firms actually staff compliance. (4) Singapore is overweighted relative to its global regulatory footprint — the productization-heavy finding is real, but Singapore's global effect on firm behaviour is smaller than EU AI Act or SR 11-7.

---

## 7. Cross-references

- [`sales-vs-productization-decomposition.md`](sales-vs-productization-decomposition.md) — parent memo; this appendix tests H1-H5 (§8) and extends §7.1 (Finding 1 re-statement)
- [`../../operations/expansion/sales-vs-productization-research-plan.md`](../../operations/expansion/sales-vs-productization-research-plan.md) — research plan identifying this as Stream D
- [`s6-national-governments.md`](s6-national-governments.md) — Singapore AI Verify positive-deviant finding this appendix sharpens
- [`s1-solo-entrepreneurs.md`](s1-solo-entrepreneurs.md) — public-good-threshold analysis gaining Singapore-as-existence-proof + Korean-rep-requirement inverse example

---

## 8. Sources

### EU AI Act

- European Commission, [AI Act | Shaping Europe's digital future](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Article 6: Classification Rules for High-Risk AI Systems](https://artificialintelligenceact.eu/article/6/)
- [Article 27: Fundamental Rights Impact Assessment](https://artificialintelligenceact.eu/article/27/)
- [Article 72: Post-Market Monitoring](https://artificialintelligenceact.eu/article/72/)
- [Article 73: Reporting of Serious Incidents](https://artificialintelligenceact.eu/article/73/)
- DLA Piper, [Latest wave of obligations under the EU AI Act take effect (Aug 2025)](https://www.dlapiper.com/en-us/insights/publications/2025/08/latest-wave-of-obligations-under-the-eu-ai-act-take-effect)
- Jones Day, [EU AI Act: European Commission Publishes GPAI Code of Practice (Aug 2025)](https://www.jonesday.com/en/insights/2025/08/eu-ai-act-european-commission-publishes-generalpurpose-ai-code-of-practice)
- Latham & Watkins, [EU AI Act: GPAI Model Obligations in Force](https://www.lw.com/en/insights/eu-ai-act-gpai-model-obligations-in-force-and-final-gpai-code-of-practice-in-place)
- Skadden, [EU GPAI Obligations Now in Force (2025)](https://www.skadden.com/insights/publications/2025/08/eus-general-purpose-ai-obligations)
- Taylor Wessing, [EU AI Act: serious incident reporting (Oct 2025)](https://www.taylorwessing.com/en/insights-and-events/insights/2025/10/eu-ai-act-deep-dive)
- [The GPAI Code of Practice · Final Version](https://code-of-practice.ai/)

### US FDA

- Arnold & Porter, [FDA "Cuts Red Tape" on CDS Software and Wearables (Jan 2026)](https://www.arnoldporter.com/en/perspectives/advisories/2026/01/fda-cuts-red-tape-on-clinical-decision-support-software)
- Covington, [5 Key Takeaways from FDA's Revised CDS Software Guidance (Jan 2026)](https://www.cov.com/en/news-and-insights/insights/2026/01/5-key-takeaways-from-fdas-revised-clinical-decision-support-cds-software-guidance)
- Ropes & Gray, [FDA Adapts: Updated Guidances on General Wellness and CDS (Jan 2026)](https://www.ropesgray.com/en/insights/alerts/2026/01/fda-adapts-with-the-times-on-digital-health-updated-guidances-on-general-wellness-products)
- Faegre Drinker, [Key Updates in FDA's 2026 CDS Guidance](https://www.faegredrinker.com/en/insights/publications/2026/1/key-updates-in-fdas-2026-general-wellness-and-clinical-decision-support-software-guidance)

### US Federal Reserve SR 11-7

- Federal Reserve, [SR 11-7: Guidance on Model Risk Management](https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm)
- Federal Reserve, [SR 21-8: Interagency Statement on MRM for BSA/AML](https://www.federalreserve.gov/supervisionreg/srletters/SR2108.htm)
- Bank Policy Institute, [Response to OSTP RFI on AI (Oct 27, 2025)](https://bpi.com/wp-content/uploads/2025/10/BPI-OSTP-AI-RFI-Response-10.27.25.pdf)
- Consumer Bankers Association, [Comment on Docket OSTP-TECH-2025-0067 (Oct 2025)](https://consumerbankers.com/wp-content/uploads/2025/10/CBA-Comment-on-Docket-OSTP-TECH-2025-0067-10.27.2025.pdf)

### US SEC AI washing

- SEC, [SEC Charges Two Investment Advisers with Making False and Misleading Statements About Their Use of AI (Mar 2024)](https://www.sec.gov/newsroom/press-releases/2024-36)
- DLA Piper, [SEC Emphasizes Focus on AI Washing (2025)](https://www.dlapiper.com/en/insights/publications/ai-outlook/2025/sec-emphasizes-focus-on-ai-washing)
- Winston & Strawn, [SEC Targets AI Washing](https://www.winston.com/en/blogs-and-podcasts/capital-markets-and-securities-law-watch/sec-targets-ai-washing-by-companies-investment-advisers-and-broker-dealers)
- Latham & Watkins, [SEC First-Ever Enforcement Actions for AI Washing](https://www.lw.com/admin/upload/SiteAttachments/SEC-Announces-First-Ever-Enforcement-Actions-for-AI-Washing.pdf)
- Global Investigations Review, [US enforcement agencies intensify scrutiny of AI washing (2026)](https://globalinvestigationsreview.com/review/the-investigations-review-of-the-americas/2026/article/us-enforcement-agencies-intensify-scrutiny-of-ai-washing)

### US FTC Operation AI Comply

- Federal Trade Commission, [Operation AI Comply press release (Sep 2024)](https://www.ftc.gov/news-events/news/press-releases/2024/09/ftc-announces-crackdown-deceptive-ai-claims-schemes)
- Benesch, [One Year In, FTC's Operation AI Comply Continues (Sep 2025)](https://www.beneschlaw.com/insight/one-year-in-ftcs-operation-ai-comply-continues-under-new-administration-signaling-enduring-enforcement-focus/)
- National Law Review, [FTC Brings Dozen AI-Washing Cases in 2025](https://natlawreview.com/press-releases/ftc-brings-dozen-ai-washing-enforcement-cases-2025-targeting-overstated-ai)
- Mintz, [FTC Sets Aside Rytr Consent Order (Feb 2026)](https://www.mintz.com/insights-center/viewpoints/54731/2026-02-13-emerging-federal-ai-strategy-ftc-sets-aside-rytr)

### US NIST AI RMF

- NIST, [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- NIST, [AI RMF 1.0 PDF](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)
- ispartners, [NIST AI RMF 2025 Updates](https://www.ispartnersllc.com/blog/nist-ai-rmf-2025-updates-what-you-need-to-know-about-the-latest-framework-changes/)

### US OMB M-25-21

- White House, [M-25-21 memo (Apr 3, 2025)](https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf)
- OMB, [2025 Federal Agency AI Use Case Inventory (GitHub)](https://github.com/ombegov/2025-Federal-Agency-AI-Use-Case-Inventory)
- Department of Homeland Security, [Compliance Plan for M-25-21 (Sep 2025)](https://www.dhs.gov/sites/default/files/2025-09/25_0926_cio_dhs_compliance_plan_for_omb_m-25-21_508.pdf)
- Federal Reserve, [Compliance Plan for M-25-21](https://www.federalreserve.gov/publications/compliance-plan-for-OMB-memorandum-m-25-21.htm)
- Inside Government Contracts, [OMB Issues First Trump 2.0-Era Requirements (Apr 2025)](https://www.insidegovernmentcontracts.com/2025/04/omb-issues-first-trump-2-0-era-requirements-for-ai-use-and-procurement-by-federal-agencies/)

### Korea AI Basic Act

- CSET, [Framework Act on the Development of AI (EN translation)](https://cset.georgetown.edu/wp-content/uploads/t0625_south_korea_ai_law_EN.pdf)
- Cooley, [South Korea's AI Basic Act: Overview and Key Takeaways (Jan 2026)](https://www.cooley.com/news/insight/2026/2026-01-27-south-koreas-ai-basic-act-overview-and-key-takeaways)
- Future of Privacy Forum, [South Korea's New AI Framework Act](https://fpf.org/blog/south-koreas-new-ai-framework-act-a-balancing-act-between-innovation-and-regulation/)
- Debevoise, [South Korea Enacts New AI Law (Mar 2025)](https://www.debevoisedatablog.com/2025/03/24/south-korea-enacts-new-ai-law/)
- ITIF, [One Law Sets South Korea's AI Policy (Sep 2025)](https://itif.org/publications/2025/09/29/one-law-sets-south-koreas-ai-policy-one-weak-link-could-break-it/)
- Library of Congress, [South Korea Comprehensive AI Legal Framework Takes Effect (Feb 2026)](https://www.loc.gov/item/global-legal-monitor/2026-02-20/south-korea-comprehensive-ai-legal-framework-takes-effect)
- OneTrust, [South Korea's New AI Law](https://www.onetrust.com/blog/south-koreas-new-ai-law-what-it-means-for-organizations-and-how-to-prepare/)

### UK ATRS + AISI

- gov.uk, [Algorithmic Transparency Recording Standard Hub](https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub)
- UK Data in Government Blog, [Making ATRS mandatory across government (May 2025)](https://dataingovernment.blog.gov.uk/2025/05/08/making-the-algorithmic-transparency-recording-standard-atrs-mandatory-across-government/)
- AISI, [Frontier AI Trends Report 2025](https://www.aisi.gov.uk/research/aisi-frontier-ai-trends-report-2025)
- AISI, [2025 Year in Review](https://www.aisi.gov.uk/blog/our-2025-year-in-review)

### Japan AI Guidelines + Promotion Act

- METI, [AI Guidelines for Business Ver 1.0 (Apr 2024)](https://www.meti.go.jp/english/press/2024/0419_002.html)
- Anderson Mori & Tomotsune, [AI Guidelines for Business v1.1 (May 2025)](https://www.amt-law.com/en/insights/trending-news/trending-news_20250522001_en_001/)
- White & Case, [Japan's first AI legislation becomes law (May 2025)](https://www.whitecase.com/insight-alert/japans-first-ai-legislation-becomes-law-focus-promoting-research-and-development-no)
- Future of Privacy Forum, [Understanding Japan's AI Promotion Act](https://fpf.org/blog/understanding-japans-ai-promotion-act-an-innovation-first-blueprint-for-ai-regulation/)
- Japan Government Online, [AI Promotion Act Now in Full Effect (Nov 2025)](https://www.gov-online.go.jp/hlj/en/november_2025/november_2025-08.html)

### Singapore AI Verify + Moonshot + GAAP

- AI Verify Foundation, [What is AI Verify](https://aiverifyfoundation.sg/what-is-ai-verify/)
- AI Verify Foundation, [Project Moonshot](https://aiverifyfoundation.sg/project-moonshot/)
- AI Verify Foundation, [moonshot GitHub repository](https://github.com/aiverify-foundation/moonshot)
- AI Verify Foundation, [Global AI Assurance Pilot](https://aiverifyfoundation.sg/ai-assurance-pilot/)
- IMDA, [SG Unveils Insights from World's First Technical Testing of Real World GenAI (2025)](https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2025/sg-unveils-insights-from-worlds-first-technical-testing-of-real-world-applications-of-genai)
- Global AI Assurance Pilot, [Report Introduction](https://assurance.aiverifyfoundation.sg/report/introduction/)

### China Generative AI Measures

- Library of Congress, [China: Generative AI Measures Finalized (2023)](https://www.loc.gov/item/global-legal-monitor/2023-07-18/china-generative-ai-measures-finalized/)
- Hogan Lovells, [China finalizes generative AI regulation](https://www.hoganlovells.com/en/publications/china-finalizes-generative-ai-regulation)
- IAPP, [Global AI Governance Law and Policy: China](https://iapp.org/resources/article/global-ai-governance-china)
- Securiti, [Navigating China's AI Regulatory Landscape in 2025](https://securiti.ai/china-ai-regulatory-landscape/)
- State Council Information Office, [346 generative AI services filed with CAC (Apr 2025)](http://english.scio.gov.cn/pressroom/2025-04/09/content_117814020.html)
- Digital Policy Alert, [CAC Domestic Generative AI Services Filing List](https://digitalpolicyalert.org/event/25904-adopted-chinese-cyberspace-administration-registration-of-generative-ai-services)
- White & Case, [AI Watch: Global regulatory tracker - China](https://www.whitecase.com/insight-our-thinking/ai-watch-global-regulatory-tracker-china)
