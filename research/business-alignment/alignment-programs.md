# AI Alignment — Programs, Fellowships, and Organizations

AI 정렬/안전 분야에서 연구 기회를 제공하는 프로그램, 교육 부트캠프, 거버넌스 조직을 정리한다. 어디서 연구 경험을 쌓을 수 있는지, 어떤 조직이 이 분야를 이끌고 있는지 파악하는 것이 목적이다.

코드 레포는 [alignment-codebases.md](alignment-codebases.md), 80,000 Hours 데이터셋 분석은 [ai-safety-fellowships-directory.md](ai-safety-fellowships-directory.md) 참조.

> **Sourcing:** 프로그램 통계(출판 수, 배출처, 코호트 규모)는 각 프로그램 웹사이트에서 가져왔다. 자기보고 수치이며 독립 검증된 것은 아니다. 2026-03-26 기준.

---

## Research Fellowships — 정렬 연구를 직접 수행할 수 있는 기회

### MATS (ML Alignment Theory Scholars)

- **Site:** https://www.matsprogram.org/
- **Format:** 12주, 대면 (Berkeley / London)
- **규모:** 170+ 출판물, 9,500+ 인용 (자기보고)
- **연구 트랙:** Empirical, Policy & Strategy, Theory, Technical Governance, Compute Infrastructure
- **멘토 조직:** Anthropic, DeepMind, OpenAI, Redwood Research, ARC, UK AISI, LawZero
- **배출처 (자기보고):** 80%가 AI 정렬/보안 분야 취업, 10%가 조직 설립 (Apollo Research, Timaeus, Center for AI Policy)
- **주요 연구 성과:** Sparse autoencoders, activation engineering, developmental interpretability, situational awareness evaluation
- **코드:** qfeuilla/BehaviorEliciationTool (자동 레드팀)
- **Summer 2026:** 최대 코호트 — 120 fellows, 100 mentors

**활용:** 정렬 연구 경력의 가장 확립된 진입점. 멘토 매칭을 통해 Anthropic/DeepMind급 연구에 참여할 수 있다.

### SPAR (Supervised Program for Alignment Research)

- **Site:** https://sparai.org/
- **Format:** 파트타임 원격, 5–40시간/주, 3개월
- **운영:** Kairos AI Project, Inc. (501(c)(3))
- **규모:** Spring 2026에 130+ 프로젝트 — AI 안전 펠로우십 중 최대 규모
- **멘토:** 130+명 (Dawn Song, Dylan Hadfield-Menell 포함)
- **분야:** AI Safety, AI Policy, AI Security, Interpretability, Biosecurity, Societal Impacts
- **성과:** NeurIPS 2024, ICML 2025 논문; TIME 보도; Google AI Safety 취업

**활용:** 풀타임이 아니어도 참여 가능하며, 프로젝트 리스트(sparai.org/projects)에서 현재 진행 중인 정렬 연구 주제를 파악할 수 있다.

**Spring 2026 주목할 프로젝트:**

Misalignment 탐지:
- Representation Engineering으로 에이전트 misalignment 사전 탐지 (Dawn Song, UC Berkeley)
- Instruction-Following과 전략적 은폐의 분리 (MATS)
- 다중 모델 상호작용에서의 emergent misalignment (LawZero)
- Shutdown-Bench: 종료가능성 평가 (Elliott Thornley, MIT)

Mechanistic Interpretability:
- SAE를 위한 Sparse Geometry와 Formal Verification
- Temporal Crosscoders — 추론 모델용 새 SAE 아키텍처 (MATS)
- 에이전트를 활용한 회로 해석 자동화

Safety Evaluation:
- LLM 에이전트 대상 적대적 레드팀 프레임워크 (Dawn Song, UC Berkeley)
- AI 안전을 위한 Jailbreak — 고성능 시스템 감사 공격 (Oxford/Anthropic)

### LASR Labs (London AI Safety Research Labs)

- **Site:** https://www.lasrlabs.org/
- **Format:** 13주 여름 프로그램 (7–10월), 3–4명 팀 + 연구자 감독
- **Stipend:** £11,000 + 사무실, 식사, 교통
- **분야:** 다중 에이전트 공모, RL 정렬 이론, 기만 탐지, 해석가능성, scalable oversight, AI control
- **성과 (자기보고):** 2024 코호트 NeurIPS 워크숍 100% 채택 (워크숍 수락률은 본 학회보다 높음에 유의); UK AISI, Apollo Research, Open Philanthropy 취업

