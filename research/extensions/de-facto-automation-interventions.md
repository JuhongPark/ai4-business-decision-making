# Evidence-Backed Interventions Against De Facto Automation

date: 2026-04-11
status: literature review (verified academic sources)
purpose: Map empirical evidence on interventions that prevent humans from rubber-stamping AI output

---

## Framing: The Problem of De Facto Automation

De facto automation occurs when humans nominally oversee AI but in practice accept AI output without meaningful evaluation. Parasuraman and Manzey (2010, Human Factors) provide the foundational framework: automation complacency and automation bias are overlapping phenomena where attention is the central mechanism. Their integrated model shows these effects occur in both naive and expert users, cannot be prevented by simple training or instructions, and affect individuals and teams alike.

Goddard, Roudsari, and Wyatt (2012, JAMIA) conducted the first systematic review of automation bias frequency and mitigators across healthcare. They found that the rate of "negative consultation" -- where a correct human decision is changed to an incorrect one based on incorrect automated advice -- ranged from 6% to 11% in healthcare studies. This establishes that automation bias is not merely attitudinal but produces measurable decision errors.

The Microsoft Aether group's literature review (2022, ~60 papers) concluded that many proposed mitigations can backfire, sometimes increasing overreliance rather than reducing it. This sets a cautionary frame for the intervention categories below.

---

## 1. Friction Design / Cognitive Forcing

### Bucinca, Malaya, and Gajos (2021) -- The Landmark Study

- **Venue**: CSCW 2021 (Proceedings of the ACM on Human-Computer Interaction, Vol. 5, No. CSCW1)
- **Sample**: N=199 (between-subjects, 6 conditions)
- **Task**: Nutritional assessment (identifying carbohydrate sources in meals)
- **Interventions**: Three cognitive forcing functions (CFFs) compared to two simple explainable AI (SXAI) conditions and a no-AI baseline. The three CFFs were:
  1. Requiring users to formulate their own answer before seeing the AI recommendation
  2. Making AI recommendations available only on demand (user must actively request)
  3. Introducing a deliberate delay before showing AI output
- **Key finding**: CFFs significantly reduced overreliance compared to SXAI conditions. Performance on incorrect AI suggestions: SXAI 0.03 vs. CFF 0.09 (F(1,207.6)=8.95, p=.003), indicating users in CFF conditions were three times better at detecting AI errors.
- **Critical caveat**: Users rated the most effective interventions least favorably. There is a direct tension between intervention effectiveness and user satisfaction.
- **Moderator**: Need for Cognition (NFC) moderated effectiveness. Participants higher in NFC benefited more from CFFs. This suggests cognitive forcing may widen performance gaps between analytically inclined and non-analytically inclined users.
- **Verdict**: Behavioral change confirmed. Reduced overreliance, not just attitude change.

### Fogliato, Chappidi, Lungren et al. (2022) -- Decision Order in Radiology

- **Venue**: FAccT 2022 (ACM Conference on Fairness, Accountability, and Transparency)
- **Sample**: N=19 veterinary radiologists (experts, not crowdworkers)
- **Task**: Clinical imaging (chest X-ray interpretation)
- **Intervention**: Two-step workflow requiring radiologists to register a provisional decision before seeing AI inferences, compared to a one-step workflow where AI output was shown alongside images.
- **Key finding**: Participants who committed to decisions before seeing AI were less likely to agree with the AI regardless of whether the advice was accurate. When they disagreed with AI, they were more likely to seek a colleague's second opinion.
- **Limitation**: Small expert sample (N=19). Participants in the pre-decision group also perceived AI as less useful, raising adoption concerns.
- **Verdict**: Behavioral change confirmed in expert population. "Decide first, then see AI" reduces anchoring.

### Rastogi, Zhang et al. (2022) -- Time Pressure and Anchoring

