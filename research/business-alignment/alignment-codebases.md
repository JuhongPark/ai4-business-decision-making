# AI Alignment Research Codebases

A survey of open-source repositories where AI alignment research is conducted through code. Star counts as of 2026-03-26.

## Scope and Method

This survey covers publicly visible GitHub repositories selected through keyword searches (alignment, RLHF, interpretability, safety evaluation, misalignment) and organization-level browsing. Selection criteria: (1) directly implements or evaluates alignment techniques, (2) has published associated research, (3) is actively maintained or recently cited. The list is not exhaustive — it excludes proprietary corporate alignment work, classified government programs, non-English-language ecosystems, and repositories that were missed during search. Organizations like EleutherAI, Redwood Research, and ARC Evals maintain relevant code that is not covered here.

## Key Observation

AI alignment research repositories structurally have fewer GitHub stars than general-purpose AI tools. Stars reflect user base size, not research quality — they are included as a rough indicator of community adoption, not as a quality measure. In alignment research, 100–1,000 stars typically indicates a core repository. Most codebases are research prototypes and paper companions, not production-ready tools.

## GitHub Organizations

| Organization | Focus | Link |
|---|---|---|
| Anthropic (official) | SDKs, APIs, Claude tooling | https://github.com/anthropics |
| Anthropic (experimental) | Research prototypes — misalignment, safety | https://github.com/anthropic-experimental |
| Safety Research | Alignment faking replication, Bloom, SAELens | https://github.com/safety-research |
| Center for AI Safety (CAIS) | Benchmarks, evaluation frameworks | https://github.com/orgs/centerforaisafety |
| PKU Alignment | Safe RLHF, constrained value alignment | https://github.com/PKU-Alignment |
| MIT NDIF Team | NNsight, nnterp — model interpretability infra | https://github.com/ndif-team |
| MIT Multimodal Interpretability | MAIA, FIND — automated interpretability | https://github.com/multimodal-interpretability |
| MIT Algorithmic Alignment Lab | Formal contracts, red-teaming, value alignment | https://github.com/Algorithmic-Alignment-Lab |

## Alignment Training Frameworks

| Repository | Stars | Maturity | Description |
|---|---|---|---|
| PKU-Alignment/safe-rlhf | ~1,600 | Research | Safe RLHF — separates harmlessness and helpfulness into independent objectives under safety constraints. Most cited alignment-specific RLHF implementation (per associated NeurIPS paper). |
| OpenLMLab/MOSS-RLHF | ~1,400 | Research | "Secrets of RLHF in Large Language Models" paper code. Analyzes PPO training pitfalls and practical alignment engineering. |
| huggingface/trl | ~17,800 | Production | Not alignment-specific, but the de facto standard for RLHF/DPO/GRPO training. Infrastructure that alignment researchers build on. Actively maintained with enterprise adoption. |
| OpenRLHF/OpenRLHF | ~9,200 | Production | Production-grade distributed RLHF framework (Ray + vLLM). Designed for scaling alignment training in deployment settings. |
| tomekkorbak/pretraining-with-human-feedback | ~180 | Research | Research on incorporating human preferences at the pretraining stage, not just fine-tuning. |

**Maturity legend:** *Production* = actively maintained, documented, used in enterprise/lab settings. *Research* = paper companion or prototype, may require significant adaptation for production use.

## Mechanistic Interpretability

