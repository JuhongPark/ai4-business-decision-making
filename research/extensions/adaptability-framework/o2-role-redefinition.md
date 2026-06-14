# O2 — Role Redefinition Cycles and Triggers

axis: O (Pillar 2 — Organizational Structure)
date: 2026-04-22
plan: research/operations/expansion/adaptability-framework-research-plan.md

---

## 1. Method

**Research question (verbatim from the plan)**: How often, and under what triggers, do organizations formally redefine roles in response to AI change? Produce concrete examples 2023–2026 of roles created, eliminated or consolidated, and merged or silently redefined, distinguishing structural change from rebranding. Output a role-life-cycle model with typical durations.

**Evidence sources (labeled)**.
- *Observed — public record*: company press releases, SEC filings, S-1 / 10-K risk-factor language, announced layoffs reported in Bloomberg / WSJ / FT / Reuters / Business Insider, earnings-call transcripts, job postings visible on Greenhouse / Lever / company careers pages, LinkedIn Economic Graph job-title series, Ravio / Pave / Levels.fyi compensation disclosures, Indeed Hiring Lab and Seek (Australia) job-title trend posts, Challenger/Gray/Christmas AI-attributed layoff tallies, BLS OES category additions, O*NET task-update releases.
- *Observed — scholarship*: Eloundou-Manning-Mishkin-Rock "GPTs are GPTs" (2023), Felten-Raj-Seamans AI exposure index updates (2024-2025), Brynjolfsson-Li-Raymond productivity field studies (2023-2025), Acemoglu labor-displacement work (2024-2025), Autor-Reynolds-Dawson reskilling studies (2024-2025).
- *Inferred*: role-life-cycle duration estimates, trigger-to-effect lag, structural-vs-rebranding boundary decisions.
- *Training-knowledge flag*: this memo uses the assistant's training knowledge cutoff January 2026 plus the 2026-04-22 date context. Where a claim depends on data post-January 2026, it is labeled [post-cutoff; flagged]. Job-posting counts and compensation bands are point-in-time estimates that drift week-to-week.

**Confidence labels**. H = high (multi-source, convergent), M = medium (single-source or partial convergence), L = low (single anecdote or strong inference beyond direct evidence).

**Structural-vs-rebranding test (applied throughout)**. A role change is counted as *structural* if at least two of the following hold: (i) a new reporting line is created, (ii) the compensation band shifts by ≥20%, (iii) the work product measurably changes (new deliverables, new tools, new accountability), (iv) hiring criteria change in a way that would have filtered out the prior incumbents. A role change is counted as *rebranding* if only the title moves and the filtering criteria / deliverables / reporting line persist.

---

## 2. Roles created 2023–2026

Table columns: role title, first-appearance date and source, peak prevalence (approx. share of AI-active firms or posting index), still-current as of 2026-04, typical level, obsolescence signals, example firms.

