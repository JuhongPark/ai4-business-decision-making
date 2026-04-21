# AI System Design & Management Reframe — Research Plan

status: research_plan
date: 2026-04-21
parent_memos:
  - [`research/extensions/scale-based/sales-vs-productization-decomposition.md`](../../extensions/scale-based/sales-vs-productization-decomposition.md)
  - [`research/operations/expansion/sales-vs-productization-research-plan.md`](sales-vs-productization-research-plan.md)
purpose: Re-ground the decomposition memo (sales skill vs productization skill) in the methodology of MIT System Design & Management (SDM). Treat the AI firm as a socio-technical system, apply classical systems-engineering frameworks (architecture, DSM, V-model, system dynamics, modularity), and produce a companion memo that an SDM-trained reader would recognise as rigorous.

---

## 1. Why this plan exists

The Wave 4 expansion (sales-vs-productization decomposition + six stream appendices) is analytically productive but is framed in firm-capability language — "sales skill," "productization skill," "verification substance." An MIT SDM reader would ask a different question: *what system architecture produces those skill patterns, and what management interventions would correct the coupling failures observed in the incident data?*

This plan answers that question by reframing the decomposition as a systems-engineering analysis of the AI firm, using frameworks the SDM curriculum treats as canonical:

- **System architecture** (Crawley, Cameron — form / function / concept view)
- **Design Structure Matrix** (Steward, Eppinger — coupling analysis)
- **V-model** (Forsberg, Mooz, Cotterman — requirements-to-verification life cycle)
- **System dynamics** (Sterman — stocks, flows, feedback loops, delays)
- **Modularity theory** (Ulrich — modular vs integral; Baldwin & Clark — design rules)
- **Architectural innovation** (Henderson & Clark — component vs architectural knowledge)
- **System-of-systems** (Maier — managerial and operational independence)
- **Complex product systems / CoPS** (Hobday — project-based coordination)
- **Platform strategy** (Meyer & Lehnerd; Boudreau; Tiwana)
- **Enterprise architecture** (Zachman; TOGAF)

The SDM reframe is not a replacement of the Wave 4 memo. It is a methodological companion that translates the capability-level decomposition into subsystem-level architecture and control-loop terms.

---

## 2. What the SDM reframe adds

Five concrete gains:

1. **A system boundary the memo did not draw.** The Wave 4 memo treats "the firm" as the unit. SDM asks: where does the AI system start and stop? Customer-facing inference? The data pipeline upstream? The monitoring stack downstream? Regulatory filings? Investor disclosures? Drawing an explicit system boundary lets interface requirements be named.

2. **Subsystem architecture the memo only hinted at.** §2 of the Wave 4 memo lists nine productization sub-dimensions as a vector. SDM recasts them as *subsystems* with architectural relationships: data subsystem, model subsystem, deployment subsystem, evaluation subsystem, monitoring subsystem, verification subsystem, sales-interface subsystem, investor-interface subsystem, regulatory-interface subsystem. Each has inputs, outputs, and coupling constraints.

3. **Coupling analysis the memo did not do.** Every observed failure in Stream B's 20-incident recoding can be re-expressed as a coupling failure between subsystems — sales-interface subsystem committing to claims the productization subsystem cannot meet. DSM formalises this and lets us ask: which coupling patterns are architecturally avoidable, and which are structurally inherent?

4. **A control-loop view of verification.** The Wave 4 memo treats verification as a productization output. SDM treats verification as a *feedback control loop* on the product. This distinction changes what counts as good verification — it is not enough to *measure* quality; the measurement must feed back to design in a way that closes the loop.

5. **A lifecycle view the memo omitted.** The Wave 4 memo is static. An SDM V-model shows AI product development as requirements → architecture → subsystem design → implementation → unit test → integration test → system verification → deployment → operation → retirement. Each phase has inputs and verification gates. Each incident from Stream B can be located on the V — almost all of them are failures at the integration-test or system-verification gate that were not caught before deployment.

---

## 3. Research streams

Four streams. Each is framed as an SDM analytical task, produces a specific SDM artifact, and feeds the final memo.

### Stream 1 — System architecture: form, function, concept

**Purpose**: Apply Crawley's three-view decomposition (form = what the thing is, function = what it does, concept = why it exists) to four canonical AI firm archetypes.

**Method**: Identify the form / function / concept of each archetype. Compare subsystem boundaries, interface specifications, and emergent property support across archetypes. Use primary sources where available (company blogs, press releases, technical reports). Use secondary sources for inferred architecture details.

