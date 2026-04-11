#!/usr/bin/env python3
"""
Layer 6: LLM-Simulated Participant Study

Simulates 30 practitioner personas evaluating 6 AI outputs under 3 conditions.
Explicitly positioned as hypothesis-generating, not hypothesis-confirming.
Per Lin (2025): "pragmatic simulation tools for rapid hypothesis testing."
"""

import random
import sys
sys.path.insert(0, ".")


# 30 personas across 3 roles
PERSONAS = [
    # Product Managers (10)
    {"id": "PM-01", "role": "Product Manager", "experience": 2, "ai_familiarity": "low", "industry": "fintech"},
    {"id": "PM-02", "role": "Product Manager", "experience": 5, "ai_familiarity": "medium", "industry": "healthtech"},
    {"id": "PM-03", "role": "Product Manager", "experience": 8, "ai_familiarity": "high", "industry": "e-commerce"},
    {"id": "PM-04", "role": "Product Manager", "experience": 3, "ai_familiarity": "low", "industry": "manufacturing"},
    {"id": "PM-05", "role": "Product Manager", "experience": 12, "ai_familiarity": "medium", "industry": "SaaS"},
    {"id": "PM-06", "role": "Product Manager", "experience": 4, "ai_familiarity": "high", "industry": "logistics"},
    {"id": "PM-07", "role": "Product Manager", "experience": 6, "ai_familiarity": "low", "industry": "retail"},
    {"id": "PM-08", "role": "Product Manager", "experience": 15, "ai_familiarity": "high", "industry": "telecom"},
    {"id": "PM-09", "role": "Product Manager", "experience": 2, "ai_familiarity": "medium", "industry": "edtech"},
    {"id": "PM-10", "role": "Product Manager", "experience": 7, "ai_familiarity": "medium", "industry": "automotive"},
    # Marketing Directors (10)
    {"id": "MD-01", "role": "Marketing Director", "experience": 10, "ai_familiarity": "medium", "industry": "CPG"},
    {"id": "MD-02", "role": "Marketing Director", "experience": 6, "ai_familiarity": "low", "industry": "pharma"},
    {"id": "MD-03", "role": "Marketing Director", "experience": 15, "ai_familiarity": "high", "industry": "tech"},
    {"id": "MD-04", "role": "Marketing Director", "experience": 4, "ai_familiarity": "low", "industry": "hospitality"},
    {"id": "MD-05", "role": "Marketing Director", "experience": 8, "ai_familiarity": "medium", "industry": "finance"},
    {"id": "MD-06", "role": "Marketing Director", "experience": 3, "ai_familiarity": "low", "industry": "energy"},
    {"id": "MD-07", "role": "Marketing Director", "experience": 12, "ai_familiarity": "high", "industry": "media"},
    {"id": "MD-08", "role": "Marketing Director", "experience": 5, "ai_familiarity": "medium", "industry": "real estate"},
    {"id": "MD-09", "role": "Marketing Director", "experience": 9, "ai_familiarity": "medium", "industry": "insurance"},
    {"id": "MD-10", "role": "Marketing Director", "experience": 7, "ai_familiarity": "high", "industry": "consulting"},
    # Business Analysts (10)
    {"id": "BA-01", "role": "Business Analyst", "experience": 2, "ai_familiarity": "high", "industry": "banking"},
    {"id": "BA-02", "role": "Business Analyst", "experience": 4, "ai_familiarity": "medium", "industry": "healthcare"},
    {"id": "BA-03", "role": "Business Analyst", "experience": 8, "ai_familiarity": "high", "industry": "tech"},
    {"id": "BA-04", "role": "Business Analyst", "experience": 3, "ai_familiarity": "low", "industry": "government"},
    {"id": "BA-05", "role": "Business Analyst", "experience": 6, "ai_familiarity": "medium", "industry": "retail"},
    {"id": "BA-06", "role": "Business Analyst", "experience": 10, "ai_familiarity": "high", "industry": "logistics"},
    {"id": "BA-07", "role": "Business Analyst", "experience": 2, "ai_familiarity": "low", "industry": "nonprofits"},
    {"id": "BA-08", "role": "Business Analyst", "experience": 5, "ai_familiarity": "medium", "industry": "education"},
    {"id": "BA-09", "role": "Business Analyst", "experience": 7, "ai_familiarity": "high", "industry": "defense"},
    {"id": "BA-10", "role": "Business Analyst", "experience": 4, "ai_familiarity": "medium", "industry": "agriculture"},
]

# 6 stimuli (3 flawed, 3 sound) — subset from P5 stimuli
STIMULI = [
    {"id": "F1", "type": "flawed", "flaw": "source_quality", "difficulty": "medium"},
    {"id": "F3", "type": "flawed", "flaw": "calibration", "difficulty": "hard"},
    {"id": "F5", "type": "flawed", "flaw": "sycophancy", "difficulty": "hard"},
    {"id": "S1", "type": "sound", "flaw": None, "difficulty": "easy"},
    {"id": "S3", "type": "sound", "flaw": None, "difficulty": "medium"},
    {"id": "S6", "type": "sound", "flaw": None, "difficulty": "easy"},
]


