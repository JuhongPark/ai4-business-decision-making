# Phase 21: Adaptive Governance Extension — Summary

## Status: research_complete
## Date: 2026-03-10

---

## Problem Addressed

Phases 00-20 produced a governance framework for AI business decision-making with strong durable principles but static recommendations. The research-practice temporal gap — where AI capabilities advance faster than governance research can conclude — creates a structural risk that recommendations become outdated before or shortly after publication.

---

## What This Phase Produced

### Document 1: Speed Gap Analysis

Comprehensive research on how the governance field is responding to the AI speed gap.

**Key findings:**
- Regulatory sandboxes (FCA, MAS, Korea, EU) provide controlled experimentation but operate on months-long cycles and focus on individual firms
- Responsible Scaling Policies (Anthropic ASL, OpenAI Preparedness, DeepMind FSF) are the most direct industry response — capability thresholds trigger governance obligations dynamically
- Continuous governance infrastructure (Google Model Cards, Microsoft RAI Standard, IBM FactSheets) embeds governance into development workflow but describes rather than constrains
- Living evidence methods (Cochrane, WHO/BMJ) are proven in concept but struggled with sustainability even in well-resourced healthcare settings
- Principle-based regulation (Singapore, NIST) survives capability shifts better than rule-based (EU AI Act) but provides less specific guidance
- Organizations with mature governance frameworks deploy AI 40% faster and achieve 30% better ROI — governance enables rather than impedes speed

**Structural gap identified:** No existing mechanism fully addresses business decision governance at the speed AI capabilities change. The existing research needed a dynamic layer between durable principles and specific recommendations.

### Document 2: Layer 2 — Transition Conditions

Defines measurable criteria for when AI authority can escalate or must regress.

**Three-layer model:**
- Layer 1 (Durable Principles): Update cycle years — established in Phases 00-20
- Layer 2 (Transition Conditions): Update cycle quarters — THIS DOCUMENT
- Layer 3 (Living Evidence): Update cycle continuous — next document

**Key constructs:**
- **Graduation criteria:** Specific, observable conditions for assist→recommend and recommend→automate transitions, defined per domain
- **Regression criteria:** Immediate triggers for authority reduction (no waiting for scheduled review)
- **Capability-governance coupling rule:** Capability improvement is necessary but not sufficient for escalation — governance, evidence, and monitoring must also be met
- **New capability integration protocol:** Distinguishes incremental improvements (flow through existing conditions) from modality shifts (require condition redesign)
- **Scoring sheet interaction:** Phase 16 scoring sheet sets the ceiling; graduation criteria determine the actual level

**Domain-specific thresholds defined for:**
- Operations (accuracy, exception rate, rollback time, telemetry quality)
- Finance (fairness validation, audit completeness, observation period, macro stability)
- Healthcare (clinical validation, safety record, clinician override, regulatory clearance)
- Investment (suitability validation, disclosure completeness, performance tracking)
- Strategy, Product, Marketing, Market Research (lighter-weight conditions)

### Document 3: Layer 3 — Living Evidence Protocol

Defines a continuous evidence maintenance system for keeping recommendations current.

**Key constructs:**
- **Living document designation:** Specifies which artifacts from Phases 00-20 become living documents with defined update cadence
- **Event-based triggers:** Capability changes, regulatory actions, incidents, academic publications, and benchmark results trigger evidence processing
- **Evidence processing protocol:** Five-step intake (source → tier → claim mapping → impact assessment → action routing)
- **Contradiction handling:** Classified as direct contradiction, scope limitation, or condition change, with resolution protocol
- **Version management:** Semantic versioning (major.minor.patch) with changelog requirements and snapshot preservation
- **Evidence source monitoring:** Structured monitoring across capability, regulatory, and deployment evidence categories

### Document 4: Industry Practice Survey

Comprehensive survey of how organizations actually implement AI governance in practice (2024-2026).

**Key findings:**

- **Big Tech diverges sharply:** Microsoft has the most documented governance (CRAO, layered safety stack, deployment gates). Meta disbanded its RAI team and automates 90% of risk assessments with AI. Apple governs through architecture (on-device processing) rather than organizational process.
- **Financial services leads maturity:** JPMorgan has multi-tiered governance with patented bias auditing. Goldman Sachs requires mandatory human reviewer for AI chatbot responses. BlackRock's Aladdin Copilot explicitly refuses to give investment advice — assist mode in practice.
- **Healthcare governance is regulation-driven:** ~75% of large health systems have AI governance committees. FDA PCCPs operationalize adaptive governance by allowing pre-approved AI updates without fresh regulatory approval.
- **Governance teams are small:** Average 9 people; 17% of organizations have only 1 person. Privacy officers absorb AI governance by default. Only 28% have formally defined oversight roles.
- **Governance enables speed:** Organizations with mature governance deploy AI 40% faster and achieve 30% better ROI. Yet 95% of GenAI pilots fail, primarily from data quality and technical maturity issues, not governance.
- **The framework's core distinction is visible in practice:** assist (BlackRock investment), recommend with human approval (Goldman chatbot), automate with guardrails (Stripe fraud detection) are all real deployment patterns.

