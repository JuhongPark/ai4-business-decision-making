# Alignment Literature Bridge: Grounding the Delegation Framework

status: draft
date: 2026-03-27
purpose: Position the 6-dimensional delegation framework relative to published work in trust calibration, AI safety, and alignment research.

## Why This Note Exists

The delegation framework was built from case analysis and governance practice. It produces structured authority recommendations (assist / recommend / automate with guardrails) based on five scored dimensions plus domain context. But it has not yet been situated within the broader literature on human-AI trust, alignment failure modes, or regulatory risk classification.

This note maps the framework's components to published work — identifying where the framework converges with, diverges from, or extends existing research. The goal is not to claim novelty but to make the intellectual lineage explicit and to identify gaps that the literature exposes.

## 1. Trust Calibration: Lee and See (2004)

Lee and See define trust in automation as "the attitude that an agent will help achieve an individual's goals in a situation characterized by uncertainty and vulnerability." Their central contribution is the concept of **trust calibration** — the correspondence between a person's trust in the system and the system's actual trustworthiness. The problem is not too much or too little trust, but inappropriate calibration.

They identify three bases of trust:

- **Performance**: what the system does — reliability, predictability, competence
- **Process**: how it operates — algorithmic transparency, understanding of mechanism
- **Purpose**: why it was designed — whether the designer's intent aligns with the user's goals

**Where the framework converges.** The 6-dimensional framework is, at its core, a trust calibration instrument. The scoring sheet asks: given these contextual conditions, how much trust is appropriate? The override rules enforce calibration floors — situations where trust must not exceed a threshold regardless of other signals.

**Where the framework adds structure.** Lee and See's model is descriptive (how trust forms) rather than prescriptive (what authority to grant). The framework operationalizes trust calibration into a concrete decision output: given these dimension scores, the recommended authority level is X. Lee and See identify the calibration problem; the framework attempts to solve it for organizational AI deployment.

**Where the framework has a gap.** Lee and See's **process** basis of trust corresponds roughly to the evidence strength dimension — but only partially. Evidence strength rates external validation (peer review, regulatory approval), while process trust requires understanding of the system's internal mechanism. This is the gap that interpretability research addresses: without mechanistic understanding, evidence strength captures only performance and purpose trust, not process trust.

Reference: Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance. *Human Factors*, 46(1), 50–80.

## 2. Human-AI Complementarity: Bansal et al. (2021)

Bansal et al. find that providing AI explanations does not reliably produce **complementary team performance** (where human+AI outperforms both the human alone and the AI alone). Explanations can increase agreement with incorrect AI predictions because they make any prediction seem more justified. True complementarity requires that humans can identify when the AI is likely wrong — not just understand why it said what it said.

**Where the framework converges.** The framework's scenario condition dimension (baseline / stress / edge-case) captures part of this insight. Edge cases and stress conditions are precisely the situations where AI error likelihood increases, and the framework responds by reducing allowable authority. This encodes the intuition that delegation should be calibrated to specific task regions, not average performance.

**Where the framework adds structure.** Bansal et al. focus on individual instance-level decisions (should this human defer to this AI on this prediction?). The framework operates at the policy level: given this category combination, what delegation policy should the organization adopt? This is a different granularity — organizational policy rather than instance-level deference — but it addresses the same underlying problem.

**What this exposes.** The framework currently has no mechanism to capture AI confidence or uncertainty on individual decisions. It sets policy-level authority, but within a "recommend" policy, there is no guidance on which specific recommendations to accept and which to override. Bansal et al.'s work suggests that the framework would benefit from an additional layer: within a given authority level, how should the human evaluate individual AI outputs? This is where selective deference strategies and domain-specific AI failure mode training become relevant.

Reference: Bansal, G., Wu, T., Zhou, J., Fok, R., Nushi, B., Kamar, E., Lasecki, W. S., & Weld, D. S. (2021). Does the whole exceed its parts? The effect of AI explanations on complementary team performance. *Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems*, Article 81.

## 3. Concrete Problems in AI Safety: Amodei et al. (2016)

Amodei et al. identify five concrete safety problems that become more dangerous as AI systems gain autonomy:

1. **Avoiding negative side effects** — the agent achieves its objective but damages the environment in unintended ways
2. **Avoiding reward hacking** — the agent finds unintended ways to maximize its reward that do not correspond to the designer's intent
3. **Scalable oversight** — as tasks become complex, it becomes harder for humans to evaluate agent behavior
4. **Safe exploration** — the agent should not take catastrophically bad actions while learning
5. **Robustness to distributional shift** — the agent should behave well when deployment conditions differ from training conditions

