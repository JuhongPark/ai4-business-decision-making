#!/usr/bin/env python3
"""
Layer 1: Formal Verification — Complete Enumeration

Exhaustively enumerates all possible scoring configurations and verifies
that no configuration violates the framework's axioms.
"""

from itertools import product

import sys
sys.path.insert(0, ".")

from prototypes.scoring_engine.delegation_scorer import score_delegation
from prototypes.scoring_engine.automation_boundary import score_boundary


def verify_delegation_axioms():
    """Enumerate all 729 delegation configurations and verify axioms."""
    dims = ["domain", "decision_structure", "risk_level",
            "scenario_condition", "evidence_strength", "governance_readiness"]

    violations = []
    band_distribution = {}
    override_fire_count = {"high_risk_weak_gov": 0, "edge_case": 0, "weak_evidence": 0}
    total = 0

    for combo in product(range(1, 4), repeat=6):
        total += 1
        scores = dict(zip(dims, combo))
        result = score_delegation(scores)

        # Track distribution
        band_distribution[result.final_authority] = band_distribution.get(result.final_authority, 0) + 1

        # Track override firing
        for o in result.overrides:
            if o.triggered and "High risk" in o.name:
                override_fire_count["high_risk_weak_gov"] += 1
            if o.triggered and "Edge-case" in o.name:
                override_fire_count["edge_case"] += 1
            if o.triggered and "Weak evidence" in o.name:
                override_fire_count["weak_evidence"] += 1

        # Axiom 1: High risk (3) + weak governance (1) → must be ASSIST
        if scores["risk_level"] == 3 and scores["governance_readiness"] == 1:
            if result.final_authority != "ASSIST":
                violations.append(f"AXIOM 1 FAIL: {scores} → {result.final_authority}")

        # Axiom 2: Edge-case scenario (3) → must be ASSIST
        if scores["scenario_condition"] == 3:
            if result.final_authority != "ASSIST":
                violations.append(f"AXIOM 2 FAIL: {scores} → {result.final_authority}")

        # Axiom 3: Weak evidence (1) + risk ≥ 2 → cannot be highest band
        if scores["evidence_strength"] == 1 and scores["risk_level"] >= 2:
            if "AUTOMATE" in result.final_authority and "RECOMMEND" not in result.final_authority:
                violations.append(f"AXIOM 3 FAIL: {scores} → {result.final_authority}")

    return total, violations, band_distribution, override_fire_count


def verify_boundary_axioms():
    """Enumerate all 729 boundary configurations and verify axioms."""
    dims = ["decision_type", "feedback_speed", "error_reversibility",
            "environment_stability", "accountability_type", "value_content"]

    violations = []
    band_distribution = {}
    total = 0

    for combo in product(range(1, 4), repeat=6):
        total += 1
        scores = dict(zip(dims, combo))
        result = score_boundary(scores)

        band_distribution[result.final_assessment] = band_distribution.get(result.final_assessment, 0) + 1

        # Axiom: Irreversible (3) → cannot be AUTOMATABLE
        if scores["error_reversibility"] == 3:
            if result.final_assessment == "AUTOMATABLE":
                violations.append(f"BOUNDARY AXIOM 1 FAIL: {scores} → {result.final_assessment}")

        # Axiom: High value (3) → cannot be AUTOMATABLE
        if scores["value_content"] == 3:
            if result.final_assessment == "AUTOMATABLE":
                violations.append(f"BOUNDARY AXIOM 2 FAIL: {scores} → {result.final_assessment}")

        # Axiom: Outcome accountability (3) + reversibility ≥ 2 → NOT AUTOMATABLE
        if scores["accountability_type"] == 3 and scores["error_reversibility"] >= 2:
            if result.final_assessment != "NOT AUTOMATABLE":
                violations.append(f"BOUNDARY AXIOM 3 FAIL: {scores} → {result.final_assessment}")

    return total, violations, band_distribution


def verify_cross_tool_consistency():
    """Check directional consistency between delegation and boundary tools."""
    d_dims = ["domain", "decision_structure", "risk_level",
              "scenario_condition", "evidence_strength", "governance_readiness"]
    b_dims = ["decision_type", "feedback_speed", "error_reversibility",
              "environment_stability", "accountability_type", "value_content"]

    inconsistencies = 0
    total_checked = 0

    # Sample 1000 random configurations with parallel scoring
    import random
    random.seed(42)

    for _ in range(1000):
        d_scores = {d: random.randint(1, 3) for d in d_dims}
        b_scores = {b: random.randint(1, 3) for b in b_dims}

        d_result = score_delegation(d_scores)
        b_result = score_boundary(b_scores)

        total_checked += 1

        # Check: if boundary says NOT AUTOMATABLE, delegation should not say AUTOMATE
        if b_result.final_assessment == "NOT AUTOMATABLE":
            if "AUTOMATE" in d_result.final_authority and "RECOMMEND" not in d_result.final_authority:
                inconsistencies += 1

    return total_checked, inconsistencies


def run_verification():
    print("=" * 70)
    print("LAYER 1: FORMAL VERIFICATION — COMPLETE ENUMERATION")
    print("=" * 70)

    # Delegation framework
    d_total, d_violations, d_dist, d_overrides = verify_delegation_axioms()
    print(f"\n  DELEGATION FRAMEWORK")
    print(f"  Configurations enumerated: {d_total}")
    print(f"  Axiom violations: {len(d_violations)}")
    if d_violations:
        for v in d_violations[:5]:
            print(f"    {v}")
    else:
        print(f"    ALL AXIOMS VERIFIED — no violations found")

    print(f"\n  Authority band distribution:")
    for band, count in sorted(d_dist.items(), key=lambda x: -x[1]):
        pct = count / d_total * 100
        print(f"    {band:<45} {count:>4} ({pct:.1f}%)")

    print(f"\n  Override firing rates:")
    for rule, count in d_overrides.items():
        pct = count / d_total * 100
        print(f"    {rule:<30} {count:>4} ({pct:.1f}%)")

    # Boundary tool
    b_total, b_violations, b_dist = verify_boundary_axioms()
    print(f"\n  AUTOMATION BOUNDARY TOOL")
    print(f"  Configurations enumerated: {b_total}")
    print(f"  Axiom violations: {len(b_violations)}")
    if b_violations:
        for v in b_violations[:5]:
            print(f"    {v}")
    else:
        print(f"    ALL AXIOMS VERIFIED — no violations found")

    print(f"\n  Assessment distribution:")
    for band, count in sorted(b_dist.items(), key=lambda x: -x[1]):
        pct = count / b_total * 100
        print(f"    {band:<20} {count:>4} ({pct:.1f}%)")

    # Cross-tool consistency
    ct_total, ct_inconsistencies = verify_cross_tool_consistency()
    print(f"\n  CROSS-TOOL CONSISTENCY")
    print(f"  Sampled configurations: {ct_total}")
    print(f"  Directional inconsistencies: {ct_inconsistencies}")
    print(f"  Consistency rate: {(ct_total - ct_inconsistencies) / ct_total * 100:.1f}%")

    print(f"\n{'=' * 70}")
    status = "PASS" if not d_violations and not b_violations else "FAIL"
    print(f"  FORMAL VERIFICATION: {status}")
    print(f"  {d_total + b_total} total configurations verified")
    print(f"  {len(d_violations) + len(b_violations)} axiom violations")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    run_verification()