- **Venue**: CSCW 2022 (Proceedings of the ACM on Human-Computer Interaction)
- **Sample**: Experiment 1: N=47; Experiment 2: N=479
- **Task**: AI-assisted decision-making under time constraints
- **Intervention**: Time-based de-anchoring strategy. Allocated more time when AI confidence was low and model was likely incorrect.
- **Key finding**: Time allocation strategy with explanation effectively de-anchored humans and improved collaborative performance when the AI had low confidence and was incorrect.
- **Verdict**: Behavioral change confirmed. Time-based friction can selectively reduce anchoring in low-confidence situations.

### de Jong, Paananen, Tag, and van Berkel (2025) -- Partial Explanations

- **Venue**: CSCW 2025 (Proceedings of the ACM on Human-Computer Interaction, Vol. 9, No. 2)
- **Sample**: N=264 (after attention check exclusions)
- **Task**: Shortest path identification in weighted graphs
- **Intervention**: Partial explanations -- showing incomplete explanations that force users to complete the reasoning themselves, rather than full AI explanations.
- **Key finding**: Partial explanations reduced overreliance. However, effectiveness varied across task difficulty levels, indicating that designers must calibrate the level of explanation incompleteness to task complexity.
- **Verdict**: Behavioral change confirmed. Partial information forces engagement.

### Ashktorab et al. (2025) -- CFFs and Hallucinations

- **Venue**: arXiv (IBM Research)
- **Sample**: N=34 (272 total tasks)
- **Task**: Content-grounded data generation
- **Intervention**: Cognitive forcing function (formulate answer first) applied to LLM-assisted content tasks with and without hallucinations.
- **Key finding**: CFFs did not mitigate hallucination effects on data quality. Users exhibited novel overreliance patterns including appending hallucinated AI text to their own correct answers. In the Formulate condition without CFF, participants relied more on AI, suggesting cognitive offloading.
- **Verdict**: Mixed. CFFs have limits -- they may not help when AI output is plausible but fabricated. This is a critical boundary condition for LLM deployment.

---

## 2. Confidence / Uncertainty Displays

### Zhang, Liao, and Bellamy (2020) -- Confidence Calibrates Trust but Not Accuracy

- **Venue**: FAccT 2020 (ACM Conference on Fairness, Accountability, and Transparency)
- **Sample**: 2x2x2 design, 9 participants per condition (~72 total)
- **Task**: Income prediction (AI-assisted classification)
- **Intervention**: Showing AI confidence scores and/or local explanations alongside predictions.
- **Key finding**: "Confidence score can help calibrate people's trust in an AI model, but trust calibration alone is not sufficient to improve AI-assisted decision making." Trust calibration and decision quality are separate phenomena. Confidence displays change how much people trust the AI, but this does not reliably translate into better decisions.
- **Limitation**: Small sample per condition. The finding that trust calibration does not equal performance improvement is the crucial takeaway.
- **Verdict**: Attitude change confirmed (trust calibration). Behavioral change insufficient on its own.

### Okamura and Yamada (2020) -- Adaptive Trust Calibration Cues

- **Venue**: PLOS ONE
- **Sample**: N=116
- **Task**: Drone-based pothole inspection (simulated)
- **Intervention**: Adaptive trust calibration cues presented when user behavior suggested inappropriate reliance. Four types of cues were tested. Importantly, the cues were adaptive (triggered by detected behavior) rather than continuous.
- **Key finding**: Adaptively presenting trust calibration cues strongly affected whether participants changed their reliance behavior. Continuously presenting reliability information did not help. Participants increased manual choices after seeing cues.
- **Verdict**: Behavioral change confirmed, but only when cues are adaptive (context-triggered), not continuous. Static displays habituate.

### Dratsch et al. (2023) -- Mammography Automation Bias Across Expertise

