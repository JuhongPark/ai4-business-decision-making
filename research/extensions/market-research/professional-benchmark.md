# Professional Benchmark: Market Research Reasoning Quality

status: Phase 1 deliverable
date_created: 2026-04-11
purpose: codify what professional-grade market research reasoning looks like, establishing the evaluation baseline against which AI market research outputs are assessed

## Why a Professional Benchmark Is Needed

AI systems can now produce market research outputs that read like professional analysis. But reading like professional analysis and being professional analysis are different things. To evaluate AI reasoning quality, there must be an explicit standard defining what "professional-grade" means at each stage of the market research workflow.

The professional standard for market research reasoning is drawn from five established methodological traditions, each contributing specific reasoning requirements that can be operationalized as verification criteria.

## Methodological Foundations

### 1. Systematic Intelligence Generation (Kohli and Jaworski, 1990)

Market orientation requires the organization-wide generation, dissemination, and responsiveness to market intelligence. Professional market research is not the assembly of plausible-sounding narratives; it is the systematic collection and interpretation of actual market signals.

**Reasoning standard**: Every market claim must trace to an identifiable market signal (customer behavior, competitive action, regulatory change, economic indicator). Claims that cannot be traced to a specific signal fail the intelligence generation standard.

**AI failure mode**: AI systems generate plausible market narratives from training data patterns rather than from current market signals. The output reads as intelligence but is pattern-matched synthesis, not evidence-grounded analysis.

### 2. Quantitative Sufficiency in Customer Research (Griffin and Hauser, 1993)

The Voice of the Customer methodology established quantitative standards for what constitutes sufficient evidence in customer needs research. Griffin and Hauser demonstrated that 20-30 in-depth interviews typically capture 90-95% of customer needs in a given segment, and that multiple analysts reading the same transcripts improve need identification reliability.

**Reasoning standard**: Customer need claims must be supported by evidence of sufficient depth and breadth. Claims about "what customers want" require identifiable evidence sources with known sample characteristics. The confidence in a customer need claim should be proportional to the evidence base.

**AI failure mode**: AI systems generate customer need statements that sound specific and grounded but derive from training data generalization rather than from identifiable research with known methodology. The claims carry implicit confidence that exceeds what the evidence base warrants.

### 3. Causal Depth in Motivation Analysis (Christensen, Jobs-to-be-Done)

Jobs-to-be-Done theory reframes market research around the functional, social, and emotional progress customers seek. Professional motivation analysis requires causal understanding of why customers make choices, not just descriptive patterns of what they choose.

**Reasoning standard**: Market research reasoning must demonstrate causal depth — explaining why a pattern exists, not just that it exists. Professional analysis distinguishes between correlation (customers who buy X also buy Y), association (customers in segment A prefer feature B), and causation (customers hire product X because it resolves tension Y in context Z).

**AI failure mode**: AI systems produce surface-level pattern descriptions that mimic causal analysis. "Customers prefer sustainable packaging because they value environmental responsibility" reads as causal but may be a restated correlation with no evidence of causal mechanism. This is the inferential failure the taxonomy calls "false causation."

### 4. Evidence-Based Gate Decisions (Cooper, Stage-Gate)

The Stage-Gate process requires evidence-based evaluation at each decision gate. Market research used at gate decisions must meet evidentiary standards that justify resource commitment. The standard escalates with investment size: early gates accept directional evidence; later gates require quantified, validated evidence.

**Reasoning standard**: The confidence level of market research claims must match the decision stage. Directional claims are acceptable for early exploration. Claims supporting major investment decisions require quantified evidence with known methodology, identified assumptions, and sensitivity analysis.

**AI failure mode**: AI systems produce market research with uniform confidence regardless of decision stage. An early-stage opportunity scan and a pre-launch market validation receive the same tone of analytical certainty. This is the calibration failure the taxonomy calls "uniform confidence."

### 5. Systematic Research Process (Malhotra, Marketing Research)

