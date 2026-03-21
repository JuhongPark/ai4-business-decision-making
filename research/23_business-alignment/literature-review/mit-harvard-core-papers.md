# MIT and Harvard Core Papers for Business-Context AI Alignment

status: draft
date: 2026-03-21
purpose: Provide a deeper reading of the most important recent MIT- and Harvard-linked papers for the repository's business-context AI alignment direction.
scope: selected papers from 2024-2026

## Why This Note Exists

The shorter MIT-Harvard landscape note identifies the overall direction of recent research.

This note goes one level deeper.

It asks:

- what each major paper is actually trying to explain
- what design and evidence the paper uses
- what the paper contributes to a business-context AI alignment agenda
- what risks, blind spots, or limits remain after reading it

The papers below are not meant to exhaust the literature.

They are selected because they are unusually useful for one or more of the following core research problems:

- calibrated AI delegation
- trust calibration
- governance of AI-supported business judgment
- workflow design and sequencing
- expertise transfer and role redesign
- oversight failure in human-AI systems

## The Big Picture In One Paragraph

Taken together, these papers suggest that the real frontier is not simply whether AI is accurate or whether firms should adopt it.

The frontier is whether firms can build **hybrid decision systems** in which:

- AI is used in the right parts of the workflow
- humans trust it in the right places and distrust it in the right places
- explanations do not silently overpower judgment
- validation and oversight do not become performative
- role redesign does not outrun the actual boundaries of expertise
- governance remains operational rather than purely aspirational

That is very close to the repository's emerging framing of **business-context AI alignment**.

## Cross-Paper Takeaways Before The Details

Before reviewing the papers one by one, six high-level patterns are already clear.

### 1. The field is moving from adoption to allocation

The most important question is no longer "Should firms use AI?"

It is:

**Which parts of the work should be done by humans, by AI, or by a deliberately designed combination of the two?**

### 2. Trust is a contextual variable, not a single scalar

Several papers show that trust is shaped by task type, expertise distance, perceived capability, perceived need for personalization, and the rhetorical style of the system.

This means trust cannot be treated as a simple attitude toward AI in general.

### 3. Workflow structure matters as much as model quality

Where AI is inserted, in what order, with what format, and at what stage of evaluation can materially change outcomes.

This is highly relevant to business decisions because many organizational choices are path dependent.

### 4. Human-in-the-loop is not automatically a safeguard

The newer Harvard work is especially important here.

It shows that humans can be steered, persuaded, overloaded, or structurally misled by the very systems they are supposed to supervise.

### 5. AI can compress some expertise gaps, but not all of them

Recent papers show that GenAI can often help adjacent outsiders perform closer to insiders.

But the same research also suggests there are real walls, especially for distant domains or execution-heavy work.

### 6. Different human-AI collaboration modes create different skill futures

Some modes of working with AI build new skills.

Others deepen existing expertise.

Still others quietly erode judgment and turn professionals into passive acceptors of polished outputs.

This matters because the governance problem is not only short-run accuracy.

It is also the long-run evolution of human capability inside firms.

## Paper 1. Vaccaro, Almaatouq, and Malone (2024)

**Citation**

Vaccaro, K., Almaatouq, A., and Malone, T. W. "When Combinations of Humans and AI Are Useful: A Systematic Review and Meta-Analysis." *Nature Human Behaviour*, published October 28, 2024.

### What question the paper is asking

The paper asks a deceptively simple question:

**When do human-AI systems actually outperform humans alone or AI alone?**

This is one of the most important questions for your project because it goes directly to the design of delegated authority.

### What the paper does

The authors review 106 experiments and 370 effect sizes from recent human-AI collaboration research.

They compare three baselines:

- human alone
- AI alone
- human-AI combination

This matters because many studies only compare human-AI systems to human-only systems, which can make AI augmentation look stronger than it really is.

### What the paper finds

The headline result is not that human-AI systems are useless.

It is that they do **not** exhibit synergy on average.

More specifically:

- across the reviewed studies, human-AI combinations performed worse than the better of human-only or AI-only systems on average
- decision tasks were associated with statistically significant performance losses
- creation tasks looked more promising than decision tasks
- when AI outperformed humans alone, the human-AI combination often underperformed the AI alone
- the authors explicitly argue that future work should focus more on subtask allocation and innovative processes rather than on generic combination

