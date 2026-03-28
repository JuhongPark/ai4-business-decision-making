# Narrative Bridge: The 71-Incident Inventory Reframed as Reasoning Acceptance Failures

status: draft
date: 2026-03-28
purpose: Reframe the project's incident inventory through the lens of reasoning trust failure, showing that the common thread across general AI and LLM incidents is unchecked reasoning, not just governance failure.
synthesis-plan-phase: 1.2

## Why This Reframing Matters

The incident inventory documents 71 business-relevant AI failures. The existing analysis classified them by governance failure mode (specification gaming, distribution shift, oversight failure, fluent hallucination) and tested whether the 6-dimensional delegation framework would have prevented them.

Results: 12 of 20 key incidents were fully prevented by the framework, 7 were partially flagged, and 1 was missed entirely.

That is a meaningful governance result. But it is incomplete.

The delegation framework answers the question: **when should an organization keep humans in the loop?** It provides graduated authority levels (assist, recommend, automate with guardrails), override rules for high-risk contexts, and scoring dimensions that evaluate governance readiness, evidence strength, risk level, decision structure, and scenario stability.

But in many of the documented incidents, humans were nominally in the loop. The framework's assumption held: humans had formal authority over the AI-influenced decision. And the failures still occurred.

The reason is that the framework addresses the **when** of human oversight but not the **how** of verification. It tells the organization to keep a human involved at a given authority level. It does not tell that human what to check, how to evaluate the AI's reasoning path, or when the reasoning itself is the source of risk.

This document reframes the 18 key incidents as reasoning acceptance failures. The argument is not that governance was irrelevant. Governance was necessary. The argument is that governance was insufficient because it did not include a method for verifying the reasoning behind AI outputs.

## The Reframing Thesis

Across both general AI and LLM incidents, the underlying failure pattern is the same:

**AI reasoning was accepted without adequate verification of the reasoning path itself.**

The mechanism differs by era:

- In general AI incidents, the reasoning is encoded in optimization objectives, scoring functions, and ranking algorithms. It is opaque by design. No one checked whether the model's internal logic was optimizing for the right thing, because the logic was not visible.
- In LLM incidents, the reasoning is expressed in fluent natural language. It is visible but deceptive. No one checked whether the reasoning was sound, because the output looked professional and the interface invited acceptance rather than scrutiny.

The common thread: in both cases, the organization lacked a method for evaluating whether the AI's reasoning path was valid for the decision at hand. The delegation framework can flag that a human should be involved. But it cannot ensure that the involved human performs substantive reasoning verification.

## Part I: General AI Incidents Reframed

The general AI incidents in the inventory are predominantly specification gaming and optimization side-effect failures. The standard reading is that these are governance failures: wrong objectives, biased data, weak oversight.

The reframing adds a layer: these are also cases where the AI's internal reasoning was never examined. The model optimized for something, produced outputs consistent with that optimization, and the organization accepted those outputs without asking whether the reasoning path behind them was aligned with the actual business objective.

### Incident-Level Reframing

