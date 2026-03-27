# Layer 3: Living Evidence Protocol

## Status: research_complete
## Phase: 21 — Adaptive Governance Extension
## Date: 2026-03-10

---

## 1. Purpose

Phases 00-20 produced static research outputs — a final paper, executive summary, think-tank report, taxonomy, and domain recommendation table. These represent the best available evidence at the time of completion but have no built-in mechanism for incorporating new evidence as AI capabilities, deployment practices, and regulatory landscapes evolve.

Layer 3 defines a **living evidence protocol** that converts static research outputs into continuously maintained knowledge. It specifies what gets updated, how updates are triggered, who is responsible, and how version integrity is preserved.

**Design principle:** The research should always represent "current best evidence," not "evidence at time of original publication." Static conclusions that cannot be updated become misleading as the underlying reality changes.

---

## 2. Concept: From Static Publication to Living Document

### 2.1 Precedent: Healthcare Living Systematic Reviews

The Cochrane Collaboration pioneered living systematic reviews — reviews that are "continually updated, incorporating relevant new evidence as it becomes available." The BMJ/WHO living guideline on COVID-19 drugs reached 14 versions with weekly updates informing global drug purchases, mask policy, and travel requirements.

Key lessons from healthcare:
- Living reviews work best when the evidence base is "dynamic, emerging quickly, and the policy context is evolving" — a direct parallel to AI governance
- Maintaining currency proved difficult: of 25 Cochrane COVID-19 living reviews, half were not updated, and only four were updated more than once
- Success requires sustained commitment, methodological capacity, and collaborative structures
- Technology (AI screening, NLP, automation) can reduce but not eliminate the update burden

### 2.2 Adaptation for AI Governance

AI governance evidence differs from clinical evidence in important ways:

| Dimension | Clinical Evidence | AI Governance Evidence |
|-----------|-------------------|----------------------|
| Evidence type | Randomized controlled trials, observational studies | Deployment reports, regulatory actions, incident reports, capability benchmarks, audit findings |
| Update frequency | Monthly to quarterly | Weekly to monthly (capability changes); quarterly (regulatory); continuous (incidents) |
| Quality control | Peer review, systematic review methodology | Evidence tier classification (Tier 1/2/3 from Phase 08) |
| Source diversity | Medical journals, registries | Regulatory filings, company disclosures, benchmark databases, incident registries, academic publications |
| Stakeholder ecosystem | Clinicians, patients, regulators | Executives, engineers, regulators, auditors, affected populations |

The living evidence protocol must accommodate faster update cycles, more diverse source types, and less standardized quality control than healthcare.

---

## 3. Living Evidence Architecture

### 3.1 Components

```
┌─────────────────────────────────────────────────┐
│  Evidence Intake                                 │
│  - Capability benchmarks and model releases      │
│  - Regulatory actions and guidance updates        │
│  - Deployment incident reports                    │
│  - Academic publications                          │
│  - Industry case studies and audit findings       │
├─────────────────────────────────────────────────┤
│  Evidence Processing                             │
│  - Classify by domain and decision type           │
│  - Assign evidence tier (Tier 1/2/3)             │
│  - Assess relevance to existing recommendations  │
│  - Flag contradictions or confirmation            │
├─────────────────────────────────────────────────┤
│  Evidence Register (Maintained Artifact)          │
│  - Source tracking with dates and tiers           │
│  - Claim-to-evidence mapping                      │
│  - Contradiction and confirmation log             │
│  - Version history                                │
├─────────────────────────────────────────────────┤
│  Recommendation Update                           │
│  - Update domain recommendation table             │
│  - Update transition condition thresholds         │
│  - Update case evidence base                      │
│  - Version and changelog maintained               │
└─────────────────────────────────────────────────┘
```

### 3.2 Maintained Artifacts

The following artifacts from Phases 00-20 are designated as **living documents** under this protocol:

| Artifact | Location | Update Cadence |
|----------|----------|----------------|
| Domain Recommendation Table | Phase 18 | Quarterly or upon material evidence change |
| Scenario Decision Matrix | Phase 15 | Quarterly or upon material evidence change |
| Evidence Register | Phase 18 | Continuous (new evidence added as identified) |
| Claims Register | Phase 19 | Quarterly (claims reassessed against new evidence) |
| Transition Conditions | Phase 21 Layer 2 | Quarterly (thresholds recalibrated) |
| Case Evidence Base | Phase 10 | Upon new case addition or existing case update |
| Taxonomy | Phase 16 | Annually (structural changes only) |

Artifacts not designated as living documents (final paper, executive summary, think-tank report) remain as versioned snapshots. New versions may be produced but are treated as distinct publications, not updates to the original.

---

## 4. Update Triggers

Updates are triggered by events, not by calendar alone. Calendar-based reviews serve as backstop to ensure evidence is not missed.

### 4.1 Event-Based Triggers

