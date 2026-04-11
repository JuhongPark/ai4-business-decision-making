# Empirical Simulation Plan: 6-Layer Pre-Participant Validation

status: active
date_created: 2026-04-11
purpose: design a rigorous empirical simulation program that validates the delegation framework, verification suite, and automation boundary tool before recruiting human participants — using methods with documented epistemic warrant

## Current Limitation

The existing prototypes demonstrate that the tools *function* but not that they *work*. Specifically:

| What we know | What we don't know |
| --- | --- |
| Scoring logic is internally consistent | Whether the scoring dimensions are the right ones |
| Retrospective validation is 100% (20 cases) | Whether prospective accuracy holds on unseen cases |
| Prospective validation is 90-100% (10 cases) | Whether this holds at scale beyond researcher-selected cases |
| Sycophancy compounding was demonstrated | Whether the measurements reflect real pipeline behavior or researcher expectations |
| 12 study stimuli exist | Whether practitioners can actually use the tools to detect failures |

The gap is between *tool correctness* and *tool usefulness*. This plan bridges that gap through 6 layers of increasingly rigorous validation.

## The 6-Layer Validation Architecture

```
Layer 1: Formal Verification (strongest epistemic warrant)
  ↓
Layer 2: Sensitivity Analysis
  ↓
Layer 3: Adversarial Stress-Testing
  ↓
Layer 4: Multi-Model Cross-Validation
  ↓
Layer 5: Cognitive Walkthrough + Heuristic Evaluation
  ↓
Layer 6: LLM-Simulated Participant Study (weakest, hypothesis-generating)
```

Each layer addresses a different validity question and produces different evidence types. The layers are ordered from strongest epistemic warrant to weakest.

---

## Layer 1: Formal Verification — Complete Enumeration

### What It Proves
Internal consistency: no configuration of scores produces an authority level that contradicts the framework's design intent.

### Method
The delegation framework has 6 dimensions × 3 levels = 3^6 = 729 base combinations. With 3 binary override rules and the automation boundary tool (another 3^6 = 729 combinations), the total enumerable space is manageable.

**Procedure**:
1. Enumerate all 729 delegation scoring configurations
2. For each, compute: raw score, authority band, triggered overrides, final authority
3. Verify: no configuration violates the framework's axioms:
   - High risk (3) + weak governance (1) always caps at ASSIST
   - Edge-case scenario (3) always caps at ASSIST
   - Weak evidence (1) + high risk (≥2) always reduces one level
   - Monotonicity: adding 1 to any dimension score never *decreases* the final authority level (unless an override triggers)
4. Repeat for all 729 automation boundary configurations
5. Cross-validate: for configurations scoreable on both tools, check directional consistency

**Output**: Complete verification report — pass/fail for each axiom, list of any violations, and the full distribution of authority bands across the score space.

**Epistemic status**: Deductive proof. If the enumeration passes, internal consistency is guaranteed. No approximation.

### Implementation
```python
# Enumerate all 3^6 = 729 combinations
for d in range(1,4):
  for s in range(1,4):
    for r in range(1,4):
      for sc in range(1,4):
        for e in range(1,4):
          for g in range(1,4):
            result = score_delegation({...})
            verify_axioms(result)
```

---

## Layer 2: Sensitivity Analysis — Which Dimensions Matter Most

### What It Proves
Which scoring dimensions have the most influence on the final authority level, and where the boundary effects are sharpest.

### Method

**2A: One-at-a-time (OAT) sensitivity**
- Hold 5 dimensions constant at their median value (2)
- Vary the 6th dimension from 1 to 3
- Record the change in final authority
- Repeat for each dimension
- Rank dimensions by their influence on the output

**2B: Probabilistic sensitivity (Monte Carlo)**
- Sample 10,000 random configurations from uniform (1,2,3) distributions
- For each, compute the final authority
- Compute the Spearman rank correlation between each dimension and the final authority
- The highest-correlation dimensions are the most influential

**2C: Boundary analysis**
- For each pair of adjacent authority bands (ASSIST ↔ RECOMMEND, RECOMMEND ↔ AUTOMATE), identify all configurations that sit exactly on the boundary (e.g., total score = 8 or 9)
- For each boundary configuration, identify which single-dimension change would flip the authority band
- Count flip frequency per dimension — the most "flippable" dimensions are where the framework is most sensitive to scoring judgment

**Output**: Dimension influence ranking, boundary sensitivity map, and identification of "swing dimensions" — the dimensions where a ±1 scoring difference changes the authority level most often.

**Why this matters**: If the framework is dominated by 1-2 dimensions, it is effectively a simpler tool than it appears. If all dimensions contribute meaningfully, the 6-dimensional structure is justified.

---

## Layer 3: Adversarial Stress-Testing — Finding Where the Framework Breaks

### What It Proves
The framework's failure modes: edge cases where it produces recommendations that a reasonable expert would reject.

### Method

