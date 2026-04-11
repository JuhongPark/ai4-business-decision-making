# Cross-Extension Synthesis: How the Research Tracks Connect

status: synthesis document (foundational — see practical-solution-synthesis.md for the evolved 3-layer intervention)
date_created: 2026-04-11
purpose: tie the five extension tracks and three standalone memos into a unified research narrative that advances the core thesis beyond the original submission
note: this document maps the theoretical architecture (Why → What → How → Test → Deploy). The research has since converged on a minimum viable governance approach — 3 actionable layers distilled from this architecture. See research/extensions/market-research/practical-solution-synthesis.md for the practical contribution.

## The Core Thesis

The original research established:

- **71 documented AI governance failures** (2018-2026) reveal that most failures are caused by delegation calibration failure, not technical incapacity.
- **A 6-dimensional adaptive framework** evaluates when AI should assist, recommend, or automate, using domain, decision structure, risk level, scenario condition, evidence strength, and governance readiness.
- **A reasoning failure taxonomy** (25 types across 6 categories) classifies how AI reasoning can fail in business contexts.
- **Verification protocols** (source quality, inferential validity, normative assessment, confidence calibration) provide methods for detecting reasoning failures.

## How Each Extension Advances the Thesis

### Track 1: Information Structure — Why the Problem Exists

**Contribution**: Explains the structural conditions that make delegation calibration necessary.

Information technology repeatedly compresses access advantages while increasing the value of higher-order capabilities. Each "information shock" (internet, search, cloud, social media, AI) democratized a layer of the information value chain. LLMs are the first shock to democratize interpretation itself — producing analyses that read like expert output.

**Connection to core**: The information structure analysis provides the economic and structural basis for the delegation framework. Organizations need delegation calibration because AI has commoditized analysis production without commoditizing analysis verification.

**Key insight**: Expert intermediation persists not because AI cannot produce analysis, but because verifying AI analysis requires the same expertise AI was meant to replace.

### Track 2: Adaptive Governance — How to Stay Current

**Contribution**: Provides the temporal dimension — how governance frameworks remain valid as AI capabilities change.

The three-layer framework:
- **Layer 1**: Static rules for current capability levels
- **Layer 2**: Transition conditions that signal when rules need updating
- **Layer 3**: Living evidence protocol for continuous governance evolution

**Connection to core**: The delegation framework scores are valid for a point in time. Adaptive governance provides the mechanism for updating those scores as AI capabilities improve, new failure patterns emerge, and regulatory requirements change.

**Key insight**: Governance that cannot evolve becomes either too permissive (allowing failures) or too restrictive (blocking value). The living evidence protocol is the mechanism that prevents both failure modes.

### Track 3: Business Alignment — Why This Is an Alignment Problem

**Contribution**: Connects delegation calibration to the AI safety and alignment research community.

The 71-incident reanalysis through alignment failure modes shows:
- Specification gaming (Krakovna et al., 2020) maps to reward hacking incidents
- Distributional shift (Amodei et al., 2016) maps to deployment-condition mismatch
- Scalable oversight failure maps to nominal human-in-the-loop that was ineffective
- Fluent hallucination maps to misinformation-category LLM failures

**Connection to core**: The delegation framework is the operational layer that translates technical alignment confidence into deployment decisions. Even a technically aligned model requires delegation calibration because alignment verification has limits.

**Key insight**: Delegation calibration and technical alignment are not separate problems — they are two faces of the same problem. Technical alignment determines whether the system can be trusted in principle. Delegation calibration determines whether it should be trusted in practice.

### Track 4: Market Research — The First Domain Test

**Contribution**: Provides the first domain-specific empirical test of the reasoning verification framework.

Market research was selected because it combines low verifiability, high interpretive burden, temporal sensitivity, and sycophancy vulnerability — making it both the hardest test domain and the domain where verification matters most.

The task decomposition reveals:
- 18 discrete reasoning tasks across 6 stages
- 56% of tasks require ASSIST-level authority after override rules
- No task qualifies for automation
- Sycophantic failures in customer need extraction and concept generation are the highest-risk, lowest-detectability hot zones
- Calibration failures in market sizing produce false precision that mimics analytical rigor

**Connection to core**: The market research extension tests whether the 25-type taxonomy and 4-method verification framework are sufficient for a specific domain or require domain-specific adaptation. It produces practitioner-facing verification tools that bridge the gap between analytical framework and daily practice.