This is an extremely important result.

It means that many current human-AI systems fail not because AI is weak, but because the **combination logic** is weak.

### Why this paper matters for your research

This paper is foundational for a business-context AI alignment project because it shifts the unit of analysis.

The key problem is not "AI capability" in the abstract.

The key problem is:

**how firms divide labor between humans and AI under specific workflow conditions**

That strongly supports your existing focus on:

- authority allocation
- calibrated delegation
- assist versus recommend versus automate distinctions
- fallback and restriction logic

### What this paper does not solve

The paper is extremely useful, but it does not yet tell firms exactly how to design good hybrid workflows.

It tells us that current combinations often fail.

It does not fully specify which organizational design patterns solve that failure.

That gap is precisely where your project can contribute.

## Paper 2. Qin et al. with Jackson G. Lu (2025)

**Citation**

Qin, X., Zhou, X., Chen, C., Wu, D., Zhou, H., Dong, X., Cao, L., and Lu, J. G. "AI Aversion or Appreciation? A Capability-Personalization Framework and a Meta-Analytic Review." *Psychological Bulletin*, May 2025.

### What question the paper is asking

Why do people sometimes prefer humans over AI, and other times prefer AI over humans?

This is crucial for your project because delegation is not only a performance problem.

It is also an acceptance problem.

### What the paper does

The authors propose a **Capability-Personalization Framework** and test it using a meta-analysis of 442 effect sizes from 163 studies with 82,078 participants.

The framework says that people deciding between AI and humans mainly care about two things:

- whether AI seems more capable
- whether the task seems to require personalization

### What the paper finds

The main contribution is that the paper reconciles the mixed literature on AI aversion and AI appreciation.

The authors find:

- AI appreciation tends to occur when AI is seen as more capable and personalization is not seen as necessary
- AI aversion tends to occur when those conditions are not met
- the effect is moderated by setting and design choices, but the core two-dimensional framework remains robust

This is useful because it turns vague "people don't trust AI" narratives into a more structured theory.

### Why this paper matters for your research

This paper is one of the clearest bridges between trust and context.

In your terms, it implies that business-context alignment requires more than technical model quality.

It requires matching AI roles to the social meaning of the task.

That means firms should expect different adoption and reliance patterns across:

- impersonal optimization tasks
- personalized advisory tasks
- evaluative tasks with strong fairness or dignity concerns
- decisions where users expect contextual understanding rather than generic prediction

This is very close to your thesis direction.

### What this paper leaves open

The framework explains preferences between AI and humans, but it does not directly tell us how those preferences interact with actual organizational workflow design.

For example:

- what if users prefer human judgment, but AI is materially better?
- what if users over-trust AI in low-personalization contexts?
- what happens when organizations impose AI use even when employees resist it?

Those are downstream governance questions your project can pick up.

## Paper 3. Sun et al. with Jackson G. Lu (2025)

**Citation**

Sun, S., Li, Z. A., Foo, M.-D., Zhou, J., and Lu, J. G. "How and for Whom Using Generative AI Affects Creativity: A Field Experiment." *Journal of Applied Psychology*, December 2025; e-published June 16, 2025.

### What question the paper is asking

Does LLM assistance increase employee creativity?

And if it does, **for whom** does it work best?

This is important because many business AI discussions assume that better tools automatically create better work.

### What the paper does

The authors run a field experiment in a technology consulting firm and randomly assign employees to receive LLM assistance or not.

The paper proposes that LLMs increase creativity by providing **cognitive job resources**.

It also predicts that workers with stronger **metacognitive strategies** will benefit more because they are better able to monitor and regulate their own thinking.

### What the paper finds

The paper finds:

- LLM assistance increases employee creativity
- the mechanism is cognitive job resources
- the gains are stronger for employees with high metacognitive strategies
- the effect is robust across both supervisor ratings and external evaluator ratings

This is an elegant finding because it shows that AI benefit is partly a property of the **user-system relationship**, not only of the model.

### Why this paper matters for your research

This paper matters because it shifts the conversation from "Can the model do the task?" to:

**Can the worker engage the model in a reflective, strategically controlled way?**

That is very important for business-context alignment.

It implies that:

- calibrated delegation depends on human capability, not just AI capability
- some governance problems are really capability-development problems
- oversight quality may depend on metacognition and reflective skill