| Trigger Category | Specific Trigger | Response |
|------------------|-----------------|----------|
| **Capability change** | Major model release by leading lab (e.g., new Claude, GPT, Gemini generation) | Reassess capability indicators; evaluate whether new tasks become eligible for escalation |
| **Capability change** | New modality introduction (e.g., agentic AI framework, multi-modal integration) | Flag for framework review; assess whether existing transition conditions apply |
| **Regulatory action** | New regulation enacted or enforced (e.g., EU AI Act provisions, new national AI law) | Update regulatory evidence in relevant domains; reassess compliance-dependent transition conditions |
| **Regulatory action** | Regulatory enforcement action against AI deployment | Add to incident register; reassess domain recommendation if in scope |
| **Regulatory action** | New regulatory guidance or interpretation | Update evidence register; assess impact on transition conditions |
| **Incident** | Publicly reported AI deployment failure with material harm | Add to incident register; reassess relevant domain recommendation |
| **Incident** | Internal deployment failure (for organizations using this framework) | Add to incident register; trigger regression evaluation per Layer 2 |
| **Academic evidence** | Peer-reviewed publication contradicting or strongly supporting a framework claim | Update claims register; flag for quarterly review |
| **Industry evidence** | Major deployment case study with Tier 2+ evidence quality | Add to case evidence base; assess relevance to domain recommendations |
| **Benchmark** | Standardized benchmark results showing material capability shift | Update capability indicators; evaluate graduation criteria impact |

### 4.2 Calendar-Based Reviews

| Review | Frequency | Scope |
|--------|-----------|-------|
| Evidence scan | Monthly | Scan for new triggers across all categories |
| Evidence register update | Quarterly | Process accumulated evidence; update registers |
| Recommendation review | Quarterly | Reassess domain recommendations against updated evidence |
| Transition condition calibration | Quarterly | Review threshold appropriateness based on observed data |
| Structural framework review | Annually | Assess whether taxonomy categories, workflow model, or infrastructure requirements need structural change |

---

## 5. Evidence Processing Protocol

### 5.1 New Evidence Intake

When new evidence is identified (via trigger or scan):

```
Step 1: Source identification
        - What is the source? (regulatory filing, academic paper, company disclosure, incident report, benchmark)

Step 2: Tier classification
        - Tier 1: Regulator-backed, audited, peer-reviewed, court-documented
        - Tier 2: Official company documentation, technical disclosures, executive statements
        - Tier 3: Investigative journalism, trade press, secondary summaries

Step 3: Domain and claim mapping
        - Which domain(s) does this evidence relate to?
        - Which existing claims does it support, contradict, or extend?
        - Does it create a new claim not covered by existing framework?

Step 4: Impact assessment
        - Does this evidence change any domain recommendation? (high impact)
        - Does this evidence change any transition condition threshold? (medium impact)
        - Does this evidence add context without changing recommendations? (low impact)

Step 5: Action routing
        - High impact: Immediate review; recommendation update within 2 weeks
        - Medium impact: Queue for next quarterly review
        - Low impact: Add to evidence register; no immediate action
```

### 5.2 Contradiction Handling

When new evidence contradicts an existing claim or recommendation:

```
Step 1: Classify the contradiction
        - Direct contradiction (new evidence says the opposite)
        - Scope limitation (existing claim was too broad; new evidence narrows it)
        - Condition change (claim was correct under old conditions; conditions have changed)

Step 2: Assess evidence strength
        - Is the new evidence stronger, equal, or weaker than existing evidence?
        - If stronger: initiate recommendation update
        - If equal: flag for deeper investigation
        - If weaker: note in evidence register but do not change recommendation

Step 3: Update claims register
        - Mark the affected claim with contradiction flag
        - Record both supporting and contradicting evidence
        - Document resolution or pending status

Step 4: If recommendation change is warranted
        - Draft updated recommendation
        - Review against transition conditions
        - Update domain recommendation table with new version number and date
        - Document the change rationale in changelog
```

---

## 6. Version Management

### 6.1 Versioning Scheme

Living documents use semantic versioning: `major.minor.patch`

- **Major** (e.g., 2.0.0): Structural change to framework (new category, removed dimension, fundamental reframing)
- **Minor** (e.g., 1.1.0): Recommendation change in one or more domains (mode change, threshold change, new domain added)
- **Patch** (e.g., 1.0.1): Evidence addition without recommendation change (new case, updated register, clarification)

### 6.2 Changelog Requirements

Every update to a living document must include:

```
## Changelog Entry

### Version: [version number]
### Date: [date]
### Type: [major | minor | patch]
### Trigger: [what triggered this update]
### Changes:
- [specific change 1]
- [specific change 2]
### Evidence basis:
- [source 1 with tier classification]
- [source 2 with tier classification]
### Impact:
- [which domain recommendations affected]
- [which transition conditions affected]
### Reviewer: [who reviewed and approved]
```

### 6.3 Snapshot Preservation

When a major or minor version is released, the previous version is preserved as a dated snapshot. This enables:
- Tracking how recommendations evolved over time
- Comparing current recommendations against historical positions
- Auditing whether changes were evidence-justified

