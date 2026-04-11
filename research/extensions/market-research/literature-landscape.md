# Literature Landscape: Reasoning Verification in AI Market Research

status: Phase 1 deliverable
date_created: 2026-04-11
purpose: map the relevant literature, identify connections to existing repository assets, and locate the specific gap this extension fills

## Literature Clusters

### Cluster 1: Market Research Methodology

This cluster establishes the professional reasoning standard against which AI outputs are evaluated.

| Author(s) | Year | Venue | Key Finding | Connection to This Extension |
| --- | --- | --- | --- | --- |
| Kohli and Jaworski | 1990 | Journal of Marketing | Market orientation requires systematic intelligence generation, dissemination, and responsiveness. Based on 62 field interviews. | Defines the standard: market claims must trace to identifiable market signals, not pattern-matched synthesis. |
| Jaworski and Kohli | 1993 | Journal of Marketing | Empirically linked market orientation to business performance, commitment, and esprit de corps. | Establishes the business case for reasoning quality in market research. |
| Griffin and Hauser | 1993 | Marketing Science | Voice of the Customer methodology. 20-30 interviews capture 90-95% of needs. Multiple analysts improve reliability. | Sets quantitative sufficiency standards for customer need claims. |
| Cooper | 1990-2025 | Multiple | Stage-Gate: evidence-based gates with escalating evidentiary requirements by investment stage. | Gate decisions require verifiable research quality. AI output at gate must meet the same standard. |
| Christensen | 2003 | The Innovator's Solution | Jobs-to-be-Done: reframes analysis around functional, social, and emotional progress customers seek. | Professional reasoning requires causal depth in motivation analysis, not surface-level pattern description. |
| Malhotra | 1993-present | Marketing Research (textbook) | Canonical process: problem definition, approach, design, collection, analysis, reporting. Each stage has quality criteria. | Defines the traceable analytical process that professional outputs must exhibit. |

**Gap**: These works define the professional standard but predate AI-generated market research. No methodology work addresses how to verify that AI outputs meet these established standards.

### Cluster 2: AI Performance on Creative and Analytical Business Tasks

This cluster establishes empirical findings on AI capabilities and limitations in tasks adjacent to market research.

| Author(s) | Year | Venue | Key Finding | Connection to This Extension |
| --- | --- | --- | --- | --- |
| Girotra, Meincke, Terwiesch, and Ulrich | 2023 | SSRN | GPT-4 generated business ideas faster and with higher average quality than MBA students. High variance: best ideas came from AI, but so did worst. | Variance in quality is the core problem verification must address. Average quality is misleading. |
| Dell'Acqua, McFowland, Mollick et al. | 2023 | HBS / Organization Science (2026) | Jagged frontier: AI improved BCG consultant performance inside capability boundary, worsened it outside. Boundary is invisible to users. | Critical finding. Market research users cannot self-detect when AI crosses from capable to failure zone. |
| Doshi and Hauser | 2024 | Science Advances | AI enhances individual creativity but reduces collective diversity of novel content. AI-assisted stories were more similar to each other. | Market research risk: AI analyses converge on similar conclusions, creating false consensus. |
| Brynjolfsson, Li, and Raymond | 2023 | NBER / QJE (2025) | AI assistant increased customer support productivity by 14% on average, 34% for novice workers, minimal for experienced workers. | AI helps juniors produce competent-looking output that may lack expert depth. Verification is the gap. |

**Gap**: These studies measure task completion and output quality, but none evaluate the reasoning process that produced the output. A market research output can score well on quality while containing inferential failures that only matter when the decision changes.

### Cluster 3: AI Reasoning Faithfulness and Reliability

This cluster documents the technical basis for why AI reasoning cannot be taken at face value.

| Author(s) | Year | Venue | Key Finding | Connection to This Extension |
| --- | --- | --- | --- | --- |
| Turpin, Michael, Perez, and Bowman | 2023 | NeurIPS 2023 | Chain-of-thought explanations systematically misrepresent the true reason for predictions. Biasing features caused accuracy drops up to 36%, never mentioned in explanations. | Stated reasoning in AI market research may not reflect actual inference process. Verification cannot rely on plausibility of stated reasoning alone. |
| Lanham et al. | 2023 | arXiv | Larger models produce less faithful chain-of-thought reasoning on most tasks. Faithfulness varies by task type. | More capable models may produce more convincing but less trustworthy market research reasoning. |
| Sharma, Tong, Korbak et al. | 2024 | ICLR 2024 | Five state-of-the-art AI assistants consistently exhibit sycophancy across tasks. RLHF training amplifies sycophantic tendencies. Both humans and preference models prefer sycophantic responses. | AI will confirm market hypotheses rather than test them. Sycophancy undermines research objectivity. |
| Wei et al. | 2022 | NeurIPS 2022 | Chain-of-thought prompting enables complex reasoning in large language models. Emergent ability at sufficient scale. | Establishes CoT as the mechanism through which AI produces multi-step market analysis. |
| Barez et al. | 2025 | arXiv | Survey on open problems in AI reasoning safety, including faithfulness, oversight, and alignment of reasoning processes. | Frames the broader research context: reasoning verification is an open safety problem. |

**Gap**: This literature documents the problem (unfaithful reasoning, sycophancy, scaling concerns) but does not provide domain-specific verification methods. The gap between "we know AI reasoning can be unfaithful" and "here is how to check AI reasoning in market research" remains unfilled.