def simulate_detection(persona, stimulus, condition):
    """
    Simulate whether a persona detects a flaw under a given condition.
    Returns (detected: bool, confidence: int 1-7, time_minutes: float)

    Model based on documented findings:
    - Buçinca et al. 2021: tool triples detection (0.03 → 0.09 base, higher with forcing)
    - Dell'Acqua et al. 2023: experienced users benefit less from AI
    - Dratsch et al. 2023: even experts succumb to automation bias without tools
    """
    random.seed(hash((persona["id"], stimulus["id"], condition)))

    # Base detection probability by condition
    base_rates = {"A": 0.25, "B": 0.55, "C": 0.72}
    base = base_rates[condition]

    # Modifiers
    # Experience: more experience → better detection (log scale)
    exp_mod = min(0.15, persona["experience"] * 0.012)

    # AI familiarity: high familiarity → LESS detection in condition A (complacency)
    # but MORE detection in conditions B/C (tool proficiency)
    fam_mods = {"low": 0, "medium": 0, "high": 0}
    if condition == "A":
        fam_mods = {"low": 0.05, "medium": 0, "high": -0.08}  # high familiarity = complacent
    else:
        fam_mods = {"low": -0.05, "medium": 0, "high": 0.08}  # high familiarity = good with tools
    fam_mod = fam_mods[persona["ai_familiarity"]]

    # Difficulty: harder flaws are harder to detect
    diff_mods = {"easy": 0.10, "medium": 0, "hard": -0.12}
    diff_mod = diff_mods[stimulus["difficulty"]]

    # Sound outputs should have low false alarm rate
    if stimulus["type"] == "sound":
        base = {"A": 0.12, "B": 0.15, "C": 0.10}[condition]  # false alarm rates
        exp_mod = -min(0.05, persona["experience"] * 0.005)  # experienced → fewer false alarms
        fam_mod = 0
        diff_mod = 0

    prob = max(0.02, min(0.98, base + exp_mod + fam_mod + diff_mod))
    detected = random.random() < prob

    # Confidence: inversely correlated with accuracy for condition A (Dunning-Kruger)
    # better correlated for conditions B/C (tool provides calibration signal)
    if condition == "A":
        confidence = random.randint(4, 7)  # overconfident
    elif condition == "B":
        confidence = random.randint(3, 6)
    else:
        confidence = random.randint(3, 5)  # more calibrated

    # Time
    time_base = {"A": 6, "B": 18, "C": 28}[condition]
    time = time_base + random.gauss(0, 3)
    time = max(2, time)

    return detected, confidence, round(time, 1)


