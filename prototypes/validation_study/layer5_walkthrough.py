#!/usr/bin/env python3
"""
Layer 5: Cognitive Walkthrough

Systematic step-by-step usability inspection of the verification protocol
from the perspective of a business practitioner (product manager).
"""


# Walkthrough of the Source Quality Verification on stimulus F1
WALKTHROUGH_F1 = {
    "stimulus": "F1: AI-Powered Inventory Optimization — European Retail Market",
    "persona": "Product manager, 5 years experience, uses AI tools weekly, no formal research training",
    "steps": [
        {
            "step": 1,
            "action": "Identify all claims with factual or quantitative content",
            "would_user_try": True,
            "would_user_succeed": "PARTIAL",
            "time_minutes": 3,
            "issue": "User can identify obvious quantitative claims (market size, percentages) but may miss implicit factual claims embedded in narrative ('growth is driven by...'). The instruction 'identify all claims' is too broad without examples.",
            "fix": "Provide 3 worked examples of claim identification in the tool. Distinguish 'key claims' (decision-driving) from 'supporting claims' (contextual).",
        },
        {
            "step": 2,
            "action": "For each claim, identify the cited source",
            "would_user_try": True,
            "would_user_succeed": "YES",
            "time_minutes": 2,
            "issue": "Straightforward — user can scan for source citations. F1 has explicit source references.",
            "fix": None,
        },
        {
            "step": 3,
            "action": "Classify each source on the 5-level hierarchy",
            "would_user_try": True,
            "would_user_succeed": "PARTIAL",
            "time_minutes": 4,
            "issue": "The 5-level hierarchy is clear for extremes (Level 1: anonymous; Level 5: peer-reviewed) but ambiguous in the middle. 'SmartStock Solutions Blog' is clearly Level 2 (informal), but what about 'SmartStock Solutions Customer Success Report'? Is that Level 2 (vendor marketing) or Level 3 (company report)?",
            "fix": "Add a decision tree for borderline cases. Rule: if the source has a financial incentive to present favorable data, cap at Level 2 regardless of format.",
        },
        {
            "step": 4,
            "action": "Match source level against claim type requirements",
            "would_user_try": "UNLIKELY without prompting",
            "would_user_succeed": "NO without training",
            "time_minutes": 5,
            "issue": "The claim-type matching rules (factual/quantitative requires Level 4+, causal requires Level 4+, etc.) are not intuitive. A product manager would not spontaneously categorize claims by type and look up required source levels. This step requires the tool to guide the user.",
            "fix": "The tool should auto-classify claim types using keywords (numbers → factual/quantitative, 'because/causes/drives' → causal, 'will/trending' → trend). Then display the required source level alongside the actual source level.",
        },
        {
            "step": 5,
            "action": "Flag mismatches and assess overall source quality",
            "would_user_try": True,
            "would_user_succeed": "YES with tool support",
            "time_minutes": 2,
            "issue": "If the tool highlights mismatches (red/yellow/green), the user can interpret the results. Without highlighting, the user would need to manually compare levels across a table.",
            "fix": "Visual traffic-light display: green (adequate), yellow (marginal), red (inadequate) for each claim.",
        },
    ],
}

