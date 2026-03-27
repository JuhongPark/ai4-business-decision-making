# Repository Organization Note

date: 2026-03-27
status: active
scope: research workspace structure and navigation policy

## Purpose

This note records the rationale for the current repository organization so the structure remains understandable, durable, and auditable over time.

## Why The Repository Was Reorganized

The earlier repository had become difficult to navigate because foundational research, polished outputs, extension tracks, and process artifacts all competed at the same level under `research/`. That made it harder to identify:

- which documents were canonical
- which documents were supporting reference material
- which documents were still process or revision artifacts
- where new work should be placed

The current zone model was introduced to separate those roles explicitly.

## Zone Model

### `core/`

Stable analytical building blocks:

- planning
- questions
- literature
- cases
- framework
- drafting
- evidence
- domain analysis
- scenario design
- scenario packs
- taxonomy

### `delivery/`

Reader-facing and submission-facing outputs:

- report outputs
- publication support materials
- submission-ready artifacts
- validation pass records

### `operations/`

Process and governance artifacts:

- application materials
- program planning
- revision materials
- expansion planning
- repository-organization reviews

### `extensions/`

Follow-on workstreams that extend the core thesis:

- adaptive governance
- information structure
- business alignment
- three-part study

## Canonical vs Supporting Material

The repository now follows this navigation rule:

- canonical documents should be promoted from folder and track READMEs
- supporting reference material should remain discoverable but visually secondary
- review files, raw scans, and scouting notes should not sit on the main narrative path unless they are part of the canonical workflow for that folder

## Naming Rules

- Prefer context-rich filenames over generic names like `plan.md` or `summary.md`.
- Prefix review files by phase, zone, or target when parallel review sets exist.
- Reserve plain `README.md` names for folder guides.
- New subareas that may accumulate multiple documents should start with a local `README.md` that states scope and boundary rules.

## Exception Policy

The repository default is English-language research content.

Exception:

- explicitly marked bilingual legacy scouting notes may remain in reference-only clusters
- these notes are supporting references, not canonical outputs
- they should not be promoted as primary repository outputs unless normalized into the repository's standard English presentation

At the time of this note, the main exception cluster is:

- [extensions/business-alignment/alignment-ecosystem/README.md](extensions/business-alignment/alignment-ecosystem/README.md)

## Change Control

Future structural changes should update:

1. [README.md](../README.md)
2. [README.md](README.md)
3. Any affected zone or track guide
4. This note when the organizing policy itself changes
