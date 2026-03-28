# Why Mechanistic Interpretability Matters for Delegation Calibration

status: draft
date: 2026-03-27
purpose: Connect the evidence strength ceiling in the delegation framework to the technical capabilities that interpretability research provides. Grounded in Lipton (2018), Rudin (2019), Doshi-Velez and Kim (2017), and Anthropic's sparse autoencoder work.

## The Evidence Strength Problem

The 6-dimensional framework evaluates AI delegation fitness using five scored dimensions. Of these, evidence strength is the most structurally limited.

The current evidence strength scale (from `taxonomy/scoring-sheet.md`):

- **Strong** (3): regulator-backed, audited, or peer-reviewed
- **Moderate** (2): official company or technical documentation
- **Weak** (1): reported or secondary evidence without direct primary confirmation

All three levels depend on external proxies — what other people or institutions say about the system. None of them assess whether the model's internal reasoning actually supports the decision it produced. A model can receive a "strong evidence" rating because a regulator approved it, even if no one understands the internal mechanism that produces its outputs.

Lee and See (2004) identify three bases of trust in automation: performance, process, and purpose. The evidence strength dimension currently captures performance trust (does it work?) and purpose trust (was it designed for this?), but not **process trust** (do we understand how it works?). This is the gap that interpretability addresses.

This creates a ceiling: the framework can evaluate the institutional context around an AI system but cannot evaluate the system itself. For high-risk domains where the framework already defaults to "assist" or "tightly governed recommend," this ceiling is tolerable — human oversight compensates for the opacity. But for any scenario where the framework might justify higher authority levels, the inability to inspect the model's reasoning becomes the binding constraint.

## What Does "Interpretability" Mean Here?

The term is contested. Before mapping interpretability methods to the evidence strength dimension, two important positions must be addressed.

### Lipton (2018): The Mythos of Model Interpretability

Lipton argues that "interpretability" is not a single concept but a collection of loosely related desiderata that are often conflated. He distinguishes:

- **Transparency**: understanding the model's mechanism at the level of the full model (simulatability), individual components (decomposability), or the training algorithm (algorithmic transparency).
- **Post-hoc explanations**: explanations generated after the model produces an output — text explanations, local approximations (e.g., LIME), saliency maps. These do not reveal the model's actual mechanism; they provide a plausible narrative about what the model might be doing.

Lipton's key warning: post-hoc explanations can be misleading. A saliency map that highlights "reasonable" input features does not guarantee that those features actually drove the decision. For delegation calibration, this means that post-hoc explanations alone are insufficient to upgrade evidence strength. They provide a sense of process trust without actually delivering it.

**Implication for the framework:** Evidence strength should not be upgraded based on the presence of post-hoc explanations alone. Only methods that reveal the model's actual decision mechanism — transparency in Lipton's terms — should count toward stronger evidence.

Reference: Lipton, Z. C. (2018). The mythos of model interpretability. *Queue*, 16(3), 31–57.

### Rudin (2019): Stop Explaining Black Box Models

Rudin takes a stronger position: for high-stakes decisions, the solution is not to explain black-box models post hoc but to use inherently interpretable models in the first place. She argues that in domains where decisions affect people's lives (criminal justice, healthcare, lending), the performance gap between black-box and interpretable models is often negligible, and the risks of relying on post-hoc explanations outweigh the benefits.

**Implication for the framework:** In high-risk domains (risk level = 1), the framework should prefer interpretable-by-design models over explained black-box models. If an inherently interpretable model is available and performs comparably, evidence strength can be rated higher than a black-box model with post-hoc explanations, even if the black-box model has marginally better accuracy.

This is a strong position that not all practitioners accept. But it aligns with the framework's conservative stance on high-risk delegation: the override rules already default high-risk domains to lower authority. Rudin's argument provides theoretical backing for why this conservatism is warranted when model internals cannot be inspected.

Reference: Rudin, C. (2019). Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. *Nature Machine Intelligence*, 1(5), 206–215.

## Interpretability Methods and Their Maturity