**Key insight**: The professional standard required to evaluate AI market research is the same professional standard the AI was meant to augment. Verification does not eliminate expert judgment — it redirects it from production to certification.

### Track 5: Three-Part Study — Organizational Implementation

**Contribution**: Translates the framework into implementation guidance across three organizational dimensions.

- **Part 1 (Workflow)**: How to embed verification into existing decision-making workflows
- **Part 2 (Infrastructure)**: What technical and institutional infrastructure supports delegation calibration
- **Part 3 (Organization)**: How organizational roles, incentives, and culture must adapt

**Connection to core**: The delegation framework describes what authority levels to assign. The three-part study describes how to operationalize those assignments within real organizations.

**Status**: Draft. Depends on findings from other tracks to provide empirically grounded recommendations.

### Standalone Memos

| Memo | Contribution |
| --- | --- |
| delegation-as-alignment.md | Articulates the core theoretical argument connecting delegation calibration to alignment |
| interpretability-bridge.md | Connects the evidence strength ceiling to mechanistic interpretability research |
| alignment-literature-bridge.md | Maps the incident taxonomy to alignment failure mode categories |

## The Unified Narrative

Reading the extensions in sequence produces a unified argument:

```
Information Structure → Delegation Framework → Reasoning Verification → Domain Application → Organizational Implementation
     (why)                  (what)                  (how)                 (test)                 (deploy)
```

1. **Why** (Information Structure): Information technology democratizes access but shifts scarcity to interpretation. LLMs democratize interpretation but create meta-interpretive burden — the need to verify AI-generated analysis.

2. **What** (Delegation Framework + Business Alignment): The 6-dimensional framework determines when AI should assist, recommend, or automate. This is an alignment problem: the framework is the operational layer translating technical alignment confidence into deployment decisions.

3. **How** (Reasoning Verification + Interpretability Bridge): The 25-type taxonomy and 4-method verification protocol provide structured methods for assessing AI reasoning quality. Evidence strength depends on interpretability. Without mechanistic understanding, evidence strength has a ceiling.

4. **Test** (Market Research): The market research extension is the first empirical test of the verification framework in a specific domain. It reveals that 56% of tasks require human retention of authority, sycophancy is the most prevalent and least detected failure category, and the professional standard for verification is the same expertise AI was supposed to augment.

5. **Deploy** (Three-Part Study + Adaptive Governance): Implementation requires workflow changes, infrastructure investment, and organizational adaptation. Governance must evolve continuously through the living evidence protocol as AI capabilities change.

## Open Research Questions Across Tracks

| Question | Primary Track | Supporting Tracks |
| --- | --- | --- |
| Can interpretability methods quantify evidence strength objectively? | Interpretability bridge | Delegation framework, Market research |
| Do failure patterns transfer across domains? | Market research | Business alignment, Information structure |
| How should authority levels adjust dynamically in real-time? | Adaptive governance | Delegation framework, Three-part study |
| What is the formal relationship between interpretability depth and maximum safe authority? | Interpretability bridge | Business alignment |
| How do oversight capacity constraints affect the framework? | Three-part study | Adaptive governance |
| Does verification cost make the framework impractical for SMEs? | Market research | Three-part study |
| Can the living evidence protocol be automated? | Adaptive governance | Market research |
| How does cross-cultural variation affect delegation calibration? | Information structure | Business alignment |

## Research Portfolio Status

| Component | Status | Contribution Locked? |
| --- | --- | --- |
| Core framework (6-dimensional) | Frozen v1 | Yes |
| 71-incident analysis | Frozen v1 | Yes |
| Reasoning failure taxonomy | Frozen v1 | Yes |
| Verification protocols | Frozen v1 | Yes |
| Information structure | Paused (~60%) | Core thesis locked; integration with verification pending |
| Adaptive governance | Complete | Yes |
| Business alignment | Draft (~40%) | Incident mapping locked; synthesis pending |
| Market research | Active (Phase 2 complete) | Phase 1-2 deliverables complete; Phases 3-5 pending |
| Three-part study | Draft (~25%) | Depends on other track completion |
| Cross-extension synthesis | This document | First version |
| Info-structure + verification integration | Complete | New contribution |