- **Venue**: Radiology (RSNA)
- **Sample**: N=27 radiologists (varying experience levels)
- **Task**: Mammography reading with AI-suggested BI-RADS categories
- **Design**: 50 mammograms, 12 with deliberately incorrect AI suggestions
- **Key finding**: All experience levels showed automation bias. Correct rating accuracy collapsed when AI was wrong: inexperienced (79.7% vs. 19.8%, p<.001), moderately experienced (81.3% vs. 24.8%, p<.001), very experienced (82.3% vs. 45.5%, p=.003). Inexperienced radiologists showed significantly higher bias (degree of bias 4.0 vs. 1.2 for very experienced, p=.009).
- **Implication for confidence displays**: Even expert users with domain knowledge and presumably better ability to assess AI confidence still succumbed to automation bias. Experience moderated but did not eliminate the effect.
- **Verdict**: Expertise provides partial protection but is insufficient. Supports need for structural interventions beyond individual capacity.

---

## 3. Adversarial / Counterfactual Prompting and Second Opinions

### Bansal, Wu et al. (2021) -- Explanations Don't Improve Complementarity

- **Venue**: CHI 2021
- **Sample**: Multiple experiments (specific N varies by dataset)
- **Task**: Multiple classification tasks where AI and human had comparable accuracy
- **Intervention**: AI explanations vs. confidence scores alone
- **Key finding**: "Explanations increased the chance that humans will accept the AI's recommendation, regardless of its correctness." Explanations did not improve complementary performance over simply showing confidence scores. The study achieved complementary performance (team > individuals) across conditions, but explanations added no additional benefit.
- **Verdict**: Explanations increased agreement, not appropriate reliance. This is a critical negative finding for XAI approaches.

### Vasconcelos et al. (2023) -- Explanations Can Help, But Only Under Specific Conditions

- **Venue**: CSCW 2023 (Stanford)
- **Sample**: N=731 across 5 studies
- **Task**: Various decision tasks at different difficulty levels
- **Key finding**: Overreliance does not reduce when AI produces explanations for easy tasks. However, explanations reduce overreliance specifically when tasks are hard for humans. People strategically choose whether to engage with explanations based on a cost-benefit analysis. Studies 1-4 showed that task difficulty, explanation difficulty, and monetary compensation all affect engagement. Study 5 used the Cognitive Effort Discounting paradigm to quantify explanation utility.
- **Verdict**: Conditional behavioral change. Explanations help only when humans have enough difficulty to motivate engagement with them.

### Lu, Wang, and Yin (2024) -- Second Opinions as Counter-Arguments

- **Venue**: CSCW 2024 (Proceedings of the ACM on Human-Computer Interaction)
- **Sample**: Three pre-registered, randomized experiments
- **Intervention**: Providing second opinions (from peers or from another AI model) alongside the primary AI recommendation.
- **Key finding**: When second opinions were always shown together with AI recommendations, decision-makers reduced over-reliance but simultaneously increased under-reliance, regardless of whether the second opinion came from a peer or another AI. When decision-makers could choose when to solicit a peer opinion, active solicitation mitigated over-reliance without inducing under-reliance.
- **Verdict**: Forced counter-arguments create a different problem (under-reliance). User-controlled access to alternative views is more promising.

### Nourani et al. (2021) -- First Impressions and Anchoring

- **Venue**: IUI 2021 (International Conference on Intelligent User Interfaces)
- **Task**: XAI-assisted decision-making with varied initial exposure
- **Key finding**: Users who saw AI perform well early formed positive anchors, built better mental models of AI capabilities, but also made more errors from over-reliance. Users with early negative impressions made fewer errors (relied more on themselves) but formed inaccurate mental models that underestimated AI capabilities. First impressions created persistent anchoring effects that shaped reliance throughout the task.
- **Implication for counterfactual prompting**: Deliberately exposing users to AI failures early could reduce overreliance, but at the cost of systematic under-utilization of AI capabilities.

---

## 4. Accountability Mechanisms

### Gaube et al. (2021) -- Expertise as Implicit Accountability

- **Venue**: npj Digital Medicine
- **Sample**: Physicians (radiologists and non-specialists)
- **Task**: Chest X-ray diagnosis with advice labeled as from "AI" or "experienced radiologist"
- **Key finding**: Expert radiologists (task specialists) significantly downrated advice labeled as from AI, applying domain-specific quality judgment. Non-expert physicians showed no significant difference based on source attribution. Diagnostic accuracy was significantly worse for all participants when they received inaccurate advice, regardless of source.
- **Implication for accountability**: Domain expertise functions as a form of implicit accountability -- experts feel responsible for accurate diagnosis and therefore evaluate AI advice more critically. Non-experts lack the domain knowledge to exercise meaningful oversight even if they feel accountable.
- **Verdict**: Accountability without expertise is empty. Formal sign-off cannot substitute for substantive evaluation capacity.

