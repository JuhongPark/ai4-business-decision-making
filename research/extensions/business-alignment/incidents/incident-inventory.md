# Business-Relevant AI Incident Inventory

status: draft
date: 2026-03-21
purpose: Build a broader, more systematic inventory of business-relevant AI incidents using the general-AI versus LLM-specific split.
scope: selected public incidents with meaningful business, legal, operational, or reputational consequences

## Why This Note Exists

This inventory provides the empirical foundation for the 6-dimensional adaptive delegation framework. The 71 cases documented here were classified using Amodei et al. (2016) and Weidinger et al. (2022), and the recurring failure patterns directly informed the framework's dimensions, scoring model, and override rules.

The earlier incident note separated general AI incidents from LLM-specific incidents, but it was still exemplar-based.

This note applies a more repeatable incident-research protocol:

1. define what counts as a business-relevant AI incident
2. search by sector, failure mechanism, and evidence type
3. validate incidents with official sources where possible
4. keep litigation signals separate from fully adjudicated findings
5. stop only after the main buckets begin to repeat rather than generate genuinely new incident types

## What Counts As An Incident Here

An incident is included when at least one of the following is true:

- it produced clear financial loss, a business wind-down, or a public product rollback
- it triggered a lawsuit, settlement, sanction, or regulator action
- it exposed a concrete governance failure with visible customer, worker, or public harm
- it forced a company to pause, restrict, or redesign AI deployment
- it materially affected trust, brand credibility, or internal AI policy

## Classification Rule

### General AI

Included here when the dominant failure mechanism is rooted in:

- prediction
- scoring
- ranking
- optimization
- surveillance
- autonomy

and is not mainly dependent on LLM-style generation or dialogue.

### LLM-Specific

Included here when the dominant failure mechanism depends on:

- fluent hallucination
- conversational over-trust
- generated explanations or narratives
- prompt-based data leakage
- weak verification inside the same interface
- large-scale generation of persuasive or error-prone language

## Inventory Coverage

This version now covers the following sectors:

- real estate
- employment
- retail
- mobility and autonomy
- housing
- fintech and pricing
- customer service
- legal services
- enterprise internal-use governance
- search and consumer AI products
- media and publishing

## Part I. General AI Incidents

| Date | Company / case | Business use | Dominant failure mechanism | Public consequence | Evidence type |
| --- | --- | --- | --- | --- | --- |
| 2021-11-02 | Zillow Offers | Home-price forecasting and iBuying operations | Forecast error plus over-delegation to predictive models in a volatile market | Zillow wound down the business, reported a roughly $304 million inventory write-down, expected additional losses, and cut about 25% of staff | Investor release; SEC filing |
| 2018-10-10 | Amazon recruiting tool | Resume screening and hiring ranking | Historical training-data bias and proxy discrimination | Amazon scrapped the internal tool after it penalized resumes with signals associated with women | Reuters reporting |
| 2018-03-18 crash; later NTSB findings | Uber ATG | Developmental automated driving system | Weak safety culture, poor oversight, automation complacency, and brittle real-world handling | Fatal crash in Tempe; NTSB identified operator distraction plus inadequate safety risk assessment and oversight | NTSB investigation |
| 2022-06-21 complaint; 2022-06-27 settlement approval | Meta housing ads | Ad-delivery and audience expansion for housing ads | Algorithmic discrimination in ad delivery and lookalike targeting | DOJ settlement required Meta to stop using Special Ad Audience for housing ads and build a variance-reduction system | DOJ complaint and settlement materials |
| 2023-12-19 FTC action | Rite Aid | Facial recognition for retail surveillance and loss prevention | Poor safeguards, false positives, and disproportionate harm | FTC action led to a five-year ban on facial-recognition surveillance use and broader compliance obligations | FTC complaint and order |
| 2022-05-05 suit; 2023-09-11 settlement | iTutorGroup | Automated applicant screening | Explicit age-based automated rejection rules | EEOC settlement required payment and relief after software rejected older applicants | EEOC suit and settlement |
| 2024-07-12 key ruling | Workday litigation | Outsourced hiring screening tools | Delegation of traditional hiring functions to algorithmic systems | Court allowed key discrimination claims to proceed under an agent theory | Court case page; legal summary of ruling |
| 2023-01-09 DOJ statement | SafeRent litigation signal | Algorithm-based tenant screening | Potential disparate impact in rental screening | DOJ statement reinforced that FHA theories can apply to algorithmic screening vendors | DOJ statement of interest |
| 2024-08-23 | RealPage | Rental pricing software | Algorithmic coordination and data-sharing across competitors | DOJ and states sued RealPage for alleged unlawful pricing coordination that harmed renters | DOJ complaint announcement |
| 2024-01-24 | FloatMe | Cash-advance eligibility and underwriting claims | Deceptive claims about algorithmic decisioning plus discriminatory practices | FTC settlement required $3 million for refunds and banned deceptive claims about algorithmic underwriting | FTC complaint and order |

