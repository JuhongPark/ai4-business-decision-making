# Asia-Region Decomposition Evidence

status: research_complete
date: 2026-04-21
purpose: Stream A deliverable of the sales-vs-productization research plan. Populates the two-skill matrix with Korean, Japanese, Chinese, and Singaporean/SEA firm cases 2024-2026, tests whether the decomposition holds in a different market structure, and identifies three structural modifications the parent memo should note when applied to Asia.
parent_memo: [`sales-vs-productization-decomposition.md`](sales-vs-productization-decomposition.md)
research_plan: [`../../operations/expansion/sales-vs-productization-research-plan.md`](../../operations/expansion/sales-vs-productization-research-plan.md)

---

## 1. Executive summary

Twenty-plus firm cases across Korea, Japan, China, and Singapore/SEA are coded against the sales × productization 2×2 matrix. Three findings:

1. **The route into the upper-left quadrant (both skills strong) is regionally distinct.** US firms enter via VC-funded AI-native scale-up (Anthropic, Cohere) or horizontal incumbent cross-sell (Microsoft, Salesforce). Korean chaebols enter via industrial captive deployment + Korean-language moat (Samsung, LG, Naver, SK). Chinese firms enter via open-source/cloud-ecosystem sales lever + state-backed chip substrate (Alibaba Qwen, Baidu, DeepSeek). Japan has a capital-substitution route (SoftBank's $64.6B into OpenAI) not seen in the US. These are distinct pathways, not reducible to the Microsoft/Salesforce pattern.

2. **The upper-right quadrant (sales ahead of product) is populated by different failure modes in Asia.** US enforcement documents VC-fraud variants (Nate Inc., Builder.ai, Presto). Asia documents consumer-product mislabeling (the KFTC's November 2025 20-case sweep), announced-then-postponed flagship models (Kakao's KoGPT 2.0), telco-scale AI-assistant overpromising that drives profit compression (SK Telecom -73% FY2025 profit), and AI-justified layoffs without implementation readiness (Japanese examples plus global). The VC-fraud pattern is rarer in Asia because fundraising paths differ (state capital, chaebol internal allocation, strategic investor dominance).

3. **The regulatory-sales-instrument asymmetry is sharper in Asia.** China's 748 generative-AI services filed with CAC plus 5,000+ algorithm filings (December 2025) create a compliance-as-sales-instrument class absent in Western markets. Korea's AI Basic Act (Jan 2026) + KFTC AI-washing enforcement layer on top. Singapore's AI Verify Foundation ships productization substance as a public good. Japan's METI Guidelines remain voluntary. These four regimes produce four different ratios of verification-claim to verification-substance and populate the matrix differently.

The decomposition holds in Asia. The H1 claim (PwC 20% = both skills) survives regionally, but the composition of that 20% differs by market.

---

## 2. Korea

### 2.1 Samsung (Gauss 2, Samsung Research, Samsung SDS) — upper-left (both strong)

- **Productization**: Gauss 2 family deployed internally; 60%+ of DX Division developers use Gauss 2 for coding, translation, summarization. Samsung Research published [TRUEBench](https://news.samsung.com/global/samsung-introduces-truebench-a-benchmark-for-real-world-ai-productivity) (Sep 2025) — a 2,485-test-set productivity benchmark across 10 categories and 12 languages. This is a native productization artifact equivalent to OpenAI Evals or Meta's 150+ benchmark harness.
- **Sales**: Samsung SDS 2025 revenue KRW 13.93T (+0.7%); cloud revenue +15.4% to KRW 2.68T driven by GPUaaS and generative AI; Samsung-OpenAI strategic partnership announced October 2025. Captive distribution through Galaxy installed base (~1B devices).
- **Classification**: Upper-left via internal-first pipeline. Unlike Microsoft, Samsung has not yet commercialised Gauss as a frontier external product — the eval and deployment substrate exists without the equivalent of Copilot's 16M paid seats.

### 2.2 Naver (HyperCLOVA X, Naver Cloud) — upper-left within Korea

- **Productization**: [HyperCLOVA X THINK](https://www.navercorp.com/en/media/pressReleasesDetail?seq=33066) (Jun 2025) reasoning model; SEED Think 32B scored 44 on Artificial Analysis Intelligence Index; 87% on agent tool-use in simulated telecom customer-service scenario. NAVER AI Ethics Principles publish Korean-language red-team and safety data.
- **Sales**: Naver Cloud revenue KRW 563.7B in 2024 (+26.1%); target high-teens to 20%+ CAGR through 2026. Brand and search distribution in Korea is the moat. Sovereign-AI products (Project CONNECT X, Neurocloud for HyperCLOVA X) launched 2025.
- **Classification**: Upper-left within Korea; globally uncertain. The Korean-language moat is also the scale ceiling.

### 2.3 LG AI Research (EXAONE 4.0/4.5, K-EXAONE) — upper-left, productization-led

- **Productization**: EXAONE 4.0 (Jul 2025) hybrid reasoning model; EXAONE 4.5 multimodal (Apr 2026); K-EXAONE 236B params (Dec 2025). On-premise agent stack running on FuriosaAI RNGD chips (2.25× performance-per-watt vs GPUs). ChatExaone internal deployment; Exaone Data Foundry.
- **Sales**: B2B enterprise focus from launch; partnership with FriendliAI for public API. LG Uplus building Korea's largest AI data center (120,000 GPUs) in Paju for K-EXAONE deployment.
- **Classification**: Upper-left, productization leading sales. Publishes open-weight models and benchmarks — closest Korean analogue to the Anthropic/Meta publication pattern.

### 2.4 SK Telecom (Adot, A.X 4.0/K1) — upper-left with productization gap

- **Productization**: A.X 4.0 + GPT-5 integration in Adot; A.X K1 planned. Multi-LLM agent architecture.
- **Sales**: 11.2M users on Adot in Q4 2025; 300,000+ cumulative users of the 'Note' feature in the first week (Jul 2025). AIDC revenue KRW 519.9B (+34.9% YoY 2025); AIX revenue KRW 198.6B (+6.4% YoY). **FY2025 net profit -73% YoY** as AI investment accelerates.
- **Classification**: Upper-left at telco-distribution scale, but the 73% profit plunge signals sales skill outrunning productization ROI — a partial Klarna-pattern at a telco.

### 2.5 Upstage (Solar Pro 2) — upper-left, Korea's first generative-AI unicorn

- **Productization**: Solar Pro 2 (31B params) scored 58 composite on Artificial Analysis, outperforming GPT-4o (41). "Frontier Model" designation. Document AI "Document Pass" as the vertical productization layer.
- **Sales**: KRW 180B Series C close (Apr 2026) at greater than KRW 1T valuation — **first Korean generative-AI unicorn**. Total capital $157M+. Customers include Samsung, Korean insurers, US/APAC enterprise. 130%+ annual revenue growth. KOSPI IPO targeted 2026; post-IPO valuation anticipated KRW 2–3T.
- **Classification**: Upper-left. Korean analogue to Cohere/Mistral. Founder Sung Kim (former Naver head of AI) is a productization-substrate founder.

### 2.6 Rebellions + FuriosaAI — lower-left migrating to upper-left

- **Productization**: FuriosaAI RNGD delivers 2.25× LLM inference performance per watt vs GPUs; 20,000 NPUs planned for 2026 delivery. Rebellions: $400M pre-IPO at $2.3B valuation (Mar 2026).
- **Sales**: FuriosaAI design-win with LG AI Research; rejected Meta acquisition offer; 2027 IPO target. Both classified as Korean unicorns.
- **Classification**: Productization-without-GTM (lower-left) for 2023-24; moved to upper-left with LG anchor customer + domestic-sovereignty tailwind. The Korean government's $1.42B VC allocation for 2026 AI/deep-tech is materially addressing the sales-skill shortfall.

### 2.7 Kakao (Kanana, KoGPT 2.0 postponed) — upper-right (sales ahead)

- **Productization**: KoGPT 2.0 permanently postponed in 2024; Kanana messenger launched 2025 with multi-size model lineup (Flag/Essence/Nano); Honeybee multimodal.
- **Sales**: Kakao's distribution moat (Kakao Talk ~50M Korean users) drove announcement-velocity; 63 AI-driven solutions released in 6 months (2024-25).
- **Classification**: **Upper-right** — the KoGPT 2.0 postponement is the cleanest Asian analogue to the "promised but undelivered" pattern. Sales / PR substrate sold "Korea's ChatGPT"; productization did not ship. Partial recovery via Kanana relaunch but productization substance remains thin relative to Naver/LG.

### 2.8 Law&Company SuperLawyer — upper-left (Korean S5 productization exemplar)

- **Productization**: 82% on Korean Bar Exam (top 5%) May 2025 — first non-English AI model to achieve this.
- **Sales**: ~38% of Korea's practicing lawyers adopted within 1 year of 2024 debut. LexisNexis partnership; Japanese-language launch preparing.
- **Classification**: Upper-left. **Direct Korean analogue to Harvey AI** — publishes bar-exam benchmark (productization substance) with strong Korean-language moat (sales substance). This is the S5 exemplar for Asia.

### 2.9 Korea AI Basic Act + KFTC AI-washing enforcement — regulatory context

- AI Basic Act in force **January 22, 2026**. Penalties: KRW 30M administrative fines for domestic-representative failure; KRW 150M + 2-year imprisonment for false or exaggerated AI advertising. Enforcement postponed one year — initially guidance-heavy.
- KFTC identified **20 AI-washing cases November 2025** (19 involved using "AI" in product names when technology was merely sensor-based). 2026 policy priorities formally include AI-washing guidelines.
- **Structural signal**: Korean AI-washing enforcement targets consumer-product mislabeling, not VC-fraud (unlike SEC Nate Inc. / Presto Voice). This populates the upper-right quadrant differently in Asia.

---

## 3. Japan

### 3.1 Preferred Networks — lower-left (engineering without GTM)

- **Productization**: Full-stack — AI chips, compute infra, foundation models, applications; rated top deep-learning capability in Japan.
- **Sales**: $315M total funding; specialised in trucking and robots — limited horizontal enterprise sales motion.
- **Classification**: Classic **lower-left**. METI's $6.34B, 5-year (FY2026 start) public-private JV with SoftBank + Preferred Networks is the forcing function to migrate PFN's productization into national-scale sales.

### 3.2 Sakana AI — upper-left (AI-native balanced)

- **Productization**: "Small models, smart design" thesis; Series B research publications on nature-inspired methods.
- **Sales**: $135M Series B at $2.65B valuation (Nov 2025); total funding $379M. **Japan's most valuable AI unicorn**. Investors include MUFG, Khosla, Mitsubishi Electric, Salesforce Ventures, Google, In-Q-Tel, Citi. Expansion into defense, intelligence, manufacturing; MUFG + Daiwa custom finance AI.
- **Classification**: Upper-left, closest Japanese analogue to Anthropic. The In-Q-Tel investment signals verification-grade productization.

### 3.3 SoftBank + Stargate + OpenAI — upper-left via capital substitution

- **Productization**: Functionally outsourced to OpenAI.
- **Sales**: **$64.6B cumulative SoftBank investment in OpenAI** (Dec 2025); Stargate 40% equity; $500B planned infrastructure by 2029. OpenAI $20B+ ARR 2025.
- **Classification**: Upper-left by acquisition of productization access. An extreme version of Microsoft's OpenAI strategy. Tests an edge of the decomposition: **a firm can reach upper-left by buying the productization skill rather than building it** — a Japanese/SoftBank-distinctive route.

### 3.4 Rakuten AI (Rakuten AI 2.0/3.0) — upper-left with vertical moat

- **Productization**: Rakuten AI 3.0 (Dec 2025) ~700B params, MoE, Japanese-language specialised; Rakuten AI 2.0 open-sourced Feb 2025. Rakuten Mobile + OpenAI voice-agent integration.
- **Sales**: Rakuten AI for Business launched for Japanese corporates; AI contributed ¥25.5B to 2025 Group profit (exceeded ¥21B target).
- **Classification**: Upper-left. Japanese e-commerce vertical analogue to Alibaba.

### 3.5 NTT Data (tsuzumi 2) + Fujitsu — upper-left at incumbent distribution

- **Productization**: tsuzumi 2 (Oct 2025) runs on single GPU with ultra-large-model-comparable performance; Fujitsu 1-bit quantisation preserves 89% accuracy at 94% memory reduction; Sarashina2-8x70B (~460B MoE).
- **Sales**: Japan IT services market $67.27B (2025) → $74.88B (2026); NTT DATA 2026 Global AI Report — only 15% of surveyed orgs qualify as "AI leaders." Microsoft partnership with 5 Japanese IT majors to train 1M AI professionals by 2030.
- **Classification**: Upper-left at SI/incumbent scale. NTT Data's "pilots to profit" framing is the Japanese version of the a16z/PwC "top 20%" selection.

### 3.6 Japan consumer AI-startup failures — upper-right, mostly quiet

- Bloomberg (Oct 2025) noted a Japanese startup case: "AI in a name is no guarantee of success."
- AI-layoff pattern (TechCrunch Feb 2026, ~50K+ AI layoffs) global but with Japan examples — companies announce AI-driven layoffs despite not having mature AI to fill roles.
- Japanese regulatory environment is non-binding (METI AI Guidelines v1.01); no fines, no bans, no mandates. This *enables* upper-right behaviour structurally.

---

## 4. China

### 4.1 Baidu (ERNIE 4.5/5.0) — upper-left at incumbent-domestic scale

- **Productization**: ERNIE 4.5 (Jun 2025, 10 variants including 424B MoE); ERNIE 5.0 omni-modal (Nov 2025) claims to beat GPT-5/Gemini on selected benchmarks.
- **Sales**: AI Cloud revenue RMB 30B (2025); AI Cloud Infra +34% YoY; subscription AI accelerator +143%; AI-powered core revenue RMB 11B+ in Q4 (43% of general business revenue).
- **Classification**: Upper-left domestically; internationally gated by CAC filings and US sanctions.

### 4.2 Alibaba (Qwen 3/3.5/3.5-Omni) — upper-left with open-source sales lever

- **Productization**: Qwen family, 600M+ downloads, 170,000+ derivative models, 100+ open-weight releases. Qwen 3.5 released Feb 2026.
- **Sales**: Alibaba Cloud fiscal 2025 revenue $16.26B (+11%); Q2 2025 cloud +26% YoY; AI-related revenue >20% of external customers for 8 consecutive quarters at triple-digit growth. Monetization pivoting from pure open-source to enterprise.
- **Classification**: Upper-left. Open-sourcing is a sales instrument: it manufactures ecosystem lock-in that converts to cloud consumption. A structurally distinctive Chinese route not available to closed-weight Western labs at this scale.

### 4.3 ByteDance / Doubao / Volcano Engine — upper-left at consumer scale

- **Productization**: Volcano Engine led ~49% of China LLM public-cloud token share mid-2025. ByteDance committing $23B AI infra 2026.
- **Sales**: Doubao 100M+ DAU, 155M weekly active users (Dec 2025). Volcano Engine revenue RMB 12B (2024), targeting RMB 25B (2025), RMB 100B by 2030.
- **Classification**: Upper-left, consumer-to-enterprise flywheel.

### 4.4 DeepSeek / Moonshot / Zhipu / MiniMax — upper-left (AI-native cluster)

- **DeepSeek**: $220M ARR run-rate mid-2025; 26,000+ enterprise API accounts; 5.7B API calls/month; first external raise $300M at $10B valuation April 2026.
- **Moonshot AI**: $4.8B valuation Jan 2026; targeting Hong Kong IPO at up to $18B.
- **Zhipu AI**: $13B market value (Knowledge Atlas IPO listing).
- **MiniMax**: $15.2B valuation Jan 2026.
- **Classification**: Upper-left cluster. All publish technical reports and benchmarks (productization substance) + rapidly monetise via API revenue (sales substance). Structurally similar to Anthropic/OpenAI/xAI/Cohere cluster but with Chinese regulatory filings (CAC) as the sales-side compliance artifact and domestic chip supply (Cambricon, Huawei Ascend) as the productization constraint.

### 4.5 Tencent Hunyuan — upper-left with vertical gaming moat

- **Productization**: Hunyuan 3D Engine global launch Nov 2025; Hunyuan-GameCraft for interactive video; HY-1.8B-2Bit mobile-ready compressed model (Feb 2026).
- **Sales**: 150+ enterprise integrations of Hunyuan 3D API across gaming, e-commerce, media. Customers include Unity China, Bambu Lab, Liblib.
- **Classification**: Upper-left via gaming-vertical productization + Tencent's WeChat/game distribution.

### 4.6 China chip stack (Huawei Ascend, Cambricon) — productization substrate

- Huawei: ~600K-650K AI chips 2025; targeting 1.6M total dies 2026; Ascend 950PR Q1 2026.
- Cambricon: 125K-150K (2025) → 500K target (2026); ByteDance >50% of orders.
- Productization-dominated profile — analogue to Korean Rebellions/FuriosaAI but at much larger state-backed scale.

### 4.7 Chinese regulatory signal — 748 generative-AI services CAC-filed by Dec 2025

CAC 748 filings (Dec 2025); 5,000+ algorithms registered. Cybersecurity Law AI amendments effective January 1, 2026. This is the highest-volume pre-deployment filing regime globally and creates a sales-instrument class absent in Western markets: a CAC filing is a verification claim Chinese firms must produce; audit substance varies.

---

## 5. Singapore and Southeast Asia

### 5.1 AI Verify Foundation + Global AI Assurance Pilot — S6 exemplar

- Global AI Assurance Pilot (Feb 2025): 16 specialist testers paired with 17 GenAI deployers across 10 industries; completed May 2025. Testing Starter Kit announced. AI Assurance Framework planned 2026.
- **Classification**: The Singapore state is producing public-good productization infrastructure that private actors cannot privately sustain. Confirms the scale-based track's public-good threshold.

### 5.2 MAS AI Risk Management Guidelines + Veritas — regulatory forcing

- MAS AIRG consultation Nov 2025 – Jan 2026; expected finalization 2026 with supervisory weight.
- Veritas toolkit integrated as AIVT plugin — bridging FEAT principles to operational testing.
- **Classification**: Regulatory forcing function into upper-left for Singapore financial institutions.

### 5.3 Sea Group (Shopee + SeaMoney) — upper-left at SEA platform scale

- **Productization**: Shopee AI personalisation +10% conversion YoY; SeaMoney AI credit scoring keeps delinquent rate at 1.3% on $7.9B loan book (+70% YoY) serving largely unbanked.
- **Sales**: FY2025 revenue $22.4B (+32.9%); Feb 2026 Google strategic AI partnership for agentic shopping on Shopee.
- **Classification**: Upper-left via regional-platform vertical (e-commerce + gaming + fintech). Structurally analogous to Alibaba/ByteDance at SEA scale.

### 5.4 Grab — upper-left, newly profitable

- FY2025 first-ever net profit $200M; revenue $3.37B (+19% YoY); EBITDA $500M (+60% YoY); targeting $4.04B-$4.10B 2026 revenue.
- AI-driven promotions + autonomous vehicle partnerships in 2028 targets.

---

## 6. Cross-regional synthesis

### 6.1 The decomposition holds, with three structural modifications

1. **Routes into upper-left differ.** US firms enter via VC-funded AI-native scale-up or horizontal incumbent cross-sell. Korean chaebols enter via industrial captive deployment + language moat. Chinese firms enter via open-source / cloud-ecosystem sales lever + state-backed chip substrate. Japan has a capital-substitution route (SoftBank's $64.6B into OpenAI). These are distinct routes, not reducible to the Microsoft/Salesforce pattern.
2. **Upper-right is populated by different failure modes.** US enforcement documents VC-fraud variants (Nate Inc., Builder.ai, Presto). Asia documents consumer-product mislabeling (KFTC 20 cases), announced-then-postponed models (Kakao KoGPT 2.0), telco-scale AI overpromising (SK Telecom -73% profit), and AI-layoffs without implementation readiness. VC-fraud is rarer in Asia because fundraising paths differ.
3. **Regulatory asymmetry is sharper in Asia.** China's 748 CAC-filed GenAI services + Korea's AI Basic Act + KFTC AI-washing enforcement + Japan's voluntary METI guidelines + Singapore AI Verify as public good produce four distinct claim-substance ratios that the parent memo's §5 should annotate.

### 6.2 Firms that defy the four-quadrant classification

- **SoftBank**: $64.6B investment in OpenAI. Productization is *vicarious* — SoftBank owns productization access without building it.
- **Preferred Networks → METI JV**: a firm whose productization is being forcibly re-classified via government-led merger. Neither firm-level nor state-level classification captures it cleanly.
- **Chinese AI-native labs (DeepSeek, Moonshot, Zhipu)**: "Both strong but sanctions-constrained" is a sub-classification of upper-left that the original matrix does not encode. Productization is demonstrable; sales to Western enterprise is gated by non-productization, non-sales factors (export controls, CAC filings, Western buyer hesitation).

### 6.3 Bearing on H1 (PwC 20% = both skills)

The hypothesis holds regionally, but the composition of the 20% differs. In Korea the upper-left cell contains 10–15 firms (4–5 chaebols + 3–5 AI-native challengers: Upstage, Rebellions, FuriosaAI, Law&Company, Samsung / Naver / LG / SK). In Japan about 10 firms (SoftBank-as-capital + Preferred / Sakana + incumbent SIs). In China 15–20 firms (four incumbents + the AI-native cluster). In Singapore/SEA 5–8 firms. The absolute count per economy is broadly comparable, but the country-specific population structure changes the policy and research implications.

---

## 7. Summary table (selected cases)

| Firm | Country | Sales | Productization | Quadrant | Key metric |
|---|---|---|---|---|---|
| Samsung (Gauss 2) | KR | H | H | Upper-left | TRUEBench 2,485-test set; SDS KRW 13.93T revenue |
| Naver (HyperCLOVA X) | KR | H | H | Upper-left | Cloud KRW 563.7B +26.1%; SEED Think 44 AA index |
| LG AI (EXAONE 4.5) | KR | M | H | Upper-left, prod-led | K-EXAONE 236B; FuriosaAI 2.25× perf/watt |
| SK Telecom (Adot) | KR | H | M | Upper-left w/ gap | 11.2M users; FY25 profit -73% |
| Upstage (Solar Pro 2) | KR | H | H | Upper-left | First KR generative-AI unicorn, >KRW 1T val |
| FuriosaAI / Rebellions | KR | M | H | Upper-left migrating | $2.3B val; 20K NPUs 2026; rejected Meta |
| Kakao (KoGPT 2.0) | KR | H | L | **Upper-right** | KoGPT 2.0 postponed; Kanana relaunched |
| Law&Company SuperLawyer | KR | H | H | Upper-left | 82% KR Bar; 38% KR lawyers adopted |
| Preferred Networks | JP | L | H | **Lower-left** | $315M funding; METI JV absorbing |
| Sakana AI | JP | H | H | Upper-left | $2.65B val; In-Q-Tel, MUFG investors |
| SoftBank/OpenAI | JP | H | H (via acq) | Upper-left (atypical) | $64.6B total OpenAI investment |
| Rakuten AI 3.0 | JP | H | H | Upper-left | 700B params; ¥25.5B AI profit |
| NTT Data (tsuzumi 2) | JP | H | H | Upper-left | Single-GPU deploy; 2026 AI report |
| Baidu (ERNIE 5.0) | CN | H | H | Upper-left (dom.) | AI Cloud RMB 30B; infra +143% |
| Alibaba (Qwen 3.5) | CN | H | H | Upper-left | 600M+ downloads; Cloud $16.26B |
| ByteDance (Doubao) | CN | H | H | Upper-left | 100M+ DAU; 49% LLM cloud share |
| DeepSeek | CN | H | H | Upper-left (sanctions) | $220M ARR; $10B val target |
| Moonshot AI | CN | H | H | Upper-left | $4.8B val; $18B HK IPO target |
| Tencent Hunyuan | CN | H | H | Upper-left (vertical) | 150+ ent. integrations 3D API |
| Sea Group (Shopee) | SG | H | H | Upper-left | $22.4B rev; 1.3% NPL on $7.9B loans |
| Grab | SG | H | M | Upper-left | First profitable year; $3.37B rev |
| AI Verify Foundation | SG | n/a | H | Public-good | 17 deployers, 10 industries pilot |

Legend: H = High; M = Medium; L = Low. Upper-left = both strong; Upper-right = sales ahead of productization; Lower-left = productization without GTM; Lower-right = both weak.

---

## 8. Sources

- [Korea AI Basic Act official](https://cset.georgetown.edu/wp-content/uploads/t0625_south_korea_ai_law_EN.pdf) | [Cooley summary Jan 2026](https://www.cooley.com/news/insight/2026/2026-01-27-south-koreas-ai-basic-act-overview-and-key-takeaways)
- [KFTC AI-washing 20 cases Nov 2025](https://www.lexology.com/library/detail.aspx?g=1a8a3351-a5e0-4100-bb05-bd04fff9b49d)
- [Singapore AI Verify Global AI Assurance Pilot](https://assurance.aiverifyfoundation.sg/) | [IMDA press release](https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2025/sg-unveils-insights-from-worlds-first-technical-testing-of-real-world-applications-of-genai)
- [MAS AI Risk Management Guidelines consultation](https://www.mas.gov.sg/publications/consultations/2025/consultation-paper-on-guidelines-on-artificial-intelligence-risk-management)
- [METI AI Guidelines v1.1](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20240419_15.pdf)
- [China CAC generative AI filings](https://iclg.com/practice-areas/telecoms-media-and-internet-laws-and-regulations/03-china-s-key-developments-in-artificial-intelligence-governance-in-2025)
- [Samsung TRUEBench](https://news.samsung.com/global/samsung-introduces-truebench-a-benchmark-for-real-world-ai-productivity)
- [HyperCLOVA X Technical Report](https://arxiv.org/html/2404.01954v1)
- [LG EXAONE / IEEE Spectrum](https://spectrum.ieee.org/exaone-lg-ai-research)
- [Upstage Series C unicorn](https://en.sedaily.com/technology/2026/04/15/upstage-becomes-koreas-first-ai-unicorn-eyes-b2c-expansion)
- [FuriosaAI $125M + LG design-win](https://www.businesswire.com/news/home/20250730613509/en/FuriosaAI-Closes-$125M-Investment-Round-to-Scale-Production-of-Next-Gen-AI-Inference-Chip)
- [Rebellions $400M pre-IPO](https://techcrunch.com/2026/03/30/ai-chip-startup-rebellions-raises-400-million-at-2-3b-valuation-in-pre-ipo-round/)
- [Sakana AI Series B](https://techcrunch.com/2025/11/17/sakana-ai-raises-135m-series-b-at-a-2-65b-valuation-to-continue-building-ai-models-for-japan/)
- [Preferred Networks / METI JV](https://www.businesskorea.co.kr/news/articleView.html?idxno=259389)
- [SoftBank $64.6B OpenAI](https://www.cnbc.com/2025/12/30/softbank-openai-investment.html)
- [Rakuten AI 3.0](https://rakuten.today/blog/rakuten-ai-in-2025-embracing-agentic-ai.html)
- [NTT DATA 2026 Global AI Report](https://us.nttdata.com/en/news/press-release/2025/december/ntt-data-2026-global-ai-report)
- [Baidu ERNIE 5.0](https://venturebeat.com/ai/baidu-just-dropped-an-open-source-multimodal-ai-that-it-claims-beats-gpt-5)
- [Alibaba Qwen 600M downloads](https://www.alibabagroup.com/en-US/document-1907873420045975552)
- [ByteDance Volcano Engine](https://en.tmtpost.com/post/7645516)
- [DeepSeek $10B raise](https://www.roic.ai/news/deepseeks-first-funding-round-targets-10-billion-plus-valuation-04-17-2026)
- [Moonshot AI IPO plans](https://chinabizinsider.com/moonshot-ai-weighs-hong-kong-ipo-at-18-billion-valuation-in-2026-tech-surge/)
- [Tencent Hunyuan 3D global launch](https://www.tencent.com/en-us/articles/2202235.html)
- [Huawei Ascend 2026 production doubling](https://www.bloomberg.com/news/articles/2025-09-29/huawei-to-double-output-of-top-ai-chip-as-nvidia-wavers-in-china)
- [Sea Group AI strategy](https://www.klover.ai/sea-limited-ai-strategy-analysis-of-dominance-in-consumer-internet/)
