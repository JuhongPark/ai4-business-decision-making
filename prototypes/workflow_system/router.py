"""
Task Router: Routes market research tasks to the appropriate handoff protocol
and enforces countermeasures against de facto automation.
"""

from dataclasses import dataclass

from ..scoring_engine.pj_classifier import (
    MARKET_RESEARCH_TASKS,
    TaskProfile,
    HandoffProtocol,
    PROTOCOL_DETAILS,
)


@dataclass
class WorkflowStep:
    task_id: str
    task_name: str
    profile: str
    protocol: str
    countermeasure: str
    verification_required: bool
    steps: list[str]
    time_estimate: str


COUNTERMEASURES = {
    HandoffProtocol.PARALLEL: "Pre-commitment: analyst must produce independent assessment BEFORE viewing AI output",
    HandoffProtocol.CHECKPOINT: "Checkpoint decomposition: AI output gated at each reasoning step with human validation",
    HandoffProtocol.CLEAN: "Spot-check: analyst validates source quality and assumption reasonableness",
}


def route_task(task_id: str) -> WorkflowStep:
    if task_id not in MARKET_RESEARCH_TASKS:
        raise ValueError(f"Unknown task: {task_id}. Available: {sorted(MARKET_RESEARCH_TASKS.keys())}")

    task = MARKET_RESEARCH_TASKS[task_id]
    details = PROTOCOL_DETAILS[task.protocol]

    return WorkflowStep(
        task_id=task_id,
        task_name=task.task_name,
        profile=task.profile.value,
        protocol=details["name"],
        countermeasure=COUNTERMEASURES[task.protocol],
        verification_required=task.profile != TaskProfile.PREDICTION_DOMINANT,
        steps=details["steps"],
        time_estimate=f"{task.time_estimate_minutes[0]}-{task.time_estimate_minutes[1]} min",
    )


def route_full_pipeline() -> list[WorkflowStep]:
    """Route all 18 market research tasks in order."""
    task_ids = sorted(MARKET_RESEARCH_TASKS.keys(), key=lambda x: float(x))
    return [route_task(tid) for tid in task_ids]


def format_workflow_step(step: WorkflowStep) -> str:
    lines = []
    lines.append(f"  Task {step.task_id}: {step.task_name}")
    lines.append(f"    Profile: {step.profile}")
    lines.append(f"    Protocol: {step.protocol} ({step.time_estimate})")
    lines.append(f"    Countermeasure: {step.countermeasure}")
    lines.append(f"    Verification: {'Required' if step.verification_required else 'Spot-check only'}")
    lines.append(f"    Steps:")
    for i, s in enumerate(step.steps, 1):
        lines.append(f"      {i}. {s}")
    return "\n".join(lines)


def format_full_pipeline() -> str:
    pipeline = route_full_pipeline()

    lines = []
    lines.append("=" * 60)
    lines.append("MARKET RESEARCH WORKFLOW — FULL PIPELINE")
    lines.append("=" * 60)

    current_stage = ""
    stage_names = {
        "1": "Environmental Scanning",
        "2": "Trend Identification",
        "3": "Customer Need Extraction",
        "4": "Competitive Mapping",
        "5": "Market Sizing",
        "6": "Concept Generation",
    }

    for step in pipeline:
        stage_num = step.task_id.split(".")[0]
        if stage_num != current_stage:
            current_stage = stage_num
            lines.append(f"\n{'─' * 60}")
            lines.append(f"STAGE {stage_num}: {stage_names.get(stage_num, '')}")
            lines.append(f"{'─' * 60}")
        lines.append("")
        lines.append(format_workflow_step(step))

    # Summary
    pred = sum(1 for s in pipeline if s.profile == "prediction-dominant")
    inter = sum(1 for s in pipeline if s.profile == "interleaved")
    judg = sum(1 for s in pipeline if s.profile == "judgment-dominant")

    total_min = sum(int(s.time_estimate.split("-")[0]) for s in pipeline)
    total_max = sum(int(s.time_estimate.split("-")[1].replace(" min", "")) for s in pipeline)

    lines.append(f"\n{'=' * 60}")
    lines.append("PIPELINE SUMMARY")
    lines.append(f"{'=' * 60}")
    lines.append(f"  Tasks: {len(pipeline)}")
    lines.append(f"  Prediction-dominant: {pred} (clean handoff)")
    lines.append(f"  Interleaved: {inter} (checkpoint protocol)")
    lines.append(f"  Judgment-dominant: {judg} (parallel path + pre-commitment)")
    lines.append(f"  Total verification time: {total_min}-{total_max} min ({total_min / 60:.1f}-{total_max / 60:.1f} hrs)")
    lines.append(f"  Tasks requiring verification: {sum(1 for s in pipeline if s.verification_required)}/{len(pipeline)}")
    lines.append(f"{'=' * 60}")

    return "\n".join(lines)
