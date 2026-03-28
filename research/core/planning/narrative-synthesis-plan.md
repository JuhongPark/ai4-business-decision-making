# Plan: Narrative Synthesis of the Research

date: 2026-03-28
purpose: Reorganize the entire body of research into a single coherent narrative arc driven by the researcher's field experience.

## The Narrative Arc

The research tells one story across three eras. Each era deepens the same question: how do humans verify what AI tells them?

```
Era 1: Interpretability Era
  "AI was right, but people wouldn't use it because they couldn't see why."
  → Solution: show the evidence (SHAP, feature attribution)
  → Result: verification loop closed — human expert evaluates visible evidence

Era 2: LLM Fact-Checking Era
  "AI became fluent, and people stopped questioning it."
  → Problem: facts can be wrong (hallucination)
  → Partial solution: fact-checking is hard but tractable
  → Field observation: even fact-checking is too hard for most companies

Era 3: Reasoning Trust Era (current)
  "Even when facts are correct, the reasoning connecting them may not be."
  → Problem: reasoning verification has no method
  → Observation: people accept AI reasoning without scrutiny
  → BCG contrast: consulting trained rigorous reasoning scrutiny; no equivalent exists for AI
  → Research goal: build the verification framework
```

This arc is not invented after the fact. It tracks the researcher's actual professional trajectory from medical AI interpretability work through LLM business deployment to the current research question.

## How Existing Research Maps to the Narrative

### Act 1: The Trust Problem (Why This Matters)

This act establishes that AI trust is not a soft concern but an operational risk with documented consequences.

| Existing Asset | Role in Narrative | Status |
|---|---|---|
| Incident inventory (71 cases) | Empirical proof that miscalibrated trust causes real harm ($304M Zillow, $100B+ Google, Rite Aid ban, legal sanctions) | Complete. Reframe as evidence of what happens when reasoning goes unchecked. |
| General AI vs LLM incidents | Shows the shift: general AI failures were about wrong objectives; LLM failures are about fluent-but-wrong reasoning accepted without scrutiny | Complete. Highlight the contrast as evidence of the era shift. |
| Alignment failure mapping | 12/20 incidents preventable, but the 8 partial/missed cases are mostly LLM reasoning failures — the gap the new direction addresses | Complete. Use the 8 gap cases as motivation for reasoning verification. |
| Implications and immediate company needs | "Authority can increase without formal delegation" — AI shapes framing, generates rationale, silently shifts decision power | Complete. This is the field observation that drives the narrative. |

**What needs to be written for Act 1:**
- A framing introduction that connects the three eras through the researcher's experience
- Recontextualization of incidents specifically through the reasoning trust lens (not just governance failures, but reasoning acceptance failures)

### Act 2: The Framework Foundation (What We Built)

This act presents the existing delegation calibration framework as the governance answer to "when should AI have authority" — while showing that it implicitly depends on a verification capability that does not yet exist.

| Existing Asset | Role in Narrative | Status |
|---|---|---|
| 6-dimensional taxonomy | The structured answer to "when should firms use AI" | Complete. Present as the governance layer. |
| Scoring sheet + decision tree | Operational tools that quantify delegation fitness | Complete. Present as the instrument. |
| Evaluation framework (7 dimensions) | The conceptual foundation with restriction defaults | Complete. Present as the theoretical backbone. |
| Cross-domain analysis (8 domains) | Shows that automation readiness varies by domain structure, not enthusiasm | Complete. Use selectively — strategy and market research findings are most relevant (reasoning failures in unstructured domains). |
| Cross-scenario synthesis | AI autonomy should be scenario-sensitive, not domain-static. Edge cases reverse the autonomy logic. | Complete. Critical finding: stress conditions magnify the cost of hidden model failure — exactly when people lean on AI most. |
| Scenario research design | The experimental backbone | Complete. Reference for methodology. |

**What needs to be written for Act 2:**
- A narrative bridge showing that the framework works as governance but has a structural assumption: the human in the loop can actually evaluate what AI tells them
- Explicit identification of where the framework depends on verification capability it does not provide

### Act 3: The Alignment Depth (Why This Is Not Just Governance)

