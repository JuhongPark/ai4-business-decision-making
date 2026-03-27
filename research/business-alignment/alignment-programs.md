# AI Alignment Programs, Fellowships, and Organizations

A directory of programs that train alignment researchers, produce safety research, and shape AI governance policy. Data collected 2026-03-26 from program websites and web searches.

For code repositories, see [alignment-codebases.md](alignment-codebases.md).
For the 80,000 Hours fellowships dataset (130 entries), see [ai-safety-fellowships-directory.md](ai-safety-fellowships-directory.md).

**Note on sourcing:** Program statistics (publication counts, alumni placement rates, cohort sizes) are drawn from each program's own website or promotional materials unless otherwise noted. These are self-reported figures and have not been independently verified. They are included for orientation, not as audited claims.

## Research Fellowships

Programs that produce alignment research outputs through structured mentorship and collaboration.

### MATS (ML Alignment Theory Scholars)

- **Site:** https://www.matsprogram.org/
- **Format:** 12-week in-person fellowship (Berkeley and London)
- **Scale:** 170+ publications, 9,500+ citations from alumni (per matsprogram.org, self-reported)
- **Research tracks:** Empirical (ML experiments on control, interpretability, oversight), Policy & Strategy, Theory, Technical Governance, Compute Infrastructure
- **Mentor orgs:** Anthropic, DeepMind, OpenAI, Redwood Research, ARC, UK AISI, LawZero
- **Alumni outcomes (self-reported):** 80% work in AI alignment/security; 10% founded organizations (Apollo Research, Timaeus, Center for AI Policy)
- **Notable outputs:** Sparse autoencoders for interpretability, activation engineering, developmental interpretability, situational awareness evaluation
- **Code:** qfeuilla/BehaviorEliciationTool (automated red-teaming)
- **Summer 2026:** Largest cohort — 120 fellows, 100 mentors

### SPAR (Supervised Program for Alignment Research)

- **Site:** https://sparai.org/
- **Format:** Part-time remote fellowship, 5–40 hours/week, 3 months
- **Operated by:** Kairos AI Project, Inc. (501(c)(3) nonprofit)
- **Scale:** 130+ projects for Spring 2026 — largest round of any AI safety research fellowship
- **Mentor count:** 130+ mentors including Dawn Song (UC Berkeley), Dylan Hadfield-Menell (MIT)
- **Research areas:** AI Safety, AI Policy, AI Security, Interpretability, Biosecurity, Societal Impacts
- **Outcomes:** Papers at NeurIPS 2024 and ICML 2025; TIME magazine coverage; job placements at Google AI Safety

**Notable Spring 2026 alignment projects:**

Misalignment detection and control:
- Pre-Emptive Detection of Agentic Misalignment via Representation Engineering (Dawn Song, UC Berkeley)
- Disentangling Instruction-Following from Strategic Obfuscation (WEN XING, MATS)
- Emergent Misalignment via Multi-Model Interactions (LawZero)
- Shutdown-Bench: Evaluating Shutdownability (Elliott Thornley, MIT)
- Stress-testing Honesty Training (Daniel Tan/Chloe Li, CLR/Anthropic)

Mechanistic interpretability:
- Sparse Geometry and Formal Verification for Interpretability (Yuxiao Li)
- Temporal Crosscoders — new SAE architecture for reasoning models (Dmitry Manning-Coe, MATS)
- Automating Circuit Interpretability with Agents (Georg Lange)
- Attribution Methods for LLMs (Uzay Macar, Anthropic Fellows)

Safety evaluation:
- Adversarial Red-Teaming Framework for LLM Agents (Dawn Song, UC Berkeley)
- Jailbreaks for AI Safety — auditing attacks for capable systems (Emil Ryd/Keshav Shenoy, Oxford/Anthropic)
- Richer Evaluations to Address Eval Awareness and Reward Hacking (Santiago Aranguri, Goodfire/NYU)

### LASR Labs (London AI Safety Research Labs)

