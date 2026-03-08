# Phase 16: Category System

status: completed
purpose: Define a reusable category system for deciding when and how AI should be used in business decision-making.

## Core Principle

AI use should not be judged case by case in an unstructured way. It should be judged by category combination.

## Category Dimensions

### 1. Domain

The business field in which the decision occurs.

- strategy
- operations
- finance
- healthcare
- investment
- product
- marketing
- market research

### 2. Decision Structure

How structured and repeatable the decision is.

- structured: repeated, measurable, rules-influenced
- semi-structured: partly data-driven, partly judgment-heavy
- unstructured: context-heavy, ambiguous, weakly measurable

### 3. Risk Level

How severe the downside is if the decision is wrong.

- low-risk: operational or internal efficiency impact
- medium-risk: meaningful customer, revenue, or cost impact
- high-risk: fairness, compliance, safety, access, or reputational impact

### 4. Scenario Condition

The operating condition under which the decision is made.

- baseline: normal operating condition
- stress: shock, surge, or deteriorating environment
- edge-case: incomplete information, drift, anomaly, or out-of-distribution case

### 5. AI Role

The degree of authority given to AI.

- assist
- recommend
- automate with guardrails

### 6. Evidence Strength

How strong the support is for claims about the system.

- strong: regulator-backed, audited, or peer-reviewed
- moderate: official company or technical documentation
- weak: reported or secondary evidence without direct primary confirmation

## Practical Formula

preferred_ai_role = domain x decision_structure x risk_level x scenario_condition x evidence_strength

## Why This Matters

This category system converts a vague case-by-case problem into a structured decision-governance problem. It provides a stable way to classify AI suitability without pretending that one rule fits all domains and situations.