**활용:** 논문 수준의 연구를 팀으로 수행할 수 있는 기회. 13주 후 출판 가능한 결과물이 나온다.

### Apart Research

- **Site:** https://apartresearch.com/fellowships
- **프로그램:**
  - **Apart Fellowship** (12–24주, 10–30시간/주, 원격) — 해커톤 아이디어를 출판 연구로 발전
  - **Partnered Fellowships** (~16주) — 파트너 조직의 연구 어젠다에 참여
- **분야:** 모델 평가, 해석가능성, 멀티에이전트, AI 보안, formal methods, 기만 탐지
- **진입:** 매월 Research Sprint에서 성과 기반 선발 — 고정 코호트가 아니라 상시 파이프라인

**활용:** 수시 지원 가능한 유일한 연구 펠로우십. Sprint 참여로 역량을 증명하면 Fellowship으로 이어진다.

---

## Training & Bootcamps — 정렬 연구에 필요한 기초 역량을 쌓을 수 있는 기회

### ARENA (Alignment Research Engineer Accelerator)

- **Site:** https://www.arena.education/
- **Format:** 4–5주 대면 부트캠프 (London), 연 2–3회; 전액 지원 (교통, 비자, 숙박, 식사)
- **내용:** AI 안전 엔지니어링 — Python, 선형대수, 확률
- **커리큘럼:** 온라인 무료 공개 — 독립 학습이나 자체 교육 과정 설계에 활용 가능
- **배출처:** Anthropic, Apollo Research, METR; MATS와 LASR 참여

**활용:** 커리큘럼이 공개되어 있어 부트캠프에 참석하지 않아도 자료를 활용할 수 있다.

### BlueDot Impact

- **Site:** https://bluedot.org/
- **Format:** 무료 AI 코스 (pay-what-you-want), 커리어 지원, 창업 가속, 글로벌 이벤트
- **규모:** 2022년 이후 5,000+ 전문가 교육; £35M 조달; 6,000+ alumni
- **코스:**
  - **Technical AI Safety** (30시간, 코호트) — 안전 기법, threat modeling, kill chain analysis. LLM/파인튜닝 기초 필요.
  - **AI Governance** (25시간, 코호트) — 거버넌스 현황, 주요 제안, 정책 커리어. 2026년 재개.
  - **AI Governance Fast-Track** (5일 집중) — 거버넌스/정책 기초 속성.
  - **Future of AI** (2시간, 셀프페이스, 무료) — 전제조건 없음. AI 역량과 위험 입문.
- **배출처:** OpenAI, Anthropic, Google DeepMind, AI Security Institute, UN, NATO, OECD, Stanford HAI

**활용:** 정렬 분야에 처음 진입하는 사람에게 가장 접근성이 좋은 코스. Future of AI(2시간)로 시작할 수 있다.

### ML4Good

- **Site:** https://ml4good.org/
- **Format:** 무료 8일 합숙 부트캠프, 두 트랙:
  - **Technical** — ML 엔지니어, CS 졸업생, 기술 연구자 대상
  - **Governance & Strategy** — 정책/법률, 운영, 커뮤니케이션 전문가 대상
- **비용:** 전액 무료 (식사, 숙박, 교육 제공; 교통비 환급)
- **배출처 (자기보고):** MATS Research, Ada Lovelace Institute, UK AISI, SaferAI, CHAI; 98% 추천율

**활용:** 기술 트랙과 거버넌스 트랙이 분리되어 있어 배경에 맞는 진입이 가능하다.

---

## AI Governance Organizations — 정책 연구와 펠로우십을 제공하는 조직

### GovAI (Centre for the Governance of AI)

- **Site:** https://www.governance.ai/
- **구조:** US 501(c)(3) + UK 자회사
- **연구 주제:** 데이터센터 인프라 정책, 중국 AI 전략, 이중용도 생물학적 역량, AI 에이전트 인프라에서의 정부 역할
- **프로그램:**
  - **Summer Fellowship — Research Track** (3개월, 6–8월, London) — GovAI 감독 하 독립 연구, £12,000 스티펜드
  - **Summer Fellowship — Applied Track** (3개월, 6–8월, London) — 비연구 프로젝트 (커뮤니케이션, 정책 참여, 이벤트), £12,000 스티펜드
  - **DC Summer Fellowship** (3개월, DC) — 미국 AI 거버넌스/정책, 초당파 참여
  - **Research Scholar** (1년) — 정책/사회과학/기술 연구
  - **Research Fellow** (2년, 갱신 가능) — 시니어 독립 연구직

