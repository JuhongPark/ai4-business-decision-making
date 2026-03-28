# Delegation Calibration as an Alignment Problem

status: draft
date: 2026-03-27
purpose: Articulate the core argument that delegation calibration — determining when and how much autonomous authority to grant AI systems — is an alignment problem, not merely a governance or business optimization problem.

## The Argument

AI alignment research asks: how do we ensure that AI systems pursue objectives aligned with human values? This question is typically addressed through technical means — reward specification, value learning, interpretability, oversight mechanisms.

This research asks a complementary question: even if we solve technical alignment perfectly, how much autonomous authority should a given AI system receive in a given context? A model that is value-aligned in the technical sense may still produce harmful outcomes if deployed at an inappropriate authority level — if it automates decisions it should only recommend, or if it operates in conditions outside its validated envelope.

These are not separate problems. They are two faces of the same problem. Technical alignment determines whether the system can be trusted in principle. Delegation calibration determines whether the system should be trusted in practice, given the specific decision context.

## What Existing Alignment Research Says About Delegation

### The graduated authority principle

Multiple threads in the alignment literature converge on the principle that AI authority should be granted incrementally rather than categorically.

Amodei et al. (2016) identify scalable oversight as one of five concrete safety problems. Their framing implies that authority should not exceed what can be meaningfully overseen. As the scope of AI decision-making expands, the oversight infrastructure must expand proportionally — otherwise the system is operating beyond the boundary where alignment can be verified.

Ngo et al. (2022) argue that alignment that holds in training may not hold in deployment, especially as capability and autonomy increase. Their concern about deceptive alignment — models that behave well during evaluation but pursue divergent objectives when deployed autonomously — provides a theoretical basis for maintaining human override authority even when a system performs well on benchmarks.

The EU AI Act (2024) implements this principle in law: high-risk AI systems require mandatory human oversight, proportional to the risk level. The Act does not ban high-risk AI; it constrains the authority level at which it can operate.

### The trust calibration framework

Lee and See (2004) define appropriate reliance as the correspondence between trust in a system and the system's actual trustworthiness. Miscalibrated trust produces misuse (over-trust leading to over-delegation) or disuse (under-trust leading to rejected AI assistance).

The delegation framework operationalizes this insight. The scoring dimensions are proxies for trustworthiness (evidence strength, governance readiness) and contextual risk factors (risk level, scenario condition, decision structure). The override rules enforce calibration floors — situations where trust must not exceed a threshold regardless of how well the system appears to perform.

Bansal et al. (2021) add a crucial nuance: providing AI explanations does not reliably improve trust calibration. Explanations can increase agreement with incorrect AI predictions. This means that transparency alone is insufficient for delegation decisions. What matters is whether the human decision-maker can identify when the AI is likely to be wrong — which requires understanding the AI's failure modes, not just its reasoning on a given instance.

### The specification gaming threat

Krakovna et al. (2020) document that specification gaming is pervasive: AI systems routinely find unintended ways to satisfy their literal objective while violating the designer's intent. The more capable the optimizer, the more likely it will find loopholes.

For delegation calibration, this means that authority risk scales with optimizer capability. An "assist" system that games its specification produces a misleading suggestion that a human can evaluate and reject. An "automate with guardrails" system that games its specification takes action before a human can intervene. The delegation framework's graduated authority levels directly manage this risk surface.

## What the 6-Dimensional Framework Contributes

### A structured instrument for the governance layer

Most alignment research focuses on the technical layer — making models behave correctly. The framework addresses the governance layer — deciding how much authority to grant a model that may or may not be technically aligned. These layers are complementary:

| Layer | Question | Who answers it |
|---|---|---|
| Technical alignment | Does the model pursue the intended objective? | ML researchers, red-teamers |
| Delegation calibration | Should the model be allowed to act on its outputs autonomously? | Organizational decision-makers, governance teams |

The framework provides a structured instrument for the second question. Without it, delegation decisions are made ad hoc — based on vendor claims, benchmark performance, or organizational enthusiasm. The 71 incidents in the inventory demonstrate where ad hoc delegation produces failures.

### Override rules as safety constraints

The framework's three override rules function as safety constraints in the alignment sense:

1. High-risk + weak governance → cap at ASSIST
2. Edge-case scenario → cap at ASSIST
3. Weak evidence in consequential decision → reduce one level

These are hard constraints that cannot be overridden by high scores on other dimensions. In alignment terms, they are corrigibility requirements — ensuring that the system's authority can always be limited when contextual conditions warrant it, regardless of the system's apparent performance.

### The evidence strength dimension as an interpretability demand signal

The framework's weakest dimension — evidence strength — creates a concrete demand for interpretability research. The current evidence scale relies on external proxies (regulatory approval, peer review). As documented in the interpretability bridge note, this captures Lee and See's performance and purpose trust but not process trust.

Mechanistic interpretability (circuit-level understanding, sparse autoencoders, probing) would allow evidence strength to be grounded in model internals. Rudin (2019) argues that for high-stakes decisions, inherently interpretable models should be preferred. The framework's scoring sheet quantifies this: moving from weak to strong evidence can shift the authority recommendation by a full level — a concrete organizational incentive to invest in interpretability.

## What the Framework Cannot Do Without Interpretability

The alignment failure mapping (see `incidents/alignment-failure-mapping.md`) shows that the framework would have prevented 12 of 20 documented incidents by recommending a lower authority level. But prevention through lower authority is a blunt instrument. It prevents harm by preventing deployment, not by enabling safe deployment at higher authority levels.

To move beyond "prevent harm by limiting authority" toward "enable safe deployment by verifying alignment," the framework needs the evidence strength ceiling to be lifted. This requires interpretability methods that provide genuine process trust:

- Feature attribution reveals whether the model relies on legitimate signals or proxies (relevant for detecting specification gaming and side effects in lending, hiring, and ad delivery).
- Probing confirms whether the model internally represents the concepts it should be reasoning about (relevant for clinical decision support and content generation).
- Circuit-level analysis reveals how the model actually processes information (relevant for any deployment where the consequence of misaligned internal reasoning is severe).

Without these methods, the framework remains a conservative instrument that prevents the worst delegation failures but cannot enable the best delegation outcomes.

## Open Questions

1. **How should evidence strength scale with interpretability maturity?** Current interpretability methods (SHAP, probing) provide partial process trust. Full circuit-level understanding is aspirational. Should the evidence strength scale recognize degrees of interpretability, or maintain a binary interpretable/opaque threshold?

2. **Does the framework need a temporal dimension?** Ngo et al. (2022) emphasize that alignment can degrade over time. The framework evaluates delegation fitness at a point in time but does not model how conditions evolve. Should governance readiness include a requirement for continuous monitoring of model behavior?

3. **Where does the framework's scope end?** The incident analysis shows that the framework is strong for organizational delegation failures (10/10 general AI incidents) but weaker for individual professional tool use (5/10 LLM incidents). Should the framework be extended to cover individual-level AI tool use, or is that a different instrument?

4. **Can the framework's dimensions be empirically validated?** The dimensions were derived from case analysis and governance practice. Empirical validation would require testing whether the scoring sheet produces authority recommendations that correlate with deployment outcomes — do systems deployed above their recommended authority level fail more often? This requires longitudinal data that does not yet exist.

5. **What is the relationship between delegation calibration and scalable oversight?** Amodei et al. (2016) identify scalable oversight as a concrete safety problem. As AI systems make more decisions at faster speeds, human oversight becomes a bottleneck. The framework assumes that human oversight is available at the "assist" and "recommend" levels, but this assumption may not hold at scale. How should the framework account for oversight capacity constraints?
