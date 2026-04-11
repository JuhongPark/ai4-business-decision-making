#!/usr/bin/env python3
"""
Delegation Scoring Engine — CLI Interface

Usage:
  python -m prototypes.scoring_engine.cli delegation
  python -m prototypes.scoring_engine.cli boundary
  python -m prototypes.scoring_engine.cli classify
  python -m prototypes.scoring_engine.cli full          # run all three assessments
  python -m prototypes.scoring_engine.cli demo          # run with example scores
  python -m prototypes.scoring_engine.cli market-research <task_id>   # lookup pre-classified task
"""

import sys

from .delegation_scorer import (
    DIMENSIONS,
    score_delegation,
    format_result,
)
from .automation_boundary import (
    BOUNDARY_DIMENSIONS,
    score_boundary,
    format_boundary_result,
)
from .pj_classifier import (
    MARKET_RESEARCH_TASKS,
    classify_task,
    format_classification,
)


def prompt_scores(dimensions: dict) -> dict[str, int]:
    scores = {}
    for key, dim in dimensions.items():
        print(f"\n{dim['label']}: {dim['question']}")
        for val, desc in dim["options"].items():
            print(f"  [{val}] {desc}")
        while True:
            try:
                choice = int(input(f"  Score (1-3): "))
                if choice in (1, 2, 3):
                    scores[key] = choice
                    break
            except (ValueError, EOFError):
                pass
            print("  Please enter 1, 2, or 3.")
    return scores


def run_delegation():
    print("\n--- 6-DIMENSIONAL DELEGATION SCORING ---\n")
    scores = prompt_scores(DIMENSIONS)
    result = score_delegation(scores)
    print("\n" + format_result(result))
    return result


def run_boundary():
    print("\n--- AUTOMATION BOUNDARY ASSESSMENT ---\n")
    scores = prompt_scores(BOUNDARY_DIMENSIONS)
    result = score_boundary(scores)
    print("\n" + format_boundary_result(result))
    return result


def run_classify():
    print("\n--- PREDICTION-JUDGMENT CLASSIFICATION ---\n")
    print("Enter key dimensions to classify a task:\n")
    dt = int(input("Decision type (1=prediction, 2=mixed, 3=judgment): "))
    fb = int(input("Feedback speed (1=immediate, 2=delayed, 3=absent): "))
    vc = int(input("Value content (1=minimal, 2=moderate, 3=high): "))
    result = classify_task(dt, fb, vc)
    print("\n" + format_classification(result))
    return result


def run_demo():
    """Run all three assessments with example scores (Zillow iBuying case)."""
    print("\n" + "=" * 60)
    print("DEMO: Zillow iBuying — Automated Home Purchase Decisions")
    print("=" * 60)

    # Delegation scoring
    delegation_scores = {
        "domain": 2,            # Finance — moderate structure
        "decision_structure": 1, # Unstructured — volatile market
        "risk_level": 3,        # High — major financial loss
        "scenario_condition": 3, # Edge-case — unprecedented market
        "evidence_strength": 1,  # Weak — model not validated for volatility
        "governance_readiness": 1, # Weak — no override mechanisms
    }
    d_result = score_delegation(delegation_scores)
    print("\n" + format_result(d_result))

    # Automation boundary
    boundary_scores = {
        "decision_type": 2,        # Prediction with judgment
        "feedback_speed": 3,       # Months to sell
        "error_reversibility": 3,  # Irreversible — capital committed
        "environment_stability": 3, # Unprecedented volatility
        "accountability_type": 3,   # Outcome accountability
        "value_content": 2,        # Financial trade-off
    }
    b_result = score_boundary(boundary_scores)
    print("\n" + format_boundary_result(b_result))

    # Prediction-judgment classification
    pj_result = classify_task(
        decision_type=2,  # Prediction with judgment
        feedback=3,       # Absent/very delayed
        value_content=2,  # Moderate
    )
    print(f"\n--- TASK CLASSIFICATION ---\n")
    print(format_classification(pj_result))

    print("\n" + "=" * 60)
    print("DEMO SUMMARY: Zillow iBuying")
    print(f"  Delegation: {d_result.final_authority} (overrides triggered)")
    print(f"  Automation: {b_result.final_assessment}")
    print(f"  Task profile: {pj_result.profile.value}")
    print(f"\n  Actual outcome: $880M loss, business shutdown, 25% workforce reduction")
    print(f"  Framework prediction: Both tools correctly identify this as non-automatable.")
    print("=" * 60)


def run_market_research_lookup(task_id: str):
    """Look up a pre-classified market research task."""
    if task_id in MARKET_RESEARCH_TASKS:
        result = MARKET_RESEARCH_TASKS[task_id]
        print(f"\n--- MARKET RESEARCH TASK {task_id} ---\n")
        print(format_classification(result))
    else:
        print(f"Unknown task ID: {task_id}")
        print(f"Available: {', '.join(sorted(MARKET_RESEARCH_TASKS.keys()))}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    command = sys.argv[1]

    if command == "delegation":
        run_delegation()
    elif command == "boundary":
        run_boundary()
    elif command == "classify":
        run_classify()
    elif command == "full":
        run_delegation()
        run_boundary()
        run_classify()
    elif command == "demo":
        run_demo()
    elif command == "market-research":
        task_id = sys.argv[2] if len(sys.argv) > 2 else None
        if task_id:
            run_market_research_lookup(task_id)
        else:
            print("Available tasks:")
            for tid, task in sorted(MARKET_RESEARCH_TASKS.items()):
                print(f"  {tid}: {task.task_name} [{task.profile.value}]")
    else:
        print(f"Unknown command: {command}")
        print(__doc__)


if __name__ == "__main__":
    main()