- **Site:** https://www.lasrlabs.org/
- **Format:** 13-week summer program (July–October), teams of 3–4 supervised by experienced researchers
- **Stipend:** £11,000 + office space, meals, travel
- **Focus:** Technical AI safety — loss of control scenarios
- **Research areas:** Multi-agent collusion, RL alignment theory, deception detection, interpretability, automated interpretability, scalable oversight, AI control
- **Outcomes (self-reported):** 2024 cohort achieved 100% NeurIPS workshop acceptance (note: workshop acceptance rates are substantially higher than main-conference rates); alumni at UK AISI, Apollo Research, Leap Labs, Open Philanthropy

### Apart Research

- **Site:** https://apartresearch.com/fellowships
- **Programs:**
  - **Apart Fellowship** (12–24 weeks, 10–30 hrs/week, remote) — develop hackathon ideas into published research
  - **Partnered Fellowships** (~16 weeks) — work on expert-defined research agendas from partner organizations
- **Focus:** Technical AI safety — model evaluations, interpretability, multi-agent systems, AI security, formal methods, deception detection
- **Entry model:** Merit-based via monthly Research Sprints; continuous pipeline rather than fixed cohorts

## Training and Bootcamps

### ARENA (Alignment Research Engineer Accelerator)

- **Site:** https://www.arena.education/
- **Format:** 4–5 week in-person bootcamp in London, 2–3 per year; fully funded (travel, visa, accommodation, meals)
- **Focus:** Technical AI safety engineering skills — Python coding, linear algebra, probability foundations
- **Curriculum:** Freely available online for independent learners or organizations running their own courses
- **Alumni outcomes:** Roles at Anthropic, Apollo Research, METR; participation in MATS and LASR

### BlueDot Impact

- **Site:** https://bluedot.org/
- **Format:** Free AI courses (pay-what-you-want), career support, entrepreneurship acceleration, global events
- **Scale:** 5,000+ professionals trained since 2022; £35M raised; 6,000+ alumni
- **Courses:**
  - **Technical AI Safety** (30 hrs, cohort-based) — safety techniques, threat modeling, kill chain analysis. Requires LLM/fine-tuning basics.
  - **AI Governance** (25 hrs, cohort-based) — governance landscape, major proposals, policy career pathways. Relaunching 2026.
  - **AI Governance Fast-Track** (5 days intensive) — accelerated AI governance and policy fundamentals.
  - **Future of AI** (2 hrs, self-paced, free) — no prerequisites, intro to AI capabilities and risks.
- **Alumni placements:** OpenAI, Anthropic, Google DeepMind, AI Security Institute, UN, NATO, OECD, Stanford HAI, Apple, Harvard Kennedy School

### ML4Good

- **Site:** https://ml4good.org/
- **Format:** Free 8-day residential bootcamps, two tracks:
  - **Technical Programme** — for ML engineers, CS graduates, technical researchers
  - **Governance & Strategy Programme** — for policy/legal professionals, operations, communications
- **Cost:** Free (food, accommodation, teaching provided; travel reimbursed)
- **Alumni outcomes (self-reported):** Roles at MATS Research, Ada Lovelace Institute, UK AISI, SaferAI, CHAI; 98% recommendation rate

## AI Governance Research Organizations

### GovAI (Centre for the Governance of AI)

- **Site:** https://www.governance.ai/
- **Structure:** US 501(c)(3) nonprofit + UK subsidiary
- **Focus:** Technical AI governance, AI progress forecasting, threat modeling, labor market impact
- **Research topics:** Data center infrastructure policy, China's AI strategy, dual-use biological capabilities, government roles in AI agent infrastructure
- **Programs:**
  - **Summer Fellowship — Research Track** (3 months, June–August, London) — independent research with GovAI supervisor, £12,000 stipend + travel + lunch + desk
  - **Summer Fellowship — Applied Track** (3 months, June–August, London) — non-research projects (comms, policy engagement, event organizing), £12,000 stipend
  - **DC Summer Fellowship** (3 months, DC) — American AI governance and policy, bipartisan engagement
  - **Research Scholar** (1 year) — policy research, social science, or technical research
  - **Research Fellow** (2 years, renewable) — senior independent research position