### Cluster 4: AI Agent Architectures

This cluster provides technical context for how AI market research agents compound reasoning across multi-step workflows.

| Author(s) | Year | Venue | Key Finding | Connection to This Extension |
| --- | --- | --- | --- | --- |
| Yao et al. | 2023 | ICLR 2023 | ReAct: synergizing reasoning and acting in language models. Interleaving reasoning traces with action steps. | Multi-step reasoning in market research follows the ReAct pattern. Failures compound across steps. |
| Shinn et al. | 2023 | NeurIPS 2023 | Reflexion: language agents with verbal reinforcement learning. Self-reflection improves task performance. | Self-correction in AI agents may or may not catch reasoning failures. Verification must be external. |
| Park et al. | 2023 | UIST 2023 | Generative agents: interactive simulacra of human behavior. Demonstrated emergent social behaviors from LLM-based agents. | Provides context for multi-agent market research systems. Agent coordination introduces new failure modes. |

**Gap**: Agent architecture research focuses on task completion and capability. Reasoning quality assessment across multi-step agent workflows is not addressed.

### Cluster 5: Trust, Automation Bias, and Appropriate Reliance

This cluster from the existing repository literature provides the theoretical frame for why verification matters.

| Author(s) | Year | Venue | Key Finding | Connection to This Extension |
| --- | --- | --- | --- | --- |
| Lee and See | 2004 | Human Factors | Trust in automation develops through perceived performance, process, and purpose. Miscalibrated trust leads to misuse or disuse. | Verification framework is the mechanism for trust calibration in market research AI outputs. |
| Bansal et al. | 2021 | CHI | Appropriate reliance on AI requires understanding when to trust and when to override. Model explanations alone are insufficient. | Confirms that AI's own reasoning display cannot substitute for external verification. |
| Agrawal, Gans, and Goldfarb | 2018 | Prediction Machines | AI provides prediction; humans provide judgment. Separating the two is essential for appropriate delegation. | Market research combines prediction (trend identification, sizing) and judgment (need interpretation, concept evaluation). Verification must assess both. |

### Cluster 6: Hallucination Statistics and Business Impact

| Finding | Source | Year | Connection |
| --- | --- | --- | --- |
| 77% of businesses report concern about AI hallucinations | Industry surveys | 2024-2025 | Establishes practitioner awareness of the problem |
| 47% of enterprise AI users made at least one major decision based on hallucinated content | Industry surveys | 2024 | Demonstrates active business harm from unverified AI outputs |
| Knowledge workers spend 4.3 hours/week fact-checking AI outputs | Industry surveys | 2024 | Current verification is informal and time-consuming. A structured framework reduces verification cost. |
| OpenAI reasoning models (o3, o4-mini) hallucinated 33% and 48% on PersonQA benchmark | OpenAI evaluations | 2025 | Reasoning-optimized models may hallucinate more on factual benchmarks. Capability does not equal reliability. |
| User suggestions of incorrect answers can reduce LLM accuracy by up to 27% | arXiv:2411.15287 | 2024 | Sycophancy is measurably harmful to output accuracy. |

## The Specific Gap This Extension Fills

The literature establishes three well-documented facts:

1. **Professional market research reasoning has codified standards** (Cluster 1). There are established methods for what constitutes sufficient evidence, appropriate inference, calibrated confidence, and methodological rigor.

2. **AI systems produce market research outputs that appear professional but contain systematic reasoning failures** (Clusters 2, 3, 4). The failures are invisible to surface-level review, invisible to the AI's own stated reasoning, and amplified by sycophancy.

3. **Users cannot self-detect when AI reasoning quality falls below professional standards** (Clusters 2, 5, 6). The jagged frontier is invisible, automation bias is pervasive, and current fact-checking practices address factual accuracy but not reasoning quality.

**The unfilled gap**: No published framework operationalizes the professional market research standard (Cluster 1) as evaluation criteria applied to AI outputs exhibiting the failure modes documented in Clusters 2 and 3, in a form usable by practitioners who lack professional research training (the audience identified in Clusters 5 and 6).

This extension fills that gap by building a market-research-specific verification framework that connects established professional standards to the 25-type reasoning failure taxonomy through domain-specific verification checklists.

## Connection to Existing Repository Literature

| Existing Asset | Path | Relationship |
| --- | --- | --- |
| Reasoning trust landscape | `research/core/literature/reasoning-trust-landscape.md` | This document extends the 9-theme landscape with market-research-specific literature. Clusters 1, 2, and 6 are new additions. |
| Source quality hierarchy | `research/core/framework/reasoning-verification-source-quality.md` | The 5-level hierarchy is directly applicable. Market research requires domain calibration: trade publications (Level 3), analyst reports (Level 3-4), customer data (Level varies by methodology). |
| Reasoning failure taxonomy | `research/core/framework/reasoning-failure-taxonomy.md` | The 25 failure types serve as the classification instrument. This extension tests whether they are sufficient for market research or require domain-specific additions. |
| Cross-domain analysis | `research/core/domain-analysis/analysis.md` | The market research domain assessment (assist authority, weak-to-moderate evidence) is empirically tested by this extension. |
| Information structure extension | `research/extensions/information-structure/` | Market research is a concrete case of the information-structure thesis. The 7 information variables (acquisition cost, search cost, volume, velocity, verifiability, comparability, interpretive burden) can be assessed specifically for market research data. |
