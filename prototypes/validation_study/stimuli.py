#!/usr/bin/env python3
"""
Practitioner Validation Study — 12 Stimuli

6 outputs with planted reasoning failures + 6 with sound reasoning.
Each output simulates a 1-page AI-generated market research briefing.
"""

STIMULI = [
    # === FLAWED OUTPUTS (6) ===

    # F1: Source quality failure — vendor blog as evidence for market size
    {
        "id": "F1",
        "flaw_type": "source_quality",
        "flaw_description": "Market size claim sourced from vendor blog; causal claim from self-published vendor case study",
        "title": "AI-Powered Inventory Optimization: European Retail Market Analysis",
        "content": """
MARKET OVERVIEW

The European AI-powered inventory optimization market is projected to reach EUR 3.8 billion by 2028, growing at a CAGR of 24.5% (Source: SmartStock Solutions Blog, "The Future of AI Inventory," March 2024). This growth is driven by increasing adoption of cloud-based retail analytics platforms and the pressure to reduce carrying costs.

KEY FINDINGS

Trend analysis: European retailers are rapidly shifting toward AI-driven demand forecasting. The adoption rate increased from 12% in 2022 to 34% in 2025, driven primarily by post-pandemic supply chain disruptions that exposed the limitations of traditional planning methods.

Customer needs: Retailers require real-time visibility into stock levels across channels, automated replenishment triggers, and predictive analytics for seasonal demand patterns. A survey of 150 retail executives found that 78% consider AI inventory tools a "top priority" for 2026 capital expenditure.

Competitive landscape: The market is fragmented with no dominant player. Key competitors include BlueYonder, o9 Solutions, and several regional players. White space exists in the mid-market segment (EUR 50M-500M revenue retailers) where enterprise solutions are too expensive and legacy tools are insufficient.

Impact evidence: Retailers implementing AI inventory optimization report a 32% reduction in stockouts and 18% decrease in carrying costs within the first year of deployment (Source: SmartStock Solutions Customer Success Report, 2025).

RECOMMENDATION: Strong market opportunity. Recommend proceeding to product concept development with focus on mid-market segment.
""",
    },

    # F2: Source quality failure — fabricated survey statistics
    {
        "id": "F2",
        "flaw_type": "source_quality",
        "flaw_description": "Survey statistics cited without methodology; 'industry survey' with no named source or sample size",
        "title": "Telemedicine Platform Expansion: Southeast Asian Market Assessment",
        "content": """
MARKET OVERVIEW

The Southeast Asian telemedicine market reached USD 4.5 billion in 2025 and is expected to grow to USD 12.3 billion by 2030 (Source: Statista, Digital Health Market Report, 2025). Growth is driven by smartphone penetration, regulatory reforms post-COVID, and chronic healthcare access gaps in rural areas.

KEY FINDINGS

Regulatory environment: Thailand, Indonesia, and the Philippines have all passed telemedicine-enabling legislation since 2022. Singapore serves as a regulatory sandbox for cross-border telehealth services.

Customer needs: According to a recent industry survey, 89% of healthcare consumers in the region prefer telemedicine for initial consultations, and 72% would pay a premium for AI-powered diagnostic support. Physicians report that 64% of primary care consultations could be handled remotely with appropriate technology.

Competitive landscape: Halodoc (Indonesia), Doctor Anywhere (Singapore), and MyDoc lead the market. However, AI-integrated diagnostic capabilities remain limited across all platforms, representing a clear gap.

Market sizing: The addressable market for AI-enhanced telemedicine specifically is estimated at USD 2.1 billion by 2028. This is based on the total telemedicine market multiplied by the expected AI integration rate of 35%.

RECOMMENDATION: Proceed with market entry focused on AI diagnostic integration. The survey data strongly supports consumer demand.
""",
    },

    # F3: Calibration failure — precise estimate from uncertain data
    {
        "id": "F3",
        "flaw_type": "calibration",
        "flaw_description": "Precise single-point market estimates with no ranges; false precision from uncertain assumptions",
        "title": "AI Writing Assistant for Legal Professionals: North American Market",
        "content": """
MARKET OVERVIEW

The North American AI legal writing assistant market will reach USD 2.847 billion by 2029. The current market size is USD 891 million (2025), growing at exactly 26.2% CAGR. The total addressable market consists of 1,352,027 licensed attorneys in the US and 145,893 in Canada, of whom 67.3% will adopt AI writing tools by 2028.

KEY FINDINGS

Demand drivers: Billable hour pressure creates strong ROI incentives. An AI writing assistant saves an average of 3.7 hours per attorney per week, translating to USD 1,480 in recovered billable time at average partner rates.

Customer segmentation: Large firms (AmLaw 200) represent 34.2% of market value. Mid-size firms (50-200 attorneys) represent 28.7%. Small firms and solo practitioners represent 37.1%. The fastest growth is in mid-size firms at 31.4% CAGR.

Competitive positioning: Thomson Reuters CoCounsel and Harvey AI lead with 23.4% and 18.7% market share respectively. Casetext (now part of Thomson Reuters) holds 12.1%. The remaining 45.8% is divided among 47 competitors.

Pricing model: Optimal pricing is USD 149/user/month for mid-size firms, with a 15.3% discount for annual commitments yielding USD 126.18/user/month.

RECOMMENDATION: Enter at the mid-size firm segment with USD 149/month pricing. The market is clearly defined and growing rapidly.
""",
    },

    # F4: Calibration failure — uniform confidence across all claims
    {
        "id": "F4",
        "flaw_type": "calibration",
        "flaw_description": "All claims expressed with equal high confidence regardless of evidence quality",
        "title": "Autonomous Last-Mile Delivery: Urban European Market",
        "content": """
MARKET OVERVIEW

The autonomous last-mile delivery market in European urban areas is a rapidly growing segment driven by e-commerce expansion, labor shortages, and sustainability mandates. The market will reach EUR 5.2 billion by 2030.

KEY FINDINGS

Regulatory certainty: European cities will implement autonomous delivery vehicle-friendly regulations by 2027. The EU's forthcoming Autonomous Mobility Act will create a harmonized framework for ground-based delivery robots and drones across all member states.

Technology readiness: Current autonomous delivery technology is fully capable of navigating complex urban environments including pedestrian zones, mixed traffic, and adverse weather conditions. Battery technology improvements will extend operational range to 150km per charge by 2027.

Customer adoption: Urban consumers will rapidly embrace autonomous delivery, with adoption reaching 45% within 2 years of service launch in any given city. Consumer resistance to robot interaction is minimal and declining.

Cost advantage: Autonomous delivery will reduce last-mile costs by 62% compared to human couriers by 2028. This cost advantage is sufficient to achieve profitability within 14 months of launch in any European city with population above 500,000.

Competitive timing: First-mover advantage is critical and will persist for at least 5 years due to network effects and regulatory capture.

RECOMMENDATION: Immediate market entry is essential. All signals indicate strong and certain market opportunity.
""",
    },

    # F5: Sycophancy failure — hypothesis confirmation, no alternatives
    {
        "id": "F5",
        "flaw_type": "sycophancy",
        "flaw_description": "Analysis confirms the user's product hypothesis without testing it; no alternatives considered",
        "title": "AI-Powered Personal Finance Coach: US Millennial Market",
        "content": """
MARKET OVERVIEW

Your concept for an AI-powered personal finance coaching app targeting US millennials addresses a clear and significant market need. The US personal finance app market is valued at USD 1.8 billion (2025) with strong growth dynamics that favor your approach.

KEY FINDINGS

Market validation: The millennial demographic (ages 28-43 in 2026) represents the ideal target market for your product. This generation has the highest financial anxiety levels, the most comfort with AI-driven tools, and the greatest willingness to pay for personalized financial guidance. Your focus on this segment is well-placed.

Need confirmation: Your product's core features — AI-driven budgeting, personalized investment recommendations, and behavioral nudges — align precisely with the top three needs expressed by millennial consumers in recent surveys. The product-market fit is strong.

Competitive advantage: Your approach of combining behavioral science with AI distinguishes you from existing competitors who focus primarily on transaction tracking (Mint) or investment automation (Wealthfront, Betterment). This positioning is unique and defensible.

Growth potential: Given the demographic tailwinds and your differentiated approach, we project your app can capture 3-5% of the millennial finance app market within 3 years, representing USD 54-90 million in annual revenue.

Risk factors: Implementation complexity is the primary risk, but your team's technical expertise mitigates this concern.

RECOMMENDATION: This is an excellent product concept with strong market validation. Proceed to development.
""",
    },

    # F6: Sycophancy failure — suppressed counter-evidence
    {
        "id": "F6",
        "flaw_type": "sycophancy",
        "flaw_description": "Disconfirming evidence systematically omitted; risks minimized to footnote level",
        "title": "AI Recruitment Screening Platform: Global Enterprise Market",
        "content": """
MARKET OVERVIEW

The global AI recruitment screening market is a high-growth segment valued at USD 3.1 billion (2025) with projected growth to USD 8.7 billion by 2030. Enterprise adoption of AI screening tools is accelerating as organizations seek to improve hiring efficiency and candidate quality.

KEY FINDINGS

Market drivers: The average enterprise receives 250+ applications per open position. Manual screening costs USD 4,200 per hire in recruiter time. AI screening can reduce time-to-hire by 40% and screening costs by 65%, creating compelling ROI for enterprise buyers.

Technology capability: Modern AI screening systems analyze resumes, assess skill fit, evaluate culture alignment, and predict job performance with high accuracy. Natural language processing advances have made these tools significantly more reliable than previous generations.

Enterprise demand: 73% of Fortune 500 companies have either implemented or are actively evaluating AI recruitment screening tools. Of those not yet using AI, 61% plan to adopt within 24 months.

Market structure: The market is consolidating around 5-6 major platforms (Workday, HireVue, Pymetrics, Eightfold, Phenom). Entry barriers are moderate; differentiation through specialized industry verticals or superior accuracy represents the strongest go-to-market strategy.

Regulatory note: Some jurisdictions are developing frameworks for AI in hiring. These developments should be monitored as they may affect feature roadmap decisions.

RECOMMENDATION: Strong market fundamentals. Enterprise demand is clear and growing. Recommend proceeding with product development focused on accuracy differentiation.
""",
    },

    # === SOUND OUTPUTS (6) ===

    # S1: Sound source quality
    {
        "id": "S1",
        "flaw_type": None,
        "flaw_description": None,
        "title": "Electric Vehicle Charging Infrastructure: Nordic Market Assessment",
        "content": """
MARKET OVERVIEW

The Nordic EV charging infrastructure market was valued at EUR 2.1 billion in 2025 (Source: European Alternative Fuels Observatory, 2025 Annual Report). Norway leads with the highest EV penetration globally (approximately 90% of new car sales in 2025, per Norwegian Road Federation statistics). Sweden, Denmark, and Finland follow with penetration rates of 55-65% (Source: European Automobile Manufacturers' Association, 2025 registration data).

KEY FINDINGS

Regulatory framework: The EU Alternative Fuels Infrastructure Regulation (AFIR, 2024) mandates minimum charging point density along TEN-T corridors. Nordic countries exceed these minimums but face growing demand-supply gaps in rural areas and multi-unit residential buildings (Source: Nordic Energy Research, "Charging Gap Analysis," 2025).

Supply-demand analysis: Current public charging points per EV ratio ranges from 1:15 (Norway) to 1:9 (Denmark) (Source: European Alternative Fuels Observatory). Industry estimates suggest a ratio of 1:10 is needed for adequate service levels, though this estimate varies by geography and usage patterns. Norway's ratio appears insufficient given its EV density, while Denmark may have temporary overcapacity.

Customer needs: Based on Volvo Car Group's 2024 consumer survey (n=12,000 across Nordic countries), the top three unmet needs are: workplace charging availability (cited by 47%), rural route charging reliability (39%), and faster charging speeds at existing stations (34%). Note: this survey was conducted by an industry participant and may overweight needs aligned with their product strategy.

Competitive landscape: ChargePoint, Ionity, and Tesla Supercharger network are dominant. However, a significant number of charging points are operated by local utilities (approximately 35% in Sweden, per Swedish Energy Agency data). This fragmentation creates both opportunity and complexity for new entrants.

LIMITATIONS: Market size projections for charging infrastructure vary significantly depending on assumptions about EV adoption curves, which remain uncertain. The range of credible estimates for 2030 Nordic charging infrastructure investment spans EUR 4-8 billion, reflecting genuine uncertainty about adoption pace and technology evolution (battery range improvements may reduce charging frequency).

RECOMMENDATION: Market opportunity exists but requires careful positioning. Workplace charging segment has clearest unmet demand. Significant uncertainty in long-term sizing warrants staged entry rather than large upfront commitment.
""",
    },

    # S2: Sound calibration
    {
        "id": "S2",
        "flaw_type": None,
        "flaw_description": None,
        "title": "AI-Powered Clinical Trial Matching: US Healthcare Market",
        "content": """
MARKET OVERVIEW

The US clinical trial matching market is estimated at USD 800 million to USD 1.4 billion (2025), with the wide range reflecting different inclusion criteria for adjacent services (Source: Grand View Research, 2025; cross-referenced with Deloitte Life Sciences Outlook, 2025). Growth projections range from 18-28% CAGR depending on regulatory developments and payer adoption timelines.

KEY FINDINGS

Problem scale: 80% of clinical trials fail to meet enrollment deadlines (Source: Tufts Center for the Study of Drug Development, 2024). Each day of delay costs sponsors an estimated USD 600K-8M depending on therapeutic area and phase (Source: Eastern Research Group analysis for FDA, 2023). These figures are well-documented but vary substantially by context.

Technology assessment: Current AI matching systems show promising but inconsistent results. A 2024 multi-site study (JAMA Network Open, n=34 sites) found that AI matching increased enrollment rates by 16-24% at sites with strong data infrastructure, but showed no significant improvement at sites with fragmented electronic health records. This suggests the technology works when underlying data quality is sufficient, which is not guaranteed.

Regulatory status: FDA has issued guidance supporting AI in clinical trial design (September 2024) but has not specifically addressed AI-driven participant matching. The regulatory path is favorable but not yet definitive. CMS reimbursement policy for AI-assisted matching is undefined, creating uncertainty about the payer model.

Customer willingness: Based on interviews with 8 pharmaceutical company clinical operations leaders (conducted by the researcher, January 2026), interest is high but procurement cycles are 12-18 months for new clinical trial technology. Budget allocation typically requires demonstrated ROI from a pilot program. Note: sample size is small; findings should be treated as directional.

Market sizing note: We deliberately present a range rather than a point estimate because the market boundaries are genuinely unclear. The lower bound assumes AI matching remains a niche service; the upper bound assumes it becomes standard practice. Both scenarios are plausible.

RECOMMENDATION: Promising market with genuine unmet need, but significant execution uncertainty. Recommend pilot-first approach with 2-3 sponsor partnerships before scaling. Avoid committing to a specific market size in investor materials — the honest answer is that it depends on adoption dynamics that are not yet determined.
""",
    },

    # S3: Sound — balanced with counter-evidence
    {
        "id": "S3",
        "flaw_type": None,
        "flaw_description": None,
        "title": "AI Content Moderation Platform: Social Media Market",
        "content": """
MARKET OVERVIEW

The global AI content moderation market was valued at USD 5.8 billion in 2025 (Source: MarketsandMarkets, 2025; validated against Gartner's Digital Risk Management forecast). Growth is driven by regulatory mandates (EU Digital Services Act, UK Online Safety Act) and platform liability concerns.

KEY FINDINGS

Regulatory drivers: The EU DSA (effective February 2024) requires platforms to implement "systemic risk assessments" and content moderation measures proportional to their reach. Fines can reach 6% of global turnover. The UK Online Safety Act (effective 2025) adds criminal liability for senior executives. These are strong compliance drivers with verified enforcement mechanisms.

Market need: Platform spend on content moderation increased approximately 300% from 2020-2025 (Source: estimates based on Meta, Google, and TikTok transparency reports cross-referenced with industry analyst models). However, accuracy remains a major challenge: Meta's own transparency report (Q4 2024) shows proactive detection rates vary from 98% (child exploitation) to 15% (bullying/harassment), demonstrating that AI moderation works well for some content types but poorly for others.

COUNTER-EVIDENCE AND RISKS:
- Human moderator displacement creates ethical and PR risks. Accenture and Teleperformance have faced lawsuits from moderators experiencing psychological harm. Automating these roles does not eliminate the harm — it concentrates it in training data curation.
- False positive rates remain problematic. A 2024 study (Stanford Internet Observatory) found that AI moderation systems disproportionately flag content in non-English languages and minority dialects, creating discrimination risk.
- Market saturation: Major platforms are building in-house solutions rather than purchasing third-party tools. Meta, Google, and ByteDance all operate proprietary systems, limiting the addressable market to mid-tier platforms and enterprise applications.
- Regulatory fragmentation: content standards vary by jurisdiction, requiring locale-specific models that increase development and maintenance costs.

Competitive landscape: Spectrum Labs, L1ght, and Crisp are established players. Open-source alternatives (Perspective API, OpenAI moderation endpoint) provide free baseline capability, pressuring pricing for commercial tools.

RECOMMENDATION: Market is real but more complex than growth numbers suggest. The strongest opportunity is in regulated enterprise applications (financial services, healthcare platforms) rather than social media, where in-house solutions dominate. Significant ethical and discrimination risks require careful product design. Enter only with a clear answer to the false-positive bias problem.
""",
    },

    # S4: Sound — properly hedged predictions
    {
        "id": "S4",
        "flaw_type": None,
        "flaw_description": None,
        "title": "Agricultural AI Platform: Sub-Saharan African Market",
        "content": """
MARKET OVERVIEW

The Sub-Saharan African agricultural technology market is estimated at USD 300-500 million (2025), with substantial uncertainty due to limited reliable market data in many countries (Source: GSMA AgriTech Programme, 2024; CTA/World Bank agricultural digitization reports). The wide range reflects genuine ambiguity about what constitutes the addressable market in a region where 60% of farming is subsistence-level.

KEY FINDINGS

Opportunity thesis: Sub-Saharan Africa has approximately 250 million smallholder farmers (Source: FAO, 2024). Mobile phone penetration among farmers ranges from 40% (DRC, Mozambique) to 85% (Kenya, South Africa) (Source: GSMA Mobile Agriculture Report, 2024). AI-powered advisory services delivered via mobile could potentially reach a large population underserved by traditional agricultural extension services.

Evidence for AI impact: Kenya's PlantVillage Nuru app (Penn State University project) has demonstrated that AI crop disease identification works on low-cost smartphones, with a 2023 field study (n=2,400 farmers across 6 counties) showing a 21% improvement in early disease detection rates. However, translation to yield improvement or income gains has not been demonstrated in a controlled study.

REASONS THIS MIGHT NOT WORK:
- Connectivity: AI features requiring cloud processing are unreliable in areas with intermittent 2G/3G coverage. Offline-first design is essential but limits model sophistication.
- Willingness to pay: Most smallholder farmers operate at subsistence level. The paying customer may need to be an aggregator, cooperative, government, or NGO rather than the farmer. This changes the business model fundamentally.
- Cultural and linguistic diversity: Sub-Saharan Africa encompasses 1,000+ languages and vastly different agricultural practices. A single platform cannot serve this diversity without massive localization investment.
- Existing alternatives: Government extension services, farmer cooperatives, and radio-based advisory programs already serve this population at zero cost to farmers. AI must demonstrably outperform free alternatives.
- Track record: Multiple ag-tech startups (Farmerline, WeFarm, AgroStar) have struggled to achieve sustainability in African markets despite strong initial traction and donor funding.

Market sizing caveat: Applying standard SaaS metrics to this market is inappropriate. Revenue per user will be orders of magnitude lower than enterprise SaaS. A more realistic framing is: how many paying intermediaries (cooperatives, governments, agribusinesses) would fund AI advisory for their farmer networks?

RECOMMENDATION: Genuine need exists, but the business model challenge is severe. Recommend a donor-funded pilot with 1-2 agricultural cooperatives in Kenya or Nigeria before any commercial commitment. Do not use standard market sizing approaches — they will produce misleadingly large numbers.
""",
    },

    # S5: Sound — competitor strengths honestly assessed
    {
        "id": "S5",
        "flaw_type": None,
        "flaw_description": None,
        "title": "AI-Powered Supply Chain Risk Monitoring: Global Enterprise",
        "content": """
MARKET OVERVIEW

The global supply chain risk management software market was valued at USD 3.2 billion in 2025 (Source: Gartner Market Guide for Supply Chain Risk Management, 2025). AI-powered risk monitoring is a growing sub-segment, estimated at USD 800M-1.2B (Source: cross-reference of Gartner, IDC, and Everest Group estimates; range reflects definitional differences).

KEY FINDINGS

Demand signal: Post-pandemic and post-Suez disruptions, 87% of chief supply chain officers rank real-time risk visibility as a top-3 priority (Source: Gartner CSCO Survey, 2025, n=400). This is a strong, well-documented demand signal from a credible source.

AI capability assessment: Current AI systems can effectively monitor known risk categories (weather, port congestion, financial distress of suppliers) with reported accuracy of 70-85% for event detection (Source: Resilinc and Everstream Analytics published benchmarks). However, "black swan" events — the risks that matter most — are by definition outside training data. AI excels at monitoring known risks but does not solve the fundamental problem of unknown risks.

HONEST COMPETITIVE ASSESSMENT:
Existing competitors are strong and well-resourced:
- Resilinc: 10+ years of supply chain mapping data; relationships with 10,000+ global suppliers. Their data moat is significant and difficult to replicate.
- Everstream Analytics: Strong NLP-based risk monitoring with a growing intelligence network. Recently raised USD 50M Series C.
- Interos: Focus on multi-tier supply chain visibility. Government contracts provide stable revenue base.
- SAP and Oracle: Integrating risk monitoring into their existing ERP suites, leveraging massive installed bases.

The competitive barrier is not technology — it is data. Supply chain risk monitoring requires supplier relationship networks that take years to build. A new entrant with superior AI but inferior data will lose to an incumbent with adequate AI and superior data.

White space assessment: Genuine white space exists in two areas: (1) mid-market companies (USD 500M-5B revenue) underserved by enterprise-priced solutions, and (2) industry-specific risk models (pharmaceutical cold chain, semiconductor supply) where general-purpose tools lack domain depth. Both niches are real but limited in size.

RECOMMENDATION: Do not enter this market with a general-purpose offering — incumbents are too strong. If entering, target a specific industry vertical where domain expertise can compensate for data disadvantage. Be realistic about the data moat problem: it takes 3-5 years to build competitive supplier networks. Plan financing accordingly.
""",
    },

    # S6: Sound — acknowledges limitations of own analysis
    {
        "id": "S6",
        "flaw_type": None,
        "flaw_description": None,
        "title": "AI-Powered Language Learning Platform: Latin American Market",
        "content": """
MARKET OVERVIEW

The Latin American digital language learning market was estimated at USD 1.2 billion in 2025 (Source: HolonIQ EdTech Market Intelligence, 2025). English language learning dominates demand (~70% of market). AI-powered personalization is the primary technology differentiator in a crowded market.

KEY FINDINGS

Demand fundamentals: English proficiency correlates strongly with wage premiums in Latin America — 30-50% in professional roles (Source: British Council and EF English Proficiency Index research). With 650 million people in the region and English proficiency below global averages in most countries, the structural demand case is real.

Current landscape: Duolingo dominates with 80M+ monthly active users in Latin America (Source: Duolingo 10-K, 2024). Platzi, Open English, and Babbel compete for the premium segment. AI tutoring startups (Speak, ELSA) are gaining traction but remain small.

WHAT THIS ANALYSIS CANNOT TELL YOU:
- We do not have primary customer research for this market. The demand analysis is based on published data and secondary sources. Before product decisions, primary research with 20-30 target users in 2-3 countries is essential.
- Pricing sensitivity in Latin America differs significantly from North American or European markets. Our pricing assumptions are extrapolated from Duolingo's and Platzi's public data, not from direct willingness-to-pay research.
- We have not assessed the competitive response risk. If Duolingo launches a feature similar to the proposed AI tutor (which they are likely developing given their AI investment trajectory), the differentiation window may be shorter than our analysis assumes.
- Regulatory requirements for EdTech vary by country. We have not conducted a country-by-country regulatory review. Brazil's LGPD and Mexico's data protection laws may affect data collection practices.

Opportunity assessment: A genuine opportunity likely exists in the premium AI tutoring segment (price point USD 15-30/month) targeting professionals seeking English fluency for career advancement. This segment is underserved by Duolingo (too gamified for professional learners) and overserved by traditional language schools (too expensive at USD 200+/month).

Estimated addressable segment: 5-15 million professionals in Brazil, Mexico, Colombia, and Argentina who would benefit from and could afford premium AI English tutoring. Revenue potential: USD 75M-450M annually at steady state. This range is wide because adoption rates are genuinely uncertain.

RECOMMENDATION: Promising but requires primary validation. Conduct user research in Brazil and Mexico before committing to product development. The analysis supports further investigation but not a product launch decision.
""",
    },
]


