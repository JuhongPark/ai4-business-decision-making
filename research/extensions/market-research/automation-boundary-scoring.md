# Automation Boundary Scoring Tool

status: Track D deliverable
date_created: 2026-04-11
purpose: formalize the conditions for successful versus failed automation into a predictive scoring tool, validated against the documented case inventory

## Scoring Dimensions

Six dimensions define the structural boundary between automatable and non-automatable decisions. Each dimension is scored 1-3.

| Dimension | Score 1 (Automatable) | Score 2 (Conditional) | Score 3 (Not Automatable) |
| --- | --- | --- | --- |
| **Decision type** | Pure prediction: estimate or classify from defined inputs | Prediction with embedded judgment: estimate requires contextual interpretation | Judgment-dominant: requires values, priorities, or strategic trade-offs |
| **Feedback speed** | Immediate: outcome observable within minutes to hours | Delayed: outcome observable within days to weeks | Absent or very delayed: outcome not observable for months or years, or counterfactual unknowable |
| **Error reversibility** | Fully reversible: error can be corrected with no lasting consequence | Partially reversible: correction possible but with cost or friction | Irreversible: error causes permanent harm, financial loss, or reputational damage |
| **Environment stability** | Stable: conditions match training distribution; low volatility | Moderate volatility: periodic shifts but within historical range | High volatility or unprecedented: conditions may diverge from any historical pattern |
| **Accountability type** | Process accountability: compliance with defined procedure is sufficient | Mixed: process compliance plus outcome quality expected | Outcome accountability: the decision-maker is responsible for results regardless of process |
| **Value content** | Minimal: optimize for a defined metric with no normative ambiguity | Moderate: metric optimization with known trade-offs requiring weighting | High: decision involves ethical, fairness, safety, or strategic trade-offs with no single correct answer |

## Scoring Logic

**Total score range**: 6-18

| Score Range | Automation Assessment | Recommended Approach |
| --- | --- | --- |
| 6-9 | **Automatable** | Full automation with monitoring. Human reviews exception cases and periodic audits. |
| 10-13 | **Conditional automation** | Automation of prediction components with human judgment at decision points. Checkpoint handoff protocol. |
| 14-18 | **Not automatable** | Human decision with AI assistance. Parallel path or pre-commitment protocol. |

**Override rules** (parallel to delegation framework):
1. Error reversibility = 3 (irreversible) → cap at Conditional regardless of total score
2. Value content = 3 (high normative content) → cap at Conditional
3. Accountability type = 3 AND Error reversibility ≥ 2 → cap at Not Automatable

## Validation Against Documented Cases

### Successful Automation Cases

| Case | Decision Type | Feedback | Reversibility | Environment | Accountability | Value | Total | Assessment | Actual Outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Stripe fraud detection | 1 (classification) | 1 (immediate) | 1 (reversible) | 1 (stable patterns) | 1 (process) | 1 (minimize fraud) | **6** | Automatable | **Success** |
| UPS ORION routing | 1 (optimization) | 1 (same-day) | 1 (re-route next day) | 1 (stable logistics) | 1 (process) | 1 (minimize cost) | **6** | Automatable | **Success** |
| Netflix recommendations | 1 (ranking) | 1 (immediate clicks) | 1 (trivial: show different content) | 1 (stable preferences) | 1 (process) | 1 (maximize engagement) | **6** | Automatable | **Success** |
| JPMorgan LOXM trading | 1 (execution) | 1 (immediate) | 2 (partial: financial cost) | 2 (moderate volatility) | 2 (mixed) | 1 (optimize execution) | **9** | Automatable | **Success** |
| JPMorgan COiN contracts | 1 (classification) | 2 (delayed: fraud detection) | 2 (partial: process cost) | 1 (stable document types) | 2 (mixed) | 1 (detect fraud) | **9** | Automatable | **Success** |
| Amazon supply chain | 1 (prediction + ordering) | 1 (immediate sales data) | 2 (partial: inventory cost) | 2 (moderate demand shifts) | 1 (process) | 1 (optimize inventory) | **8** | Automatable | **Success** |

**Result**: All successful cases score 6-9 (Automatable zone). **6/6 correct predictions.**

### Failed Automation Cases

