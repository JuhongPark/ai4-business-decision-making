# Incident Dataset Recoded Against the Sales-vs-Productization Decomposition

status: research_complete
date: 2026-04-21
purpose: Stream B deliverable from the `sales-vs-productization-research-plan.md`. Recodes the 20 structured incidents in `alignment-failure-mapping.md` against the sales-skill × productization-skill 2×2 matrix. Tests whether the decomposition is consistent with the project's anchor evidence base, and surfaces patterns the earlier Amodei/Weidinger coding did not.

---

## 1. Method

The 20 incidents coded in [`alignment-failure-mapping.md`](../business-alignment/incidents/alignment-failure-mapping.md) (10 general AI + 10 LLM-specific) are the structured subset of the project's broader incident inventory. Each incident is recoded here with four new labels:

- **Sales skill strength at firm at time of incident** (L/M/H): the firm's brand, distribution, customer relationships, and investor access at the relevant moment.
- **Productization skill strength at firm at time of incident** (L/M/H): the firm's data, model, MLOps, eval, and verification infrastructure at the relevant moment. For this label "firm" means the producer of the AI system, not the buyer — so for Workday-as-vendor the Workday coding is used, not the customer's.
- **Quadrant**: Both strong / Sales ahead of product / Product without GTM / Both weak / Not matrix-applicable.
- **Dominant failure locus**: productization / sales / both / information-governance (out of matrix).