| Incident | Standard Classification | Reasoning Acceptance Failure | Reasoning Verification Question That Would Have Caught It |
|---|---|---|---|
| **Zillow Offers** ($304M loss) | Forecast error plus over-delegation to predictive models | The pricing model optimized for proxy metrics (statistical patterns in historical price data) rather than genuine market value indicators. The organization accepted model outputs as actionable pricing signals without verifying that the reasoning path connected to real market fundamentals. | "Does this pricing reasoning rely on genuine market value indicators, or is it finding statistical shortcuts in historical data that may not hold under market volatility?" |
| **Amazon recruiting** | Training-data bias and proxy discrimination | The resume screening model learned to use gender-correlated features as proxies for candidate quality. The reasoning path from "this resume has feature X" to "this candidate is less qualified" was never examined for whether feature X was a legitimate quality indicator or a demographic proxy. | "Is the model's reasoning about candidate quality based on job-relevant qualifications, or does it rely on features that correlate with protected characteristics?" |
| **Uber ATG crash** | Weak safety culture and oversight | The automated driving system's safety reasoning was accepted without scrutiny of its failure mode coverage. The system classified pedestrians according to internal logic that was never verified against the full range of real-world scenarios. The safety assessment process itself was a form of reasoning acceptance: the organization treated the system's operational envelope claims as valid without independent verification. | "Does the safety assessment reasoning account for all relevant pedestrian detection failure modes, including edge cases outside the training distribution?" |
| **Meta housing ads** | Algorithmic discrimination in ad delivery | The ad delivery algorithm's targeting reasoning optimized for engagement and conversion metrics. The reasoning path from "this user profile predicts engagement" to "show this housing ad to this user" was never checked for whether the optimization was reproducing discriminatory patterns prohibited by fair housing law. | "Does the targeting reasoning conform to fair housing requirements, or does the optimization path produce delivery patterns that function as prohibited discrimination?" |
| **Rite Aid facial recognition** | False positives with disproportionate harm | The identification system's reasoning assigned match confidence scores that were treated as sufficient for consequential action (confronting or monitoring individuals). The reasoning path from "this face has similarity score X" to "this person should be flagged" was accepted without verifying that the confidence threshold was appropriate for the severity of the consequence. | "Does the identification reasoning meet the confidence threshold required for the consequential action that follows, given the documented false positive rates across demographic groups?" |
| **iTutorGroup / Workday hiring** | Age-based or algorithm-mediated automated rejection | The screening systems applied rejection logic that encoded age-based or proxy-based criteria. In iTutorGroup's case, explicit age cutoffs were programmed into the system. In the Workday litigation, the claim is that algorithmic screening reproduced discriminatory patterns through delegated decision-making. In both cases, the screening reasoning was accepted without verification against employment law norms. | "Does the screening reasoning conform to employment law, and does the rejection path rely on criteria that are legally permissible for the job in question?" |
| **RealPage** | Algorithmic pricing coordination | The pricing algorithm's reasoning incorporated competitor pricing data to recommend rental prices. The reasoning path from "comparable units are priced at X" to "recommend price Y" was accepted as legitimate market intelligence without examining whether the coordination mechanism produced outcomes that function as unlawful price-fixing. | "Does the pricing reasoning produce outcomes consistent with competition law, or does the data-sharing mechanism create a coordination effect that substitutes for independent pricing decisions?" |
| **FloatMe** | Deceptive algorithmic underwriting claims | The company marketed its cash-advance eligibility algorithm as providing certain outcomes that the algorithm did not actually deliver. The reasoning gap was between the marketed claims and the actual algorithmic logic. This is a reasoning verification failure at the organizational level: the firm's public reasoning about what its algorithm does did not match what the algorithm actually did. | "Does the underwriting reasoning actually match the marketed claims, and can the algorithm's eligibility logic be verified against the representations made to consumers?" |

### Pattern: Opaque Optimization as Unverified Reasoning

The general AI incidents share a structural pattern. In each case:

1. The AI system contained an internal reasoning path (an optimization objective, a scoring function, a classification rule).
2. That reasoning path produced outputs (prices, rankings, scores, identifications, delivery patterns).
3. The organization accepted the outputs as valid inputs to business decisions.
4. No one verified whether the reasoning path was aligned with the actual business objective, the legal constraints, or the welfare of affected people.

The standard governance reading focuses on the objective and the oversight. The reasoning trust reading adds: even if the objective had been better specified and the oversight had been stronger, the failure could still have occurred if no one had a method for examining the reasoning path itself.

This matters because of the 12 incidents the delegation framework fully prevented, most were cases where the framework would have lowered authority or triggered an override rule before the reasoning path had a chance to cause harm. But the 7 partially flagged and 1 missed incident are predominantly cases where the framework assigned appropriate authority but the human in the loop still could not verify the reasoning. The gap is not in when to involve a human. The gap is in what that human should examine.

## Part II: LLM Incidents Reframed

The LLM incidents differ mechanically but share the same underlying failure. Where general AI reasoning is opaque, LLM reasoning is visible but deceptive: it reads as professional, coherent, and confident, which makes it harder to question rather than easier to verify.

