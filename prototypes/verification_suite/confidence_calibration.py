"""
Module B: Confidence Calibration Auditor

Checks whether expressed confidence in AI output matches evidence strength.
Based on research/core/framework/reasoning-verification-confidence-calibration.md.
"""

from dataclasses import dataclass
from enum import IntEnum


class ConfidenceLevel(IntEnum):
    LOW = 1       # "may", "could", wide ranges, explicit uncertainty
    MEDIUM = 2    # "likely", "suggests", qualified language, ranges provided
    HIGH = 3      # "will", "clearly", definitive language, precise single-point estimates


class EvidenceStrength(IntEnum):
    WEAK = 1      # Level 1-2 sources, single source, no convergence
    MODERATE = 2  # Level 3-4 with some convergence
    STRONG = 3    # Multiple Level 4-5 sources converging


CONFIDENCE_MARKERS = {
    ConfidenceLevel.HIGH: [
        "will", "clearly", "certainly", "definitely", "without doubt",
        "is", "are", "must", "proves", "demonstrates", "confirms",
    ],
    ConfidenceLevel.MEDIUM: [
        "likely", "probably", "suggests", "indicates", "appears",
        "tends to", "generally", "in most cases",
    ],
    ConfidenceLevel.LOW: [
        "may", "might", "could", "possibly", "perhaps",
        "it is uncertain", "it remains unclear", "depending on",
    ],
}


@dataclass
class CalibrationCheck:
    claim_text: str
    expressed_confidence: ConfidenceLevel
    evidence_strength: EvidenceStrength
    alignment: str = ""  # well-calibrated / over-confident / under-confident
    flag: bool = False

    def __post_init__(self):
        diff = int(self.expressed_confidence) - int(self.evidence_strength)
        if diff <= 0:
            self.alignment = "well-calibrated"
        elif diff == 1:
            self.alignment = "mildly over-confident"
            self.flag = True
        else:
            self.alignment = "over-confident"
            self.flag = True


@dataclass
class CalibrationReport:
    checks: list[CalibrationCheck]
    overall_rating: str = ""
    flagged_count: int = 0

    def __post_init__(self):
        self.flagged_count = sum(1 for c in self.checks if c.flag)
        total = len(self.checks)
        if total == 0:
            self.overall_rating = "NO CLAIMS ASSESSED"
        elif self.flagged_count == 0:
            self.overall_rating = "WELL-CALIBRATED"
        elif self.flagged_count <= total * 0.3:
            self.overall_rating = "SELECTIVELY CALIBRATED — some claims over-confident"
        else:
            self.overall_rating = "OVER-CONFIDENT — majority of key claims exceed evidence"


def detect_confidence_level(text: str) -> ConfidenceLevel:
    """Heuristic detection of expressed confidence from linguistic markers."""
    text_lower = text.lower()

    high_count = sum(1 for m in CONFIDENCE_MARKERS[ConfidenceLevel.HIGH] if m in text_lower)
    low_count = sum(1 for m in CONFIDENCE_MARKERS[ConfidenceLevel.LOW] if m in text_lower)

    if high_count > low_count:
        return ConfidenceLevel.HIGH
    elif low_count > high_count:
        return ConfidenceLevel.LOW
    return ConfidenceLevel.MEDIUM


def assess_calibration(checks: list[CalibrationCheck]) -> CalibrationReport:
    return CalibrationReport(checks=checks)


def format_calibration_report(report: CalibrationReport) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append("CONFIDENCE CALIBRATION AUDIT")
    lines.append("=" * 60)

    for i, c in enumerate(report.checks, 1):
        flag = "FLAG" if c.flag else "OK"
        lines.append(f"\n  [{flag}] Claim {i}: {c.claim_text[:80]}...")
        lines.append(f"    Expressed confidence: {c.expressed_confidence.name}")
        lines.append(f"    Evidence strength: {c.evidence_strength.name}")
        lines.append(f"    Alignment: {c.alignment}")

    lines.append(f"\n  SUMMARY: {len(report.checks)} claims checked, {report.flagged_count} flagged")
    lines.append(f"  OVERALL: {report.overall_rating}")
    lines.append("=" * 60)
    return "\n".join(lines)