| Role title | First-appearance (date, source) | Peak prevalence | Still current Apr 2026 | Typical level | Obsolescence signals | Example firms | Confidence |
|---|---|---|---|---|---|---|---|
| Prompt engineer | Early 2023; viral coverage in WSJ, Bloomberg, Time (Mar-May 2023); Anthropic posting for "Prompt Engineer / Librarian" at $250-375K base (Apr 2023) | Peaked Q3 2023 by LinkedIn and Indeed job-title counts | Declined; surviving in vertical-domain pockets (legal prompt engineer at Harvey; clinical prompt engineer at select health-IT firms) and as part of merged "AI engineer" or "applied AI engineer" titles | IC; occasional senior IC | Title frequency collapsed ~60-80% on LinkedIn/Indeed 2024 vs. 2023 peak; OpenAI o1 and Claude 3.5 Sonnet / 4 Opus reduced payoff per hour of prompt tuning; essays "Death of Prompt Engineering" (2024-2026); merged into "AI engineer" | Anthropic, Scale AI, Boston Consulting Group, Klarna, Klaviyo, early adopters across fintech/SaaS | H (emergence, decline) |
| Forward-deployed engineer (FDE) | Originated at Palantir ~2010s as deployment-strategist hybrid; re-popularized 2023-2024 at Scale AI, OpenAI, Anthropic, Cognition, Harvey, Sierra | Adopted 2024-2026 by most agent/application AI firms | Yes — growing | IC through senior IC; small firms give VP-FDE | None yet; structurally protected because customers demand on-site integration | Palantir, Scale AI (pre-Meta investment), OpenAI, Anthropic, Cognition, Harvey, Sierra, Decagon, Glean, Adept (pre-shutdown) | H |
| AI / ML evaluation engineer (eval engineer) | Formal titles visible late 2023 at Anthropic; proliferated 2024-2025 at OpenAI, Google DeepMind, Apple, Meta, Scale AI SEAL, Harvey | 2025-2026 peak, still rising | Yes — rising | IC through staff IC; some research-scientist variants | None visible; reinforced by Gartner LLM-observability forecast to 50% of deployments by 2028 | Anthropic, OpenAI, Apple (Siri AI Quality Engineering), Meta, Google DeepMind, Scale AI SEAL / Scale Labs, Harvey, Patronus, Galileo, Arize, Braintrust | H |
| Chief AI Officer (CAIO) | First named C-suite appointments 2022-2023 (some earlier at GE, Bosch); US federal Executive Order 14110 (Oct 30, 2023) mandated CAIO at each federal agency; Fortune 500 wave 2023-2025 | By late 2025 majority of Fortune 500 had an identified AI leader; IBM survey and Spencer Stuart / Heidrick reports indicated 15-40% with a named CAIO depending on definition | Yes — saturating | C-suite (sometimes SVP, "Head of AI") | Risk of absorption into existing CTO / CDO / COO as AI stops being treated as a separate workstream; 2026 press ("Does every company still need a CAIO?") signals consolidation pressure | JPMorgan (Teresa Heitsenrether, 2023), Accenture, Mastercard, Dell, HPE, Procter & Gamble, Mayo Clinic, US Cabinet agencies, Bloomberg | H |
| AI product manager (AI PM) | Late-2022 / early-2023 at Microsoft, Google, Meta; standard at OpenAI / Anthropic / Scale hires 2023-2024 | 2024-2026 plateau at most large firms; differentiated into agentic PM, platform PM, applied AI PM | Yes — core | IC through director | None; being absorbed into "PM" baseline at AI-forward firms (see §4) | Microsoft, Google, Meta, OpenAI, Anthropic, Stripe, Notion, Linear, Intercom, Klarna, Atlassian | H |
| AI solutions architect / AI deployment engineer | Wide postings 2023-2024 at Nvidia, AWS, Google Cloud, Microsoft, Databricks, Snowflake | 2024-2026 stable | Yes | IC through senior IC | None yet | Nvidia, AWS, GCP, Microsoft, Databricks, Snowflake, Accenture, Deloitte, IBM consulting | H |
| AI red-teamer / model-safety red-teamer | Structured at OpenAI (GPT-4 red-team cohort, 2022-2023), Anthropic, Google DeepMind; UK AISI and US AISI (2023-2024) institutionalized it; Meta GenAI Trust & Safety | 2024-2026 expansion | Yes | IC through staff; government-lab equivalents | None visible; expanding with regulatory pressure | Anthropic, OpenAI, Google DeepMind, Meta, UK AISI, US AISI, Scale SEAL, Haize Labs | H |
| AI governance / responsible-AI lead | 2023-2024 formalization tracked by IAPP AI Governance Professional (AIGP) certification (launched 2023) with ~10,000 certified by 2025 per IAPP | 2024-2026 expansion under EU AI Act compliance deadlines (General-purpose AI obligations Aug 2025; high-risk systems Aug 2026) | Yes | Manager through VP | None visible near term | Microsoft (Office of Responsible AI since 2019, expanded), IBM, Accenture, Deloitte, KPMG, PwC, EY, JPMorgan, Goldman Sachs, large pharma | H |
| AI ops / LLMOps / MLOps-for-LLM engineer | 2023 cloud vendor postings; 2024-2025 canonicalized as LLMOps | 2024-2026 rising; increasingly merged into platform engineering | Yes — may merge | IC | Consolidation into "platform engineer (AI)" visible | Databricks, Weights & Biases, Hugging Face, ClickHouse (post-Langfuse acquisition Jan 2026), LangChain | M-H |
| AI ethicist / AI policy manager | Existed pre-2023 at Microsoft, Google, IBM, Accenture; expansion 2023-2026 | 2024-2026 rising | Yes | Manager through director | None; but oscillates with layoff cycles — Google disbanded parts of responsible-AI team Dec 2023-Jan 2024 (per WSJ reporting) and rebuilt; Microsoft ethics and society team disbanded Mar 2023 | Microsoft, Google, IBM, Accenture, McKinsey, Deloitte | M |
| AI applied research engineer / AI engineer | Canonicalized by Chip Huyen's *AI Engineering* (O'Reilly, 2025) and Maven / a16z discourse 2024-2025 | 2024-2026 dominant new generalist title | Yes | IC through staff | None; absorbing "prompt engineer" and "LLM engineer" subroles | OpenAI, Anthropic, Meta, Google, Stripe, Notion, Linear, Cursor, Replit, Perplexity, Harvey | H |
| Model welfare researcher | Published titles at Anthropic from 2024; discrete research agenda | Very small — < 50 identifiable positions globally | Yes — niche | IC research scientist | None; still niche | Anthropic (Kyle Fish, public hire Sep 2024), Eleos AI (non-profit) | M |
| Agent / agentic engineer | Late-2024 onward; widespread 2025-2026 after Devin (Cognition, Mar 2024), Claude computer-use (Oct 2024), GPT-5 agentic modes, OpenAI Operator (Jan 2025), Anthropic Claude Code (Feb 2025) | 2025-2026 rising | Yes | IC through staff | None; risk of re-absorption into "AI engineer" as scaffolding abstractions stabilize | Cognition, Anthropic, OpenAI, Google, Adept (pre-shutdown), Perplexity, Sierra, Decagon | H |
| Head of AI training data / data ops for AI | 2023-2024 at Scale AI, Surge AI, Invisible, Snorkel, Prolific | Peak 2024-2025; dampened by Scale's customer-loss post-Meta investment and by synthetic-data advances | Yes — but crowded market | Director through VP | Synthetic data (Claude, GPT-4-class annotators replacing human labellers) compresses demand in low-complexity domains; high-complexity domains (math, code, multimodal, PhD-tier) expanding | Scale AI, Surge AI, Labelbox, Invisible, Snorkel, Prolific, Mercor (post-2024 pivot to expert labor) | M-H |
| AI curriculum / AI skills lead (L&D) | 2023-2024 at McKinsey, Accenture, BCG, Deloitte, EY, KPMG, BCG X, Bain Vector | Peak 2024-2025 during large-firm reskilling waves; BCG, McKinsey, Accenture all announced >100K employee reskilling by 2024-2025 | Yes — may merge into L&D | Director | None yet; consolidates back into L&D once AI fluency is a baseline expectation | McKinsey, BCG, Accenture, Deloitte, PwC, EY, KPMG, Salesforce, Microsoft | M |
| Workplace AI program manager (internal deployment PM) | 2024-2025 internal tooling and adoption roles at Shopify, Klarna, Goldman Sachs, JPMorgan, Salesforce | Peak 2025-2026 | Yes | Senior IC through director | Risk of merging into general IT / COO function | Shopify, Klarna, Goldman Sachs, JPMorgan, Salesforce, Atlassian | M |
| Vertical-AI domain lead (legal AI lead, clinical AI lead, financial AI lead) | 2023-2026 at Harvey, Hippocratic AI, AbridgeAI, Bloomberg, JPMorgan, Moody's, OneMedical | Rising 2024-2026 | Yes | Director through SVP / MD | None visible; likely to proliferate as regulated domains accelerate | Harvey, Hippocratic AI, Abridge, Moody's AI, Bloomberg GPT program, Epic / Cerner clinical-AI leads | H |
| AI adoption / AI value realization analyst | 2024-2026 at consultancies and enterprise IT orgs | Rising 2025-2026 | Yes — bubble risk | IC through manager | Likely to consolidate back into general transformation analyst once tracking stabilizes | Accenture, Deloitte, Gartner, IDC, McKinsey Digital, large enterprise IT PMOs | L-M |

