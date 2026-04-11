"""
Module A: Source Quality Auditor

5-level source hierarchy with claim-source matching rules.
Based on research/core/framework/reasoning-verification-source-quality.md.
"""

from dataclasses import dataclass, field
from enum import IntEnum


class SourceLevel(IntEnum):
    UNRELIABLE = 1       # Anonymous, vendor marketing, AI-generated, circular
    INFORMAL = 2         # Blog posts, unattributed reports, social media, podcasts
    PROFESSIONAL = 3     # FT, WSJ, Bloomberg, annual reports, named expert presentations
    INSTITUTIONAL = 4    # Gartner, McKinsey Global Institute, World Bank, central bank
    PRIMARY_AUTH = 5     # SEC filings, peer-reviewed journals, gov statistics, legislation


SOURCE_LABELS = {
    SourceLevel.UNRELIABLE: "Unreliable / Non-verifiable",
    SourceLevel.INFORMAL: "Informal",
    SourceLevel.PROFESSIONAL: "Professional Secondary",
    SourceLevel.INSTITUTIONAL: "Institutional Analytical",
    SourceLevel.PRIMARY_AUTH: "Primary Authoritative",
}

# Minimum source level required for each claim type
CLAIM_REQUIREMENTS = {
    "factual_quantitative": {
        "min_level": SourceLevel.INSTITUTIONAL,
        "description": "Factual or quantitative claims in strategy/financial modeling",
    },
    "causal": {
        "min_level": SourceLevel.INSTITUTIONAL,
        "description": "Causal claims driving strategic decisions",
    },
    "trend": {
        "min_level": SourceLevel.PROFESSIONAL,
        "description": "Trend claims influencing resource allocation",
    },
    "regulatory": {
        "min_level": SourceLevel.PRIMARY_AUTH,
        "description": "Regulatory or legal claims",
    },
    "benchmark": {
        "min_level": SourceLevel.PROFESSIONAL,
        "description": "Benchmarks or best practice claims",
    },
    "anecdotal": {
        "min_level": SourceLevel.INFORMAL,
        "description": "Anecdotal or contextual claims",
    },
}


@dataclass
class Claim:
    text: str
    claim_type: str
    source_description: str
    source_level: SourceLevel
    required_level: SourceLevel = SourceLevel.PROFESSIONAL
    match: str = ""  # adequate / marginal / inadequate

    def __post_init__(self):
        if self.claim_type in CLAIM_REQUIREMENTS:
            self.required_level = CLAIM_REQUIREMENTS[self.claim_type]["min_level"]

        if self.source_level >= self.required_level:
            self.match = "adequate"
        elif self.source_level >= self.required_level - 1:
            self.match = "marginal"
        else:
            self.match = "inadequate"


@dataclass
class SourceQualityReport:
    claims: list[Claim] = field(default_factory=list)
    total_claims: int = 0
    adequate_count: int = 0
    marginal_count: int = 0
    inadequate_count: int = 0
    unsourced_count: int = 0
    source_distribution: dict[int, int] = field(default_factory=dict)
    overall_rating: str = ""

    def compute(self):
        self.total_claims = len(self.claims)
        self.adequate_count = sum(1 for c in self.claims if c.match == "adequate")
        self.marginal_count = sum(1 for c in self.claims if c.match == "marginal")
        self.inadequate_count = sum(1 for c in self.claims if c.match == "inadequate")

        self.source_distribution = {}
        for c in self.claims:
            lv = int(c.source_level)
            self.source_distribution[lv] = self.source_distribution.get(lv, 0) + 1

        if self.total_claims == 0:
            self.overall_rating = "NO CLAIMS ASSESSED"
        elif self.inadequate_count == 0 and self.marginal_count <= 1:
            self.overall_rating = "ADEQUATE"
        elif self.inadequate_count <= 2:
            self.overall_rating = "MARGINAL — review flagged claims"
        else:
            self.overall_rating = "INADEQUATE — significant source quality issues"


def create_claim(text: str, claim_type: str, source_desc: str, source_level: int) -> Claim:
    return Claim(
        text=text,
        claim_type=claim_type,
        source_description=source_desc,
        source_level=SourceLevel(source_level),
    )


def assess_sources(claims: list[Claim]) -> SourceQualityReport:
    report = SourceQualityReport(claims=claims)
    report.compute()
    return report


def format_source_report(report: SourceQualityReport) -> str:
    lines = []
    lines.append("=" * 60)
    lines.append("SOURCE QUALITY AUDIT")
    lines.append("=" * 60)

    for i, c in enumerate(report.claims, 1):
        status = {"adequate": "OK", "marginal": "WARN", "inadequate": "FAIL"}[c.match]
        lines.append(f"\n  [{status}] Claim {i}: {c.text[:80]}...")
        lines.append(f"    Type: {c.claim_type} (requires Level {int(c.required_level)}+)")
        lines.append(f"    Source: {c.source_description} (Level {int(c.source_level)}: {SOURCE_LABELS[c.source_level]})")
        lines.append(f"    Match: {c.match}")

    lines.append(f"\n  SUMMARY: {report.total_claims} claims assessed")
    lines.append(f"    Adequate: {report.adequate_count}  Marginal: {report.marginal_count}  Inadequate: {report.inadequate_count}")
    lines.append(f"\n  Source distribution:")
    for lv in sorted(report.source_distribution.keys()):
        lines.append(f"    Level {lv} ({SOURCE_LABELS[SourceLevel(lv)]}): {report.source_distribution[lv]}")
    lines.append(f"\n  OVERALL: {report.overall_rating}")
    lines.append("=" * 60)
    return "\n".join(lines)