### IAPS (Institute for AI Policy and Strategy)

- **Site:** https://www.iaps.ai/fellowship
- **Type:** Nonpartisan think tank — AI policy research at the intersection of AI, national security, geopolitics
- **AI Policy Fellowship 2026:** 3-month program (June–August), mandatory 2-week DC residency
  - Senior Fellows: $22,000 stipend; Fellows: $15,000 stipend
  - ~30 fellows per cohort
  - Projects: policy briefs, government briefings, conferences, op-eds
  - No technical expertise required

### Orion AI Governance Initiative

- **Site:** https://www.orionaigov.org/
- **Base:** UK-based talent development for AI governance
- **Programs:**
  - **AI Policy Accelerator** — 5-week training course (4 hrs/week: lectures, workshops, guest speakers) covering compute governance, model evaluations, international AI governance. Then 4-week research project (10 hrs/week) in small teams with experienced supervisor. For graduating students (Master's, final-year undergrad).
  - **Internship** — ~3 months over summer, £3,200/month. Placements at think tanks and AI governance organizations (2025: Safe AI Forum, Social Market Foundation).
  - **Mentorship Programme** — pairing students with AI governance professionals from GovAI, RAND, Ada Lovelace Institute, frontier AI lab policy teams. Availability depends on mentor pool.

## Pipeline Map

The alignment ecosystem has a clear progression structure:

```
Entry (no prerequisites)
  → BlueDot Future of AI (2 hrs)
  → ML4Good bootcamp (8 days)

Foundation (some technical/policy background)
  → BlueDot Technical AI Safety or AI Governance (25-30 hrs)
  → ARENA bootcamp (4-5 weeks)
  → Orion Accelerator (5 weeks + 4 weeks research)

Research (demonstrated ability)
  → SPAR (3 months part-time, remote)
  → Apart Research Sprints → Fellowship
  → LASR Labs (13 weeks, London)
  → MATS (12 weeks, Berkeley/London)
  → Anthropic Fellows (2-6 months, SF)

Governance track
  → GovAI Fellowship (3 months, London/DC, £12k)
  → IAPS Fellowship (3 months, DC, $15-22k)
  → RAND CAST Fellows (rolling)

Career destinations
  → Anthropic, DeepMind, OpenAI, UK AISI
  → Apollo Research, Redwood Research, METR
  → GovAI, RAND, CNAS, government positions
```

## Relevance to Business-Context Alignment

These connections are hypothesized based on ecosystem observation, not empirically verified:

1. **Research fellowships** (MATS, SPAR, LASR) produce safety techniques (e.g., activation engineering, deception detection) that may inform future enterprise safety tools — though no direct adoption pathway from fellowship output to commercial product has been documented here.
2. **Training programs** (BlueDot, ARENA, ML4Good) are likely sources of AI safety talent for hiring, given their alumni placement records at major labs. However, the actual hiring flow from these programs to non-lab businesses is not tracked.
3. **Governance organizations** (GovAI, IAPS, Orion) produce policy research that may influence regulatory frameworks. GovAI's work has been cited in UK and EU policy discussions (per governance.ai), but the pathway from think-tank output to binding regulation is indirect and uncertain.
4. The **pipeline structure** suggests alignment is professionalizing — relevant for organizations planning to build internal AI governance teams, though the talent supply remains small relative to demand.

## Limitations

- **Self-reported data:** Program outcome statistics (placement rates, publication counts, recommendation rates) are sourced from program websites and are not independently verified.
- **Selection bias:** Programs included here are primarily English-language, Western-centric, and concentrated in the EA/AI safety community. Corporate training programs, government initiatives, and non-Anglophone programs are underrepresented.
- **No quality evaluation:** Programs are listed descriptively without quality ranking or comparative assessment. Inclusion does not imply endorsement.
- **Temporal validity:** Program details (stipends, dates, cohort sizes) are as of 2026-03-26 and change frequently.
- **Missing demand-side analysis:** This directory covers the supply of alignment talent and research but does not analyze which businesses adopt these outputs or how.
