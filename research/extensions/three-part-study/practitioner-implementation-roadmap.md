# Practitioner Implementation Roadmap: From Framework to Organizational Practice

status: draft
date_created: 2026-04-11
purpose: translate the 6-dimensional delegation framework, reasoning verification protocols, and domain-specific findings into actionable implementation guidance for organizations deploying AI in business decisions

## Who This Is For

This roadmap is for organizations that:
- Use AI systems for business analysis, recommendations, or decision support
- Lack a structured method for determining appropriate AI authority levels
- Want to verify AI reasoning quality before acting on AI-generated analysis
- Need to implement governance that scales across teams and use cases

It is designed for three audiences:
1. **Executive leaders** setting AI governance policy
2. **Operational managers** embedding AI in team workflows
3. **Individual practitioners** evaluating AI outputs in their daily work

## Implementation Stages

### Stage 1: Assessment (Weeks 1-4)

**Goal**: Understand where AI is currently used and at what de facto authority levels.

#### 1.1 AI Decision Inventory

Map every use of AI in decision-making across the organization. For each use case, document:

| Field | Description |
| --- | --- |
| Decision type | What decision does the AI inform? |
| Current authority | Is AI assisting, recommending, or automating? |
| Formal authority | What authority was formally assigned? |
| Gap | Does actual authority exceed formal authority? |
| Domain | Which of the 8 domains applies? |
| Decision structure | Unstructured, semi-structured, or structured? |
| Risk level | Low, medium, or high? |
| Frequency | How often is this decision made? |
| Who reviews | Who reviews AI output before acting? |
| Review method | How do they review it? (Formal checklist, quick scan, no review) |

**Critical finding to look for**: The gap between formal authority and actual authority. Research shows that 66% of employees accept AI output without evaluation, meaning "assist" and "recommend" modes often collapse into de facto "automate" in practice.

#### 1.2 Delegation Framework Scoring

For each use case identified in 1.1, apply the 6-dimensional scoring model:

1. Score each dimension 1-3
2. Sum to get total score (5-15)
3. Map to authority level (5-8: ASSIST, 9-11: RECOMMEND, 12-15: AUTOMATE WITH GUARDRAILS)
4. Apply override rules:
   - High risk + weak governance → cap at ASSIST
   - Edge-case scenario → cap at ASSIST
   - Weak evidence in consequential decision → reduce one level

**Output**: A scored inventory showing recommended vs. actual authority levels for every AI use case.

#### 1.3 Gap Analysis

Compare recommended authority levels with actual authority levels. Classify gaps:

| Gap Type | Description | Action Required |
| --- | --- | --- |
| Authority excess | Actual authority exceeds recommended level | Immediate: add verification gates or reduce authority |
| Verification gap | Authority is appropriate but no verification process exists | Priority: implement verification protocol |
| Governance gap | Authority is appropriate but governance infrastructure is weak | Build: governance readiness improvement plan |
| No gap | Authority, verification, and governance are aligned | Monitor: maintain current state |

### Stage 2: Verification Infrastructure (Weeks 4-8)

**Goal**: Implement structured verification for high-priority use cases.

#### 2.1 Verification Protocol Selection

For each use case requiring verification (from the gap analysis), select the appropriate verification methods:

| Decision Type | Primary Verification | Secondary Verification |
| --- | --- | --- |
| Data-driven analysis (market sizing, trend analysis) | Confidence calibration | Source quality assessment |
| Strategic recommendations | Inferential validity | Normative assessment |
| Customer-facing content | Source quality | Normative assessment |
| Risk-sensitive decisions | All four methods | Weakest-link integration |
| Creative/ideation tasks | Sycophancy check + inferential validity | Confidence calibration |

#### 2.2 Verification Checklists

Create domain-specific verification checklists adapted from the general protocol. Each checklist should:

1. List the specific verification questions for that decision type
2. Define what "pass" and "fail" look like for each question
3. Estimate the time required for verification
4. Identify who should perform the verification (role and skill requirements)

**Template structure** (adapted from the market research verification work):

```
Decision: [type]
AI authority level: [assist/recommend/automate]
Verification method: [source quality/inferential/normative/calibration]

Check 1: [specific verification question]
  Pass: [what a satisfactory answer looks like]
  Fail: [what triggers escalation]
  Time: [estimated minutes]

Check 2: ...
```

#### 2.3 Escalation Paths

Define what happens when verification identifies a failure:

| Failure Severity | Action | Timeline |
| --- | --- | --- |
| Critical (could cause material harm) | Stop use. Escalate to governance lead. Document incident. | Immediate |
| High (could cause significant error) | Override AI recommendation. Document failure for taxonomy. Review authority level. | Same day |
| Moderate (quality below standard but not harmful) | Add human correction. Flag for pattern monitoring. | Within review cycle |
| Low (minor quality issue) | Note in feedback log. No workflow change. | At convenience |

### Stage 3: Organizational Embedding (Weeks 8-16)

**Goal**: Make verification a standard part of how the organization uses AI.

