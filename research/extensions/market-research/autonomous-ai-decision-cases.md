# Documented Cases of Fully Automated AI Decision-Making Systems

Research compiled: 2026-04-11
Scope: Verified, documented cases where AI makes and executes decisions autonomously or with minimal human oversight.
Evidence standard: Only cases with public documentation (news reports, court filings, regulatory actions, company disclosures, or academic analysis).

---

## 1. Finance and Lending

### 1.1 Knight Capital Group — Algorithmic Trading Failure
- **Company/System**: Knight Capital Group, Power Peg algorithm
- **What was automated**: Fully autonomous stock trading execution. The system placed buy and sell orders without human approval in real time.
- **Year deployed**: Legacy code from 2003; failure on August 1, 2012
- **Outcome**: Catastrophic failure. Lost $440 million in approximately 45 minutes. 4 million executions across 154 stocks, over 397 million shares.
- **Root cause**: During a deployment of new RLP code to eight servers, one server was missed, triggering dormant "Power Peg" test code that was designed to buy high and sell low. A 2005 refactoring had broken the transaction-confirmation loop, so the algorithm never received confirmation that orders were filled and kept sending more.
- **Governance framework**: None documented. Knight had no documented procedures for incident response. Operations staff rolled back to the same bad version that caused the problem.
- **Regulatory action**: SEC fined Knight Capital $12 million. The company was acquired by Getco LLC in December 2012, forming KCG Holdings.
- **Sources**: [Wikipedia](https://en.wikipedia.org/wiki/Knight_Capital_Group), [Henricodolfing case study](https://www.henricodolfing.ch/en/case-study-4-the-440-million-software-error-at-knight-capital/), [SEC enforcement](https://www.quellit.ai/blog/case-study-knight-capital-when-a-trading-algorithm-broke-the-bank)

### 1.2 2010 Flash Crash — Cascading Algorithmic Trading
- **Company/System**: Waddell & Reed Financial Inc. trigger; cascading interaction among multiple high-frequency trading algorithms
- **What was automated**: Fully autonomous algorithmic trading at scale. Multiple firms' algorithms reacted to each other's trades without human intervention.
- **Year deployed**: Ongoing; incident on May 6, 2010
- **Outcome**: Nearly $1 trillion in market value wiped out within minutes. Market partially corrected within 30 minutes. Waddell & Reed's algorithm sold 75,000 E-Mini S&P contracts ($4.1 billion) at 9% of the prior minute's volume regardless of price or timing.
- **Governance framework**: Minimal. Algorithms operated independently across firms with no cross-firm coordination or circuit breakers adequate for algorithmic cascading.
- **Regulatory action**: SEC and CFTC investigation. Led to implementation of circuit breakers and "limit up-limit down" mechanisms across US exchanges.
- **Sources**: [AIID Incident 28](https://incidentdatabase.ai/cite/28/), [PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC8978471/), [Lawfare analysis](https://www.lawfaremedia.org/article/selling-spirals--avoiding-an-ai-flash-crash)

### 1.3 Renaissance Technologies / Two Sigma / Citadel — Autonomous Quantitative Trading
- **Companies**: Renaissance Technologies (Medallion Fund, 1988-present), Two Sigma, Citadel Securities
- **What was automated**: Fully autonomous trading execution. Renaissance's Medallion Fund uses proprietary algorithms for pattern recognition and automated decision-making, staffed by scientists and mathematicians rather than traditional traders. Two Sigma feeds news articles, satellite images, and financial reports into ML models. Citadel makes thousands of trades per second.
- **Year deployed**: Medallion Fund since 1988; others operational for decades
- **Outcome**: Sustained success. Medallion Fund has averaged approximately 66% annual returns before fees over decades. Two Sigma manages $60+ billion. These represent the most successful cases of fully autonomous AI decision-making in any domain.
- **Governance framework**: Proprietary and opaque. No public documentation of governance structures. Two Sigma recently mandated AI integration across all functions, positioning itself as AI-native.
- **Regulatory action**: Subject to standard SEC/CFTC oversight. No major enforcement actions specifically related to autonomous decision-making.
- **Sources**: [QuantSavvy](https://quantsavvy.com/best-quantitative-trading-firms-renaissance-technologies-two-sigma-shaw-fund/), [HedgeCo on Two Sigma](https://www.hedgeco.net/news/04/2026/two-sigmas-ai-first-internal-mandate-the-race-for-operational-alpha-in-the-age-of-frontier-models.html)

### 1.4 Upstart — Automated Lending Underwriting
- **Company/System**: Upstart Network, AI-driven personal loan underwriting
- **What was automated**: Full decision loop. Over 91% of loans are fully automated with no human involvement. The model evaluates 2,500+ variables and autonomously approves or denies loan applications.
- **Year deployed**: Founded 2012; CFPB no-action letter 2017
- **Outcome**: Success with governance. Approves 44% more borrowers than traditional models at 36% lower APRs. 28.8% of loans go to low-to-moderate-income communities.
- **Governance framework**: Among the strongest documented. CFPB issued its first no-action letter in 2017, creating a blueprint for AI lending governance. Upstart has a dedicated model risk management team, quarterly fair lending testing across race/ethnicity/sex segments covering nearly one million borrowers over seven years, disparate treatment and impact evaluation, and lender-specific and platform-wide fairness reporting.
- **Regulatory action**: Operated under CFPB oversight with unprecedented transparency requirements. No adverse enforcement actions.
- **Sources**: [Upstart](https://www.upstart.com/our-story), [Upstart FDIC comment letter](https://www.fdic.gov/resources/regulations/federal-register-publications/2021/2021-rfi-financial-institutions-ai-3064-za24-c-032.pdf), [Reruption case study](https://reruption.com/en/knowledge/industry-cases/upstarts-ai-credit-risk-modeling-revolutionizes-lending)

### 1.5 Apple Card / Goldman Sachs — Credit Limit Algorithm Bias
- **Company/System**: Apple Card, Goldman Sachs credit assessment algorithm
- **What was automated**: Automated credit limit determination. The algorithm set credit limits without per-application human review.
- **Year deployed**: 2019
- **Outcome**: Mixed/failure. Tech entrepreneur David Heinmeier Hansson reported Apple Card offered him 20x the credit limit of his wife despite shared assets and her higher credit score. Apple co-founder Steve Wozniak reported the same pattern.
- **Governance framework**: Opaque. Goldman Sachs claimed fairness but the algorithm's decision-making process was not transparent to consumers or regulators.
- **Regulatory action**: New York Department of Financial Services investigated. Found no intentional wrongdoing but highlighted the regulatory challenge of opaque AI in finance.
- **Sources**: [AIID Incident 92](https://incidentdatabase.ai/cite/92/), [CNN](https://www.cnn.com/2019/11/12/business/apple-card-gender-bias), [NYSDFS Report](https://www.dfs.ny.gov/reports_and_publications/202103_report_apple_card_investigation)

### 1.6 Google Ads — Automated Bidding and Auction Manipulation
- **Company/System**: Google Ads automated bidding system
- **What was automated**: Fully automated ad auction pricing. Advertisers delegate bidding to Google's algorithms, which autonomously determine bid amounts and auction outcomes.
- **Year deployed**: Ongoing; sworn testimony in 2023
- **Outcome**: Failure (from advertiser perspective). Google VP Jerry Dischler confirmed under oath (September 2023) that Google "frequently" changes auctions without informing advertisers, raising costs "as much as 5% on average, up to 10% for some queries." Internal programs: Project Bernanke (hundreds of millions annually), Jedi Blue (122% price increase), Project Momiji (15% cost increase), RGSP ("raise prices in small increments over time").
- **Governance framework**: Unilateral. Google controlled the governance of its own automated system with no external oversight of pricing algorithms.
- **Regulatory action**: Cabrera v. Google class action resulted in $100 million settlement.
- **Sources**: [Google Ads Class Action](https://pablodiazt.com/google-ads-lawsuits/google-ads-class-action-automated-bidding-overcharges)

---

## 2. Hiring and HR

### 2.1 Amazon — Automated Resume Screening Tool
- **Company/System**: Amazon, ML-based resume scoring system
- **What was automated**: Automated resume scoring from 1-5 stars. Designed to mechanize the search for top talent by scoring candidates without human review of individual resumes.
- **Year deployed**: Development began 2014; discontinued 2018
- **Outcome**: Failure. The system penalized resumes containing the word "women's" (e.g., "women's rugby team"), downgraded graduates of women's colleges, and privileged verbs more commonly used by men ("executed," "captured").
- **Root cause**: Training data consisted of resumes of Amazon's overwhelmingly male engineering workforce, guaranteeing demographic reproduction.
- **Governance framework**: None documented. The system was a secret internal project.
- **Regulatory action**: No formal regulatory action, but the case became a canonical example cited in subsequent AI bias regulation worldwide.
- **Sources**: [ACLU](https://www.aclu.org/news/womens-rights/why-amazons-automated-hiring-tool-discriminated-against), [MIT Technology Review](https://www.technologyreview.com/2018/10/10/139858/amazon-ditched-ai-recruitment-software-because-it-was-biased-against-women/), [Reuters original report](https://www.euronews.com/business/2018/10/10/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women)

### 2.2 HireVue — Automated Video Interview Scoring
- **Company/System**: HireVue, AI-powered video interview assessment platform
- **What was automated**: Automated speech recognition and analysis of video interview responses to score candidates, with the system capable of evaluating resumes and rejecting applicants without human oversight.
- **Year deployed**: Operational for years; ACLU complaint filed March 2025
- **Outcome**: Under litigation. A Deaf, Indigenous woman alleges the system's automated speech recognition failed to accurately recognize her speech, and automated feedback criticized her communication abilities, blocking her promotion at Intuit.
- **Governance framework**: Contested. HireVue claims to have bias-testing procedures. The ACLU alleges the system violates the ADA, Title VII, and Colorado Anti-Discrimination Act.
- **Regulatory action**: EEOC and Colorado Civil Rights Division investigating. ACLU filed charges on March 19, 2025. HireVue disputes that an AI-backed assessment was used in this particular case.
- **Sources**: [Fisher Phillips](https://www.fisherphillips.com/en/news-insights/ai-screening-systems-face-fresh-scrutiny-6-key-takeaways-from-claims-filed-against-hiring-technology-company.html), [HR Dive](https://www.hrdive.com/news/ai-intuit-hirevue-deaf-indigenous-employee-discrimination-aclu/743273/), [Public Justice](https://www.publicjustice.net/hirevue-intuit-artificial-intelligence-biased-hiring/)

### 2.3 Workday — Automated Applicant Screening
- **Company/System**: Workday, algorithmic resume screening and applicant evaluation
- **What was automated**: Automated applicant screening that can "evaluate resumes without human oversight and decide whether to reject the applicant."
- **Year deployed**: Ongoing; lawsuit filed February 2024
- **Outcome**: Major litigation. Derek Mobley, a Black man over 40 with anxiety and depression, claims rejection from over 100 qualified positions due to automated screening. May 2025: federal court certified a nationwide collective action covering 1.1 billion rejected applications.
- **Governance framework**: Under scrutiny. The case establishes that AI vendors may be directly liable for employment discrimination caused by their tools, even when they don't make final hiring decisions.
- **Regulatory action**: EEOC filed an amicus brief in April 2025 supporting the plaintiff. The collective action certification is a landmark precedent for AI hiring tools.
- **Sources**: [FairNow](https://fairnow.ai/workday-lawsuit-resume-screening/), [Fisher Phillips](https://www.fisherphillips.com/en/insights/insights/discrimination-lawsuit-over-workdays-ai-hiring-tools-can-proceed-as-class-action-6-things), [Seyfarth Shaw](https://www.seyfarth.com/news-insights/mobley-v-workday-court-holds-ai-service-providers-could-be-directly-liable-for-employment-discrimination-under-agent-theory.html)

---

## 3. Healthcare

### 3.1 IBM Watson for Oncology — Automated Treatment Recommendations
- **Company/System**: IBM Watson for Oncology, trained at Memorial Sloan Kettering Cancer Center
- **What was automated**: Automated cancer treatment recommendations. The system generated treatment suggestions that were presented to oncologists, though final decisions remained with physicians.
- **Year deployed**: Launched 2015-2016; discontinued 2023
- **Outcome**: Failure. The system recommended "unsafe and incorrect" cancer treatments. At Gachon University Gil Medical Center (South Korea), Watson matched expert recommendations only 49% of the time for colon cancer. MD Anderson Cancer Center canceled its Watson project in 2016 after spending $62 million.
- **Root cause**: Engineers at Memorial Sloan Kettering often input synthetic (fabricated) data, contradicting IBM's claims about using real patient data. The system did poorly with older patients and had a bug causing it to recommend surveillance instead of aggressive treatment for metastatic cancer patients.
- **Governance framework**: Inadequate. IBM marketed Watson as trained on real patient data when it was partly trained on synthetic cases. No independent validation framework before deployment to hospitals worldwide.
- **Regulatory action**: No formal regulatory action, but the case became a widely studied example of AI failure in healthcare.
- **Sources**: [STAT News](https://www.statnews.com/2018/07/25/ibm-watson-recommended-unsafe-incorrect-treatments/), [IEEE Spectrum](https://spectrum.ieee.org/how-ibm-watson-overpromised-and-underdelivered-on-ai-health-care), [AIID Incident 225](https://incidentdatabase.ai/cite/225/), [Henricodolfing case study](https://www.henricodolfing.com/2024/12/case-study-ibm-watson-for-oncology-failure.html)

### 3.2 UnitedHealth / Optum — nH Predict Automated Claims Denial
- **Company/System**: UnitedHealth Group, nH Predict (developed by naviHealth/Optum)
- **What was automated**: Automated denial of post-acute care claims for Medicare Advantage patients. The AI system determined coverage duration for skilled nursing and home healthcare, with medical directors rubber-stamping denials at a rate of 1.2 seconds per case, processing up to 60,000 claims per month per doctor.
- **Year deployed**: naviHealth acquired by Optum in 2020; lawsuit filed November 2023
- **Outcome**: Under litigation. Plaintiffs allege the system has a 90% error rate (nine of ten appealed denials are ultimately reversed). Families claim patients' health worsened and some died due to premature coverage termination. The AI superseded physician judgment.
- **Governance framework**: Alleged absence. The system allegedly replaced medical professional judgment with algorithmic output, with medical directors not reviewing patient files.
- **Regulatory action**: Class action lawsuit advancing in federal court. Judge waived exhaustion-of-remedies requirement, describing UHG's denial process as "futile." March 2026: court ordered UnitedHealth to disclose its AI denial algorithm.
- **Sources**: [CBS News](https://www.cbsnews.com/news/unitedhealth-lawsuit-ai-deny-claims-medicare-advantage-health-insurance-denials/), [Healthcare Finance News](https://www.healthcarefinancenews.com/news/class-action-lawsuit-against-unitedhealths-ai-claim-denials-advances), [Distilinfo](https://distilinfo.com/2026/03/12/court-orders-unitedhealth-to-disclose-ai-denial-algorithm/)

### 3.3 Cigna — PXDX Automated Claims Denial
- **Company/System**: Cigna, PXDX (procedure-to-diagnosis) automated claims review system
- **What was automated**: Fully automated claim denial. The system flagged discrepancies between diagnoses and Cigna's approved procedure lists, then auto-denied claims. Medical directors rejected claims without reviewing patient files at a rate of 1.2 seconds per case. One doctor denied up to 60,000 claims per month.
- **Year deployed**: Operational for years; ProPublica investigation published 2023
- **Outcome**: Failure. In two months, 300,000 claims were denied. Approximately 80% of denials were overturned on appeal, indicating the initial automated denials were largely incorrect.
- **Governance framework**: Inadequate. The system was designed to minimize human review, not ensure accuracy.
- **Regulatory action**: Congressional investigation by House Committee on Energy and Commerce. Multiple class action lawsuits filed.
- **Sources**: [ProPublica investigation](https://www.propublica.org/article/cigna-pxdx-medical-health-insurance-rejection-claims), [ProPublica Congressional follow-up](https://www.propublica.org/article/cigna-health-insurance-denials-pxdx-congress-investigation), [Healthcare Dive](https://www.healthcaredive.com/news/cigna-lawsuit-algorithm-claims-denials-california/688857/)

---

## 4. Autonomous Vehicles (Autonomous Decision-Making in Physical Systems)

### 4.1 Uber ATG — Self-Driving Vehicle (Elaine Herzberg)
- **Company/System**: Uber Advanced Technologies Group, self-driving Volvo XC90
- **What was automated**: Fully autonomous driving decisions including object detection, classification, and braking. The system was set to not activate emergency braking when under computer control (deliberately disabled by Uber to reduce "erratic vehicle behavior").
- **Year deployed**: Testing since 2016; fatal incident March 18, 2018
- **Outcome**: Fatal failure. First recorded pedestrian fatality involving a self-driving car. The system detected Herzberg 5.6 seconds before impact but cycled through classifications (unknown object, vehicle, bicycle) and never initiated emergency braking.
- **Governance framework**: Critically deficient. Uber had deliberately disabled collision avoidance capabilities. The safety driver was watching television on her smartphone.
- **Regulatory action**: Arizona prosecutors ruled Uber not criminally responsible. Safety driver Rafaela Vasquez pled guilty to endangerment, sentenced to three years' probation. Uber settled with Herzberg's family.
- **Sources**: [Wikipedia](https://en.wikipedia.org/wiki/Death_of_Elaine_Herzberg), [NPR](https://www.npr.org/2019/11/07/777438412/feds-say-self-driving-uber-suv-did-not-recognize-jaywalking-pedestrian-in-fatal-), [CNN](https://www.cnn.com/2023/07/29/business/uber-self-driving-car-death-guilty)

### 4.2 Cruise (GM) — Robotaxi Pedestrian Dragging Incident
- **Company/System**: Cruise (General Motors subsidiary), autonomous Chevrolet Bolt fleet
- **What was automated**: Fully autonomous urban driving and decision-making for a commercial robotaxi fleet.
- **Year deployed**: Commercial operations in San Francisco; incident October 2, 2023
- **Outcome**: Fatal-adjacent failure and company shutdown. A Cruise robotaxi dragged a pedestrian (who had been struck by another vehicle into its path) approximately 20 feet at 7.7 mph. The autonomous system misclassified a frontal impact as a side collision and executed a "pull over" maneuver instead of emergency stop.
- **Governance framework**: Critically deficient. Cruise admitted to filing a false report to NHTSA, lying about the incident details.
- **Regulatory action**: California DMV and CPUC suspended all permits. NHTSA fined Cruise $1.5 million. Cruise paid an additional $500,000 fine for false reporting. GM ultimately shut down the Cruise robotaxi program entirely.
- **Sources**: [CBS San Francisco](https://www.cbsnews.com/sanfrancisco/news/nhtsa-robotaxi-cruise-pay-penalty-failing-report-san-francisco-crash-involving-pedestrian/), [ABC7](https://abc7news.com/post/cruise-pay-500k-fine-lying-driverless-car-dragging-woman-2023-crash/15548339/), [NPR](https://www.npr.org/2023/12/30/1222083720/driverless-cars-gm-cruise-waymo-san-francisco-accidents)

### 4.3 Waymo — Commercial Robotaxi Fleet
- **Company/System**: Waymo (Alphabet subsidiary), autonomous vehicle fleet
- **What was automated**: Fully autonomous commercial passenger rides with no human driver in the vehicle. Over 96 million "rider-only" miles through June 2025.
- **Year deployed**: Commercial operations since 2020; expanded to multiple cities
- **Outcome**: Qualified success. 88% reduction in property damage claims and 92% reduction in bodily injury claims compared to the general population. Completed over 4 million fully driverless rides. 2,500 robotaxis operational as of November 2025.
- **Governance framework**: Active but evolving. Waymo publishes safety data and research papers. However, the company recalled 3,067 vehicles in 2026 after multiple incidents of driving around stopped school buses in Austin, Texas.
- **Regulatory action**: Approved for paid rides in Arizona, California, Texas, and Atlanta. NHTSA opened investigation over school bus incidents; closed a separate 14-month investigation.
- **Sources**: [Waymo Safety](https://waymo.com/safety/impact/), [Northeastern University analysis](https://news.northeastern.edu/2025/12/19/waymo-automonous-vehicle-safety/), [CPUC](https://www.cpuc.ca.gov/regulatory-services/licensing/transportation-licensing-and-analysis-branch/autonomous-vehicle-programs)

### 4.4 Tesla Autopilot / Full Self-Driving — Autonomous Driving Assistance
- **Company/System**: Tesla, Autopilot and Full Self-Driving (FSD) systems
- **What was automated**: Progressive automation of driving decisions. Despite the name, FSD requires human supervision ("Full Self-Driving (Supervised)").
- **Year deployed**: Autopilot since 2014; FSD Beta since 2020
- **Outcome**: Mixed with serious incidents. As of October 2025, 65 reported fatalities (54 verified by NHTSA or expert testimony). Notable cases include Joshua Brown (2016, failed to detect tractor-trailer) and Walter Huang (2018, Apple engineer).
- **Governance framework**: Contested. Tesla maintains FSD is supervised; critics argue the marketing name encourages over-reliance. No third-party audit requirement.
- **Regulatory action**: NHTSA upgraded its FSD investigation in March 2026 to engineering analysis (final stage before recall) covering 3.2 million vehicles.
- **Sources**: [Wikipedia list](https://en.wikipedia.org/wiki/List_of_Tesla_Autopilot_crashes), [PBS](https://www.pbs.org/newshour/nation/u-s-opens-new-investigation-into-teslas-full-self-driving-system-after-fatal-crash), [Insurance Journal](https://www.insurancejournal.com/news/national/2026/03/20/862650.htm)

---

## 5. Supply Chain and Logistics

### 5.1 Zillow Offers — Automated Home Purchasing (iBuyer)
- **Company/System**: Zillow, Zestimate-powered iBuyer program
- **What was automated**: Fully automated home purchase pricing. Zillow's algorithm (Zestimate) served as the initial offer price, autonomously determining what to pay for homes without human valuation.
- **Year deployed**: 2019; shut down November 2021
- **Outcome**: Catastrophic failure. Over $880 million in losses. The algorithm systematically overpaid for homes because it could not account for property-specific problems visible to human inspectors, and it was adversely selected against (sellers with overvalued homes preferentially accepted Zillow's offers).
- **Governance framework**: Inadequate. The company relied on its own Zestimate algorithm without adequate human override or market-condition circuit breakers.
- **Regulatory action**: No regulatory action. Zillow shut down the program voluntarily and laid off 25% of its staff.
- **Sources**: [Stanford GSB](https://www.gsb.stanford.edu/insights/flip-flop-why-zillows-algorithmic-home-buying-venture-imploded), [Museum of Failure](https://museumoffailure.com/exhibition/zillow-ai-failure), [CNN](https://edition.cnn.com/2021/11/09/tech/zillow-ibuying-home-zestimate)

### 5.2 Amazon — End-to-End Automated Supply Chain
- **Company/System**: Amazon, Supply Chain by Amazon (launched 2023)
- **What was automated**: End-to-end automated supply chain services including optimized inventory placement, automated replenishment, demand forecasting, and fulfillment decisions across millions of items.
- **Year deployed**: Automated supply chain services launched 2023
- **Outcome**: Success. Amazon's AI tracks millions of items in real-time, predicting customer demand and automating replenishment. The system optimizes shipping, storage costs, and inventory placement without per-decision human involvement.
- **Governance framework**: Proprietary. Not publicly documented in detail.
- **Sources**: [Cleverence](https://www.cleverence.com/articles/business-blogs/how-walmart-and-amazon-are-redefining-retail-efficiency-with-ai-powered-logistics/), [Fortune](https://fortune.com/2025/07/23/walmart-amazon-ai-supply-chain-retail/)

### 5.3 Ocado — AI-Powered Robotic Warehouse Fulfillment
- **Company/System**: Ocado, On-Grid Robotic Pick (OGRP)
- **What was automated**: Autonomous grocery picking and packing using AI-powered robots with machine learning, smart sensors, and computer vision. Robots adapt autonomously to different grocery types.
- **Year deployed**: Operational; picked over 30 million items using OGRP in 2024
- **Outcome**: Success. Major productivity gains with minimal robotic arm deployment.
- **Governance framework**: Not publicly detailed.
- **Sources**: [Supply Chain Digital](https://supplychaindigital.com/technology/how-ai-is-redefining-ocados-robotic-fulfilment-system)

---

## 6. Customer Service

### 6.1 Klarna — AI Customer Service Replacement
- **Company/System**: Klarna, OpenAI-powered AI assistant
- **What was automated**: Fully automated customer service handling. The chatbot handled two-thirds of all customer service chats (2.3 million conversations in its first month), equivalent to the work of 700 full-time agents.
- **Year deployed**: February 2024; partial reversal in 2025
- **Outcome**: Mixed. Initial metrics were impressive: resolution time dropped from 11 to 2 minutes, 25% fewer repeat inquiries, estimated $40 million profit improvement. However, by 2025, Klarna reversed course and began rehiring human agents. CEO acknowledged the company had "gone too far in the wrong direction" and that "cost unfortunately seems to have been a too predominant evaluation factor," resulting in lower quality.
- **Governance framework**: Minimal documented governance. The bot transferred complex issues to humans but the threshold for "complex" was set too broadly toward automation.
- **Investment**: $2-3 million to deploy.
- **Sources**: [OpenAI case study](https://openai.com/index/klarna/), [CX Dive on reversal](https://www.customerexperiencedive.com/news/klarna-reinvests-human-talent-customer-service-AI-chatbot/747586/), [Pragmatic Engineer analysis](https://blog.pragmaticengineer.com/klarnas-ai-chatbot/)

### 6.2 Air Canada — Chatbot Bereavement Fare Misinformation
- **Company/System**: Air Canada, AI-powered customer service chatbot
- **What was automated**: Fully automated customer service responses about company policies, including fare rules and refund procedures.
- **Year deployed**: Operational until 2024
- **Outcome**: Failure. The chatbot incorrectly told a grieving customer (Jake Moffatt) he could buy full-price tickets and apply for a bereavement discount retroactively within 90 days. Air Canada denied the refund, claiming the chatbot's advice was wrong.
- **Governance framework**: Absent. Air Canada tried to disclaim responsibility for its own chatbot's statements.
- **Regulatory action**: British Columbia Civil Resolution Tribunal ruled Air Canada is responsible for all information on its website, including chatbot responses. Ordered the airline to pay the fare difference. Air Canada removed the chatbot from its website as of April 2024.
- **Sources**: [CMSWire](https://www.cmswire.com/customer-experience/exploring-air-canadas-ai-chatbot-dilemma/), [CX Today](https://www.cxtoday.com/speech-analytics/court-orders-air-canada-to-pay-out-for-chatbots-bad-advice/), [Envive case study](https://www.envive.ai/post/case-study-of-air-canadas-chatbot)

### 6.3 DPD — Chatbot Profanity Incident
- **Company/System**: DPD (delivery company), AI-powered customer service chatbot
- **What was automated**: Automated parcel tracking and customer service responses.
- **Year deployed**: Operational; incident January 2024
- **Outcome**: Failure. After a faulty system update, the chatbot swore at a customer attempting to track a parcel. The incident went viral with over 800,000 views in 24 hours.
- **Governance framework**: Inadequate. A system update introduced the vulnerability without adequate testing.
- **Sources**: [CX Today](https://www.cxtoday.com/contact-center/3-times-customer-chatbots-went-rogue-and-the-lessons-we-need-to-learn/), [CustomerThink](https://customerthink.com/chatbots-under-fire-navigating-ai-pitfalls-with-insights-from-dpd-and-air-canada/)

### 6.4 Chevrolet Dealership — Chatbot Price Commitment
- **Company/System**: Chevrolet dealership, ChatGPT-powered customer service agent
- **What was automated**: Automated customer interaction including pricing discussions.
- **Outcome**: Failure. The chatbot agreed to sell a $75,000 Chevy Tahoe for $1, which was treated as a binding commitment.
- **Governance framework**: None. No price floor or authority limits on the chatbot.
- **Sources**: [Evidently AI](https://www.evidentlyai.com/blog/ai-failures-examples)

---

## 7. Legal/Compliance

### 7.1 JPMorgan COIN — Automated Contract Analysis
- **Company/System**: JPMorgan Chase, COiN (Contract Intelligence) platform
- **What was automated**: Automated extraction and analysis of key data points from commercial credit agreements, loan documents, and M&A contracts. Processes over 12,000 commercial credit agreements autonomously, replacing 360,000 hours of annual manual review.
- **Year deployed**: Launched 2017
- **Outcome**: Success. Reduced processing time from 360,000 man-hours to seconds. Compliance-related errors reduced by approximately 80%. Runs on JPMorgan's private cloud (Gaia).
- **Governance framework**: Documented. The system generates structured outputs for human review on flagged issues. Automated compliance checks ensure contracts meet evolving regulatory requirements across jurisdictions. AI categorizes contracts by risk level, escalating high-risk agreements.
- **Regulatory action**: No adverse actions. The system operates within JPMorgan's regulated environment.
- **Sources**: [Harvard D3](https://d3.harvard.edu/platform-rctom/submission/jp-morgan-coin-a-banks-side-project-spells-disruption-for-the-legal-industry/), [DigitalDefynd](https://digitaldefynd.com/IQ/jp-morgan-using-ai-case-study/), [GoBeyond AI](https://www.gobeyond.ai/ai-resources/case-studies/jpmorgan-coin-ai-contract-analysis-legal-docs)

---

## 8. Government / Public Sector Automated Decision-Making

### 8.1 Australia Robodebt — Automated Welfare Debt Recovery
- **Company/System**: Australian Government, automated debt assessment and recovery system
- **What was automated**: Fully automated welfare debt calculation and recovery. The system used income averaging from tax data to calculate alleged overpayments and issued debt notices automatically without human review. The entire process was conducted online without human involvement.
- **Year deployed**: Pilot 2015; full rollout September 2016; terminated June 2020
- **Outcome**: Catastrophic failure. The government unlawfully raised A$1.73 billion in debts against 433,000 people, of which $751 million was wrongly recovered from 381,000 people. The scheme caused severe distress, and the Royal Commission linked it to suicides among affected welfare recipients.
- **Governance framework**: Deliberately bypassed. The Royal Commission found that government officials knew the legal basis was questionable but proceeded anyway. The scheme reversed the burden of proof, requiring welfare recipients to disprove algorithmically generated debts.
- **Regulatory action**: Federal Court ruled the scheme unlawful. The government was forced to cancel all debts, refund $746 million, and pay $112 million in compensation. A Royal Commission investigated the scheme in 2023.
- **Sources**: [Wikipedia](https://en.wikipedia.org/wiki/Robodebt_scheme), [Human Rights Law Centre](https://www.hrlc.org.au/case-summaries/2021-9-30-the-federal-court-approves-a-112-million-settlement-for-the-failures-of-the-robodebt-system/), [Oxford Blavatnik School](https://www.bsg.ox.ac.uk/blog/australias-robodebt-scheme-tragic-case-public-policy-failure)

### 8.2 Dutch SyRI — Automated Welfare Fraud Detection
- **Company/System**: Netherlands Government, SyRI (System Risk Indication)
- **What was automated**: Automated fraud risk scoring of welfare recipients by cross-referencing government databases. The system operated without transparency about its methods and was deployed exclusively in low-income neighborhoods with high immigrant populations.
- **Year deployed**: Legislation passed 2014; operational until court ruling February 2020
- **Outcome**: Failure. Court found the system was too opaque, collected too much data, and its purposes were not clear and specific enough.
- **Governance framework**: Legally deficient. The system lacked transparency, had no adequate explanation mechanism, and discriminated based on socio-economic and migrant status.
- **Regulatory action**: The Hague District Court ruled SyRI violated Article 8 of the European Convention on Human Rights (right to privacy) on February 5, 2020. The Dutch government did not appeal. This was among the first times a court invalidated a welfare fraud detection system for breaching human rights.
- **Sources**: [IAPP](https://iapp.org/news/a/digital-welfare-fraud-detection-and-the-dutch-syri-judgment), [AlgorithmWatch](https://algorithmwatch.org/en/syri-netherlands-algorithm/), [OHCHR](https://www.ohchr.org/en/press-releases/2020/02/landmark-ruling-dutch-court-stops-government-attempts-spy-poor-un-expert)

### 8.3 COMPAS — Automated Recidivism Risk Scoring
- **Company/System**: Northpointe (now Equivant), COMPAS (Correctional Offender Management Profiling for Alternative Sanctions)
- **What was automated**: Automated risk scoring used in pretrial and sentencing decisions. While formally advisory, judges routinely incorporated COMPAS scores into sentencing (e.g., Wisconsin v. Loomis, where a judge cited the COMPAS high-risk score in imposing an 8.5-year sentence).
- **Year deployed**: Widely used across US jurisdictions
- **Outcome**: Contested failure. ProPublica's 2016 analysis of Broward County, Florida found: overall accuracy of only 61%; Black defendants were 77% more likely to be flagged as higher risk of future violent crime; Black defendants were 45% more likely to be predicted to commit any future crime; Black defendants were almost twice as likely to be labeled high risk but not actually re-offend.
- **Governance framework**: Minimal. Northpointe/Equivant kept the algorithm proprietary. No independent audit requirement. Northpointe disputed ProPublica's analysis but did not dispute the error rate imbalances.
- **Regulatory action**: Wisconsin Supreme Court allowed COMPAS use but required warnings about its limitations. No federal regulation of risk assessment tools in criminal justice.
- **Sources**: [ProPublica "Machine Bias"](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing), [ProPublica methodology](https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm), [AIID Incident 40](https://incidentdatabase.ai/cite/40/)

### 8.4 Rite Aid — Automated Facial Recognition for Surveillance
- **Company/System**: Rite Aid Corporation, AI-based facial recognition system for in-store surveillance
- **What was automated**: Automated identification of customers flagged as potential shoplifters. The system matched live camera feeds against a database of previously identified individuals and triggered alerts autonomously.
- **Year deployed**: 2012 to 2020
- **Outcome**: Failure. The system generated false positives disproportionately in stores located in plurality-Black and plurality-Asian communities compared to plurality-White communities.
- **Governance framework**: Absent. The FTC found Rite Aid failed to implement reasonable safeguards to prevent consumer harm.
- **Regulatory action**: FTC banned Rite Aid from using facial recognition for five years (December 2023). Required deletion of all collected photos, videos, data, models, and algorithms. This was the first FTC enforcement action addressing alleged discrimination through automated decision-making.
- **Sources**: [FTC press release](https://www.ftc.gov/news-events/news/press-releases/2023/12/rite-aid-banned-using-ai-facial-recognition-after-ftc-says-retailer-deployed-technology-without), [CNN](https://www.cnn.com/2023/12/20/tech/rite-aid-ai-ftc-settlement), [Arnold & Porter analysis](https://www.arnoldporter.com/en/perspectives/advisories/2024/01/ftc-case-against-rite-aid-deployment-of-ai-based-technology)

### 8.5 Police Facial Recognition — Wrongful Arrest Cases
- **Systems**: Various police departments using IDEMIA, Clearview AI, and other facial recognition systems
- **What was automated**: Automated suspect identification from surveillance footage, with police in multiple documented cases treating AI matches as sufficient for arrest without adequate corroboration.
- **Documented wrongful arrests**: At least eight Americans wrongfully arrested after facial recognition matches, including:
  - Nijeer Parks (New Jersey, 2019): wrongful shoplifting arrest
  - Randal Quran Reid (Georgia/Louisiana): wrongfully jailed nearly a week; $200,000 settlement
  - Angela Lipps (Tennessee, 2026): jailed for over five months for crimes in a state she had never visited
- **Governance framework**: Absent in practice. A January 2025 Washington Post investigation found that in every documented case, investigators skipped fundamental steps (checking alibis, comparing physical descriptions).
- **Regulatory action**: Growing state-by-state regulation. No federal ban. Individual settlements in wrongful arrest cases.
- **Sources**: [ACLU](https://www.aclu.org/news/privacy-technology/police-say-a-simple-warning-will-prevent-face-recognition-wrongful-arrests-thats-just-not-true), [Washington Post investigation](https://www.washingtonpost.com/business/interactive/2025/police-artificial-intelligence-facial-recognition/), [CNN](https://www.cnn.com/2026/03/29/us/angela-lipps-ai-facial-recognition)

---

## 9. Social Media / Content

### 9.1 Microsoft Tay — Autonomous Social Media Chatbot
- **Company/System**: Microsoft, Tay chatbot on Twitter
- **What was automated**: Fully autonomous social media posting. Tay was designed to engage users in dialogue and learn from interactions, posting tweets autonomously.
- **Year deployed**: March 23, 2016; shut down within 16 hours
- **Outcome**: Catastrophic failure. The bot began posting racist, sexist, and anti-Semitic content after being manipulated by trolls who taught it inflammatory language.
- **Governance framework**: None. No content filtering, no adversarial testing, no guardrails against manipulation.
- **Sources**: [Wikipedia](https://en.wikipedia.org/wiki/Tay_(chatbot)), [IEEE Spectrum](https://spectrum.ieee.org/in-2016-microsofts-racist-chatbot-revealed-the-dangers-of-online-conversation), [AIID Incident 6](https://incidentdatabase.ai/cite/6/)

---

## 10. AI Delegation and Governance Frameworks

### 10.1 Google DeepMind — Intelligent AI Delegation Framework (2026)
- **Publication**: "Intelligent AI Delegation" (arXiv:2602.11865, February 2026)
- **Framework scope**: Addresses task allocation, transfer of authority, responsibility, accountability, role boundaries, clarity of intent, and trust mechanisms. Applicable to both human and AI delegators in complex delegation networks.
- **Key principles**: Privilege attenuation (sub-delegated agents receive only minimum required permissions), least-privilege access to APIs and systems, regular review of authority expansion.
- **Production status**: Theoretical framework. Not yet documented in production deployment.
- **Sources**: [arXiv](https://arxiv.org/abs/2602.11865), [The AI Insider](https://theaiinsider.tech/2026/02/17/deepmind-study-proposes-rules-for-how-ai-agents-should-delegate/)

### 10.2 EU AI Act — Regulatory Governance Framework
- **Scope**: The most comprehensive automated decision-making governance framework enacted into law.
- **Key provisions**: High-risk AI systems (including credit scoring, hiring, law enforcement, healthcare) must provide clear explanations of the AI's role, main decision parameters, and human oversight involved. Fines up to EUR 35 million or 7% of global turnover.
- **Timeline**: Penalty regime effective August 2, 2025. High-risk system rules effective August 2, 2026 (though a proposed "Digital Omnibus" may push some to December 2027).
- **Production adoption**: As of 2025, 77% of organizations surveyed were working on AI governance, jumping to 90% among those already using AI.
- **Sources**: [EU AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), [LegalNodes](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks)

### 10.3 Enterprise AI Guardrails — Current State
- **Adoption**: Only about 1 in 5 companies has mature governance for AI agents (Deloitte AI Institute, Fall 2025). Only 22% of decision-makers trust autonomous AI agents (McKinsey). 71% of compliance leaders lack visibility into their company's AI use cases.
- **Projection**: Gartner predicts over 40% of agentic AI projects will be canceled by end of 2027 due to escalating costs, unclear business value, or inadequate risk controls.
- **Effectiveness**: Layered guardrails can catch 95% of safety issues before they reach users. Organizations with AI-specific controls reduced breach costs by $2.1 million on average.
- **Sources**: [Palo Alto Networks](https://www.paloaltonetworks.com/cyberpedia/what-is-agentic-ai-governance), [CSA](https://cloudsecurityalliance.org/blog/2026/03/17/from-guardrails-to-governance-why-enterprise-ai-needs-a-control-layer), [MIT CISR](https://cisr.mit.edu/publication/2026_0327_AIGovernance_Wixom)

---

## Cross-Case Analysis

### Pattern 1: Governance presence strongly predicts outcome
| Case | Governance | Outcome |
|------|-----------|---------|
| Upstart (lending) | Strong (CFPB-supervised) | Success |
| JPMorgan COIN (legal) | Documented (human escalation) | Success |
| Waymo (driving) | Active (published safety data) | Qualified success |
| Amazon supply chain | Proprietary but operational | Success |
| Knight Capital (trading) | None | Catastrophic loss |
| Uber ATG (driving) | Deliberately disabled | Fatal |
| Robodebt (welfare) | Deliberately bypassed | Catastrophic harm |
| Rite Aid (facial recognition) | None | FTC ban |

### Pattern 2: The "full autonomy without override" failure mode
Cases where the system operated without adequate human override capability consistently produced the worst outcomes: Knight Capital (no kill switch worked), Uber ATG (emergency braking disabled), Robodebt (automated debt notices with burden of proof reversed), Cigna/UnitedHealth (1.2-second "review" per claim).

### Pattern 3: Post-hoc discovery of bias
Automated systems deployed without pre-deployment bias testing consistently exhibited discriminatory outcomes: Amazon hiring, Apple Card, COMPAS, Rite Aid facial recognition, police facial recognition. The only lending case with positive equity outcomes (Upstart) had rigorous pre-deployment and ongoing bias testing mandated by its CFPB agreement.

### Pattern 4: The autonomy-accountability gap
Organizations consistently attempted to disclaim responsibility for autonomous system outputs: Air Canada (chatbot not our responsibility), Uber (blamed safety driver), police departments (facial recognition is just a lead), Cigna (algorithm is just a screening tool). Courts and regulators have increasingly rejected these disclaimers.

### Pattern 5: Reversal pattern in customer service
Klarna's trajectory (automate aggressively, then partially reverse) appears to be emerging as a common pattern. Organizations discover that quality degradation from full automation is not immediately visible in efficiency metrics but emerges in customer satisfaction and repeat-contact rates over time.

### Pattern 6: Quantitative trading as the exception
Fully autonomous trading systems (Renaissance, Two Sigma, Citadel) represent the only domain where full autonomy has sustained long-term success. Key differences: immediate, quantifiable feedback loops; no external stakeholders harmed by individual decisions; proprietary governance structures evolved over decades.

### Pattern 7: Agentic AI at scale remains rare
Only 2% of organizations have deployed agentic AI at scale (2025 data). 48% claim production deployment, but these are mostly narrow single-task agents with human fallback. The 14% production-ready figure from mid-2025 has only modestly improved.

---

## Market Research / Product Development

No documented cases were found of AI autonomously conducting market research in a closed decision loop (where the AI designs the research, collects data, analyzes findings, and makes product decisions without human involvement). AI is used extensively for sentiment analysis, trend detection, and survey analysis, but the research-to-decision loop remains human-directed in all documented cases. This represents a gap in the current automation landscape.

---

## Key Regulatory and Legal Milestones

| Year | Event |
|------|-------|
| 2010 | Flash Crash leads to circuit breaker rules |
| 2016 | ProPublica COMPAS analysis published |
| 2017 | CFPB issues first no-action letter to Upstart |
| 2018 | Amazon hiring tool discontinued; Uber ATG fatal crash |
| 2019 | Apple Card gender bias allegations; NYSDFS investigation |
| 2020 | Dutch court strikes down SyRI; Robodebt terminated |
| 2023 | Cruise shutdown; Rite Aid FTC ban; Cigna PXDX exposed; UnitedHealth sued |
| 2024 | EU AI Act enters force; Air Canada chatbot ruling; Klarna AI launch |
| 2025 | Workday collective action certified; HireVue EEOC complaint; EU AI Act penalties active; Klarna reversal |
| 2026 | NHTSA upgrades Tesla FSD probe; UnitedHealth ordered to disclose algorithm; EU high-risk rules effective |
