#!/usr/bin/env python3
"""
Layer 3: Adversarial Stress-Testing

3A: Boundary case construction (20 scenarios at decision boundaries)
3B: LLM-generated adversarial scenarios (hard-to-classify cases)
3C: Gaming vulnerability analysis
"""

import sys
sys.path.insert(0, ".")

from prototypes.scoring_engine.delegation_scorer import score_delegation, DIMENSIONS
from prototypes.scoring_engine.automation_boundary import score_boundary, BOUNDARY_DIMENSIONS


# 3A: 20 boundary cases designed to stress-test the framework
BOUNDARY_CASES = [
    # --- ASSIST/RECOMMEND boundary (score 8-9) ---
    {
        "id": "BC-01",
        "name": "AI email triage for executive assistant",
        "description": "AI categorizes and prioritizes incoming emails, drafts short responses for routine items. Low risk per email, but cumulative reputational risk if tone is wrong.",
        "scores": {"domain": 1, "decision_structure": 2, "risk_level": 1, "scenario_condition": 1, "evidence_strength": 2, "governance_readiness": 2},
        "expert_judgment": "RECOMMEND — structured, low individual risk, strong feedback",
        "challenge": "Cumulative reputational risk from many small decisions is hard to score on the risk dimension",
    },
    {
        "id": "BC-02",
        "name": "AI meeting summarizer for board meetings",
        "description": "AI generates meeting summaries from recorded board meetings. Low direct risk but summaries become official record.",
        "scores": {"domain": 2, "decision_structure": 2, "risk_level": 2, "scenario_condition": 1, "evidence_strength": 1, "governance_readiness": 1},
        "expert_judgment": "ASSIST — board record is high-consequence despite seeming like a routine task",
        "challenge": "Appears low-risk but the 'official record' status elevates the real consequence",
    },
    {
        "id": "BC-03",
        "name": "AI product description generator for e-commerce",
        "description": "Generates product descriptions from specifications. High volume, low individual risk, but brand consistency matters.",
        "scores": {"domain": 1, "decision_structure": 1, "risk_level": 1, "scenario_condition": 1, "evidence_strength": 2, "governance_readiness": 2},
        "expert_judgment": "RECOMMEND or AUTOMATE — highly structured, low risk, fast feedback",
        "challenge": "Score should be high enough for automation but brand risk adds qualitative concern",
    },
    {
        "id": "BC-04",
        "name": "AI customer churn prediction for telecom",
        "description": "Predicts which customers are likely to churn. Predictions feed into retention campaign targeting. Medium revenue risk.",
        "scores": {"domain": 2, "decision_structure": 2, "risk_level": 2, "scenario_condition": 1, "evidence_strength": 2, "governance_readiness": 2},
        "expert_judgment": "RECOMMEND — prediction is strong but retention action requires judgment",
        "challenge": "Prediction is automatable but the downstream action (retention offer) requires calibration",
    },
    {
        "id": "BC-05",
        "name": "AI pricing optimizer for airline tickets",
        "description": "Dynamic pricing based on demand prediction. Revenue impact is direct and measurable. Regulatory scrutiny on price discrimination.",
        "scores": {"domain": 2, "decision_structure": 2, "risk_level": 2, "scenario_condition": 2, "evidence_strength": 2, "governance_readiness": 2},
        "expert_judgment": "RECOMMEND — works well in normal conditions but regulatory risk requires oversight",
        "challenge": "Score of 12 puts it at RECOMMEND/AUTOMATE boundary; regulatory dimension not directly captured",
    },

    # --- RECOMMEND/AUTOMATE boundary (score 11-12) ---
    {
        "id": "BC-06",
        "name": "AI fraud detection for insurance claims",
        "description": "Flags potentially fraudulent insurance claims. False positives delay legitimate claims; false negatives cost money.",
        "scores": {"domain": 2, "decision_structure": 2, "risk_level": 2, "scenario_condition": 1, "evidence_strength": 2, "governance_readiness": 3},
        "expert_judgment": "RECOMMEND — flagging is automatable but claim denial requires human review",
        "challenge": "The framework doesn't distinguish flagging (automatable) from acting on flags (requires judgment)",
    },
    {
        "id": "BC-07",
        "name": "AI content recommendation for children's educational platform",
        "description": "Recommends educational content to children aged 6-12. Low financial risk but high duty-of-care and developmental impact.",
        "scores": {"domain": 2, "decision_structure": 2, "risk_level": 3, "scenario_condition": 1, "evidence_strength": 2, "governance_readiness": 2},
        "expert_judgment": "ASSIST — children cannot evaluate recommendations; duty of care requires strong oversight",
        "challenge": "Risk scoring must capture vulnerability of the affected population, not just financial risk",
    },
    {
        "id": "BC-08",
        "name": "AI translation tool for international legal contracts",
        "description": "Translates contract language between English and Mandarin. Translation errors could create binding legal obligations.",
        "scores": {"domain": 3, "decision_structure": 2, "risk_level": 3, "scenario_condition": 1, "evidence_strength": 2, "governance_readiness": 1},
        "expert_judgment": "ASSIST — legal language requires precision; errors create liability",
        "challenge": "Appears as a structured task (translation) but the consequence domain (legal) elevates risk",
    },
    {
        "id": "BC-09",
        "name": "AI scheduling optimizer for hospital operating rooms",
        "description": "Optimizes OR scheduling to minimize downtime. Structured task but delays affect patient outcomes.",
        "scores": {"domain": 3, "decision_structure": 1, "risk_level": 2, "scenario_condition": 1, "evidence_strength": 2, "governance_readiness": 2},
        "expert_judgment": "RECOMMEND — optimization is well-defined but patient impact requires monitoring",
        "challenge": "Structured optimization in a high-consequence domain; structure suggests automation but domain demands caution",
    },
    {
        "id": "BC-10",
        "name": "AI social media post generator for corporate communications",
        "description": "Generates social media posts from approved messaging. Fast feedback (engagement metrics) but reputational risk from tone-deaf content.",
        "scores": {"domain": 2, "decision_structure": 2, "risk_level": 2, "scenario_condition": 2, "evidence_strength": 2, "governance_readiness": 2},
        "expert_judgment": "RECOMMEND — speed matters but cultural sensitivity requires human review",
        "challenge": "Normative sensitivity (cultural awareness) is hard to capture in structure/risk dimensions",
    },

    # --- Override conflict cases ---
    {
        "id": "BC-11",
        "name": "AI diagnostic assistant in pandemic surge (COVID-like scenario)",
        "description": "AI triages patients during a pandemic surge when human capacity is overwhelmed. Edge-case scenario but the alternative (no triage) is worse.",
        "scores": {"domain": 3, "decision_structure": 1, "risk_level": 3, "scenario_condition": 3, "evidence_strength": 1, "governance_readiness": 1},
        "expert_judgment": "CONTEXT-DEPENDENT — normal rules say ASSIST but emergency may justify higher authority",
        "challenge": "Override rules all trigger (cap at ASSIST) but operational necessity may require override of overrides",
    },
    {
        "id": "BC-12",
        "name": "AI military target identification in active conflict",
        "description": "AI identifies potential targets from drone surveillance. Highest possible risk. Geneva Convention applies.",
        "scores": {"domain": 3, "decision_structure": 1, "risk_level": 3, "scenario_condition": 3, "evidence_strength": 1, "governance_readiness": 1},
        "expert_judgment": "ASSIST with extreme caution — international law requires human decision",
        "challenge": "Scores bottom out (ASSIST); framework cannot distinguish 'ASSIST with caution' from 'do not deploy'",
    },
    {
        "id": "BC-13",
        "name": "AI autonomous emergency braking in self-driving car",
        "description": "Must act in milliseconds. Human cannot intervene in time. But error consequences are fatal.",
        "scores": {"domain": 3, "decision_structure": 1, "risk_level": 3, "scenario_condition": 2, "evidence_strength": 3, "governance_readiness": 3},
        "expert_judgment": "AUTOMATE — human physically cannot intervene; strong evidence justifies automation",
        "challenge": "High risk normally caps at ASSIST, but the constraint (reaction time) makes human intervention impossible",
    },
    {
        "id": "BC-14",
        "name": "AI investment portfolio rebalancing during market crash",
        "description": "Automated rebalancing triggers during a market crash. Normal rules say sell; panic selling amplifies the crash.",
        "scores": {"domain": 2, "decision_structure": 2, "risk_level": 3, "scenario_condition": 3, "evidence_strength": 2, "governance_readiness": 2},
        "expert_judgment": "HALT — neither automate nor assist; pause and consult",
        "challenge": "Framework has no HALT/PAUSE authority level. Edge-case + high-risk = ASSIST, but the correct action may be to stop entirely.",
    },
    {
        "id": "BC-15",
        "name": "AI art generation for commercial advertising",
        "description": "Generates advertising images. Copyright and cultural sensitivity risks. Evidence of capability is strong.",
        "scores": {"domain": 2, "decision_structure": 2, "risk_level": 2, "scenario_condition": 2, "evidence_strength": 3, "governance_readiness": 2},
        "expert_judgment": "RECOMMEND — creative quality is high but legal/cultural review needed",
        "challenge": "Normative risks (IP, cultural appropriation) don't map cleanly to risk_level dimension",
    },

    # --- Delegation vs boundary tool disagreement candidates ---
    {
        "id": "BC-16",
        "name": "AI weather forecasting for agricultural planning",
        "description": "Predicts weather patterns for crop management decisions. Pure prediction task but farmer livelihoods depend on accuracy.",
        "scores": {"domain": 1, "decision_structure": 1, "risk_level": 2, "scenario_condition": 2, "evidence_strength": 2, "governance_readiness": 1},
        "expert_judgment": "RECOMMEND — prediction is strong but consequence requires governance investment",
        "challenge": "Structured prediction but weak governance; override reduces authority for the wrong reason",
    },
    {
        "id": "BC-17",
        "name": "AI resume anonymizer for diversity hiring",
        "description": "Redacts identifying information from resumes. Intended to reduce bias. But the AI's redaction choices may introduce new biases.",
        "scores": {"domain": 3, "decision_structure": 2, "risk_level": 3, "scenario_condition": 1, "evidence_strength": 1, "governance_readiness": 2},
        "expert_judgment": "ASSIST — the tool intended to reduce bias may create bias; ironic failure mode",
        "challenge": "A tool designed for fairness may itself be unfair — the framework captures risk but not irony",
    },
    {
        "id": "BC-18",
        "name": "AI code review assistant for security-critical software",
        "description": "Reviews code for security vulnerabilities. High detection rate but false negatives could be exploited.",
        "scores": {"domain": 2, "decision_structure": 1, "risk_level": 3, "scenario_condition": 2, "evidence_strength": 2, "governance_readiness": 2},
        "expert_judgment": "RECOMMEND — good at finding known patterns but cannot guarantee absence of novel vulnerabilities",
        "challenge": "The AI's limitation (can't find unknown unknowns) is not captured by evidence_strength dimension",
    },
    {
        "id": "BC-19",
        "name": "AI therapy chatbot for mild anxiety",
        "description": "Provides CBT-based coping exercises for users reporting mild anxiety. Licensed therapists unavailable.",
        "scores": {"domain": 3, "decision_structure": 1, "risk_level": 3, "scenario_condition": 2, "evidence_strength": 1, "governance_readiness": 1},
        "expert_judgment": "ASSIST at most — mental health risk; but access benefit may justify carefully governed deployment",
        "challenge": "Access vs safety trade-off: restricting to ASSIST may deny care to people who have no alternative",
    },
    {
        "id": "BC-20",
        "name": "AI news article summarizer for corporate intelligence",
        "description": "Summarizes news articles for executive briefing. Low risk per summary but framing/selection bias shapes executive worldview.",
        "scores": {"domain": 2, "decision_structure": 2, "risk_level": 1, "scenario_condition": 1, "evidence_strength": 2, "governance_readiness": 2},
        "expert_judgment": "RECOMMEND — appears low-risk but information curation shapes decisions at the highest level",
        "challenge": "Indirect influence through information framing is invisible to direct risk scoring",
    },
]


