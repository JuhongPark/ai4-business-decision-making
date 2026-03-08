# Phase 16: Decision Tree

status: completed
purpose: Provide a practical sequence for deciding when and how AI should be used.

## Step 1: Identify the Domain

Is the decision in:

- operations or bounded marketing
- product or market research
- strategy
- finance, healthcare, investment, or another high-stakes domain

## Step 2: Classify the Decision Structure

Is the decision:

- structured
- semi-structured
- unstructured

If unstructured, default to `assist`.

## Step 3: Classify the Risk Level

Does failure create:

- mainly internal efficiency cost
- meaningful commercial or customer harm
- fairness, safety, compliance, access, or investor-protection risk

If high-risk, default to `assist` or tightly governed `recommend`.

## Step 4: Classify the Scenario

Is the situation:

- baseline
- stress
- edge-case

If edge-case, default to `assist`.

## Step 5: Check Evidence Strength

Is the supporting evidence:

- strong
- moderate
- weak

If weak, reduce autonomy by one level.

## Step 6: Check Governance Readiness

Does the organization have:

- clear accountability
- monitoring and auditability
- explainability proportional to risk
- escalation and fallback rules

If not, reduce autonomy by one level.

## Decision Output

- if structured + low-risk + baseline + moderate/strong evidence + governance ready: `recommend` or `automate with guardrails`
- if semi-structured + medium-risk + baseline: `assist` or `recommend`
- if high-risk + baseline + strong evidence + governance ready: `assist` or tightly governed `recommend`
- if stress or edge-case raises uncertainty: reduce autonomy toward `assist`