**Summary**. Eighteen role families covered in this table. Eight are in emergence or rising phases (eval engineer, AI red-teamer, AI governance lead, agentic engineer, vertical-AI domain lead, CAIO, AI PM variants, FDE). Five are plateauing (AI solutions architect, AI ethicist, AI ops / LLMOps, head of AI data, AI curriculum lead). Two are in visible decline or absorption (prompt engineer, AI curriculum lead in some consultancies). Three are bubble-prone and may consolidate (AI adoption analyst, workplace AI PM, AI ops in small firms).

---

## 3. Roles eliminated or consolidated 2023–2026

Table columns: role, trigger, firm(s), date, magnitude, structural vs. rebranding, evidence, confidence.

| Role eliminated or consolidated | Primary trigger | Firm(s) | Date | Magnitude | Structural vs. rebranding | Evidence | Confidence |
|---|---|---|---|---|---|---|---|
| Customer-support tier-1 agent (English-language, text chat) | Capability release (GPT-3.5 / Claude 2 inflection) + cost pressure | Klarna | Feb 2024 announcement | Claimed 700 FTE-equivalent handled by AI assistant; workforce reduction from ~5,500 to ~3,500 over 2023-2024 per company statements | Structural | Klarna Feb 2024 press release; Sebastian Siemiatkowski public statements; Bloomberg / FT / Reuters coverage | H |
| Copywriting / content marketing generalist | Capability release + price collapse | IBM (marketing), BuzzFeed (content), Microsoft (MSN editorial), Red Ventures, CNET parent | 2023-2024 | BuzzFeed News shutdown Apr 2023 (partly unrelated); CNET byline pause Jan 2023 after AI-authored articles discovered; MSN editorial team layoff 2020-2024 trajectory | Mixed — structural in low-end, rebranding/consolidation at the high end | Futurism / The Verge coverage of CNET Jan 2023; NYT coverage of MSN; company releases | H |
| Translation — generalist localization reviewer for common language pairs | Capability release | Duolingo (contractor base cut ~10% Dec 2023); Unity, Electronic Arts, Activision reductions 2023-2024 | Dec 2023 onward | Duolingo: ~10% contractor translation workforce reduction, explicitly attributed to generative AI | Structural | Bloomberg Jan 2024 reporting; Duolingo IR statements | H |
| Illustrators / stock-image photographers (entry-level) | Capability release (Midjourney, DALL-E 3, Stable Diffusion XL, Flux) + price collapse | Getty, Shutterstock, freelance / gig platforms | 2023-2026 | Getty and Shutterstock licensing pivots; freelance hourly rates on Upwork / 99designs declined in several photographic categories per platform labor reports | Mixed | Getty lawsuits vs. Stability; Upwork / Fiverr platform reports; Bloom et al. freelance studies | M-H |
| Junior software engineer (entry pipeline) | Capability release (Copilot, Cursor, Devin, Claude Code); price collapse; cost-cutting | Multiple large tech firms | 2023-2026 | Not a formal eliminated *title* — but an attenuated hiring pipeline; new-grad SWE hiring at FAANG down 20-50% 2023-2025 per multiple press reports; several CEOs (Shopify, Klarna, Meta, Amazon) publicly required AI-use justification before headcount requests | Structural (hiring filter and pipeline change) without formal title removal | Shopify Tobi Lütke memo Apr 2025; Klarna IR; Meta / Amazon public hiring pauses; NACE / Handshake new-grad reports; Eloundou-Manning Li et al. studies | H |
| Research analyst — low-complexity equity research | Capability release + cost-cutting | JPMorgan, Goldman Sachs, Citi, Morgan Stanley, Bloomberg Intelligence | 2023-2026 | Partial — headcount compressed in low-complexity coverage; upgraded in high-complexity coverage | Mixed; mostly consolidation | Earnings calls; FT coverage of sell-side analyst trimming; Bloomberg and Morningstar AI-tool deployment | M |
| Paralegal (entry-level discovery and contract review) | Capability release (Harvey, Thomson Reuters CoCounsel, Lexis+ AI) | Multiple AmLaw 100 firms | 2024-2026 | Partial; entry pipeline compressed, senior paralegal augmented | Mixed | Harvey case studies; A&O Shearman, Allen & Overy, Ashurst, Macfarlanes deployments 2023-2025; Law.com coverage | M |
| Tier-1 clinical transcriptionist | Capability release (Nuance DAX Copilot, Abridge, Ambience Healthcare, Suki, DeepScribe) | Large US health systems | 2023-2026 | Substantial; transcription-specific headcount cuts at scribing services; ambient documentation roles expanded | Structural (work replaced) with some rebranding (to AI-assisted scribe QA) | Nuance / Microsoft press; Epic integration posts; KLAS AI scribe reports; Abridge expansion | H |
| Graphic designer — marketing-production generalist (low-complexity assets) | Capability release + price collapse | Agencies — Publicis, WPP, Omnicom; in-house teams at CPG and retail | 2023-2026 | Partial; automation of variant production and asset resizing | Mixed | WPP AI partnership press (with Nvidia, Nov 2023); Publicis CoreAI initiative (Nov 2023); Omnicom-IPG merger Dec 2024 with AI-stated efficiencies | M |
| IT helpdesk / support tier-1 generalist | Capability release (ServiceNow Now Assist, Zendesk AI, Moveworks-Zendesk deal Mar 2024 $1.25B later amended) | Large enterprise IT | 2023-2026 | Substantial in large enterprise IT | Structural | ServiceNow, Zendesk, Moveworks press; Gartner IT service desk forecasts | H |
| Market-research survey analyst (low-complexity) | Capability release | Qualtrics, Nielsen, Ipsos | 2024-2026 | Partial | Mixed | Qualtrics earnings; Nielsen / Ipsos press | L-M |
| Proofreader / entry-level editorial assistant | Capability release | Publishing, content agencies | 2023-2025 | Partial | Mixed | Trade coverage (Publishers Weekly, The Bookseller); Grammarly, Writer, Jasper adoption | M |
| Data-entry clerk | Capability release + pre-existing OCR trend | Insurance, healthcare admin, banking ops | 2023-2026 | Substantial but continuation of pre-2023 trend; AI is an accelerator, not sole cause | Structural (continuation) | BLS OES, Challenger / Gray / Christmas trackers, Brookings automation studies | H (trend); M (AI attribution) |
| Low-end call-center CSR (outside US / offshore contact centers) | Capability release + cost-cutting | BT, Teleperformance, IBM BPO, Indian / Philippine BPO majors | 2023-2026 | Heavy in English-language queues; BT announced 55K reductions May 2023 attributing portion to AI | Structural | BT 2023 press; Teleperformance guidance downgrade 2024 after AI-replacement concerns; IBM Arvind Krishna May 2023 pausing back-office hiring | H |