One school of thought in alignment research holds that interpretability is a necessary verification layer — that without understanding model internals, alignment claims remain difficult to verify (cf. Anthropic's "Scaling Monosemanticity" research direction). This is not universally accepted; behavioral evaluation approaches argue that external testing can suffice without internal understanding.

| Repository | Stars | Maturity | Description |
|---|---|---|---|
| TransformerLensOrg/TransformerLens | ~3,200 | Research | Widely used tool for mechanistic interpretability of GPT-style models. Created by Neel Nanda (ex-Anthropic). Exposes internal activations for reverse-engineering learned algorithms. |
| decoderesearch/SAELens | ~1,300 | Research | Sparse Autoencoder training and analysis. Open-source implementation of Anthropic's monosemanticity research — decomposing model internals into interpretable features. |
| callummcdougall/sae_vis | — | Research | Visualization tool replicating Anthropic's SAE feature visualizations. |
| wesg52/sparse-probing-paper | ~66 | Research | Sparse probing research — how model internal representations correspond to human-interpretable concepts. |

Anthropic's primary interpretability research is published at transformer-circuits.pub rather than as GitHub repositories.

## MIT Alignment Research

MIT's alignment research concentrates on interpretability tooling — building instruments to see inside models rather than training aligned models directly.

### NDIF / NNsight (MIT EECS, David Bau Lab)

| Repository | Stars | Description |
|---|---|---|
| ndif-team/nnsight | ~870 | Model internals interpretation and manipulation library. Wraps HuggingFace models with a tracing system for interventions. MIT's primary alternative to TransformerLens. |
| ndif-team/nnterp | ~104 | Unified interface for transformer analysis via NNsight. Supports 50+ model variants across 16 architecture families. |
| ndif-team/ndif | ~43 | National Deep Inference Fabric — remote deep inference server for large-scale interpretability research. |
| ndif-team/cookbook | 5 | NNsight implementations of published mechanistic interpretability papers. |

### Multimodal Interpretability (MIT CSAIL, Sarah Schwettmann Lab)

| Repository | Stars | Description |
|---|---|---|
| multimodal-interpretability/maia | ~105 | MAIA — Multimodal Automated Interpretability Agent. Uses vision-language models to automatically interpret other models' internals. |
| multimodal-interpretability/FIND | ~52 | NeurIPS '23. Function Interpretation Benchmark for evaluating interpretability methods. |
| multimodal-interpretability/nnn | ~20 | Nearest Neighbor Normalization (EMNLP 2024). |

This group launched Transluce (transluce.org) in October 2024 as a nonprofit research lab for open, scalable AI understanding tools.

### Algorithmic Alignment Lab (MIT CSAIL, Dylan Hadfield-Menell Lab)

| Repository | Stars | Description |
|---|---|---|
| Algorithmic-Alignment-Lab/contracts | ~19 | Formal contracts for multi-agent reinforcement learning. Theoretical framework for agent coordination under alignment constraints. |
| Algorithmic-Alignment-Lab/CommonClaim | ~13 | "Explore, Establish, Exploit: Red Teaming Language Models from Scratch." Systematic red-teaming methodology. |

This group focuses more on theory and policy than code — formal frameworks for aligning AI development with human interests and values.

### MIT AI Risk Repository (MIT FutureTech, Peter Slattery)

Not a code repository but a structured research database relevant to alignment:

- **Site:** https://airisk.mit.edu/
- **Scale:** 1,700+ AI risks extracted from 74 frameworks (Version 4, December 2025)
- **Taxonomies:** Causal taxonomy (how/when/why risks occur) and Domain taxonomy (7 domains, 24 subdomains)
- **AI Incident Tracker:** LLM-powered categorization of incidents from the AI Incident Database (AIID)
- **Paper:** arXiv:2408.12622

## Safety Evaluation and Red-Teaming

| Repository | Stars | Maturity | Description |
|---|---|---|---|
| centerforaisafety/HarmBench | ~890 | Research | Standardized evaluation framework for automated red-teaming. 33 LLMs, 18 attack methods. Measures where alignment fails. |
| promptfoo/promptfoo | ~18,500 | Production | LLM red-teaming, pentesting, vulnerability scanning. Claims usage by OpenAI and Anthropic (per project website, vendor self-reported — not independently verified). The most enterprise-ready safety evaluation tool in this list. |
| agencyenterprise/PromptInject | ~470 | Research | Prompt injection attack framework. Studies alignment bypass vulnerabilities. |
| hendrycks/ethics | ~320 | Research | "Aligning AI with Shared Human Values" (ICLR 2021). Dan Hendrycks (CAIS founder). Original value alignment benchmark. |

## Misalignment and Alignment Faking Research

| Repository | Stars | Description |
|---|---|---|
| anthropic-experimental/agentic-misalignment | ~580 | Anthropic official. Studies agentic misalignment behavior — blackmail, information leakage, deceptive compliance in frontier models. |
| safety-research/open-source-alignment-faking | ~54 | Open-source replication of Anthropic's alignment faking paper. Studies models that appear aligned during evaluation but behave differently when unmonitored. |

## Anthropic's Research Publication Channels

Anthropic publishes alignment research primarily through dedicated sites, not GitHub:

- **alignment.anthropic.com** — Alignment science blog (Bloom auto-evals, Petri auditing tool, etc.)
- **transformer-circuits.pub** — Mechanistic interpretability research (Scaling Monosemanticity, circuit analysis)
- **anthropic.com/research** — Full research index

Code accompaniments, when released, appear under the `anthropic-experimental` or `safety-research` organizations.

## Business Implications

For organizations deploying LLMs, the practical takeaway from this landscape:

1. **Immediate enterprise use:** Only promptfoo (safety evaluation), trl (RLHF training), and OpenRLHF (distributed RLHF) are production-grade. All other repositories require significant adaptation for non-research use.
2. **Safety evaluation first:** Organizations that want to assess LLM safety before deployment should consider promptfoo for red-teaming and vulnerability scanning — it is the only tool here with claimed enterprise adoption (vendor self-reported).
3. **Interpretability tools are pre-commercial:** TransformerLens, SAELens, and NNsight are research instruments. No publicly documented case exists of an organization using them in production governance workflows as of this writing. Their business relevance is forward-looking, not immediate.
4. **Hiring signal:** Familiarity with these tools is a strong signal for AI safety hiring. Candidates who have used TransformerLens, contributed to SAELens, or published via MATS/SPAR are among the few with hands-on alignment experience.

## Limitations

- **Coverage:** This survey is limited to publicly visible, English-language GitHub repositories found through keyword search. Proprietary alignment work at Anthropic, OpenAI, DeepMind, and others is not represented. Non-GitHub platforms (e.g., GitLab, internal repos) are excluded.
- **Star counts** are a rough adoption proxy, not a quality measure. They are included for orientation and decay rapidly.
- **Maturity classifications** (Production/Research) are the author's judgment based on documentation quality, maintenance activity, and stated adoption — not independently verified.
- **Snapshot date:** All data is as of 2026-03-26 and will become stale. This is a one-time survey, not a maintained resource. Users should verify current status before acting on any entry.
- **Author positionality:** The author is not affiliated with any organization, program, or lab listed in this survey. No funding was received from any listed entity.