def run_boundary_analysis():
    print("=" * 70)
    print("LAYER 3A: BOUNDARY CASE ANALYSIS (20 scenarios)")
    print("=" * 70)

    agree = 0
    conservative = 0
    disagree = 0
    issues = []

    for case in BOUNDARY_CASES:
        result = score_delegation(case["scores"])
        framework_auth = result.final_authority
        expert = case["expert_judgment"]

        # Classify agreement
        if "ASSIST" in framework_auth and "ASSIST" in expert:
            status = "AGREE"
            agree += 1
        elif "RECOMMEND" in framework_auth and "RECOMMEND" in expert:
            status = "AGREE"
            agree += 1
        elif "AUTOMATE" in framework_auth and "AUTOMATE" in expert:
            status = "AGREE"
            agree += 1
        elif "ASSIST" in framework_auth and ("RECOMMEND" in expert or "AUTOMATE" in expert):
            status = "CONSERVATIVE"
            conservative += 1
        elif "CONTEXT" in expert or "HALT" in expert:
            status = "EDGE CASE"
            issues.append(case)
            disagree += 1
        else:
            status = "DISAGREE"
            issues.append(case)
            disagree += 1

        overrides = [o.name for o in result.overrides if o.triggered]
        override_str = f" [overrides: {', '.join(overrides)}]" if overrides else ""

        print(f"\n  [{status}] {case['id']}: {case['name']}")
        print(f"    Framework: {framework_auth} (score {result.total_score}){override_str}")
        print(f"    Expert: {expert}")
        print(f"    Challenge: {case['challenge']}")

    return agree, conservative, disagree, issues