The "Not matrix-applicable" category is used when the incident is about internal employee use (Samsung) or about a tool so narrow in scope that the matrix does not cleanly apply (Amazon's internal recruiting tool, which was never commercialised).

Incident dates and facts are taken directly from the alignment-failure-mapping document. No new primary research is added in this stream — the purpose is to test whether the decomposition is consistent with evidence the project already owns.

---

## 2. Full recoding table

### 2.1 General AI incidents

| # | Incident | Year | Sales skill | Productization skill | Quadrant | Dominant failure locus |
|---|---|---|---|---|---|---|
| 1 | Zillow Offers wind-down | 2021 | H (major real-estate brand, recently IPO'd iBuying narrative) | M (ML team present; forecast validation weak for volatile markets) | Sales ahead of product | Both — productization failure (forecast quality) compounded by sales/management over-delegation |
| 2 | Amazon recruiting tool | 2018 | H (corporate brand) but internal tool, not commercialised | M (Amazon ML capability strong; fairness audit absent) | Not matrix-applicable (internal tool) | Productization (biased training data, no fairness audit) |
| 3 | Uber ATG Tempe crash | 2018 | H (rapid investor-facing AV narrative) | L (NTSB found inadequate safety culture, poor operator oversight) | Sales ahead of product | Productization (safety culture, operator design) pressured by sales-driven deployment pace |
| 4 | Meta housing ads | 2022 | H (dominant ad platform) | M (ad-delivery systems mature; fairness-audit sub-component weak) | Both strong, productization gap in fairness | Productization (fairness engineering sub-skill absent) |
| 5 | Rite Aid facial recognition | 2023 | H (major retailer) | L (procured vendor tech with weak accuracy; poor safeguards per FTC) | Sales ahead of product | Both — vendor sales persuasion + Rite Aid productization-side absence of validation |
| 6 | iTutorGroup age discrimination | 2022 | M (online tutoring brand) | L (rule-based age exclusion, not sophisticated AI) | Both weak | Productization (discriminatory rules baked in) |
| 7 | Workday algorithmic hiring | 2024 | H (enterprise HR software leader) | M (mainstream HR tech, moderate AI) | Sales ahead of product | Sales (sold as objective screening; productization under-disclosed limits) |
| 8 | SafeRent tenant screening | 2023 | M (mid-market screening vendor) | L (disparate impact unaudited) | Sales ahead of product | Productization (no fairness audit) |
| 9 | RealPage rental pricing | 2024 | H (major rental pricing vendor) | M–H (sophisticated algorithms, wrong objective) | Both strong | Both — productization engineered for coordination; sales sold it as competitive tool |
| 10 | FloatMe cash advance | 2024 | M–H (fintech with "AI underwriting" marketing) | L (FTC found deceptive claims about algorithmic decisioning) | Sales ahead of product | Sales (deceptive claims beyond product capability) |

### 2.2 LLM-specific incidents

| # | Incident | Year | Sales skill | Productization skill | Quadrant | Dominant failure locus |
|---|---|---|---|---|---|---|
| 11 | Air Canada chatbot | 2024 | H (major airline) | L (chatbot not grounded in actual policies, no ground-truth enforcement) | Sales ahead of product | Productization (RAG / policy-grounding absent) |
| 12 | Mata v. Avianca | 2023 | L (solo / small firm attorneys) | L (general ChatGPT, no verification infrastructure) | Both weak | Productization (no verification) — also cited in scale-based track as S5 Solo exemplar |
| 13 | AP Electric sanctions | 2025 | L (small firm attorneys) | L (general LLM, no cite-check) | Both weak | Productization (no verification) |
| 14 | Samsung ChatGPT ban | 2023 | H (Samsung brand) | M (Samsung has substantial internal AI capability) | Not matrix-applicable (employee use, not Samsung's AI product) | Information governance (prompt-based data boundary) |
| 15 | Google Bard demo | 2023 | H (Google brand, public demo stakes) | M–H (Bard was a real product, factually mis-stated in demo setup) | Sales ahead of product (launch narrative ran ahead of pre-demo fact-check) | Sales (rushed launch exposed productization calibration gap) |
| 16 | Google Gemini image generation | 2024 | H (Google brand) | M–H (Gemini real product; safety mechanism over-corrected) | Both strong | Productization (safety alignment produced unintended discriminatory output) |
| 17 | CNET / Red Ventures | 2023 | H (CNET brand, audience reach) | L (AI content generation without editorial review or disclosure) | Sales ahead of product | Productization (no editorial review pipeline) + disclosure (sales-side) |
| 18 | Chicago Sun-Times AI book list | 2025 | M (newspaper brand, freelance supplement) | L (freelancer generated content without verification) | Both weak | Productization (no verification; freelancer case) |
| 19 | DPD chatbot rogue behaviour | 2024 | H (DPD delivery brand) | L (chatbot not robust to adversarial prompts) | Sales ahead of product | Productization (no adversarial testing) |
| 20 | Elegant Enterprise AI job ads | 2026 | M (small firm) | L (AI-generated job ads, no content screening) | Both weak | Productization (no content review) |

---

## 3. Distribution

Across the 20 incidents:

| Quadrant | Count | Share |
|---|---|---|
| **Sales ahead of product** (sales H/M, productization L) | **10** | 50% |
| **Both weak** | 5 | 25% |
| **Both strong** (with productization-sub-skill gap) | 3 | 15% |
| **Not matrix-applicable** (internal / information governance) | 2 | 10% |
| **Product without GTM** | 0 | 0% |

By dominant failure locus:

| Failure locus | Count | Share |
|---|---|---|
| Productization (primary) | 12 | 60% |
| Both sales and productization | 4 | 20% |
| Sales (primary) | 3 | 15% |
| Information governance / out-of-matrix | 1 | 5% |

---

## 4. Findings

### 4.1 The "sales ahead of product" quadrant is the modal documented failure

Exactly half of the 20 structured incidents sit in the sales-ahead quadrant. This is the upper-right cell of the decomposition memo's §4 matrix. The documented failure cases are disproportionately firms where the sales function produced a claim or deployed a product that the productization function had not built to the level the claim implied.

This is the strongest single finding. The decomposition memo's §5 case list (Klarna, Humane, Builder.ai, Nate Inc., Character.AI, Deloitte AU) is not an isolated cluster — it extends to the project's anchor evidence base. The memo's claim that "most documented failures are sales-ahead-of-product cases" is consistent with the 20-incident coded sample.

### 4.2 "Product without GTM" is absent — and the absence is explainable

No incident in the dataset sits in the lower-left quadrant (product strong, sales weak). The decomposition memo named this quadrant as real (Humane's acquihired engineering org, EleutherAI, pre-commercial labs, AI assurance tooling startups) but the 20-incident sample has no exemplar.

**Why**: incidents enter the inventory via public visibility — regulatory action, litigation, press coverage, product rollback. Firms with strong productization but weak sales rarely become public at incident scale because they never reach the deployment volume that creates the incident surface. The absence of "product without GTM" in the incident inventory is a selection effect of the inventory itself, not a claim that the quadrant is empty.

This is a methodological note the decomposition memo should add: the 2×2 matrix has four quadrants, but only three quadrants produce incidents at public-inventory scale.

### 4.3 "Both weak" clusters at S5 Solo and small-firm exemplars

All 5 "both weak" cases are small firms or individuals: iTutorGroup (small-sample discrimination rules), Mata / AP Electric (solo attorneys), Chicago Sun-Times freelancer, Elegant Enterprise (small firm). This directly corresponds to the scale-based track's S5 Solo tier (Charlotin corpus, 1,174+ cases) and S1 sub-populations.

The decomposition memo's §6 tier table predicted that S5 Solo and S1 uniformly sit in the lower-right quadrant. The incident coding confirms the prediction with 5/5 of the "both weak" cases fitting that tier prediction.

### 4.4 "Both strong" cases reveal a productization sub-skill gap

The three "both strong" cases — Meta housing ads, RealPage, Google Gemini image gen — are firms that have substantial sales skill AND substantial productization skill, but a specific productization sub-skill failed:

- **Meta housing ads**: ad-delivery productization mature; fairness-audit sub-skill absent.
- **RealPage**: pricing-algorithm productization sophisticated; productization was deliberately engineered for anti-competitive coordination, which is a sales-adjacent product choice (maximising landlord revenue).
- **Google Gemini image**: image-generation productization mature; safety-alignment sub-skill over-corrected.

The decomposition memo's §2.2 lists nine productization sub-dimensions (data, model, MLOps, eval, verification, monitoring, inference, plus speed and resources on the productization dimension). The "both strong" incidents show that productization is not a single scalar — a firm can be strong on most sub-dimensions and still fail through a single weak sub-component. The memo should add this nuance to §2.2: productization skill is a vector, not a scalar.

### 4.5 "Not matrix-applicable" cases identify a scope boundary

Two cases (Amazon internal recruiting, Samsung ChatGPT ban) do not fit the matrix. Neither is an organisational AI-product deployment. Amazon is internal tooling that was never commercialised. Samsung is an employee-use case where the "firm's AI product" is not the relevant unit of analysis.

This identifies a decomposition scope boundary the memo did not state explicitly:

> The sales-productization decomposition applies to firms producing AI products or AI-driven services. It does not apply to internal-only AI tooling, to employee use of third-party AI, or to information-governance incidents where the boundary failure is between users and external tools rather than between firm-produced product and firm-sold narrative.

This boundary should be stated in the memo's §11 limitations.

### 4.6 Productization failures dominate the dominant-failure-locus coding

12 of 20 incidents have productization as the primary failure locus, 4 have both sales and productization, 3 have sales primary, and 1 is out-of-matrix. This is not inconsistent with the sales-ahead-of-product quadrant count (10) — the two codings measure different things:

- **Quadrant** describes the firm's skill *balance* at time of incident.
- **Failure locus** describes *where* the incident actually went wrong.

A firm in the sales-ahead-of-product quadrant can fail at the productization layer (Air Canada chatbot: sales ahead, productization layer is where the RAG grounding was missing) or at the sales layer (FloatMe: sales ahead, sales claims beyond product capability were the specific legal issue) or both (Rite Aid: vendor sales pitch + buyer productization validation absent).

The cross-tabulation:

| Quadrant / Locus | Productization | Sales | Both | Out-of-matrix | Total |
|---|---|---|---|---|---|
| Sales ahead of product | 7 | 2 | 1 | 0 | 10 |
| Both weak | 5 | 0 | 0 | 0 | 5 |
| Both strong | 2 | 1 | 0 | 0 | 3 |
| Not matrix-applicable | 0 | 0 | 0 | 1 (+1 productization) | 2 |

The pattern: even in the "sales ahead" quadrant (where the imbalance is the conceptual story), the specific point of failure is usually in productization. Sales ahead is the *condition*; productization gap is the *mechanism*.

### 4.7 The framework detection rate reanalysis

The alignment-failure-mapping document reports that the 6-dimensional framework would have flagged 12/20 incidents outright, 7/20 partially, and 1/20 not captured. The decomposition allows a parallel analysis:

- All 10 sales-ahead-of-product incidents fail specifically at productization sub-skills that the 6-dimensional framework's "evidence strength" and "governance readiness" dimensions partially proxy for, but do not fully capture.
- The 5 both-weak incidents fail at S5 Solo / S1 productization floor — the scale-based track names this as a public-good problem, not a framework problem.
- The 3 both-strong incidents fail at productization *sub-skills* — a failure mode the 6-dimensional framework is least equipped to flag because the aggregated dimension scores look fine.
- The 2 not-matrix-applicable cases are outside the decomposition's scope.

**Implication**: the 6-dimensional framework's dimension-5 "evidence strength" and dimension-6 "governance readiness" are productization-skill proxies. They work well when productization is uniformly weak (capturing both-weak cases). They work less well when productization is strong on most sub-skills but has a specific weak sub-component (both-strong cases). A framework revision could add a "productization sub-skill audit" to dimension 5 or 6.

---

## 5. What this stream adds to the decomposition memo

Five additions the main memo should incorporate:

1. **The 50% sales-ahead-of-product rate in the structured incident sample.** This is a quantitative anchor the memo §5 lacked.
2. **The "product without GTM" absence is a selection effect of the incident inventory.** Add as a methodological note in §11.
3. **The "both weak" cluster confirms the S5 Solo / S1 tier predictions.** Strengthens H5 in §8.
4. **Productization is a vector, not a scalar — sub-skill failures produce incidents even in both-strong firms.** Add to §2.2 definitions.
5. **The decomposition's scope boundary is firms producing AI products, not internal tooling or employee use.** Add to §11 limitations.

---

## 6. What this stream leaves for future work

- **Extension beyond the 20 coded cases.** The project's broader 71-case narrative inventory has cases (Character.AI, Nate Inc., Humane, Klarna, Builder.ai, Deloitte AU, Cursor, Perplexity) that are cited in the decomposition memo §5 but not in the structured alignment-failure-mapping. A fuller recoding would cover all 71.
- **Test against new 2026 incidents.** The incident inventory stops in early 2026. The decomposition would benefit from forward testing — does it predict the failure patterns of Q2/Q3 2026 incidents (not yet inventoried)?
- **Recode against tier classification.** Each incident has an implicit scale-based tier; a combined (tier × quadrant) classification would produce a richer cross-tab.

---

## 7. Cross-references

- [`alignment-failure-mapping.md`](../business-alignment/incidents/alignment-failure-mapping.md) — the 20-incident structured inventory this stream recodes.
- [`incident-inventory.md`](../business-alignment/incidents/incident-inventory.md) — the fuller narrative inventory.
- [`sales-vs-productization-decomposition.md`](sales-vs-productization-decomposition.md) — the main memo this stream tests and strengthens.
- [`sales-vs-productization-research-plan.md`](../../operations/expansion/sales-vs-productization-research-plan.md) — the Stream B specification.
