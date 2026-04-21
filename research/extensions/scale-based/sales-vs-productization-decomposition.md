# Sales Skill and Productization Skill: A Two-Dimensional Decomposition of AI Adoption

status: research_complete
date: 2026-04-21
purpose: Supplementary memo to the scale-based track. Decomposes the `size-speed-resource-tradeoff.md` memo's three-axis framing (speed, resources, verification quality) into two distinct firm-level skills — **sales skill** (sales and investment) and **productization skill** (product implementation only). Shows that speed and resources decompose asymmetrically across the two skills, that verification quality lives almost entirely inside productization skill, and that the three load-bearing findings of the scale-based track become sharper when the decomposition is applied.

---

## 1. Why this memo exists

The `size-speed-resource-tradeoff.md` memo established that AI adoption has three axes — speed advantage, resource advantage, and verification quality — and that the three are not located on a single tradeoff curve. That framing treated the firm as a monolithic actor with a single adoption profile. It is productive but compresses a distinction that the external empirical literature now makes visible.

This memo splits the firm into two skills:

- **Sales skill (sales and investment)** — the firm's capability to persuade *external capital-holders* to pay for its AI. "Capital-holders" covers both customers (paying for sales) and investors (paying for funding). Both are fundamentally about convincing others to pay; they share a common substrate of positioning, narrative, trust, brand, and distribution.
- **Productization skill (product implementation only)** — the firm's capability to build the AI product. The purely technical act of shipping a working system: data acquisition, model development, MLOps, evaluation, verification infrastructure, monitoring, inference. *Not* pricing, positioning, fundraising narrative, or customer success.

The decomposition is not an arbitrary reorganisation. It matters because:

1. **The three axes from the tradeoff memo decompose asymmetrically.** Speed advantage of small firms applies to productization but not always to sales cycle. Resource advantage of large firms applies to sales cleanly but to productization only non-monotonically. Verification quality lives almost entirely in productization skill and is consumed by sales skill as instruments.
2. **Firms routinely exhibit strong one skill and weak the other.** The literature documents cases — Klarna, Humane, Deloitte Australia, Nate Inc., Builder.ai — where sales skill ran ahead of productization skill. And cases — Humane's engineering org, early Anthropic, Singapore AI Verify — where productization skill exists without proportionate sales skill. The decomposition lets the repo name the asymmetry directly.
3. **The scale-based track's three load-bearing findings become sharper under the decomposition.** "Infrastructure, not headcount, predicts verification quality" becomes "*productization* infrastructure predicts verification *substance*, while *sales* infrastructure predicts verification *claims*." The 66%/91% overtrust finding becomes the predicted equilibrium of sales narrative × productization shortfall. The public-good threshold runs through both skills.

The memo is analytical, not prescriptive. It does not propose a new framework; it refines the interpretation of the scale-based track's existing findings by splitting them along a new axis.

---

## 2. Defining the two skills

### 2.1 Sales skill (sales and investment)

| Sub-dimension | What it is | 2025-2026 empirical anchors |
|---|---|---|
| **Positioning and messaging** | Framing the product category, target persona, differentiation | Harvey positions as "vertical AI for law"; Sierra positions as "customer support AI"; thin wrappers collapse when category gets taken by frontier lab (PDF-chat wrappers 2024) |
| **Pricing power** | Willingness-to-pay extraction; model (per-seat, usage, outcome, hybrid) | Metronome 2025: seat-based 21% → 15%; hybrid 27% → 41%; per-seat AI has 40% lower gross margins and 2.3× higher churn than usage/outcome alternatives; Salesforce reversed *back* to seat-based with credits in Dec 2025 because buyers prefer predictability |
| **Sales motion** | PLG, enterprise sales, channel, or hybrid | Cursor $1B+ ARR with <50 employees via PLG + developer virality; Sierra $150M ARR via enterprise sales; Scale AI $29B via sales-led; hybrid dominant |
| **Customer acquisition and retention** | Lead generation, conversion, NRR, churn | AI deals close 2× faster than traditional SaaS but only in AI-native vendors; 47% of AI pilots reach production vs ~25% for traditional SaaS (Menlo 2025) |
| **Brand and distribution moat** | Installed-base leverage, switching costs, trust | Microsoft 365 Copilot 16.1M paid seats; 90%+ Fortune 500; Salesforce 202,600 customers vs 91,400 at Microsoft; a16z 100-CIO: incumbents win on switching cost, AI-natives win on product-velocity |
| **Fundraising capability** | VC, PE, strategic, public-markets | Q1 2026: $242B of global VC (80%) went to AI; $188B (65%) went to four frontier labs; late-stage AI +140% YoY; seed AI at 42% valuation premium |
| **Speed on the sales dimension** | Cycle time, messaging pivot, vertical pivot | B2B cycle extended to 6.5 months overall; AI-native shortens to ~3-4 months; small vendors pivot narrative in weeks, large vendors cannot |
| **Resources on the sales dimension** | Brand equity, salesforce headcount, investor network, marketing spend | Linear with firm size for most sub-components; frontier startups buy the resource via hires (Cohere hired Joelle Pineau) |

### 2.2 Productization skill (product implementation only)

| Sub-dimension | What it is | 2025-2026 empirical anchors |
|---|---|---|
| **Data acquisition and quality** | Training data, labelling, RAG grounding, feature stores | RSM 2025: 41% of mid-market cite data quality as top AI problem; Databricks names data lineage as load-bearing |
| **Model development** | Training, fine-tuning, RAG architecture, prompt engineering | AI-native (Anthropic, OpenAI, Cohere, Mistral) vs AI-using (Harvey, Cursor, Perplexity) vs pure wrapper; Perplexity hybrid — Vespa retrieval + own Sonar fine-tunes + frontier APIs |
| **MLOps and deployment** | Pipelines, CI/CD for ML, rollback | Databricks 2025: 11× YoY production deployment growth; DORA 2025: AI adoption correlates positively with throughput but negatively with stability |
| **Evaluation infrastructure** | Eval harness, benchmarks, red-team | Anthropic: capability, safety, alignment evaluations pre-deployment; Meta Llama 3.1 used 150+ benchmarks + 1,800-prompt internal eval; OpenAI "eval-driven development"; Harvey publishes VLAIR scores; lm-evaluation-harness 5,000+ citations |
| **Verification infrastructure** | Per-decision logs, confidence APIs, reasoning traces | Microsoft AETHER + Sensitive Uses (mixed eng/policy/ethics); JPMorgan 2,000 AI/ML specialists + Model Risk Governance; Anthropic Frontier Red Team (research-framed); Singapore AI Verify open-source modular |
| **Monitoring and drift management** | Production monitoring, drift detection, feedback loops | MIT: 91% of ML models degrade over time without monitoring; 75% of firms saw AI perf decline without monitoring; >50% reported measurable revenue losses |
| **Inference infrastructure** | Compute, latency, cost, GPU access | GPU shortage through Q3 2026; HBM triopoly; hyperscaler forward orders absorbed most 2027 Blackwell allocation; inference = 55–80% of enterprise AI GPU spend |
| **Speed on the productization dimension** | Engineering cycle, deploy frequency, feature velocity | Small firms ship MVP in 6 weeks vs 6 months at large firms (Advancio 2025); Thoughtworks Tech Radar 33 names "context engineering" as architectural concern |
| **Resources on the productization dimension** | ML engineer headcount, compute budget, proprietary data, eval staff | **Non-monotonic with firm size**. JPMorgan 2,000 specialists + $17B tech; Anthropic <2,000 total but eval infrastructure denser than most Fortune 500; frontier labs concentrate productization resources that S4 typical firms spread thin |

### 2.3 Why this decomposition, not others

Alternative decompositions exist (technical/business; engineering/go-to-market; model/product). The sales + investment / productization split is preferred for three reasons specific to the scale-based track:

1. **It isolates the variable that predicts verification quality.** Verification infrastructure is a productization output. By separating it from sales/investment skill, the memo can state clean predictions about where verification will be substantive (high productization skill) vs where it will be performative (high sales skill without proportionate productization skill).

