# AI Alignment Research Landscape: Codebases, Programs, and Organizations

A survey of the AI alignment research ecosystem — open-source code repositories, fellowship programs, training bootcamps, and governance organizations that collectively form the field's infrastructure.

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
| MIT NDIF Team | NNsight, nnterp — model interpretability infra | https://github.com/ndif-team |
| MIT Multimodal Interpretability | MAIA, FIND — automated interpretability | https://github.com/multimodal-interpretability |
| MIT Algorithmic Alignment Lab | Formal contracts, red-teaming, value alignment | https://github.com/Algorithmic-Alignment-Lab |

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

## Research Fellowship Programs

Programs that produce alignment research outputs through structured mentorship and collaboration.

### MATS (ML Alignment Theory Scholars)

- **Site:** https://www.matsprogram.org/
- **Format:** 12-week in-person fellowship (Berkeley and London)
- **Scale:** 170+ publications, 9,500+ citations from alumni
- **Research tracks:** Empirical (ML experiments on control, interpretability, oversight), Policy & Strategy, Theory, Technical Governance, Compute Infrastructure
- **Mentor orgs:** Anthropic, DeepMind, OpenAI, Redwood Research, ARC, UK AISI, LawZero
- **Alumni outcomes:** 80% work in AI alignment/security; 10% founded organizations (Apollo Research, Timaeus, Center for AI Policy)
- **Notable outputs:** Sparse autoencoders for interpretability, activation engineering, developmental interpretability, situational awareness evaluation
- **Code:** qfeuilla/BehaviorEliciationTool (automated red-teaming)
- **Summer 2026:** Largest cohort — 120 fellows, 100 mentors

### SPAR (Supervised Program for Alignment Research)

- **Site:** https://sparai.org/
- **Format:** Part-time remote fellowship, 5–40 hours/week, 3 months
- **Operated by:** Kairos AI Project, Inc. (501(c)(3) nonprofit)
- **Scale:** 130+ projects for Spring 2026 — largest round of any AI safety research fellowship
- **Mentor count:** 130+ mentors including Dawn Song (UC Berkeley), Dylan Hadfield-Menell (MIT)
- **Research areas:** AI Safety, AI Policy, AI Security, Interpretability, Biosecurity, Societal Impacts
- **Outcomes:** Papers at NeurIPS 2024 and ICML 2025; TIME magazine coverage; job placements at Google AI Safety

**Notable Spring 2026 alignment projects:**

Misalignment detection and control:
- Pre-Emptive Detection of Agentic Misalignment via Representation Engineering (Dawn Song, UC Berkeley)
- Disentangling Instruction-Following from Strategic Obfuscation (WEN XING, MATS)
- Emergent Misalignment via Multi-Model Interactions (LawZero)
- Shutdown-Bench: Evaluating Shutdownability (Elliott Thornley, MIT)
- Stress-testing Honesty Training (Daniel Tan/Chloe Li, CLR/Anthropic)

Mechanistic interpretability:
- Sparse Geometry and Formal Verification for Interpretability (Yuxiao Li)
- Temporal Crosscoders — new SAE architecture for reasoning models (Dmitry Manning-Coe, MATS)
- Automating Circuit Interpretability with Agents (Georg Lange)
- Attribution Methods for LLMs (Uzay Macar, Anthropic Fellows)

Safety evaluation:
- Adversarial Red-Teaming Framework for LLM Agents (Dawn Song, UC Berkeley)
- Jailbreaks for AI Safety — auditing attacks for capable systems (Emil Ryd/Keshav Shenoy, Oxford/Anthropic)
- Richer Evaluations to Address Eval Awareness and Reward Hacking (Santiago Aranguri, Goodfire/NYU)

### LASR Labs (London AI Safety Research Labs)

- **Site:** https://www.lasrlabs.org/
- **Format:** 13-week summer program (July–October), teams of 3–4 supervised by experienced researchers
- **Stipend:** £11,000 + office space, meals, travel
- **Focus:** Technical AI safety — loss of control scenarios
- **Research areas:** Multi-agent collusion, RL alignment theory, deception detection, interpretability, automated interpretability, scalable oversight, AI control
- **Outcomes:** 2024 cohort achieved 100% NeurIPS workshop acceptance; alumni at UK AISI, Apollo Research, Leap Labs, Open Philanthropy