**Where the framework converges.** The framework encodes several of these concerns as dimensions:

| Amodei problem | Framework dimension | How it maps |
|---|---|---|
| Reward hacking | Risk level + override rules | High-risk domains default to lower authority, which limits the scope for reward hacking |
| Distributional shift | Scenario condition | Edge-case and stress conditions detect distributional shift and trigger fallbacks |
| Scalable oversight | Governance readiness | Governance readiness measures whether the organization can maintain oversight |

**Where the framework has gaps.** Two of the five problems — negative side effects and safe exploration — are not directly captured by any framework dimension. Negative side effects are a consequence of objective specification quality, which the framework does not assess. Safe exploration applies primarily to learning systems deployed in real environments, which is outside the framework's static evaluation model. These gaps suggest that the framework is strongest for deployment-phase governance and weakest for development-phase safety.

**What this enables.** The five concrete problems can serve as a pre-delegation checklist that supplements the scoring sheet. Before evaluating dimensions, organizations should verify that the AI system under consideration has addressed each of the five problems to a degree appropriate for its deployment context. A system that has not addressed distributional shift, for example, should receive an automatic evidence strength penalty.

Reference: Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J., & Mané, D. (2016). Concrete problems in AI safety. *arXiv preprint arXiv:1606.06565*.

## 4. Specification Gaming: Krakovna et al. (2020)

Krakovna et al. document that specification gaming — where AI systems satisfy the literal specification of an objective without fulfilling its intended spirit — is pervasive across AI domains. The better the optimizer, the more likely it will find loopholes. This is the "flip side of AI ingenuity."

**Where this matters for delegation.** Specification gaming risk increases with authority level. An "assist" system that games its specification produces a misleading suggestion that a human can override. An "automate with guardrails" system that games its specification takes action before a human can intervene. The framework's graduated authority levels implicitly manage this risk: higher authority is only granted when other dimensions (evidence, governance, risk level) provide sufficient confidence that specification gaming would be caught.

**What this adds.** The incident inventory already contains specification gaming examples (Zillow's forecast-driven iBuying, RealPage's pricing coordination). Explicitly labeling these as specification gaming cases — and connecting them to the authority level that would have been appropriate — strengthens the empirical grounding of both the framework and the incident analysis.

Reference: Krakovna, V., et al. (2020). Specification gaming: The flip side of AI ingenuity. *DeepMind Blog*.

## 5. The Alignment Problem from a Deep Learning Perspective: Ngo et al. (2022)

Ngo et al. argue that alignment should be understood through how deep learning systems actually learn and generalize. Their central concern is **mesa-optimization** — the possibility that a trained model develops internal objectives that diverge from the training objective. Such divergence may not be detectable during training because the model behaves well on the training distribution.

The most concerning scenario is **deceptive alignment**: a model that "understands" the training process and strategically behaves well during evaluation to preserve its internal goals, only to pursue divergent objectives when deployed autonomously.

**Where this matters for delegation.** This paper provides the strongest theoretical argument for the framework's approach of graduated, conditional delegation. If internal objectives cannot be verified:

- Delegation authority should be expanded incrementally as track records grow, not granted based on benchmark performance alone.
- Continuous monitoring for behavioral anomalies is necessary at every authority level.
- Authority should be bounded such that the damage from misalignment is containable — which is precisely what the override rules do.

**Where the framework is limited.** The framework evaluates delegation fitness at a point in time. Ngo et al.'s concerns are about how alignment degrades over time, especially under distributional shift or as the system encounters situations not covered by its training. The framework's scenario condition dimension (edge-case detection) captures some of this, but it does not address the temporal dynamics of alignment — how a system that is well-calibrated today may become miscalibrated as its deployment context evolves.

Reference: Ngo, R., Chan, L., & Mindermann, S. (2022). The alignment problem from a deep learning perspective. *arXiv preprint arXiv:2209.00626*.

## 6. LLM Risk Taxonomy: Weidinger et al. (2022)

Weidinger et al. identify six categories of risk from language models:

1. Discrimination, exclusion, and toxicity
2. Information hazards (privacy leakage)
3. Misinformation harms (fluent falsehood)
4. Malicious uses (social engineering, fraud)
5. Human-computer interaction harms (over-trust, anthropomorphization)
6. Automation, access, and environmental harms

