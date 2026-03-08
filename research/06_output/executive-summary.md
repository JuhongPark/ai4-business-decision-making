# Executive Summary

title: AI in Business Decision-Making
subtitle: Executive Summary
status: draft_v1

## Core Message

AI should not be deployed with one fixed autonomy model across all business decisions. The right role for AI depends on domain risk, scenario condition, evidence quality, and governance burden.

## Main Findings

1. Operations is the strongest candidate for `automate with guardrails`, but only in stable and measurable settings.
2. Finance should usually remain `assist` or tightly governed `recommend`, especially under stress or fairness uncertainty.
3. Healthcare should remain `assist` or tightly governed `recommend` because patient safety and edge-case uncertainty are too important for broad automation.
4. Scenario condition matters as much as domain type. Baseline, stress, and edge-case conditions produce different autonomy recommendations.

## Strategic Implication

The most important organizational decision is not whether to adopt AI. It is how much authority to delegate to AI under specific conditions.

## Policy Implication

High-stakes domains require stronger evidence, clearer accountability, and explicit fallback rules before AI autonomy can expand.

## Recommended Deployment Logic

- lower-risk, repeatable environments: `recommend` or `automate with guardrails`
- high-stakes regulated environments: `assist` or tightly governed `recommend`
- edge-case or uncertainty-heavy environments: revert toward `assist`