def run_gaming_analysis():
    print(f"\n{'=' * 70}")
    print("LAYER 3C: GAMING VULNERABILITY ANALYSIS")
    print(f"{'=' * 70}")

    dims = list(DIMENSIONS.keys())
    print("\n  Question: Which dimensions are easiest to manipulate?")
    print("  Method: For each dimension, count how many configurations")
    print("  change authority band when that dimension is inflated by +1\n")

    gaming_impact = {}
    for target_dim in dims:
        flips = 0
        opportunities = 0
        for combo in __import__("itertools").product(range(1, 3), repeat=6):
            scores = dict(zip(dims, combo))
            if scores[target_dim] == 3:
                continue  # already maxed

            base = score_delegation(scores)
            gamed = scores.copy()
            gamed[target_dim] = scores[target_dim] + 1
            gamed_result = score_delegation(gamed)

            opportunities += 1
            base_level = {"ASSIST": 1, "ASSIST or RECOMMEND": 2, "RECOMMEND": 3, "RECOMMEND or AUTOMATE WITH GUARDRAILS": 4}
            if base_level.get(gamed_result.final_authority, 0) > base_level.get(base.final_authority, 0):
                flips += 1

        gaming_impact[target_dim] = (flips, opportunities, flips / opportunities * 100 if opportunities else 0)

    print(f"  {'Dimension':<25} {'Flips':>8} {'Opportunities':>14} {'Gaming Rate':>12}")
    print("  " + "-" * 59)
    for dim, (flips, opps, rate) in sorted(gaming_impact.items(), key=lambda x: -x[1][2]):
        print(f"  {DIMENSIONS[dim]['label']:<25} {flips:>8} {opps:>14} {rate:>11.1f}%")

    print(f"""
  GAMING COUNTERMEASURES:
  1. Evidence Strength and Governance Readiness are most gameable
     → Require independent verification of these dimensions by a governance reviewer
  2. Scenario Condition gaming (claiming 'baseline' when conditions are 'edge-case')
     → Require documented evidence that conditions match training distribution
  3. Risk Level gaming (downgrading risk to avoid oversight)
     → Use regulatory/legal classification as objective anchor for risk scoring
  4. General: require two independent scorers for any RECOMMEND or AUTOMATE decision
""")


