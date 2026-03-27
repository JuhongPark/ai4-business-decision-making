# AI Alignment Research — Open-Source Codebases

status: bilingual_reference_note
summary: Reference scan of open-source repositories and tooling used in AI alignment research.
language_note: This appendix is retained as a legacy bilingual scouting note while the broader repository is normalized to English.

This document catalogs the open-source repositories most often used to study AI alignment in code form and where code-level reference material can be found.

Star counts are as of 2026-03-26. They indicate community adoption rather than research quality. Because the field is relatively small, repositories with 100-1,000 stars can still be core tools. Most of the repositories here are research code rather than production systems.

> **Coverage note:** This scan centers on public GitHub repositories. It excludes internal corporate code from labs such as Anthropic, OpenAI, and DeepMind, as well as non-English repositories. Other relevant groups such as EleutherAI, Redwood Research, and ARC Evals operate adjacent codebases that are not exhaustively covered here.

## GitHub Organizations

| Organization | Focus | Link |
|---|---|---|
| Anthropic (official) | SDKs, APIs, Claude tooling | https://github.com/anthropics |
| Anthropic (experimental) | 정렬 연구 프로토타입 — misalignment, safety | https://github.com/anthropic-experimental |
| Safety Research | Alignment faking 재현, Bloom, SAELens | https://github.com/safety-research |
| Center for AI Safety (CAIS) | 벤치마크, 평가 프레임워크 | https://github.com/orgs/centerforaisafety |
| PKU Alignment | Safe RLHF, 제약 조건 하 가치 정렬 | https://github.com/PKU-Alignment |
| MIT NDIF Team | NNsight, nnterp — 모델 해석가능성 인프라 | https://github.com/ndif-team |
| MIT Multimodal Interpretability | MAIA, FIND — 자동 해석가능성 | https://github.com/multimodal-interpretability |
| MIT Algorithmic Alignment Lab | Formal contracts, red-teaming | https://github.com/Algorithmic-Alignment-Lab |

## Alignment Training Frameworks

RLHF/DPO 등 정렬 학습을 직접 구현하는 레포. 기업에서 모델을 정렬하려면 이 도구들이 출발점이 된다.

| Repository | Stars | Maturity | Description |
|---|---|---|---|
| huggingface/trl | ~17,800 | Production | RLHF/DPO/GRPO 학습의 사실상 표준. 정렬 전용은 아니지만 정렬 연구자들이 기반으로 쓴다. |
| OpenRLHF/OpenRLHF | ~9,200 | Production | Ray + vLLM 기반 분산 RLHF. 대규모 정렬 학습에 사용. |
| PKU-Alignment/safe-rlhf | ~1,600 | Research | 유해성과 유용성을 분리 최적화하는 Safe RLHF. NeurIPS 논문 동반. |
| OpenLMLab/MOSS-RLHF | ~1,400 | Research | "Secrets of RLHF in LLMs" 논문 코드. PPO 학습의 실제 함정을 분석. |
| tomekkorbak/pretraining-with-human-feedback | ~180 | Research | 파인튜닝이 아닌 사전학습 단계에서 인간 선호를 반영하는 연구. |

> **Maturity:** *Production* = 기업/랩에서 실제 사용, 문서화 양호. *Research* = 논문 동반 코드, 프로덕션 적용에는 상당한 수정 필요.

## Mechanistic Interpretability

Anthropic의 "Scaling Monosemanticity" 연구 방향에서는 모델 내부를 이해하지 않으면 정렬 주장을 검증하기 어렵다고 본다. 반대로 행동주의 평가(behavioral evaluation) 접근은 외부 테스트만으로 충분하다고 주장한다. 두 입장 모두 활발히 연구 중이다.

| Repository | Stars | Description |
|---|---|---|
| TransformerLensOrg/TransformerLens | ~3,200 | MI 연구의 표준 도구. Neel Nanda(ex-Anthropic) 제작. 내부 activation 접근/수정 가능. |
| decoderesearch/SAELens | ~1,300 | Sparse Autoencoder 학습/분석. Anthropic monosemanticity 연구의 오픈소스 재현. |
| callummcdougall/sae_vis | — | Anthropic SAE 시각화 재현 도구. |
| wesg52/sparse-probing-paper | ~66 | 모델 내부 표현이 인간 개념과 어떻게 대응하는지 연구. |

이 분야의 핵심 연구는 GitHub이 아니라 **transformer-circuits.pub**에 게시된다.

## MIT Alignment Research

MIT는 정렬 학습보다 해석가능성 도구 개발에 집중한다. 여기서 나온 도구를 활용하면 모델 내부 분석 연구를 수행할 수 있다.

### NDIF / NNsight (David Bau Lab, MIT EECS)

| Repository | Stars | Description |
|---|---|---|
| ndif-team/nnsight | ~870 | HuggingFace 모델을 래핑해서 내부 activation에 개입하는 라이브러리. TransformerLens의 MIT 대안. |
| ndif-team/nnterp | ~104 | NNsight 기반 통합 인터페이스. 50+ 모델, 16개 아키텍처 패밀리 지원. |
| ndif-team/ndif | ~43 | National Deep Inference Fabric — 원격 deep inference 서버. |
| ndif-team/cookbook | 5 | MI 논문들의 NNsight 구현 모음. 연구 재현에 유용. |

