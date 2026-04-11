"""
Module B: Automation Boundary Scorer

Implements the scoring model from research/extensions/market-research/automation-boundary-scoring.md.
Input: 6 boundary dimension ratings (1-3 each)
Output: Automation assessment + override status
"""

from dataclasses import dataclass


BOUNDARY_DIMENSIONS = {
    "decision_type": {
        "label": "Decision Type",
        "question": "What type of cognitive operation does this decision require?",
        "options": {
            1: "Pure prediction: estimate or classify from defined inputs",
            2: "Prediction with embedded judgment: estimate requires contextual interpretation",
            3: "Judgment-dominant: requires values, priorities, or strategic trade-offs",
        },
    },
    "feedback_speed": {
        "label": "Feedback Speed",
        "question": "How quickly can you observe whether the decision was correct?",
        "options": {
            1: "Immediate: outcome observable within minutes to hours",
            2: "Delayed: outcome observable within days to weeks",
            3: "Absent or very delayed: months/years, or counterfactual unknowable",
        },
    },
    "error_reversibility": {
        "label": "Error Reversibility",
        "question": "If the AI makes an error, how reversible is the consequence?",
        "options": {
            1: "Fully reversible: correction with no lasting consequence",
            2: "Partially reversible: correction possible but with cost or friction",
            3: "Irreversible: permanent harm, financial loss, or reputational damage",
        },
    },
    "environment_stability": {
        "label": "Environment Stability",
        "question": "How stable is the operating environment relative to historical data?",
        "options": {
            1: "Stable: conditions match training distribution, low volatility",
            2: "Moderate volatility: periodic shifts but within historical range",
            3: "High volatility or unprecedented: conditions may diverge from any historical pattern",
        },
    },
    "accountability_type": {
        "label": "Accountability Type",
        "question": "What type of accountability applies to this decision?",
        "options": {
            1: "Process accountability: compliance with defined procedure is sufficient",
            2: "Mixed: process compliance plus outcome quality expected",
            3: "Outcome accountability: decision-maker responsible for results regardless of process",
        },
    },
    "value_content": {
        "label": "Value Content",
        "question": "How much normative/ethical judgment does this decision involve?",
        "options": {
            1: "Minimal: optimize for a defined metric with no normative ambiguity",
            2: "Moderate: metric optimization with known trade-offs requiring weighting",
            3: "High: ethical, fairness, safety, or strategic trade-offs with no single correct answer",
        },
    },
}

AUTOMATION_BANDS = [
    (6, 9, "AUTOMATABLE", "Full automation with monitoring. Human reviews exceptions and periodic audits."),
    (10, 13, "CONDITIONAL", "Automate prediction components; human judgment at decision points. Checkpoint handoff."),
    (14, 18, "NOT AUTOMATABLE", "Human decision with AI assistance. Parallel path or pre-commitment protocol."),
]

CASE_LIBRARY = [
    {"name": "Stripe fraud detection", "scores": [1, 1, 1, 1, 1, 1], "total": 6, "outcome": "Success"},
    {"name": "UPS ORION routing", "scores": [1, 1, 1, 1, 1, 1], "total": 6, "outcome": "Success"},
    {"name": "Netflix recommendations", "scores": [1, 1, 1, 1, 1, 1], "total": 6, "outcome": "Success"},
    {"name": "JPMorgan LOXM trading", "scores": [1, 1, 2, 2, 2, 1], "total": 9, "outcome": "Success"},
    {"name": "Amazon supply chain", "scores": [1, 1, 2, 2, 1, 1], "total": 8, "outcome": "Success"},
    {"name": "Zillow iBuying", "scores": [2, 3, 3, 3, 3, 2], "total": 16, "outcome": "Failed ($880M loss)"},
    {"name": "Amazon hiring tool", "scores": [3, 3, 3, 2, 3, 3], "total": 17, "outcome": "Failed (bias)"},
    {"name": "Uber ATG", "scores": [2, 1, 3, 3, 3, 3], "total": 15, "outcome": "Failed (fatality)"},
    {"name": "IBM Watson Oncology", "scores": [3, 3, 3, 2, 3, 3], "total": 17, "outcome": "Failed (unsafe)"},
    {"name": "UnitedHealth nH Predict", "scores": [2, 3, 3, 2, 3, 3], "total": 16, "outcome": "Failed (90% error)"},
    {"name": "Australian Robodebt", "scores": [1, 3, 3, 1, 3, 3], "total": 14, "outcome": "Failed (A$1.73B unlawful)"},
    {"name": "BlackRock Aladdin Copilot", "scores": [3, 3, 3, 3, 3, 3], "total": 18, "outcome": "Deliberately kept at ASSIST"},
]