2. **It matches how the external literature actually describes the problem.** The SEC/FTC AI-washing enforcement (Presto, Nate Inc., Delphia, Global Predictions, Rite Aid), the MIT 95% pilot failure finding, the Klarna/Duolingo rollbacks, and the Humane/Rabbit failure cases all point at the same pattern — sales narrative out of proportion to productization substance. Naming the asymmetry explicitly gives the pattern a vocabulary.

3. **It integrates sales and investment into a single skill because they share the same substrate.** Customers and investors are both external capital-holders being persuaded; the literature on "AI washing" treats the two as a single class (SEC ScrutINY covers both investor disclosures and customer-facing claims). Splitting them would obscure the shared skill. Splitting productization further (into data / model / MLOps) is useful for sub-analysis but not for the top-level decomposition.

---

## 3. Re-mapping the three axes from size-speed-resource-tradeoff

The tradeoff memo proposed speed (small-firm advantage), resources (large-firm advantage), and verification quality (independent third axis). The decomposition shows that each axis decomposes differently across the two skills.

### 3.1 Speed decomposes asymmetrically

| | **Sales-skill speed** | **Productization-skill speed** |
|---|---|---|
| Small firms | Ambiguous. AI-native vendors close 2× faster than traditional SaaS but overall B2B cycle *lengthened* to 6.5 months. Small vendors without AI-native narrative may be slower than incumbents. | **Consistent advantage.** MVPs in 6 weeks vs 6 months; Cursor reached $2B ARR with ~50 engineers; solo founders ship with Cursor/Claude Code. |
| Large firms | **Underappreciated advantage**: existing customer relationships collapse the sales cycle for cross-sell. Microsoft sold Copilot to 90%+ of Fortune 500 via Azure/M365 contracts — a cycle small vendors cannot match on the same customer base. Salesforce Agentforce reached $800M ARR in 15 months primarily through installed-base upsell. | Slow. Committee structures, procurement, security review, legal review; a four-week rollout stretches to four months (AuFait). |
| Middle market (S3) | Worst of both. Not fast enough to pivot like S2; no installed base like S4. | Worst of both. 74% of mid-market lack in-house AI expertise (KeyBank 2025); 62% find AI harder to implement than expected (RSM 2025). |

**What the tradeoff memo got right and what the decomposition sharpens.** The "small firms ship faster" claim holds on the productization dimension; it holds *conditionally* on the sales dimension (only when the firm is AI-native and the product sells through PLG). For traditional-SaaS-shaped firms, sales cycles at Series B-D vendors are now longer than Fortune 500 cross-sell cycles. The speed advantage is not a monolithic small-firm property.

### 3.2 Resources decompose asymmetrically

| | **Sales-skill resources** | **Productization-skill resources** |
|---|---|---|
| Small firms | Typically weak. No brand, limited salesforce, no distribution moat, fragile investor network. Exception: frontier labs (Anthropic, OpenAI, xAI) absorbed 65% of Q1 2026 global VC — a sales/investment resource position that dwarfs most Fortune 500. | **Bimodal**. AI-native firms (Anthropic ~2,000 staff; Cursor ~50 at $2B ARR) concentrate more purpose-built productization resource per decision than most S4 typical firms. AI-using firms rent from vendors and have essentially zero training/eval stack. |
| Large firms | **Strongest advantage.** Brand, salesforce (Salesforce: 202,600 customers to upsell; Microsoft: 415M commercial seats to convert); distribution moat; D&O insurance; legal/IR capacity. Linear with firm size. | **Non-monotonic.** JPMorgan 2,000 specialists with Model Risk Governance is a substantive productization resource. Meta AI auto-review is an S4 firm with weak per-decision productization substance. The resource is there but is not deployed into verification infrastructure unless a regulator or internal ethics function forces it. |
| Middle market (S3) | Weak. Limited brand relative to S4, limited pivot speed relative to S2. | Weak. 70% of mid-market say they need outside help; 47% of dedicated AI budget goes to consulting (RSM 2025). Productization is rented. |

**Reframing.** The tradeoff memo's resource advantage claim is cleanest on sales-side resources, where firm-size scaling is close to linear. It is non-monotonic on productization-side resources, where purpose-built allocation (frontier-lab S2, S4 substantive) beats diffuse allocation (S4 typical, Fortune 500 spread across many products). This is the mechanism behind Finding 1 — **"infrastructure, not headcount, predicts verification quality"** — and the decomposition lets the mechanism be stated precisely: *productization* headcount distributed into *verification infrastructure* predicts verification substance; sales headcount does not.

### 3.3 Verification quality lives in productization skill — and is consumed by sales skill as instruments

Verification quality is almost entirely a productization output. The components that produce it — eval harnesses (Anthropic, OpenAI, Meta Llama 150+ benchmarks + 1,800-prompt internal eval), red teams (Anthropic FRT), model risk governance (JPMorgan), sensitive-uses review (Microsoft AETHER), assurance testing (Singapore AI Verify) — are all engineering functions. None is a sales or marketing function.

Sales skill, however, *consumes* verification output in the form of sales instruments:

- **Compliance badges** — SOC 2, ISO 42001, ISO 27001, HIPAA attestations.
- **Trust Centers** — public-facing compliance portals.
- **Model cards and system cards** — published technical documentation.
- **Governance disclosures** — RSPs, AI governance alliance memberships, transparency reports.
- **Framework certifications** — "NIST AI RMF aligned," "EU AI Act ready."
- **Insurance** — D&O and cyber insurance policies that name AI specifically.
- **Third-party audits** — Big Four SOC 2 audits, AI-specific audit firms.

These instruments are products of the sales/trust-communication function, not of the verification function. A firm can produce them without producing substantive verification. The external literature now documents the gap explicitly: the SEC's "AI washing" actions against Presto Automation (Jan 2025), Nate Inc. ($42M fraud, Philippines contractors), Delphia, and Global Predictions all describe cases where sales-instrument verification (marketing claims about AI capabilities) had no corresponding productization substance. The FTC's "Operation AI Comply" (Sep 2024, continuing) brought at least a dozen similar cases in 2025.

The decomposition therefore names a structural gap:

> **Verification quality splits into verification *substance* (produced by productization skill) and verification *claims* (produced by sales skill). These can diverge arbitrarily. When claims run ahead of substance, the firm ships unverified AI with verified-sounding messaging.**

This is the core decoupling the memo identifies. §5 develops it into a matrix of cases.

---

## 4. The sales-productization skill matrix

A 2×2 matrix of firms by sales skill (low/high) × productization skill (low/high) clarifies the decoupling. The cells are populated with 2025-2026 evidence from the scale-based tier reports and the external literature.

| | **Productization skill: HIGH** | **Productization skill: LOW** |
|---|---|---|
| **Sales skill: HIGH** | **"Balanced frontier"** — both strong, verification substance + claims aligned. Anthropic (13/15 RVCS-1, 40% enterprise share), Microsoft AETHER + Sensitive Uses (14/15), JPMorgan MRG, Singapore AI Verify (12/15), Harvey AI (published 94.8% Document Q&A, $195M ARR), Sierra ($150M ARR), OpenAI (top of eval benchmarks + 27% enterprise share). | **"Sales ahead of product"** — the governance-theater / AI-washing cell. Klarna AI-first reversal (sold story succeeded; product delivered worse service; 700 CS agents re-hired), Duolingo (walked back AI-first within a week), Humane AI Pin (sold as smartphone replacement; returns exceeded sales; bricked Feb 2025), Rabbit R1, Builder.ai ($1.2B valuation, bankruptcy; product relied on human engineers), Nate Inc. ($42M raised; Philippines contractors), Presto Voice, Deloitte Australia (A$440K fabricated citations), Cursor wrappers circa 2024, Meta auto-review (5/15). |
| **Sales skill: LOW** | **"Engineering without go-to-market"** — productization substance exists without proportionate commercial pull. Humane's engineering org specifically (acquihired by HP for $116M after product collapsed — signal that eng had value even as product did not); pre-commercial labs (EleutherAI, early Cohere); government AI testing facilities (Singapore AI Verify before commercialisation, UK AISI); most academic AI groups; Patronus AI, Galileo, Arize at early stage (strong productization of eval tooling, sales still building). | **"Structurally weak"** — both low. S5 Solo attorneys filing hallucinated citations (1/15); S1 founders shipping landing pages (0/15); S3 typical middle-market (weak brand AND 74% lack in-house expertise); retail investors producing AI-generated stock theses (0/15); failed thin wrappers (60–70% generate zero revenue; 95% of pilots deliver no P&L — MIT State of AI in Business 2025). |

