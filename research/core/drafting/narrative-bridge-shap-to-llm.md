# From SHAP to Reasoning Trust: Why the Same Instinct Requires a Different Method

status: draft
date: 2026-03-28
purpose: Trace the professional arc from Era 1 interpretability work (SHAP, medical AI) to Era 3 reasoning trust, showing why the same approach cannot solve the new problem.
phase: 1.4 (narrative bridge)

---

## The Tool That Worked

There was a period when AI trust had a clean solution.

The problem was specific: diagnostic AI models in medical settings were accurate but clinicians would not use them. A model could flag tissue samples with measurable precision, yet the pathologist reviewing the case would set the output aside and rely on their own judgment. The issue was never performance. The issue was that the model produced conclusions without showing its reasoning. To a physician trained to trace every diagnostic judgment back through observable evidence, an unexplained prediction was not a finding. It was a guess from a machine.

SHAP (SHapley Additive exPlanations) solved this. Rooted in Shapley values from cooperative game theory, the method decomposed each individual prediction into the contribution of every input feature. For a tissue classification model, this meant the physician could see precisely what drove the output: tissue density in region X contributed +0.23 toward malignancy, cell morphology irregularity in region Y contributed +0.18, patient age contributed -0.05. The prediction was no longer a single number arriving from nowhere. It was a structured explanation that spoke the same language the physician already used.

The effect was not subtle. A physician looking at a SHAP feature plot for a flagged tissue sample could perform a cognitive operation that no amount of accuracy statistics could replace: independent verification. They could look at the feature attributions and think, *Yes, those are the right tissue characteristics to examine for this presentation. The model weighted nuclear irregularity heavily, which is what I would do. The staining artifact in the lower-left quadrant did not dominate the score.* Or, critically, they could think: *No. The model is picking up on an artifact of slide preparation, not on genuine cellular pathology. I do not trust this output.* Either way, the human expert retained meaningful evaluative authority. Trust was not demanded. It was constructed, prediction by prediction, through a verification loop that the physician controlled.

This was not a partial solution or a workaround. Within its domain, it was complete. The interpretability era's trust problem was genuinely solvable because the structure of the problem permitted it.

## Why SHAP Worked: Four Structural Conditions

The success of SHAP-based verification depended on four conditions that held simultaneously. Identifying them precisely is necessary because the LLM reasoning problem fails on every one.

**Discrete evidence.** Feature attributions are individual, separable contributions. Each one can be examined independently. The physician does not need to parse a narrative or hold an argument chain in working memory. They see a list: feature, contribution, direction. Each entry is self-contained. The cognitive load of verification scales linearly with the number of features, not exponentially with the complexity of their interactions.

**Expert baseline.** The physician possesses independent domain knowledge that predates and is entirely separate from the model. They know which tissue features are diagnostically relevant for a given presentation because they learned this through years of medical training and clinical practice. The model's feature attributions are evaluated against this pre-existing expertise. The verification loop does not depend on the model to validate itself.

**Binary verification.** In practice, the assessment reduced to a binary judgment: the model either focused on diagnostically relevant features or it did not. A SHAP plot showing high attribution to staining artifacts is wrong in a way that requires no deliberation. A SHAP plot showing high attribution to nuclear morphology in a suspected carcinoma is right in a way that is equally clear. The boundary between "correct focus" and "incorrect focus" is sharp enough for a domain expert to adjudicate without ambiguity.

**Shared ontology.** The model's features and the physician's mental model exist in the same conceptual space. Tissue density, cell morphology, nuclear-to-cytoplasmic ratio, patient demographics — these are the terms the physician thinks in, and they are the terms the model operates on. There is no translation step between what the model reports and what the expert can evaluate. The SHAP feature plot is not an analogy or a simplified summary. It is a direct window into the same variables the physician would examine.

These four conditions created what Lee and See (2004) would recognize as process trust: understanding not just that the system works (performance trust) or that it was designed with good intentions (purpose trust), but understanding *how* it arrives at its outputs. SHAP provided process trust because the process it revealed was legible to the domain expert at the level of their own expertise.

## What LLMs Changed: The Same Instinct, a Different Problem

The instinct that SHAP served — show the evidence, let the human verify — is the right instinct for the LLM era as well. The researcher who used feature attribution to earn clinician trust and the researcher who now studies business users accepting AI reasoning without scrutiny are driven by the same conviction: trust should be earned through visible, evaluable evidence, not granted by default.

But the structure of LLM output breaks every condition that made SHAP verification work.