def list_stimuli():
    print("=" * 70)
    print(f"PRACTITIONER VALIDATION STUDY — 12 STIMULI")
    print("=" * 70)

    print(f"\n  FLAWED OUTPUTS (6):")
    for s in STIMULI:
        if s["flaw_type"]:
            print(f"    {s['id']}: [{s['flaw_type']}] {s['title']}")
            print(f"         Flaw: {s['flaw_description']}")

    print(f"\n  SOUND OUTPUTS (6):")
    for s in STIMULI:
        if not s["flaw_type"]:
            print(f"    {s['id']}: {s['title']}")

    print(f"\n  Distribution:")
    flaw_types = [s["flaw_type"] for s in STIMULI if s["flaw_type"]]
    for ft in set(flaw_types):
        count = flaw_types.count(ft)
        print(f"    {ft}: {count} flawed outputs")
    print(f"    sound: {sum(1 for s in STIMULI if not s['flaw_type'])} outputs")

    # Word count comparison
    flawed_words = [len(s["content"].split()) for s in STIMULI if s["flaw_type"]]
    sound_words = [len(s["content"].split()) for s in STIMULI if not s["flaw_type"]]
    print(f"\n  Word count (to ensure surface quality parity):")
    print(f"    Flawed: {min(flawed_words)}-{max(flawed_words)} words (avg {sum(flawed_words)//len(flawed_words)})")
    print(f"    Sound:  {min(sound_words)}-{max(sound_words)} words (avg {sum(sound_words)//len(sound_words)})")
    print("=" * 70)


if __name__ == "__main__":
    list_stimuli()
