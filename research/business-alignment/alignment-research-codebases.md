# AI Alignment Research Codebases

A survey of open-source repositories where AI alignment research is conducted through code — training frameworks, interpretability tools, safety evaluation benchmarks, and misalignment studies.

## Key Observation

AI alignment research repositories structurally have fewer GitHub stars than general-purpose AI tools. Stars reflect user base size, not research quality. In alignment research, 100–1,000 stars typically indicates a core repository. The research community is small and deep; most codebases serve as paper companions rather than production tools.

## Organizations

| Organization | Focus | Link |
|---|---|---|
| Anthropic (official) | SDKs, APIs, Claude tooling | https://github.com/anthropics |
| Anthropic (experimental) | Research prototypes — misalignment, safety | https://github.com/anthropic-experimental |
| Safety Research | Alignment faking replication, Bloom, SAELens | https://github.com/safety-research |
| Center for AI Safety (CAIS) | Benchmarks, evaluation frameworks | https://github.com/orgs/centerforaisafety |
| PKU Alignment | Safe RLHF, constrained value alignment | https://github.com/PKU-Alignment |

## Alignment Training Frameworks

| Repository | Stars | Description |
|---|---|---|
| PKU-Alignment/safe-rlhf | ~1,600 | Safe RLHF — separates harmlessness and helpfulness into independent objectives under safety constraints. Most complete alignment-specific RLHF implementation. |
| OpenLMLab/MOSS-RLHF | ~1,400 | "Secrets of RLHF in Large Language Models" paper code. Analyzes PPO training pitfalls and practical alignment engineering. |
| huggingface/trl | ~17,800 | Not alignment-specific, but the de facto standard for RLHF/DPO/GRPO training. Infrastructure that alignment researchers build on. |
| OpenRLHF/OpenRLHF | ~9,200 | Production-grade distributed RLHF framework (Ray + vLLM). Used for scaling alignment training. |
| tomekkorbak/pretraining-with-human-feedback | ~180 | Research on incorporating human preferences at the pretraining stage, not just fine-tuning. |

## Mechanistic Interpretability

Interpretability is the verification layer for alignment — without understanding model internals, alignment claims remain unverifiable.

| Repository | Stars | Description |
|---|---|---|
| TransformerLensOrg/TransformerLens | ~3,200 | Standard tool for mechanistic interpretability of GPT-style models. Created by Neel Nanda (ex-Anthropic). Exposes internal activations for reverse-engineering learned algorithms. |
| decoderesearch/SAELens | ~1,300 | Sparse Autoencoder training and analysis. Open-source implementation of Anthropic's monosemanticity research — decomposing model internals into interpretable features. |
| callummcdougall/sae_vis | — | Visualization tool replicating Anthropic's SAE feature visualizations. |
| wesg52/sparse-probing-paper | ~66 | Sparse probing research — how model internal representations correspond to human-interpretable concepts. |

Anthropic's primary interpretability research is published at transformer-circuits.pub rather than as GitHub repositories.

## Safety Evaluation and Red-Teaming

| Repository | Stars | Description |
|---|---|---|
| centerforaisafety/HarmBench | ~890 | Standardized evaluation framework for automated red-teaming. 33 LLMs, 18 attack methods. Measures where alignment fails. |
| promptfoo/promptfoo | ~18,500 | LLM red-teaming, pentesting, vulnerability scanning. Used by OpenAI and Anthropic. Broader than alignment but directly relevant. |
| agencyenterprise/PromptInject | ~470 | Prompt injection attack framework. Studies alignment bypass vulnerabilities. |
| hendrycks/ethics | ~320 | "Aligning AI with Shared Human Values" (ICLR 2021). Dan Hendrycks (CAIS founder). Original value alignment benchmark. |

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

## Relevance to Business-Context Alignment

These codebases are relevant to business AI alignment in several ways:

1. **Safe RLHF** demonstrates that harmlessness and helpfulness can be separated — directly applicable to business AI where domain risk varies.
2. **HarmBench** provides evaluation methodology transferable to domain-specific safety assessment.
3. **Alignment faking** research raises governance questions: monitoring AI systems that may behave differently under observation vs. production.
4. **Interpretability tools** (TransformerLens, SAELens) are prerequisites for any organization claiming to understand what their AI systems are doing internally.
5. **Agentic misalignment** research is directly relevant as businesses adopt AI agents for autonomous decision-making.

The gap between frontier alignment research (model-level) and business alignment (workflow-level) is where organizational governance must bridge — technical alignment is necessary but not sufficient for safe business deployment.