Four observations from the matrix:

1. **The upper-right cell (sales-ahead-of-product) is the most instructive cell.** It is where the verification-claim / verification-substance gap is maximised. Every named case is a firm that sold AI capability that its productization had not built.
2. **The lower-left cell (engineering-without-go-to-market) explains Humane's asset sale.** HP paying $116M for a bankrupt firm's engineering org, OS, and patents is a clean statement that productization has standalone market value even when sales skill has collapsed. The engineering was not lost; it was repriced.
3. **The upper-left cell (balanced frontier) is where the PwC top-20% live.** The PwC 2026 finding that 20% of companies capture 75% of AI economic gains is well predicted by asking which firms have both skills. The other 80% have one or neither.
4. **The lower-right cell is where the scale-based track's public-good argument applies most directly.** Firms in the lower-right cannot privately produce either verification substance (no productization skill) or verification claims (no sales skill). External infrastructure is needed.

---

## 5. The verification-claim / verification-substance gap: case analysis

The upper-right cell of the matrix is the site of most documented AI failures. The decomposition lets the failures be named more precisely than "AI washing" or "governance theater." In each case the sales function produced an artifact (a claim, a badge, a disclosure) that the productization function had not produced as substance.

| Case | Sales claim | Productization shortfall | Resolution |
|---|---|---|---|
| **Klarna AI-first** (2024-25) | Sold "AI replaces 700 CS agents" to public markets; press, investor, narrative all worked | Chatbot service quality fell measurably; customer complaints rose | CEO reversed in 2025; re-hired agents; stock narrative cost exceeded productization savings |
| **Humane AI Pin** (2023-25) | Sold as smartphone replacement; $230M+ raised on the claim | Battery fire risk; returns outpaced sales summer 2024; price cut $200 in Oct 2024 | Bricked Feb 2025; HP acquihired engineering for $116M |
| **Rabbit R1** (2024-25) | Sold "Large Action Model" that performs any task | Demo-only capability; core promised features never shipped | Steady product decline; post-mortems cite "shipped based on roadmap, not on what works today" |
| **Builder.ai** (2016-25) | Sold "AI builds apps for anyone"; Microsoft-backed at $1.2B | Core delivery relied on human engineers, not autonomous AI | Bankruptcy 2025 |
| **Nate Inc.** (2018-25) | Raised $42M on AI-shopping-app claim | Transactions processed by Philippines contractors | SEC/DOJ fraud charges Apr 2025 |
| **Presto Voice** (pre-2025) | Overstated drive-through AI capability; did not disclose third-party AI or human intervention | Heavy human-in-the-loop required | SEC enforcement Jan 2025 (first public-company AI-washing case) |
| **Deloitte Australia** (2025) | Sold A$440K government report with AI-generated citations | Citations fabricated; productization-grade cite-check absent | Refund; reputational damage |
| **Meta auto-review** (2025) | Responsible AI apparatus publicly cited | Per-decision review outsourced to AI itself (5/15 RVCS-1) | Ongoing incident exposure |
| **Character.AI** (2023-25) | Marketed as safe companion product | Q3 normative review absent (deliberate product incentive to maximise engagement) | Wrongful-death litigation, Texas AG, country-level bans |
| **Cursor enterprise wrapper** (2024-25) | Sold enterprise-safe AI coding | Per-decision eval minimal (5/15 RVCS-1 at typical use) | Cursor reacted by investing in enterprise features at higher ARR |

The pattern is not rare. The MIT State of AI in Business 2025 finding that 95% of enterprise GenAI pilots deliver no measurable ROI, against 2024-25 global GenAI spend of ~$30-40B, is consistent with a population where sales skill pulls spend that productization skill cannot convert to business outcomes. The MIT "67% succeed for purchased AI vs 33% for internal builds" finding is the buyer-side mirror: buying from a vendor with demonstrable productization skill beats building with the buyer's own weak productization skill by 2×.

---

## 6. Decomposition across the seven tiers

Applying the two-skill lens to the scale-based comparative matrix produces a tier-by-tier decomposition.

| Tier | Sales skill profile | Productization skill profile | Dominant failure mode in decomposition terms |
|---|---|---|---|
| **S7 International institutions** | Sales substitute is *legitimacy* — multi-state adoption, treaty ratification, donor coordination. Not commercial. | Productization substitute is *peer review* and *document genealogy*. No per-claim engineering. | Legitimacy laundering downward: S7 outputs become binding national law without productization-grade verification. |
| **S6 National governments** | Sales substitute is *public accountability* — procurement votes, parliamentary confirmation. Not commercial. | Productization substitute is *regulatory pre-deployment testing* (AI Verify, FRIA templates). Per-decision productization absent. | Reasoning-erasure under FOIA (MuckRock 2025). Singapore AI Verify is the counterexample that proves S6 can build productization-grade verification when it chooses. |
| **S5 Big Law** | **High sales skill** — brand, firm reputation, partner network, client trust, referral chains are the moat. | **Productization is a manufactured human pipeline substitute** — cite-check layer + partner sign-off acts as the productization of verification. Harvey, CoCounsel, Westlaw Precision are rented productization. | When the human pipeline is present (Big Law with SOP): 11/15 RVCS-1. When sales inherits the brand without the pipeline (e.g., Ellis George): 4/15. The variance is in productization, not in sales. |
| **S5 Solo** | Low sales skill (no referral network, no brand-protected trust) AND inherits full S5 liability from bar membership. | Low productization (general-purpose ChatGPT; no SOP; no cite-checker; no vendor-grade tool). | 1,174+ Charlotin corpus: 89.9% of sanctioned hallucination cases are solo/small. Both skills are absent; the bar license imports S5 sanctions on S1 skills. |
| **S4 substantive (Microsoft AETHER, JPMorgan MRG, GE HealthCare FDA)** | **High sales skill** — brand, installed base, executive relationships. | **High productization skill**, deliberately channelled into verification infrastructure. 14/15 RVCS-1 at Microsoft; JPMorgan 2,000 AI/ML specialists. | Substantive cases are the upper-left quadrant made real. Forced from outside — FDA, EU AI Act, SR 11-7 examinations, internal ethics committees. |
| **S4 typical (Meta auto-review, Fortune 500 average)** | High sales skill at institutional level (brand, distribution, D&O insurance, compliance narrative). | **Low per-decision productization skill**. Apparatus-level productization exists (OneTrust, Credo AI, Fiddler) but the verification function at the analyst's desk is absent. 66% of employees accept AI without evaluation. | **Governance theater** is the pure upper-right quadrant expression. The sales/apparatus function publishes governance; productization at the point of use does not back it. |
| **S3 Mid-sized enterprises** | Weak sales skill (less brand than S4, less pivot speed than S2); middle-market squeeze. | Weak productization skill (74% lack in-house expertise; everything rented from vendors; SOC 2 Type II / ISO 42001 substituted for substantive Q3). | Both skills compressed. Q1 and Q4 collapse first. Q2 survives only through pre-existing professional practice. Q3 substituted wholesale by vendor attestations. |
| **S2 AI-native** (Anthropic, OpenAI, Cohere, Mistral) | Sales skill rising fast (Q1 2026 VC dominance, 40% Anthropic enterprise share); earlier stage, strong investor skill. | **High productization skill.** Research-lab alumni as founders; eval harnesses, red teams, capability evaluations, RSPs, AISI partnerships. 13/15 RVCS-1 at Anthropic. | When the sales skill catches up with the productization skill, the firm moves into the upper-left quadrant. During the catch-up period, productization substance predates sales claims — the opposite of the governance-theater pattern. |
| **S2 AI-using** (Harvey wrapping, Cursor, Perplexity, Cleo) | Sales skill variable. Harvey built strong enterprise sales from the start; many wrappers are pure sales plays. | Productization skill variable. **Harvey has demonstrable productization (94.8% VLAIR)** despite wrapper critique; Klarna/Character.AI/Cleo have weak productization. The two-population split is really a productization-skill split more than a sales-skill split. | Q3 normative failures dominate (Character.AI, Clearview, DoNotPay, Cleo, Workado) where productization incentives override ethics. |
| **S1 Solo entrepreneurs** | Uniformly weak sales skill (no brand, no distribution moat, thin investor access). Exception: solo founders with verified-exit track records. | Uniformly weak productization skill. Productization through Cursor/Claude Code/Lovable raises the floor but not to S4-substantive levels. | Upper-left quadrant is rare (Base44 exit to Wix, Pieter Levels $3M ARR as solo operator); lower-right quadrant is modal. Public-good threshold applies. |