#### 3.1 Role Definitions

Define who is responsible for what:

| Role | Responsibility | Required Competence |
| --- | --- | --- |
| AI user | Apply verification checklist before acting on AI output | Domain expertise + verification training |
| Team lead | Review verification logs. Identify patterns. Adjust authority levels. | Domain expertise + framework understanding |
| AI governance lead | Maintain scoring inventory. Update verification checklists. Report to leadership. | Framework expertise + cross-domain view |
| Executive sponsor | Set governance policy. Resource the verification infrastructure. | Strategic understanding of AI risk/value |

#### 3.2 Training Program

Train staff on the verification framework. Training should cover:

1. **Why verification matters** (30 minutes): The 71-incident evidence base. Why AI output cannot be taken at face value. The jagged frontier (Dell'Acqua et al., 2023).
2. **How to use the scoring model** (60 minutes): 6 dimensions, scoring, override rules, authority levels.
3. **How to apply verification checklists** (90 minutes): Hands-on practice with domain-specific checklists. Real examples of AI output with and without reasoning failures.
4. **How to escalate** (30 minutes): When to flag, who to notify, how to document.

#### 3.3 Feedback Loop

Implement a feedback mechanism:

- **Incident log**: Document every instance where verification catches a significant AI reasoning failure. Classify using the 25-type taxonomy.
- **Pattern analysis**: Monthly review of incident log for failure patterns. Are certain failure types increasing? Are specific use cases generating more failures?
- **Authority adjustment**: Quarterly review of delegation scores using accumulated evidence. Apply the adaptive governance living evidence protocol.
- **Checklist refinement**: Update verification checklists based on observed failure patterns.

### Stage 4: Continuous Governance (Ongoing)

**Goal**: Keep the governance framework current as AI capabilities change.

Apply the adaptive governance three-layer model:

- **Layer 1 (Static rules)**: Current delegation scores and authority assignments. Updated quarterly.
- **Layer 2 (Transition conditions)**: Monitor for signals that rules need updating:
  - New AI capability releases (model upgrades, new modalities)
  - New failure patterns not captured by current taxonomy
  - Regulatory changes affecting AI use in the organization's domain
  - Significant changes in organizational AI usage patterns
- **Layer 3 (Living evidence protocol)**: When transition conditions are triggered, run the evidence update cycle:
  1. Assess whether new evidence changes delegation scores
  2. Test whether verification checklists catch new failure types
  3. Update governance rules, checklists, and training
  4. Document the change and rationale

## Implementation Priorities by Organization Size

| Organization Size | Stage 1 Focus | Stage 2 Focus | Stage 3 Focus |
| --- | --- | --- | --- |
| Large enterprise (1000+) | Full inventory across divisions | Role-specific verification checklists | Governance lead role + formal training program |
| Mid-size (100-1000) | Priority use case inventory | Team-level verification checklists | Manager training + lightweight governance |
| Small/startup (<100) | Founder-led assessment of top 5 AI uses | Simple pass/fail checklists for critical decisions | Team awareness + incident documentation |

## Cost-Benefit Frame

| Investment | Cost | Return |
| --- | --- | --- |
| Assessment (Stage 1) | 2-4 person-weeks | Identifies authority excess and verification gaps |
| Verification infrastructure (Stage 2) | 4-8 person-weeks + ongoing verification time | Catches reasoning failures before they affect decisions |
| Organizational embedding (Stage 3) | Training time + governance lead role | Systematic risk reduction + organizational learning |
| Continuous governance (Stage 4) | Quarterly review time | Governance stays current; avoids both over-permission and over-restriction |

**The cost of not implementing**: The 71-incident analysis shows that delegation calibration failure produces regulatory fines (FTC actions), litigation (employment discrimination, consumer harm), reputational damage (hallucinated content, biased outputs), and operational losses (flawed decisions based on unverified AI analysis). The verification cost is small relative to the potential cost of even one significant AI governance failure.

## Connection to Research Assets

| Implementation Need | Research Asset | Path |
| --- | --- | --- |
| Scoring model | Taxonomy scoring sheet | `research/core/taxonomy/scoring-sheet.md` |
| Decision tree | 6-step sequential decision tree | `research/core/taxonomy/decision-tree.md` |
| Failure classification | 25-type reasoning failure taxonomy | `research/core/framework/reasoning-failure-taxonomy.md` |
| Source verification | 5-level source quality hierarchy | `research/core/framework/reasoning-verification-source-quality.md` |
| Inferential verification | Inferential validity checking method | `research/core/framework/reasoning-verification-inferential-validity.md` |
| Confidence verification | Confidence calibration method | `research/core/framework/reasoning-verification-confidence-calibration.md` |
| Domain example | Market research verification | `research/extensions/market-research/task-decomposition.md` |
| Governance evolution | Living evidence protocol | `research/extensions/adaptive-governance/layer3-living-evidence-protocol.md` |
| Incident reference | 71-incident inventory | `research/extensions/business-alignment/incidents/incident-inventory.md` |