# Walkthrough of the Confidence Calibration check on stimulus F3
WALKTHROUGH_F3 = {
    "stimulus": "F3: AI Writing Assistant for Legal Professionals — false precision",
    "persona": "Same product manager persona",
    "steps": [
        {
            "step": 1,
            "action": "Identify the 3-5 highest-stakes claims",
            "would_user_try": True,
            "would_user_succeed": "YES",
            "time_minutes": 2,
            "issue": "User can identify high-stakes claims (market size, adoption rate, pricing). The instruction is clear.",
            "fix": None,
        },
        {
            "step": 2,
            "action": "Rate expressed confidence (high/medium/low) for each claim",
            "would_user_try": True,
            "would_user_succeed": "PARTIAL",
            "time_minutes": 3,
            "issue": "F3 uses definitive language ('will reach $2.847B', 'exactly 26.2%'). Most users would recognize this as high confidence. But distinguishing medium from low confidence in hedged language is harder. The linguistic markers list helps but users may not cross-reference it.",
            "fix": "Provide 3 example sentences at each confidence level, calibrated to business analysis contexts.",
        },
        {
            "step": 3,
            "action": "Rate evidence strength for each claim",
            "would_user_try": "UNLIKELY without prompting",
            "would_user_succeed": "NO for most users",
            "time_minutes": 5,
            "issue": "This is the hardest step. Assessing evidence strength requires understanding what constitutes strong vs. weak evidence for a given claim type. A product manager may not know that a market size estimate from a single vendor report is 'weak' evidence. This is the verification paradox in action: the expertise needed to judge evidence strength is the expertise the user lacks.",
            "fix": "Link this step to the source quality module. If the source quality audit has already been run, use its output as the evidence strength input. The tool should automate this connection rather than requiring the user to independently judge evidence strength.",
        },
        {
            "step": 4,
            "action": "Check alignment between expressed confidence and evidence strength",
            "would_user_try": True,
            "would_user_succeed": "YES with tool support",
            "time_minutes": 2,
            "issue": "If steps 2 and 3 produce structured outputs, the alignment check is a simple matrix comparison. The tool can automate this.",
            "fix": "Display a 3x3 matrix with the user's ratings plotted. Highlight the over-confidence zone (top-left: high confidence + weak evidence).",
        },
        {
            "step": 5,
            "action": "Interpret the calibration result and decide whether to act on the analysis",
            "would_user_try": True,
            "would_user_succeed": "PARTIAL",
            "time_minutes": 3,
            "issue": "Users understand 'over-confident' but may not know what to do about it. The tool flags the problem but doesn't guide the response. 'This market size is over-confident' — then what?",
            "fix": "Add action recommendations per failure type: for over-confidence → request ranges instead of point estimates; for inadequate sources → specify what source level is needed.",
        },
    ],
}

# Walkthrough of the Sycophancy detection on stimulus F5
WALKTHROUGH_F5 = {
    "stimulus": "F5: AI-Powered Personal Finance Coach — sycophancy",
    "persona": "Same product manager persona",
    "steps": [
        {
            "step": 1,
            "action": "Identify the implicit hypothesis in the original prompt",
            "would_user_try": "UNLIKELY",
            "would_user_succeed": "NO without training",
            "time_minutes": 3,
            "issue": "Most users do not think about their prompt as containing an implicit hypothesis. They think they asked a neutral question. Recognizing that 'explore the opportunity for...' is a biased frame requires metacognitive awareness that most practitioners lack.",
            "fix": "The tool should analyze the prompt and explicitly surface the implicit hypothesis. Display: 'Your prompt appears to assume: [hypothesis]. The analysis may be confirming this assumption rather than testing it.'",
        },
        {
            "step": 2,
            "action": "Count the confirmation rate (% claims supporting hypothesis)",
            "would_user_try": "UNLIKELY manually",
            "would_user_succeed": "NO — too labor-intensive",
            "time_minutes": 10,
            "issue": "Manually counting confirming vs. disconfirming claims is tedious and subjective. Users will not do this without tool assistance.",
            "fix": "Automate with NLP. The tool should classify each claim as supporting, neutral, or challenging the hypothesis, then display the ratio.",
        },
        {
            "step": 3,
            "action": "Count alternatives considered and counter-evidence cited",
            "would_user_try": "YES for alternatives",
            "would_user_succeed": "PARTIAL",
            "time_minutes": 3,
            "issue": "Users can count alternatives if the output lists them. But recognizing the ABSENCE of alternatives is harder — users don't notice what isn't there. F5 has no alternatives, but the user may not register this as a problem.",
            "fix": "The tool should explicitly state: 'This analysis considers N alternatives. Professional standard: minimum 3.' Make the absence visible.",
        },
        {
            "step": 4,
            "action": "Assess overall sycophancy risk",
            "would_user_try": True,
            "would_user_succeed": "YES with indicators",
            "time_minutes": 2,
            "issue": "If the tool displays the 4 indicators with thresholds, the user can interpret the result. The word 'sycophancy' may be unfamiliar — use 'confirmation bias' or 'echo chamber risk' in practitioner-facing language.",
            "fix": "Rename in UI: 'Sycophancy Risk' → 'Confirmation Bias Assessment'. Display threshold comparison: 'Your analysis: 95% confirming. Professional standard: <75%.'",
        },
    ],
}