**What the tier decomposition adds.** The "infrastructure, not headcount" finding is now re-expressible as: within each tier, the firms that score well on verification quality are firms with *productization infrastructure*; the firms that score poorly have *sales infrastructure* without proportionate productization infrastructure. The within-tier variance at S4, S5, and S2 — which the scale-based track already identified as exceeding between-tier variance — is the variance in the productization skill axis specifically.

---

## 7. Reinterpretation of the three load-bearing findings

### 7.1 Finding 1 — Infrastructure, not headcount, predicts verification quality

**Original statement**: The RVCS-1 scores cluster by infrastructure class, not by tier number. Substantive cases (Microsoft 14/15, Anthropic 13/15, Singapore AI Verify 12/15, Big Law + Harvey 11/15) are more similar to each other than to typical cases in their own tiers.

**Decomposed statement**: **Productization infrastructure, not firm headcount or sales infrastructure, predicts verification *substance*. Sales infrastructure predicts verification *claims*.** When the two diverge, a firm produces claims without substance (the governance-theater pattern). When they align, the firm produces substantive verification backed by credible claims (the upper-left quadrant).

**What the decomposition adds to the original finding:**

- The finding was indifferent to *which kind* of infrastructure matters. The decomposition names it: productization infrastructure, specifically the investment in eval harnesses, red teams, per-decision verification tools, and model risk governance.
- The decomposition explains the otherwise puzzling S4-typical case. Meta, GM, and other S4 firms with weak per-decision RVCS-1 scores have *plenty* of sales infrastructure and even plenty of institutional-level governance infrastructure. What they lack is productization-side verification investment at the analyst's desk.
- The PwC 2026 "top 20% capture 75% of gains" finding becomes predictable: the 20% are firms with both sales and productization skill; the 80% have one or neither.

### 7.2 Finding 2 — The 66%/91% overtrust finding is the predicted equilibrium

**Original statement**: The Microsoft 2025 finding (66% of employees accept AI without evaluation) and McKinsey 2024-25 finding (91% of executives agree employees overtrust AI) are the predicted equilibrium of the verification capacity curve, not a cultural failing. The framework assumes conditions (10-50 minutes per-decision verification budget, N>1 reviewers, chain depth >0) that do not exist at S4 typical.

**Decomposed statement**: **The overtrust is the joint failure of sales skill × productization skill.** Sales skill sold AI to executives as capable enough to trust; productization skill did not build the verification affordances (confidence scores, source citations, disagreement surfaces, reasoning traces) that would let users calibrate that trust. The 66%/91% finding is the equilibrium between the narrative the sales function produced *and* the verification surface the productization function did not produce.

**What the decomposition adds to the original finding:**

- The original finding named the budget problem. The decomposition names the narrative problem that makes the budget problem possible. If AI were sold more honestly as "fluent but frequently wrong; verify before commitment," the 66% acceptance rate would be lower even at the same verification budget.
- MIT's 95% pilot failure finding is consistent: sales pull creates pilot spend that productization cannot convert. RAND's "leadership/communication misunderstanding" as top failure cause (2024) names the sales-side half of the failure; MIT's "integration / contextual adaptation" (2025) names the productization-side half. They are the two halves of the same joint failure.
- The intervention implication is two-sided. Reducing overtrust requires either more productization investment in verification surfaces (confidence APIs, reasoning logs, disagreement UX) *or* more honest sales narrative (less confident marketing, explicit uncertainty language in vendor collateral). The scale-based track pointed at the first; the SEC/FTC enforcement agenda pointed at the second. Both are the same intervention in two vocabularies.

### 7.3 Finding 3 — The public-good threshold runs through tiers, not between them

**Original statement**: The boundary below which verification cannot be privately produced is a conditional boundary defined by three co-occurring conditions (infrastructure absence, verifier compression, external-compulsion failure). It appears inside every tier with internal variance. S1 uniformly sits below the boundary.

**Decomposed statement**: **The public-good threshold runs through both skills, not just productization.** Below the threshold, the firm can privately produce neither substantive verification (productization shortfall) nor credible verification claims (sales shortfall). The classical AI-liability literature (AI Frontiers 2025) names this as a sales-adjacent public-good argument: small firms cannot privately produce regulatory compliance, legal defence, or liability insurance. The scale-based track names it as a productization-adjacent argument: small firms cannot privately produce eval, red team, or verification infrastructure. **Both arguments converge on the same structural conclusion from two sides.**

**What the decomposition adds to the original finding:**

- The original finding treated the threshold as a function of co-occurring conditions. The decomposition explains why those conditions co-occur: below a certain scale, both skills reach their public-good floors simultaneously. The capital intensity of sales infrastructure (brand, legal counsel, compliance staff, insurance premiums) and the capital intensity of productization infrastructure (eval engineers, compute, data assets, monitoring) are each above what S1 can privately sustain.
- The three candidate infrastructure designs in the S1 tier report (standardised reasoning audit APIs, verification marketplaces, mandatory vendor disclosure) map to both skills. Audit APIs and verification marketplaces are productization-adjacent public goods. Mandatory vendor disclosure is sales-adjacent — it forces the sales function to expose productization substance as metadata.
- The middle-market squeeze literature (Law.com, WEF 2026, RSM 2025) describes S3 as pressured on *both* skills: no S2 pivot speed, no S4 brand (sales shortfall); no in-house expertise, no dedicated teams (productization shortfall). Calling it "the squeeze" elides the fact that it is two squeezes coinciding.

---

## 8. Five new hypotheses the decomposition surfaces

### H1 — The PwC 20%-capture pattern is a "both skills" selection

*Hypothesis*: The PwC 2026 finding that 20% of companies capture 75% of AI economic gains selects for firms that are strong on *both* sales skill and productization skill. The other 80% have one or neither.

*Why it matters*: The PwC finding, the Bessemer Cloud 100 data, and the Crunchbase late-stage AI concentration all describe outcome distributions without naming the underlying selection variable. The decomposition proposes the variable: **joint strength on both skills is the PwC 20%**. This is testable with Crunchbase/PitchBook metadata (revenue + funding + team composition) plus eval-benchmark publications.

*Caveat*: The hypothesis does not claim the decomposition is the only selection variable; network effects, data moats, and timing also matter. But a firm with only sales skill becomes Klarna/Builder.ai; a firm with only productization skill becomes Humane (eng without GTM); both sales and productization are required for sustained capture.

### H2 — Governance theater is a structural skill asymmetry, not an organisational failure

*Hypothesis*: The governance-theater pattern identified in the scale-based comparative matrix (D8 failure mode profile at S4 typical) is a structural consequence of sales skill and productization skill being organisationally separable. Sales skill publishes governance artifacts; productization skill has not produced the substance the artifacts claim.

*Why it matters*: The original scale-based finding treated governance theater as a failure of discipline at the analyst's desk. The decomposition relocates the failure earlier: sales skill produces verification-as-instrument because it is sellable; productization skill produces verification-as-substance only when forced. Without a forcing function (regulator, ethics committee, contract), the asymmetry is the default equilibrium.