### Multimodal Interpretability (Sarah Schwettmann Lab, MIT CSAIL)

| Repository | Stars | Description |
|---|---|---|
| multimodal-interpretability/maia | ~105 | MAIA — 비전-언어 모델로 다른 모델 내부를 자동 해석하는 에이전트. |
| multimodal-interpretability/FIND | ~52 | NeurIPS '23. 해석가능성 메서드 평가 벤치마크. |
| multimodal-interpretability/nnn | ~20 | Nearest Neighbor Normalization (EMNLP 2024). |

이 그룹에서 2024년 10월 **Transluce**(transluce.org) 비영리 연구소를 설립했다. AI 시스템 이해를 위한 오픈 도구를 만드는 곳이다.

### Algorithmic Alignment Lab (Dylan Hadfield-Menell Lab, MIT CSAIL)

| Repository | Stars | Description |
|---|---|---|
| Algorithmic-Alignment-Lab/contracts | ~19 | 멀티에이전트 RL을 위한 formal contracts. |
| Algorithmic-Alignment-Lab/CommonClaim | ~13 | "Explore, Establish, Exploit" — LLM 레드팀 from scratch. |

코드보다 이론/정책 연구 비중이 높은 그룹. 정렬의 수학적·철학적 기반을 연구한다.

### MIT AI Risk Repository (Peter Slattery, MIT FutureTech)

코드 레포가 아니라 구조화된 리스크 데이터베이스다. 정렬 관련 리스크를 체계적으로 분류한 자료를 찾을 수 있다.

- **Site:** https://airisk.mit.edu/
- **Scale:** 1,700+ AI 리스크, 74개 프레임워크에서 추출 (Version 4, 2025년 12월)
- **Taxonomies:** 인과 분류(how/when/why) + 도메인 분류(7개 도메인, 24개 서브도메인)
- **AI Incident Tracker:** AIID 기반 사고 사례 LLM 분류
- **Paper:** arXiv:2408.12622

## Safety Evaluation & Red-Teaming

LLM 안전성을 평가하는 도구들. 기업 배포 전 안전 검증에 활용할 수 있다.

| Repository | Stars | Maturity | Description |
|---|---|---|---|
| promptfoo/promptfoo | ~18,500 | Production | LLM 레드팀/펜테스팅/취약점 스캔. OpenAI, Anthropic 사용 주장(벤더 자기보고). **이 목록에서 가장 기업 활용에 가까운 도구.** |
| centerforaisafety/HarmBench | ~890 | Research | 자동 레드팀 표준 평가 프레임워크. 33개 LLM, 18개 공격 기법. |
| agencyenterprise/PromptInject | ~470 | Research | 프롬프트 인젝션 공격 프레임워크. 정렬 우회 취약점 연구. |
| hendrycks/ethics | ~320 | Research | "Aligning AI with Shared Human Values" (ICLR 2021). 가치 정렬 벤치마크 원조. |

## Misalignment & Alignment Faking

모델이 정렬된 척하거나 에이전트로서 오정렬 행동을 보이는 현상을 연구하는 코드. 거버넌스 관점에서 중요한 자료다.

| Repository | Stars | Description |
|---|---|---|
| anthropic-experimental/agentic-misalignment | ~580 | Anthropic 공식. 에이전트 misalignment — 협박, 정보 유출, 기만적 순응 시나리오. |
| safety-research/open-source-alignment-faking | ~54 | Anthropic alignment faking 논문 오픈소스 재현. 평가 시 정렬된 척하고 실제로는 다르게 행동하는 현상. |

## Anthropic 연구 발표 채널

Anthropic의 핵심 정렬 연구는 GitHub이 아니라 전용 사이트에 게시된다. 코드가 동반될 때는 `anthropic-experimental` 또는 `safety-research` org 아래로 나온다.

- **alignment.anthropic.com** — 정렬 과학 블로그 (Bloom, Petri 등)
- **transformer-circuits.pub** — MI 연구 (Scaling Monosemanticity, circuit analysis)
- **anthropic.com/research** — 전체 연구 인덱스

## Enterprise Use Perspective

| Need | Useful tools | Notes |
|---|---|---|
| Pre-deployment LLM safety testing | promptfoo | The clearest production-grade safety evaluation tool in this list |
| RLHF/DPO model training | trl, OpenRLHF | Production-viable and immediately usable |
| Model internals and interpretability | TransformerLens, NNsight, SAELens | Still research-stage; no clear public evidence of production governance use |
| Hiring signals for AI safety talent | Experience with these tools, plus MATS/SPAR backgrounds | Hands-on experience remains rare in the talent market |

## Notes

- promptfoo, trl, and OpenRLHF are the clearest production-usable tools in this set; the rest are better treated as research tools.
- The maturity labels are author judgments based on documentation quality, maintenance activity, and public usage signals.
- All data reflects a 2026-03-26 snapshot.