**Archetypes to analyse**:
- **Frontier lab monolith** (Anthropic, OpenAI). Integrated training + eval + deployment + safety inside one organisation.
- **Federated enterprise** (Microsoft, Google, JPMorgan). AI distributed across multiple BUs with a central-governance function.
- **Vertical AI platform** (Harvey, Sierra, Cursor). Focused domain, rented foundation, domain-specific productization.
- **Thin wrapper** (most pre-Series-A Gen AI startups, Klarna's AI chatbot circa 2024). Foundation-model API call wrapped in UI.

**Output artifact**: 4×3 matrix (archetype × form/function/concept) with interface specifications for each. Narrative interpretation of how the form view explains the Wave 4 quadrant placements.

**Acceptance criterion**: Each archetype has named subsystems, named interfaces, named emergent properties. At least one testable prediction per archetype about which quadrant it defaults to.

### Stream 2 — Organisational DSM and interface analysis

**Purpose**: Apply Eppinger's DSM methodology to the organisational coupling between sales, productization, verification, governance, and regulatory subsystems.

**Method**:
- Identify the five subsystems (Sales Interface, Productization Engineering, Verification, Governance, Regulatory Interface).
- Enumerate the information, artifact, and decision flows between them (who produces what; who consumes what; what depends on what).
- Construct a 5×5 DSM with binary (coupled / not) and ordinal (strength 1-3) versions.
- Identify the dominant coupling failures in Stream B's incident sample as specific DSM cell failures.
- Apply Ulrich's modular-integral classification: which cells are *architecturally coupled* (inherent) and which are *parametrically coupled* (avoidable via interface specification)?

**Output artifact**: 5×5 DSM with named interfaces and coupling strengths. List of the top three coupling-failure patterns that produce upper-right-quadrant firms. Baldwin-Clark "design rules" candidates for each interface.

**Acceptance criterion**: DSM is produced for at least two archetypes (frontier lab and wrapper). Incident-driven coupling failures are located in specific DSM cells.

### Stream 3 — V-model lifecycle and system dynamics

**Purpose**: Map AI development to the V-model and construct a causal loop diagram of the sales-productization drift dynamic.

**Method, V-model side**:
- Left arm: user needs → stakeholder requirements → system requirements → AI functional architecture → subsystem requirements → subsystem design → unit implementation.
- Right arm: unit test → subsystem integration test → system verification → system validation → deployment → operation → decommission.
- Map the five verification disciplines (Q1-Q5 in the reasoning verification framework) to specific right-arm stages.
- Map the 20 Stream B incidents to the V-model stage where the failure should have been caught but was not.

**Method, system dynamics side**:
- Construct a causal loop diagram (CLD) of the sales-productization drift: stocks (verification debt, sales commitments, productization capacity), flows (commitment rate, productization velocity, verification throughput), feedback loops (positive — sales pressure drives hiring; negative — verification findings drive deployment delay), delays (productization lags sales commitments by N quarters).
- Identify the reinforcing loop that produces "governance theater" and the balancing loop that would close it.

**Output artifacts**: One V-model diagram with 20 incident placements. One CLD for the drift dynamic with named stocks, flows, and loops. One-paragraph policy implication per loop.

**Acceptance criterion**: V-model placement is unambiguous for 15 of 20 incidents. CLD has at least one reinforcing and one balancing loop identified with real-world exemplars.

### Stream 4 — Classical SDM literature bridge

**Purpose**: Connect the decomposition to the specific SDM canonical works an MIT SDM student would cite.

**Method**: For each theorist, extract the core proposition and apply it to AI firms:
- **Ulrich (1995)** — modular vs integral product architecture. Which AI firms are modular? Which are integral? What are the interface conditions for modularity?
- **Baldwin & Clark (2000)** — design rules. What are the "design rules" an AI platform must publish to allow modular contributions from third parties? Foundation-model APIs as a design rule surface.
- **Henderson & Clark (1990)** — architectural vs component innovation. Does AI create architectural innovation? If so, what are the core-component and architecture knowledge stocks that must change?
- **Maier (1998)** — system-of-systems: managerial independence, operational independence, evolutionary development, emergent behaviour, geographic distribution. Does the AI supply chain (data, compute, foundation model, fine-tune, deployment) satisfy the SoS criteria?
- **Hobday (1998)** — complex product systems. Are frontier AI labs CoPS? What coordination mechanisms do they use?
- **Utterback (1994)** — dominant design + S-curve. Has the AI industry reached a dominant design for the productization stack? What are the competing paradigms?
- **Sterman (2000)** — system dynamics. Link to Stream 3.
- **Crawley, Cameron, Selva (2015)** *System Architecture*. Link to Stream 1.
- **Eppinger & Browning (2012)** *Design Structure Matrix Methods and Applications*. Link to Stream 2.
- **Meyer & Lehnerd (1997)** — product platforms. Does the foundation-model + fine-tune-layer architecture satisfy platform-strategy conditions?
- **Boudreau (2010), Tiwana (2014)** — platform openness and governance. How do Anthropic MCP, OpenAI function-calling schemas, Google Agent Builder compare on platform-governance dimensions?

**Output artifact**: A bridge table mapping each named theorist to (a) the SDM concept they formalise, (b) the AI firm exemplar that embodies the concept, and (c) the refinement the concept adds to the sales-productization decomposition.

**Acceptance criterion**: At least 10 theorists bridged. Each entry cites a specific primary work and a specific 2024-2026 AI firm example.

---

## 4. Execution order

1. Run Stream 1 (architecture) and Stream 2 (DSM) — architectural frames inform the other streams.
2. Run Stream 3 (V-model + system dynamics) — requires the architectural decomposition.
3. Run Stream 4 (literature bridge) — synthesises and cites across streams.
4. Write final memo `ai-system-design-management-view.md` integrating all four streams.
5. Update the main decomposition memo with a forward reference (§14.8) to the SDM view.
6. Update `scale-based/README.md` to list the SDM memo.
7. Run language-policy check.
8. Commit.

---

## 5. Deliverables

Two file categories:

**New files**:
- `research/operations/expansion/ai-system-design-management-research-plan.md` — this document.
- `research/extensions/scale-based/ai-system-design-management-view.md` — the integrated SDM memo.

**Modified files**:
- `research/extensions/scale-based/sales-vs-productization-decomposition.md` — add forward reference in §14 and in §13 cross-references.
- `research/extensions/scale-based/README.md` — add SDM memo to the recommended reading list.

---

## 6. What the SDM reframe deliberately does not attempt

- **Not a quantitative simulation.** The CLD in Stream 3 is qualitative (named stocks, flows, loops); no Vensim / Stella model is built. The Wave 4 data does not support a parameterised simulation.
- **Not a TOGAF / Zachman enterprise architecture.** Full EA would require 30-50 stakeholder interviews. Stream 1's form / function / concept analysis is the lightweight version.
- **Not a MBSE SysML model.** The V-model diagram is narrative, not formal SysML. The audience of the memo is the broader research community, not a systems-engineering certification body.
- **Not a substitute for primary-source interviews.** An SDM thesis-grade analysis would include subject-matter-expert interviews at each subsystem. This cycle synthesises public data only; interview-based Wave is a future extension.
- **Not an extension into mechanical / physical AI systems.** The memo stays within software AI firms. Embodied AI (robotics, autonomous vehicles, medical devices) has different architectural constraints and would be a separate analysis.

---

## 7. Evidence grading

Expected evidence mix per stream:

| Stream | Expected grade distribution | Why |
|---|---|---|
| 1 (architecture) | B majority — company blogs and technical reports are practitioner-grade primary sources | Some C for inferred interface specifications |
| 2 (DSM) | B/C — DSM is an analytical construct, not a measurement | Anchored to Stream B incident evidence which is A/B |
| 3 (V-model + SD) | B — V-model placements are inferred; CLD is qualitative | One D-graded parameter: "how much do delays contribute to drift" |
| 4 (literature bridge) | A for the classical works (citable primary sources); B for AI-firm examples | Bridge itself is analytical |

The SDM memo expects at least one D-graded claim (the delay magnitude in the CLD). This is appropriate — SDM analysis at this level of abstraction routinely includes qualitative claims with honest confidence labels.

---

## 8. Success criteria

The SDM reframe succeeds if:

1. The new memo presents the AI firm as a socio-technical system with named subsystems, interfaces, and emergent properties.
2. Each of the four SDM streams contributes a specific artifact (architecture matrix, DSM, V-model diagram, literature bridge table) — not just prose.
3. The memo maps Stream B's 20-incident sample to specific V-model stages and DSM cells, showing that the decomposition is consistent with a system-failure analysis.
4. At least 10 canonical SDM works are cited with their specific propositions applied to AI firms.
5. The memo's conclusions are testable in a follow-on cycle (Wave 6): stream-by-stream predictions that can be falsified.

Failure modes to avoid:

- **Terminology drift without analytical gain.** Relabeling "sales skill" as "sales subsystem" without a coupling or interface analysis is not SDM work.
- **Over-claiming modelling rigour.** A qualitative CLD is not a simulation; the memo must be explicit about this.
- **Citing SDM canon without applying it.** Each theorist-citation must produce a concrete refinement to the decomposition.

---

## 9. Cross-references

- [`../../extensions/scale-based/sales-vs-productization-decomposition.md`](../../extensions/scale-based/sales-vs-productization-decomposition.md) — the parent memo this plan extends methodologically.
- [`sales-vs-productization-research-plan.md`](sales-vs-productization-research-plan.md) — the Wave 4 research plan whose six streams this plan's four streams build on.
- [`../../extensions/scale-based/cross-tier-synthesis.md`](../../extensions/scale-based/cross-tier-synthesis.md) — the scale-based findings this memo's architectural view must remain consistent with.
- [`../../extensions/scale-based/incident-decomposition-recoding.md`](../../extensions/scale-based/incident-decomposition-recoding.md) — Stream B of Wave 4, the incident source for Stream 3 V-model mapping and Stream 2 DSM failure cells.
- [`../../extensions/scale-based/regulatory-regime-skill-asymmetry-appendix.md`](../../extensions/scale-based/regulatory-regime-skill-asymmetry-appendix.md) — Stream D of Wave 4, the regulatory-interface subsystem input for Stream 1 architecture.
- [`scale-based-reasoning-trust-research-plan.md`](scale-based-reasoning-trust-research-plan.md) — the parent scale-based research plan whose multi-stream Wave design this plan replicates.
