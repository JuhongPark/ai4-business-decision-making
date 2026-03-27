# Recent External Research Relevant to Business-Context AI Alignment

status: draft
date: 2026-03-21
purpose: Summarize recent external research that is most relevant to the repository's emerging focus on business-context AI alignment.
scope: 2024-2026 primary sources

## Scope Note

This note does not review the whole AI alignment field.

It focuses on recent research most relevant to the following question:

**How should organizations design, govern, and ethically constrain AI-supported business decision systems so that delegation remains calibrated rather than naive, over-trusting, or under-governed?**

The sources below were selected because they speak directly to one or more of these themes:

- human-AI delegation
- trust calibration
- AI interaction expertise
- organizational governance
- accountability and ethics in agentic systems

## Main Directional Takeaways

The strongest recent pattern is that relevant research is moving away from the simple question of whether AI improves work, and toward harder questions about:

1. how work should be divided between humans and AI
2. when human-AI combinations outperform either alone
3. how users calibrate trust under uneven model reliability
4. how organizations assign responsibility for AI governance
5. how agentic systems should be bounded by accountability and ethical norms

This direction is highly compatible with the repository's emerging framing of business-context AI alignment.

## 1. Human-AI Collaboration Is Becoming A Delegation Design Problem

### Vaccaro, Almaatouq, and Malone (2024)

Source:
- Nature Human Behaviour, published October 28, 2024
- https://www.nature.com/articles/s41562-024-02024-1

Key result:
- Across 106 experiments and 370 effect sizes, human-AI combinations performed worse than the best of human alone or AI alone on average.
- Decision tasks were associated with performance losses.
- Creation tasks showed more promise.
- The paper explicitly suggests that better results may require giving AI only the subtasks where it is clearly better.

Why it matters here:
- This is one of the strongest recent empirical supports for the claim that business-context alignment is not mainly a "use AI or do not use AI" problem.
- It is a delegation-design problem.
- It strongly supports the repository's authority-allocation logic and argues against fixed-autonomy deployment.

Repository implication:
- The project should treat **division of labour** as a central alignment variable, not a secondary implementation detail.

### Dell'Acqua et al. (2025)

Source:
- NBER Working Paper 33641, issue date April 2025
- https://www.nber.org/papers/w33641

Key result:
- In a preregistered field experiment with 776 professionals at Procter & Gamble, individuals using AI matched the performance of teams without AI.
- AI also reduced functional silo effects and changed the social dynamics of work.

Why it matters here:
- This moves the discussion beyond productivity.
- AI is not just a faster tool. It can partially substitute for collaboration structure and reshape how expertise is combined.

Repository implication:
- The project should analyze AI delegation not only at the level of individual task performance, but also at the level of **team structure, expertise integration, and social coordination**.

### Ayoubi et al. (2024)

Source:
- ICIS 2024 Proceedings, published December 15, 2024
- https://aisel.aisnet.org/icis2024/aiinbus/aiinbus/2

Key result:
- In a field experiment on early-stage innovation evaluation, AI-assisted screeners were more likely to fail solutions.
- Narrative AI rationales influenced subjective judgments more strongly than black-box AI outputs.
- The study argues that AI interaction expertise is needed, especially where evaluation includes subjective criteria.

Why it matters here:
- This is directly relevant to business decisions involving screening, prioritization, and expert evaluation.
- It shows that AI explanations do not merely inform judgment. They can actively shape and bias subjective assessment.

Repository implication:
- The project should treat **AI rationales** as governance objects, not just usability features.
- Subjective business decisions need stronger guardrails against narrative overreliance.

### Agarwal, Moehring, and Wolitzky (2025)

Source:
- NBER Working Paper 33949, issue date June 2025
- https://www.nber.org/papers/w33949

Key result:
- Humans under-respond to AI predictions and reduce effort when AI is highly confident.
- Overconfidence in one's own signal rather than distrust of AI drives under-response.
- The paper's optimal policy result is selective: automate confident cases, delegate the rest, and disclose the prediction.

Why it matters here:
- This is highly relevant to your focus because it formalizes the design of human-AI collaboration as a policy problem, not just a UX problem.

Repository implication:
- The project should explicitly develop a **selective automation and disclosure logic** rather than treating all recommendation settings as similar.

## 2. Trust Calibration Is Becoming More Explicit And More Central

### Gans (2026)

Source:
- NBER Working Paper 34712, issue date January 2026
- https://www.nber.org/papers/w34712

Key result:
- The paper models "Artificial Jagged Intelligence" as uneven local reliability across nearby tasks.
- A blind user sees only coarse quality signals and may adopt poorly.
- A calibrated user who learns where the system works can still obtain positive value.

Why it matters here:
- This is one of the clearest recent statements of the trust-calibration problem in economic and decision terms.
- It closely matches your intended research emphasis on not just AI quality, but **calibrated reliance**.

Repository implication:
- The project should treat **local reliability mapping** and **where the model works** as first-class research concepts.
- "Miscalibrated delegation" can be grounded in this jaggedness logic.

### Lane et al. plus Vaccaro et al. together

Inference from sources:
- The Lane study shows that rationales can increase adherence in subjective evaluation.
- The Vaccaro meta-analysis shows that decision tasks are where human-AI combinations most often fail.

Combined implication:
- The business problem is not only whether people trust AI too much or too little.
- It is whether they trust the AI in the right places, under the right task structure, and for the right reasons.

This is very close to the core idea of business-context AI alignment.

## 3. Governance Research Is Becoming More Organizationally Concrete