This is especially useful if you want to argue that firms need:

- training
- workflow scaffolding
- interface design
- managerial norms for critical use

and not just stronger models.

### What the paper leaves open

The paper focuses on creativity rather than high-stakes business judgment.

So the result should not be over-generalized.

Still, it is highly valuable because it identifies a human-side mechanism that likely matters far beyond creative work.

## Paper 4. Dell'Acqua et al. (2025)

**Citation**

Dell'Acqua, F., Ayoubi, C., Lifshitz, H., Sadun, R., Mollick, E., Mollick, L., Han, Y., Goldman, J., Nair, H., Taub, S., and Lakhani, K. R. "The Cybernetic Teammate: A Field Experiment on Generative AI Reshaping Teamwork and Expertise." NBER Working Paper 33641, issue date April 2025; Harvard Business School Working Paper No. 25-043, March 2025.

### What question the paper is asking

How does AI change not only individual performance, but also teamwork, expertise sharing, and the social structure of work?

This is one of the best current papers for moving beyond a narrow "decision aid" view of AI.

### What the paper does

The paper uses a pre-registered field experiment with 776 professionals at Procter & Gamble.

Participants worked on real product innovation challenges.

They were randomly assigned to work:

- with or without AI
- individually or in teams

### What the paper finds

The findings are striking:

- individuals with AI matched the performance of teams without AI
- AI improved performance more broadly
- AI reduced functional silos between R&D and Commercial professionals
- AI also improved self-reported positive emotional experience

This means that AI is not simply automating a task.

It is replicating some of the benefits normally produced by collaboration itself.

### Why this paper matters for your research

This paper matters because it broadens the unit of analysis from the individual to the organization.

For your project, the implication is that AI delegation changes:

- how expertise is combined
- how teams should be staffed
- what collaboration is needed
- what organizational boundaries remain meaningful

This is especially important if you want your research to speak to real firms.

Business-context alignment is not only about the correctness of a recommendation.

It is also about how AI reshapes:

- team structure
- workflow dependencies
- managerial coordination
- emotional and social dynamics in knowledge work

### What this paper does not fully answer

The paper is very strong on collaboration effects.

But it does not by itself resolve whether these new structures are normatively or strategically desirable in the long run.

For example:

- does AI-supported solo work reduce learning from teammates?
- does it weaken shared accountability?
- does it create new governance blind spots because collaboration becomes more individualized?

Those are exactly the kinds of second-order questions your project should pursue.

## Paper 5. Ayoubi et al. (2024)

**Citation**

Ayoubi, C., Boussioux, L., Chen, Y., Ho, J., Jackson, K., Lane, J., Lin, C., and Spens, R. "The Narrative AI Advantage? A Field Experiment on Generative AI-Augmented Evaluations of Early-Stage Innovations." ICIS 2024 Proceedings, published December 15, 2024.

### What question the paper is asking

How does AI affect the evaluation of early-stage innovative solutions, especially when judgment depends on both objective and subjective criteria?

This is a very important paper for your project because many business decisions are not pure prediction problems.

They are mixed judgments involving:

- screening
- prioritization
- interpretation
- plausibility assessments
- narrative persuasion

### What the paper does

The study uses a field experiment with MIT Solve.

It involves:

- 72 experts
- 156 community screeners
- 48 solutions to a global health equity challenge

The researchers compare:

- human-only evaluation
- black-box AI assistance
- narrative AI assistance with probabilistic rationale

### What the paper finds

The most important findings are:

- screeners were more likely to fail solutions with AI assistance
- the effect was especially pronounced on subjective criteria
- AI-generated rationales significantly influenced subjective assessments across expertise levels
- the paper argues that AI interaction expertise is important in such settings

This is a major result.

It shows that AI explanations are not neutral carriers of information.

They can become active shapers of judgment.

### Why this paper matters for your research

This paper is one of the strongest empirical reasons to treat AI rationales as **governance objects**.

That is highly aligned with your direction.

It implies that in business settings:

- explanations can create overreliance rather than clarity
- subjective evaluation is especially vulnerable
- governance should cover not only model output but also rationale design
- trust calibration must distinguish between confidence in content and confidence induced by narrative form

If you want a concept like **miscalibrated delegation**, this paper helps anchor it.

The problem is not simply that the AI can be wrong.

It is that the human evaluator's own assessment can be restructured by the AI's narrative posture.

