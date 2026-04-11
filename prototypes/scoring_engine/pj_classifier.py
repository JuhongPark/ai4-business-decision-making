"""
Module C: Prediction-Judgment Classifier

Classifies tasks by prediction-judgment profile and recommends handoff protocols.
Based on research/extensions/market-research/prediction-judgment-interleave.md.
"""

from dataclasses import dataclass
from enum import Enum


class TaskProfile(Enum):
    PREDICTION_DOMINANT = "prediction-dominant"
    INTERLEAVED = "interleaved"
    JUDGMENT_DOMINANT = "judgment-dominant"


class HandoffProtocol(Enum):
    CLEAN = "clean_handoff"
    CHECKPOINT = "checkpoint"
    PARALLEL = "parallel_path"


PROTOCOL_DETAILS = {
    HandoffProtocol.CLEAN: {
        "name": "Clean Handoff",
        "description": "AI executes full task → delivers output with metadata → human spot-checks",
        "time_minutes": (5, 10),
        "steps": [
            "AI executes the complete task",
            "AI delivers output with source list, assumptions, confidence, and coverage gaps",
            "Human spot-checks: source quality, assumption validity, coverage gaps",
            "Human decides: Accept / Request revision / Flag for deeper review",
        ],
    },
    HandoffProtocol.CHECKPOINT: {
        "name": "Checkpoint Handoff",
        "description": "AI generates intermediate → human validates → AI integrates → repeat",
        "time_minutes": (15, 25),
        "steps": [
            "AI produces factual/analytical component",
            "Human reviews factual component for accuracy",
            "Human adds contextual interpretation or judgment",
            "AI integrates human input into next analytical step",
            "Human validates integrated output before proceeding",
        ],
    },
    HandoffProtocol.PARALLEL: {
        "name": "Parallel Path",
        "description": "AI and human generate independent analyses → human reconciles",
        "time_minutes": (20, 40),
        "steps": [
            "Human produces independent analysis WITHOUT seeing AI output (pre-commitment)",
            "AI output is revealed",
            "Human reconciles: convergence points, divergence points, AI value-add, AI deficiencies",
            "Final output is the human's reconciled analysis (human baseline, AI augments)",
        ],
    },
}


@dataclass
class ClassificationResult:
    task_name: str
    profile: TaskProfile
    protocol: HandoffProtocol
    prediction_component: str
    judgment_component: str
    handoff_point: str
    time_estimate_minutes: tuple[int, int]