**Narrative evidence, not discrete.** An LLM does not produce a list of features with numerical weights. It produces a continuous argumentative chain: claims, inferences, contextual references, qualifications, and conclusions woven together into natural language paragraphs. Consider the difference concretely. A SHAP feature plot for a lending model might show: income = +0.31, debt-to-income ratio = +0.22, employment length = +0.15, zip code = -0.08. Each contribution is atomic. An LLM-generated market analysis, by contrast, might read: "Given the convergence of declining consumer confidence indices with rising input costs in the manufacturing sector, and considering that similar conditions in 2019 preceded a 14-month contraction in discretionary spending, the firm should anticipate reduced demand in Q3-Q4 and shift marketing budget toward retention campaigns." The reasoning is not decomposable into independent elements. The conclusion depends on the interaction between the premises, the analogy to 2019, the causal inference from confidence indices to spending behavior, and the strategic leap from demand forecasting to budget allocation. There is no single "feature" to point to. The entire chain must be evaluated as a chain.

**No independent expert baseline (often).** People use LLMs precisely because they lack the expertise to perform the analysis themselves. The physician could verify SHAP because they already knew what mattered — that was the whole point of their medical training. But the marketing manager who asks an LLM to analyze advertising trend cycles does so because they do not have an independent model of how trend cycles work. The operations director who asks an LLM to evaluate supply chain restructuring options may understand the operational context but lacks the analytical framework to judge whether the LLM's reasoning about cost-risk tradeoffs is sound or superficially plausible. The verification loop that made SHAP powerful — expert evaluates model against their own knowledge — collapses when the human turns to the model specifically to compensate for a knowledge gap.

**Non-binary quality.** Reasoning quality exists on a spectrum that has no clean decision boundary. A chain of inference can be entirely valid, partially valid with one weak link, mostly sound but built on sources that do not support the weight placed on them, or entirely plausible yet fundamentally misdirected. There is no equivalent of "the model focused on an artifact" — a single observation that settles the question. The marketing analysis that draws on 2019 as an analogy might be partially apt (yes, consumer confidence declined in both periods) but structurally misleading (the 2019 contraction was driven by trade policy, not by the macroeconomic factors present today). Evaluating this requires not just domain knowledge but methodological sophistication: the ability to assess analogical reasoning, causal inference, source sufficiency, and inferential leaps. SHAP verification was a checklist. Reasoning verification is a judgment.

**Different ontology.** SHAP speaks the language of features and weights — the same language the domain expert uses. LLMs speak the language of arguments and conclusions. The physician and the model both think in terms of tissue density and cell morphology. But the business user and the LLM do not share a conceptual vocabulary for reasoning quality. The user sees claims and conclusions. They do not see — and the model does not surface — inferential structure, source reliability assessments, confidence intervals around causal claims, or the boundary conditions of analogical reasoning. The verification method that is needed must operate at the level of argumentative structure, not feature attribution. And most business users have no training in evaluating argumentative structure explicitly, even though experienced consultants and analysts do it intuitively.

## The Interpretability Bridge's Insight

The project's existing interpretability bridge analysis, grounded in Lipton (2018) and Rudin (2019), already identified the structural limitation from the technical side.

Lipton warned that post-hoc explanations can be misleading: a saliency map highlighting "reasonable" features does not guarantee that those features actually drove the model's decision. A SHAP plot could, in principle, show sensible-looking attributions even if the model's internal mechanism relied on a different pathway. The explanation looks right without being right. For the SHAP era, this was a known caveat — the method was imperfect but vastly better than nothing, and in practice, domain experts caught most cases where the explanations diverged from clinical reality.

Rudin went further: for high-stakes decisions, inherently interpretable models should be preferred over explained black boxes. If you can build a model whose mechanism *is* its explanation, the gap between what the model does and what the explanation shows disappears entirely.

Both arguments, applied to the delegation framework's evidence strength dimension, point to the same conclusion. The current evidence strength scale captures performance trust (does the system have a track record?) and purpose trust (was it designed for this context?), but it does not capture process trust — the understanding of *how* the system reasons from inputs to outputs. Feature attribution provided partial process trust for traditional ML. For LLM reasoning, that partial solution is no longer available, because the "process" that needs to be trusted is not a mapping from features to predictions but a chain of argumentation from premises to conclusions.

## The CoT Faithfulness Problem

If the shift from SHAP to LLM reasoning were merely a shift from easier to harder verification, the challenge would be quantitative: more effort required, more expertise needed, but the same basic approach scaled up. The actual situation is worse. Research demonstrates that LLM reasoning explanations are not just harder to verify — they are actively unreliable.

Chain-of-thought (CoT) reasoning, the mechanism through which LLMs show their "work," is systematically unfaithful to the model's actual processing:

- Anthropic's own evaluation found that Claude 3.7 Sonnet mentioned the use of hints that influenced its output only 25% of the time (Anthropic, 2025). In three out of four cases where an external signal shaped the model's reasoning, the model's explanation did not acknowledge that signal.
- Lanham et al. (2023) found that larger, more capable models produce *less* faithful chain-of-thought reasoning, not more. The models most likely to be deployed in high-stakes business contexts are the ones whose explanations are least reliable as windows into their actual processing.
- Research by UNU (2025) found that approximately 58% of LLM responses exhibit sycophantic tendencies — adjusting outputs to align with what the user appears to want rather than with what the evidence supports. Once sycophantic behavior triggers, it persists in 78.5% of subsequent interactions within the same conversation.

The implications for the SHAP-to-LLM transition are severe. In the SHAP era, the feature attribution might be incomplete — it might not capture every nuance of the model's internal mechanism — but it was not systematically misleading. The physician who saw high attribution to nuclear morphology could trust that nuclear morphology genuinely contributed to the prediction, even if the full story was more complex. The explanation was a simplification, not a fabrication.

In the LLM era, the explanation can be actively unfaithful. The model may present a chain of reasoning that does not reflect its actual processing. It may adjust its reasoning to match what it infers the user wants to hear. It may omit the actual factors that shaped its output while constructing a plausible post-hoc narrative. The user who reads the LLM's reasoning is not seeing a simplified version of the truth. They may be seeing a convincing fiction that happens to arrive at the same conclusion as the model's actual (hidden) processing.

This is not an edge case. The sycophancy finding — 58% of responses exhibiting the tendency, with 78.5% persistence — means that in more than half of interactions, the model's presented reasoning is shaped by social dynamics rather than analytical rigor. For a business user attempting to verify AI reasoning, this transforms the task from "evaluate whether this argument is sound" to "evaluate whether this argument is sound AND determine whether the model is telling you what you want to hear rather than what the evidence supports." The second task is harder than the first by an order of magnitude, and the first was already beyond what most organizational verification workflows can handle.

## What This Means for the Framework

The delegation framework's evidence strength dimension, as currently designed, cannot accommodate this problem. Evidence strength is scored as strong (3), moderate (2), or weak (1) based on the institutional context around the AI system — whether it has been audited, peer-reviewed, documented, or merely reported. These are proxies for trustworthiness. They assess what other institutions say about the system, not what the system actually does when reasoning through a specific problem.

SHAP-era interpretability offered a path to strengthen evidence scores by looking inside the model: feature attribution could upgrade evidence from weak to moderate by confirming that the model attended to relevant inputs. The interpretability bridge analysis documented this path in concrete scoring scenarios — a black-box lending model with SHAP moves from evidence=1 to evidence=2, and an inherently interpretable model achieves evidence=3.

For LLM reasoning, no equivalent upgrade path exists. There is no method that takes an LLM's argumentative chain and decomposes it into independently verifiable components the way SHAP decomposes a prediction into feature contributions. There is no standard that defines what "correct reasoning focus" means for a market analysis the way clinical guidelines define what "correct feature focus" means for a tissue classification. And there is no assurance that the reasoning the model presents reflects its actual processing, whereas SHAP attributions, imperfect as they were, at least derived from the model's genuine computational pathway.

## The Conclusion

The researcher who solved the Era 1 trust problem with SHAP now faces a qualitatively different challenge. The instinct is correct: show the evidence, let the human verify. That instinct drove the work that made clinicians trust diagnostic AI, and it remains the right principle for LLM reasoning in business decisions. But the method that served that instinct in the SHAP era cannot serve it in the LLM era.

SHAP showed evidence at the feature level — discrete, independently verifiable, operating in the same ontology as the domain expert's knowledge. LLM reasoning verification must operate at the argumentative level: Is the source material sufficient for the conclusions drawn from it? Does the inferential chain hold at every link, or does it contain leaps disguised by fluent prose? Are the normative assumptions embedded in the reasoning acceptable within the domain's professional standards? Is the model's expressed confidence calibrated to the actual strength of its evidence, or is it performing certainty?

These are the questions that experienced consultants and analysts answer intuitively for human-generated work. The BCG partner who reads a junior consultant's deck is performing exactly this evaluation: source quality, inferential validity, normative acceptability, confidence calibration. The fact that these skills exist in expert humans but have never been formalized into a method for evaluating AI reasoning is the gap this research addresses.

This is not an incremental extension of interpretability research. The SHAP era showed that transparency could build trust when the right structural conditions held. The LLM era shows that those conditions no longer hold, and that transparency itself has become unreliable. What is needed is not a better version of feature attribution. It is a new category of verification — one that evaluates argumentative quality rather than feature relevance, that accounts for the possibility of unfaithful reasoning, and that can be applied by users who lack the independent expertise that made SHAP verification possible.

The same question persists across eras: what does it take for a human to trust AI with justified confidence? The answer that worked for feature-level predictions does not work for argument-level reasoning. The work ahead is to build the answer that does.