### Apart Research

- **Site:** https://apartresearch.com/fellowships
- **Programs:**
  - **Apart Fellowship** (12–24 weeks, 10–30 hrs/week, remote) — develop hackathon ideas into published research
  - **Partnered Fellowships** (~16 weeks) — work on expert-defined research agendas from partner organizations
- **Focus:** Technical AI safety — model evaluations, interpretability, multi-agent systems, AI security, formal methods, deception detection
- **Entry model:** Merit-based via monthly Research Sprints; continuous pipeline rather than fixed cohorts

### ARENA (Alignment Research Engineer Accelerator)

- **Site:** https://www.arena.education/
- **Format:** 4–5 week in-person bootcamp in London, 2–3 per year; fully funded (travel, visa, accommodation, meals)
- **Focus:** Technical AI safety engineering skills — Python coding, linear algebra, probability foundations
- **Curriculum:** Freely available online for independent learners or organizations running their own courses
- **Alumni outcomes:** Roles at Anthropic, Apollo Research, METR; participation in MATS and LASR

### BlueDot Impact

- **Site:** https://bluedot.org/
- **Format:** Free AI courses, career support, entrepreneurship acceleration, global events
- **Scale:** 5,000+ professionals trained since 2022; £35M raised; 6,000+ alumni
- **Alumni placements:** OpenAI, Anthropic, Google DeepMind, AI Security Institute, UN, NATO, OECD, Stanford HAI, Apple, Harvard Kennedy School

### ML4Good

- **Site:** https://ml4good.org/
- **Format:** Free 8-day residential bootcamps, two tracks:
  - **Technical Programme** — for ML engineers, CS graduates, technical researchers
  - **Governance & Strategy Programme** — for policy/legal professionals, operations, communications
- **Cost:** Free (food, accommodation, teaching provided; travel reimbursed)
- **Alumni outcomes:** Roles at MATS Research, Ada Lovelace Institute, UK AISI, SaferAI, CHAI; 98% recommendation rate

## AI Governance Research Organizations

### GovAI (Centre for the Governance of AI)

- **Site:** https://www.governance.ai/
- **Structure:** US 501(c)(3) nonprofit + UK subsidiary
- **Focus:** Technical AI governance, AI progress forecasting, threat modeling, labor market impact
- **Research topics:** Data center infrastructure policy, China's AI strategy, dual-use biological capabilities, government roles in AI agent infrastructure
- **Programs:** Summer fellowship (research track), open positions

### IAPS (Institute for AI Policy and Strategy)

- **Site:** https://www.iaps.ai/fellowship
- **Type:** Nonpartisan think tank — AI policy research at the intersection of AI, national security, geopolitics
- **AI Policy Fellowship 2026:** 3-month program (June–August), mandatory 2-week DC residency
  - Senior Fellows: $22,000 stipend; Fellows: $15,000 stipend
  - ~30 fellows per cohort
  - Projects: policy briefs, government briefings, conferences, op-eds
  - No technical expertise required

### Orion AI Governance Initiative

- **Site:** https://www.orionaigov.org/
- **Base:** UK-based talent development for AI governance
- **Programs:**
  - **AI Policy Accelerator** — 5-week training course + 4-week research project (10 hrs/week) for graduating students
  - **Internship** — ~3 months over summer, £3,200/month (2025 placements: Safe AI Forum, Social Market Foundation)
  - **Mentorship Programme** — pairing students with AI governance professionals from GovAI, RAND, Ada Lovelace Institute, frontier AI lab policy teams

## Relevance to Business-Context Alignment

These codebases are relevant to business AI alignment in several ways:

1. **Safe RLHF** demonstrates that harmlessness and helpfulness can be separated — directly applicable to business AI where domain risk varies.
2. **HarmBench** provides evaluation methodology transferable to domain-specific safety assessment.
3. **Alignment faking** research raises governance questions: monitoring AI systems that may behave differently under observation vs. production.
4. **Interpretability tools** (TransformerLens, SAELens) are prerequisites for any organization claiming to understand what their AI systems are doing internally.
5. **Agentic misalignment** research is directly relevant as businesses adopt AI agents for autonomous decision-making.

The gap between frontier alignment research (model-level) and business alignment (workflow-level) is where organizational governance must bridge — technical alignment is necessary but not sufficient for safe business deployment.