def run_walkthrough():
    print("=" * 70)
    print("LAYER 5: COGNITIVE WALKTHROUGH")
    print("=" * 70)

    for wt in [WALKTHROUGH_F1, WALKTHROUGH_F3, WALKTHROUGH_F5]:
        print(f"\n{'─' * 70}")
        print(f"  STIMULUS: {wt['stimulus']}")
        print(f"  PERSONA: {wt['persona']}")
        print(f"{'─' * 70}")

        total_time = 0
        issues_found = 0
        critical_issues = 0

        for step in wt["steps"]:
            success_icon = {"YES": "OK", "PARTIAL": "WARN", "NO": "FAIL",
                           "YES with tool support": "OK*", "NO without training": "FAIL",
                           "NO for most users": "FAIL", "UNLIKELY": "FAIL",
                           "UNLIKELY without prompting": "WARN",
                           "UNLIKELY manually": "FAIL"}
            icon = success_icon.get(str(step["would_user_succeed"]),
                   success_icon.get(str(step["would_user_try"]), "??"))

            print(f"\n  Step {step['step']}: {step['action']}")
            print(f"    User would try: {step['would_user_try']}")
            print(f"    User would succeed: {step['would_user_succeed']} [{icon}]")
            print(f"    Time: {step['time_minutes']} min")
            if step["issue"]:
                print(f"    Issue: {step['issue'][:120]}")
                issues_found += 1
                if "FAIL" in icon:
                    critical_issues += 1
            if step.get("fix"):
                print(f"    Fix: {step['fix'][:120]}")
            total_time += step["time_minutes"]

        print(f"\n  Summary: {total_time} min total, {issues_found} issues, {critical_issues} critical")

    # Overall findings
    print(f"\n{'=' * 70}")
    print("LAYER 5: WALKTHROUGH FINDINGS")
    print(f"{'=' * 70}")
    print("""
  CRITICAL USABILITY ISSUES (prevent successful use without fixes):

  1. CLAIM-SOURCE MATCHING requires training that practitioners lack
     Fix: Tool auto-classifies claim types and displays required source levels
     Affected: Source quality module, Step 4

  2. EVIDENCE STRENGTH judgment requires domain expertise
     Fix: Chain source quality output into confidence calibration input
     Affected: Confidence calibration module, Step 3

  3. SYCOPHANCY DETECTION requires metacognitive awareness
     Fix: Tool surfaces implicit hypothesis from prompt analysis
     Affected: Sycophancy module, Step 1

  4. MANUAL COUNTING is too labor-intensive for practitioners
     Fix: Automate confirmation rate and alternative counting with NLP
     Affected: Sycophancy module, Steps 2-3

  MODERATE USABILITY ISSUES (reduce effectiveness without fixes):

  5. MIDDLE LEVELS of source hierarchy are ambiguous
     Fix: Add decision tree for borderline cases + vendor incentive rule

  6. CONFIDENCE LEVEL DISCRIMINATION is unclear for hedged language
     Fix: Provide calibrated examples at each level

  7. ACTION GUIDANCE is missing after failure detection
     Fix: Add per-failure-type action recommendations

  TERMINOLOGY ISSUES:

  8. 'Sycophancy' is unfamiliar to practitioners
     Fix: Use 'Confirmation Bias Assessment' in practitioner-facing tools

  ESTIMATED TOOL-ASSISTED VERIFICATION TIME:
    Source quality audit:     12-16 min per output
    Confidence calibration:   8-12 min per output
    Sycophancy assessment:    5-8 min per output (with automation)
    Total per output:        25-36 min
    Full pipeline (6 stages): 2.5-3.6 hours
""")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    run_walkthrough()
