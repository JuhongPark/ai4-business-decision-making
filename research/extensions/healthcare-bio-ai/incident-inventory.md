# Healthcare and Bio AI Incident Inventory

status: draft
date: 2026-04-21
scope: 2018–2026 healthcare, hospital, pharma, and biotech AI failure cases with regulatory filings, peer-reviewed validation studies, or major-journalism documentation
evidence_tiers: A = primary source (regulator filing, peer-reviewed paper, court docket); B = credible journalism or peer commentary; C = inferred from partial sources; D = speculative (excluded unless flagged)
relationship: This inventory supplements the core 71-case AI governance failure corpus (`research/extensions/business-alignment/incidents/incident-inventory.md`). It is not promoted into the core count. Incidents are tagged with the nine healthcare sub-domains (HC1-HC9) defined in `sub-domain-taxonomy.md`.

---

## 1. Inventory table

| # | Case | Year(s) | HC sub-domain | Actor type | Jurisdiction | What went wrong | Failure mechanism | Primary source | Tier |
|---|------|---------|---------------|------------|--------------|-----------------|-------------------|----------------|------|
| HBI-01 | Epic Sepsis Model external validation | 2021 | HC2 | EHR vendor + hospitals | US | Proprietary sepsis predictor deployed at 100+ hospitals showed AUC 0.63 at Michigan Medicine vs developer-claimed 0.76-0.83; missed 67% of sepsis cases while firing alerts on 18% of all hospitalisations | Lack of safety evaluation; specification gaming (proxy outcome) | [Wong et al., JAMA Internal Medicine 2021](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2781307) | A |
| HBI-02 | Epic Deterioration Index in COVID-19 triage | 2020-2021 | HC2 | EHR vendor + hospitals | US | Proprietary deterioration score deployed for COVID triage with 39% sensitivity; would have mis-routed many ICU-level patients | Deployment outside intended use | [Singh et al., Annals ATS 2021](https://pubmed.ncbi.nlm.nih.gov/33357088/) | A |
| HBI-03 | IBM Watson for Oncology | 2013-2018 | HC2, HC6 | Tech vendor + AMCs | US, India, global | Trained on small number of synthetic hypothetical cases rather than real patient data; generated "unsafe and incorrect" cancer treatment recommendations per internal IBM documents | Training data bias; lack of safety evaluation | [STAT News, Ross & Swetlitz 2018](https://www.statnews.com/2018/07/25/ibm-watson-recommended-unsafe-incorrect-treatments/) | B |
| HBI-04 | COVID chest-imaging AI systematic review | 2020-2021 | HC1 | Academic and startup models | Global | Systematic review of 232 COVID-19 chest X-ray/CT ML papers: none of 62 quality-screened models judged clinically usable due to methodological flaws and dataset biases | Spurious correlation; lack of safety evaluation | [Roberts et al., Nature Machine Intelligence 2021](https://www.nature.com/articles/s42256-021-00307-0) | A |
| HBI-05 | Zech et al. pneumonia CNN hospital shortcut | 2018 | HC1 | Academic | US | CNN identified hospital system from equipment-specific metadata (>99.95%) rather than pneumonia features; performance collapsed on external data | Spurious correlation | [Zech et al., PLOS Medicine 2018](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1002683) | A |
| HBI-06 | Optum / Impact Pro risk algorithm racial bias | 2019 | HC3, HC8 | Insurer + vendor | US | Widely deployed risk-stratification algorithm affecting ~200M people used cost as proxy for need; reduced Black patient referrals for care by more than half | Training data bias; specification gaming | [Obermeyer et al., Science 2019](https://www.science.org/doi/10.1126/science.aax2342) | A |
| HBI-07 | Dermatology AI on dark skin (DDI study) | 2022 | HC1 | Academic + startups | US | State-of-the-art dermatology classifiers showed substantial accuracy drops on dark skin tones and uncommon diseases on curated diverse dataset | Training data bias | [Daneshjou et al., Science Advances 2022](https://www.science.org/doi/10.1126/sciadv.abq6147) | A |
| HBI-08 | Pulse oximeter racial bias FDA panel | 2020-2022 | HC2 | Device manufacturers | US | FDA advisory panel concluded pulse oximeters overestimate SpO2 in darker-skinned patients; associated with delayed COVID-19 therapy eligibility | Training data bias; distributional shift | [Fawzy et al., JAMA Internal Medicine 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9257583/) | A |
| HBI-09 | UnitedHealth nH Predict class action | 2023-present | HC8 | Insurer | US | Class action alleges nH Predict used to deny post-acute care to Medicare Advantage patients; plaintiffs claim ~90% of denials overturned on appeal; breach of contract claims allowed to proceed Feb 2025 | Oversight failure; specification gaming (cost proxy) | [Estate of Lokken v. UnitedHealth](https://litigationtracker.law.georgetown.edu/wp-content/uploads/2023/11/Estate-of-Gene-B.-Lokken-et-al_20231114_COMPLAINT.pdf) | A |
| HBI-10 | Humana nH Predict class action | 2023-present | HC8 | Insurer | US | Barrows v. Humana alleges same nH Predict used to terminate post-acute care; employees disciplined for deviating from projected length of stay | Oversight failure | [STAT News, 2023](https://www.statnews.com/2023/12/12/humana-algorithm-medicare-advantage-patients-lawsuit/) | A |
| HBI-11 | Cigna PxDx automated denials | 2022-present | HC8 | Insurer | US | ProPublica: Cigna doctors spent ~1.2 seconds per case using PxDx to batch-deny 300,000 claims over two months; ERISA breach claim advanced March 2025 | Oversight failure | [ProPublica, Rucker & Armstrong 2023](https://www.propublica.org/article/cigna-pxdx-medical-health-insurance-rejection-claims) | A |
| HBI-12 | NEDA Tessa eating-disorder chatbot | 2023 | HC7 | Nonprofit + vendor (Cass) | US | Chatbot meant to replace human helpline recommended calorie restriction and weight loss to users with eating disorders after vendor swapped rule-based bot for generative version without sponsor approval | Deployment outside intended use; normative violation | [NPR, Wells 2023](https://www.npr.org/sections/health-shots/2023/06/08/1180838096/an-eating-disorders-chatbot-offered-dieting-advice-raising-fears-about-ai-in-hea) | B |
| HBI-13 | Koko GPT-3 covert experiment | 2022-2023 | HC7 | Mental-health platform | US | Koko used GPT-3 to write or co-write ~4,000 peer-support responses without explicit informed consent; founder's public disclosure triggered IRB/ethics backlash | Normative violation | [NBC News, Ingram 2023](https://www.nbcnews.com/tech/internet/chatgpt-ai-experiment-mental-health-tech-app-koko-rcna65110) | B |
| HBI-14 | Character.AI teen suicide (Setzer) | 2024-2026 | HC7 | Platform | US | 14-year-old user died by suicide after prolonged chatbot relationship; lawsuit alleges platform failed to escalate self-harm disclosures; Character.AI and Google agreed to settle Jan 2026 | Oversight failure; normative violation | [CNN Business, Duffy 2024](https://www.cnn.com/2024/10/30/tech/teen-suicide-character-ai-lawsuit) | A |
| HBI-15 | Replika Italy GDPR ban | 2023-2025 | HC7 | Chatbot platform (Luka) | Italy / EU | Garante blocked Replika from processing Italian user data over risks to minors and vulnerable users, inadequate age gating, lack of lawful basis; multi-million euro fine in 2025 | Normative violation | [Garante order, Feb 2023 via IAPP](https://iapp.org/news/a/italy-s-dpa-reaffirms-ban-on-replika-over-ai-and-children-s-privacy-concerns) | A |
| HBI-16 | Babylon Health symptom checker and collapse | 2018-2023 | HC2, HC7 | Digital-health startup | UK, US, Rwanda | Chatbot triage missed heart-attack presentations and misclassified painful breast lump; MHRA expressed concerns; company went bankrupt 2023 | Lack of safety evaluation | [TechCrunch, 2021](https://techcrunch.com/2021/03/05/uks-mhra-says-it-has-concerns-about-babylon-health-and-flags-legal-gap-around-triage-chatbots/) | B |
| HBI-17 | DeepMind-Royal Free Streams (AKI) | 2015-2017 | HC3 | Tech partner + NHS trust | UK | ICO ruled 1.6M patient records transferred without lawful basis or adequate patient notification; became cautionary tale for health-AI data governance | Normative violation | [UK ICO ruling, July 2017](https://www.digitalhealth.net/2017/07/royal-free-and-deepmind-did-not-comply-with-dpa-ico/) | A |
| HBI-18 | BenevolentAI BEN-2293 atopic dermatitis failure | 2023 | HC4 | AI-drug startup | UK | Phase IIa trial for AI-discovered topical eczema drug missed efficacy endpoints; triggered ~180 layoffs and collapse of commercial deal prospects | Distributional shift (pre-clinical → clinical); lack of safety evaluation | [Fierce Biotech, 2023](https://www.fiercebiotech.com/biotech/benevolentai-cruel-rd-ai-enabled-drug-flunks-midphase-eczema-trial-dent-deal-plans) | B |
| HBI-19 | Exscientia CEO dismissal and pipeline setbacks | 2024 | HC4 | AI-drug startup | UK / US | CEO fired for cause after undisclosed relationships; company previously halted internal cancer program after target viability concerns; emblematic of AI-drug hype-reality gap | Oversight failure | [Fierce Biotech, 2024](https://www.fiercebiotech.com/biotech/exscientia-fires-ceo-andrew-hopkins-over-inappropriate-relationships-2-employees) | B |
| HBI-20 | Recursion REC-994 CCM Phase 2 | 2024 | HC4 | AI-drug startup | US | AI-generated lead drug met safety endpoint but showed only "trend towards" lesion reduction at high dose; AI-generated pipeline's first major efficacy readout underwhelmed | Distributional shift (pre-clinical → clinical) | [BioPharma Dive, 2024](https://www.biopharmadive.com/news/recursion-study-results-cerebral-cavernous-malformation-ai-drug/725846/) | B |
| HBI-21 | Olive AI shutdown | 2022-2023 | HC3, HC9 | Revenue-cycle startup | US | Once-$4B-valued hospital automation firm shut down Oct 2023 after revelations of manual workarounds behind "AI" branding and unmet savings claims | Specification gaming (commercial overclaim) | [Axios, 2023](https://www.axios.com/pro/health-tech-deals/2023/10/31/olive-ai-is-shutting-down) | B |
| HBI-22 | Forward Health CarePods shutdown | 2024 | HC2, HC7 | Direct-primary-care startup | US | AI-kiosk primary care concept shut down Nov 2024 after $400M burn; reports of patients trapped inside pods, technical failures, limited clinical utility | Deployment outside intended use | [Fierce Healthcare, 2024](https://www.fiercehealthcare.com/health-tech/primary-care-player-forward-shutters-after-raising-400m-rolling-out-carepods) | B |
| HBI-23 | OpenAI Whisper hospital transcription hallucinations | 2024 | HC9 | Foundation-model vendor + Nabla + 40+ health systems | US | Whisper-based medical scribe hallucinated non-existent medications ("hyperactivated antibiotics"), racial commentary, fabricated dialogue; Cornell/UW research found ~1.4% hallucination rate across transcriptions | Fluent hallucination | [AP via ABC / Fortune 2024](https://fortune.com/2024/10/26/openai-transcription-tool-whisper-hallucination-rate-ai-tools-hospitals-patients-doctors/) | B |
| HBI-24 | Permanente ambient-scribe pilot misdiagnoses | 2024 | HC9 | Payer-provider + scribe vendor | US | Real-world pilot of 10,000 Permanente clinicians documented misdiagnosed conditions, omitted details, summarisation inconsistencies in AI-generated notes | Fluent hallucination | [NEJM Catalyst, 2024](https://thehealthcareblog.com/blog/2024/03/18/the-latest-ai-craze-ambient-scribing/) | B |
| HBI-25 | ChatGPT pharmacotherapy counselling evaluations | 2023-2026 | HC7 | Foundation-model vendor | International | Long Island University: only 10/39 drug questions answered satisfactorily by free-tier ChatGPT; BJCP 2026 concluded use in pharmacotherapy counselling "strongly discouraged"; repeated reference fabrication documented | Fluent hallucination | [Krichevsky et al., BJCP 2026](https://bpspubs.onlinelibrary.wiley.com/doi/10.1002/bcp.70321) | A |
| HBI-26 | GPT-4 racial / gender bias in clinical vignettes | 2023-2024 | HC2 | Foundation-model vendor | US | Evaluation found GPT-4 perpetuated stereotyped assumptions in diagnostic reasoning and treatment recommendations across race and gender | Training data bias | [Zack et al., Lancet Digital Health 2024](https://www.thelancet.com/journals/landig/article/PIIS2589-7500(23)00225-X/fulltext) | A |
| HBI-27 | Novo Nordisk FDA pharmacovigilance warning | 2025-2026 | HC5 | Pharma | US | FDA warning letter documented systemic post-approval adverse-event reporting failures including an unreported patient death on semaglutide; tied to automated case-intake procedures that improperly invalidated cases | Oversight failure | [FDA Warning Letter 717576, Mar 2026](https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/warning-letters/novo-nordisk-inc-717576-03052026) | A |
| HBI-28 | Kaiser Permanente mental-health AI screening strike | 2024-2026 | HC7 | Integrated provider/payer | US | California Nurses Association and NUHW clinicians struck over automated telephone triage and AI questionnaires replacing licensed assessment; 2,400 therapists + 23,000 nurses one-day strike Mar 2026 | Deployment outside intended use; normative violation | [KQED, 2026](https://www.kqed.org/news/12076753/northern-california-kaiser-therapists-hold-1-day-strike-over-ai-patient-care-concerns) | B |
| HBI-29 | Tempus AI securities and genetic-privacy suits | 2024-2026 | HC6 | Precision-medicine AI | US | Post-IPO securities class actions allege AI-washing; overstated AI capability while revenue dominated by acquired genomic testing; parallel Illinois GIPA class actions over DNA-data resale to 70+ pharma clients | Specification gaming (commercial overclaim); normative violation | [Stanford SCAC, Tempus filing](https://securities.stanford.edu/filings-case.html?id=108617) | A |
| HBI-30 | Woebot Health app sunset | 2021-2025 | HC7 | Mental-health chatbot startup | US | FDA Breakthrough-Designated postpartum-depression digital therapeutic (WB001) never reached full marketing authorisation; CEO cited cost of FDA compliance and LLM regulatory gap before retiring consumer app June 2025 | Oversight failure (regulatory gap effect) | [STAT News, 2025](https://www.statnews.com/2025/07/02/woebot-therapy-chatbot-shuts-down-founder-says-ai-moving-faster-than-regulators/) | B |

## 2. FICS-1 distribution

Applying the scale-based track's Failure Incident Coding Scheme (FICS-1), the healthcare-bio inventory of 30 cases distributes across failure mechanisms as follows:

| Failure mechanism | Count | Representative cases |
|---|---|---|
| Oversight failure | 8 | HBI-09, 10, 11, 14, 19, 22, 27, 30 |
| Training data bias | 6 | HBI-03, 06, 07, 08, 26, 03 |
| Specification gaming | 5 | HBI-01, 06, 09, 21, 29 |
| Normative violation | 6 | HBI-12, 13, 14, 15, 17, 28, 29 |
| Distributional shift | 4 | HBI-02, 04, 18, 20 |
| Spurious correlation | 2 | HBI-04, 05 |
| Fluent hallucination | 3 | HBI-23, 24, 25 |
| Lack of safety evaluation | 5 | HBI-01, 03, 04, 16, 18 |
| Deployment outside intended use | 4 | HBI-02, 12, 22, 28 |

(Counts sum to more than 30 because some cases code to multiple mechanisms.)

The dominant mechanism is **oversight failure**, driven by the cluster of insurer-utilization cases (HBI-09, 10, 11) and the mental-health-chatbot cases (HBI-14, 22, 28). This differs from the core 71-case corpus, which was dominated by **reward hacking / specification gaming** and **fluent hallucination**. Healthcare's dominant mode is upstream of those: the review step itself fails or is compromised.

## 3. Cross-cutting failure patterns

Four patterns are structurally healthcare-distinct, not merely instances of generic AI failure modes:

### Pattern 1 — Proprietary clinical AI deployed at scale before external validation

Epic Sepsis Model (HBI-01), Epic Deterioration Index (HBI-02), and IBM Watson for Oncology (HBI-03) share a sector-specific structural defect: clinical models are sold to hospitals as vendor-controlled infrastructure, deployed system-wide, and only externally validated after years of use. Wong et al. could not fully inspect ESM's feature set until after publication. The Zech pneumonia study (HBI-05) and Roberts COVID-imaging review (HBI-04) extend the pattern to imaging — high internal AUCs masked shortcut learning on hospital-equipment signatures and ward-acquired CT artefacts, visible only under external evaluation.

The failure mechanism is not exotic — it is lack of safety evaluation. But the healthcare-specific element is the **regulatory-perimeter gap** that made the lack of evaluation legal: the 21st Century Cures Act CDS carve-out kept these models outside FDA pre-market review. The same model, marketed as a device rather than as CDS, would have required clearance data that the external validators eventually produced too late.

### Pattern 2 — Cost-proxy and coverage-gatekeeper substitution ("algorithm as benefit denier")

A specifically healthcare-financial pattern runs through Optum Impact Pro (HBI-06), UnitedHealth nH Predict (HBI-09), Humana (HBI-10), and Cigna PxDx (HBI-11). In each, a predictive or rule-based system substitutes for clinical judgment at the coverage decision point. Obermeyer et al. showed cost-as-label turns a "health needs" model into a race-biased one. The nH Predict litigation shows the same move applied to post-acute care denial. Cigna PxDx reaches the endpoint where "AI" is effectively a deterministic denial rule labelled as clinical review (1.2 seconds per denial).

The failure mechanism combines **specification gaming** (cost as proxy for clinical need) with **oversight failure** (human-in-the-loop vestigial). The healthcare-specific element is the **adversarial verification chain**: the reviewer is employed by the party whose financial interest is served by denial. RVCS-1 scoring treats verification as a capability-neutral review step; HC8's verification step is structurally not neutral.

### Pattern 3 — Conversational AI deployed on vulnerable populations without safety infrastructure

Koko (HBI-13), NEDA Tessa (HBI-12), Character.AI/Setzer (HBI-14), Replika (HBI-15), and Kaiser (HBI-28) together show that conversational-AI failure in healthcare differs qualitatively from retail or enterprise. Tessa's vendor swapped a rule-based safe system for a generative one without sponsor knowledge; Character.AI did not escalate documented suicidal ideation; Koko ran an unconsented psychological experiment on people seeking peer support. The common mechanism is **normative violation** — the question is not whether the model hallucinated but whether the deployment was ever permissible given the population.

The healthcare-specific element is the **regulatory-gap compounding**: wellness carve-outs keep most of these deployments outside FDA authority, so the sector combines maximum population vulnerability with minimum pre-market oversight. Woebot (HBI-30) shows the consequence of the gap running the other way — a company that chose the FDA pathway exhausted its runway before clearance.

### Pattern 4 — Drug-discovery AI's translation cliff

BenevolentAI (HBI-18), Exscientia (HBI-19), and Recursion (HBI-20) reveal a recurring pattern where AI-generated or AI-prioritised drug candidates pass pre-clinical and early-clinical hurdles but show thin or absent efficacy in Phase 2. The failure mechanism is best captured as **distributional shift at the target-validation layer**: AI platforms optimise for binding affinity, ADME properties, or synthesizability within a training distribution of historic medicinal-chemistry data, and these are poor proxies for human clinical efficacy in novel indications.

The healthcare-specific element is the **delayed detectability**: unlike diagnostic AI where a misclassification surfaces within hours or days, drug-discovery AI's failure surfaces in a Phase 2 readout years after the AI's actual decision. This asymmetry between fast AI iteration and slow biological verification is what makes HC4 a structurally different governance problem.

## 4. Secondary observations

- **Pharmacovigilance failures** (HBI-27) are an emergent and under-investigated category. Automated adverse-event triage systems that invalidate reports on structural grounds may constitute a systemic post-approval compliance risk across pharma. The Novo Nordisk warning letter is likely the first of a class.
- **AI-washing securities risk** (HBI-29) and **revenue-cycle automation collapse** (HBI-21) show a healthcare-specific commercial failure pattern: overstating AI capability while the actual workflow runs on human labour. The pattern is the mirror of the clinical-safety pattern, affecting different stakeholders (investors, hospital administrators) rather than patients directly.
- **Health data governance** (HBI-17, 15, 29) is at least as frequent an incident category as clinical safety in the current enforcement record. DPA actions (Italian Garante, UK ICO) are doing enforcement work that health-AI-specific regulators are not.

## 5. Cases considered but excluded

- LifeWhisperer / embryo lawsuits — no documented AI-specific incident surfaced in search window.
- Aidoc / Viz.ai false-positive claims — performance reports exist but none rise to documented "failure" in the regulator-filing sense.
- IDx-DR disparities — published literature indicates no significant performance gap by race after deployment; not an incident.
- Rad AI / Aidence / Lunit FDA warning letters — none surfaced in search window specific to those vendors.
- Mount Sinai pediatric sepsis-COVID kidney model — research exists but no documented deployment failure.

These are listed to show the boundary of the inventory, not to imply that problems do not exist with these products or studies.

## 6. How this inventory connects to other track documents

- `sub-domain-taxonomy.md` provides the HC1-HC9 tags used in column 3.
- `framework-application.md` uses this inventory to test the 6-dim delegation framework and 5-discipline reasoning verification against healthcare-specific cases.
- `scale-mapping.md` places the actor in each incident onto the S1-S7 scale tiers.
- `synthesis.md` uses the Pattern 1-4 structure in §3 as its evidence basis.
- Cases HBI-01, HBI-06, HBI-09, and HBI-14 are strong candidates for promotion into the core 71-case corpus in a future update cycle; the decision to promote is not taken in this track.

## 7. Limitations

- 30 cases is sufficient to surface four clean cross-cutting patterns but too few for statistical claims about base rates.
- Coverage skews US / EU. Korean (JLK-related), Chinese (DeepWise, Tencent Miying, AliHealth), and Japanese documented incidents are under-represented due to language and access constraints.
- Vendor-positive cases (e.g., successful deployments) are not in scope; the inventory is by design a failure corpus.
- Peer-reviewed validation papers that contradict vendor claims are counted as incidents (HBI-01, HBI-04, HBI-05, HBI-07, HBI-08, HBI-25, HBI-26). This follows the core 71-case corpus practice of treating rigorous external evaluation as documentation of failure.
- Several ambient-scribe and drug-discovery cases are currently B-tier; promotion to A-tier awaits peer-reviewed retrospective evaluation.