**Notes**. Where the line between "eliminated" and "consolidated" is uncertain, the memo prefers "consolidated" because most 2023-2026 moves compressed low-end variants into augmented higher-skill variants rather than erasing a role family. The Klarna case is the most cited as pure elimination; the paralegal and junior-SWE cases are the most cited as pipeline-attenuation without formal title removal.

---

## 4. Roles merged or silently redefined without formal rename

These are the roles whose title stayed the same but whose scope changed enough to filter out prior incumbents or reshape deliverables.

| Role (unchanged title) | What changed | Trigger | When | Firm(s) / evidence | Confidence |
|---|---|---|---|---|---|
| Software engineer (general) | Expected fluency with Copilot / Cursor / Claude Code; PR review of AI-generated code; "AI-native" coding workflows; some firms (Shopify, Amazon) made AI-use justification part of promotion or headcount process | Capability release; cost-cutting | 2023-2026 | Shopify memo Apr 2025; Amazon / Andy Jassy June 2025 memo on expecting smaller corporate workforce; Microsoft and Google internal dev-productivity programs; Meta's 2024 "year of efficiency" continuation | H |
| Product manager (general) | Expected to write and evaluate AI prompts; own evals for AI features; ship under daily model-update uncertainty | Capability release | 2023-2026 | Shreya Shankar / Hamel Husain Maven course "AI Evals for Engineers and PMs"; Lenny Rachitsky AI-PM content; internal competency maps at Atlassian, Intercom, Stripe | M-H |
| Designer (UX / product) | Expanded to include agent / conversational UI, eval-as-design, prompt-surface design; also expected fluency in Figma AI / Midjourney / v0 / Lovable | Capability release | 2024-2026 | v0 (Vercel) adoption 2023-2025; Lovable / Bolt / Replit Agent; Figma AI release 2024-2025; design-leader blogs | M |
| Copywriter (surviving positions) | Moved up the value chain to brand voice, prompt-library authorship, model-evaluation for brand consistency | Capability release | 2023-2026 | Writer, Jasper, Typeface case studies; WPP / Publicis AI content workflows | M |
| Technical writer | Merged with AI-documentation engineering; now includes prompt library curation, doc eval, LLM-friendly markup | Capability release | 2024-2026 | GitBook, Mintlify, Readme / Docs platforms AI features; internal docs at Stripe, Linear | L-M |
| Customer-support specialist (surviving) | Escalation-only scope; specialized in complex cases, AI-QA of automated responses; "AI supervisor" de facto | Capability release | 2023-2026 | Klarna, Intercom, Decagon, Sierra, Zendesk, Ada case studies | H |
| Sales engineer | Expanded to include AI solution scoping, eval design for customer POCs, agent orchestration demos | Capability release | 2024-2026 | Nvidia, OpenAI, Anthropic, Databricks, Glean sales-engineer postings | H |
| Data scientist | Shifted toward LLM-assisted analysis, prompt engineering for analytics, less classical ML feature engineering; titles bifurcating into "research scientist" and "applied data scientist (LLM)" | Capability release | 2023-2026 | OpenAI / Anthropic postings; a16z blog on data-science role evolution (2024-2025); internal competency maps at Stripe, Airbnb, Uber | M |
| Security engineer | Added AI-model red-teaming, prompt-injection defense, MCP / agent sandboxing scope; OWASP Top 10 for LLM Applications (2023, updated 2024-2025) and MITRE ATLAS updates | Capability release; regulatory | 2023-2026 | OWASP LLM Top 10; MITRE ATLAS; NIST AI RMF profiles; firm-level CISO blogs | H |
| Recruiter | Expected to use AI sourcing tools (Gem, Juicebox, HireEZ AI, Mercor) and to screen for AI fluency in candidates | Capability release | 2023-2026 | Recruiter tool vendor case studies; LinkedIn Talent Solutions AI features | M |
| Lawyer (associate) | AI-augmented drafting, contract review, due-diligence review expected; some firms (A&O Shearman, Macfarlanes) restructured associate training around AI | Capability release | 2024-2026 | Harvey case studies; firm press; NLJ / Law.com coverage | M-H |
| Financial analyst | AI-augmented document review (earnings, filings), LLM-assisted model building, research drafting | Capability release; cost-cutting | 2023-2026 | JPMorgan LLM Suite / IndexGPT; Goldman Sachs GS AI Platform; Morgan Stanley AI assistant with OpenAI; Bloomberg GPT | H |
| Teacher / instructional designer (K-12 and corporate L&D) | AI-assisted content generation, Khanmigo-like tutor integration, rubric-based AI eval of student work | Capability release | 2023-2026 | Khan Academy Khanmigo (2023-2025); Chegg strategic pivot and CEO comment May 2023; corporate L&D at Coursera, Udemy | M |

