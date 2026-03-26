# In-Text Citation Map

status: completed
purpose: Map each major claim in the thinktank report to its evidence source and strength tier.

## How to Use

This document supplements the thinktank report (submission_ready_v1) by providing paragraph-level citation mapping. Each entry identifies the report section, the claim made, the supporting source, and the evidence tier.

## Citation Map

### Introduction and Framing

| Claim | Source | Evidence Tier |
| --- | --- | --- |
| AI authority should be adaptive, not fixed | Agrawal, Gans, Goldfarb (prediction-judgment framework) | strong: conceptual literature |
| Suitability depends on decision structure, evidence quality, downside risk, and governance burden | NIST AI RMF; OECD AI Principles | strong: regulatory framework |
| Same domain may tolerate different autonomy under different conditions | scenario-based research design (internal) | design logic |

### Analytical Framework

| Claim | Source | Evidence Tier |
| --- | --- | --- |
| Three AI roles (assist, recommend, automate with guardrails) are the right unit of analysis | Jarrahi 2018 (human-AI complementarity) | strong: conceptual organizational research |
| Six-part category system captures the relevant decision variables | Agrawal et al. (prediction framing) + NIST AI RMF (governance dimensions) | strong: combined conceptual and regulatory |

### Operations Findings

| Claim | Source | Evidence Tier |
| --- | --- | --- |
| Operations is the strongest automation candidate | UPS ORION materials (routing optimization) | moderate: official company materials |
| Automate-with-guardrails is defensible for repeated, measurable routing decisions | UPS ORION; general operations research | moderate: design logic |
| Stress conditions require stronger human override | scenario analysis (internal) + Brynjolfsson, Hitt, Kim (organizational complements) | moderate to strong |
| Edge cases with degraded data justify fallback to assist | NIST AI RMF (risk management); scenario logic | strong: regulatory framework |

### Finance Findings

| Claim | Source | Evidence Tier |
| --- | --- | --- |
| AI assist and tightly governed recommend improve consistency in underwriting | CFPB Upstart materials; HMDA data context | strong to moderate: regulator records + firm materials |
| Fairness exposure and macro uncertainty increase under stress | CFPB fair lending guidance; Federal Reserve stress test scenarios | strong: regulatory |
| Drift and subgroup anomalies trigger fallback to assist | EEOC AI adverse impact guidance; NIST AI RMF | strong: regulatory |
| Model-risk becomes more salient under adverse macro conditions | Federal Reserve SR 11-7 (model risk management) | strong: regulatory |

### Healthcare Findings

| Claim | Source | Evidence Tier |
| --- | --- | --- |
| Healthcare has the strongest governance burden | FDA AI in SaMD materials | strong: regulatory device guidance |
| AI can support triage and clinical prioritization under routine conditions | FDA SaMD framework; clinical decision support literature | strong: regulatory |
| Edge cases with incomplete information justify clinician-led judgment | FDA post-market surveillance requirements | strong: regulatory |
| Surge conditions justify stronger recommendation support, not automation | scenario analysis + FDA framework | strong: combined regulatory and design logic |

### Human-AI Complementarity (MIT Research)

| Claim | Source | Evidence Tier |
| --- | --- | --- |
| Human-AI combinations are not automatically better than best standalone performer | Vaccaro, Almaatouq et al. 2024 (MIT CCI meta-analysis) | strong: empirical research |
| Performance gains depend on organizational complements, not model capability alone | Brynjolfsson, Li, Raymond (generative AI in customer support) | strong: empirical research |
| Algorithm design changes both candidate quality and diversity | Li (hiring research, MIT Sloan) | strong: empirical research |
| Transparency does not automatically solve adoption problems | Kellogg (organizational algorithm use, MIT Sloan) | strong: empirical research |

### Cross-Domain Comparison

| Claim | Source | Evidence Tier |
| --- | --- | --- |
| Operations and marketing are strongest bounded automation candidates | UPS ORION; Netflix technical blog | moderate: company materials |
| Finance, healthcare, and investment require governance-first deployment | CFPB; FDA; SEC robo-adviser bulletin | strong: regulatory |
| Strategy, product, and market research are augmentation domains | Productboard; Qualtrics materials | moderate: vendor materials |

### Governance and Restriction Logic

| Claim | Source | Evidence Tier |
| --- | --- | --- |
| Seven-step decision sequence is a conservative authority-assignment rule | NIST AI RMF + OECD AI Principles + internal taxonomy | strong: regulatory + design logic |
| Fallback planning is a managerial obligation | NIST AI RMF (governance function); Dietvorst et al. (algorithm aversion) | strong: regulatory + experimental |
| High-impact claims should rely on regulator-backed or peer-reviewed evidence | evidence-tier methodology (internal) | design logic |

### Taxonomy-Based Usage Rules

| Rule | Primary Support | Evidence Tier |
| --- | --- | --- |
| Rule 1: structured + low-risk + baseline can justify recommend or automate | Agrawal et al.; UPS ORION example | strong to moderate |
| Rule 2: semi-structured + medium-risk usually justify assist or recommend | Jarrahi 2018; scenario analysis | strong: conceptual |
| Rule 3: high-risk defaults to assist or tightly governed recommend | FDA SaMD; CFPB; EEOC guidance | strong: regulatory |
| Rule 4: stress increases support value but not automation justification | scenario analysis; Brynjolfsson et al. | strong: empirical + design |
| Rule 5: edge cases trigger fallback toward assist | NIST AI RMF; all domain scenarios | strong: regulatory |
| Rule 6: weak evidence reduces allowable autonomy | evidence-tier methodology; NIST AI RMF | strong: regulatory + design |
| Rule 7: strong evidence is necessary but not sufficient in high-risk domains | FDA SaMD; CFPB Upstart review | strong: regulatory |

## Evidence Tier Definitions

| Tier | Description | Example Source Types |
| --- | --- | --- |
| strong | regulatory frameworks, peer-reviewed empirical research, official government guidance | NIST, FDA, CFPB, EEOC, SEC, peer-reviewed journals |
| strong to moderate | regulator records combined with firm-level materials | CFPB Upstart review, Fed stress scenarios |
| moderate | official company materials, vendor documentation, technical blogs | UPS ORION, Netflix, Productboard |
| design logic | internal analytical constructs supported by conceptual reasoning | scenario design, taxonomy, evidence-tier method |
