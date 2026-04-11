"""
Module A: 6-Dimensional Delegation Scorer

Implements the scoring model from research/core/taxonomy/scoring-sheet.md.
Input: 6 dimension ratings (1-3 each)
Output: Recommended authority level + override status + justification
"""

from dataclasses import dataclass


DIMENSIONS = {
    "domain": {
        "label": "Domain",
        "question": "What business domain does this AI application serve?",
        "options": {
            1: "Operations, logistics, or routine marketing — well-structured domain with strong feedback",
            2: "Finance, product, or market research — moderate structure with mixed evidence quality",
            3: "Strategy, healthcare, investment, or compliance — high judgment, high consequence",
        },
    },
    "decision_structure": {
        "label": "Decision Structure",
        "question": "How structured is the decision the AI informs?",
        "options": {
            1: "Structured: clear inputs, defined rules, repeatable process",
            2: "Semi-structured: defined process but requires contextual interpretation",
            3: "Unstructured: ambiguous inputs, no standard process, requires judgment",
        },
    },
    "risk_level": {
        "label": "Risk Level",
        "question": "What is the risk level if the AI produces an incorrect output?",
        "options": {
            1: "Low: operational inefficiency, minor cost, easily correctable",
            2: "Medium: revenue impact, customer dissatisfaction, reputational friction",
            3: "High: regulatory violation, safety hazard, discrimination, major financial loss",
        },
    },
    "scenario_condition": {
        "label": "Scenario Condition",
        "question": "How closely do current conditions match the AI's training/validation data?",
        "options": {
            1: "Baseline: conditions are stable and match historical patterns",
            2: "Stress: conditions are under pressure but within historical range",
            3: "Edge-case: unprecedented conditions, outside historical distribution",
        },
    },
    "evidence_strength": {
        "label": "Evidence Strength",
        "question": "How strong is the evidence supporting the AI system's reliability?",
        "options": {
            1: "Weak: limited testing, no independent validation, anecdotal performance claims",
            2: "Moderate: internal testing with documented results, some independent review",
            3: "Strong: peer-reviewed validation, regulatory approval, extensive track record",
        },
    },
    "governance_readiness": {
        "label": "Governance Readiness",
        "question": "How mature is the governance infrastructure around this AI system?",
        "options": {
            1: "Weak: no formal oversight, no audit trail, no escalation path",
            2: "Adequate: designated oversight, basic monitoring, defined escalation",
            3: "Strong: formal governance body, continuous monitoring, tested escalation, regular review",
        },
    },
}

AUTHORITY_BANDS = [
    (5, 8, "ASSIST", "AI provides analysis and drafts; human retains final authority"),
    (9, 11, "ASSIST or RECOMMEND", "AI provides structured recommendations; human reviews before action"),
    (12, 15, "RECOMMEND or AUTOMATE WITH GUARDRAILS", "AI acts within predefined boundaries; human handles exceptions"),
]


@dataclass
class Override:
    name: str
    triggered: bool
    reason: str
    action: str


@dataclass
class DelegationResult:
    scores: dict[str, int]
    total_score: int
    raw_authority: str
    raw_description: str
    overrides: list[Override]
    final_authority: str
    final_description: str


def check_overrides(scores: dict[str, int]) -> list[Override]:
    overrides = []

    # Override 1: High risk + weak governance → cap at ASSIST
    if scores["risk_level"] == 3 and scores["governance_readiness"] == 1:
        overrides.append(Override(
            name="High risk + weak governance",
            triggered=True,
            reason="High-risk decisions require strong governance. Weak governance cannot support elevated authority.",
            action="Cap at ASSIST",
        ))

    # Override 2: Edge-case scenario → cap at ASSIST
    if scores["scenario_condition"] == 3:
        overrides.append(Override(
            name="Edge-case scenario",
            triggered=True,
            reason="Unprecedented conditions exceed AI's validated envelope. Human judgment required.",
            action="Cap at ASSIST",
        ))

    # Override 3: Weak evidence in consequential decision → reduce one level
    if scores["evidence_strength"] == 1 and scores["risk_level"] >= 2:
        overrides.append(Override(
            name="Weak evidence + consequential decision",
            triggered=True,
            reason="Insufficient evidence to justify current authority level for this risk profile.",
            action="Reduce one level",
        ))

    return overrides


def get_authority_band(total: int) -> tuple[str, str]:
    for low, high, authority, description in AUTHORITY_BANDS:
        if low <= total <= high:
            return authority, description
    return "ASSIST", "Score out of expected range; defaulting to ASSIST"


def apply_overrides(raw_authority: str, overrides: list[Override]) -> tuple[str, str]:
    authority = raw_authority
    for override in overrides:
        if not override.triggered:
            continue
        if override.action == "Cap at ASSIST":
            authority = "ASSIST"
        elif override.action == "Reduce one level":
            if "AUTOMATE" in authority:
                authority = "RECOMMEND"
            elif "RECOMMEND" in authority and "ASSIST" not in authority:
                authority = "ASSIST or RECOMMEND"
            elif "ASSIST or RECOMMEND" in authority:
                authority = "ASSIST"

    descriptions = {
        "ASSIST": "AI provides analysis and drafts; human retains final authority",
        "ASSIST or RECOMMEND": "AI provides structured recommendations; human reviews before action",
        "RECOMMEND": "AI provides structured recommendations; human reviews before action",
        "RECOMMEND or AUTOMATE WITH GUARDRAILS": "AI acts within predefined boundaries; human handles exceptions",
    }
    return authority, descriptions.get(authority, "")


def score_delegation(scores: dict[str, int]) -> DelegationResult:
    total = sum(scores.values())
    raw_authority, raw_description = get_authority_band(total)
    overrides = check_overrides(scores)
    final_authority, final_description = apply_overrides(raw_authority, overrides)

    if any(o.triggered for o in overrides):
        pass  # already applied
    else:
        final_authority = raw_authority
        final_description = raw_description

    return DelegationResult(
        scores=scores,
        total_score=total,
        raw_authority=raw_authority,
        raw_description=raw_description,
        overrides=overrides,
        final_authority=final_authority,
        final_description=final_description,
    )


def format_result(result: DelegationResult) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append("DELEGATION SCORING RESULT")
    lines.append("=" * 60)
    lines.append("")

    for key, score in result.scores.items():
        label = DIMENSIONS[key]["label"]
        desc = DIMENSIONS[key]["options"][score]
        lines.append(f"  {label}: {score}/3 — {desc}")

    lines.append(f"\n  Total Score: {result.total_score}/18")
    lines.append(f"  Raw Authority: {result.raw_authority}")

    triggered = [o for o in result.overrides if o.triggered]
    if triggered:
        lines.append(f"\n  OVERRIDES TRIGGERED ({len(triggered)}):")
        for o in triggered:
            lines.append(f"    [{o.name}] {o.reason}")
            lines.append(f"    → Action: {o.action}")

    lines.append(f"\n  FINAL AUTHORITY: {result.final_authority}")
    lines.append(f"  {result.final_description}")
    lines.append("=" * 60)

    return "\n".join(lines)