@dataclass
class BoundaryOverride:
    name: str
    triggered: bool
    reason: str


@dataclass
class BoundaryResult:
    scores: dict[str, int]
    total_score: int
    raw_assessment: str
    raw_description: str
    overrides: list[BoundaryOverride]
    final_assessment: str
    final_description: str
    nearest_cases: list[dict]


def get_automation_band(total: int) -> tuple[str, str]:
    for low, high, assessment, description in AUTOMATION_BANDS:
        if low <= total <= high:
            return assessment, description
    return "NOT AUTOMATABLE", "Score out of expected range; defaulting to NOT AUTOMATABLE"


def check_boundary_overrides(scores: dict[str, int]) -> list[BoundaryOverride]:
    overrides = []

    if scores["error_reversibility"] == 3:
        overrides.append(BoundaryOverride(
            name="Irreversible errors",
            triggered=True,
            reason="Irreversible consequences require human judgment regardless of total score.",
        ))

    if scores["value_content"] == 3:
        overrides.append(BoundaryOverride(
            name="High normative content",
            triggered=True,
            reason="Ethical/fairness/safety trade-offs require human judgment.",
        ))

    if scores["accountability_type"] == 3 and scores["error_reversibility"] >= 2:
        overrides.append(BoundaryOverride(
            name="Outcome accountability + non-trivial errors",
            triggered=True,
            reason="Outcome-accountable decisions with non-trivial error consequences require human authority.",
        ))

    return overrides


def find_nearest_cases(total: int, n: int = 3) -> list[dict]:
    sorted_cases = sorted(CASE_LIBRARY, key=lambda c: abs(c["total"] - total))
    return sorted_cases[:n]


def score_boundary(scores: dict[str, int]) -> BoundaryResult:
    total = sum(scores.values())
    raw_assessment, raw_description = get_automation_band(total)
    overrides = check_boundary_overrides(scores)

    final_assessment = raw_assessment
    final_description = raw_description

    for o in overrides:
        if o.triggered:
            if final_assessment == "AUTOMATABLE":
                final_assessment = "CONDITIONAL"
                final_description = "Override applied: automation capped at CONDITIONAL."
            if "Outcome accountability" in o.name:
                final_assessment = "NOT AUTOMATABLE"
                final_description = "Override applied: outcome accountability requires human authority."

    nearest = find_nearest_cases(total)

    return BoundaryResult(
        scores=scores,
        total_score=total,
        raw_assessment=raw_assessment,
        raw_description=raw_description,
        overrides=overrides,
        final_assessment=final_assessment,
        final_description=final_description,
        nearest_cases=nearest,
    )


def format_boundary_result(result: BoundaryResult) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append("AUTOMATION BOUNDARY ASSESSMENT")
    lines.append("=" * 60)
    lines.append("")

    for key, score in result.scores.items():
        label = BOUNDARY_DIMENSIONS[key]["label"]
        desc = BOUNDARY_DIMENSIONS[key]["options"][score]
        lines.append(f"  {label}: {score}/3 — {desc}")

    lines.append(f"\n  Total Score: {result.total_score}/18")
    lines.append(f"  Raw Assessment: {result.raw_assessment}")

    triggered = [o for o in result.overrides if o.triggered]
    if triggered:
        lines.append(f"\n  OVERRIDES ({len(triggered)}):")
        for o in triggered:
            lines.append(f"    [{o.name}] {o.reason}")

    lines.append(f"\n  FINAL: {result.final_assessment}")
    lines.append(f"  {result.final_description}")

    lines.append("\n  COMPARABLE CASES:")
    for case in result.nearest_cases:
        lines.append(f"    {case['name']} (score {case['total']}) → {case['outcome']}")

    lines.append("=" * 60)
    return "\n".join(lines)
