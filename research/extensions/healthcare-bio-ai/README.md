# Healthcare and Bio AI Special Topic

status: wave_1_in_progress
date: 2026-04-21
track_type: special topic (lateral extension)
parent_track: reasoning trust verification direction

This directory contains a special-topic exploration of AI in healthcare, hospitals, pharmaceuticals, and biotech. It tests whether the repo's adaptive framework (6-dimensional delegation × 5-discipline reasoning verification × 7-tier scale-based capacity) produces actionable guidance across the structurally distinct sub-domains of healthcare AI.

## Why this track exists

Healthcare occupies one slot in the core framework's 8-domain comparison but is thinly represented (one case study, one scenario pack). In practice, "healthcare AI" spans deployments as structurally different as diagnostic imaging, drug discovery, hospital scheduling, mental-health chatbots, and insurance prior authorization. A single domain label hides that variation. This track decomposes the domain and tests the framework against the decomposition.

This is a **special topic**, not a new core thesis. It feeds findings back into the core only where they are load-bearing enough to warrant it. The scale-based reasoning verification track and the reasoning trust verification direction remain the primary extension workstreams.

## Reading order

1. [research-plan.md](research-plan.md) — the plan, scope, and procedures. Read first.
2. [sub-domain-taxonomy.md](sub-domain-taxonomy.md) — the nine structurally distinct sub-domains of healthcare AI, with delegation-mode defaults and failure profiles.
3. [regulatory-landscape.md](regulatory-landscape.md) — comparative matrix of FDA, EU AI Act + MDR, MHRA, PMDA, MFDS, NMPA, WHO, IMDRF regimes with structural-gap analysis.
4. [incident-inventory.md](incident-inventory.md) — documented healthcare-bio AI failure cases coded with FICS-1 and mapped to existing failure taxonomies.
5. [framework-application.md](framework-application.md) — 6-dim delegation framework and 5-discipline reasoning verification applied sub-domain by sub-domain.
6. [scale-mapping.md](scale-mapping.md) — healthcare actors mapped to S1-S7 tiers with verification capacity implications.
7. [synthesis.md](synthesis.md) — load-bearing findings, framework revision recommendations, connection to the core thesis.

## Nine sub-domains

The track decomposes healthcare AI into these structurally distinct sub-domains (detailed in `sub-domain-taxonomy.md`):

| # | Sub-domain | Decision being made | Representative actors |
|---|---|---|---|
| HC1 | Diagnostic imaging and pathology AI | Image → finding / flag / prioritisation | Radiologists, pathologists, imaging-AI vendors |
| HC2 | Clinical decision support and deterioration prediction | Patient → risk flag / treatment suggestion | Hospital ICU / ward clinicians, Epic / Cerner, startups |
| HC3 | Hospital operations AI | Capacity / flow / staffing allocation | Hospital administrators, revenue-cycle vendors |
| HC4 | Drug discovery and R&D AI | Target / molecule / trial-design candidate selection | Pharma R&D, biotech startups, AI-first drug discovery |
| HC5 | Pharmacovigilance and post-market drug safety | Signal detection in adverse-event data | Pharma safety teams, FDA / EMA, regulators |
| HC6 | Precision medicine and genomics AI | Variant → clinical significance / treatment match | Molecular diagnostics labs, oncologists, pharma |
| HC7 | Mental health and patient-facing AI | Symptom → support / screening / escalation | Consumer apps, platforms, patients directly |
| HC8 | Health insurance / utilization management AI | Claim → approve / deny / flag for review | Insurers, claims processors, state Medicaid programmes |
| HC9 | Administrative and documentation AI | Clinical encounter → note / code / bill | Hospital administration, ambient-scribe vendors |

## Connection to the rest of the project

This track is a lateral test case for three active workstreams:

1. **Delegation calibration framework (core)** — healthcare is the stress test. If the framework cannot differentiate authority levels across HC1-HC9, it is too coarse.
2. **Scale-based reasoning trust verification (extension)** — healthcare adds depth to S5 (regulated professions) and sharpens the S4 substantive-vs-typical distinction through academic medical centre vs. community hospital variance.
3. **Adaptive governance (extension)** — healthcare is the most regulated of the repo's domains; it tests whether the adaptive-governance model accurately describes how regulator lag manifests in the highest-regulation case.

The track is **not** structured as a standalone publication. Its role is internal: test, decompose, and feed back.

## Status and honest limitations

- Single-cycle work. Breadth over depth; each sub-domain gets a page-level treatment.
- Documentary evidence only. No clinician interviews, no regulatory FOIA, no hospital site visits.
- US and EU regulatory material is strongest; Asia coverage is lighter (same practice as the scale-based track's Asia-market appendix).
- Agentic clinical AI is referenced but not characterised in depth; the space is in flux.
- Citations and regulatory document names are current as of April 2026 and may age within 6-12 months.

## What this track does not claim

- It does not propose a new framework for healthcare AI specifically. Where findings require framework adaptation, they are noted as revisions to the core framework.
- It does not catalogue AI devices, vendors, or products. Market-research scanning is the job of the `market-research/` track.
- It does not attempt ethical theory. Where normative questions arise (Q3 in RVCS-1), they are treated through the existing framework's normative-acceptability discipline, not through bioethics.

## Upstream references

- Main research plan for this track: [`research-plan.md`](research-plan.md)
- Core framework: [`research/core/taxonomy/category-system.md`](../../core/taxonomy/category-system.md)
- Core healthcare case and scenarios: [`research/core/domain-analysis/cases/healthcare-case.md`](../../core/domain-analysis/cases/healthcare-case.md), [`research/core/scenario-packs/healthcare-scenarios.md`](../../core/scenario-packs/healthcare-scenarios.md)
- Reasoning verification framework: [`research/core/framework/reasoning-failure-taxonomy.md`](../../core/framework/reasoning-failure-taxonomy.md) and sibling files
- Scale-based track: [`research/extensions/scale-based/README.md`](../scale-based/README.md)
