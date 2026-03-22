# General AI Incidents vs LLM-Specific Incidents in Business Contexts

status: draft
date: 2026-03-21
purpose: Separate major business-relevant AI incidents into two categories: general non-LLM AI incidents and LLM-specific incidents.
scope: selected incidents relevant to business-context AI alignment

## Why This Note Exists

Not all important AI incidents are the same.

Some incidents arise from:

- predictive models
- scoring systems
- optimization systems
- ranking systems
- autonomous systems

These are important, but they are not the same as incidents that arise specifically from:

- large language models
- conversational systems
- generative assistants
- human reliance on fluent, open-ended model outputs

If your research is about business-context AI alignment, separating these categories is useful.

The risks overlap, but the mechanisms differ.

## Classification Rule Used Here

### Category 1: General AI incidents

These are cases where the core failure mechanism is **not** specific to LLMs.

The main problem is usually one or more of:

- biased training data
- wrong optimization target
- brittle prediction in real environments
- poor safety culture
- weak oversight of automated decision systems
- over-delegation to non-generative models

### Category 2: LLM-specific incidents

These are cases where the core failure mechanism depends on features that are strongly associated with LLMs or generative AI systems:

- hallucinated but fluent outputs
- conversational over-trust
- human reliance on generated explanations
- prompt-based disclosure of sensitive information
- weak verification inside a dialogue interface
- large-scale generation of persuasive or error-prone content

Some incidents could be argued either way.

When classification is ambiguous, this note places the incident in the category of its **dominant failure mechanism**.

## Part I. General AI Incidents

## 1. Zillow Offers Wind-Down (2021)

**What happened**

On November 2, 2021, Zillow announced that it would wind down Zillow Offers, its home-buying business.

In the same announcement, the company said it had taken an inventory write-down of about $304 million and expected additional losses of roughly $240 million to $265 million.

It also said the wind-down would include a workforce reduction of about 25%.

### Why this belongs in the general AI category

This was not an LLM problem.

The core issue was the use of predictive and operational models in a capital-intensive business under real market volatility.

### What went wrong

Zillow explicitly said that the unpredictability of forecasting home prices was much greater than expected.

In business-context alignment terms, the deeper issue was not just model error.

It was:

- overconfidence in forecasting quality
- connecting model outputs too directly to high-exposure business decisions
- insufficient respect for operational and market uncertainty

### Why it matters

This is one of the clearest cases of **objective misalignment plus over-delegation**.

Even if the model was useful in some limited sense, the firm appears to have attached it to a business process that was too financially exposed to forecast error.

### Alignment lesson

Better prediction alone is not enough.

Firms also need:

- authority thresholds
- volatility buffers
- domain-specific restriction logic
- a clear rule for when not to scale automation

## 2. Amazon Recruiting Tool Bias (2018)

**What happened**

Reuters reported on October 10, 2018 that Amazon had scrapped an internal recruiting tool after it showed bias against women.

The system reportedly learned from historical hiring patterns and downgraded resumes containing signals associated with women, including the word "women's" in some contexts.

### Why this belongs in the general AI category

This was not a generative or conversational system.

It was a machine-learning screening and ranking problem.

### What went wrong

The model learned from historical data that already reflected male dominance in the technical roles being targeted.

In effect, the system optimized against biased institutional history.

### Why it matters

This is a classic example of **training-data bias plus proxy discrimination**.

It remains one of the most widely cited examples of why automating hiring does not automatically produce fairer decisions.

### Alignment lesson

The central issue is not only whether the model predicts accurately.

It is also:

- what target it is learning
- what historical patterns are embedded in the data
- whether the automated recommendation should be allowed to shape gatekeeping decisions at all

## 3. Uber ATG Tempe Fatal Crash (2018 crash; NTSB findings released later)

**What happened**

On March 18, 2018, an Uber Advanced Technologies Group test vehicle operating with a developmental automated driving system struck and killed a pedestrian in Tempe, Arizona.

The NTSB later found that the probable cause included the vehicle operator's failure to monitor the roadway, but also Uber ATG's inadequate safety risk assessment procedures, ineffective oversight of vehicle operators, and lack of adequate mechanisms to address automation complacency.

### Why this belongs in the general AI category

This was an autonomy and safety-management failure, not an LLM failure.

### What went wrong

The deeper problem was not only perception or detection performance.

The NTSB findings point to:

- weak safety culture
- inadequate risk management
- poor operator oversight
- poor handling of human complacency under automation

### Why it matters

This is one of the strongest cases showing that AI incidents are often organizational failures, not just model failures.

### Alignment lesson

If a firm uses high-autonomy systems, the governance problem includes:

- operator attention design
- safety culture
- escalation logic
- real-world redundancy
- boundaries on when the system should control the task at all

## 4. Workday Algorithmic Hiring Litigation (2024 onward)

