# Shadow AI Formalization Protocol

status: research deliverable
date_created: 2026-04-11
purpose: design a protocol for formalizing existing shadow AI practices with the 3-layer minimum viable governance, preserving innovation while adding structured quality assurance

## The Baseline Reality

- 90% of organizational AI tools operate without IT approval (ISC2/industry surveys, 2025)
- 46% of employees would continue using unauthorized AI even if explicitly banned
- Employees use AI 3x more often than managers realize (Waters-Lynch et al., 2025)
- 80% of American office workers use AI; only 22% rely exclusively on employer-provided tools

**Shadow AI is not a problem to solve — it is the actual state of AI adoption.** Any governance approach that starts from "implement official AI governance" ignores the fact that ungoverned AI use is already the dominant practice.

## The Formalization Approach

Waters-Lynch et al. (2025) identify four organizational responses to shadow AI:

| Response | Action | Outcome |
| --- | --- | --- |
| Repressive | Ban unauthorized AI | Innovation stops; shadow use goes deeper underground |
| Permissive | Ignore shadow AI | Innovation continues; risks accumulate invisibly |
| **Integrative** | Formalize shadow use into governance | Innovation preserved; oversight restored |
| Structural | Redesign organization around AI | Maximum potential; maximum disruption |

The 3-layer solution maps to the **integrative** response: formalize what already exists with minimum additional structure.

## The 4-Step Formalization Protocol

### Step 1: Surface (1 week)

**Goal**: Make shadow AI use visible without punishing it.

**Action**: Anonymous survey asking:
1. Which AI tools do you use for work? (list all, including personal accounts)
2. For each tool, what tasks do you use it for?
3. How often do you check AI output before acting on it? (always / sometimes / rarely / never)
4. Have you ever caught AI producing wrong or misleading output? (yes / no / not sure)

**Expected finding**: Most employees use AI for drafting, summarizing, analyzing, and generating content. Most do not systematically verify output. Some have caught errors; many haven't because they haven't looked.

**Key output**: A task inventory of actual AI use — the real-world equivalent of the 18-task decomposition, but grounded in what people actually do, not what a researcher designed.

### Step 2: Classify (1 session, 2 hours)

**Goal**: Apply Layer B (selective intervention) to the surfaced task inventory.

**Action**: In a team session, classify each surfaced AI use into the 3 profiles:

For each AI task the team reported:
- "If the AI gives a wrong answer, would you catch it by looking at the result?" → If yes: prediction-dominant
- "Does the task require you to interpret what the AI produced in context?" → If yes: interleaved
- "Does the task require you to make a judgment call that the AI can't make?" → If yes: judgment-dominant

**Key output**: A team-specific task map with governance assignments:
- Prediction-dominant tasks → keep using AI as-is (spot-check occasionally)
- Interleaved tasks → use bidirectional prompts (Layer A templates provided)
- Judgment-dominant tasks → "own answer first" before viewing AI output

**Critical design**: This session does NOT tell people to stop using AI. It tells them "keep doing what you're doing, but for THESE specific tasks, use this prompt template / write your answer first." The change is additive and targeted, not comprehensive.

### Step 3: Template (1 day)

**Goal**: Apply Layer A (bidirectional prompts) by providing ready-to-use prompt templates.

**Action**: For each interleaved and judgment-dominant task identified in Step 2, create a bidirectional prompt template that the team can copy-paste or save as a preset.

**Template format**:
```
[Task-specific instruction]

Before providing your analysis:
- List 3 points supporting [the likely conclusion]
- List 3 points challenging [the likely conclusion]
- Rate your confidence in each point

Then provide your analysis, explicitly weighing both sides.
Include at least one recommendation AGAINST the most obvious conclusion.
```

**Key output**: A shared prompt library (Google Doc, Notion page, or saved presets in AI tool) with bidirectional templates for each high-priority task.

**Critical design**: Users don't need to understand WHY bidirectional prompts work. They need to use the template. The knowledge is embedded in the artifact.

### Step 4: Habit (2 weeks of practice)

**Goal**: Apply Layer C ("own answer first") until it becomes automatic.

**Action**: For judgment-dominant tasks only, implement the rule:

> "Before you read the AI's output, open a note and write one sentence: what you think the answer is."

**Implementation options** (from least to most structured):
1. **Honor system**: Team agrees to the rule. Lowest friction, lowest compliance.
2. **Buddy system**: Pairs of colleagues share their pre-assessments with each other before viewing AI output. Social accountability without management oversight.
3. **Tool-embedded**: AI tool requires a text input before showing output. (Requires tool access/customization.)
4. **Slack/Teams ritual**: Post your pre-assessment in a dedicated channel before running the AI analysis. Creates a visible record.

**Expected timeline**: Per Trenz (2024), implementation intentions become habitual within 2-3 weeks of consistent practice. The habit persists without external enforcement once established.

## What Changes vs What Doesn't

| What changes | What doesn't change |
| --- | --- |
| Some prompts use bidirectional templates | Which AI tools people use |
| Judgment tasks get a 5-minute pre-assessment | How often people use AI |
| Team has a shared task classification | Who does what work |
| Shadow use is acknowledged, not punished | The underlying workflow |

**Total organizational disruption**: Minimal. One survey, one session, one template library, one behavioral rule. No new technology, no new roles, no new processes, no new approvals.

## Expected Outcomes

| Metric | Before formalization | After formalization |
| --- | --- | --- |
| AI use visibility | 10-20% (only official tools tracked) | 80-90% (shadow use surfaced) |
| Governance coverage | 0% of shadow AI use | 100% of high-risk tasks classified |
| Verification rate for judgment tasks | ~34% (industry average for any review) | 70-80% (behavioral rule for judgment tasks) |
| Time overhead per task | 0 (no governance) | 5 min for judgment tasks; 0 for prediction tasks |
| User satisfaction | High (no friction) | Slightly lower initially; recovers as habit forms |
| Error detection | Unknown (no measurement) | Measurable (pre-assessment creates comparison baseline) |

## The Formalization Pitch

When presenting to leadership, the pitch is not "we need AI governance." The pitch is:

> "90% of our team already uses AI daily. We don't know which decisions it's influencing. This protocol makes that visible in one week and adds quality assurance for the highest-risk tasks — without changing anyone's tools, workflows, or job descriptions. Total investment: one 2-hour session and a shared prompt library."

## Connection to the Research

This protocol IS the minimum viable governance applied to the real-world baseline (shadow AI). It demonstrates that the 3-layer solution can be deployed through formalization rather than transformation — the "integrative" response that Waters-Lynch et al. (2025) identify as optimal.

The protocol also generates data. The pre-assessments from Step 4 create a dataset of human-AI judgment comparisons that can be analyzed for:
- Which tasks show the largest human-AI divergence (these need more governance attention)
- Which tasks show consistent human-AI agreement (these can be safely delegated further)
- Whether divergence patterns change over time (tracking the organization's absorptive capacity growth)

This data closes the feedback loop: the governance mechanism also measures its own effectiveness.
