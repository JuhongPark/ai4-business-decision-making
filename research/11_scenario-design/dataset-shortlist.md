# Phase 11: Dataset Shortlist

status: completed
purpose: Identify public datasets and official scenario sources suitable for the first scenario-based study.

## Recommended First-Wave Domains

1. operations
2. finance
3. healthcare

## Operations

### Primary Dataset

dataset: NYC TLC Trip Record Data
use_case: routing, demand variation, dispatch pressure, trip volume shocks
why_useful: high-volume operational decisions with measurable outcomes
source: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
evidence_strength: official public administrative data

### Scenario Ideas

- normal demand day
- peak demand surge
- disruption from congestion or vehicle shortage

## Finance

### Primary Dataset

dataset: HMDA
use_case: credit access, approval patterns, fairness-sensitive lending analysis
why_useful: large-scale official lending data for high-stakes financial decisions
source: https://www.consumerfinance.gov/data-research/hmda/
evidence_strength: official regulatory dataset

### Scenario Source

scenario_source: Federal Reserve supervisory stress test scenarios
use_case: macroeconomic shock construction for adverse credit conditions
source: https://www.federalreserve.gov/publications/2026-stress-test-scenarios.htm
evidence_strength: official regulatory scenario source

### Scenario Ideas

- baseline lending condition
- adverse macro downturn
- severe stress or tightening risk condition

## Healthcare

### Primary Dataset

dataset: MIMIC-IV
use_case: triage, deterioration risk, clinical support, patient pathway analysis
why_useful: rich clinical dataset for decision-support research
source: https://physionet.org/content/mimiciv/
evidence_strength: established research dataset with controlled access

### Regulatory Context

context_source: FDA AI in Software as a Medical Device
use_case: defining safety and governance constraints for healthcare AI scenarios
source: https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-software-medical-device
evidence_strength: official regulatory guidance

### Scenario Ideas

- routine triage support
- high-acuity patient surge
- edge case with uncertain or incomplete information

## Optional Second-Wave Datasets

### Marketing

dataset: Online Retail II
source: https://archive.ics.uci.edu/dataset/502/online+retail+ii
use_case: demand response, customer targeting, retention scenarios

### Investment

dataset: SEC and Investor.gov robo-adviser guidance plus public market data
source: https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-45
use_case: advisory logic, disclosure, and investor suitability scenarios

## Selection Recommendation

The first implementation should start with NYC TLC, HMDA plus Fed scenarios, and MIMIC-IV because together they provide:

- one lower-risk operational environment
- one high-stakes financial environment
- one safety-critical healthcare environment