### Green and Chen (2019) -- Disparate Interactions

- **Venue**: FAT* 2019 (ACM Conference on Fairness, Accountability, and Transparency)
- **Sample**: N=2,140 (Amazon Mechanical Turk)
- **Task**: Predicting recidivism risk for defendants (simulated judicial decision)
- **Key finding**: Participants adhered to algorithmic advice to a greater degree when it predicted high risk for a Black defendant or low risk for a white defendant. AI advice amplified pre-existing biases in the decision-making process. The human-AI team did not outperform AI alone because humans followed incorrect AI advice or ignored correct AI advice in biased patterns.
- **Implication for accountability**: Formal human oversight of algorithmic recommendations can reproduce and amplify rather than correct bias. Accountability mechanisms must account for the possibility that human overseers bring their own systematic errors.

### Structural Evidence Gap

No controlled experiments were found that directly test whether requiring formal documentation or sign-off for AI-assisted decisions reduces automation bias compared to identical settings without such requirements. The accountability literature in AI-assisted decision-making is largely prescriptive (frameworks, ethical guidelines, governance proposals) rather than experimental. This is a significant gap: the most commonly proposed organizational intervention (formal sign-off) lacks direct experimental evidence of effectiveness.

---

## 5. Selective Automation / Task Decomposition

### He, Hemmer, Vossing, Schemmer, and Gadiraju (2025) -- Multi-Step Transparent Workflows

- **Venue**: arXiv (under review)
- **Sample**: N=233
- **Task**: Composite fact-checking (multi-step verification)
- **Intervention**: Multi-Step Transparent (MST) decision workflow that decomposes complex tasks into intermediate steps with visible reasoning, compared to single-step AI assistance.
- **Key finding**: MST workflows outperformed single-step collaboration when AI advice was misleading. Effectiveness was contingent on users actually engaging with intermediate steps -- those who demonstrated "relatively high consideration" of the steps benefited most.
- **Critical insight**: "There is no one-size-fits-all decision workflow." Task decomposition helps, but only when users treat the sub-steps as genuine evaluation points rather than additional items to rubber-stamp.
- **Verdict**: Conditional behavioral change. Decomposition creates opportunity for engagement but does not guarantee it.

### Partial Automation During Training -- Wilinghoefer et al. (2024)

- **Venue**: International Journal of Human-Computer Interaction
- **Task**: Worker training with fully vs. partially automated AI
- **Key finding**: Participants trained with fully automated AI had significantly worse error-detection performance compared to those trained with partial or no automation. Full automation during training hindered skill acquisition. Partial automation enhanced motivation, engagement, and skill development, enabling participants to better adapt when AI failed.
- **Verdict**: How you introduce automation shapes long-term capacity for oversight. Full automation from the start degrades the very skills needed for meaningful oversight.

---

## 6. Training Interventions

### Chiang and Yin (2022) -- ML Literacy Interventions

- **Venue**: IUI 2022 (International Conference on Intelligent User Interfaces)
- **Task**: AI-assisted decision-making tasks
- **Intervention**: Interactive vs. non-interactive tutorial about the specific ML model. Tutorials addressed model strengths, limitations, and expected behavior.
- **Key finding**: For individuals with relatively high ability in solving tasks themselves, interactive tutorials tailored to the specific model reduced over-reliance when they could outperform the model. Low-performing individuals' reliance was not affected by tutorial type.
- **Verdict**: Training helps capable users. It does not help users who lack the domain skills to evaluate AI output independently. Training addresses knowledge gaps but cannot create evaluation capacity from nothing.

### Parasuraman and Manzey (2010) -- Training Cannot Overcome Bias