*Caveat*: Not all governance artifacts are theatre. Microsoft's Sensitive Uses committee, JPMorgan's MRG, Singapore's AI Verify all produce both artifacts and substance. The hypothesis is about the modal case, not the substantive exemplars.

### H3 — The S2 AI-native vs AI-using split is primarily a productization-skill split

*Hypothesis*: The two-population split at S2 that the scale-based track documents (AI-native vs AI-using; RVCS-1 13/15 vs 5/15) is not principally a sales-skill split. Both populations can be strong or weak on sales. The consistent difference is productization skill — AI-native firms have trained on the problem; AI-using firms have rented the model and built orchestration.

*Why it matters*: This clarifies where the intervention should target. For S2 AI-using firms, improving verification quality requires productization investment (evals, monitoring, per-decision verification). For S2 AI-native firms whose sales skill lags, the productization advantage is already present; the gap is in go-to-market.

*Caveat*: Hybrid cases exist. Perplexity has some in-house Sonar fine-tuning *and* uses frontier APIs — productization is neither purely native nor purely using. Harvey scores high on productization benchmarks despite being critiqued as a GPT wrapper. The split is a gradient, not a binary.

### H4 — The middle-market squeeze is two squeezes coinciding

*Hypothesis*: The RSM / Law.com / WEF middle-market squeeze is a sales-skill squeeze and a productization-skill squeeze that happen to coincide at S3. Sales pressure comes from rising customer AI expectations, competitor narrative, regulatory reporting. Productization pressure comes from in-house expertise scarcity, data quality, integration cost. The two pressures reinforce but do not require each other.

*Why it matters*: Interventions targeting the "squeeze" differ by which half is being addressed. Sales-side interventions (industry standardisation, shared brand credentials, insurance pools) differ from productization-side interventions (managed vendor stacks, consortium evals, shared MLOps services). The original squeeze framing collapsed these; the decomposition separates them.

*Caveat*: For S3 firms in high-regulation industries (banking, healthcare, legal), the squeezes may be tightly coupled — regulatory-driven sales pressure creates immediate productization demand.

### H5 — The S2→S5 single-contract transition is a sales event meeting a productization gap

*Hypothesis*: The scale-based track's most consequential scale-crossing dynamic (S2 startup lands a regulated-industry customer and inherits S5 liability) is specifically a sales event that exposes a pre-existing productization gap. Sales skill closed the contract; productization skill has not built the per-decision audit trail, cite-check, or clinical-review pipeline the contract implicitly assumed.

*Why it matters*: The "30-day S2→S5 crossing kit" the scale-based track proposed is specifically a productization kit — a minimum viable verification infrastructure a startup can deploy. The sales function does not need retooling (it already won the contract); the productization function does.

*Caveat*: Some S2→S5 transitions are driven by a sales function that oversold verification substance to close the contract. In those cases, the gap is both sales (claims) and productization (substance), and the crossing kit needs a sales-narrative revision alongside the technical build.

---

## 9. Implications for the three paper candidates

The scale-based research plan identifies three paper candidates. Each gains a cleaner framing from the decomposition.

### Paper Candidate 1 — "The Verification Tax Across Organizational Scales"

*Update*: Distinguish verification *claims* from verification *substance*. The verification tax is a productization-side tax, and its scaling properties are different from the scaling properties of the sales-side verification-claim cost. The paper can report verification substance (RVCS-1 scores, VTI) as productization output and verification claims (SOC 2 cost, ISO 42001 cost, insurance premium) as sales-side cost. They are related but not the same. This lets the paper make a stronger "the tax is not where you think it is" argument.

### Paper Candidate 2 — "The Legal Profession's Reasoning Verification Crisis"