This act shows that the trust problem connects to deeper alignment questions — delegation calibration is an alignment problem, and interpretability is the technical path to lifting the evidence ceiling.

| Existing Asset | Role in Narrative | Status |
|---|---|---|
| Delegation as alignment | Core argument: even a technically aligned model can cause harm at the wrong authority level | Complete. Present as the conceptual deepening. |
| Interpretability bridge | SHAP-era solution (feature attribution) vs. what LLMs need (process trust). Post-hoc explanations are insufficient. | Complete. This is the direct bridge from Era 1 to Era 3 — the same researcher who used SHAP to solve trust now recognizes that SHAP-style solutions do not work for LLM reasoning. |
| Alignment literature bridge | Maps the framework to 7 published sources. Confirms strengths, identifies 5 gaps. | Complete. Use Gap #1 (no process trust) and Gap #5 (instance-level output verification) as the pivot to reasoning trust. |
| Business-context alignment framework (6 layers) | Layer 4 (validation alignment) is the key: symbolic review fails when generation and validation happen in the same interface | Complete. The "rubber stamp" problem is the organizational mechanism of blind trust. |
| Final synthesis | Business-context alignment as the integrating concept | Complete. Provides the wrapper. |

**What needs to be written for Act 3:**
- A narrative that traces the personal arc: "I used SHAP to solve the Era 1 trust problem. I now see that the same approach cannot solve the Era 3 problem. Here is why."
- Connection between the interpretability bridge's finding (post-hoc explanations ≠ process trust) and the field observation (companies accept AI reasoning without scrutiny because they have no method to scrutinize it)

### Act 4: The Information Structure Insight (Why This Is Getting Worse)

This act explains why the problem accelerates: each information shock lowers costs but raises new scarcities, and the AI shock made trust calibration the scarce resource.

| Existing Asset | Role in Narrative | Status |
|---|---|---|
| Information structure analysis | Five information shocks. Each made information cheaper and verification harder. AI made interpretation cheap but trust calibration scarce. | Complete. This is the structural explanation for why blind trust is the natural outcome. |
| LLM decision paradigm | LLMs excel at pre-optimization structuring, not autonomous judgment. Unscaffolded LLM reasoning degrades with complexity. | Complete. Explains why the "just use AI" approach fails for complex decisions. |
| Capability ladder | Seven-level stack. Replacement is level-dependent. Upper levels (judgment, legitimacy, accountability) resist automation for institutional reasons. | Complete. Provides the theoretical limit: some decision capabilities cannot be delegated regardless of model quality. |
| Consulting firm narratives | Consulting persisted through every information shock by providing what free information cannot: problem framing, signal filtering, legitimacy | Complete. Direct parallel to the BCG experience — the skills that survive are verification and judgment skills. |

**What needs to be written for Act 4:**
- A narrative connecting the information structure analysis to the personal observation: "I saw companies that could not even fact-check, let alone verify reasoning. The information structure analysis explains why — each wave made information cheaper but verification harder, and AI made it hardest of all."
- The capability ladder reframed: the levels where AI is weakest (judgment, legitimacy) are exactly the levels where reasoning verification matters most

### Act 5: The Research Direction (What Must Be Built)

This act presents the reasoning trust verification framework as the missing layer — the thing that makes everything else work.

| Existing Asset | Role in Narrative | Status |
|---|---|---|
| Research direction statement | The narrative-driven articulation of the problem and the goal | Complete (just written). |
| Literature landscape survey | Confirms the gap exists in published research | Complete (just written). |
| Research direction review | Shows how the new direction connects to and extends existing work | Complete (just written). |

**What needs to be written for Act 5:**
- Framework design specification: what does a reasoning verification framework actually look like? What are its components, how is it applied, what does it produce?
- Reasoning failure taxonomy: classification of reasoning failure types observed in business contexts (beyond the four types already listed in the direction statement)
- Source quality assessment method: the BCG-trained instinct formalized — how to evaluate whether the sources behind AI reasoning meet professional standards
- Inferential validity assessment method: structured approach to checking whether conclusions follow from premises
- Normative acceptability assessment method: how to detect when AI reasoning violates domain-specific professional standards
- Connection to the existing scoring sheet: how reasoning verification integrates as a new component of evidence strength
- Pilot case design: testing the framework against the existing incident inventory and against new LLM-generated business analyses