- **Venue**: Human Factors (review article)
- **Key finding from literature synthesis**: "Automation bias occurs in both naive and expert participants, cannot be prevented by training or instructions, and can affect decision-making in individuals as well as in teams."
- **Implication**: Simple awareness training about automation bias does not inoculate against it. This is consistent with decades of research in cognitive bias more broadly showing that knowing about a bias does not reliably prevent it.

### Poursabzi-Sangdeh et al. (2021) -- Transparency Does Not Equal Appropriate Reliance

- **Venue**: CHI 2021
- **Sample**: N=3,800 (pre-registered experiments)
- **Task**: Prediction tasks with models of varying transparency (number of features, black-box vs. clear models)
- **Key finding**: Participants viewing transparent models with fewer features could better simulate predictions, but transparency made them LESS able to detect and correct the model's substantial mistakes, "seemingly due to information overload." Increased interpretability did not cause participants to follow the model's predictions more closely when doing so would have been beneficial.
- **Verdict**: Making the system more transparent or training people to understand it better does not translate to appropriate reliance. This is one of the most important negative findings in the field.

---

## Cross-Cutting Synthesis

### What Actually Works (Evidence of Behavioral Change)

| Intervention | Studies | Reduces Overreliance? | Key Condition |
|---|---|---|---|
| Formulate-own-answer-first | Bucinca 2021, Fogliato 2022 | Yes | Users must genuinely commit to initial judgment |
| On-demand AI (user requests advice) | Bucinca 2021 | Yes | Users must bear the cost of seeking AI help |
| Deliberate delay before AI output | Bucinca 2021, Rastogi 2022 | Yes | Time pressure eliminates the benefit |
| Partial explanations | de Jong 2025 | Yes | Must be calibrated to task difficulty |
| Adaptive (not static) confidence cues | Okamura 2020 | Yes | Must be triggered by detected behavior |
| User-controlled second opinions | Lu 2024 | Partially | User must choose to seek; forced display backfires |
| Task decomposition with visible steps | He 2025 | Conditionally | Users must engage with each step |
| Interactive, model-specific training | Chiang 2022 | For high-ability users only | Requires pre-existing domain competence |
| Partial automation during training | Wilinghoefer 2024 | Indirectly | Builds skills needed for oversight |

### What Does NOT Work (or Backfires)

| Intervention | Evidence | Why It Fails |
|---|---|---|
| Adding explanations to AI output | Bansal 2021, Bucinca 2020 | Increases agreement regardless of correctness |
| Static confidence displays | Zhang 2020, Okamura 2020 | Calibrates trust but not decisions; users habituate |
| Making models more transparent | Poursabzi-Sangdeh 2021 (N=3800) | Information overload; REDUCES error detection |
| General awareness training about AI limitations | Parasuraman 2010 | Cannot overcome attentional mechanisms of bias |
| Forced second opinions | Lu 2024 | Reduces overreliance but creates under-reliance |
| Fully automated AI during training | Wilinghoefer 2024 | Degrades skills needed for oversight |

### Key Moderators

1. **Need for Cognition**: Cognitive forcing interventions benefit analytically motivated individuals more (Bucinca 2021). Risk of intervention-generated inequality.
2. **Domain Expertise**: Experts are better (but not immune) at resisting automation bias (Gaube 2021, Dratsch 2023). Non-experts cannot exercise meaningful oversight.
3. **Task Difficulty**: Explanations help with hard tasks, not easy ones (Vasconcelos 2023). Most workplace decisions are perceived as routine (easy), which is exactly where overreliance is worst.
4. **First Impressions**: Early exposure to AI performance anchors reliance patterns throughout use (Nourani 2021). Onboarding design matters.

### The Fundamental Tension

The interventions that most effectively reduce overreliance (cognitive forcing, delays, on-demand access) are also the ones users rate least favorably (Bucinca 2021). Organizations face a direct tradeoff: interventions that feel burdensome to users are the ones that work. Frictionless AI assistance and meaningful human oversight are structurally in tension.

---

## Measurement Framework: Schemmer et al. (2023)