**활용:** AI 거버넌스 분야에서 가장 확립된 연구 조직. 여기 출판물(governance.ai/research)에서 최신 거버넌스 논의를 추적할 수 있다.

### IAPS (Institute for AI Policy and Strategy)

- **Site:** https://www.iaps.ai/fellowship
- **유형:** 초당파 싱크탱크 — AI, 국가안보, 지정학 교차점의 정책 연구
- **AI Policy Fellowship 2026:** 3개월 (6–8월), DC 2주 필수 거주
  - Senior Fellows: $22,000; Fellows: $15,000
  - 코호트 ~30명
  - 산출물: 정책 브리프, 정부 브리핑, 컨퍼런스, 기고문
  - 기술 전문성 불요

**활용:** 기술 배경 없이도 AI 정책 연구에 진입할 수 있는 드문 기회.

### Orion AI Governance Initiative

- **Site:** https://www.orionaigov.org/
- **기반:** UK, AI 거버넌스 인재 양성
- **프로그램:**
  - **AI Policy Accelerator** — 5주 교육 (주 4시간: 강의, 워크숍, 게스트 스피커) + 4주 연구 프로젝트 (주 10시간). Compute governance, model evaluations, 국제 AI 거버넌스. 석사/학부 졸업 예정자 대상.
  - **Internship** — 여름 ~3개월, £3,200/월. 싱크탱크/거버넌스 조직 배치 (2025: Safe AI Forum, Social Market Foundation).
  - **Mentorship Programme** — GovAI, RAND, Ada Lovelace Institute, 프론티어 AI 랩 정책팀 전문가와 1:1 매칭.

**활용:** 짧은 기간(5주+4주)에 AI 거버넌스 연구 경험을 쌓을 수 있어 학기 중에도 병행 가능하다.

---

## Pipeline Map — 정렬 분야 진입 경로

실제 커리어 경로는 비선형적이며 아래는 프로그램 간 관계를 단순화한 것이다.

```
진입 (전제조건 없음)
  → BlueDot Future of AI (2시간)
  → ML4Good bootcamp (8일)

기초 (기술/정책 배경 있음)
  → BlueDot Technical AI Safety / AI Governance (25-30시간)
  → ARENA bootcamp (4-5주)
  → Orion Accelerator (5주 + 4주 연구)

연구 (역량 입증)
  → SPAR (3개월 파트타임, 원격)
  → Apart Research Sprints → Fellowship
  → LASR Labs (13주, London)
  → MATS (12주, Berkeley/London)
  → Anthropic Fellows (2-6개월, SF)

거버넌스 트랙
  → GovAI Fellowship (3개월, London/DC, £12k)
  → IAPS Fellowship (3개월, DC, $15-22k)
  → RAND CAST Fellows (상시)

커리어 목적지
  → Anthropic, DeepMind, OpenAI, UK AISI
  → Apollo Research, Redwood Research, METR
  → GovAI, RAND, CNAS, 정부 기관
```

---

## 이 자료와 비즈니스 정렬 연구의 연결

1. **연구 펠로우십** (MATS, SPAR, LASR)에서 나오는 기법(activation engineering, deception detection 등)은 향후 기업용 안전 도구의 기반이 될 수 있다.
2. **교육 프로그램** (BlueDot, ARENA, ML4Good)은 AI 안전 인재풀의 주요 공급원이다. 채용 시 이 프로그램 출신 여부가 시그널이 된다.
3. **거버넌스 조직** (GovAI, IAPS, Orion)의 정책 연구가 규제 프레임워크에 영향을 줄 수 있다. GovAI의 연구는 UK/EU 정책 논의에서 인용된 바 있다.
4. **파이프라인 구조** 자체가 정렬이 전문 직업 분야로 성장하고 있음을 보여준다. 기업 내 AI 거버넌스 팀 구성 시 참고할 수 있다.

## Notes

- 프로그램 통계는 각 프로그램 웹사이트 기반 자기보고 수치이다.
- EA/AI 안전 커뮤니티 중심으로 조사했으며, 기업 내 교육, 정부 프로그램, 비영어권은 충분히 반영되지 않았다.
- 모든 데이터는 2026-03-26 기준이다.