Rather than listing methods generically, this section assesses which methods are mature enough to actually inform evidence strength grading in a deployment context.

### Feature Attribution (SHAP, Integrated Gradients)

What it does: identifies which input features contributed to a specific prediction.

Maturity: widely available in production ML pipelines. SHAP (Lundberg and Lee, 2017) provides theoretically grounded attributions based on Shapley values from cooperative game theory.

Limitation: feature attribution shows which inputs mattered, but not how the model processed them. A model can attend to the "right" features for the "wrong" reasons. Rudin (2019) notes that saliency-based explanations can be unfaithful to the model's actual mechanism.

**Evidence strength impact:** Feature attribution can upgrade evidence from weak to moderate — it confirms that the model is looking at relevant inputs. But it cannot confirm that the model's internal processing is sound, so it should not by itself justify strong evidence.

### Probing and Representation Analysis

What it does: trains auxiliary classifiers on model internal representations to test whether the model encodes specific concepts. If a probing classifier can extract "patient acuity" from a clinical model's hidden states, the model likely represents that concept internally.

Maturity: established in NLP research (Belinkov and Glass, 2019), but not yet standard in production deployment workflows. Requires expertise to design and interpret probes.

Limitation: probing shows that information is present in representations, not that the model uses it for its predictions. The "right" information may be present but ignored during inference.

**Evidence strength impact:** Probing can support an upgrade from moderate to strong when combined with other methods. It provides partial process trust — confirming that the model represents the right concepts — but does not fully close the gap.

### Sparse Autoencoders (SAEs) and Circuit-Level Analysis

What it does: decomposes model activations into interpretable features (SAEs), or traces computation through specific circuits that implement identifiable functions (circuit analysis). This is the mechanistic interpretability program pursued by Anthropic (Bricken et al., 2023; Templeton et al., 2024) and others.

Maturity: rapidly advancing but not yet deployable in production governance workflows. SAEs have been applied to language models to identify monosemantic features (features that correspond to single, identifiable concepts), but the method requires substantial computational resources and expertise.

Limitation: current SAE work has been demonstrated primarily on language models. Applicability to other model architectures (tabular models, time series, computer vision) is less established. Circuit analysis remains labor-intensive and does not scale to arbitrary model behaviors.

**Evidence strength impact:** When available, this is the only method that can justify a full upgrade to strong evidence. Circuit-level understanding provides genuine process trust — not just what the model looked at or what concepts it encodes, but how it actually processes information to produce its output. However, given current maturity, this is aspirational for most production deployments.

### Inherently Interpretable Models (per Rudin)

What it does: uses model architectures that are interpretable by design — linear models, decision trees, rule lists, generalized additive models (GAMs), scoring systems.

Maturity: fully mature and deployable. The tradeoff is that these models may have lower accuracy on complex tasks, though Rudin argues the gap is often negligible in practice.

**Evidence strength impact:** Inherently interpretable models provide strong evidence by construction — the model's mechanism is its explanation. For high-risk domains where the framework already constrains authority, these models offer the most direct path to higher evidence strength ratings.

## Concrete Delegation Scenarios

### Lending (finance, high-risk)

| Condition | Structure | Risk | Scenario | Evidence | Governance | Score | Authority |
|---|---|---|---|---|---|---|---|
| Black-box, no explanation | semi (2) | high (1) | baseline (3) | weak (1) | strong (3) | 10 | ASSIST (override: weak evidence) |
| Black-box with SHAP | semi (2) | high (1) | baseline (3) | moderate (2) | strong (3) | 11 | RECOMMEND |
| Interpretable model (GAM) | semi (2) | high (1) | baseline (3) | strong (3) | strong (3) | 12 | RECOMMEND |

The Rudin argument applied: if an interpretable lending model (e.g., a scoring card or GAM) achieves comparable accuracy to a black-box model, the framework recommends using the interpretable model because it achieves strong evidence without requiring post-hoc explanation infrastructure.

### Clinical Decision Support (healthcare, high-risk)