## Reading Of The General AI Cases

The general AI incidents now cluster into five recurring patterns.

### 1. Objective and optimization failures

Zillow, RealPage, and parts of Amazon's hiring case all show that the main problem is often not whether a model is technically advanced.

It is whether the firm attached the model to the wrong business objective or scaled the objective too aggressively.

### 2. Historical bias and proxy discrimination

Amazon, iTutorGroup, Meta housing ads, Workday, and SafeRent all point toward a core lesson:

automating a decision process often automates the institution's history, not neutral merit.

### 3. Safety and real-world brittleness

Uber shows that even when perception or control systems are the visible issue, the deeper failure often lies in:

- safety culture
- operator role design
- escalation structure
- unrealistic assumptions about supervision

### 4. Accountability does not disappear when a vendor is involved

Workday, SafeRent, and RealPage matter because they show that:

- outsourcing the system does not dissolve responsibility
- delegation to software vendors can still create legal exposure

### 5. Regulation is moving from abstract concern to operational intervention

FTC, DOJ, and EEOC actions show that regulators are increasingly willing to intervene at the level of:

- design choices
- data use
- system deployment
- vendor structure
- business process delegation

## Part II. LLM-Specific Incidents

| Date | Company / case | Business use | Dominant failure mechanism | Public consequence | Evidence type |
| --- | --- | --- | --- | --- | --- |
| 2024-02-14 decision | Air Canada | Website chatbot for customer policy guidance | Fluent policy misstatement and customer reliance | Tribunal held Air Canada liable for inaccurate chatbot advice on bereavement fares and awarded compensation | Tribunal summary by legal practitioners |
| 2023-06-22 | Mata v. Avianca | Legal research and briefing | Hallucinated cases plus failed attorney verification | Federal court imposed sanctions and a $5,000 penalty after lawyers submitted fake ChatGPT-generated cases | Court order |
| 2025-07-28 | AP Electric sanctions | Legal research and briefing | Fabricated quotations and parentheticals generated through AI | Federal court sanctioned counsel and explicitly warned that real case names do not solve LLM reliability problems | Court order |
| 2023-05-02 reported ban | Samsung | Internal employee use of ChatGPT and similar tools | Prompt-based leakage of confidential code and data | Samsung temporarily banned generative AI tools on company devices and networks after internal leaks | TechCrunch reporting citing Samsung spokesperson and memo |
| 2023-02-08 | Google Bard demo | Public-facing launch of a conversational search product | Hallucinated factual error in high-visibility product demo | Alphabet shares fell sharply and more than $100 billion in market value was erased after Bard gave a wrong answer in promotional material | Reuters reporting |
| 2024-02-23 | Google Gemini image generation pause | Consumer conversational AI product | Overcompensation, inaccurate and offensive generated outputs | Google paused image generation of people in Gemini and publicly acknowledged the feature had missed the mark | Official Google blog |
| 2023-01 to 2023-02 | CNET / Red Ventures | AI-generated finance explainers and editorial production | Large-scale generative content errors, poor disclosure, and plagiarism concerns | Articles required corrections, credibility suffered, and the company paused parts of the rollout | CNET scandal reporting by Futurism |
| 2025-05-21 | Chicago Sun-Times / Philadelphia Inquirer supplement | AI-assisted content creation for lifestyle publishing | Hallucinated nonfiction disguised as real recommendations | Fake summer reading list entries led to retractions, investigation, and termination of the freelance creator by King Features | AP reporting |
| 2024-01-20 | DPD chatbot incident | Customer-service chatbot | Prompt-induced rogue behavior and weak control of brand voice | DPD disabled the affected AI component after the chatbot swore and insulted the company | The Guardian reporting |
| 2026-02-25 | Elegant Enterprise-Wide Solutions | AI-generated job advertisements | Unlawful content generation in hiring communications | DOJ settlement addressed AI-generated ads that unlawfully excluded U.S. workers based on citizenship status | DOJ press release |