---

## 7. Evidence Source Categories and Monitoring

### 7.1 Capability Evidence Sources

| Source | What to Monitor | Typical Frequency |
|--------|----------------|-------------------|
| Model release announcements | New capability claims, benchmark results | Monthly |
| Standardized benchmarks (MMLU, HumanEval, etc.) | Performance trends across model generations | Quarterly |
| Red team reports | Safety and capability findings | Per release |
| Responsible scaling reports | ASL/CCL level changes | Per release |
| Academic capability evaluations | Independent performance assessments | Quarterly |

### 7.2 Regulatory Evidence Sources

| Source | What to Monitor | Typical Frequency |
|--------|----------------|-------------------|
| EU AI Act implementation | New provisions taking effect, enforcement actions | Quarterly |
| National AI laws (Korea AI Basic Act, etc.) | Enactment, implementation dates, guidance | Quarterly |
| Sector regulators (FDA, CFPB, SEC, EEOC) | New guidance, enforcement actions, sandbox results | Monthly |
| NIST AI RMF updates | Framework revisions, new supplements | Annually |
| International frameworks (OECD, Council of Europe) | New guidance, treaty updates | Annually |

### 7.3 Deployment Evidence Sources

| Source | What to Monitor | Typical Frequency |
|--------|----------------|-------------------|
| AI incident databases (AIID, OECD) | New incidents by domain and severity | Monthly |
| Regulatory enforcement actions | Enforcement outcomes related to AI deployment | Monthly |
| Company disclosures and transparency reports | Deployment outcomes, governance practices | Quarterly |
| Academic case studies | Peer-reviewed deployment analyses | Quarterly |
| Industry surveys (Stanford HAI, McKinsey, etc.) | Adoption patterns, governance maturity | Annually |

---

## 8. Integration with Existing Research Structure

### 8.1 How Living Evidence Connects to Phases 00-20

```
Phase 16 (Taxonomy)          ← Structural framework review (annual)
Phase 18 (Domain Table)      ← Recommendation updates (quarterly or event-triggered)
Phase 18 (Evidence Register) ← Continuous evidence intake
Phase 19 (Claims Register)   ← Quarterly claims reassessment
Phase 15 (Scenario Matrix)   ← Quarterly recommendation review
Phase 21 Layer 2             ← Quarterly threshold calibration
Phase 10 (Case Base)         ← New case addition (event-triggered)
```

### 8.2 How Living Evidence Connects to Layer 2

Layer 2 defines transition conditions with specific thresholds. Layer 3 provides the evidence base for:
- Determining whether graduation criteria are met (new benchmark data, deployment track records)
- Calibrating threshold levels (are current thresholds too conservative or too aggressive given observed outcomes?)
- Detecting regression triggers (incident reports, drift signals, regulatory changes)

**Flow:**
```
New evidence (Layer 3) → Triggers threshold evaluation (Layer 2) → May change authority level
New evidence (Layer 3) → Updates domain recommendation (Phase 18) → Informs organizational decisions
```

---

## 9. Practical Implementation Guidance

### 9.1 For Research Teams

- Designate a living evidence maintainer responsible for monthly evidence scans
- Use the evidence intake protocol for all new sources
- Maintain the evidence register as the single source of truth
- Produce quarterly evidence summaries documenting what changed and what was confirmed

### 9.2 For Organizations Adopting the Framework

- Subscribe to evidence source monitoring for domains relevant to your AI deployments
- Map internal deployment outcomes to the evidence register format
- Use event-based triggers to initiate internal governance reviews
- Treat the domain recommendation table as a living reference, not a fixed policy

### 9.3 For Policymakers

- Use the living evidence protocol to maintain currency of AI governance guidance
- Regulatory sandboxes generate evidence that should feed back into the living evidence cycle
- Enforcement actions should be documented in a format compatible with evidence register intake

---

## 10. Limitations and Open Questions

1. **Resource sustainability:** Living evidence requires sustained effort. The Cochrane experience shows that even well-resourced teams struggle to maintain update currency. AI governance lacks the institutional infrastructure that supports clinical evidence maintenance.

2. **Quality control at speed:** Faster update cycles increase the risk of incorporating lower-quality evidence or premature conclusions. The evidence tier system mitigates but does not eliminate this risk.

3. **Fragmentation:** If multiple organizations maintain their own living evidence registers, evidence may fragment rather than accumulate. Shared evidence infrastructure (like AI incident databases) helps but is not yet comprehensive.

4. **Update fatigue:** Stakeholders may disengage if updates are too frequent or too minor. The severity-based action routing (high/medium/low impact) is designed to focus attention on material changes.

5. **Backward compatibility:** As recommendations evolve, organizations that deployed based on earlier versions need guidance on whether and how to transition. The version management system supports this but does not automate it.

6. **Scope creep:** Living evidence protocols can expand indefinitely. The defined artifact scope (Section 3.2) and calendar-based review cadence provide boundaries, but discipline is required to maintain focus.