**3A: Boundary case construction (manual)**
Construct 20 scenarios designed to sit on decision boundaries:
- 5 cases at the ASSIST/RECOMMEND boundary (total score 8-9)
- 5 cases at the RECOMMEND/AUTOMATE boundary (total score 11-12)
- 5 cases where override rules conflict with raw scores
- 5 cases where the delegation tool and boundary tool disagree

For each, the researcher independently judges the "correct" authority level and compares with the framework's output.

**3B: LLM-generated adversarial scenarios**
Prompt 3 different LLMs: "Generate a business AI deployment scenario that would be especially difficult for a delegation scoring framework to classify. The scenario should be one where reasonable experts would disagree on the appropriate authority level."

Collect 10 scenarios per LLM (30 total). Score each using the framework. Identify scenarios where the framework's recommendation seems counterintuitive.

**3C: Gaming analysis**
Construct scenarios where a motivated user tries to "game" the framework to achieve a desired authority level:
- User wants AUTOMATE but situation warrants ASSIST: which dimensions can be plausibly inflated?
- User wants ASSIST (to avoid accountability) but situation warrants RECOMMEND: which dimensions can be plausibly deflated?

Identify the framework's most gameable dimensions and propose countermeasures (e.g., requiring independent scoring by a governance reviewer).

**Output**: Adversarial scenario catalog, identified failure modes, gaming vulnerability report, and proposed framework refinements.

---

## Layer 4: Multi-Model Cross-Validation — Scoring Agreement Across LLMs

### What It Proves
Whether the framework's scoring criteria are clear enough that different AI systems apply them consistently.

### Method

Select 30 test scenarios (20 from existing case library + 10 from adversarial stress-testing).

For each scenario, prompt 4 LLMs (Claude, GPT-4, Gemini, Llama-3) with:
```
Given this AI deployment scenario, score each dimension of the
delegation framework from 1-3 using the provided rubric.
[Scenario description]
[Complete rubric for each dimension]
Provide your scores with brief justification for each.
```

**Measurements**:
- Per-dimension Fleiss' Kappa (4 raters × 30 scenarios × 6 dimensions)
- Per-scenario authority band agreement (do all 4 models assign the same band?)
- Overall framework reliability (average Kappa across all dimensions)

**Interpretation thresholds** (Landis & Koch, 1977):
- Kappa > 0.8: Almost perfect agreement → scoring criteria are clear
- Kappa 0.6-0.8: Substantial agreement → criteria are adequate with minor ambiguity
- Kappa 0.4-0.6: Moderate agreement → criteria need refinement
- Kappa < 0.4: Fair/poor → criteria are too ambiguous for reliable application

**Expected results**: High agreement (>0.7) on structured dimensions (decision structure, risk level) and lower agreement (0.4-0.6) on judgment-intensive dimensions (evidence strength, governance readiness).

**Output**: Reliability report with per-dimension Kappa values, identified dimensions needing criteria clarification, and a revised rubric where Kappa < 0.6.

---

## Layer 5: Cognitive Walkthrough + Heuristic Evaluation — Usability Inspection

### What It Proves
Whether a business practitioner can follow the framework's procedures and reach a defensible conclusion.

### Method

**5A: Cognitive walkthrough of the verification suite**
Select 4 AI-generated outputs (2 flawed, 2 sound from the P5 stimuli). For each, walk through the complete verification protocol step by step:

At each step, record:
1. Would a product manager know what to do here?
2. Would they understand the criterion?
3. Would they reach the correct conclusion?
4. How long would this step take?

Document every point of ambiguity, confusion, or excessive cognitive load.

**5B: Heuristic evaluation of the scoring sheet**
Recruit 3-5 colleagues (not AI governance specialists) to independently score the same 5 scenarios using the delegation scoring sheet.