**Interpretation**. Silent redefinition is more prevalent than explicit title change. For most large incumbent organizations, the dominant adaptation pattern 2023-2026 was "keep the title, change the expectation" — a workflow retooling (see A3) that does not register as a role-life-cycle event in org charts but does register in hiring criteria, promotion standards, and job-posting descriptions.

---

## 5. Trigger taxonomy

| Trigger | Role-change mechanism | Typical time lag (trigger to observable role change) | Dominant effect direction | Example |
|---|---|---|---|---|
| Capability release (new frontier-model generation) | Creates net-new specialist roles (eval, agentic, red-team) and silently redefines generalist roles (SWE, PM, lawyer, analyst); at high enough capability jump can eliminate low-end roles | 3-12 months to posting; 6-18 months to title standardization; 12-36 months to O*NET / BLS updates | Creation + redefinition > elimination | GPT-4 (Mar 2023) → prompt engineer postings Q2-Q3 2023; Claude 3.5 Sonnet (Jun 2024) and o1 (Sep 2024) → agentic engineer postings 2024-2025 |
| Price collapse (10× cost drop) | Elimination / consolidation of labor-substitutable roles; expansion of AI usage and therefore of AI-ops and AI-PM | 3-9 months | Elimination / consolidation > creation | GPT-4o pricing Apr 2024; Claude 3.5 Haiku (Nov 2024); DeepSeek-V3 (Dec 2024) / R1 (Jan 2025) cost shock; Gemini 2.0 Flash |
| Competitor move | Forcing function for a prominent AI hire (CAIO) or visible reorg | 1-6 months | Creation (often symbolic) | Klarna Feb 2024 → incumbents' similar public announcements; OpenAI / Anthropic hiring of CAIOs triggering CPG/financials to do the same |
| Board / investor pressure | C-suite additions (CAIO), mandated AI initiatives, headcount discipline | 1-6 months | Creation at top; elimination / freeze at bottom | Activist letters 2024-2025 at large firms; Microsoft / Amazon / Meta "year of efficiency" continuation |
| Cost-cutting initiative | Elimination / consolidation of replaceable roles; sometimes disguised as "AI-led efficiency" even when replacement is partial | 0-6 months | Elimination / consolidation > creation | Meta 2023-2024 efficiency; Google 2023 layoffs; Salesforce 2023-2024; Amazon 2023-2025; IBM 2023 back-office; BT 2023; Klarna |
| Regulatory change | Creation of governance / compliance roles; reshapes counsel, compliance, audit roles | 12-36 months | Creation > elimination | EU AI Act (final text Jul 2024; GPAI obligations Aug 2025; high-risk Aug 2026); US Exec Order 14110 Oct 2023 (rescinded 2025) required CAIOs in federal agencies; SEC AI rule moves; state-level laws (Colorado AI Act, NYC AEDT) |
| Workforce adoption plateau / "AI fluency mandate" | Silent redefinition of generalist titles | 3-12 months | Redefinition > creation | Shopify Tobi Lütke memo (Apr 2025) requiring AI-use justification; similar memos at Amazon, Duolingo (2023-2024), Procore (2024); Klarna job posting language |