Malhotra's canonical process defines market research as a sequence of methodologically distinct stages: problem definition, approach development, research design, data collection, analysis, and reporting. Each stage has defined quality criteria and common pitfalls.

**Reasoning standard**: Professional market research follows a traceable analytical process. The reader can identify what question was asked, what method was used to answer it, what data was collected, how it was analyzed, and what conclusions were drawn. Methodological choices are explicit, not implicit.

**AI failure mode**: AI systems produce market research that jumps from question to conclusion without a visible analytical process. The methodology is implied rather than stated, and the reader cannot assess whether the analytical approach was appropriate for the question. This is the structural failure of "scope mismatch" — the analytical method does not match the question's requirements.

## The Professional Reasoning Standard by Market Research Stage

### Stage 1: Environmental Scanning

**Professional standard**: Identify relevant signals from multiple independent sources. Distinguish signals from noise. Assess source reliability explicitly. Acknowledge coverage gaps.

| Reasoning Operation | Professional Requirement | Verification Question |
| --- | --- | --- |
| Source identification | Multiple independent sources covering different perspectives | Are sources from at least two independent categories (e.g., industry data + customer data + regulatory data)? |
| Relevance filtering | Explicit criteria for including and excluding signals | Can the analyst explain why certain signals were included and others excluded? |
| Signal-noise discrimination | Distinguish trends from anomalies with stated reasoning | Is there evidence that apparent patterns were tested against alternative explanations? |
| Coverage assessment | Acknowledge what the scan does not cover | Does the analysis identify its blind spots? |

### Stage 2: Trend Identification

**Professional standard**: Identify patterns with temporal evidence. Distinguish durable trends from temporary shifts. Estimate magnitude with appropriate uncertainty. Cite comparable historical patterns when using analogical reasoning.

| Reasoning Operation | Professional Requirement | Verification Question |
| --- | --- | --- |
| Pattern recognition | Identify trends with at least three data points over time | Is the trend supported by temporal evidence, or is it a single observation projected forward? |
| Temporal analysis | Distinguish acceleration, deceleration, and cyclical patterns | Does the analysis account for the trend's rate of change, not just its direction? |
| Magnitude estimation | Provide ranges rather than point estimates for uncertain trends | Are trend magnitude claims expressed as ranges with stated assumptions? |
| Historical comparison | Use analogies explicitly with acknowledged differences | When historical patterns are cited, are material differences from the current situation identified? |

### Stage 3: Customer Need Extraction

**Professional standard**: Ground need claims in identifiable evidence. Distinguish stated needs from latent needs and label the inference type. Apply the JTBD lens: what progress is the customer trying to make? Acknowledge the interpretive gap between raw data and need statements.

| Reasoning Operation | Professional Requirement | Verification Question |
| --- | --- | --- |
| Evidence grounding | Trace each need to identifiable customer evidence | Can each need statement be linked to specific customer behavior, feedback, or research? |
| Need hierarchy | Distinguish functional, social, and emotional dimensions | Does the analysis identify what type of need is being addressed? |
| Latent need inference | Label abductive inferences explicitly | When a latent need is proposed, is it labeled as an inference rather than presented as an observation? |
| Interpretive transparency | Acknowledge the gap between data and interpretation | Does the analysis distinguish between what customers said and what the analyst interprets they mean? |

### Stage 4: Competitive Mapping

**Professional standard**: Use current sources with known recency. Distinguish capability from strategy. Assess competitive moves through multiple lenses (financial, product, market position). Acknowledge information gaps about competitors.

| Reasoning Operation | Professional Requirement | Verification Question |
| --- | --- | --- |
| Source recency | Date all competitive information and flag items older than 12 months | Are competitive claims dated, and are stale claims flagged? |
| Capability vs. strategy | Distinguish what competitors can do from what they intend to do | Does the analysis separate demonstrated capabilities from inferred strategic intent? |
| Multi-lens analysis | Assess competitors from financial, product, and market position perspectives | Does the competitive map cover more than one dimension of comparison? |
| Information gaps | Acknowledge what is unknown about competitors | Does the analysis explicitly state what competitive information is missing? |