### Engel and Duske (2025)

Source:
- AMCIS 2025 Proceedings, published August 15, 2025
- https://aisel.aisnet.org/amcis2025/is_leader/is_leader/1

Key result:
- Based on interviews with nine AI governance leaders, the paper develops a RACI matrix for AI governance activities.
- It argues that effective governance requires centralized accountability at the C-level plus decentralized responsibility through specialized roles.

Why it matters here:
- This is concrete evidence that governance research is moving from principles toward operating models and role assignment.

Repository implication:
- Your governance work is directionally well aligned with the literature.
- It would benefit from making role allocation even more explicit in business terms.

### Meimandi et al. (2025)

Source:
- arXiv:2510.03368, submitted October 3, 2025
- https://arxiv.org/abs/2510.03368

Key result:
- The paper studies RAI governance in decentralized organizations and proposes the ARGO framework.
- Its core finding is that organizations need a balance between shared foundation standards, central advisory resources, and local implementation.

Why it matters here:
- This is especially relevant for large enterprises with distributed business units and uneven local contexts.
- It connects directly to your interest in practical business governance rather than purely abstract principles.

Repository implication:
- The project should treat **decentralized implementation** as a central governance problem, not an edge case.
- This is especially important if the research is meant to speak to real firms rather than only idealized organizations.

### Kolt (2025)

Source:
- arXiv:2501.07913, revised February 11, 2025
- https://arxiv.org/abs/2501.07913

Key result:
- The paper analyzes AI agents using principal-agent theory and agency law.
- It identifies information asymmetry, discretionary authority, and loyalty as core governance problems.
- It argues that standard monitoring and enforcement tools may be insufficient when AI systems are opaque and fast.

Why it matters here:
- This is a strong bridge between technical agency and organizational governance.
- It gives a more formal vocabulary for the kind of alignment problem you are interested in.

Repository implication:
- The project should explicitly connect AI delegation to **principal-agent problems**, not only to generic governance language.

## 4. Recent Research Is Expanding Alignment Into Relational And Ethical Questions

### Gabriel et al. (2024)

Source:
- arXiv:2404.16244, revised April 28, 2024
- https://arxiv.org/abs/2404.16244

Key result:
- The paper frames advanced AI assistants as systems that act on behalf of users across domains.
- It treats trust, privacy, manipulation, anthropomorphism, appropriate relationships, cooperation, and societal impact as part of the evaluation problem.

Why it matters here:
- This is important for your project because it shows how "alignment" expands once assistants become more agentic and embedded in real decision contexts.

Repository implication:
- Ethics should not replace the business-delegation focus, but it should remain a contextual layer covering **manipulation, appropriate influence, privacy, and legitimacy**.

### Lange, Keeling, Manzini, and McCroskery (2025)

Source:
- npj Artificial Intelligence, published November 5, 2025
- https://www.nature.com/articles/s44387-025-00041-7

Key result:
- The paper argues that accountability mechanisms are needed in human-AI agent relationships to ensure alignment with user and societal interests.
- It proposes conditional engagement strategies: distancing, disengaging, and discouraging.

Why it matters here:
- This adds an ethical and relational dimension to alignment that is directly relevant once business systems become agentic, conversational, and persistent.
- It also fits your view that ethics matters, but as a supporting logic rather than the whole project.

Repository implication:
- The project should incorporate an **ethics-context layer** that explains when AI systems should push back, refuse, or impose friction rather than optimizing only for assistance and compliance.

## 5. Human Capability Research Is Also Shifting Toward AI-Orchestration Skills

### Weidmann, Xu, and Deming (2025)

Source:
- NBER Working Paper 33662, issue date April 2025
- https://www.nber.org/papers/w33662

Key result:
- Leadership skill with AI agents strongly predicted leadership skill with human groups.
- Successful leaders with AI agents asked more questions and engaged in more conversational turn-taking.

Why it matters here:
- This suggests that future managerial capability may include AI orchestration as a real leadership skill, not just tool use.

Repository implication:
- The project can connect calibrated delegation not only to system design, but also to **managerial capability development**.

## Overall Assessment For This Repository

The recent external literature strongly supports the following shift:

from:

- "Should firms adopt AI in decision-making?"

to:

- "How should firms design delegation, trust, governance, and ethical boundaries so that AI-supported decision systems remain aligned with organizational goals and real-world constraints?"

This means the repository is already on a productive path.

Its strongest existing overlap with recent literature is:

- authority allocation
- fallback and escalation
- governance architecture
- domain-sensitive restriction logic

Its clearest current gaps, relative to the recent literature, are:

1. explicit trust-calibration theory
2. miscalibrated delegation as a named failure mode
3. governance of AI rationales in subjective evaluations
4. decentralized enterprise governance design
5. ethical accountability mechanisms for agent-like systems

## Recommended Research Upgrades

If the project is explicitly repositioned as business-context AI alignment, the most useful next additions would be:

1. a trust-calibration memo centered on jagged reliability and calibrated reliance
2. a miscalibrated-delegation memo linking over-trust, under-trust, and local reliability
3. a business-decision memo on subjective evaluation, AI rationales, and narrative overreach
4. a governance-design memo for decentralized firms
5. an ethics-context memo focused on manipulation, legitimacy, and conditional engagement

## Bottom Line

The recent literature is moving toward the exact area that this repository can plausibly own:

**business-context AI alignment as the design of calibrated delegation, trustworthy collaboration, bounded risk, operational governance, and ethically legitimate human-AI decision systems.**