## Reading Of The LLM Cases

The LLM-specific cases reveal a different set of recurring mechanisms.

### 1. Fluent falsehood is a business risk, not just a model-quality issue

Air Canada, Bard, and the fake-book-list case all show that a wrong answer becomes more dangerous when it is:

- confident
- user-facing
- embedded in a trusted interface
- treated as actionable guidance

### 2. Human review often fails inside the same interface

Mata and AP Electric are especially important because they show that "human in the loop" can fail when the human reviewer:

- does not independently verify claims
- treats the output as a plausible draft rather than as untrusted content
- stays inside the same generative workflow

### 3. LLM use creates a new data-boundary problem

Samsung is a strong example of this.

The incident was not mainly about output accuracy.

It was about the fact that a useful conversational tool invites employees to paste sensitive material into an external system.

### 4. Brand voice becomes an alignment problem

DPD and Air Canada both show that once a conversational agent speaks in the name of the company, the firm may face:

- reputational harm
- liability risk
- customer confusion
- pressure to disable or tightly constrain the system

### 5. Content-scale risk is different from prediction risk

CNET and the fake-book-list incident matter because generative systems can create:

- many errors quickly
- misleadingly polished prose
- weak disclosure trails
- downstream editorial and reputational cleanup costs

### 6. LLM incidents often require withdrawal or hard constraints, not just fine-tuning

Gemini's image pause, Samsung's restriction, and DPD's disablement all show a recurring governance move:

when the system's behavior becomes difficult to bound in production, firms often resort to pausing features, shrinking scope, or re-routing the workflow.

## Cross-Category Comparison

The split between general AI and LLM-specific incidents now looks clearer.

### General AI incidents are mostly about:

- the wrong objective
- biased data
- brittle prediction
- unsafe scaling
- classification or ranking errors
- weak institutional accountability

### LLM-specific incidents are mostly about:

- fluent but wrong outputs
- conversational reliance
- generated explanations
- prompt leakage
- same-interface verification failure
- uncontrolled language generation in public or professional settings

This distinction is important because it suggests that the governance toolkit should not be the same.

### General AI governance usually needs:

- threshold setting
- bias testing
- objective review
- human override design
- vendor accountability rules
- risk management for deployment in the real environment

### LLM governance usually needs:

- verification outside the chat interface
- prompt and data-boundary controls
- stronger brand and policy grounding
- restrictions on use in high-consequence communication
- disclosure and editorial control
- guardrails for generated rationales, not just generated answers

## Most Important Incidents For Your Research

If the goal is business-context AI alignment, the strongest incidents are not necessarily the most famous ones.

The most conceptually useful incidents are the ones that best reveal the shape of the governance problem.

### Most useful general AI cases

- Zillow Offers: over-delegation to high-exposure forecasting
- Meta housing ads: algorithmic discrimination in delivery rather than only targeting
- Rite Aid: automated identification with weak safeguards and real consumer harm
- Workday / SafeRent: vendor-mediated decision systems and delegated accountability
- RealPage: algorithmic coordination and pricing power in concentrated markets

### Most useful LLM cases

- Air Canada: chatbot output as legally attributable company speech
- Mata and AP Electric: why human review does not guarantee safe LLM use
- Samsung: internal-use productivity can conflict with data security
- CNET and the fake-book-list case: scale risks in generated content workflows
- Bard and Gemini: public-facing model failure can force immediate rollback or impose market cost

## Saturation Check

At this stage, the incident inventory is much broader than the first pass, but it is still not complete.

The most under-covered buckets remain:

- internal enterprise copilots in finance, procurement, and operations
- B2B sales and customer-success copilots
- supply-chain and logistics decision support
- clinical or biomedical enterprise deployments outside insurance denial workflows
- agentic approval systems where LLMs do more than draft and begin to sequence or trigger actions

Those should be the next expansion targets if you continue the incident work.

## Bottom-Line Reading

The broader search confirms that the distinction between general AI incidents and LLM-specific incidents is real and analytically useful.

General AI incidents mainly expose failures in:

- optimization
- prediction
- screening
- surveillance
- autonomy

LLM-specific incidents mainly expose failures in:

- language-mediated trust
- verification
- policy communication
- generated content governance
- prompt and interface control

That means your research should not ask only:

- "When does AI fail in firms?"

It should ask:

- "What kind of AI failure is this, and what layer of business alignment failed?"

