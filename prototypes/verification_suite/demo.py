#!/usr/bin/env python3
"""
Verification Suite Demo — runs a complete verification on a simulated AI market research output.
"""

from .source_quality import (
    create_claim, assess_sources, format_source_report, SourceLevel,
)
from .confidence_calibration import (
    CalibrationCheck, ConfidenceLevel, EvidenceStrength,
    assess_calibration, format_calibration_report,
)
from .sycophancy_detector import (
    assess_sycophancy, assess_pipeline,
    format_sycophancy_report, format_pipeline_report,
)
from .integrated_assessment import integrate, format_integrated_report


def run_demo():
    print("\n" + "=" * 60)
    print("VERIFICATION SUITE DEMO")
    print("Simulated AI Market Research: Sustainability SaaS in Europe")
    print("=" * 60)

    # --- Module A: Source Quality ---
    claims = [
        create_claim(
            "The European ESG compliance market will reach $4.2B by 2028",
            "factual_quantitative",
            "Blog post from ESG software vendor",
            int(SourceLevel.INFORMAL),
        ),
        create_claim(
            "CSRD affects approximately 50,000 companies in the EU",
            "regulatory",
            "European Commission official directive text",
            int(SourceLevel.PRIMARY_AUTH),
        ),
        create_claim(
            "85% of sustainability officers report difficulty with compliance",
            "factual_quantitative",
            "Survey by sustainability consulting firm (n=200)",
            int(SourceLevel.INSTITUTIONAL),
        ),
        create_claim(
            "AI-powered compliance tools reduce reporting time by 60%",
            "causal",
            "Case study published by an AI vendor on their own website",
            int(SourceLevel.UNRELIABLE),
        ),
        create_claim(
            "McKinsey projects sustainability services as fastest-growing segment",
            "trend",
            "McKinsey Global Institute report, 2024",
            int(SourceLevel.INSTITUTIONAL),
        ),
    ]
    source_report = assess_sources(claims)
    print("\n" + format_source_report(source_report))

    # --- Module B: Confidence Calibration ---
    cal_checks = [
        CalibrationCheck(
            claim_text="The market will reach $4.2B by 2028",
            expressed_confidence=ConfidenceLevel.HIGH,
            evidence_strength=EvidenceStrength.WEAK,
        ),
        CalibrationCheck(
            claim_text="CSRD affects approximately 50,000 companies",
            expressed_confidence=ConfidenceLevel.HIGH,
            evidence_strength=EvidenceStrength.STRONG,
        ),
        CalibrationCheck(
            claim_text="AI tools reduce reporting time by 60%",
            expressed_confidence=ConfidenceLevel.HIGH,
            evidence_strength=EvidenceStrength.WEAK,
        ),
        CalibrationCheck(
            claim_text="Sustainability services likely the fastest-growing segment",
            expressed_confidence=ConfidenceLevel.MEDIUM,
            evidence_strength=EvidenceStrength.MODERATE,
        ),
    ]
    cal_report = assess_calibration(cal_checks)
    print("\n" + format_calibration_report(cal_report))

    # --- Module D: Sycophancy Detection (single stage) ---
    syc_report = assess_sycophancy(
        prompt_hypothesis="European sustainability compliance market is a significant opportunity",
        confirmation_rate=0.92,
        diversity_count=2,
        counter_evidence_rate=0.05,
        confidence_trend=0.4,
        stage_name="Concept Generation (Stage 6)",
    )
    print("\n" + format_sycophancy_report(syc_report))

    # --- Pipeline compounding (simulated 6-stage) ---
    stages = [
        assess_sycophancy("Sustainability SaaS opportunity", 0.65, 6, 0.25, 0.0, "Environmental Scanning"),
        assess_sycophancy("Sustainability SaaS opportunity", 0.72, 5, 0.20, 0.1, "Trend Identification"),
        assess_sycophancy("Sustainability SaaS opportunity", 0.80, 4, 0.12, 0.2, "Customer Need Extraction"),
        assess_sycophancy("Sustainability SaaS opportunity", 0.85, 3, 0.08, 0.3, "Competitive Mapping"),
        assess_sycophancy("Sustainability SaaS opportunity", 0.90, 2, 0.05, 0.4, "Market Sizing"),
        assess_sycophancy("Sustainability SaaS opportunity", 0.95, 1, 0.02, 0.5, "Concept Generation"),
    ]
    pipeline_report = assess_pipeline(stages)
    print("\n" + format_pipeline_report(pipeline_report))

    # --- Module E: Integrated Assessment ---
    integrated = integrate(
        source_rating=source_report.overall_rating,
        calibration_rating=cal_report.overall_rating,
        sycophancy_risk=syc_report.risk_level,
    )
    print("\n" + format_integrated_report(integrated))

    print("\n" + "=" * 60)
    print("DEMO INTERPRETATION")
    print("=" * 60)
    print("""
  This simulated AI market research output exhibits:

  1. SOURCE QUALITY: Marginal — key quantitative claim ($4.2B market)
     sourced from vendor blog; causal claim (60% time reduction)
     sourced from vendor self-published case study.

  2. CONFIDENCE: Over-confident — definitive language used for claims
     supported only by weak evidence. Market size stated as precise
     figure without uncertainty range.

  3. SYCOPHANCY: High — 95% confirmation rate at final stage, only 1
     alternative considered, 2% counter-evidence. Pipeline shows
     monotonic compounding from 65% to 95% confirmation.

  4. INTEGRATED: FAIL — weakest link is sycophancy at HIGH risk.
     The analysis confirms the initial hypothesis rather than testing it.

  The verification framework would recommend:
  - Reject the market size claim until sourced from Level 4+ data
  - Require uncertainty ranges for all quantitative estimates
  - Re-run concept generation with adversarial counter-prompt
  - Insert human checkpoint between Stages 2 and 3 (critical transition)
""")


if __name__ == "__main__":
    run_demo()
