# Operations Scenario Pack

status: completed
domain: operations
dataset_anchor: NYC TLC Trip Record Data
recommended_default_mode: automate with guardrails

## Scenario O1

scenario_id: O1
scenario_class: baseline
ai_role_focus: assist vs recommend vs automate

### Business Context

A high-volume dispatch environment must allocate trips efficiently under stable demand conditions.

### Triggering Condition

Normal weekday demand with predictable trip volume and no major disruption.

### Decision Required

How should dispatching, routing, and resource allocation be managed to maintain speed and utilization?

### Available Data

- historical trip demand
- pickup and dropoff patterns
- time-of-day volume
- route duration estimates

### Mode Comparison

- `human-only`: slower but flexible decision updates
- `AI assist`: improved visibility and load balancing support
- `AI recommend`: stronger consistency and better route suggestions
- `AI automate with guardrails`: strongest efficiency under bounded operating rules

### Preferred Mode

automate with guardrails

### Why

The environment is repeated, measurable, and feedback-rich. Under stable conditions, higher autonomy is defensible if escalation paths exist for exceptions.

## Scenario O2

scenario_id: O2
scenario_class: stress
ai_role_focus: automation under surge

### Business Context

Demand spikes during peak hours while vehicle capacity remains constrained.

### Triggering Condition

Unexpected trip surge, congestion buildup, and delayed service windows.

### Decision Required

How should dispatch priorities and routing logic change under demand pressure?

### Available Data

- live demand intensity
- congestion indicators
- fleet availability
- trip completion lag

### Mode Comparison

- `human-only`: adaptable but too slow at scale
- `AI assist`: useful for situational awareness
- `AI recommend`: strong option if supervisors retain override authority
- `AI automate with guardrails`: effective if service thresholds and escalation triggers are predefined

### Preferred Mode

recommend or automate with guardrails

### Why

Speed becomes more important under stress, but human override remains necessary when local optimization may conflict with broader service goals.

## Scenario O3

scenario_id: O3
scenario_class: edge_case
ai_role_focus: exception handling

### Business Context

The system encounters a compound disruption with data instability and service anomalies.

### Triggering Condition

Vehicle shortage, incomplete telemetry, and localized network disruption.

### Decision Required

Should routing and dispatch remain automated, or should the system fall back to human-led control?

### Available Data

- partial trip data
- incomplete fleet status
- degraded traffic signal quality

### Mode Comparison

- `human-only`: best for improvised exception handling
- `AI assist`: useful for partial prioritization support
- `AI recommend`: acceptable only if confidence is transparent
- `AI automate with guardrails`: too risky if inputs are unstable

### Preferred Mode

assist

### Why

When the data substrate degrades, the justification for automation weakens quickly. Exception-heavy operations need human-led recovery.

## Domain Takeaway

Operations is the clearest domain for bounded automation, but only while decision structure and data quality remain stable. Under edge-case conditions, the preferred mode shifts back toward assist.