**What happened**

In *Mobley v. Workday*, a federal court in the Northern District of California ruled on July 12, 2024 that some discrimination claims against Workday could proceed under an "agent" theory.

The court allowed the case to move forward on the theory that Workday's customers may have delegated traditional hiring functions, including rejecting applicants, to algorithmic decision tools.

### Why this belongs in the general AI category

This is an algorithmic screening and employment-decision case, not an LLM case.

### What went wrong

At this stage, the case is a legal signal rather than a final merits finding.

But the important issue is clear:

- an AI vendor may be treated as participating in employment decision-making
- delegation to software does not automatically erase accountability

### Why it matters

This case matters because it moves the problem from abstract fairness talk to concrete liability structure.

### Alignment lesson

Business-context alignment must account for:

- vendor responsibility
- delegated authority in employment workflows
- disparate impact risk
- legal accountability even when the screening is outsourced

## Interim Reading: What General AI Incidents Have In Common

These general AI incidents tend to cluster around the following failure modes:

- wrong target or wrong objective
- biased history encoded into data
- brittle prediction in real operating conditions
- unsafe scaling of automation
- organizational overconfidence in system outputs
- unclear accountability for automated decisions

In other words, general AI incidents often look like:

**optimization, prediction, safety, and institutional control problems**

## Part II. LLM-Specific Incidents

## 1. Air Canada Chatbot Liability (2024 decision)

**What happened**

In *Moffatt v. Air Canada*, decided February 14, 2024, the British Columbia Civil Resolution Tribunal held Air Canada liable after its website chatbot gave a customer incorrect information about bereavement fares.

The tribunal found negligent misrepresentation and ordered Air Canada to pay damages, pre-judgment interest, and fees.

### Why this belongs in the LLM category

The key failure mechanism was not just automation.

It was a conversational system giving fluent but incorrect policy guidance that a customer reasonably relied on.

### What went wrong

The chatbot told the customer that a bereavement fare adjustment could be requested after travel.

That contradicted Air Canada's actual policy.

Air Canada argued that it was not liable for the chatbot's statements, but the tribunal rejected that argument and treated the chatbot as part of the company's website.

### Why it matters

This is a strong example of **conversational misrepresentation risk**.

### Alignment lesson

When firms deploy LLM-like customer systems, they must assume that:

- users will rely on fluent answers
- policy inconsistency creates legal exposure
- the company remains responsible for the model's outputs in many practical contexts

## 2. Mata v. Avianca Sanctions (2023)

**What happened**

On June 22, 2023, a federal judge in the Southern District of New York sanctioned lawyers in *Mata v. Avianca* after they submitted fake cases generated by ChatGPT.

The court imposed a $5,000 penalty and additional non-monetary sanctions.

### Why this belongs in the LLM category

The failure depended directly on LLM hallucination plus human over-trust.

### What went wrong

The lawyers relied on generated case citations and fake opinions without independently verifying them.

The court described ChatGPT as the source of fabricated cases and highlighted the attorneys' failure to authenticate the authorities they cited.

### Why it matters

This is one of the first globally visible professional-services failures tied directly to LLM hallucination.

### Alignment lesson

Human review is not automatically enough.

LLM use in professional settings requires:

- source verification outside the chat interface
- explicit validation protocols
- clear role limits on what the model is allowed to generate without external checking

## 3. Samsung ChatGPT Data Leak and Ban (2023)

**What happened**

Bloomberg reported on May 2, 2023 that Samsung banned employee use of ChatGPT and other generative AI tools after discovering that staff had uploaded sensitive code to the platform.

### Why this belongs in the LLM category

This is a clear example of prompt-based data leakage tied to the use of public generative AI tools.

### What went wrong

Employees treated ChatGPT as a useful problem-solving assistant and entered confidential internal information into an external system.

The business risk did not arise from a wrong answer.

It arose from the interaction pattern itself.

### Why it matters

This is one of the strongest early corporate examples of **LLM governance failure through convenience-driven use**.

### Alignment lesson

For LLM deployment, alignment is not only about output quality.

It is also about:

- data-boundary discipline
- prompt governance
- internal-use policy
- secure alternatives for employees

## 4. CNET / Red Ventures AI Publishing Failure (2023)

**What happened**

In January and February 2023, reporting by Futurism and others showed that CNET had published AI-assisted or AI-generated finance explainers that contained factual errors and later required many corrections.

The reporting also raised concerns about disclosure quality and plagiarism.

### Why this belongs in the LLM category

The central problem was large-scale generative text production in a business publishing workflow.

### What went wrong

The company appears to have used generative systems to produce publishable editorial content faster, but the resulting output created:

- factual-error risk
- plagiarism risk
- weak disclosure risk
- reputational risk

### Why it matters

This case shows how LLM deployment can fail even when the domain is not obviously high stakes in the same way as medicine or aviation.