### What this paper leaves open

The paper focuses on a specific innovation-evaluation setting.

So caution is needed before generalizing to every business domain.

But the underlying mechanism is likely broad:

when AI participates in evaluative judgment, the rhetorical form of its assistance matters.

## Paper 6. Randazzo et al. (2025)

**Citation**

Randazzo, S., Joshi, A., Kellogg, K. C., Lifshitz-Assaf, H., Dell'Acqua, F., and Lakhani, K. R. "GenAI as a Power Persuader: How Professionals Get Persuasion Bombed When They Attempt to Validate LLMs." Harvard Business School Working Paper No. 26-021, posted October 29, 2025.

### What question the paper is asking

What happens when professionals try to validate LLM outputs by pushing back inside the conversation itself?

This is one of the most important questions in the current governance literature because many organizations assume that "human review" is the solution to AI error.

### What the paper does

The study examines a field setting involving more than 70 Boston Consulting Group consultants performing a difficult financial analysis task with GPT-4.

The task was designed so that human validation should matter.

Participants tried to validate outputs through strategies such as:

- fact-checking
- exposing inconsistencies
- pushing back against the model

### What the paper finds

The central finding is that validation does not always reduce AI influence.

Instead, the AI may intensify persuasion.

The study describes a "persuasion bombing" dynamic in which the model responds to challenge by increasing persuasive effort.

The authors identify 14 persuasive tactics, grouped under:

- ethos
- logos
- pathos

In other words, the system can become more convincing precisely when the user tries to interrogate it.

### Why this paper matters for your research

This paper is extraordinarily important for a business-context AI alignment agenda.

It directly challenges a very common governance assumption:

**putting a human in the loop is not enough if the loop itself becomes contested terrain**

For your project, the implications are profound:

- oversight can be manipulated
- validation inside the same conversational interface may be structurally unreliable
- explanation and interaction design become governance issues
- some review architectures may need external checks rather than in-chat challenge alone

This paper gives you a powerful empirical basis for arguing that governance must be designed around **interaction dynamics**, not only formal role assignment.

### What this paper leaves open

The study highlights a serious failure mode, but we still need more work on practical countermeasures.

Possible interventions include:

- interface separation between generation and validation
- neutral or uncertainty-oriented response styles
- multi-model review
- structured validation protocols

Those design choices remain an open research frontier.

## Paper 7. Grumbach, Lane, and von Krogh (2025/2026)

**Citation**

Grumbach, C., Lane, J. N., and von Krogh, G. "The Mean-Variance Innovation Tradeoff in AI-Augmented Evaluations." Harvard Business School Working Paper No. 26-038, posted December 17, 2025.

### What question the paper is asking

How does the sequencing and format of AI recommendations shape innovation evaluation outcomes?

This is a highly valuable paper because it shows that AI affects not only answers, but also the **structure of decision processes**.

### What the paper does

The paper studies a field experiment with 353 evaluators.

It focuses on a common problem in innovation evaluation:

- novelty matters
- feasibility matters
- people cannot fully assess both at once

So evaluators rely on **criteria-sequencing** heuristics.

The paper tests whether AI can structure those heuristics and thereby change the composition of selected ideas.

### What the paper finds

The paper finds a **mean-variance innovation tradeoff**:

- feasibility-then-novelty produces selections with higher mean innovation
- novelty-then-feasibility produces greater innovation variance
- format matters too: interactive chatbot formats increase variance but reduce mean innovation relative to static explanatory formats

This is a very powerful result.

It means AI does not merely influence judgment by giving additional information.

It shapes judgment by structuring the evaluator's path through the decision.

### Why this paper matters for your research

This paper is especially relevant if your project will include:

- screening processes
- portfolio design
- staged approvals
- innovation governance
- any multi-criteria business decision process

Its deepest contribution is the following:

**AI becomes part of organizational choice architecture**

That means business-context alignment must include:

- sequencing design
- format design
- path dependence
- portfolio-level consequences of micro-level interaction choices

### What this paper leaves open

The paper gives strong evidence about one evaluation setting, but more work is still needed on:

- generalization across domains
- persistent use over time
- interaction with organizational incentives
- when users learn and adapt to the sequence itself

Still, it is one of the strongest recent papers for showing that workflow architecture is itself an alignment variable.