**Critical gaps between framework and practice:**
- Governance capacity assumptions are too optimistic (most organizations lack dedicated teams)
- Meta's AI-automated governance challenges the assumption that human oversight must be operationally real
- Architecture-based governance (Apple) is underrepresented in the framework
- Agentic AI governance is urgent but barely exists (Singapore January 2026 is the first framework)
- US political oscillation on AI governance creates regulatory instability the framework does not address

### Document 5: Governance Trend Analysis

Tracks directional change in AI governance practice across 2023-2026.

**Key trends:**

- **CAIO role institutionalizing rapidly:** 11% (2023) → 26% (2025) → 40%+ projected (2026). More than half now report directly to CEO or board. Becoming the primary accountability anchor.
- **Governance becoming infrastructure, not policy:** AI governance platform market at $492M (2026), heading toward $1B (2030). Organizations deploying platforms are 3.4x more likely to achieve high governance effectiveness. Shift from "do we have a policy?" to "does our infrastructure enforce it?"
- **Agentic AI forcing governance redesign:** 74% plan agentic deployment but only 21% have governance ready. The shift from AI that predicts to AI that acts is the most disruptive governance challenge. Governance must now cover actions, permissions, tool access, and multi-step workflows.
- **Insurance and liability as governance drivers:** AI liability insurance market projected at $29.7B by 2033. D&O insurers scrutinizing AI governance during underwriting. Market-driven incentive operating faster than regulation.
- **Regulatory fragmentation increasing:** US federal-state divergence (deregulation vs 38 states passing ~100 AI measures); EU AI Act pragmatic timeline adjustments; global convergence on principles but divergence on technique.
- **Responsible AI restructuring, not disappearing:** Standalone RAI teams declining (Meta disbanded, Microsoft offloaded training team). RAI concerns being embedded into product engineering and compliance. RAI research publications still growing (+28.8%).
- **Foundation model governance diverging from traditional ML:** Non-deterministic outputs, adversarial testing, hallucination monitoring, continuous prompt changes require fundamentally different governance approaches.

**Priority framework updates identified:**
1. Agentic AI governance extension (highest priority)
2. Automated governance position (when can governance itself be automated?)
3. Insurance/liability integration as governance forcing function
4. Supply chain governance for third-party model risk
5. Regulatory resilience design (framework should work across political cycles)

---

## How This Phase Extends the Research

| Phases 00-20 | Phase 21 Addition |
|--------------|-------------------|
| "AI authority should be adaptive" (principle) | Defines measurable conditions for adaptation |
| "Finance should default to assist" (recommendation) | Specifies graduation criteria for moving beyond assist |
| Evidence register as static list | Evidence register as living document with intake protocol |
| Domain recommendation table as fixed output | Domain recommendation table as versioned living artifact |
| Framework validated at point in time | Framework designed for continuous validation |
| Normative framework (what should be done) | Industry practice survey (what is actually done) |
| Point-in-time assessment | Trend analysis showing directional change |

---

## Relationship to Existing Phases

```
Phases 00-07: Foundation (question, literature, framework, validation)
Phases 08-13: Expansion (evidence tiers, domain analysis, scenarios)
Phases 15-19: Maturation (taxonomy, publication prep, submission ready)
Phase 20:     Implementation (workflow, infrastructure, organization)
Phase 21:     Adaptation (speed gap, transition conditions, living evidence, industry practice)
```

Phase 21 does not replace earlier phases. It adds a dynamic governance layer that keeps the framework relevant as AI capabilities, regulatory landscapes, and deployment practices evolve.

---

## Limitations

1. **Threshold calibration:** Domain-specific thresholds are starting points requiring organizational calibration
2. **Resource requirements:** Living evidence protocol requires sustained commitment that may be difficult to maintain
3. **Agentic AI gap:** Transition conditions still assume discrete workflow stages; agentic AI governance remains an open extension
4. **Untested in practice:** The living evidence approach has not been substantively tested in AI governance contexts
5. **No competitive pressure exception:** Framework explicitly rejects competitive pressure as an escalation justification, which may face organizational resistance

---

## Next Steps (Not Yet Executed)

1. **Agentic AI governance extension:** Adapt transition conditions for continuous AI workflows without discrete human checkpoints
2. **Post-LLM case updates:** Add foundation model era cases to replace or supplement pre-LLM case base
3. **Pilot the living evidence protocol:** Test the evidence intake and update cycle on a small set of domains
4. **Cross-framework mapping:** Map transition conditions to EU AI Act requirements, NIST AI RMF functions, and Singapore governance framework
5. **Lightweight governance track:** Design a minimum viable governance model for resource-constrained organizations (addressing the finding that 17% have only 1 governance person)
6. **AI-governed-AI evaluation:** Assess Meta's model of automating governance itself — under what conditions is this acceptable, and where must human oversight remain?
7. **Governance-by-architecture analysis:** Evaluate Apple's approach (on-device processing, data minimization) as a complementary governance mechanism