### Incident-Level Reframing

| Incident | Standard Classification | Reasoning Acceptance Failure | Reasoning Verification Question That Would Have Caught It |
|---|---|---|---|
| **Air Canada chatbot** | Fluent policy misstatement and customer reliance | The chatbot generated a policy explanation that sounded authoritative and specific. The reasoning path from "the customer asked about bereavement fares" to "here is the policy" was fluent and confident, but the underlying policy reasoning was fabricated. The customer accepted it because the interface (an airline's official website chatbot) conferred legitimacy and the language conferred confidence. | "Does this policy reasoning accurately reflect actual company rules as documented in the approved policy source, or is the system generating a plausible-sounding policy that may not exist?" |
| **Mata v. Avianca** | Hallucinated case citations | The LLM generated legal citations that were structurally correct (proper case name format, plausible court, reasonable year) but entirely fabricated. The reasoning path from "I need supporting cases" to "here are relevant precedents" was fluent and superficially persuasive. The attorneys accepted the reasoning because the citations looked real and the analysis appeared professionally written. | "Are the cited sources real, and does the legal reasoning they are claimed to support actually appear in those sources?" |
| **AP Electric** | Fabricated quotations and parentheticals | Same pattern as Mata but with a deeper failure: the AI generated accurate case names paired with fabricated quotations and parenthetical descriptions. This is a more sophisticated reasoning failure because it mixes real references with invented content, making verification harder. The court explicitly noted that real case names do not solve LLM reliability problems. | "Even where the case citations are real, are the specific quotations, holdings, and parenthetical descriptions accurately drawn from those sources, or has the system fabricated content attributed to real authorities?" |
| **Samsung data leakage** | Prompt-based leakage of confidential data | This incident is a boundary failure rather than a reasoning failure. Employees did not accept bad reasoning from the AI; they disclosed confidential information to an external system. The failure is in organizational controls, not in reasoning verification. It is included here for completeness but does not fit the reasoning acceptance pattern. | N/A (boundary control failure, not reasoning acceptance failure) |
| **Google Bard demo** ($100B+ market cap loss) | Hallucinated factual error in high-visibility demo | The system generated a factual claim about the James Webb Space Telescope that was wrong. The reasoning path from "the user asked a factual question" to "here is the answer" produced a confident, specific, and incorrect statement. The demo team accepted the output without independently verifying the factual premises before a public presentation with enormous financial exposure. | "Are the factual premises of this reasoning verified against authoritative sources before this output is used in a public presentation?" |
| **CNET AI articles** | Factual errors in AI-generated finance content | The AI-generated articles contained financial reasoning with factual errors. The content was published because it read as professionally written and editorially plausible. The review process did not catch the errors because the generated prose was fluent enough to pass a surface-level editorial check. | "Does the financial reasoning in this content rely on verified data, and have the specific numerical claims and procedural descriptions been checked against authoritative financial sources?" |
| **DPD chatbot** | Prompt-induced rogue behavior | This incident is a control failure rather than a reasoning acceptance failure. The chatbot was manipulated through adversarial prompting to produce inappropriate responses. The organization did not accept bad reasoning; the system's behavioral boundaries were breached. Like Samsung, it does not fit the reasoning acceptance pattern. | N/A (prompt control failure, not reasoning acceptance failure) |
| **Elegant Enterprise Solutions** | AI-generated job ads that excluded US workers | The AI generated job advertisement text that violated employment law by excluding applicants based on citizenship status. The reasoning path from "generate a job ad for this position" to the discriminatory text was not reviewed for legal compliance before publication. The organization accepted the generated content as usable output without verifying that its normative content was lawful. | "Does the job posting content comply with employment regulations, and has the generated text been reviewed for discriminatory language or unlawful exclusion criteria?" |

### Pattern: Fluent Narration as Unverified Reasoning

The LLM incidents share a different structural pattern from the general AI cases, but the core failure is the same:

1. The LLM produced output that contained an implicit or explicit reasoning path (a policy explanation, a legal argument, a factual claim, a financial analysis, a job advertisement).
2. That reasoning path was expressed in fluent, confident, professional-sounding language.
3. The recipient accepted the reasoning as sound because the output looked and read as though a competent professional had written it.
4. No one verified whether the reasoning path was factually grounded, logically valid, or normatively acceptable.

The key difference from general AI is the mechanism of acceptance. In general AI, reasoning was accepted because it was invisible: the model produced a number, and the number was used. In LLM incidents, reasoning was accepted because it was fluent: the model produced a narrative, and the narrative was believed.

Both mechanisms lead to the same outcome: unverified reasoning causes harm.

## Part III: The Cross-Era Pattern

### What the Delegation Framework Catches and What It Misses

The framework's 20-incident test produced three categories of results:

| Category | Count | What the framework did | What was still needed |
|---|---|---|---|
| Fully prevented | 12 | Framework correctly restricted authority or triggered override rules, preventing the AI from gaining enough influence to cause harm | Nothing additional needed at the governance level |
| Partially flagged | 7 | Framework identified risk factors but could not prevent harm because the human in the loop lacked a method to verify the specific reasoning failure | Reasoning verification capability for the involved human |
| Missed entirely | 1 | Framework did not flag the incident because the failure occurred outside the scored dimensions | Expansion of the assessment scope |

The 7 partially flagged and 1 missed incident are disproportionately cases where output-level reasoning verification, not just governance-level delegation rules, would have been needed. The framework said "keep a human involved." The human was involved. The human could not evaluate the reasoning.

### Two Eras, One Failure Mode

| Dimension | General AI Incidents | LLM Incidents |
|---|---|---|
| **Nature of AI reasoning** | Encoded in optimization objectives and scoring functions | Expressed in natural language |
| **Visibility of reasoning** | Opaque (hidden inside model parameters) | Visible but deceptive (fluent and confident) |
| **Why reasoning was accepted** | The output was a number; numbers feel objective | The output was a narrative; narratives feel professional |
| **What verification would require** | Inspecting the optimization path for proxy reliance, bias encoding, and objective misalignment | Checking factual premises, inferential validity, and normative acceptability of the generated reasoning |
| **Why verification did not happen** | No accessible method for inspecting model internals in deployment contexts | No established practice for scrutinizing AI-generated reasoning; the interface discourages questioning |
| **Governance layer (delegation framework)** | Can restrict authority based on risk, evidence, and governance scores | Can restrict authority based on risk, evidence, and governance scores |
| **Missing layer** | Reasoning path verification for opaque systems | Reasoning path verification for fluent systems |

The common thread is that the delegation framework provides the governance layer but not the verification layer. It correctly identifies when humans should be involved. It does not equip those humans to verify AI reasoning.

### The Structural Assumption

The 6-dimensional delegation framework contains an implicit assumption that is now visible through the incident reframing:

**The framework assumes that when it assigns "assist" or "recommend" authority, the human decision-maker can evaluate the AI's output well enough to use it safely.**

This assumption holds when:

- The output is a simple prediction or classification that the human can cross-check against domain knowledge
- The human has independent access to the evidence base
- The organizational review architecture separates generation from validation
- The human has been trained to question AI outputs rather than accept them

The assumption fails when:

- The output contains embedded reasoning that the human cannot independently evaluate (general AI cases)
- The output is fluent enough to suppress the instinct to verify (LLM cases)
- The review happens inside the same interface that generated the output (Mata, AP Electric)
- The human lacks a structured method for reasoning verification (nearly all cases)

This is the gap that the reasoning verification framework must fill. The delegation framework tells the organization when to keep a human in the loop. The reasoning verification framework must tell that human how to evaluate what the AI has produced.

## Part IV: What Reasoning Verification Would Have Asked

For each of the 18 key incidents, a reasoning verification step would have introduced a structured question between the AI's output and the human's acceptance of that output. The verification questions cluster into four types.

### Type 1: Source Quality Verification

**Question pattern:** Are the factual inputs and cited authorities real, current, and relevant?

**Incidents addressed:** Mata v. Avianca, AP Electric, Google Bard demo, CNET AI articles

This is the most straightforward verification type. It asks whether the reasoning rests on real evidence. In the LLM era, this corresponds to hallucination detection, but it extends beyond simple fact-checking to include the quality and relevance of the sources the reasoning relies on.

### Type 2: Inferential Validity Verification

**Question pattern:** Does the conclusion follow from the premises, or is there a logical gap, proxy reliance, or unjustified leap?

**Incidents addressed:** Zillow Offers, Amazon recruiting, Meta housing ads, RealPage, Air Canada chatbot

This type checks the reasoning path itself. Even if the inputs are correct, the inference may be flawed. Zillow's models may have used real market data but drew conclusions about pricing that did not account for volatility. Amazon's model used real resume features but drew inferences about quality that were proxies for gender. The Air Canada chatbot constructed a policy explanation that was internally coherent but did not correspond to real policy.

### Type 3: Normative Acceptability Verification

**Question pattern:** Does the reasoning produce outcomes that conform to legal requirements, ethical standards, and domain-specific professional norms?

**Incidents addressed:** Meta housing ads, Rite Aid, iTutorGroup/Workday, RealPage, FloatMe, Elegant Enterprise Solutions

This type checks whether the reasoning path, even if factually grounded and logically coherent, produces outcomes that are acceptable within the relevant normative framework. A pricing algorithm can be factually grounded and logically valid but still produce outcomes that violate competition law. A screening algorithm can use real data and valid inference but still violate employment discrimination rules.

### Type 4: Confidence Calibration Verification

**Question pattern:** Does the certainty expressed in the output match the actual reliability of the underlying reasoning?

**Incidents addressed:** Uber ATG, Google Bard demo, Rite Aid, Air Canada chatbot

This type checks whether the AI's expressed confidence is warranted. The Bard demo produced a factual claim with no hedging. The Air Canada chatbot stated policy as definitive fact. The Rite Aid system assigned match scores that were treated as high-confidence identifications. In each case, the output expressed more certainty than the reasoning could support.

### How the Four Types Map to the Incident Inventory

| Incident | Source Quality | Inferential Validity | Normative Acceptability | Confidence Calibration |
|---|---|---|---|---|
| Zillow Offers | | Primary | | Secondary |
| Amazon recruiting | | Primary | Primary | |
| Uber ATG | | Secondary | | Primary |
| Meta housing ads | | Primary | Primary | |
| Rite Aid | | | Primary | Primary |
| iTutorGroup / Workday | | | Primary | |
| RealPage | | Primary | Primary | |
| FloatMe | | | Primary | |
| Air Canada chatbot | Primary | | | Primary |
| Mata v. Avianca | Primary | | | |
| AP Electric | Primary | | | |
| Samsung | N/A | N/A | N/A | N/A |
| Google Bard demo | Primary | | | Primary |
| CNET AI articles | Primary | Primary | | |
| DPD chatbot | N/A | N/A | N/A | N/A |
| Elegant Enterprise Solutions | | | Primary | |

Note: Samsung and DPD are classified as boundary control failures and prompt control failures respectively, not reasoning acceptance failures. They are included for inventory completeness.

### Reading the Pattern

The mapping reveals a clear distribution:

- **Source quality failures** dominate LLM incidents (Mata, AP Electric, Bard, CNET, Air Canada). This is the hallucination problem, but reframed as a reasoning verification problem: the reasoning rested on sources that were fabricated, wrong, or absent.
- **Inferential validity failures** dominate general AI incidents (Zillow, Amazon, Meta, RealPage, CNET). This is the specification gaming and proxy reliance problem, reframed: the reasoning path from inputs to conclusions contained unjustified inferential leaps.
- **Normative acceptability failures** span both categories (Meta, Rite Aid, iTutorGroup, Workday, RealPage, FloatMe, Elegant Enterprise). These are the incidents where the reasoning was technically functional but produced outcomes that violated legal or ethical norms.
- **Confidence calibration failures** appear as secondary failures across both categories (Uber, Bard, Rite Aid, Air Canada, Zillow). In each case, the output expressed a level of certainty that exceeded what the underlying reasoning could justify.

This distribution suggests that a reasoning verification framework needs all four verification types. No single type covers the full range of failure modes. Source quality verification alone would miss the inferential and normative failures. Normative verification alone would miss the hallucination cases. A complete framework requires all four layers operating together.

## Part V: Why This Reframing Changes the Research Direction

### From Governance to Verification

The original incident analysis asked: would the delegation framework have prevented this failure?

The reframing asks a different question: even where the framework placed humans in the loop, did those humans have a method for verifying the AI's reasoning?

The answer, across 16 of 18 key incidents (excluding Samsung and DPD as non-reasoning failures), is no.

This is not a criticism of the delegation framework. The framework was designed to address the governance question: when and how much authority should AI have? It answers that question well. The 12 fully prevented incidents demonstrate its value.

But the 7 partially flagged and 1 missed incident expose a structural gap. The framework depends on a verification capability that it does not itself provide. When it says "keep the human in the loop," it assumes the human can evaluate what the AI has produced. That assumption fails when:

- The AI's reasoning is opaque (general AI)
- The AI's reasoning is fluent but unsound (LLMs)
- The review process lacks a structured method for examining reasoning quality

### The Missing Layer in the 6-Layer Alignment Framework

The business-context alignment framework identifies six layers: problem alignment, authority alignment, trust alignment, validation alignment, policy and knowledge alignment, and commercial alignment.

Layer 4 (validation alignment) comes closest to reasoning verification. It asks: "Does the review architecture actually test the output?" Its main failure mode is "symbolic human oversight that fails because generation and validation happen inside the same interface or under the same framing pressure."

But even Layer 4 focuses on the architecture of review rather than the content of review. It asks whether the review structure is adequate. It does not specify what the reviewer should be examining. A firm could have strong validation alignment (separate review process, independent evidence checks, expert reviewers) and still fail to catch reasoning errors if the reviewers do not have a method for evaluating reasoning quality itself.

Reasoning verification is the operational content of validation alignment. It fills Layer 4 with the specific questions a reviewer should ask:

1. Are the sources real and relevant? (Source quality)
2. Does the conclusion follow from the premises? (Inferential validity)
3. Does the reasoning produce normatively acceptable outcomes? (Normative acceptability)
4. Does the expressed confidence match the reliability of the reasoning? (Confidence calibration)

### What This Means for the Synthesis

The incident reframing provides three things for the overall narrative:

1. **Empirical motivation.** The 16 reasoning acceptance failures (of 18 key incidents) demonstrate that the reasoning verification gap is not theoretical. It has already caused documented harm totaling hundreds of millions of dollars, regulatory sanctions, legal liability, and market value destruction.

2. **Framework extension logic.** The reframing shows precisely where the existing delegation framework needs to be extended. It does not need to be replaced. It needs a reasoning verification layer that operationalizes what the human in the loop should examine.

3. **Connection to the three-era narrative.** The incident inventory spans both the general AI era and the LLM era. The reframing shows that the underlying failure (unverified reasoning) is constant across both eras. What changes is the mechanism: opaque optimization in Era 1 and 2, fluent narration in Era 3. This supports the synthesis plan's argument that reasoning trust verification is the natural next step in the progression from interpretability (making reasoning visible) to fact-checking (verifying factual claims) to reasoning verification (evaluating whether the reasoning path itself is sound).

## Sources

This document draws on the incident data and analysis from the following project assets:

- `research/extensions/business-alignment/incidents/incident-inventory.md`
- `research/extensions/business-alignment/incidents/general-ai-vs-llm-incidents.md`
- `research/extensions/business-alignment/incidents/implications-and-immediate-company-needs.md`
- `research/extensions/business-alignment/alignment-framework.md`
- `research/extensions/alignment-literature-bridge.md`
- `research/extensions/interpretability-bridge.md`
- `research/core/taxonomy/scoring-sheet.md`
- `research/core/planning/narrative-synthesis-plan.md`