## Synthesis Document Structure

The final synthesis should be a single document that tells the complete story:

```
1. Three Eras of AI Trust
   1.1 Era 1: The Interpretability Solution (SHAP, medical AI, visible evidence)
   1.2 Era 2: The LLM Disruption (fluency, fact-checking, the BCG example)
   1.3 Era 3: The Reasoning Gap (what facts cannot tell you)

2. What We Know: The Delegation Framework
   2.1 The 6-dimensional taxonomy
   2.2 The scoring instrument and override rules
   2.3 71 incidents and what they show
   2.4 The structural assumption: humans can evaluate what AI tells them

3. Why It Goes Deeper: Delegation as Alignment
   3.1 From governance to alignment
   3.2 The interpretability path (and its limits for LLM reasoning)
   3.3 The five gaps in the alignment literature bridge
   3.4 The rubber stamp problem (validation alignment failure)

4. Why It Gets Worse: Information Structure and Decision Capability
   4.1 Five information shocks and the scarcity shift
   4.2 Where LLMs actually help (and where they do not)
   4.3 The capability ladder and its ceiling
   4.4 Why consulting-grade verification matters more than ever

5. What Must Be Built: Reasoning Trust Verification
   5.1 The three questions (fact, reasoning, meta-verification)
   5.2 What exists in the literature (and what does not)
   5.3 The framework specification
   5.4 Reasoning failure taxonomy for business contexts
   5.5 Source quality, inferential validity, normative acceptability
   5.6 Integration with the delegation scoring system
   5.7 Pilot validation design

6. The Conviction
   6.1 Not blind trust, not rejection — informed trust through verifiable reasoning
   6.2 How this enables better AI adoption and protects organizations
```

## Execution Sequence

### Phase 1: Reframing (recontextualize existing assets)

Write the narrative bridges that connect existing research to the new story. No new research needed — this is about reframing what exists.

- [ ] 1.1 Write the three-era framing introduction with personal narrative
- [ ] 1.2 Reframe the incident inventory through the reasoning trust lens
- [ ] 1.3 Write the "structural assumption" section showing where the framework depends on verification it does not provide
- [ ] 1.4 Write the SHAP-to-LLM personal arc bridging Era 1 interpretability to Era 3 reasoning trust
- [ ] 1.5 Connect information structure analysis to the field observation of companies unable to verify

### Phase 2: New Research (the reasoning verification framework itself)

This is the genuinely new contribution. Requires design work.

- [ ] 2.1 Develop the reasoning failure taxonomy for business contexts
- [ ] 2.2 Design the source quality assessment method (formalizing the BCG instinct)
- [ ] 2.3 Design the inferential validity assessment method
- [ ] 2.4 Design the normative acceptability assessment method
- [ ] 2.5 Design the confidence calibration assessment method
- [ ] 2.6 Integrate reasoning verification into the existing scoring sheet as a new evidence strength component
- [ ] 2.7 Design the pilot validation protocol (test against incidents + live LLM outputs)

### Phase 3: Synthesis (write the unified document)

Assemble everything into the structure outlined above.

- [ ] 3.1 Draft the synthesis document following the six-part structure
- [ ] 3.2 Ensure all existing assets are referenced and connected, not duplicated
- [ ] 3.3 Validate that the narrative flows from personal experience through existing research to new contribution
- [ ] 3.4 Review for internal consistency with the delegation framework, taxonomy, and alignment extensions

## What This Plan Does NOT Propose

- **No restructuring of existing files.** The existing research assets are complete and valid. This plan references them, it does not reorganize them.
- **No discarding of previous work.** Every major existing document has a role in the narrative. The delegation framework, taxonomy, incidents, alignment extensions, and information structure analysis all contribute.
- **No change to the core framework.** The 6-dimensional taxonomy and scoring system remain. Reasoning verification extends them; it does not replace them.
