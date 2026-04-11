"""
Module E: Integrated Assessment

Combines all verification modules using weakest-link principle.
Based on research/core/framework/reasoning-verification-scoring-integration.md.
"""

from dataclasses import dataclass


@dataclass
class ComponentScore:
    name: str
    rating: str      # e.g., "ADEQUATE", "WELL-CALIBRATED", "LOW"
    severity: int     # 1=good, 2=warning, 3=critical
    details: str


@dataclass
class IntegratedReport:
    components: list[ComponentScore]
    weakest_link: str = ""
    overall_severity: int = 1
    overall_rating: str = ""
    priority_actions: list[str] = None

    def __post_init__(self):
        self.priority_actions = self.priority_actions or []
        if not self.components:
            self.overall_rating = "NO ASSESSMENT"
            return

        self.overall_severity = max(c.severity for c in self.components)
        weakest = max(self.components, key=lambda c: c.severity)
        self.weakest_link = weakest.name

        severity_labels = {1: "PASS", 2: "WARNING", 3: "FAIL"}
        self.overall_rating = severity_labels.get(self.overall_severity, "UNKNOWN")

        for c in sorted(self.components, key=lambda c: -c.severity):
            if c.severity >= 2:
                self.priority_actions.append(f"[{c.name}] {c.details}")


def map_source_severity(rating: str) -> int:
    if "INADEQUATE" in rating:
        return 3
    if "MARGINAL" in rating:
        return 2
    return 1


def map_calibration_severity(rating: str) -> int:
    if "OVER-CONFIDENT" in rating:
        return 3
    if "SELECTIVELY" in rating:
        return 2
    return 1


def map_sycophancy_severity(risk: str) -> int:
    return {"HIGH": 3, "MEDIUM": 2, "LOW": 1}.get(risk, 1)


def integrate(
    source_rating: str = "",
    calibration_rating: str = "",
    sycophancy_risk: str = "",
    additional_components: list[ComponentScore] = None,
) -> IntegratedReport:
    components = []

    if source_rating:
        components.append(ComponentScore(
            name="Source Quality",
            rating=source_rating,
            severity=map_source_severity(source_rating),
            details=f"Source quality assessment: {source_rating}",
        ))

    if calibration_rating:
        components.append(ComponentScore(
            name="Confidence Calibration",
            rating=calibration_rating,
            severity=map_calibration_severity(calibration_rating),
            details=f"Confidence calibration: {calibration_rating}",
        ))

    if sycophancy_risk:
        components.append(ComponentScore(
            name="Sycophancy",
            rating=sycophancy_risk,
            severity=map_sycophancy_severity(sycophancy_risk),
            details=f"Sycophancy risk: {sycophancy_risk}",
        ))

    if additional_components:
        components.extend(additional_components)

    return IntegratedReport(components=components)


def format_integrated_report(report: IntegratedReport) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append("INTEGRATED VERIFICATION ASSESSMENT")
    lines.append("=" * 60)

    severity_icons = {1: "OK", 2: "WARN", 3: "FAIL"}

    for c in report.components:
        icon = severity_icons.get(c.severity, "??")
        lines.append(f"\n  [{icon}] {c.name}: {c.rating}")

    lines.append(f"\n  WEAKEST LINK: {report.weakest_link}")
    lines.append(f"  OVERALL: {report.overall_rating}")

    if report.priority_actions:
        lines.append(f"\n  PRIORITY ACTIONS:")
        for i, action in enumerate(report.priority_actions, 1):
            lines.append(f"    {i}. {action}")

    lines.append("=" * 60)
    return "\n".join(lines)