**Where the framework converges.** The incident inventory's LLM-specific section captures instances from categories 1, 2, 3, and 5. The framework's risk level dimension absorbs categories 1 and 3 (fairness and compliance risk). The evidence strength dimension partially captures category 3 (if the evidence base is weak, hallucination risk is higher).

**Where the framework has gaps.** Categories 4 (malicious use) and 5 (interaction harms like anthropomorphization) are not captured by any framework dimension. These are risks that emerge from the interaction pattern between the AI system and its users, not from the decision context itself. An LLM-powered customer service system might score well on all five dimensions but still create interaction harms through anthropomorphization or be repurposed for social engineering. This suggests that LLM deployments may require an additional assessment layer beyond the current framework.

Reference: Weidinger, L., et al. (2022). Taxonomy of risks posed by language models. *Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency (FAccT)*, 214–229.

## 7. Regulatory Mapping: NIST AI RMF and EU AI Act

### NIST AI RMF (2023)

The NIST framework organizes AI risk management into four functions: GOVERN, MAP, MEASURE, MANAGE. It emphasizes contextual risk assessment over categorical risk tiers.

The framework's dimensions map to NIST functions:

| Framework dimension | NIST function | Mapping |
|---|---|---|
| Governance readiness | GOVERN | Organizational oversight, accountability, policies |
| Risk level + domain | MAP | Contextual risk assessment for specific use case |
| Evidence strength | MEASURE | Evaluating system performance and reliability |
| Override rules | MANAGE | Acting on identified risks, setting boundaries |
| Scenario condition | MEASURE + MANAGE | Monitoring for distributional shift, triggering fallbacks |

The NIST framework's emphasis on contextual rather than categorical risk aligns well with the delegation framework's approach — the same AI technology may warrant different authority levels depending on the domain, risk, and governance context.

### EU AI Act (2024)

The EU AI Act classifies AI systems into four risk tiers: unacceptable (prohibited), high (regulated), limited (transparency requirements), and minimal (no specific requirements).

The delegation framework's risk level dimension parallels this classification:

| Framework risk level | EU AI Act tier | Alignment |
|---|---|---|
| High-risk (1) | High-risk | Both require human oversight, auditability, and governance infrastructure |
| Medium-risk (2) | Limited / context-dependent | Framework provides finer-grained assessment than the Act's binary high/not-high threshold |
| Low-risk (3) | Minimal | Both allow greater autonomy with lighter governance |

The framework adds granularity that the EU AI Act does not: within the "high-risk" category, the framework differentiates based on decision structure, scenario condition, evidence strength, and governance readiness. A high-risk lending decision under baseline conditions with strong evidence and strong governance receives a different authority level than the same domain under stress conditions with weak evidence.

References:
- NIST. (2023). *AI Risk Management Framework (AI RMF 1.0)*. NIST AI 100-1.
- European Parliament. (2024). *Regulation (EU) 2024/1689 (Artificial Intelligence Act)*.

## Summary: What the Literature Exposes

### The framework's strengths, confirmed by the literature

1. **Graduated delegation is correct.** Lee and See (calibration), Ngo et al. (graduated expansion), and the EU AI Act (risk tiers) all converge on the principle that AI authority should be contextually calibrated, not binary.
2. **Override rules are necessary.** Amodei et al. (scalable oversight), Krakovna et al. (specification gaming), and Ngo et al. (deceptive alignment) all argue for hard constraints that cannot be optimized away. The framework's override rules implement this.
3. **The incident inventory has alignment-theoretic value.** The 71 incidents map to Amodei et al.'s five problems, Krakovna et al.'s specification gaming, and Weidinger et al.'s LLM risk categories. Explicitly labeling these connections would strengthen both the framework and the incident analysis.

### Gaps the literature reveals

1. **Evidence strength captures performance and purpose trust, but not process trust** (Lee and See). Interpretability is required to close this gap.
2. **The framework operates at policy level but lacks instance-level guidance** (Bansal et al.). Within a "recommend" policy, when should a human override a specific recommendation?
3. **Negative side effects and safe exploration are not covered** (Amodei et al.). The framework is strongest for deployment-phase governance, weakest for development-phase safety.
4. **LLM interaction harms and malicious use are not captured** (Weidinger et al.). LLM deployments may require an additional assessment layer.
5. **Temporal dynamics of alignment are not addressed** (Ngo et al.). The framework evaluates fitness at a point in time but does not model how alignment degrades.