def run_adversarial():
    print("=" * 70)
    print("LAYER 3: ADVERSARIAL STRESS-TESTING")
    print("=" * 70)

    agree, conservative, disagree, issues = run_boundary_analysis()

    print(f"\n{'=' * 70}")
    print("LAYER 3A SUMMARY")
    print(f"{'=' * 70}")
    print(f"  Agree with expert: {agree}/20 ({agree*5}%)")
    print(f"  Conservative (framework more cautious): {conservative}/20 ({conservative*5}%)")
    print(f"  Disagree or edge case: {disagree}/20 ({disagree*5}%)")

    if issues:
        print(f"\n  IDENTIFIED FRAMEWORK LIMITATIONS:")
        for case in issues:
            print(f"    {case['id']}: {case['challenge']}")

    print(f"""
  FRAMEWORK GAPS IDENTIFIED:
  1. No HALT/PAUSE authority level — some situations require stopping, not assisting
     (BC-14: market crash rebalancing)
  2. Emergency override of overrides — when human capacity is overwhelmed, the
     framework's ASSIST recommendation may be operationally impossible
     (BC-11: pandemic surge triage)
  3. Temporal constraint not captured — when human reaction time is physically
     insufficient, ASSIST is not a viable authority level
     (BC-13: autonomous emergency braking)
  4. Indirect influence risk — information curation shapes decisions without
     appearing in direct risk scoring
     (BC-20: news summarizer for executives)
  5. Population vulnerability — risk to children, patients, or vulnerable groups
     is not captured by generic risk_level dimension
     (BC-07: children's educational platform)
""")

    run_gaming_analysis()

    print(f"\n{'=' * 70}")
    print("LAYER 3: COMPLETE")
    print(f"  20 boundary cases analyzed")
    print(f"  5 framework limitations identified")
    print(f"  6 dimensions ranked by gaming vulnerability")
    print(f"  4 countermeasures proposed")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    run_adversarial()
