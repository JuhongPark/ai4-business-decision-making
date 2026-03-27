# Visual Diagrams

status: completed
purpose: Provide visual representations of the core analytical framework, decision logic, and domain comparison from the thinktank report.

## 1. Seven-Step AI Authority Decision Sequence

```mermaid
flowchart TD
    S1[1. Classify domain] --> S2[2. Classify decision structure]
    S2 --> S3[3. Classify risk level]
    S3 --> S4[4. Classify scenario condition]
    S4 --> S5[5. Check evidence strength]
    S5 --> S6[6. Check governance readiness]
    S6 --> S7[7. Assign lowest justified AI authority]
    S7 --> OUT1[assist]
    S7 --> OUT2[recommend]
    S7 --> OUT3[automate with guardrails]

    style S7 fill:#e8e8e8,stroke:#333
    style OUT1 fill:#c8e6c9,stroke:#2e7d32
    style OUT2 fill:#fff9c4,stroke:#f9a825
    style OUT3 fill:#ffcdd2,stroke:#c62828
```

## 2. AI Role Spectrum with Escalation and Fallback

```mermaid
flowchart LR
    A[assist] -->|escalation: stronger evidence,<br>stable conditions,<br>governance ready| B[recommend]
    B -->|escalation: structured task,<br>low risk,<br>measurable outcomes| C[automate with guardrails]
    C -->|fallback: drift detected,<br>stress condition,<br>data degradation| B
    B -->|fallback: edge case,<br>fairness concern,<br>incomplete information| A

    style A fill:#c8e6c9,stroke:#2e7d32
    style B fill:#fff9c4,stroke:#f9a825
    style C fill:#ffcdd2,stroke:#c62828
```

## 3. Domain Positioning by Risk and Automation Suitability

```mermaid
quadrantChart
    title Domain Positioning: Risk Level vs Automation Suitability
    x-axis Low Risk --> High Risk
    y-axis Low Automation Suitability --> High Automation Suitability
    quadrant-1 Governance-heavy automation
    quadrant-2 Bounded automation zone
    quadrant-3 Augmentation zone
    quadrant-4 Restriction zone
    Operations: [0.25, 0.85]
    Marketing: [0.35, 0.70]
    Product: [0.40, 0.45]
    Market Research: [0.30, 0.40]
    Strategy: [0.50, 0.25]
    Finance: [0.75, 0.50]
    Investment: [0.70, 0.40]
    Healthcare: [0.85, 0.35]
```

## 4. Scenario-Dependent Authority Shift

```mermaid
flowchart TD
    subgraph Baseline
        B_OPS[Operations:<br>automate with guardrails]
        B_FIN[Finance:<br>assist / recommend]
        B_HC[Healthcare:<br>assist / recommend]
    end

    subgraph Stress
        S_OPS[Operations:<br>recommend / automate]
        S_FIN[Finance:<br>assist]
        S_HC[Healthcare:<br>recommend]
    end

    subgraph Edge Case
        E_OPS[Operations:<br>assist]
        E_FIN[Finance:<br>assist]
        E_HC[Healthcare:<br>assist]
    end

    B_OPS -->|stress trigger| S_OPS
    B_FIN -->|stress trigger| S_FIN
    B_HC -->|stress trigger| S_HC

    S_OPS -->|edge case trigger| E_OPS
    S_FIN -->|edge case trigger| E_FIN
    S_HC -->|edge case trigger| E_HC

    style B_OPS fill:#ffcdd2
    style S_OPS fill:#fff9c4
    style E_OPS fill:#c8e6c9
    style B_FIN fill:#fff9c4
    style S_FIN fill:#c8e6c9
    style E_FIN fill:#c8e6c9
    style B_HC fill:#fff9c4
    style S_HC fill:#fff9c4
    style E_HC fill:#c8e6c9
```

## 5. Six-Part Category Taxonomy

```mermaid
flowchart LR
    subgraph Taxonomy
        D[Domain] --> DS[Decision Structure]
        DS --> RL[Risk Level]
        RL --> SC[Scenario Condition]
        SC --> AR[AI Role]
        AR --> ES[Evidence Strength]
    end

    D ---|operations, finance,<br>healthcare, strategy,<br>product, marketing,<br>investment, market research| DS
    DS ---|structured,<br>semi-structured,<br>unstructured| RL
    RL ---|low, medium, high| SC
    SC ---|baseline, stress,<br>edge case| AR
    AR ---|assist, recommend,<br>automate with guardrails| ES
    ES ---|strong, moderate,<br>design logic| OUT[Authority Assignment]

    style OUT fill:#e8e8e8,stroke:#333
```

## 6. Business-Context AI Alignment Layers

```mermaid
flowchart TB
    L1[Problem Alignment<br>Is the right problem being solved?] --> L2[Authority Alignment<br>What level of AI delegation is justified?]
    L2 --> L3[Trust Alignment<br>Is trust calibrated, not blind?]
    L3 --> L4[Validation Alignment<br>Can outputs be substantively reviewed?]
    L4 --> L5[Policy Alignment<br>Is the system grounded in approved sources?]
    L5 --> L6[Commercial Alignment<br>Is the system deployable, insurable, procurable?]

    style L1 fill:#e3f2fd,stroke:#1565c0
    style L2 fill:#e8f5e9,stroke:#2e7d32
    style L3 fill:#fff3e0,stroke:#e65100
    style L4 fill:#fce4ec,stroke:#c62828
    style L5 fill:#f3e5f5,stroke:#7b1fa2
    style L6 fill:#e0f2f1,stroke:#00695c
```

## Rendering Note

These diagrams use Mermaid syntax. They render natively in GitHub, GitLab, VS Code (with Mermaid extension), Obsidian, and most modern markdown viewers. For PDF or print output, use a Mermaid CLI tool or online renderer.