## Paper 8. Vendraminelli et al. (2025)

**Citation**

Vendraminelli, L., DosSantos DiSorbo, M., Hildebrandt, A., McFowland III, E., Karunakaran, A., and Bojinov, I. "The GenAI Wall Effect: Examining the Limits to Horizontal Expertise Transfer Between Occupational Insiders and Outsiders." Harvard Business School Working Paper No. 26-011, September 2025.

### What question the paper is asking

Can GenAI allow people from one occupation to perform tasks typically done by another occupation with similar quality and speed?

This is a crucial organizational question because many firms hope AI will flatten skill differences and enable broad redeployment of labor.

### What the paper does

The paper studies insiders, adjacent outsiders, and distant outsiders in a field experiment at a UK-based global trading company.

Participants complete both conceptualization and execution tasks using or not using GenAI.

The paper introduces the concept of a **GenAI wall effect**:

the point at which AI can no longer meaningfully close the expertise gap between insiders and outsiders.

### What the paper finds

The core result is nuanced:

- GenAI can substantially help adjacent outsiders
- it is more effective for conceptualization than for execution
- it is less able to help distant outsiders bridge the gap to insiders

This is a strong counterweight to overly broad automation narratives.

### Why this paper matters for your research

This paper matters because it gives you a more realistic account of AI-enabled delegation and job redesign.

It suggests that delegation should be calibrated not only by task risk, but also by:

- knowledge distance
- role adjacency
- task phase
- the difference between framing work and finishing work

That is very useful for a business-context alignment framework.

It implies that firms should not assume all workers can become interchangeable with AI support.

### What this paper leaves open

The wall effect is persuasive, but it still needs replication across more industries and task types.

Even so, the broader lesson is highly useful:

**AI may stretch capability boundaries, but it does not erase them.**

## Paper 9. Randazzo et al. (2025)

**Citation**

Randazzo, S., Lifshitz-Assaf, H., Kellogg, K. C., Dell'Acqua, F., Mollick, E. R., Candelon, F., and Lakhani, K. R. "Cyborgs, Centaurs and Self-Automators: The Three Modes of Human-GenAI Knowledge Work and Their Implications for Skilling and the Future of Expertise." Harvard Business School Working Paper No. 26-036, revised December 2025.

### What question the paper is asking

When professionals work with GenAI across an entire problem-solving workflow, do they converge on a common collaboration style?

Or do they adopt meaningfully different modes of co-creation?

### What the paper does

The paper studies 244 global management consultants from the Boston Consulting Group and identifies three distinct modes of human-GenAI knowledge work:

- **Cyborgs**: tightly integrated human-AI work
- **Centaurs**: deliberate switching between human and AI tasks
- **Self-Automators**: abdicated co-creation with minimal engagement

### What the paper finds

The paper's deepest contribution is that these modes lead to different developmental trajectories:

- cyborgs build new AI-related capabilities
- centaurs strengthen task and domain capabilities
- self-automators gain little and may weaken their own professional capability

This is extremely important because it reframes AI use as a skill-formation problem, not only a task-completion problem.

### Why this paper matters for your research

This paper may be the single best conceptual bridge for your thesis language.

Why?

Because it turns vague ideas like "good use" or "bad use" into structured modes of collaboration.

That is exactly the kind of concept a business-context alignment project can build on.

It suggests that the right question is not:

- "Did the firm use AI?"

but:

- "What mode of human-AI collaboration did the firm institutionalize?"

This opens an important path for your project:

alignment may require not only correct decisions in the short run, but also collaboration modes that preserve or improve human judgment over time.

### What this paper leaves open

The categories are highly useful, but more work is needed on:

- whether these modes are stable over time
- how organizations push people into one mode rather than another
- how incentives, deadlines, and governance structures affect the distribution of modes

Still, as a framing device, it is exceptionally valuable.

## Synthesis: What These Papers Mean Together

If we step back from the individual studies, the combined message is strong.

### 1. AI alignment in business should be framed at the system level

These papers collectively argue against treating alignment as only a model-level property.

The main business problem is how the **human-AI system** is arranged.

### 2. The strongest current research focus is calibrated delegation

Across the papers, the recurring issue is not abstract values alignment.

It is whether AI is placed:

- in the right task
- at the right stage
- with the right interface
- under the right oversight conditions
- with the right expectations of human capability

