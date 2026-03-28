# Research Direction: From Delegation Governance to Alignment and Safety

status: draft
date: 2026-03-27

## Where the Research Stands

This repository started with a practical question: under what conditions should organizations let AI systems assist, recommend, or automate business decisions? The answer took the form of a 6-dimensional scoring framework, 7 decision rules, 3 override constraints, and a 71-incident failure inventory.

During the course of this work, a broader realization emerged. The question "how much authority should this AI system receive?" is not only a business governance question. It is an alignment question. The framework already encodes alignment-relevant structure — risk thresholds, fallback triggers, evidence requirements — but the research has not yet made that connection explicit or grounded it in the alignment literature.

## What the Research Already Contains

| Framework component | What it does | Alignment parallel |
|---|---|---|
| Authority levels (assist / recommend / automate) | Grades how much autonomy AI receives | Delegation spectrum in human oversight research |
| Risk level dimension | Evaluates consequence severity | Catastrophic risk assessment |
| Evidence strength dimension | Rates confidence in the AI system's outputs | Model inspectability — how verifiable is the reasoning? |
| Governance readiness dimension | Checks organizational oversight capacity | Oversight infrastructure and corrigibility |
| Override rules | Hard constraints that cap authority regardless of score | Safety constraints that cannot be optimized away |
| Incident inventory (71 cases) | Catalogs real-world AI deployment failures | Alignment failure modes — specification gaming, distributional shift, oversight collapse |

These parallels are not retrofitted. The framework was built to answer "when should AI be trusted with authority," which is the deployment-side formulation of the alignment problem.

## Open Problems

### 1. The evidence strength ceiling

The framework's weakest dimension is evidence strength. Currently it relies on external proxies: regulatory validation, peer review, company documentation. These tell you whether other people trust the system, not whether the system's internal reasoning supports the decision.

This is where interpretability becomes necessary — not as a theoretical interest, but as a practical requirement. If a lending model scores high on every other dimension but its reasoning cannot be inspected, the framework forces a one-level authority reduction. Mechanistic interpretability would allow evidence strength to be grounded in model internals rather than external reputation.

### 2. The incident inventory lacks alignment-theoretic grounding

71 incidents are cataloged and split into general-AI and LLM-specific failure types. The classification was done by sector and failure mechanism, but it has not been mapped to alignment failure mode taxonomies in the literature. Connecting the incident patterns to established concepts (specification gaming, reward hacking, goal misgeneralization, distributional shift) would strengthen both the incident analysis and the framework's theoretical basis.

### 3. The delegation framework lacks connection to human-AI trust calibration research

The scoring dimensions were derived from case analysis and governance practice. They have not been compared to existing models of human-AI trust, delegation, and reliance from the decision science and AI safety literature. Grounding the framework in this body of work would clarify what the dimensions capture and what they miss.

## Next Steps

### Step 1: Make the alignment connection explicit (completed)

The README and research framing now reflect the delegation calibration problem directly, with sections connecting the framework to AI safety, interpretability, and alignment failure modes.

### Step 2: Ground the framework in alignment and trust calibration literature

Write a literature bridge note that connects the 6-dimensional framework to relevant published work.

**`research/extensions/alignment-literature-bridge.md`**

Key literature threads to engage:

1. **Human-AI delegation and trust calibration.** Lee and See (2004) on trust in automation. Dietvorst et al. (2015) on algorithm aversion — already in reading notes. Bansal et al. (2021) on when humans should and should not defer to AI. The framework's authority levels (assist/recommend/automate) should be positioned relative to these models: where does the framework agree, where does it add structure, and where is it missing nuance?

2. **AI governance frameworks in practice.** NIST AI RMF (2023), EU AI Act risk classification, ISO 42001. The framework's risk level dimension parallels the EU AI Act's risk tiers (unacceptable/high/limited/minimal). Document where the framework's classification converges with and diverges from these regulatory taxonomies.

3. **Alignment failure mode taxonomies.** Amodei et al. (2016) on concrete problems in AI safety. Krakovna et al. (2020) on specification gaming examples. Ngo et al. (2022) on alignment problem framing. Map the 71 incidents to these established taxonomies rather than inventing a new one.

4. **Interpretability and trust.** Doshi-Velez and Kim (2017) on interpretability desiderata. Lipton (2018) on the mythos of model interpretability. Anthropic's work on sparse autoencoders and circuit-level understanding. Connect these to the evidence strength dimension — what specific interpretability methods would satisfy each evidence strength level?

### Step 3: Deepen the interpretability bridge with literature grounding

The current `interpretability-bridge.md` describes the evidence strength ceiling and sketches how interpretability tools address it. The next version should:

1. Reference specific interpretability methods and their maturity levels, rather than listing them generically. For each method (feature attribution, probing, SAEs, circuit analysis), cite the key paper and assess whether the method is mature enough to actually grade evidence strength in a deployment context.

2. Engage with critiques of interpretability. Lipton (2018) and Rudin (2019) have different positions on what interpretability means and when it matters. The bridge document should acknowledge these tensions and take a position on which interpretability definition the framework requires.

3. Connect to the OECD/NIST transparency requirements that already apply to high-risk AI systems. The framework's evidence strength dimension should be positioned as a bridge between technical interpretability research and regulatory explainability requirements.

### Step 4: Strengthen the incident analysis with literature-grounded taxonomy

The current incident inventory classifies by sector and failure mechanism. Reanalyze the incidents using an alignment-grounded taxonomy:

1. Apply the Amodei et al. (2016) concrete problems framework: which incidents are reward hacking, side effects, distributional shift, unsafe exploration, or scalable oversight failures?

2. For LLM-specific incidents, apply the Weidinger et al. (2022) taxonomy of LLM risks: which incidents are misinformation, bias, data privacy, malicious use, human-AI interaction failure, or environmental cost?

3. Produce a revised incident classification table that maps each incident to both the framework's 6 dimensions and to alignment failure mode categories from the literature. This creates a testable claim: if the framework had been applied beforehand, which dimensions would have flagged the failure?

### Step 5: Write a research note on delegation as an alignment problem

A standalone note that makes the core argument explicitly, suitable for use in applications or as a paper seed.

**`research/extensions/delegation-as-alignment.md`**

Structure:

1. The delegation calibration problem — what it is, why it matters, how it differs from technical alignment but complements it.
2. What existing alignment research says about delegation and oversight — synthesize from the literature survey in Step 2.
3. What the 6-dimensional framework contributes — a concrete, structured instrument for the governance layer that sits between technical alignment and organizational decision-making.
4. What the framework cannot do without interpretability — the evidence strength ceiling argument.
5. Open questions — where this line of research leads.

## Execution Priority

| Order | Step | Effort | Rationale |
|---|---|---|---|
| 1 | Step 1: alignment framing | Done | README and framing already updated |
| 2 | Step 2: literature bridge | 3–4 hours | Grounds the framework in published work — this is the highest-value addition |
| 3 | Step 4: incident reanalysis | 2–3 hours | Makes the incident inventory academically rigorous |
| 4 | Step 3: interpretability bridge revision | 2 hours | Deepens existing document with literature references |
| 5 | Step 5: delegation-as-alignment note | 2–3 hours | Crystallizes the core argument into a standalone document |

## Constraints

- Do not alter existing research content. Add new analysis and literature connections alongside it.
- Do not overstate the alignment connection. This is governance research that borders alignment, not an alignment solution.
- Cite specific papers rather than making generic claims about "the literature."
- Incident reanalysis must preserve source attribution and evidence-type classification.
