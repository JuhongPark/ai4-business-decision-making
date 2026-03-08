# Phase 16: Decision Rules

status: completed
purpose: Translate the category system into rules for when and how AI should be used.

## Rule Set

### Rule 1: Structured plus low-risk plus baseline

If the decision is structured, low-risk, and taking place under baseline conditions, the preferred mode is usually `recommend` or `automate with guardrails`.

Typical examples:

- routing
- scheduling
- inventory balancing
- bounded personalization logic

### Rule 2: Semi-structured plus medium-risk

If the decision is semi-structured and materially consequential, the preferred mode is usually `assist` or `recommend`.

Typical examples:

- product prioritization
- campaign optimization
- pricing review
- demand planning

### Rule 3: High-risk domains default to lower autonomy

If the decision affects fairness, compliance, safety, access, or investor protection, the default mode should be `assist` or tightly governed `recommend`.

Typical examples:

- credit underwriting
- clinical support
- investment advice
- hiring-related screening

### Rule 4: Stress conditions increase support value but reduce automation tolerance

If the environment moves from baseline to stress, AI may become more useful for speed and consistency, but the acceptable autonomy level usually does not increase by the same amount.

Interpretation:

- assist often becomes more valuable
- recommend may remain acceptable
- automate should be treated more cautiously

### Rule 5: Edge cases trigger fallback

If the system encounters degraded data, drift, incomplete information, subgroup anomalies, or atypical cases, the default response should be to fall back toward `assist`.

### Rule 6: Weak evidence reduces allowable autonomy

If the evidence supporting the system is weak, autonomy should be reduced even if the domain appears structurally suitable.

### Rule 7: Strong evidence is necessary but not sufficient

Even strong evidence does not justify broad automation in high-risk domains unless governance, oversight, and fallback design are also strong.

## Short Executive Rule

Do not ask only whether AI works. Ask whether this category combination justifies this level of AI authority.
