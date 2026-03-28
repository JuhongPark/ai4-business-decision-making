# Normative Acceptability Assessment Method

status: active
phase: 2.4
date: 2026-03-28
purpose: Structured method for assessing whether AI-generated business reasoning conforms to applicable professional, ethical, legal, and social standards.

## The Problem

AI reasoning can be factually correct and logically valid but still violate the standards that would apply if a human professional produced the same analysis. A cost optimization that recommends legally questionable labor practices, a marketing strategy that crosses ethical boundaries, or a financial analysis that ignores regulatory constraints — all may be internally coherent while being normatively unacceptable.

This method checks whether AI reasoning meets the standards of the relevant professional domain.

---

## Step 1: Identify Applicable Normative Domains

Every business decision operates within multiple normative frameworks. Identify which apply:

| Domain | Scope | Examples |
|---|---|---|
| **Legal/regulatory** | Binding rules with enforcement mechanisms | Employment law, securities regulation, antitrust, data privacy (GDPR, CCPA), sector-specific regulation (FDA, CFPB) |
| **Professional standards** | Codified standards of practice for licensed professions | CFA standards (finance), clinical guidelines (healthcare), GAAP/IFRS (accounting), bar ethics rules (legal), engineering codes |
| **Ethical principles** | Established ethical frameworks applicable to the context | Non-discrimination, informed consent, fair dealing, fiduciary duty, stakeholder consideration |
| **Social conventions** | Unwritten but widely accepted norms | Industry customs, cultural expectations, relationship norms, reputational standards |

Normative domains are cumulative: a hiring recommendation must satisfy employment law AND professional HR standards AND non-discrimination ethics AND organizational culture norms.

## Step 2: The Professional Review Test

For each major recommendation or conclusion in the AI output, ask:

> "If a licensed professional in this domain reviewed this reasoning, what would they flag?"

Operationalize by domain:

| If the reasoning involves... | Ask whether it would pass review by... |
|---|---|
| Financial analysis or projections | CFA charterholder or senior financial analyst |
| Hiring or HR recommendations | Employment lawyer or senior HR professional |
| Marketing strategy | Marketing executive with regulatory awareness |
| Healthcare-related claims | Licensed clinician or clinical researcher |
| Legal analysis | Practicing attorney in the relevant jurisdiction |
| Operational recommendations | Domain operations manager with safety responsibility |

This test does not require access to these professionals. It requires asking: "Would this survive scrutiny from someone who knows the rules?"

## Step 3: Specific Normative Checks

### 3a. Regulatory Compliance Check
- Does the reasoning identify which regulations apply?
- Does it account for jurisdiction-specific requirements?
- Do any recommendations require actions that may violate applicable regulations?
- Are regulatory risks acknowledged?

### 3b. Professional Standard Check
- Does the analysis meet the evidentiary standards of the relevant profession?
- Are methods appropriate for the domain? (e.g., DCF for valuation, controlled studies for clinical claims)
- Would the conclusions withstand peer review in the relevant profession?

### 3c. Discriminatory Reasoning Check
- Does the reasoning use protected characteristics (race, gender, age, disability, religion) as decision factors?
- Does it use proxies for protected characteristics? (e.g., zip code as proxy for race, university name as proxy for socioeconomic status)
- Would the recommendation produce disparate impact on protected groups?
- This check applies even when the AI does not explicitly mention protected characteristics — the question is about outcomes.

### 3d. Externality Check
- Does the reasoning account for costs imposed on third parties?
- Are stakeholders beyond the immediate decision-maker considered?
- Would this recommendation be acceptable if its effects on all affected parties were visible?

### 3e. Power Asymmetry Check
- Does the reasoning recommend leveraging information or power imbalances beyond accepted bounds?
- Would the recommended action be acceptable if the other party had full information?
- Does it exploit vulnerable populations, uninformed consumers, or captive audiences?

## Step 4: Assess Severity of Violations

Not all normative issues carry equal weight:

| Severity | Definition | Response |
|---|---|---|
| **Critical** | Legal violation, discrimination, or safety risk | Reject the reasoning. Do not act on it. |
| **Serious** | Professional standard violation or significant ethical concern | Modify before acting. Consult domain expert. |
| **Moderate** | Social convention deviation or minor standard gap | Flag for awareness. Acceptable with explicit acknowledgment of the trade-off. |
| **Low** | Stylistic or cultural mismatch without substantive impact | Note for refinement. Does not block action. |

## Step 5: Overall Assessment

| Rating | Criteria |
|---|---|
| **Acceptable** | No normative violations identified. Reasoning conforms to applicable legal, professional, ethical, and social standards. |
| **Conditionally acceptable** | Minor normative issues identified. Acceptable with specified modifications or explicit risk acknowledgment. |
| **Unacceptable** | One or more critical or serious normative violations. Reasoning must be revised or rejected before action. |

---

## Worked Example

**AI output**: "To optimize customer support costs, reduce staffing to minimum legally required levels during off-peak hours. Analysis shows this could save $2.4M annually with minimal impact on SLA metrics."

**Step 1 — Applicable domains**:
- Legal: labor law (minimum staffing), consumer protection (service obligations)
- Professional: customer service industry standards, SLA contractual requirements
- Ethical: duty to customers, employee welfare
- Social: brand reputation, customer relationship expectations

**Step 2 — Professional review test**:
A senior customer experience executive would flag: "minimum legally required" is a compliance floor, not a service standard. Building a strategy around the legal minimum signals a willingness to degrade service to the lowest defensible level.

**Step 3 — Specific checks**:
- Regulatory: Legal if minimum staffing meets labor law requirements. But "minimum legally required" may not satisfy contractual SLA obligations.
- Professional standard: Customer service professionals define quality by responsiveness, resolution rate, and customer satisfaction — not by legal minimums.
- Externality: Customers bear the cost of longer wait times and lower service quality. Employees bear the cost of increased workload and stress.
- Power asymmetry: Customers with service contracts may have limited alternatives. Reducing quality below reasonable expectations exploits this.

**Step 4 — Severity**:
- SLA contractual risk: Serious (potential breach of contract)
- Service standard deviation: Moderate (legal but below professional norms)
- Employee impact: Moderate (increased workload)
- Brand/reputation risk: Moderate (perception of cost-cutting over service)

**Step 5 — Assessment**: Conditionally acceptable. The cost savings are real, but the recommendation must be modified to: (a) verify SLA compliance, (b) define staffing by service quality targets rather than legal minimums, (c) assess employee retention impact, (d) consider brand perception effects.