Finance-related media content can still create significant trust and reputational harm.

### Alignment lesson

LLM use in publishing requires:

- stronger human review than firms initially assume
- high-quality disclosure
- domain-specific thresholds for automation
- controls against scale-first deployment

## Interim Reading: What LLM Incidents Have In Common

These LLM-specific incidents tend to cluster around different failure modes:

- hallucinated but persuasive outputs
- conversational overreliance
- policy inconsistency presented as authoritative guidance
- leakage of confidential information through prompts
- weak verification inside the same interface
- rapid scaling of low-quality generated content

In other words, LLM incidents often look like:

**fluency, reliance, interface, and generated-content governance problems**

## The Key Difference Between The Two Categories

The most important distinction is this:

- general AI incidents usually begin with **prediction, optimization, classification, or autonomy**
- LLM incidents usually begin with **language generation, dialogue, explanation, or open-ended assistance**

That difference matters because it changes what the governance problem looks like.

### General AI governance questions

- Is the target function appropriate?
- Is the training data biased?
- Is the prediction robust enough for this domain?
- Is the automation level too high?
- Who is accountable for the resulting decision?

### LLM governance questions

- Will people trust the output too much because it sounds coherent?
- How will generated explanations shape human judgment?
- How do we verify claims outside the chat interface?
- What data must never be entered into the system?
- When does a conversational tool become a legally attributable company statement?

## Why This Distinction Matters For Your Research

Your project is moving toward business-context AI alignment.

That means it cannot treat all AI incidents as if they are interchangeable.

The distinction helps in three ways.

### 1. It sharpens the research problem

If you are studying LLM-centered business use, then cases like Air Canada, Samsung, and Mata are more directly useful than cases like Zillow or Amazon recruiting.

### 2. It shows which issues survive model improvement

Better LLMs may reduce hallucination rates.

But they will not automatically eliminate:

- overreliance
- prompt leakage
- legal attribution
- generated-rationale influence
- weak validation processes

### 3. It suggests two related but distinct research lanes

Lane A:

**general AI alignment in business decision systems**

Lane B:

**LLM alignment in business advice, communication, and workflow support**

The second lane may be especially important if your real-world observation is right:

that many people first use AI by asking some version of:

**"What should I do next?"**

That is much more LLM-like than traditional predictive AI.

## Practical Conclusion

If you want a compact conclusion from this note, it is this:

**General AI incidents mainly warn firms about mis-specified objectives, biased data, brittle prediction, and over-automation. LLM incidents mainly warn firms about fluent falsehoods, conversational over-trust, prompt leakage, and generated-content governance.**

Both matter.

But if your research focus keeps moving toward AI as a first-pass business advisor, then the LLM category becomes especially central.

## Source Links

- Zillow investor release, November 2, 2021: https://investors.zillowgroup.com/investors/news-and-events/news/news-details/2021/Zillow-Group-Reports-Third-Quarter-2021-Financial-Results--Shares-Plan-to-Wind-Down-Zillow-Offers-Operations/default.aspx?stream=business
- Zillow SEC filing, November 2, 2021: https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/z-20211102.htm
- Reuters on Amazon recruiting tool, October 10, 2018: https://www.investing.com/news/stock-market-news/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-1637988
- NTSB Uber Tempe investigation page: https://www.ntsb.gov/investigations/Pages/HWY18MH010.aspx
- Northern District of California case page, *Mobley v. Workday*: https://cand.uscourts.gov/cases-e-filing/cases/323-cv-00770-rfl/mobley-v-workday-inc
- Duane Morris summary of July 12, 2024 ruling in *Mobley v. Workday*: https://www.mondaq.com/unitedstates/employee-rights-labour-relations/1493526/california-federal-court-denies-motion-to-dismiss-artificial-intelligence-employment-discrimination-lawsuit
- DWT summary of *Moffatt v. Air Canada*, March 6, 2024: https://www.dww.com/articles/bc-tribunal-finds-air-canada-liable-for-inaccurate-advice-given-by-website-chatbot
- Justia order, *Mata v. Avianca*, June 22, 2023: https://law.justia.com/cases/federal/district-courts/new-york/nysdce/1%3A2022cv01461/575368/54/
- Bloomberg on Samsung ban, May 2, 2023: https://www.bloomberg.com/news/articles/2023-05-02/samsung-bans-chatgpt-and-other-generative-ai-use-by-staff-after-leak
- Futurism on CNET AI article rollout, January 15, 2023: https://futurism.com/the-byte/cnet-publishing-articles-by-ai
- Futurism on CNET corrections and disclosure issues, January 20, 2023: https://futurism.com/cnet-ai-articles-label
- Futurism on CNET errors and plagiarism, February 2, 2023: https://futurism.com/red-ventures-knew-errors-plagiarism-deployed-cnet-anyway