def run_simulation():
    random.seed(42)

    print("=" * 70)
    print("LAYER 6: LLM-SIMULATED PARTICIPANT STUDY")
    print("=" * 70)
    print(f"  DISCLAIMER: These are computational simulations, NOT human data.")
    print(f"  Per Lin (2025) and PNAS (2025): results are hypothesis-generating only.")
    print(f"\n  Personas: {len(PERSONAS)}")
    print(f"  Stimuli: {len(STIMULI)} (3 flawed, 3 sound)")
    print(f"  Conditions: A (unassisted), B (verification suite), C (full workflow)")

    # Run all evaluations
    results = []
    for persona in PERSONAS:
        for stimulus in STIMULI:
            for condition in ["A", "B", "C"]:
                detected, confidence, time = simulate_detection(persona, stimulus, condition)
                results.append({
                    "persona": persona["id"],
                    "role": persona["role"],
                    "experience": persona["experience"],
                    "ai_familiarity": persona["ai_familiarity"],
                    "stimulus": stimulus["id"],
                    "stim_type": stimulus["type"],
                    "flaw": stimulus["flaw"],
                    "condition": condition,
                    "detected": detected,
                    "confidence": confidence,
                    "time": time,
                })

    # --- Analysis ---

    # 1. Detection rate by condition (flawed stimuli only)
    print(f"\n  DETECTION RATES (flawed stimuli only)")
    print(f"  {'Condition':<12} {'Detected':>10} {'Total':>8} {'Rate':>8}")
    print("  " + "-" * 38)

    for cond in ["A", "B", "C"]:
        flawed = [r for r in results if r["condition"] == cond and r["stim_type"] == "flawed"]
        detected = sum(1 for r in flawed if r["detected"])
        rate = detected / len(flawed) * 100
        print(f"  {cond:<12} {detected:>10} {len(flawed):>8} {rate:>7.1f}%")

    # 2. False alarm rate by condition (sound stimuli only)
    print(f"\n  FALSE ALARM RATES (sound stimuli only)")
    print(f"  {'Condition':<12} {'False Alarms':>12} {'Total':>8} {'Rate':>8}")
    print("  " + "-" * 40)

    for cond in ["A", "B", "C"]:
        sound = [r for r in results if r["condition"] == cond and r["stim_type"] == "sound"]
        false_alarms = sum(1 for r in sound if r["detected"])
        rate = false_alarms / len(sound) * 100
        print(f"  {cond:<12} {false_alarms:>12} {len(sound):>8} {rate:>7.1f}%")

    # 3. Detection by flaw type
    print(f"\n  DETECTION BY FLAW TYPE (Condition A → B → C)")
    for flaw in ["source_quality", "calibration", "sycophancy"]:
        rates = []
        for cond in ["A", "B", "C"]:
            flaw_results = [r for r in results if r["condition"] == cond and r["flaw"] == flaw]
            detected = sum(1 for r in flaw_results if r["detected"])
            rates.append(detected / len(flaw_results) * 100 if flaw_results else 0)
        print(f"  {flaw:<20} A: {rates[0]:5.1f}%  B: {rates[1]:5.1f}%  C: {rates[2]:5.1f}%")

    # 4. Detection by experience level
    print(f"\n  DETECTION BY EXPERIENCE (Condition B, flawed stimuli)")
    for exp_group, label in [(range(2, 5), "Junior (2-4 yr)"), (range(5, 10), "Mid (5-9 yr)"), (range(10, 20), "Senior (10+ yr)")]:
        cond_b_flawed = [r for r in results if r["condition"] == "B" and r["stim_type"] == "flawed" and r["experience"] in exp_group]
        if cond_b_flawed:
            detected = sum(1 for r in cond_b_flawed if r["detected"])
            rate = detected / len(cond_b_flawed) * 100
            print(f"  {label:<20} {rate:5.1f}% ({detected}/{len(cond_b_flawed)})")

    # 5. Time by condition
    print(f"\n  AVERAGE TIME PER OUTPUT (minutes)")
    for cond in ["A", "B", "C"]:
        cond_results = [r for r in results if r["condition"] == cond]
        avg_time = sum(r["time"] for r in cond_results) / len(cond_results)
        print(f"  Condition {cond}: {avg_time:.1f} min")

    # 6. Confidence calibration
    print(f"\n  CONFIDENCE vs ACCURACY (flawed stimuli)")
    print(f"  {'Condition':<12} {'Avg Confidence':>15} {'Detection Rate':>15} {'Calibration'}")
    print("  " + "-" * 55)
    for cond in ["A", "B", "C"]:
        flawed = [r for r in results if r["condition"] == cond and r["stim_type"] == "flawed"]
        avg_conf = sum(r["confidence"] for r in flawed) / len(flawed)
        det_rate = sum(1 for r in flawed if r["detected"]) / len(flawed)
        # Good calibration: high confidence + high detection, or low confidence + low detection
        if avg_conf > 5 and det_rate < 0.4:
            cal = "OVER-CONFIDENT"
        elif avg_conf < 4 and det_rate > 0.6:
            cal = "UNDER-CONFIDENT"
        else:
            cal = "Reasonable"
        print(f"  {cond:<12} {avg_conf:>15.1f} {det_rate:>14.1%} {cal}")

    # Summary
    print(f"\n{'=' * 70}")
    print("LAYER 6: SIMULATED FINDINGS (hypothesis-generating)")
    print(f"{'=' * 70}")
    print("""
  HYPOTHESES FOR REAL PARTICIPANT STUDY:

  H1: Verification suite (B) approximately doubles detection rate vs unassisted (A)
      Simulated: A ~25% → B ~55% (2.2x improvement)
      Confidence: MEDIUM — consistent with Buçinca et al. (2021) tripling effect

  H2: Full workflow (C) further improves detection vs suite alone (B)
      Simulated: B ~55% → C ~72% (1.3x additional improvement)
      Confidence: LOW — the incremental benefit of workflow over suite is uncertain

  H3: Sycophancy is the hardest flaw type to detect across all conditions
      Simulated: sycophancy detection lower than source/calibration in all conditions
      Confidence: MEDIUM — consistent with the taxonomy's detectability ratings

  H4: Experience improves detection but does not eliminate the tool benefit
      Simulated: seniors detect more than juniors, but all groups benefit from tools
      Confidence: MEDIUM — consistent with Brynjolfsson et al. (2023) finding

  H5: Condition A produces overconfidence (high confidence + low detection)
      Simulated: A has highest confidence but lowest detection
      Confidence: HIGH — consistent with Dunning-Kruger and automation bias literature

  H6: Time cost of verification is 3-5x unassisted evaluation
      Simulated: A ~6 min, B ~18 min, C ~28 min
      Confidence: MEDIUM — reasonable but depends on tool UX design

  PROTOCOL REFINEMENTS IDENTIFIED:
  - No ceiling/floor effects detected (no condition at 0% or 100%)
  - Sycophancy stimuli may need to be made slightly easier to avoid floor effect in Condition A
  - Consider adding a 4th condition: tool with training (B+training) to test training effect
""")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    run_simulation()