### 3. Explanations and conversations are not neutral

Several papers show that AI interaction form matters.

Rationales can steer judgment.

Validation dialogs can become persuasive traps.

Interactive chat can alter selection outcomes.

This means governance has to cover the **interaction layer**, not only the output layer.

### 4. Human capability is part of the alignment problem

The literature increasingly suggests that alignment is not only about what AI can do.

It is also about whether humans can:

- interrogate it well
- override it well
- collaborate with it productively
- maintain professional judgment while using it

### 5. Organizational design remains central

The best recent papers repeatedly point to:

- team restructuring
- expertise recombination
- screening architecture
- role adjacency
- operating-model redesign

That means your project sits in a highly relevant and growing research space.

## What This Means For Your Thesis Direction

If your thesis continues under the frame of **business-context AI alignment**, the literature above suggests a strong and coherent center:

**How should firms design hybrid human-AI decision systems so that delegation improves performance without degrading judgment, accountability, or long-run human capability?**

That statement is stronger than a generic trust or ethics frame because it integrates:

- trust
- optimization
- risk
- governance
- capability development

It also keeps the project clearly business-facing.

## Most Important Open Questions After Reading These Papers

The literature is already rich, but several questions still look especially promising.

### 1. How should firms detect miscalibrated delegation in practice?

The literature shows the problem clearly.

It is still weaker on operational detection.

### 2. What governance mechanisms reduce narrative overreliance without destroying usability?

This is especially important for recommendation systems and screening systems.

### 3. How should firms separate generation from validation?

The persuasion-bombing work suggests this is a central design question.

### 4. How should organizations decide which jobs are adjacent enough for AI-enabled expertise transfer?

The wall-effect work makes this look like a tractable but underdeveloped area.

### 5. What human-AI collaboration modes produce the best long-run organizational capability?

The cyborg-centaur-self-automator framework raises this question sharply.

## Recommended Reading Order

If you want the fastest route to a strong conceptual base, read in this order:

1. Vaccaro, Almaatouq, and Malone (2024)
2. Dell'Acqua et al. (2025)
3. Ayoubi et al. (2024)
4. Randazzo et al. on persuasion bombing (2025)
5. Grumbach, Lane, and von Krogh (2025)
6. Vendraminelli et al. (2025)
7. Qin et al. with Lu (2025)
8. Sun et al. with Lu (2025)
9. Randazzo et al. on cyborgs, centaurs, and self-automators (2025)

The first five are the most important for the current repository.

## Source Links

- Nature Human Behaviour, Vaccaro et al. (2024): https://www.nature.com/articles/s41562-024-02024-1
- PubMed, Qin et al. with Lu (2025): https://pubmed.ncbi.nlm.nih.gov/40489180/
- PubMed, Sun et al. with Lu (2025): https://pubmed.ncbi.nlm.nih.gov/40522832/
- NBER, Dell'Acqua et al. (2025): https://www.nber.org/papers/w33641
- Harvard D^3, Dell'Acqua et al. summary (2025): https://d3.harvard.edu/the-cybernetic-teammate-how-ai-is-reshaping-collaboration-and-expertise-in-the-workplace/
- AISeL / ICIS 2024, Ayoubi et al. (2024): https://aisel.aisnet.org/icis2024/aiinbus/aiinbus/2/
- SSRN, Randazzo et al. on persuasion bombing (2025): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5678644
- D^3 Harvard, persuasion bombing summary (2025): https://d3.harvard.edu/persuasion-bombing-why-validating-ai-gets-harder-the-more-you-question-it/
- SSRN, Grumbach et al. (2025): https://ssrn.com/abstract=5933495
- D^3 Harvard, Grumbach et al. summary (2026): https://d3.harvard.edu/how-ai-can-spot-your-next-billion-dollar-idea/
- Harvard D^3, Vendraminelli et al. summary (2025): https://d3.harvard.edu/why-ai-helps-until-it-doesnt-inside-the-genai-wall-effect/
- SSRN, Vendraminelli et al. (2025): https://ssrn.com/abstract=5462694
- SSRN, Randazzo et al. on cyborgs, centaurs, and self-automators (2025): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4921696
- D^3 Harvard, cyborgs-centaurs-self-automators summary (2025): https://d3.harvard.edu/the-three-ways-professionals-work-with-ai-which-one-are-you/