Measure:
- Inter-rater reliability (Fleiss' Kappa across human raters)
- Time to complete scoring (per scenario)
- Points of confusion (free-text feedback)

Compare human inter-rater reliability with the multi-model reliability from Layer 4. If humans agree less than LLMs, the scoring criteria are too ambiguous for practical use.

**5C: Self-Wizard-of-Oz test**
Have one colleague (unfamiliar with the framework) use the complete workflow system on a real AI output they encounter in their work. Observe without helping. Record:
- Task completion success/failure
- Time to completion
- Points where they deviate from the intended protocol
- Their final assessment vs. the researcher's assessment

**Output**: Usability report with categorized issues (critical, major, minor), estimated time-to-complete for real-world use, and specific wording changes for ambiguous criteria.

---

## Layer 6: LLM-Simulated Participant Study — Hypothesis Generation

### What It Proves
Nothing definitively — but generates testable hypotheses about how different practitioner profiles might respond to the framework.

### Validity Framing
Per Lin (2025): LLM-simulated participants are "pragmatic simulation tools for rapid hypothesis testing and computational modeling," not replacements for human participants. Results are explicitly positioned as hypothesis-generating.

Per PNAS (2025): LLM surrogates produce systematically biased results and should not be treated as equivalent to human data.

### Method

**Persona construction**: Create 30 practitioner personas based on realistic profiles:
- 10 product managers (varying experience: 2-15 years)
- 10 marketing directors (varying industry: tech, healthcare, finance, retail, manufacturing)
- 10 business analysts (varying AI familiarity: low, medium, high)

Each persona includes: role, years of experience, industry, AI tool usage frequency, decision-making authority level, and educational background.

**Task**: Each persona evaluates 6 AI-generated market research outputs (3 flawed, 3 sound) under 3 conditions:
- Condition A: Unassisted (persona + output only)
- Condition B: With verification suite report
- Condition C: With full workflow system guidance

For each evaluation, the persona responds to:
1. "Does this analysis contain significant reasoning problems?" (Yes/No)
2. "What specific problems did you identify?" (free text)
3. "Would you act on this analysis?" (Yes/No/Need more info)
4. "How confident are you?" (1-7)

**Implementation**: Run with 3 LLMs (Claude, GPT-4, Gemini) to measure inter-model agreement on simulated responses.

**Analysis**:
- Simulated detection rate by condition (expecting A < B < C)
- Simulated detection rate by persona type (expecting experienced > junior)
- Inter-model agreement on simulated responses (Fleiss' Kappa)
- Comparison of simulated detection patterns with predictions from the practitioner study design

**Critical limitation**: These are NOT human responses. They are computational simulations of what the model predicts humans might say. The primary value is:
- Identifying which experimental conditions produce ceiling/floor effects (if simulated participants score 100% in Condition C, the stimuli may be too easy)
- Piloting the experimental protocol (does the task make sense? are the response options adequate?)
- Generating hypotheses about which persona characteristics predict detection accuracy

**Output**: Simulated response dataset, preliminary effect size estimates (to be confirmed with real participants), identified ceiling/floor effects, and protocol refinements.

---

## Statistical Methods Across All Layers

### For Quantitative Layers (1, 2, 4, 6)

**Bootstrap confidence intervals (BCa method)**
- For detection rates, agreement coefficients, and effect size estimates
- 10,000 resamples with bias-corrected acceleration
- Report 95% CI alongside point estimates

**Permutation tests**
- For cross-condition comparisons (A vs B vs C)
- No distributional assumptions; exact for any sample size
- 10,000 random permutations for Monte Carlo approximation

**Bayesian updating with incident priors**
- Use the 71-incident retrospective analysis as prior distribution for failure type frequencies
- Update with prospective validation data as it accumulates
- Allows small prospective samples to be interpreted in context of the larger evidence base

### For Qualitative Layers (3, 5)

**Structured coding**
- All adversarial scenarios and walkthrough notes coded using the 25-type reasoning failure taxonomy
- Inter-rater reliability for coding assessed using Cohen's Kappa

---

## Execution Timeline

| Layer | Effort | Dependencies | Priority |
| --- | --- | --- | --- |
| 1: Formal verification | 1 day (code + enumerate) | P1 scoring engine (done) | Immediate |
| 2: Sensitivity analysis | 2 days (code + analyze) | Layer 1 | Immediate |
| 3: Adversarial testing | 1 week (scenario construction + analysis) | Layers 1-2 | High |
| 4: Multi-model cross-validation | 1 week (API calls + coding) | LLM API access | High |
| 5: Cognitive walkthrough | 3-5 days (inspection + colleague sessions) | P4 workflow system (done) | Medium |
| 6: Simulated participant study | 1-2 weeks (persona design + runs + analysis) | All above layers, LLM API access | After layers 1-5 |

**Total pre-participant timeline**: 4-6 weeks

---

## What This Produces

At the end of 6 layers, you will have:

1. **Internal consistency proof** (Layer 1): The framework provably never produces contradictory recommendations
2. **Sensitivity map** (Layer 2): Which dimensions matter most, where boundaries are sharpest
3. **Known failure modes** (Layer 3): Edge cases where the framework struggles, with proposed fixes
4. **Reliability coefficients** (Layer 4): Per-dimension Kappa values showing which criteria are clear vs ambiguous
5. **Usability assessment** (Layer 5): Time-to-complete, confusion points, specific wording fixes
6. **Preliminary effect sizes** (Layer 6): Simulated detection rate improvements to power the real participant study

This evidence package is sufficient for:
- A methodology paper ("How to validate AI governance frameworks before deployment")
- Submission to FAccT or AIES as a framework validation study
- IRB application for the real participant study (demonstrating due diligence in pre-testing)
- Investor/stakeholder confidence that the tools have been rigorously tested

---

## Connection to Publication Strategy

| Layer | Publication Target | Contribution |
| --- | --- | --- |
| 1-2 | Methods section of framework paper | Formal verification + sensitivity analysis |
| 3 | Standalone adversarial validation paper | Novel: adversarial testing of governance frameworks |
| 4 | Inter-model reliability study | Novel: multi-model agreement as framework quality metric |
| 5-6 | Pre-study validation section of practitioner paper | Methodological rigor in study design |
| All | FAccT 2026 or AIES 2026 | Complete 6-layer validation methodology |