That is a much stronger research question.

## Sources

### General AI

- Zillow investor release, November 2, 2021: https://investors.zillowgroup.com/investors/news-and-events/news/news-details/2021/Zillow-Group-Reports-Third-Quarter-2021-Financial-Results--Shares-Plan-to-Wind-Down-Zillow-Offers-Operations/default.aspx?stream=business
- Zillow SEC filing, November 2, 2021: https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/z-20211102.htm
- Reuters on Amazon recruiting tool, October 10, 2018: https://www.investing.com/news/stock-market-news/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-1637988
- NTSB Tempe investigation: https://www.ntsb.gov/investigations/Pages/HWY18MH010.aspx
- DOJ Meta housing ads case page: https://www.justice.gov/crt/case/united-states-v-meta-platforms-inc-fka-facebook-inc-sdny
- FTC on Rite Aid facial recognition, December 19, 2023: https://www.ftc.gov/news-events/news/press-releases/2023/12/rite-aid-banned-using-ai-facial-recognition-after-ftc-says-retailer-deployed-technology-without
- EEOC suit against iTutorGroup, May 5, 2022: https://www.eeoc.gov/newsroom/eeoc-sues-itutorgroup-age-discrimination
- EEOC settlement with iTutorGroup, September 11, 2023: https://www.eeoc.gov/newsroom/itutorgroup-pay-365000-settle-eeoc-discriminatory-hiring-suit
- Northern District of California case page, Mobley v. Workday: https://cand.uscourts.gov/cases-e-filing/cases/323-cv-00770-rfl/mobley-v-workday-inc
- Duane Morris summary of July 12, 2024 Workday ruling: https://www.mondaq.com/unitedstates/employee-rights-labour-relations/1493526/california-federal-court-denies-motion-to-dismiss-artificial-intelligence-employment-discrimination-lawsuit
- DOJ SafeRent statement of interest, January 9, 2023: https://www.justice.gov/usao-ma/pr/us-attorneys-office-files-statement-interest-fair-housing-act-case-alleging-unlawful
- DOJ RealPage complaint announcement, August 23, 2024: https://www.justice.gov/opa/pr/justice-department-sues-realpage-algorithmic-pricing-scheme-harms-millions-american-renters
- FTC FloatMe action, January 24, 2024: https://www.ftc.gov/news-events/news/press-releases/2024/01/ftc-acts-stop-floatmes-deceptive-free-money-promises-discriminatory-cash-advance-practices-baseless

### LLM-Specific

- Deeth Williams Wall summary of Moffatt v. Air Canada: https://www.dww.com/articles/bc-tribunal-finds-air-canada-liable-for-inaccurate-advice-given-by-website-chatbot
- Mata v. Avianca sanctions order: https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1%3A2022cv01461/575368/54/
- AP Electric sanctions order, July 28, 2025: https://law.justia.com/cases/federal/district-courts/michigan/miedce/4%3A2023cv11342/370246/92/
- TechCrunch on Samsung's ban, May 2, 2023: https://techcrunch.com/2023/05/02/samsung-bans-use-of-generative-ai-tools-like-chatgpt-after-april-internal-data-leak/
- Reuters on Bard error via Al Jazeera, February 8, 2023: https://www.aljazeera.com/economy/2023/2/8/google-shares-tank-8-as-ai-chatbot-bard-flubs-answer-in-ad
- Google blog on Gemini image generation issue, February 23, 2024: https://blog.google/products/gemini/gemini-image-generation-issue/
- Futurism on CNET AI article rollout: https://futurism.com/the-byte/cnet-publishing-articles-by-ai
- Futurism on CNET labeling and disclosure issues: https://futurism.com/cnet-ai-articles-label
- Futurism on CNET errors and plagiarism concerns: https://futurism.com/red-ventures-knew-errors-plagiarism-deployed-cnet-anyway
- AP on fake summer book list, May 21, 2025: https://apnews.com/article/fake-book-list-ai-newspaper-summer-reading-fcdf454a5b467dad3adfed6ca1a224d2
- The Guardian on DPD chatbot incident, January 20, 2024: https://www.theguardian.com/technology/2024/jan/20/dpd-ai-chatbot-swears-calls-itself-useless-and-criticises-firm
- DOJ on Elegant Enterprise-Wide Solutions, February 25, 2026: https://www.justice.gov/opa/pr/civil-rights-division-obtains-settlement-company-used-ai-generated-advertisements-excluded
