# M1 — Systems-Dynamics Map of the Three-Pillar Adaptability Problem

axis: M (Meta — Cross-Pillar Integration)
date: 2026-04-22
plan: research/operations/expansion/adaptability-framework-research-plan.md

---

## 1. Method

This memo is primarily a conceptual synthesis rather than an empirical study. It applies MIT SDM and system-dynamics modelling conventions (Sterman 2000; Forrester 1961) to the author's three-pillar decomposition — AI usage × organizational structure × technical infrastructure — and reads the coupling through Teece's dynamic capabilities (Teece 1997, 2007), O'Reilly and Tushman's ambidextrous organization (O'Reilly and Tushman 2004), Hollnagel's resilience engineering (Hollnagel 2014), Beer's Viable System Model (Beer 1972, 1979), Christensen's disruption theory (Christensen 1997), and Meadows's leverage-point hierarchy (Meadows 1999). The stocks, flows, loops, and delays proposed below are modelling choices; their calibration is deferred to memos A1–T3 and M2 in the same research track. Evidence is labelled as *observed* when drawn from the sibling extension tracks already written (scale-based, healthcare-bio-ai, sales-vs-productization), and as *inferred* or *speculative* when the claim is model-generated rather than evidentially grounded. Confidence labels (high / medium / low) are attached to claims whose strength differs.

---

## 2. System boundary and actors

**Inside the model**
- The three pillars as coupled subsystems: Pillar 1 (AI Usage — prompts, model choices, evaluation, workflow embedding); Pillar 2 (Organization — roles, teams, governance, learning practices); Pillar 3 (Technical Infrastructure — serving stack, data plane, observability, compute procurement).
- Six stocks: capability debt, trust debt, talent stock, tooling stock, data assets, organizational slack.
- The firm's environment insofar as it supplies inputs or absorbs outputs (capability releases from frontier labs; hiring market; regulatory signals; customer demand; incident disclosure channels).
- Cross-pillar feedback through named reinforcing and balancing loops.

**Outside the model (exogenous)**
- Frontier model release cadence — treated as an exogenous driver with roughly monthly-to-quarterly tick rate (observed 2022–2026). A full model would endogenize this via firm-to-lab feedback; for the M1 scope it is held exogenous.
- Macro factors — interest rates, venture capital availability, geopolitical compute restrictions — entered only as shock inputs to specific flows.
- Individual cognition and affect — Kahneman / Simon / March-style bounded rationality is present but compressed into aggregate behavioural parameters rather than modelled at the person level.

**Unit of analysis**
- Default: a single knowledge-work organization of 50–50,000 FTE operating on 2022–2026 AI technology. The S7-international-institution and S1-solo tiers of the scale-based track are treated as boundary cases, noted where the model breaks.

---

## 3. Stocks and flows

System dynamics distinguishes stocks (accumulations, state variables) from flows (rates that change stocks). The six stocks below are the load-bearing state of the adaptability system. Each stock has at least one inflow and one outflow; several are coupled through shared flows.

### 3.1 Capability debt (CD)

*Definition*: the gap between the frontier AI capability that the market has made available and the capability that the firm actually runs in production. Measured (aspirationally) as a weighted lag in days, or as foregone value per month. Related to M2's *capability-to-deployment lag* indicator.

- **Inflow — capability release rate**: frontier labs ship; CD increases by the delta unless matched by firm adoption.
- **Outflow — integration rate**: the firm ingests a new capability into production. Rate is rate-limited by evaluation capacity, infrastructure elasticity, and workflow redesign throughput.
- **Outflow — obsolescence rate**: yesterday's capability becomes irrelevant (for example, function-calling displaces bespoke parsers); CD decreases not because the firm caught up but because the capability ceased to matter.

### 3.2 Trust debt (TD)

*Definition*: the gap between deployed capability and validated capability — the portion of production AI behaviour that has not been verified against user-facing or regulator-facing requirements. The analogue of the "verification debt" stock from the sales-vs-productization memo.

- **Inflow — deployment without validation**: each unverified deploy increases TD.
- **Inflow — evaluator drift**: already-validated behaviour re-enters TD when the evaluation apparatus (LLM-as-judge, golden sets, probes) itself drifts against true quality. Related to T3's evaluator-drift finding.
- **Outflow — verification throughput**: evaluation engineering capacity applied to close the gap.
- **Outflow — incident realization**: a trust failure surfaces (customer complaint, regulator letter, public incident), converting TD from a latent stock into a concrete loss and forcing re-validation.

### 3.3 Talent stock (TS)

*Definition*: headcount weighted by AI-relevant skill vintage. A 2024-trained ML engineer and a 2026-trained evaluation engineer are not fungible in this model; each vintage is tracked.

- **Inflow — hiring rate**: new joins, weighted by vintage and fit.
- **Inflow — internal reskilling**: existing FTE reclassified into higher-vintage skill bucket after training.
- **Outflow — attrition**: voluntary exits, weighted by vintage; senior ML talent attrits faster under wage inflation.
- **Outflow — skill staleness**: existing FTE whose skill vintage is overtaken by capability shift (2023-era prompt-engineering craft largely subsumed by tool-calling and o1-class reasoning by 2025–2026).

### 3.4 Tooling stock (TL)

*Definition*: the accumulated inventory of prompts, playbooks, evaluators, RAG pipelines, fine-tunes, adapters, and internal tools the firm operates. Connected to T3's taxonomy of AI-system technical debt.

- **Inflow — build rate**: new tooling produced by engineers and AI ops staff.
- **Inflow — acquisition / vendor integration**: imported tooling (Arize, LangSmith, Braintrust, internal vendor).
- **Outflow — deprecation**: deliberate removal of obsolete tooling.
- **Outflow — attrition / rot**: tooling that still exists but no longer works because a dependency moved (model deprecation, API breakage, embedding-space drift). A stock that looks healthy on inventory but is silently decaying.

### 3.5 Data assets (DA)

*Definition*: proprietary or semi-proprietary data holdings usable as evaluation sets, fine-tune corpora, RAG corpora, or revealed-preference signal. Distinct from tooling because data has different persistence properties.

- **Inflow — data accrual**: user interactions, domain operations, labelled sets, partner integrations.
- **Inflow — synthetic generation**: model-generated data (with provenance caveats).
- **Outflow — regulatory decay**: data that becomes unusable under changed consent or licensing terms (GDPR, EU AI Act, sector rules).
- **Outflow — schema obsolescence**: data that no longer fits the question being asked because the product shifted or the model's input surface changed.

### 3.6 Organizational slack (OS)

*Definition*: uncommitted capacity — engineering-weeks, decision-maker attention, compute reserve, budget reserve — available to respond to a capability shock without cancelling prior commitments. The analogue of Cyert-March organizational slack, applied to the three-pillar system. Related to Hollnagel's (2014) resilience-engineering capacity to *respond*.

- **Inflow — deliberate slack creation**: budgeting for unplanned work; spare capacity reservation; multi-provider routing surplus.
- **Inflow — emergent slack**: unused capacity that arises from over-provisioning (compute headroom).
- **Outflow — commitment**: new products, contracts, roadmap items consuming slack.
- **Outflow — crisis consumption**: incident response, unplanned migration, emergency hiring consumes slack at elevated rates.

---

## 4. Causal loop diagram

Loops are named as reinforcing (R) or balancing (B) following Sterman (2000) notation. Signs in text-based diagrams use `+` (same direction) and `−` (opposite direction). All loops are labelled; each has a short narrative. The diagram below is split into several panels for readability, but the six stocks and the flows in §3 are shared across panels.

### 4.1 Loop panel A — adoption pressure and capability debt

```
Frontier capability                                      +
release rate  ───────►  Capability debt (CD)  ─────────►  Competitive pressure
                          ▲                                              │
                          │                                              │
                          │  (−)                                         │ (+)
                          │                                              ▼
               Integration rate ◄────────── Evaluation throughput ◄──── Deployment
                          ▲                         ▲                    │ urgency
                          │ (+)                     │ (+)                 │
                          │                         │ (+)                 │
                          └─── Infrastructure ◄── Organizational
                               elasticity         attention
```

- **R1 — Capability treadmill (reinforcing)**: frontier release → CD rises → competitive pressure rises → deployment urgency rises → more deploys attempted → CD partially closed → perceived velocity rises → more aggressive commitments → CD rises again at the next release. Drives the classic "running on a moving walkway" feeling reported in O1 and O2 evidence.
- **B1 — Evaluation-bounded integration (balancing)**: CD rises → integration rate is requested faster → evaluation throughput becomes the bottleneck → integration rate saturates at evaluation capacity → CD closure slows to a deliberate pace. When B1 dominates, the firm is adaptable but slow; when it is weak or bypassed, R1 drives trust debt (loop panel B).

### 4.2 Loop panel B — trust debt and the erosion-of-goals archetype

```
Deployment urgency ───────────►  Deploy without full validation
       │                                           │
       │ (+)                                       │ (+)
       │                                           ▼
       │                              Trust debt (TD)
       │                                    │         │
       │                                    │ (+)     │ (+, delayed)
       │                                    ▼         ▼
       │                           Evaluator drift   Incident realization
       │                                    │              │
       │                                    │ (+)          │ (−)
       │                                    ▼              ▼
       │                            More TD accrual   Verification
       │                                               throughput ↑ (crisis)
       │                                                   │
       │                                                   │ (−)
       ▼                                                   ▼
Evaluation budget ◄─────── Time pressure ◄─────────── TD reduction
  (−)                         (+)
```

- **R2 — Erosion-of-goals on verification (reinforcing)**: when commitment rate exceeds productization throughput, time pressure cuts evaluation budgets, verification throughput drops, TD accrues, evaluator drift compounds TD further. Named and recognizable from Senge's and Sterman's erosion-of-goals archetype (the sales-vs-productization memo catalogues two dozen instances in AI firms 2023–2026). Confidence: high that this loop exists empirically; medium on calibration across firm sizes.
- **B2 — Incident-forces-correction (balancing, delayed)**: TD rises → after a lag, incidents realize → verification throughput jumps (crisis response) → TD reduces → prior urgency remains, the loop re-opens. The delay (§5) is the crux: the balancing force is present but arrives after harm.
- **B3 — Regulatory or insurance pricing (balancing, regime-dependent)**: TD in a productization-forcing regulatory regime (EU AI Act high-risk, FDA-regulated, SR 11-7, Singapore AI Verify) is capped ex ante by mandatory verification; analogous pricing pressure from AI liability insurance (Armilla, Munich Re aiSure, Verisk) is emerging as a market-based B3. Treated as two sub-loops B3a (regulatory) and B3b (insurance). Confidence: high on existence; low on strength outside high-risk sectors in 2026.

### 4.3 Loop panel C — talent, tooling, and the ambidextrous tension

```
Hiring rate ──►  Talent stock (TS)  ──►  Tooling build rate ──►  Tooling stock (TL)
   ▲                 │                                                   │
   │ (+)             │ (−)                                               │ (+)
   │                 ▼                                                   ▼
Hiring budget ◄── Attrition ◄── Wage pressure                    Capability debt
   │                                                                 closure
   │ (+)
   │
Operating margin ◄── Revenue from deployed AI ◄─────────────────── Integration rate
                                    ▲                                   ▲
                                    │ (+)                               │ (+)
                                    │                                   │
                                    └────── Tooling stock (TL) ─────────┘
```

- **R3 — Adoption pays for adoption (reinforcing)**: successful integration → revenue from AI features → operating margin → hiring budget → TS rises → more tooling build → faster integration. Strongest in the upper-left quadrant of the sales-vs-productization matrix — firms with real productization substance harvest this loop; wrapper firms do not.
- **B4 — Wage-inflation drain on talent (balancing)**: TS rises → market signals the firm can hire → wage pressure on senior talent from competitors rises → attrition rises → TS decays. Observed as the 2023–2024 wage spiral in frontier-lab compensation. Firms countered by re-weighting the hiring pipeline toward junior + reskilling rather than senior acquisition.
- **R4 — Ambidextrous exploitation crowds out exploration (reinforcing, pathological)**: TL rises along exploitative lines → short-term revenue rises → hiring favours exploitation → exploration tooling underfunded → the firm's ability to *sense* new capability weakens (Teece 2007). Directly the problem O'Reilly and Tushman (2004) identified: without structural separation, exploitation crowds out exploration. A structurally-ambidextrous firm inserts a B5 to counter R4.
- **B5 — Ambidextrous separation (balancing, design-imposed)**: a dedicated exploration unit with protected budget, senior-level integration (O'Reilly and Tushman's architectural prescription), and cross-unit transfer mechanism. B5 is not automatic; it is deliberately engineered. Firms that fail to install B5 observe R4 dominating.

### 4.4 Loop panel D — data assets, organizational slack, and capability-debt compounding

```
Data accrual rate ──► Data assets (DA) ──► Evaluation set coverage ──► Verification throughput
       ▲                    │                                                   │
       │ (+)                │ (−)                                               │ (+)
       │                    ▼                                                   ▼
Deployment footprint ◄── Regulatory / ◄── Trust debt (TD)                   Trust debt ↓
       ▲                schema decay                                            │
       │ (+)                                                                    │ (−)
       │                                                                        ▼
       └─────────────────────── Organizational slack (OS) ◄────────── Incident realization
                                         ▲                                (consumes slack)
                                         │ (−)
                                         │
                          Commitment-rate overshoot (R1, R2)
```

- **R5 — Data flywheel (reinforcing, conditional)**: deployment footprint → data accrual → DA rises → evaluation coverage rises → verification throughput rises → TD falls → confidence to deploy more rises. Operates cleanly only in permissive data-governance regimes; in regulated domains it is heavily damped (see healthcare-bio-ai track).
- **B6 — Slack is the resilience buffer (balancing)**: crisis consumption of OS maintains the system short-term but starves future resilience unless refilled. When OS falls below a threshold, the firm cannot absorb the next capability shock without cutting commitments, and B2-style crisis correction becomes the only option. Directly Hollnagel's (2014) *capacity to respond*: slack is the material form of that capacity.

### 4.5 Named-loop summary

| Loop | Type | Semantics | Dominant pillar | Canonical archetype |
|---|---|---|---|---|
| R1 | Reinforcing | Capability treadmill | Pillar 1 → all | Sterman "Limits to growth" inverse |
| R2 | Reinforcing | Verification debt under pressure | Pillar 1 × Pillar 2 | Senge "Eroding goals" |
| R3 | Reinforcing | Adoption pays for adoption | Cross-pillar | Senge "Success to the successful" |
| R4 | Reinforcing | Exploitation crowds out exploration | Pillar 2 | March 1991 trap |
| R5 | Reinforcing | Data flywheel | Pillar 3 × Pillar 1 | Platform flywheel |
| B1 | Balancing | Evaluation-bounded integration | Pillar 1 × Pillar 3 | Capacity bottleneck |
| B2 | Balancing | Incident-forces-correction (delayed) | Cross-pillar | Delayed feedback |
| B3 | Balancing | Regulatory / insurance gate | Pillar 2 × environment | External forcing |
| B4 | Balancing | Wage inflation drains talent | Pillar 2 | Market feedback |
| B5 | Balancing | Ambidextrous separation (designed) | Pillar 2 | Structural ambidexterity |
| B6 | Balancing | Slack reserves resilience | Cross-pillar | Hollnagel "respond" |

---

## 5. Delays and pathologies

Delays are structural, not incidental. Sterman (2000) establishes that long and variable delays in feedback loops are a primary cause of oscillation, overshoot, and policy resistance. The AI-era adaptability system is unusually delay-rich, and each delay produces a recognisable pathology.

### 5.1 Delay inventory

| Delay | Typical magnitude (2022–2026 evidence) | Which loop it sits in |
|---|---|---|
| Hiring lag — search to productive contribution | 3–9 months; senior ML closer to 12 | R3, R4, B4 |
| Tooling lag — capability release to stable production tooling | 2–8 months (A2 evidence) | R1, B1 |
| Learning lag — individual FTE internalizes new capability | 4–12 weeks of effective use | R3, R4 |
| Evaluation lag — eval harness ready for a new capability | 1–6 months; longer in regulated domains | B1, B2 |
| Regulatory lag — regulator recognizes and acts on a new failure class | 12–36 months (EU AI Act 2019→2024 enactment; FDA SaMD updates; SEC AI-washing 2024) | B3a |
| Incident realization lag — TD accrues to realized incident | 1–8 quarters | B2 |
| Infrastructure lag — new serving architecture designed and stable | 3–18 months | R3, B1 |
| Reorganization lag — formal role redefinition to productive new structure | 6–18 months | B5, R4 |
| Insurance-pricing lag — aggregate incident data to priced AI liability | 2–5 years (still maturing) | B3b |

### 5.2 Named pathologies

1. **Infrastructure built for last year's model**. The infrastructure lag (3–18 months) exceeds the frontier release cadence (≈ quarterly). By the time a custom serving stack is stable, the model generation it was tuned for has been partially displaced. The firm faces a rewrite-vs-ride-out decision annually. Pathological form: sunk-cost resistance freezes the stack on an obsolete capability curve, and R1 opens a growing capability debt. *Observed* pattern in T1 and T3 evidence 2024–2026.

2. **Team structure outliving the capability shift that created it**. The reorganization lag (6–18 months) plus political costs of undoing a previous reorg mean teams created for the 2023 prompt-engineering wave or the 2024 agent wave persist into 2026 even when the underlying capability has migrated into model default behaviour. Pathological form: R4 dominates because the exploitation org has codified the capability it was chartered to handle, while exploration remains under-resourced. The O2 memo is the empirical instrument.

3. **Evaluation debt accumulation**. Evaluation lag plus evaluator-drift lag jointly exceed the deployment cadence under R2. TD accrues silently until B2 forces correction. The Wave 4 sales-vs-productization memo documents this across two dozen cases. Pathological form: governance-theatre — an eval team exists but does not gate deployment. Structural fix is to shorten B2 (faster incident disclosure) or install B3 (regulatory or insurance gate).

4. **Talent vintage stratification**. Hiring lag plus skill-staleness outflow from TS produce cohort strata: 2022-era pre-ChatGPT engineers, 2023-era prompt-engineers, 2024–25 agent-engineers, 2026 evaluation-engineers. Each stratum was premium-priced at hire and may be penalised-priced by the time the next stratum arrives. Pathological form: Messages-to-hire-the-last-wave-of-talent being sent a quarter after the wave has broken. Observed in Kaggle and freelance market signals (scale-based track feeder).

5. **Slack erosion under continuous pressure**. B6 degrades silently when R1 + R2 both drive high commitment rates. The firm remains outwardly productive until a capability shock or incident arrives, at which point there is no buffer. Hollnagel's (2014) resilience-engineering warning — a system optimised for Safety-I (avoiding known failures) can have zero Safety-II capacity (handling novelty) — maps directly here.

6. **Data-asset decay under regulatory change**. Regulatory lag is long, but once a rule lands (GDPR erasure, EU AI Act data-governance, sector-specific consent changes) DA can drop discontinuously. Firms that had treated DA as a monotonically-growing stock are surprised. Pathological form: the R5 flywheel seizes and capability confidence drops.

7. **Integration-cost overhang**. The tooling lag plus hiring lag plus evaluation lag — each 2–9 months, largely additive when sequential — means total release-to-stable-integration can run two to three quarters. The A2 memo measures this as capability-to-adoption lag. Pathological form: the firm always runs ~2 releases behind and mistakes that lag for prudence.

---

## 6. Leverage points (Meadows)

Meadows's (1999) twelve leverage points run from weakest (12 — numbers, parameters) to strongest (1 — paradigm / transcending paradigm). Higher-numbered points are cheaper to change but produce smaller systemic effect; lower-numbered points are harder but more potent. The adaptability system exposes several of them. Three are prioritised below as actionable in 2026 contexts.

### 6.1 Which Meadows points apply, ranked by locus

| Meadows # | Meadows name | Manifestation in the three-pillar model |
|---|---|---|
| 12 | Constants, parameters, numbers | Evaluation budget %, hiring rate, compute reserve ratio |
| 11 | Buffer sizes | Organizational slack (OS); compute headroom; evaluation set coverage |
| 10 | Stock-flow structure | Whether evaluation is a gate (flow-limiting) or a filter (stock-accumulating); whether tooling has versioned export points (modular) or is bespoke |
| 9 | Delays | Incident disclosure latency; hiring lag; reorganization lag |
| 8 | Balancing-loop strength | Strength of B2 (incident correction), B3 (regulatory or insurance), B5 (ambidextrous separation) |
| 7 | Reinforcing-loop strength | Strength of R2 (verification debt) versus R3 (adoption pays) |
| 6 | Information flows | Who sees what incident data, what evaluator output; the governance DSM cells V→SI and G→PE from the sales-productization memo |
| 5 | System rules | Deploy-gate policy, role charters, promotion criteria, regulatory regime |
| 4 | Power to add, change, self-organize | Ability to form, kill, and recombine teams; ability to declare a new role or retire an old one |
| 3 | System goals | "Maximize this-quarter AI revenue" vs. "maintain capability-deployment parity while keeping trust debt bounded" |
| 2 | Paradigm | Whether leadership views AI as a static capability to be installed once, or as continuous flux to be metabolised |
| 1 | Transcending paradigm | The meta-stance that models, and even the three-pillar decomposition itself, are provisional |

### 6.2 Three prioritised leverage points for 2026 AI-era organizations

**Priority A — Meadows #9: Shorten the incident-realization and reorganization delays.** Mid-range difficulty, high payoff. Concretely: public incident registries (OECD AI Incidents Monitor, AI Incident Database) combined with mandatory internal post-mortem circulation within days, and standing reorganization authority held by a senior ambidextrous-org lead so B5 can fire without a 6–18-month political cycle. This is the delay-reduction lever that most directly tames R1–R2 without requiring a paradigm shift. Confidence: high.

**Priority B — Meadows #6: Redesign information flows across the V→SI and G→PE DSM cells.** Evaluation findings must reach sales commitments before commitments bind; governance policy must reach productization engineering before deploy decisions fire. In Beer VSM terms, this is installing System 2 (coordination) and System 4 (intelligence) channels. Low cost, high payoff when the firm has the political will; vanishes when it does not. Confidence: high.

**Priority C — Meadows #3: Reframe the system's explicit goal.** The single most commonly mis-stated organizational goal in the 2023–2026 AI-era is "deploy more AI." Replacing it with "maintain capability-deployment parity while keeping trust debt bounded and organizational slack above X%" re-points the selection pressure that cascades into every lower leverage point. This is Teece's (2007) *transforming* capability: the firm is asked to reshape its own evaluative criteria, not just its assets. Confidence: medium on operational feasibility; high on potency when achieved.

A fourth latent lever — Meadows #2, the paradigm shift from static-capability to continuous-flux metabolism — is the deepest but also the hardest. The author's own frame evolution (from "AI-based decision making" to "adaptability under continuous AI-driven change") is an instance of that shift. Most firms will not make it voluntarily; disruption theory (§7.5) predicts it will be imposed by incumbent failure.

---

## 7. Theory integration

Each subsection ties the M1 model to a specific theoretical tradition. The integrations are compressed; full treatment is deferred to M2 and the final synthesis memo.

### 7.1 Teece — dynamic capabilities (sensing, seizing, transforming)

Teece's (1997, 2007) three microfounded capabilities map directly onto three parts of the M1 model.

- **Sensing** ≈ the inflow to CD's *integration rate*, and the information flows at Meadows #6. A firm that cannot detect a capability release cannot close CD. Pathology 4 (talent vintage stratification) is a sensing failure when the hiring pipeline is staring at the wrong wave.
- **Seizing** ≈ flows into TL, TS, DA when a capability is identified as worth committing to. The R3 adoption-pays-for-adoption loop is the seizing loop. O'Reilly-Tushman's B5 protects seizing from being confused with exploitation of last quarter's capability.
- **Transforming** ≈ the ability to reshape stocks themselves — retire old tooling, retire old roles, rewrite stack assumptions. Directly Meadows #4 (self-organization) and #3 (goals). Hollnagel's (2014) *learning* capacity is the transformational substrate.

Fit: strong. Teece's language is the closest natural-language fit to the modelled stocks and flows. Confidence: high.

### 7.2 O'Reilly and Tushman — ambidextrous organization

R4 (exploitation crowds out exploration) and B5 (ambidextrous separation) are the direct operationalisation of O'Reilly and Tushman (2004). The model predicts that firms which install a structural B5 — a protected exploration unit with senior-level integration and a transfer mechanism — survive R1 treadmill effects without sacrificing R2 control. Firms that attempt "contextual ambidexterity" (every team does both) observe R4 domination under high R1 pressure. Fit: strong on structural ambidexterity; weaker on contextual ambidexterity (where the model would need to add interpersonal-level flows not currently represented). Confidence: high for large firms; medium for S1–S2 where the model's distinction collapses.

### 7.3 Hollnagel — resilience engineering and Safety-II

Hollnagel (2014) distinguishes Safety-I (preventing known failures) from Safety-II (handling novelty) and identifies four capacities: respond, monitor, learn, anticipate.

- *Respond* ≈ OS (organizational slack) — B6.
- *Monitor* ≈ evaluation-throughput capacity and information flows — B1, Meadows #6.
- *Learn* ≈ the transforming flow into skill vintage, tooling rewrite, and data-asset reuse — Meadows #3 and #4.
- *Anticipate* ≈ sensing capacity at R1 — Meadows #2 paradigm stance that the system is in continuous flux.

The pathology of "slack erosion under continuous pressure" is precisely the Safety-I trap: a firm that optimises for Safety-I known-failure prevention will cannibalise B6 and lose Safety-II capacity for novelty. Fit: strong; Hollnagel's capacities map cleanly onto the model's stocks and flows. Confidence: high.

### 7.4 Beer — Viable System Model

Beer's (1972, 1979) VSM names five systems: System 1 (operations), System 2 (coordination), System 3 (control / internal regulation), System 4 (intelligence / environment scanning), System 5 (policy / identity).

- System 1 ≈ the three pillars running in production.
- System 2 ≈ the coordination flows across V→SI and G→PE (Meadows #6).
- System 3 ≈ B1, B2 — internal verification and incident response.
- System 4 ≈ sensing at R1 — environmental scanning of the capability frontier.
- System 5 ≈ Meadows #3 and #2 — the firm's stated goal and paradigm.

VSM's key prescription — that System 3 and System 4 must balance, neither dominating — maps to the R4-vs-B5 tension of ambidexterity: System 3 dominance = exploitation trap; System 4 dominance = exploration without productization (wrapper quadrant in the Wave 4 matrix). Fit: strong structurally but the VSM vocabulary is less immediately legible than Teece or Meadows, so practical uptake is lower. Confidence: medium.

### 7.5 Christensen — disruption theory

Christensen's (1997) distinction between low-end and new-market disruption applies to the AI-era in a specific, partially modified form. The *low-end disruption* path — cheaper-but-inferior technology improves until it displaces incumbents — maps well to open-weight model families (Llama, Qwen, DeepSeek, Mistral) relative to closed-frontier offerings in 2024–2026. The *new-market disruption* path maps to agentic workflows opening non-consumption into addressable work (Sierra, Decagon, Cursor, Harvey for contract drafting). Where Christensen's theory modifies: in AI, the price-performance frontier moves so fast that incumbents cannot observe a long, stable low-end run-up; the disruption window compresses. Connection to M1: R1 is the treadmill that makes it structurally difficult for incumbents to avoid Christensen's innovator's dilemma without Meadows #2-level paradigm shift. Fit: moderate; the theory applies with compressed time scales. Confidence: medium.

### 7.6 Secondary references

- **Sterman (2000)** — the CLD vocabulary and archetype labels (erosion of goals, success to the successful, limits to growth) are Sterman's. Used throughout §4.
- **Cohen and Levinthal (1990)** absorptive capacity — TS + TL + DA jointly are the firm's absorptive capacity; R3 is the flywheel that grows it.
- **March (1991)** exploration / exploitation — the native language for R4 / B5. O'Reilly-Tushman is March made managerial.
- **Senge (1990)** — archetypes named in the R / B table above are Senge's packaging of Sterman.

---

## 8. Proposed interventions

Five design interventions, derived from the prioritised leverage points (§6.2). Each is stated at the level of a structural change the firm could actually install, with the loops it targets.

### I1. Dedicated evaluation-engineering function with deploy-gate authority

Install evaluation engineering as a named discipline with charter authority to block production deployment (not merely advisory review). Targets R2 directly by raising verification throughput and capping TD accrual. Shortens Pathology 3 (evaluation debt accumulation). Targets Meadows #6 (information flow: the deploy gate is where the information flow terminates in a decision). Lineage: the eval-engineering profession appendix already documents the emerging role signature; this intervention elevates it from role to structural control point.

### I2. Incident-transparency regime with short internal disclosure latency

Institute internal incident-disclosure SLAs: any AI behaviour flagged as incident-level must be visible to the ambidextrous-org lead within 48 hours and to the full evaluation function within one week, regardless of external disclosure timing. Targets Pathology 3 and the B2 delay. Targets Meadows #9 (delay reduction). External mirror: public incident registries (OECD AI Incidents Monitor, MIT AI Incident Database) accelerate the industry-level B2 by shortening cross-firm incident realization.

### I3. Ambidextrous separation with senior-level integration

Structurally separate an exploration unit (sensing-oriented, measured on capability-experiment throughput and new-market probes) from exploitation teams (measured on revenue and reliability). Integration happens only at senior / C-suite level, with explicit transfer contracts for experiments that graduate. Targets R4 with B5 installation. Directly O'Reilly-Tushman (2004). Beer VSM System 3 / System 4 balance check applies. Targets Meadows #4 (self-organization) and #5 (rules).

### I4. Compute and evaluation-set slack budget, monitored as a board-level metric

Formalise OS as a tracked resource: compute reserve as % of average load; evaluation-set coverage as % of deployed behaviour paths; engineer-weeks of unassigned capacity per quarter. Report to the board. Targets B6. Directly Hollnagel (2014) *respond* capacity. Targets Meadows #11 (buffer size). Practical anchor: reserve 15–25% of each resource type (inferred from S3–S4 evidence; calibration is an M2 task).

### I5. Reframe the primary operational goal from "deploy AI" to "maintain parity under flux"

The organization's explicit stated goal shifts from a deployment-volume metric to a composite (capability-deployment parity × bounded TD × maintained OS). Targets Meadows #3. This is a System 5 change in Beer's VSM — the firm's identity statement is altered. Observationally expensive (requires board and executive alignment); structurally potent because it re-points every lower-level selection pressure. Related to the author's original frame evolution from "AI-based decision making" to "adaptability under AI flux."

---

## 9. Testable hypotheses

Ten falsifiable predictions the model generates. Each is paired with a proposed empirical instrument. These are candidates for M2's dashboard and for the final synthesis memo's empirical programme.

1. **H1 (evaluation-engineering reduces deploy-to-incident lag)**: organizations with a dedicated evaluation-engineering function holding deploy-gate authority show ≥ 30% lower realized-incident rate per deployed model-feature compared to peers without such a gate, across 2024–2026. Instrument: case-controlled comparison on firms of matched size and domain.

2. **H2 (ambidextrous structural separation vs. capability lag)**: firms with O'Reilly-Tushman-style structural separation of exploration and exploitation show ≥ 40% shorter capability-to-deployment lag for category-changing capabilities (o1-class reasoning, tool-use, computer-use) than contextually-ambidextrous peers. Instrument: A2-style capability-adoption velocity chart, cut by org structure.

3. **H3 (incident disclosure latency drives industry correction)**: sectors with public incident registries and < 90-day disclosure norms show measurable decline in repeat-incident class frequency after 18 months of the registry, relative to pre-registry baseline. Instrument: OECD AI Incidents Monitor longitudinal.

4. **H4 (slack predicts resilience to model-generation shocks)**: firms that entered the GPT-4 → GPT-4o, GPT-5, Claude 4 transitions with OS ≥ 15% of engineering and compute capacity completed transitions in ≤ 50% of the engineering-months reported by OS < 5% peers. Instrument: A1 evidence extended with slack-capacity disclosures.

5. **H5 (tool-stock rot under model deprecation)**: within 12 months of a major model deprecation, ≥ 20% of a typical firm's tooling stock exhibits measurable rot (fails its own tests against current models), independent of whether the firm's inventory system flags it. Instrument: automated tooling regression audits (possible as T3 extension).

6. **H6 (talent-vintage turnover)**: the modal premium-priced AI hiring role turns over every 12–18 months (2022 ML engineer → 2023 prompt-engineer → 2024–25 agent-engineer → 2026 evaluation-engineer). Quarterly job-posting analyses show the premium salary concentration migrating accordingly. Instrument: LinkedIn + public job-board scrapes already established in A2 feeder work.

7. **H7 (regulatory-regime effect on trust-debt accumulation)**: firms operating primarily in EU AI Act high-risk / FDA-regulated / SR 11-7 sectors accumulate TD at < 50% of the rate observed in sales-instrument-regime peers (Japan METI, Korea AI Basic Act grace, US SEC disclosure-only). Instrument: cross-jurisdictional incident rate / deployment footprint.

8. **H8 (paradigm-shift firms outperform static-capability firms)**: firms whose public communications (annual reports, investor calls) re-stated AI as "continuous flux" rather than "installed capability" by year-end 2024 show higher 2026 revenue share from AI features released < 6 months earlier. Instrument: NLP-based stance classification of 2023–2024 public filings, compared against M2's "recent-release revenue share" indicator.

9. **H9 (R2 erosion-of-goals in sales-instrument regimes)**: firms whose sales commitments outrun productization by > 2 quarters (visible in public claim-vs-capability gap) accumulate incidents at a rate that predicts bankruptcy, rollback, or regulatory enforcement within 8–16 quarters, conditional on regime. Instrument: already in the sales-vs-productization matrix as Wave 5 follow-on.

10. **H10 (data-asset regulatory decay is discontinuous, not continuous)**: firms operating in jurisdictions enacting new AI data rules between 2024 and 2026 show a step-function drop in DA usability within 1 quarter of enforcement, not a gradual decay, contrary to the model's naive diffusion assumption. This hypothesis, if confirmed, calls for a modification of the DA outflow structure. Instrument: controlled case studies around named regulatory events (EU AI Act enforcement milestones, sector-specific rules).

Hypotheses H4, H7, and H9 are prioritised as the most testable and highest-leverage for 2026–2027 empirical follow-on.

---

## 10. Open questions and boundary problems

- **Endogenization of the frontier release cadence**. The model treats monthly capability releases as exogenous. In a more complete model, firm-to-lab feedback (enterprise contracts funding frontier training) endogenizes the frontier clock. The M1 scope did not attempt this; a follow-on at industry-level SDM scale should.
- **Person-level cognitive delays**. The learning lag is modelled at aggregate FTE level. Individual-level cognitive load, identity investment in obsolete skills, and workflow habits are compressed into averages. A managerial / HR-layer model would disaggregate.
- **Coupling with financial / capital market loops**. Valuation feedback (R1 amplification through capital availability) is only sketched. The full SDM ties this into an investor-firm loop that Sterman-style models of tech cycles have historically treated carefully.
- **Scale-tier applicability**. The default unit is a 50–50,000 FTE knowledge-work firm. S1 solo operators have collapsed pillars (single person plays all three); S7 international institutions have partially decoupled pillars running on different clocks. The loops R1–R5 and B1–B6 hold topologically but calibrate very differently. The scale-based track is the instrument for that.
- **Agentic AI as participant in its own loops**. As agents increasingly perform evaluation, tooling build, and even hiring shortlisting (2025–2026 observed), the firm-internal distinction between "human FTE" and "agent" starts to blur. The TS stock, in particular, may need to disaggregate agent-FTE-equivalents. Still speculative in 2026.
- **Cross-firm externalities through platform APIs**. Boudreau-Tiwana platform theory suggests governance failures at a wrapper firm may expose the platform firm (see the sales-vs-productization memo §6.2). The M1 boundary currently terminates at the single firm; a platform-level model would expand.
- **Path-dependence and hysteresis**. Once a firm has invested in infrastructure for a capability generation, the cost of switching exceeds the nominal rewrite cost because of sunk-cost politics. Model extension: stock-based infrastructure commitments should have asymmetric outflow (faster inflow, slower outflow). Not currently captured.

---

## 11. Feedback to three-pillar adaptability frame

- **The three pillars are coupled by named, structural feedback loops, not by coincidence.** R1–R5 and B1–B6 give specific semantics to the coupling. The engineering question (anchor 1 — how is the technical infrastructure designed and built) and the managerial question (anchor 2 — what operational and governance structures are required) cannot be answered independently: Pillar 3 infrastructure choices determine the loop strengths of R3 and B1, Pillar 2 org choices determine R4 vs B5 balance, Pillar 1 usage choices set the R1 cadence.

- **Adaptability is a stock, not a flag.** Organizational slack, skill vintage, tooling freshness, data-asset fitness, and trust debt are all stocks with distinct inflows and outflows. A one-time "transformation" that spikes a flow without sustaining it reverts to mean. The three-pillar adaptability frame should therefore be operationalised through stock-level indicators (M2 task), not event-level indicators.

- **Delays are the mechanism; paradigm is the lever.** Meadows's hierarchy implies that operating on numbers (budget %), buffers (slack ratios), and delays (disclosure latency) yields moderate gains; operating on system goals and paradigm yields large gains but demands leadership bandwidth that most firms cannot sustain. The framework should carry both levels — tactical and paradigmatic — because different firms have access to different leverage.

- **Engineering decisions and managerial decisions share loops.** The V-model / DSM analysis of the sales-vs-productization track already located coupling failures in specific cells (V→SI, G→PE). The M1 CLD extends that by naming R2 as the shared reinforcing loop that makes those cells fail. Engineering and management are not separate explanations of the same pathology; they are the same feedback structure observed from different pillars.

- **Resilience, not efficiency, is the adaptability signature.** Hollnagel's Safety-II, Beer's VSM System 4, Teece's transforming, and Meadows's #3 all converge: the adaptive organization over-provisions on slack, monitoring, and exploration relative to what a static efficiency metric would justify. The three-pillar frame should carry that as a load-bearing prescription: efficiency maximisation is a pathological goal in monthly-flux environments.

- **Decision making is relocated, not eliminated.** The author's original anchor — AI-based decision making — is preserved in the adaptability frame as the instantaneous output of the system. The M1 model predicts that a firm whose three-pillar system is mis-tuned will produce poor decisions not because of any individual judgment error but because the loops producing the inputs to judgment are themselves eroding. The adaptability research programme is therefore a necessary extension of, and not a replacement for, the decision-making programme.

---

## References

- Beer, S. (1972). *Brain of the Firm*. Allen Lane.
- Beer, S. (1979). *The Heart of Enterprise*. Wiley.
- Christensen, C. M. (1997). *The Innovator's Dilemma*. Harvard Business School Press.
- Cohen, W. M., and Levinthal, D. A. (1990). Absorptive capacity: a new perspective on learning and innovation. *Administrative Science Quarterly*, 35(1), 128–152.
- Forrester, J. W. (1961). *Industrial Dynamics*. MIT Press.
- Hollnagel, E. (2014). *Safety-I and Safety-II: The Past and Future of Safety Management*. Ashgate.
- March, J. G. (1991). Exploration and exploitation in organizational learning. *Organization Science*, 2(1), 71–87.
- Meadows, D. H. (1999). *Leverage Points: Places to Intervene in a System*. The Sustainability Institute.
- O'Reilly, C. A., and Tushman, M. L. (2004). The ambidextrous organization. *Harvard Business Review*, 82(4), 74–81.
- Senge, P. M. (1990). *The Fifth Discipline: The Art and Practice of the Learning Organization*. Doubleday.
- Sterman, J. D. (2000). *Business Dynamics: Systems Thinking and Modeling for a Complex World*. Irwin McGraw-Hill.
- Teece, D. J., Pisano, G., and Shuen, A. (1997). Dynamic capabilities and strategic management. *Strategic Management Journal*, 18(7), 509–533.
- Teece, D. J. (2007). Explicating dynamic capabilities: the nature and microfoundations of (sustainable) enterprise performance. *Strategic Management Journal*, 28(13), 1319–1350.