# Pre-classified market research tasks from the interleave mapping
MARKET_RESEARCH_TASKS = {
    "1.1": ClassificationResult("Source identification", TaskProfile.PREDICTION_DOMINANT, HandoffProtocol.CLEAN, "Identify and collect sources", "Minimal: criteria pre-specified", "AI delivers list; human spot-checks quality", (5, 10)),
    "1.2": ClassificationResult("Regulatory assessment", TaskProfile.INTERLEAVED, HandoffProtocol.CHECKPOINT, "Identify regulations and changes", "Interpret compliance implications", "AI delivers landscape → human interprets implications", (15, 25)),
    "1.3": ClassificationResult("Signal-noise discrimination", TaskProfile.JUDGMENT_DOMINANT, HandoffProtocol.PARALLEL, "Identify candidate signals", "Determine durability; requires industry intuition", "AI generates signals; human independently assesses; reconcile", (20, 40)),
    "2.1": ClassificationResult("Trend pattern recognition", TaskProfile.PREDICTION_DOMINANT, HandoffProtocol.CLEAN, "Detect temporal patterns", "Minimal: primarily statistical", "AI delivers patterns; human validates data quality", (5, 10)),
    "2.2": ClassificationResult("Trend trajectory estimation", TaskProfile.INTERLEAVED, HandoffProtocol.CHECKPOINT, "Extrapolate direction and magnitude", "Select analogies; assess applicability", "AI generates estimate → human validates assumptions", (15, 25)),
    "2.3": ClassificationResult("Trend significance assessment", TaskProfile.JUDGMENT_DOMINANT, HandoffProtocol.PARALLEL, "Rank by quantitative indicators", "Assess strategic relevance", "AI ranks by data; human ranks by strategy; reconcile", (20, 40)),
    "3.1": ClassificationResult("Feedback synthesis", TaskProfile.INTERLEAVED, HandoffProtocol.CHECKPOINT, "Extract themes from data", "Interpret themes for product decisions", "AI extracts → human validates → AI refines", (15, 25)),
    "3.2": ClassificationResult("Latent need identification", TaskProfile.JUDGMENT_DOMINANT, HandoffProtocol.PARALLEL, "Identify behavioral patterns", "Infer causal motivation (JTBD)", "AI proposes; human proposes independently; compare", (20, 40)),
    "3.3": ClassificationResult("Need prioritization", TaskProfile.INTERLEAVED, HandoffProtocol.CHECKPOINT, "Score against quantitative criteria", "Weight criteria, resolve trade-offs", "AI scores → human reviews weights → final prioritization", (15, 25)),
    "4.1": ClassificationResult("Competitor capability", TaskProfile.PREDICTION_DOMINANT, HandoffProtocol.CLEAN, "Compile competitor data", "Minimal: verifiable information synthesis", "AI delivers profiles; human validates currency", (5, 10)),
    "4.2": ClassificationResult("White space identification", TaskProfile.INTERLEAVED, HandoffProtocol.CHECKPOINT, "Cross-reference need and capability maps", "Assess whether gaps are real opportunities", "AI identifies gaps → human assesses genuineness", (15, 25)),
    "4.3": ClassificationResult("Competitive response prediction", TaskProfile.JUDGMENT_DOMINANT, HandoffProtocol.PARALLEL, "Model likely moves from history", "Assess intent, risk tolerance, priorities", "AI generates scenarios; human adds intuition; reconcile", (20, 40)),
    "5.1": ClassificationResult("Market size estimation", TaskProfile.PREDICTION_DOMINANT, HandoffProtocol.CLEAN, "Calculate from data and assumptions", "Minimal: primarily quantitative", "AI delivers estimate; human validates assumptions", (5, 10)),
    "5.2": ClassificationResult("WTP assessment", TaskProfile.INTERLEAVED, HandoffProtocol.CHECKPOINT, "Estimate from data and analogies", "Select appropriate analogies", "AI generates range → human validates analogy selection", (15, 25)),
    "5.3": ClassificationResult("Opportunity prioritization", TaskProfile.JUDGMENT_DOMINANT, HandoffProtocol.PARALLEL, "Rank by quantitative scores", "Weight dimensions, make go/no-go", "AI ranks quantitatively; human ranks strategically; reconcile", (20, 40)),
    "6.1": ClassificationResult("Concept generation", TaskProfile.JUDGMENT_DOMINANT, HandoffProtocol.PARALLEL, "Generate from need-capability map", "Evaluate novelty and strategic alignment", "AI generates; human generates independently; merge", (20, 40)),
    "6.2": ClassificationResult("Feasibility assessment", TaskProfile.INTERLEAVED, HandoffProtocol.CHECKPOINT, "Evaluate against constraints", "Assess constraint flexibility", "AI evaluates → human assesses flexibility → joint score", (15, 25)),
    "6.3": ClassificationResult("Concept screening", TaskProfile.JUDGMENT_DOMINANT, HandoffProtocol.PARALLEL, "Score on defined criteria", "Make go/no-go with resource implications", "AI scores; human assesses independently; AI is one input", (20, 40)),
}


def classify_task(decision_type: int, feedback: int, value_content: int) -> ClassificationResult:
    """Classify a generic task based on key dimensions."""
    if decision_type == 1 and value_content <= 1:
        profile = TaskProfile.PREDICTION_DOMINANT
        protocol = HandoffProtocol.CLEAN
        time_est = (5, 10)
    elif decision_type == 3 or value_content == 3:
        profile = TaskProfile.JUDGMENT_DOMINANT
        protocol = HandoffProtocol.PARALLEL
        time_est = (20, 40)
    else:
        profile = TaskProfile.INTERLEAVED
        protocol = HandoffProtocol.CHECKPOINT
        time_est = (15, 25)

    return ClassificationResult(
        task_name="Custom task",
        profile=profile,
        protocol=protocol,
        prediction_component="(to be specified)",
        judgment_component="(to be specified)",
        handoff_point="(to be specified)",
        time_estimate_minutes=time_est,
    )


def get_protocol_steps(protocol: HandoffProtocol) -> list[str]:
    return PROTOCOL_DETAILS[protocol]["steps"]


def format_classification(result: ClassificationResult) -> str:
    details = PROTOCOL_DETAILS[result.protocol]
    lines = []
    lines.append(f"Task: {result.task_name}")
    lines.append(f"Profile: {result.profile.value}")
    lines.append(f"Protocol: {details['name']}")
    lines.append(f"Time estimate: {result.time_estimate_minutes[0]}-{result.time_estimate_minutes[1]} min")
    lines.append(f"Prediction component: {result.prediction_component}")
    lines.append(f"Judgment component: {result.judgment_component}")
    lines.append(f"Handoff point: {result.handoff_point}")
    lines.append(f"\nProtocol steps:")
    for i, step in enumerate(details["steps"], 1):
        lines.append(f"  {i}. {step}")
    return "\n".join(lines)
