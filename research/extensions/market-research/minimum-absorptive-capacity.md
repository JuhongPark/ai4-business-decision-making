# Minimum Absorptive Capacity for the 3-Layer Solution

status: research deliverable
date_created: 2026-04-11
purpose: define the minimum knowledge threshold an organization needs to implement the 3-layer solution, and test whether the solution itself can provide that knowledge

## The Question

Cohen and Levinthal (1990) established that absorptive capacity — the ability to recognize, assimilate, and apply new knowledge — is the prerequisite for technology adoption. Organizations below the threshold experience "lockout" and cannot adopt regardless of governance.

For the 3-layer solution, the question is: **what does an organization need to know BEFORE they can use bidirectional prompts, selective intervention, and "own answer first"?**

## Knowledge Requirements by Layer

### Layer A (Bidirectional Prompts): Near-Zero Prerequisite

**What the user needs to know**: That AI tends to confirm the direction of the prompt, and that asking for both sides produces better analysis.

**How long this takes to learn**: One example. Show a standard prompt and its sycophantic output, then show a bidirectional prompt and its balanced output. The contrast is immediately legible.

**Can the solution itself teach this?** Yes. The prompt template IS the knowledge. A user who follows the template ("List 3 reasons for AND 3 reasons against before analyzing") is applying the knowledge without needing to understand the theory.

**Minimum absorptive capacity**: Ability to follow a prompt template. This is equivalent to "can fill in a form" — the lowest possible threshold.

### Layer B (Selective Intervention): Moderate Prerequisite

**What the user needs to know**: Which of their tasks require human judgment and which can be delegated to AI with spot-checking.

**How long this takes to learn**: This requires understanding one's own work process well enough to distinguish prediction tasks from judgment tasks. For an experienced practitioner, this is 15-30 minutes of guided classification using the 3-profile framework:
- "Does this task have a verifiable right answer?" → prediction-dominant
- "Does this task require interpreting what data means in context?" → interleaved
- "Does this task require choosing between options based on values or strategy?" → judgment-dominant

**Can the solution itself teach this?** Partially. The task decomposition for market research (18 tasks pre-classified) serves as both the governance tool AND the knowledge base. A market research practitioner reading the decomposition learns which tasks require their judgment and which don't. The tool teaches the user what they need to know to use the tool. The critical intervention point identified in pipeline-cognitive-forcing.md is the Stage 2→3 boundary, where analysis transitions from data synthesis to interpretation — this is where the classification matters most.

For non-market-research domains: a facilitator needs to lead the team through a task classification exercise (~2 hours) to produce the domain-specific decomposition. This is a one-time investment.

**Minimum absorptive capacity**: Ability to describe one's own work process as a sequence of tasks. This requires basic process awareness — knowing what you do, not just doing it.

### Layer C (Own Answer First): Low Prerequisite

**What the user needs to know**: That their own judgment is valuable and that forming it before seeing AI improves the combined outcome.

**How long this takes to learn**: This is a behavioral change, not a knowledge acquisition. The user needs to believe that their pre-AI judgment matters. For experienced practitioners, this is intuitive — they have professional pride in their judgment. For junior staff, it may require explicit framing: "Your experience-based intuition catches things AI misses."

**Can the solution itself teach this?** Yes, through experience. After 3-5 uses of the "own answer first" protocol, users observe instances where their pre-assessment identified issues the AI missed. This self-reinforcing loop builds the belief that underpins the behavior.

**Minimum absorptive capacity**: Willingness to spend 5 minutes writing before reading AI output. This is a behavioral threshold, not a knowledge threshold.

## The Minimum Viable Knowledge Package

An organization needs exactly THREE things to implement the 3-layer solution:

### 1. One Example of Sycophancy (5 minutes)

Show a side-by-side comparison:
- Standard prompt → sycophantic output (100% confirming, no alternatives)
- Bidirectional prompt → balanced output (65% confirming, 3 alternatives, counter-evidence)

This single example establishes WHY the solution is needed. No theory, no framework, no training program — just one visible contrast.

### 2. One Task Classification Session (2 hours, one-time)

The team classifies their key AI-assisted tasks into 3 categories:
- "AI can just do this" (prediction) → spot-check only
- "AI does the analysis, I add the interpretation" (interleaved) → checkpoint review
- "I need to think about this myself" (judgment) → own answer first

This produces a domain-specific task map that serves as both the governance structure and the knowledge base. It requires a facilitator for the first session but is self-maintaining afterward.

### 3. One Behavioral Rule (30 seconds to state, 2 weeks to habituate)

"Before you read what the AI wrote, write one sentence about what YOU think the answer is."

This is the entire Layer C. It requires no knowledge acquisition, no training program, and no technology change. Per Trenz (2024), implementation intentions become habits within 2-3 weeks of consistent practice.

## The Self-Teaching Property

A critical finding: **the 3-layer solution is self-teaching**. The solution itself provides the absorptive capacity needed to use the solution.

| Layer | Knowledge needed | How the solution provides it |
| --- | --- | --- |
| A | AI confirms prompt direction | The bidirectional template demonstrates the problem by contrast |
| B | Which tasks need judgment | The task classification exercise produces the knowledge as output |
| C | Pre-AI judgment has value | Using the protocol 3-5 times demonstrates the value experientially |

This means the lockout condition (Cohen and Levinthal's permanent adoption failure) is unlikely for the 3-layer solution, because the minimum knowledge is embedded in the intervention itself. The only true prerequisite is willingness to try.

## Absorptive Capacity Threshold Test

**Prediction**: An organization can implement the 3-layer solution if it meets ALL THREE of these minimum conditions:

1. **Process awareness**: At least one person can describe the team's AI-assisted work as a sequence of tasks (not just "we use AI for analysis")
2. **Prompt access**: The team can modify the prompts they use with AI (not locked into a fixed interface with no prompt control)
3. **Time willingness**: The team is willing to invest 5 minutes of pre-AI thinking per judgment-dominant task

**Organizations below this threshold**: Cannot implement the 3-layer solution and are likely in the lockout condition for any AI governance. The intervention for these organizations is not governance but basic AI literacy — understanding that AI produces output that requires evaluation, not acceptance.

## Implications

The absorptive capacity analysis suggests that **the 3-layer solution's real competitor is not other governance frameworks but organizational willingness**. The knowledge barrier is near-zero (one example + one session + one rule). The remaining barrier is motivational: does the organization want to use AI responsibly, or does it want to use AI fast?

This reframes the adoption challenge from "how do we train people to use the framework?" to "how do we demonstrate in 5 minutes that the framework is worth 5 minutes of effort per task?" The one-example demonstration (sycophantic vs balanced output) is the minimum viable pitch.

## Scope Limitation

This analysis focuses on **knowledge absorption barriers**, which are minimal for the 3-layer solution. However, organizational, professional identity, liability, and psychological adoption barriers documented in adoption-barrier-implications.md may exceed knowledge barriers in practical importance and require separate intervention strategies. The absorptive capacity threshold is necessary but not sufficient — an organization that meets the knowledge threshold may still face resistance from professional identity threat (e.g., analysts who feel demoted to "AI checkers") or liability uncertainty (e.g., who signs off on AI-assisted decisions). These barriers are addressed elsewhere in the research portfolio but are not solvable by the 3-layer solution alone.