### Stage 5: Market Sizing and Opportunity Assessment

**Professional standard**: Make assumptions explicit and testable. Distinguish top-down and bottom-up estimates and triangulate. Express uncertainty proportional to the estimation method. Conduct sensitivity analysis on key assumptions.

| Reasoning Operation | Professional Requirement | Verification Question |
| --- | --- | --- |
| Assumption explicitness | List every assumption underlying the estimate | Can the reader identify all assumptions required for the estimate to hold? |
| Methodological transparency | State whether estimate is top-down, bottom-up, or analogical | Is the estimation method stated and appropriate for the question? |
| Uncertainty expression | Provide ranges with probability-weighted scenarios | Does the estimate include a range, or is it a single point presented as definitive? |
| Sensitivity analysis | Identify which assumptions drive the largest variance | Does the analysis identify which assumptions, if wrong, would change the conclusion most? |

### Stage 6: Concept Generation and Screening

**Professional standard**: Generate concepts that address identified needs with traceable logic. Evaluate feasibility with explicit criteria. Test concepts against disconfirming evidence. Resist framing effects from the originating hypothesis.

| Reasoning Operation | Professional Requirement | Verification Question |
| --- | --- | --- |
| Need-concept traceability | Each concept addresses a specific identified need | Can each concept be traced to a documented customer need? |
| Feasibility criteria | Evaluate concepts against stated technical, market, and financial criteria | Are the screening criteria explicit, or does the evaluation rely on implicit judgment? |
| Disconfirmation testing | Actively seek reasons each concept might fail | Does the analysis include reasons the concept might not work? |
| Framing resistance | Evaluate concepts independently of the initial hypothesis | Is there evidence that concepts were evaluated on their merits, not on their alignment with a prior belief? |

## Composite Professional Standard

A professional market research output meets the following composite criteria:

1. **Source grounding**: Every substantive claim traces to an identifiable source with known quality level.
2. **Methodological transparency**: The analytical method is stated, appropriate for the question, and traceable in the output.
3. **Calibrated confidence**: Claim certainty matches evidence strength. Directional claims use hedged language; quantified claims include ranges and assumptions.
4. **Causal depth**: Causal claims are distinguished from correlational claims and supported by evidence of mechanism.
5. **Temporal awareness**: Time-sensitive claims are dated. Trend claims include temporal evidence. Competitive intelligence is recency-checked.
6. **Interpretive honesty**: The gap between evidence and interpretation is acknowledged. Latent need inferences are labeled. Coverage gaps are stated.
7. **Disconfirmation discipline**: The analysis includes counterfactual reasoning. Alternative explanations are considered. Framing effects are resisted.

## Connection to the Reasoning Failure Taxonomy

Each element of the composite professional standard maps to specific failure types in the 25-type taxonomy:

| Professional Standard | Violated By (Taxonomy Failure Types) |
| --- | --- |
| Source grounding | Fabricated sources, Misrepresented sources, Inadequate source quality, Selection bias in sources |
| Methodological transparency | Scope mismatch, Circular reasoning |
| Calibrated confidence | Overconfidence, False precision, Certainty laundering, Uniform confidence |
| Causal depth | Non sequitur, False causation, Overgeneralization |
| Temporal awareness | Outdated sources, Temporal confusion |
| Interpretive honesty | Missing counterfactual, Anchoring on irrelevant precedent, Composition fallacy |
| Disconfirmation discipline | Confirmation bias amplification, Question-shaped answers, Progressive sycophancy, Audience-optimized reasoning |

This mapping establishes a direct analytical path from the professional standard to the taxonomy, enabling systematic verification of AI market research outputs against codified professional requirements.