Schemmer, Hemmer, Nitsche, Kuhl, and Vossing (IUI 2023, N=200) proposed the Appropriateness of Reliance (AoR) framework with two metrics:
- **RAIR (Relative positive AI Reliance)**: How often humans update their own incorrect decisions based on accurate AI advice. Low RAIR = under-reliance.
- **RSR (Relative positive Self-Reliance)**: How often humans reject incorrect AI suggestions and rely on their own accurate judgment. Low RSR = over-reliance (automation bias).

This two-dimensional measurement is important because many interventions that reduce overreliance (raise RSR) simultaneously reduce beneficial reliance (lower RAIR). An intervention that simply makes people ignore AI achieves high RSR but low RAIR -- effectively defeating the purpose of AI assistance.

---

## Gaps in the Literature

1. **Accountability experiments**: No controlled studies directly testing whether formal documentation requirements, audit trails, or sign-off procedures reduce automation bias. The most commonly prescribed organizational intervention lacks experimental evidence.
2. **Longitudinal effects**: Nearly all studies are single-session. Whether cognitive forcing functions remain effective over weeks or months of use is unknown. Habituation is a serious concern.
3. **LLM-specific interventions**: Most studies use classification tasks with clear ground truth. Few address the problem of overreliance on LLM-generated text or reasoning where ground truth is ambiguous.
4. **Organizational context**: Studies use crowdworkers or isolated experts. How team dynamics, time pressure, incentive structures, and organizational culture interact with interventions is unstudied.
5. **Combined interventions**: Studies test single interventions. Whether combining interventions (e.g., cognitive forcing + confidence display + accountability) produces additive or interactive effects is unknown.
6. **Cost-effectiveness**: No studies assess the productivity cost of friction interventions against the error-reduction benefit in realistic settings.

---

## Key References (Alphabetical)

- Ashktorab et al. (2025). Emerging reliance behaviors in human-AI content grounded data generation. arXiv:2409.08937.
- Bansal, Wu et al. (2021). Does the whole exceed its parts? CHI 2021.
- Bucinca, Malaya, Gajos (2021). To trust or to think. CSCW 2021 (PACM HCI 5, CSCW1).
- Bucinca, Lin, Gajos, Glassman (2020). Proxy tasks and subjective measures can be misleading. IUI 2020.
- Chiang and Yin (2022). Exploring the effects of ML literacy interventions. IUI 2022.
- de Jong, Paananen, Tag, van Berkel (2025). Cognitive forcing through partial explanations. CSCW 2025.
- Dratsch et al. (2023). Automation bias in mammography. Radiology.
- Fogliato, Chappidi, Lungren et al. (2022). Who goes first? FAccT 2022.
- Gaube et al. (2021). Do as AI say. npj Digital Medicine.
- Goddard, Roudsari, Wyatt (2012). Automation bias: systematic review. JAMIA 19(1).
- Green and Chen (2019). Disparate interactions. FAT* 2019.
- He, Hemmer, Vossing, Schemmer, Gadiraju (2025). Fine-grained appropriate reliance. arXiv:2501.10909.
- Lai, Chen, Liao, Smith-Renner, Tan (2021). Towards a science of human-AI decision making. arXiv:2112.11471.
- Lu, Wang, Yin (2024). Does more advice help? CSCW 2024.
- Microsoft Aether (2022). Overreliance on AI: literature review.
- Nourani et al. (2021). Anchoring bias affects mental model formation. IUI 2021.
- Okamura and Yamada (2020). Adaptive trust calibration. PLOS ONE.
- Parasuraman and Manzey (2010). Complacency and bias. Human Factors 52(3).
- Poursabzi-Sangdeh et al. (2021). Manipulating and measuring model interpretability. CHI 2021.
- Rastogi, Zhang et al. (2022). Deciding fast and slow. CSCW 2022.
- Schemmer et al. (2023). Appropriate reliance on AI advice. IUI 2023.
- Vasconcelos et al. (2023). Explanations can reduce overreliance. CSCW 2023.