| Condition | Structure | Risk | Scenario | Evidence | Governance | Score | Authority |
|---|---|---|---|---|---|---|---|
| Black-box, no explanation | semi (2) | high (1) | baseline (3) | moderate (2) | partial (2) | 10 | RECOMMEND |
| Black-box with probing validation | semi (2) | high (1) | baseline (3) | strong (3) | partial (2) | 11 | RECOMMEND |

Here the authority level does not change, but the score margin increases. With probing validation confirming that the model represents clinical concepts correctly, the recommendation is more robust to perturbations. A stress scenario (score -1) would drop the non-interpretability case below the RECOMMEND threshold but keep the interpretability case above it.

### Resume Screening (hiring, high-risk)

| Condition | Structure | Risk | Scenario | Evidence | Governance | Score | Authority |
|---|---|---|---|---|---|---|---|
| Black-box, no explanation | semi (2) | high (1) | baseline (3) | weak (1) | partial (2) | 9 | ASSIST (override: weak evidence) |
| Black-box with SHAP | semi (2) | high (1) | baseline (3) | moderate (2) | partial (2) | 10 | RECOMMEND |
| Interpretable model | semi (2) | high (1) | baseline (3) | strong (3) | partial (2) | 11 | RECOMMEND |

This is where interpretability makes the largest practical difference. The Amazon hiring incident from the incident inventory is a case where an opaque model encoded gender bias through proxy features. Feature attribution (SHAP) would have revealed the proxy reliance. An inherently interpretable model would have made the bias visible by construction.

## Regulatory Context

The framework's evidence strength dimension does not exist in a vacuum. Regulatory requirements already mandate varying degrees of model transparency:

- **EU AI Act (2024)**: High-risk AI systems must be "sufficiently transparent to enable deployers to interpret a system's output and use it appropriately." This is a process trust requirement.
- **NIST AI RMF (2023)**: Lists "explainable and interpretable" as a trustworthiness characteristic. The MEASURE function includes evaluating explainability.
- **OECD AI Principles (2019)**: Principle 1.3 calls for "transparency and responsible disclosure" including "meaningful information to foster understanding."
- **FDA guidance on AI/ML in medical devices**: Requires that developers provide information about the logic and intended use of AI-enabled devices.

The evidence strength dimension can serve as a bridge between these regulatory transparency requirements and technical interpretability research. Regulatory requirements define what must be explainable; interpretability research provides the methods to achieve it; the framework translates both into a delegation authority decision.

## Research Directions

### 1. Interpretability-Aware Evidence Grading

The current 3-level evidence scale could be extended with interpretability-specific criteria:

- **Strong**: external validation AND internal mechanisms are inspectable and aligned with intended reasoning (Lipton's transparency, or Rudin's inherent interpretability)
- **Moderate**: external validation AND post-hoc explanations available (feature attribution, probing) — but mechanism not fully transparent
- **Weak**: external validation only, or no validation at all — no insight into model internals

This revision would make Lee and See's process trust explicit in the framework and create a formal link between interpretability research outputs and governance decisions.

### 2. Incident-Driven Interpretability Priorities

The alignment failure mapping (see `incidents/alignment-failure-mapping.md`) identifies which failure modes the framework's current dimensions cannot detect. Reward hacking and side effects are the most common general AI failures, and both are detectable through interpretability methods — feature attribution reveals proxy reliance, and probing reveals whether the model encodes the intended concepts.

The priority for interpretability research, from a delegation calibration perspective, should be the methods that detect the most common failure modes, not the most technically elegant methods. Feature attribution (mature, deployable) addresses the most frequent failures. Circuit-level analysis (immature, aspirational) addresses the deepest failures but is not yet practical.

### 3. The Interpretable-by-Design Path

Rudin's argument suggests that for high-risk domains where the framework already constrains authority, the most practical path to higher evidence strength is not to explain complex models but to use simpler, interpretable models. This trades marginal accuracy for substantially higher process trust. The framework's scoring sheet quantifies this tradeoff: if moving from a black-box (evidence=1) to an interpretable model (evidence=3) raises the score by 2 points, that may cross an authority band threshold — a concrete organizational benefit that justifies the accuracy tradeoff.
