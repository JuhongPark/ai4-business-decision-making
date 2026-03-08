# Phase 16: Usage Matrix

status: completed
purpose: Show when and how AI should be used by category combination.

## Matrix

| Category Pattern | Preferred Mode | How to Use AI | When to Limit It | Typical Domains |
| --- | --- | --- | --- | --- |
| structured + low-risk + baseline + moderate/strong evidence | recommend or automate with guardrails | allow AI to execute repeated decisions within clear rules | limit when data quality degrades or objectives conflict | operations, bounded marketing |
| structured + low-risk + stress | recommend or automate with guardrails plus stronger human override | use AI for speed, prioritization, and load balancing | limit when disruption creates unstable inputs | operations |
| semi-structured + medium-risk + baseline | assist or recommend | use AI for synthesis, scoring, and prioritization support | limit when metrics are weak proxies for actual value | product, marketing, some finance workflows |
| semi-structured + medium-risk + edge-case | assist | use AI as one signal among several | limit when ambiguity or novel conditions dominate | product, market research |
| high-risk + baseline + strong evidence | assist or tightly governed recommend | use AI for screening, triage support, or recommendation support with auditable review | limit when explainability or fairness review is weak | finance, healthcare, investment |
| high-risk + stress | assist | use AI to surface risk and support prioritization, but keep final authority human-led | limit when model uncertainty rises under pressure | finance, healthcare |
| high-risk + edge-case | assist | use AI only as a weak supporting signal | limit aggressively because safety, fairness, or compliance risk dominates | finance, healthcare, investment |
| unstructured + ambiguous + moderate or weak evidence | assist | use AI for synthesis, drafting, and option generation | do not treat outputs as autonomous decisions | strategy, market research |

## Reading Rule

The matrix should be read from left to right:

1. identify the category pattern
2. assign the preferred mode
3. specify how AI should be used
4. specify the trigger for limiting or fallback

## Main Takeaway

The correct question is not “Which domain should use AI?” The correct question is “Which category combination justifies which level of AI authority?”
