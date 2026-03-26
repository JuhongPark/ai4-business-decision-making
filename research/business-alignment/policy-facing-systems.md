# Policy-Facing and Customer-Facing AI Systems

status: draft
date: 2026-03-25
purpose: define why policy-facing and customer-facing AI systems need stricter grounding and governance than ordinary internal support tools

## Why This Note Exists

One of the clearest findings from the repository's incident work is that LLM systems create a distinct communication and policy risk.

The issue is not only whether the output is factually wrong.

It is whether the system is treated as if it were authorized to represent:

- company policy
- customer commitments
- hiring communications
- compliance guidance
- legal or HR boundaries

When this happens, the firm's alignment problem becomes sharper.

## Core Claim

**Policy-facing and customer-facing AI systems should not be governed like general internal copilots.**

They require:

- narrower scope
- stronger grounding in approved sources
- clearer refusal and escalation behavior
- stronger change-management rules
- more explicit logging and accountability

## Evidence Base

### 1. Repository incident logic

Evidence strength: strong within the study design

The incident synthesis shows recurring failure patterns:

- firms trust fluent outputs without independent verification
- human review is often nominal rather than structurally strong
- LLMs can create legal and reputational exposure when their outputs are treated as company speech
- vendor procurement does not remove the firm's accountability

Interpretation:

These patterns justify treating policy-facing systems as a separate governance class.

### 2. Current public-sector and enterprise governance signals

Evidence strength: strong

- The White House announced on April 7, 2025 that OMB had released M-25-21 and M-25-22, two revised policies on federal agency AI use and procurement. The related memoranda are dated April 3, 2025.
- M-25-21 focuses on AI use through innovation, governance, and public trust.
- M-25-22 focuses on acquiring effective and trustworthy AI capabilities responsibly.
- Microsoft's Supplier Security and Privacy Assurance program states that suppliers working with personal data, confidential data, or AI systems are in scope, that work cannot begin until compliance is complete for new suppliers, and that suppliers may be selected for independent assurance.

Interpretation:

Institutional buyers increasingly expect AI systems that affect decision-making or communications to operate inside explicit governance boundaries. This is especially relevant when a system could be interpreted as speaking or acting on behalf of the organization.

## What Makes These Systems Different

### 1. They create representation risk

A policy-facing or customer-facing system does not merely generate text.

It can be interpreted as:

- an authorized company answer
- a statement of policy
- a commitment to a customer
- a signal about hiring or eligibility
- a compliance instruction

### 2. They invite over-trust through fluency

LLMs explain, persuade, and maintain conversational flow.

That makes it easy for users to confuse:

- confident language with policy certainty
- smooth conversation with authorized guidance
- plausible paraphrase with official rule content

### 3. They fail asymmetrically

A small number of bad outputs can create outsized damage through:

- customer compensation
- public backlash
- regulator attention
- employment claims
- internal policy confusion

### 4. They degrade quickly when change management is weak

Even a well-grounded system can drift out of alignment if:

- policies change but the knowledge base is outdated
- escalation logic is unclear
- owners do not review edge cases
- prompt or workflow changes are made informally

## System Types

### Type A: Company-policy assistants

Examples:

- employee policy Q&A
- HR guidance assistants
- internal compliance and process assistants

Default rule:

- grounded assist only

Why:

- ambiguous cases often require interpretation, exception handling, and escalation rather than free-form response generation

### Type B: Customer-facing assistants

Examples:

- support chatbots
- self-service return or refund guidance
- billing or account policy explanations

Default rule:

- grounded assist or tightly governed recommend

Why:

- the system can create de facto commitments to customers

### Type C: Decision-adjacent communication systems

Examples:

- hiring communications
- underwriting explanation tools
- claims or eligibility notifications

Default rule:

- assist only unless the workflow has strong legal, fairness, and review controls

Why:

- these systems affect rights-sensitive outcomes and can create strong reliance by affected people

## Governance Requirements

### 1. Grounding in approved sources

Minimum requirement:

- responses should be tied to approved policy or knowledge repositories

High-priority controls:

- source restriction
- citation or traceability
- knowledge freshness checks
- no-answer behavior when sources are missing

### 2. Narrow response scope

The system should answer only within approved boundaries.

Examples:

- answer the policy question but do not improvise exceptions
- explain a documented refund policy but do not create new commitments
- summarize an approved rule but do not give legal advice

### 3. Refusal and escalation behavior

The system should escalate when:

- the policy source is unclear
- the case appears novel or exceptional
- the answer could affect eligibility, rights, or contractual commitments
- the system lacks confidence or source coverage

### 4. Separation of generation and approval

Where the output carries policy significance, review should not happen as a quick in-chat acknowledgment.

Stronger options include:

- structured approval templates
- human sign-off outside the conversational interface
- audit logs of source retrieval and final response

### 5. Change management

Whenever policy changes, the organization should know:

- who updates the knowledge source
- when the deployment is refreshed
- which prompts or templates changed
- what testing occurred before release

## Practical Governance Matrix

| System type | Default role | Main failure mode | Required controls | Escalation threshold |
| --- | --- | --- | --- | --- |
| Internal policy assistant | grounded assist | policy improvisation | source restriction, freshness checks, citation, escalation | medium |
| Customer support assistant | grounded assist or tightly governed recommend | unintended commitments | narrow scope, template controls, monitoring, human handoff | medium to high |
| HR or hiring communication assistant | assist | fairness and representation risk | approved content only, legal review, logging, escalation | high |
| Compliance guidance assistant | assist | unauthorized interpretation | approved sources, strict boundary control, audit trail | high |
| Public-facing FAQ agent | grounded assist | reputational and policy drift | source traceability, monitoring, rollback path | medium |

## Bottom Line

Inference from the evidence:

Policy-facing and customer-facing systems should be treated less like open-ended assistants and more like bounded organizational interfaces.

The governing question is not:

- "Can the model answer fluently?"

It is:

- "Can the organization justify letting this system represent policy under real conditions of ambiguity, change, and accountability?"

## Sources

- `research/business-alignment/incidents/implications-and-immediate-company-needs.md`
- `research/business-alignment/business-implications-and-immediate-needs.md`
- White House, "White House Releases New Policies on Federal Agency AI Use and Procurement," April 7, 2025. https://www.whitehouse.gov/articles/2025/04/white-house-releases-new-policies-on-federal-agency-ai-use-and-procurement/
- White House OMB memorandum listing, including M-25-21 and M-25-22 dated April 3, 2025. https://www.whitehouse.gov/omb/information-resources/guidance/memoranda/
- White House, M-25-22, "Driving Efficient Acquisition of Artificial Intelligence in Government," April 3, 2025. https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-22-Driving-Efficient-Acquisition-of-Artificial-Intelligence-in-Government.pdf
- Microsoft Procurement, "Supplier Security & Privacy Assurance Program." https://www.microsoft.com/en-us/procurement/sspa