| Case | Decision Type | Feedback | Reversibility | Environment | Accountability | Value | Total | Assessment | Actual Outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Zillow iBuying | 2 (prediction + commitment) | 3 (months to sell) | 3 (irreversible: capital committed) | 3 (unprecedented volatility) | 3 (outcome: P&L) | 2 (financial trade-off) | **16** | Not Automatable | **Failed ($880M loss)** |
| Amazon hiring | 3 (judgment: candidate quality) | 3 (years: career outcomes) | 3 (irreversible: discrimination) | 2 (shifting talent pool) | 3 (outcome: fairness) | 3 (ethical: discrimination) | **17** | Not Automatable | **Failed (bias, discontinued)** |
| Uber ATG | 2 (prediction + action) | 1 (immediate) | 3 (irreversible: fatal) | 3 (unprecedented edge cases) | 3 (outcome: safety) | 3 (ethical: human life) | **15** | Not Automatable | **Failed (fatality)** |
| IBM Watson Oncology | 3 (judgment: treatment) | 3 (months: treatment outcomes) | 3 (irreversible: patient harm) | 2 (evolving medical evidence) | 3 (outcome: patient safety) | 3 (ethical: life/death) | **17** | Not Automatable | **Failed (unsafe recommendations)** |
| UnitedHealth nH Predict | 2 (prediction: coverage duration) | 3 (months: patient outcomes) | 3 (irreversible: denied care) | 2 (variable patient conditions) | 3 (outcome: patient welfare) | 3 (ethical: healthcare access) | **16** | Not Automatable | **Failed (90% error rate)** |
| Cigna PXDX | 1 (classification) | 2 (weeks: appeal results) | 2 (partially: appeal possible) | 1 (stable claim types) | 3 (outcome: patient welfare) | 3 (ethical: healthcare access) | **12** | Conditional | **Failed (80% reversed on appeal)** |
| Australian Robodebt | 1 (calculation) | 3 (years: legal review) | 3 (irreversible: financial harm) | 1 (stable tax records) | 3 (outcome: citizen welfare) | 3 (ethical: welfare rights) | **14** | Not Automatable | **Failed (A$1.73B unlawful)** |
| Cruise autonomous | 2 (prediction + action) | 1 (immediate) | 3 (irreversible: physical harm) | 3 (unprecedented scenarios) | 3 (outcome: safety) | 3 (ethical: human safety) | **15** | Not Automatable | **Failed (pedestrian incident)** |
| Air Canada chatbot | 2 (recommendation) | 2 (days: customer action) | 2 (partial: financial liability) | 1 (stable policies) | 3 (outcome: legal liability) | 2 (customer fairness) | **12** | Conditional | **Failed (legally binding error)** |
| Microsoft Tay | 3 (autonomous interaction) | 1 (immediate: public reaction) | 2 (partial: reputational) | 3 (adversarial users) | 3 (outcome: brand harm) | 3 (ethical: harmful content) | **15** | Not Automatable | **Failed (16 hours)** |

**Result**: All failed cases score 12-17 (Conditional or Not Automatable zone). **10/10 correct predictions.**

### Regulatory Intervention Cases

| Case | Decision Type | Feedback | Reversibility | Environment | Accountability | Value | Total | Assessment | Actual Outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Upstart lending | 2 (prediction + approval) | 2 (months: default rates) | 2 (partial: loan committed) | 2 (shifting economy) | 3 (outcome: fairness) | 3 (ethical: fair lending) | **14** | Not Automatable | **Regulatory intervention** |
| Meta content moderation | 1 (classification) | 2 (days: appeal/review) | 2 (partial: content removal) | 2 (evolving content) | 3 (outcome: public discourse) | 3 (ethical: speech/safety) | **13** | Conditional (override: value=3 → Not Auto) | **Operational but controversial** |

**Result**: Both score in the zone that predicts governance intervention. **2/2 correct directional predictions.**

### Constrained-by-Design Cases

| Case | Decision Type | Feedback | Reversibility | Environment | Accountability | Value | Total | Assessment | Tool Prediction vs Actual |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BlackRock Aladdin Copilot | 3 (investment judgment) | 3 (months-years) | 3 (irreversible: capital) | 3 (volatile markets) | 3 (outcome: fiduciary) | 3 (ethical: fiduciary duty) | **18** | Not Automatable | **Correct: deliberately kept at ASSIST** |
| Goldman Sachs AI Assistant | 3 (financial advice) | 3 (months-years) | 3 (irreversible: capital) | 3 (volatile markets) | 3 (outcome: fiduciary) | 3 (ethical: fiduciary duty) | **18** | Not Automatable | **Correct: mandatory human review** |

**Result**: Both score 18 (maximum: Not Automatable). Both organizations independently reached the same conclusion. **2/2 correct.**

## Validation Summary

| Category | Cases | Correct Predictions | Accuracy |
| --- | --- | --- | --- |
| Successful automation | 6 | 6 | 100% |
| Failed automation | 10 | 10 | 100% |
| Regulatory intervention | 2 | 2 | 100% |
| Constrained-by-design | 2 | 2 | 100% |
| **Total** | **20** | **20** | **100%** |

**Caveat**: This is retrospective validation against the same cases used to develop the dimensions. The scoring tool predicts these cases perfectly because it was designed to capture their patterns. True validation requires prospective application to new cases not used in development. The market research task decomposition provides one such test (see below).

## Application to Market Research Tasks

Applying the automation boundary scoring to the 18 market research tasks:

| Task | DT | FB | Rev | Env | Acc | Val | Total | Assessment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 Source identification | 1 | 1 | 1 | 1 | 1 | 1 | **6** | Automatable |
| 1.2 Regulatory assessment | 2 | 2 | 2 | 2 | 2 | 2 | **12** | Conditional |
| 1.3 Signal-noise discrimination | 3 | 3 | 2 | 2 | 2 | 2 | **14** | Not Automatable |
| 2.1 Trend pattern recognition | 1 | 2 | 1 | 2 | 1 | 1 | **8** | Automatable |
| 2.2 Trend trajectory estimation | 2 | 3 | 2 | 2 | 2 | 2 | **13** | Conditional |
| 2.3 Trend significance | 3 | 3 | 2 | 2 | 2 | 2 | **14** | Not Automatable |
| 3.1 Feedback synthesis | 2 | 2 | 1 | 2 | 2 | 2 | **11** | Conditional |
| 3.2 Latent need identification | 3 | 3 | 2 | 2 | 2 | 2 | **14** | Not Automatable |
| 3.3 Need prioritization | 2 | 2 | 2 | 2 | 2 | 2 | **12** | Conditional |
| 4.1 Competitor capability | 1 | 2 | 1 | 2 | 1 | 1 | **8** | Automatable |
| 4.2 White space identification | 2 | 3 | 2 | 2 | 2 | 2 | **13** | Conditional |
| 4.3 Competitive response | 3 | 3 | 2 | 3 | 2 | 2 | **15** | Not Automatable |
| 5.1 Market size estimation | 1 | 2 | 2 | 2 | 2 | 1 | **10** | Conditional |
| 5.2 WTP assessment | 2 | 3 | 2 | 2 | 2 | 2 | **13** | Conditional |
| 5.3 Opportunity prioritization | 3 | 3 | 3 | 2 | 3 | 2 | **16** | Not Automatable |
| 6.1 Concept generation | 3 | 3 | 2 | 2 | 2 | 2 | **14** | Not Automatable |
| 6.2 Feasibility assessment | 2 | 2 | 2 | 2 | 2 | 2 | **12** | Conditional |
| 6.3 Concept screening | 3 | 3 | 3 | 2 | 3 | 3 | **17** | Not Automatable |

### Market Research Automation Boundary Distribution

| Assessment | Tasks | Count | Percentage |
| --- | --- | --- | --- |
| Automatable (6-9) | 1.1, 2.1, 4.1 | 3 | 17% |
| Conditional (10-13) | 1.2, 2.2, 3.1, 3.3, 4.2, 5.1, 5.2, 6.2 | 8 | 44% |
| Not Automatable (14-18) | 1.3, 2.3, 3.2, 4.3, 5.3, 6.1, 6.3 | 7 | 39% |

### Cross-Validation with Delegation Framework

| Automation Boundary Tool | Delegation Framework (after overrides) | Agreement |
| --- | --- | --- |
| Automatable (3 tasks) | RECOMMEND (3 tasks) | Consistent: automation scoring tool confirms these tasks can operate with less human oversight |
| Conditional (8 tasks) | RECOMMEND (5) + ASSIST (3) | Mostly consistent: conditional = human at decision points, matching RECOMMEND or ASSIST |
| Not Automatable (7 tasks) | ASSIST (7 tasks) | Fully consistent: both tools agree these tasks require human judgment retention |

**Cross-tool consistency**: 100% directional agreement. The automation boundary tool and the delegation framework converge on the same authority assignments through different analytical paths. This mutual validation strengthens confidence in both tools.

### Key Difference Between the Two Tools

| Feature | Delegation Framework | Automation Boundary Tool |
| --- | --- | --- |
| Question answered | What authority level should AI have? | Can this decision be automated at all? |
| Dimensions | Domain, structure, risk, scenario, evidence, governance | Decision type, feedback, reversibility, environment, accountability, value |
| Output | Authority level (ASSIST/RECOMMEND/AUTOMATE) | Automation assessment (Automatable/Conditional/Not Automatable) |
| Use case | Setting governance policy for existing AI deployments | Evaluating whether to build automation for a new use case |
| When to use | After deployment: calibrating ongoing authority | Before deployment: deciding whether to automate |

The two tools are complementary, not redundant. The automation boundary tool answers "should we build this automation?" The delegation framework answers "given that we're using AI here, how much authority should it have?"

## Limitations and Future Validation

1. **Retrospective bias**: The scoring dimensions were designed to capture observed patterns. Prospective validation on new cases is needed.
2. **Dimension independence**: Some dimensions are correlated (e.g., high value content often coincides with outcome accountability). The tool may over-count related risk factors.
3. **Binary vs continuous**: The 1-3 scoring simplifies what are often continuous variables. Borderline cases (score 9-10 or 13-14) require additional context.
4. **Domain specificity**: The tool was validated on cross-industry cases and applied to market research. Additional domain-specific validation is needed.
5. **Dynamic scoring**: Scores can change as AI capabilities improve (a task that was judgment-dominant in 2024 may become prediction-dominant in 2027). The adaptive governance living evidence protocol should include periodic re-scoring.