*Update*: The Big Law vs Solo finding has a productization reading (Big Law's manufactured cite-check + partner pipeline *is* a productization substitute) and a sales reading (Solo attorneys lack brand protection and referral networks that would filter out AI-generated errors before client delivery). Both are present; the paper can make the argument stronger by naming them separately and then showing they reinforce.

### Paper Candidate 3 — "Solo Founders and the Verification Floor"

*Update*: The public-good argument has a sales-adjacent version (from AI liability literature, AI Frontiers 2025) and a productization-adjacent version (from the scale-based track). Both converge on the same structural conclusion — that S1 actors cannot privately produce verification of either kind. The paper can cite both literatures and show that the two-sided public-good claim is stronger than either alone.

---

## 10. Two new tables the decomposition lets the project produce

### 10.1 The sales-productization case log (candidate for S2 tier report update)

A registry of 2024-2026 AI failures coded by the four-quadrant matrix. Starter entries:

| Year | Firm | Tier | Sales skill | Productization skill | Outcome |
|---|---|---|---|---|---|
| 2025 | Klarna AI-first | S4 typical | H | L | Rollback, re-hire |
| 2025 | Humane AI Pin | S2 AI-native attempt | L (final) | M (acquihired) | HP buys assets $116M |
| 2025 | Builder.ai | S4 via acquisition | H | L | Bankruptcy |
| 2025 | Nate Inc. | S2 AI-using | H | L | SEC/DOJ fraud |
| 2025 | Presto Voice | S4 listed | M | L | SEC enforcement |
| 2025 | Deloitte AU | S4 substantive firm, typical case | H | L (per-output) | Refund, reputational |
| 2025 | Meta auto-review | S4 typical | H | L (per-decision) | Ongoing |
| 2025 | Character.AI | S2 AI-using | H | L (Q3) | Texas AG, litigation |
| 2025 | Cleo | S2 AI-using | H | L | FTC action |
| 2025 | Ellis George | S5 (mid-law) | M | L | $31,100 sanction |
| 2025 | Duolingo AI-first | S4 | H | M (decent product; bad messaging) | Narrative walkback |
| 2025 | Salesforce Agentforce seat reversal | S4 | H (adaptive) | M | Reprice to seat-based |

This registry, expanded, is the direct evidence base for Paper Candidate 1.

### 10.2 Compute-concentration × productization access (candidate for S2 tier report update)

The GPU shortage through Q3 2026 (HBM triopoly, TSMC CoWoS allocation, hyperscaler forward orders) changes productization resource economics. The compute distribution by firm size should be a table the project produces:

| Actor | Access to compute | Productization consequence |
|---|---|---|
| Frontier labs (Anthropic, OpenAI, xAI) | Direct training compute + reserved inference | Full productization surface |
| Hyperscaler AI units (Microsoft, Google, Meta, Amazon internal) | Forward-ordered Blackwell allocation | Full productization surface; distribution leverage |
| Scale-up AI-native (Cohere, Mistral, Cursor, Harvey) | Priority cloud allocation at premium pricing | Productization constrained by inference cost (55–80% of GPU spend) |
| S4 typical | Spot/general cloud allocation | Rate-limited; inference latency-bounded |
| S3 / S2 AI-using | Pay-per-token at vendor APIs | No training productization surface; orchestration only |
| S1 | Consumer-tier subscriptions | Productization is prompt engineering + orchestration |

The decomposition lets the compute story be told as a productization-skill constraint rather than a sales-skill constraint, which sharpens the argument about what S3, S2 AI-using, and S1 actors can and cannot do.

---

## 11. What this memo does not claim

- **Not all AI failures are sales-productization asymmetries.** Some are pure productization failures (a well-built system that hits an unexpected distributional shift). Some are pure sales failures (accurate products mis-messaged). The decomposition is a lens for reading a substantial subset of failures, not a universal theory.
- **The decomposition does not propose a new framework.** The scale-based track's 10-dimensional comparative matrix, verification capacity curve, and framework portability table remain the primary analytical artefacts. This memo is an interpretive layer, analogous to how `size-speed-resource-tradeoff.md` is an interpretive layer.
- **The upper-left quadrant is not a guarantee of good outcomes.** Firms with both strong sales and strong productization skill still face specification gaming, adversarial users, distributional shift, and novel failure modes. They are less likely to have the sales-ahead-of-product failure pattern, but they are still exposed to the others.
- **The lower-right quadrant is not uniformly doomed.** S1 solo actors in non-liable domains (personal productivity, indie SaaS) can operate below the threshold because the cost of unverified output is privately absorbed. The public-good argument applies strongest where the cost is externalised (regulated professions, consequential decisions, fiduciary roles).
- **The two-skill decomposition is not exhaustive.** Network effects, data moats, regulatory capture, timing, and luck also determine outcomes. The decomposition isolates the two skills most directly relevant to the verification-quality question because that is the scale-based track's core concern.

---

## 12. Sources

### 12.1 Enterprise AI sales and investment

- Menlo Ventures, [*2025 The State of Generative AI in the Enterprise*](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/)
- Crunchbase, [*Q1 2026 Record-Breaking Venture Funding*](https://news.crunchbase.com/venture/record-breaking-funding-ai-global-q1-2026/)
- CB Insights, [*State of Venture Q1'26*](https://www.cbinsights.com/research/report/venture-trends-q1-2026/)
- CB Insights, [*State of AI Q1'26*](https://www.cbinsights.com/research/report/ai-trends-q1-2026/)
- PwC, [*2026 AI Performance Study*](https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-performance-study.html)
- a16z, [*100 Enterprise CIOs*](https://a16z.com/ai-enterprise-2025/)
- a16z, [*Leaders, Gainers, and Unexpected Winners in the Enterprise AI Arms Race*](https://a16z.com/leaders-gainers-and-unexpected-winners-in-the-enterprise-ai-arms-race/)
- CIO Dive, [*Microsoft, Google Rule AI Market*](https://www.ciodive.com/news/microsoft-google-rule-ai-market-enterprises/808311/)
- Bessemer, [*State of AI 2025*](https://www.bvp.com/atlas/the-state-of-ai-2025)
- Bessemer, [*Cloud 100 Benchmarks 2025*](https://www.bvp.com/atlas/the-cloud-100-benchmarks-report/)

### 12.2 Pricing and GTM

- Metronome, [*2025 AI Pricing Field Report*](https://metronome.com/blog/ai-pricing-in-practice-2025-field-report-from-leading-saas-teams)
- BCG, [*Rethinking B2B Software Pricing in the Era of AI*](https://www.bcg.com/publications/2025/rethinking-b2b-software-pricing-in-the-era-of-ai)
- Register, [*Salesforce Seat-Based Pivot*](https://www.theregister.com/2025/12/12/ai_agents_salesforce_pricing/)
- Sacra, [*Harvey*](https://sacra.com/c/harvey/), [*Sierra*](https://sacra.com/c/sierra/), [*Decagon*](https://sacra.com/c/decagon/)
- Innovation Endeavors, [*Enterprise Sales Playbook*](https://www.innovationendeavors.com/insights/enterprise-sales-playbook)
- Spearhead, [*Cursor by Anysphere Fastest-Growing SaaS*](https://www.spearhead.so/blogs/cursor-by-anysphere-the-fastest-growing-saas-product-ever)

### 12.3 AI washing, SEC/FTC enforcement

- DLA Piper, [*SEC Emphasizes Focus on AI Washing*](https://www.dlapiper.com/en/insights/publications/ai-outlook/2025/sec-emphasizes-focus-on-ai-washing)
- Holland & Knight, [*SEC and DOJ Warm Up to Enforcement Over AI Washing*](https://www.hklaw.com/en/insights/publications/2025/07/sec-and-doj-warm-up-to-enforcement-over-ai-washing)
- Benesch, [*Operation AI Comply One Year In*](https://www.beneschlaw.com/insight/one-year-in-ftcs-operation-ai-comply-continues-under-new-administration-signaling-enduring-enforcement-focus/)
- Winston & Strawn, [*SEC Targets AI Washing*](https://www.winston.com/en/blogs-and-podcasts/capital-markets-and-securities-law-watch/sec-targets-ai-washing-by-companies-investment-advisers-and-broker-dealers)
- WilmerHale, [*FTC Rite Aid Action*](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20240111-ftc-announces-groundbreaking-action-against-rite-aid-for-unfair-use-of-ai)
- Fortune, [*MIT 95% Pilot Failure*](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/)

### 12.4 Productization engineering: MLOps, eval, verification infra

- Databricks, [*State of Data + AI*](https://www.databricks.com/resources/ebook/state-of-data-ai)
- Databricks, [*Hidden Technical Debt in GenAI Systems*](https://www.databricks.com/blog/hidden-technical-debt-genai-systems)
- Google Cloud, [*DORA State of DevOps 2025*](https://cloud.google.com/devops/state-of-devops)
- Stack Overflow, [*2025 Developer Survey*](https://survey.stackoverflow.co/2025/ai)
- Thoughtworks, [*Tech Radar vol. 33*](https://www.thoughtworks.com/about-us/news/2025/thoughtworks-tech-radar-33-rapid-ai)
- McKinsey, [*State of AI*](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)
- Stanford HAI, [*AI Index 2025*](https://hai.stanford.edu/ai-index/2025-ai-index-report)
- Sculley et al., [*Hidden Technical Debt in ML Systems*](https://papers.neurips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf), NeurIPS 2015
- RAND, [*Root Causes of AI Failure*](https://www.rand.org/pubs/research_reports/RRA2680-1.html)
- Anthropic, [*Frontier Red Team*](https://red.anthropic.com/), [*Bloom*](https://alignment.anthropic.com/2025/bloom-auto-evals/), [*Strengthening Red Teams*](https://alignment.anthropic.com/2025/strengthening-red-teams/)
- Microsoft, [*Responsible AI*](https://www.microsoft.com/en-us/ai/responsible-ai)
- Horvitz, [*AETHER Committee*](https://erichorvitz.com/Aether_Committee_Microsoft.htm)
- JPMorgan, [*AI and Model Risk Governance*](https://www.jpmorgan.com/technology/news/ai-and-model-risk-governance)
- AI Verify Foundation, [*What is AI Verify*](https://aiverifyfoundation.sg/what-is-ai-verify/)
- OpenAI, [*Evals*](https://evals.openai.com/)
- Meta, [*Llama 3.1 Announcement*](https://ai.meta.com/blog/meta-llama-3-1/)
- EleutherAI, [*lm-evaluation-harness*](https://github.com/EleutherAI/lm-evaluation-harness)
- LawNext, [*Legal AI Benchmark Study*](https://www.lawnext.com/2025/02/legal-ai-tools-show-promise-in-first-of-its-kind-benchmark-study-with-harvey-and-cocounsel-leading-the-pack.html)
- Vals AI, [*VLAIR 2.27.25*](https://www.vals.ai/industry-reports/vlair-2-27-25)

### 12.5 Failure cases

- TechCrunch, [*Humane AI Pin / HP $116M*](https://techcrunch.com/2025/02/18/humanes-ai-pin-is-dead-as-hp-buys-startups-assets-for-116m/)
- Axios, [*Humane AI Pin Shut Down*](https://www.axios.com/2025/02/18/humane-ai-pin-shut-down-hp)
- Fast Company, [*Klarna and Duolingo AI-first Backfire*](https://www.fastcompany.com/91332763/going-ai-first-appears-to-be-backfiring-on-klarna-and-duolingo)
- Fortune, [*Duolingo CEO Walks Back AI-first*](https://fortune.com/2025/05/24/duolingo-ai-first-employees-ceo-luis-von-ahn/)
- Mind the Product, [*Klarna Recruitment Drive After AI-first*](https://www.mindtheproduct.com/klarna-goes-on-recruitment-drive-after-ditching-ai-first-policy/)
- Digital Applied, [*AI Product Failures 2026 Lessons*](https://www.digitalapplied.com/blog/ai-product-failures-2026-sora-humane-rabbit-lessons)
- MIT, [*State of AI in Business 2025*](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/) (coverage)

### 12.6 Middle-market and solo founders

- RSM US, [*Middle Market AI Survey 2025*](https://rsmus.com/insights/services/digital-transformation/rsm-middle-market-ai-survey-2025.html)
- KeyBank, [*AI Trends in 2025*](https://www.key.com/businesses-institutions/business-expertise/articles/ai-trends-in-2025.html)
- Law.com, [*The AI Squeeze on Midsize Firms*](https://www.law.com/pro-mid-market/2026/04/02/the-ai-squeeze-time-and-cost-pressures-on-midsize-firms/)
- WEF, [*AI Mid-Market Business Moment*](https://www.weforum.org/stories/2026/01/ai-mid-market-business-growth/)
- Contrary Research, [*Cursor*](https://research.contrary.com/company/cursor)
- TechCrunch, [*Cursor $10B Valuation*](https://techcrunch.com/2025/03/07/cursor-in-talks-to-raise-at-a-10b-valuation-as-ai-coding-sector-booms/)
- Quartz, [*Unicorn Entrepreneur Solo AI*](https://qz.com/unicorn-entrepreneur-founder-solo-ai-startup-automation-workforce)
- WeAreFounders, [*30 Solo Startups $10M/Employee*](https://www.wearefounders.uk/the-30-highest-valued-solo-startups-of-2026/)

### 12.7 Compute and infrastructure

- Spheron, [*GPU Shortage 2026*](https://www.spheron.network/blog/gpu-shortage-2026/)
- Clarifai, [*GPU Shortages 2026*](https://www.clarifai.com/blog/gpu-shortages-2026)
- GMI Cloud, [*GPU Cloud Costs for AI Startups*](https://www.gmicloud.ai/blog/how-much-do-gpu-cloud-platforms-cost-for-ai-startups-in-2025)

### 12.8 Classical strategy and academic

- Hyytinen et al., [*Unpacking liabilities of newness and smallness in innovative start-ups*](https://www.sciencedirect.com/science/article/abs/pii/S004873332030127X), *Research Policy* 2020
- Christensen Institute, [*What does Disruptive Innovation say about AI?*](https://www.christenseninstitute.org/blog/what-does-disruptive-innovation-say-about-ai/)
- AI Frontiers, [*The Case for AI Liability*](https://ai-frontiers.org/articles/case-for-ai-liability)
- Galileo, [*LangSmith Alternatives*](https://galileo.ai/blog/best-langsmith-alternatives)
- arXiv, [*BenchRisk*](https://arxiv.org/pdf/2510.21460), [*ReliabilityBench*](https://arxiv.org/html/2601.06112)

---

## 13. Repository cross-references

- [`size-speed-resource-tradeoff.md`](size-speed-resource-tradeoff.md) — the parent memo this decomposes. The three axes in that memo decompose across the two skills introduced here.
- [`cross-tier-synthesis.md`](cross-tier-synthesis.md) — the three load-bearing findings this memo reinterprets in §7.
- [`comparative-matrix.md`](comparative-matrix.md) — the D8 failure mode profile column is what the sales-productization case log in §10.1 extends.
- [`verification-capacity-curve.md`](verification-capacity-curve.md) — the quantitative backbone for the claim that productization infrastructure predicts RVCS-1 score.
- [`framework-portability.md`](framework-portability.md) — the 5×7 discipline portability matrix. Q3 at S2 AI-using is the incentive problem that the decomposition re-expresses as "sales skill outpaces productization Q3 discipline."
- [`s2-small-enterprises-startups.md`](s2-small-enterprises-startups.md) — the two-population split that H3 in §8 reinterprets as a productization-skill split.
- [`s4-large-corporations.md`](s4-large-corporations.md) — the governance-theater hypothesis that H2 in §8 reinterprets as a structural skill asymmetry.
- [`s5-regulated-professions.md`](s5-regulated-professions.md) — the Big Law vs Solo finding whose productization/sales reading Paper Candidate 2 in §9 updates.
- [`s1-solo-entrepreneurs.md`](s1-solo-entrepreneurs.md) — the public-good argument whose two-sided structure §7.3 and Paper Candidate 3 in §9 develop.
- [`../../adaptive-governance/speed-gap-analysis.md`](../../adaptive-governance/speed-gap-analysis.md) — the research-practice temporal gap the sales-cycle-speed findings in §3.1 refine.
- [`incident-decomposition-recoding.md`](incident-decomposition-recoding.md) — Stream B appendix recoding the 20-incident structured inventory against the decomposition (2026-04-21). Discussed in §14.
- [`asia-market-decomposition-appendix.md`](asia-market-decomposition-appendix.md) — Stream A appendix populating the matrix with Korean / Japanese / Chinese / Singaporean cases (2026-04-21). Discussed in §14.
- [`eval-engineering-profession-appendix.md`](eval-engineering-profession-appendix.md) — Stream C appendix documenting eval engineering as an emerging productization sub-skill (2026-04-21). Discussed in §14.
- [`regulatory-regime-skill-asymmetry-appendix.md`](regulatory-regime-skill-asymmetry-appendix.md) — Stream D appendix comparing 11 regulatory regimes by sales-instrument vs productization-substance asymmetry (2026-04-21). Discussed in §14.
- [`vertical-ai-depth-appendix.md`](vertical-ai-depth-appendix.md) — Stream E appendix on 21 vertical-AI firms coded by sales motion, productization depth, and eval publication (2026-04-21). Discussed in §14.
- [`../../operations/expansion/sales-vs-productization-research-plan.md`](../../operations/expansion/sales-vs-productization-research-plan.md) — the Wave 4 research plan this memo's §14 integrates.

---

## 14. Wave 4 cross-stream expansion (2026-04-21)

This section integrates six parallel research streams commissioned under [`sales-vs-productization-research-plan.md`](../../operations/expansion/sales-vs-productization-research-plan.md). Each stream closed a specific gap identified in the research plan. The appendices live as sibling files; this section summarises the findings that bear on the memo's hypotheses.

### 14.1 Six streams and where they land

| Stream | Gap closed | Deliverable | Primary finding |
|---|---|---|---|
| **A** | Asia-region evidence | [`asia-market-decomposition-appendix.md`](asia-market-decomposition-appendix.md) | Decomposition holds in Asia with three structural modifications (regional routes into upper-left, different upper-right failure modes, sharper regulatory asymmetry). |
| **B** | 71-incident recoding | [`incident-decomposition-recoding.md`](incident-decomposition-recoding.md) | 50% of the 20 structured incidents sit in the sales-ahead-of-product quadrant; modal documented failure is exactly the upper-right cell. |
| **C** | Eval engineering profession | [`eval-engineering-profession-appendix.md`](eval-engineering-profession-appendix.md) | Eval engineering is crystallising as a named profession (dedicated titles, $100M+ tooling market, named curriculum) — productization skill is empirically decomposable into nameable sub-skills. |
| **D** | Regulatory regime × skill | [`regulatory-regime-skill-asymmetry-appendix.md`](regulatory-regime-skill-asymmetry-appendix.md) | Seven regimes coded; Japan + Korea + US SEC/FTC are sales-instrument regimes; EU AI Act high-risk + FDA + SR 11-7 are productization-forcing; Singapore is the unique productization-substance-as-public-good regime. |
| **E** | Vertical AI depth | [`vertical-ai-depth-appendix.md`](vertical-ai-depth-appendix.md) | 21 vertical-AI firms coded; firms that train or fine-tune concentrate in upper-left and price at 10× SaaS revenue/FTE; prompt-only wrappers cluster upper-right or fail. |
| **F** | Quadrant distribution | §14.2 below | Central estimate: upper-left 5–8%, upper-right 8–15%, lower-left 5–15%, lower-right 55–75% of the ~10,000 venture-funded AI startup universe. |

### 14.2 Stream F — Quantitative quadrant distribution

Applying publicly available aggregates from Menlo Ventures, Bessemer, Carta, PitchBook, PwC, MIT, and RSM to the ~10,000 venture-funded AI startup universe, the best-estimate distribution is:

| | **Productization: HIGH** | **Productization: LOW** | **Row total** |
|---|---|---|---|
| **Sales: HIGH** | **5–8%** "Balanced frontier" (Anthropic, OpenAI, Harvey, Sierra, Decagon, Cursor, Glean, Abridge, Cresta, Perplexity, Scale AI, Cohere, Mistral, xAI; Cloud-100 AI cohort) | **8–15%** "Sales ahead of product" (Klarna, Humane, Builder.ai, Nate Inc., Presto Voice, Character.AI, Cleo, Rabbit R1, AI-washing enforcement population, sales-led wrappers) | **13–23%** sales-strong |
| **Sales: LOW** | **5–15%** "Engineering without go-to-market" (pre-commercial labs, eval-tooling startups pre-revenue, government AI testing facilities, acquihire-destined engineering orgs) | **55–75%** "Structurally weak" (pre-revenue wrappers, failed pilots, non-graduating seed, sub-$1M ARR, mid-market with 70% outside-help dependence, thin wrappers) | **60–90%** sales-weak |
| **Column total** | **10–23%** productization-strong | **63–90%** productization-weak | — |

Central point estimates (midpoints): upper-left 6.5%, upper-right 11.5%, lower-left 10%, lower-right 65%. **The modal firm is lower-right by a factor of 4–6× any other cell.** Confidence: **C/D-graded** — no public dataset directly cross-tabulates these axes at scale; every cell combines observed aggregates with inferred overlap.

**Economic-value-captured distribution is the reverse**: the upper-left 5–8% of firms capture the majority of AI economic gains per PwC 2026, and the top three frontier labs (Anthropic 40%, OpenAI 27%, Google 21% of enterprise LLM spend per Menlo) account for 88% of enterprise LLM revenue. The distribution is a power law — single-peak at lower-right by firm count, single-peak at upper-left by value captured — not the bimodal "missing middle" structure the memo initially implied in §8.

### 14.3 Hypothesis scorecard

| Hypothesis | Verdict | Primary supporting evidence |
|---|---|---|
| **H1** PwC 20%-capture pattern is a "both skills" selection | **Supported in a softer form** | PwC top-performer multipliers (1.7× Responsible AI framework, 1.5× cross-functional governance, 1.8–1.9× advanced/autonomous deployment, 2.8× human-out-of-loop decisions) are productization-infrastructure correlates. But the 20% is an enterprise *adopter* figure, not a vendor figure; it overlaps with but is not identical to the ~5–8% upper-left vendor cell. Restate as: "the top 20% is disproportionately upper-left, with a minority upper-right fraction still revenue-productive while productization lags." [Streams F, E] |
| **H2** Governance theater is a structural skill asymmetry, not an organisational failure | **Strongly supported** | Stream B's 50% sales-ahead-of-product rate in the structured incident sample is the upper-right cell empirically. Stream D's finding that US SEC/FTC target claim-substance gaps (every AI-washing case is a disclosure case, not a defect case) names the enforcement equilibrium. Stream F's 1.7× Responsible AI framework gap between top-20% and non-top quantifies the structural wedge. [Streams B, D, F] |
| **H3** The S2 AI-native vs AI-using split is primarily a productization-skill split | **Strongly supported** | Stream E's 21-firm coding: 8 training / fine-tuning firms price at the top of their verticals and concentrate in upper-left; 4 RAG-only-or-weaker firms cluster upper-right or acquired. Stream C's confirmation that eval engineering (a productization sub-skill) is the profession-visible marker of AI-native firms. [Streams E, C] |
| **H4** The middle-market squeeze is two squeezes coinciding | **Partially supported, refined** | Stream F's mid-market data (RSM 91% use GenAI; 62% harder than expected; 70% need outside help) confirms the two-sided pressure. Stream D adds a regulatory dimension — Korean and Japanese mid-market firms face sales-instrument compliance (AI Basic Act, METI guidelines) without proportionate productization mandate, compressing both skills simultaneously via different levers. [Streams D, F] |
| **H5** S2→S5 single-contract transition is a sales event meeting a productization gap | **Not directly tested; evidence aligned** | No stream directly measured the S2→S5 crossing event. Stream B's 5/5 "both weak" cases clustering at S5 Solo / S1 tiers and Stream E's vertical-AI firms scaling only when they invest in productization both indirectly support the hypothesis. A Wave 5 primary-data study would be required for direct test. [Streams B, E] |

### 14.4 Three findings that do not fit the decomposition cleanly

The streams also surface data that the two-skill decomposition does not cleanly accommodate. Naming them honestly is necessary.

1. **SoftBank's $64.6B into OpenAI is productization-by-acquisition.** The decomposition treats a firm's productization skill as internal capability. SoftBank reaches upper-left status by owning 40% of Stargate and a large OpenAI equity stake, not by building productization. This is a route the memo did not anticipate and suggests productization skill can be instantiated at the corporate-group level rather than the operating-company level. [Stream A]

2. **Apple is further along on title differentiation than frontier labs.** Stream C found five distinct Siri-side evaluation engineering titles at Apple versus one each at Anthropic and OpenAI. The memo's §2.2 implicitly assumed frontier labs crystallise productization sub-skills first; the evidence is that product-layer incumbents with regulated-industry exposure (Apple's consumer AI + GDPR/consumer-protection exposure) force earlier title differentiation than research-heavy labs. [Stream C]

3. **Singapore AI Verify is productization substance built as a public good.** Stream D identified the Singapore regime as uniquely building the testing infrastructure itself rather than requiring private firms to produce it. This is the first working form of the S1 tier report's three infrastructure proposals and demonstrates that productization substance can be produced at state scale, not only firm scale. The decomposition's Finding 3 reinterpretation in §7.3 is consistent with this, but the §4 matrix cells are firm-level and do not encode the state-as-producer case. [Stream D]

### 14.5 Refinements the memo now incorporates

Three refinements are added to the pre-Wave-4 memo body:

- **§2.2 productization is a vector, not a scalar.** Stream B's "both strong" incidents (Meta housing ads, RealPage, Google Gemini) show firms that are strong on most productization sub-dimensions and still fail via a single weak sub-component (fairness audit at Meta; normative specification at RealPage; safety alignment at Gemini). The nine sub-dimensions listed in §2.2 should be read as a vector, not a single skill level.
- **§4 matrix scope boundary.** Stream B's "not matrix-applicable" cases (Amazon internal recruiting, Samsung ChatGPT ban) identify a boundary: the decomposition applies to firms producing AI products or AI-driven services, not to internal-only AI tooling, employee use of third-party AI, or information-governance incidents. This is added to §11.
- **§8 H1 softer form.** Stream F's analysis requires H1 to be restated as "the top 20% is disproportionately upper-left, with a minority upper-right fraction" rather than a clean 20%=both-skills identity. The PwC 1.7×–2.8× multipliers are the specific quantitative hook.

### 14.6 What Wave 4 does not resolve

- **Longitudinal movement across quadrants** (Gap 8 in the research plan) remains unaddressed. The expansion is still a snapshot.
- **Insurance and liability market pricing** (Gap 9) is touched at in Stream C (Armilla AI, Munich Re aiSure, Verisk January 2026 exclusion) but not systematically analysed.
- **Solo-founder productization ceiling** (Gap 10) remains unbounded. Base44, Cursor, Bolt, Midjourney, Gumloop are existence proofs; where productization through AI coding tools stops being enough is not answered.
- **Primary interviews or surveys** are out of scope for Wave 4. The scale-based track's own Wave 4 primary-fieldwork list (S1 diary study, FICS-1 expansion, S3 survey, S7 institutional access) would be the natural extension.

### 14.7 Evidence grade mix across streams

| Stream | Dominant evidence grade | Notes |
|---|---|---|
| A (Asia) | B majority, A for government filings (Korea AI Basic Act, Japan METI, China CAC, Singapore AI Verify) | Some C for cross-regional population estimates |
| B (incident recoding) | A/B — inherited from alignment-failure-mapping inventory | C for skill-balance coding where firm-at-time-of-incident data is thin |
| C (eval engineering) | B — job postings and funding are primary but transient | C for salary comparability estimates |
| D (regulatory) | A majority — regulatory texts are primary | B for enforcement volume claims |
| E (vertical AI) | B — private-company ARR and funding data are practitioner-level | C for strategic moat claims |
| F (quadrant distribution) | C/D — indirect inference from aggregated public data | No primary dataset cross-tabulates these axes |

The Wave 4 expansion does not contain A-graded claims that contradict the pre-Wave-4 memo; it produces B- and C-graded refinements that strengthen or soften the existing hypotheses within the grade limits the scale-based track's evidence rubric allows.