**Empirical observation (confidence M)**. In 2023-2024, capability releases and cost-cutting initiatives were the dominant triggers for the highest-volume role changes; in 2024-2025 price collapse intensified (GPT-4o, Haiku 3.5, DeepSeek); in 2025-2026 regulatory change is emerging as a major trigger specifically for governance, compliance, red-team, and eval roles. Board / investor pressure acts mostly as an accelerator on top of other triggers rather than an independent cause.

---

## 6. Role life-cycle model

The synthesized life-cycle distinguishes four stages. Durations are typical ranges from 2023-2026 empirical examples; individual roles diverge widely.

**Stage 1 — Emergence (0-12 months from trigger)**. A single firm or small cluster of frontier firms posts a new title. Compensation is heterogeneous and often inflated (prompt engineer 2023: $250K-$375K base at Anthropic). Title variance across firms is high (eval engineer has at least six distinct titles). Typical output: a handful of Greenhouse / Lever postings, one or two viral essays, no textbook.

**Stage 2 — Normalization (6-24 months)**. The title spreads beyond frontier firms to the Fortune 500 adjacent tier. A curriculum begins to form (Maven courses, O'Reilly books, conference workshops). Compensation bands narrow. Job-description templates stabilize across firms. LinkedIn / Indeed / Seek show measurable title-frequency growth.

**Stage 3 — Consolidation (12-36 months)**. The role either (a) merges upward into a more senior title (prompt engineer → AI engineer), (b) merges laterally into an adjacent discipline (LLMOps engineer → platform engineer for AI), or (c) becomes a baseline expectation of an older title (PM, SWE absorb AI-PM / AI-SWE expectations). A textbook or canonical certification appears. The initial salary premium compresses.

**Stage 4 — Obsolescence or permanent role (24-60 months)**. Either the title falls off LinkedIn / Indeed frequency charts (prompt engineer 2024-2025), or it stabilizes as a permanent discipline with its own career ladder and sub-specializations (eval engineer 2025-2026; forward-deployed engineer 2024-2026; CAIO 2024-2026). Permanence is indicated by (i) a named professional organization or conference track, (ii) a recognized certification, (iii) a stable compensation band across firms.

**Typical durations observed 2023-2026**.

| Role | Emerged | Normalized | Consolidated | Current stage | Total arc length observed |
|---|---|---|---|---|---|
| Prompt engineer | Q1-Q2 2023 | Q3 2023 - Q2 2024 | Q2 2024 - Q2 2025 (absorbed into AI engineer) | Obsolescence (as standalone) | ~24-30 months to absorption |
| Forward-deployed engineer | Historically pre-2023; re-popularized 2023-2024 | 2024 | 2025-2026 | Permanent | multi-year (permanent) |
| Eval engineer | Late 2023 - 2024 | 2024-2025 | 2025-2026 | Normalization / consolidation | ~24-30 months so far |
| CAIO | 2022-2023 | 2023-2024 | 2024-2026 | Normalization plateau | ~36 months |
| AI PM | 2022-2023 | 2023-2024 | 2024-2026 (merging into PM baseline at AI-forward firms) | Consolidation / absorption | ~36 months |
| AI governance lead | 2023-2024 | 2024-2025 | 2025-2026 | Normalization (regulatory-driven) | ~24 months so far |
| Agentic engineer | 2024-2025 | 2025-2026 | 2026+ | Emergence / normalization | ~12-18 months so far |
| Vertical-AI domain lead (legal / clinical / financial) | 2023-2024 | 2024-2025 | 2025-2026 | Normalization | ~24-36 months |
| LLMOps / AI ops | 2023 | 2024-2025 | 2025-2026 (merging with platform eng) | Consolidation | ~24-30 months |

**Synthesis (confidence M)**. For AI-era knowledge-work roles, the empirical 2023-2026 lifecycle shows:
- *Time to first visible posting*: 3-6 months after triggering capability release.
- *Time to normalization (textbook, curriculum, cross-firm consistency)*: 12-24 months after first posting.
- *Time to consolidation or obsolescence*: 24-36 months after normalization, or 36-60 months after first posting, for most roles so far.
- *Survivability test*: roles with a durable accountability (customer-facing deployment for FDE; regulatory accountability for governance lead; measurable artifact for eval engineer) survive. Roles defined only by a capability gap in models (prompt engineer) absorb into senior titles as the gap closes.

**Permanent vs. transient classification (as of 2026-04)**.
- *Permanent (stable career ladder forming)*: FDE, eval engineer, CAIO, AI governance lead, AI red-teamer, vertical-AI domain lead, AI solutions architect.
- *Absorbing into older titles*: AI PM → PM; AI SWE → SWE; LLMOps → platform eng; AI curriculum lead → L&D.
- *Transient (majority absorbed, residual niche)*: prompt engineer (standalone); AI adoption analyst (bubble-prone).

---

## 7. Rebranding-vs-substance filter

Roles flagged as likely rebranding (retitle without new deliverables or filter criteria), as of 2026-04:

- **AI adoption analyst** — largely overlaps with transformation analyst or business analyst roles that pre-date the AI wave; distinguished mainly by tooling vendor-managed dashboards. Confidence of rebranding: M.
- **AI curriculum lead** — large consultancies already employed digital / data curriculum leads; AI-specific relabeling is partial. Confidence: M.
- **AI ethicist at some large firms** — where responsibilities do not include sign-off authority, training data review, or kill-switch rights, the title overlaps heavily with pre-existing compliance / policy roles. Confidence: M (varies by firm).
- **Chief AI Officer (weak form)** — where the CAIO reports to the CIO with a primarily coordination mandate and no P&L or hiring authority, the role overlaps with a senior program-management role rebranded. Confidence: H for a subset of CAIOs, L for the flagship CAIOs (JPMorgan, Mastercard, Accenture).
- **AI solutions architect at system integrators** — often a retitled solutions architect with added AI collateral. Confidence: M.
- **Prompt engineer in late 2024-2025 at non-frontier firms** — some postings late in the life cycle were cosmetic retitles of technical writer or QA tester roles. Confidence: L-M (spotty evidence).

Roles flagged as substantive (survive the filter):
- **Forward-deployed engineer** — distinct deliverable (customer-specific agent / pipeline), distinct reporting line (often to CTO or VP of Solutions), distinct hiring filter (full-stack + customer-facing + ML). Structural. Confidence: H.
- **Eval engineer** — distinct artifact (eval harness, rubric, LLM-as-judge setup, regression pipeline), distinct tooling stack (Braintrust / LangSmith / Arize / Galileo / custom), distinct hiring filter. Structural. Confidence: H.
- **AI governance lead** under EU AI Act compliance — mandated sign-off authority, incident reporting, regulator-facing role. Structural. Confidence: H.
- **Agentic engineer** — distinct scaffolding, tool-use patterns, failure modes (tool-use loop, context-window management, memory). Structural. Confidence: M-H.
- **CAIO (strong form)** — when holding direct authority over AI strategy, data, and infrastructure across business units; JPMorgan's Heitsenrether is the flagship case. Structural. Confidence: H for flagship cases.

---

## 8. Open questions and negative evidence

**Open questions**.
1. *What fraction of CAIOs are rebranded CIO / CDO vs. substantive net-new roles?* Reliable longitudinal data is not public. Spencer Stuart / Heidrick reports are fee-gated; IBM and PwC surveys report different shares depending on definition.
2. *How much of the 2023-2024 prompt-engineer decline was absorbed vs. eliminated?* Job-title frequency fell sharply but it is unclear how much of the underlying work continued under other titles. Anthropic, OpenAI and Scale all have postings that are "AI engineer" but with prompt-engineering-like scopes.
3. *Did the Klarna narrative hold?* Klarna's 2024 claim of AI replacing 700 FTE was widely cited; 2025 coverage reported partial rehiring of human customer-service roles. The net structural change remains contested.
4. *Has the junior-SWE pipeline permanently narrowed or temporarily?* 2024-2026 reduced hiring could reflect macro cost pressure plus AI; the AI-only attribution is unresolved. Eloundou-Manning et al. provide exposure estimates but not displacement measurements.
5. *How quickly will agentic engineer consolidate?* The role is young enough (≤24 months visible) that its life-cycle trajectory is not determinable.
6. *Regulatory-triggered roles post-Aug 2026* — the EU AI Act high-risk obligations kick in August 2026. The volume of governance/compliance roles that obligation will generate is [post-cutoff; flagged; projected].

**Negative evidence (actively searched, not found)**.
1. No credible public dataset tracks "role redefinition frequency per 1000 FTE per year" at firm level. This is a known gap for M2.
2. No consistent BLS / O*NET taxonomy update has yet canonicalized "eval engineer," "agentic engineer," or "forward-deployed engineer." O*NET updates are typically 18-36 months behind labor-market changes; SOC code revisions cycle every ~5 years.
3. LinkedIn Economic Graph has published fragmentary job-title trend data (2023-2025 reports on AI-related titles) but has not released a full time-series with consistent methodology suitable for longitudinal analysis.
4. Ravio / Pave / Levels.fyi track compensation, not role creation; their datasets are good for Stage-2 / Stage-3 signals (compensation band narrowing) but not for Stage-1 emergence detection.
5. No published academic longitudinal study directly tests a role-life-cycle model for AI-era roles; studies tend to treat individual waves (Eloundou-Manning exposure, Felten-Raj-Seamans exposure, Brynjolfsson-Li-Raymond productivity) without a unified life-cycle framework.
6. Challenger/Gray/Christmas tallies of AI-attributed layoffs are subject to firm-reported attribution bias; the true AI-attributable share is likely different from the reported share in either direction.

---

## 9. Feedback to three-pillar adaptability frame

- **Role life-cycle duration is a measurable adaptability proxy**. The 2023-2026 evidence suggests a ~24-36 month envelope from role-emergence to consolidation or obsolescence for the most AI-specific new titles. This is faster than the ~5-7 year cycle for SOC code / O*NET revisions — i.e., formal labor taxonomies are institutionally lagging behind the Pillar 2 adaptability clock by approximately a factor of two to three. Feeds M1 (delays) and M2 (indicator design).
- **Triggers are asymmetric in the kind of change they produce**. Capability releases predominantly create and redefine roles (expansion); price collapses predominantly eliminate and consolidate (contraction); regulatory change predominantly creates (governance layer). Any adaptability indicator that treats "role change" as a single number conflates incompatible mechanisms and mis-scores firms whose adaptations are trigger-specific.
- **Silent redefinition is the dominant adaptation channel at incumbents**. An organization can look static at the title level while having reshaped filtering criteria, promotion standards, and daily deliverables across its entire knowledge-worker base. Pillar 2 adaptability cannot be measured by titles alone; it requires a deeper signal (hiring-criteria text, promotion-rubric text, job-description text at the clause level). This is a design constraint for M2.
- **The structural-vs-rebranding distinction is load-bearing**. Firms that produce many new titles without new reporting lines, new accountability, or new deliverables are performing adaptability theater. A rebranding-heavy firm and a substance-heavy firm will score identically on a naive title-count metric and differently on a structural metric. Feeds O1 (PR-vs-substance filter) and M2.
- **Regulated-domain roles behave differently from unregulated**. Governance leads, AI red-teamers, and compliance-AI roles emerge on regulatory-deadline timing (EU AI Act Aug 2025 / Aug 2026), not on capability-release timing. This is a distinct dynamic that the adaptability frame should surface as a separate curve — "regulatory-pull role creation" versus "capability-push role creation." Connects to the healthcare-bio-ai extension and to any sector where regulatory timelines dominate capability timelines.
- **Role-life-cycle concentration is a warning signal, not a health signal**. A firm that just stood up a CAIO plus six flanking AI roles in 2024-2025 is either genuinely adapting (and will show downstream P&L / productivity effects) or is performing the AI-announcement ritual (and will show the same titles quietly merged back into existing functions by 2027-2028). The adaptability frame should include a forward predictor — which Stage-1 / Stage-2 roles are likely to survive to Stage-3 — rather than only a backward count.
