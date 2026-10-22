# Figures and visual conventions

The figures separate field organization, learning mechanisms, measurement practice, evidence, and system cost. Constructed examples illustrate analytical properties; published observations retain their source conditions.

| Figure | Purpose | Interpretation |
|---|---|---|
| 1 · [Survey at a glance](../figures/overview.svg) | The rollout–learning loop, the A/B families, and four assessment levels. | Conceptual synthesis. |
| 2 · [Research timeline](../figures/timeline.svg) | Representative methods in publication order, paired with author institutions. | Grouped first public release; selected mechanism labels, all institution names, and at most three marks per work. |
| 3 · [Policy identities](../figures/policies.svg) | Learner, sampling snapshot, actual behavior, proximal anchor, and KL reference. | A ratio decomposition at a fixed token and history, rather than a data-flow diagram. |
| 4 · [Component taxonomy](../figures/taxonomy.svg) | All focal works mapped to four intervention classes, with scheduling and supporting roles separate. | A component map; papers can contribute to several classes. |
| 5 · [Mismatch-to-learning mechanisms](../figures/mechanisms.svg) | Relative influence, conditional score drift, update decisions, and subsequent feedback. | Representative method responses are linked to the mechanisms they address. |
| 6 · [Measurement regimes](../figures/measurement_practice.svg) | Controlled numerical probes and online learning diagnostics. | The former isolates execution under fixed controls; the latter can include lag and policy movement. |
| 7 · [Rollout-guided rounding](../figures/rounding.svg) | Agreement across paths versus approximation to a higher-precision value. | Constructed fixed-scale example: learner 0.74 and rollout 0.76. |
| 8 · [Update visibility](../figures/quantization.svg) | Whether a parameter change crosses a quantization boundary. | A fixed-step scalar example, separate from cross-path agreement. |
| 9 · [Estimator correction and update control](../figures/operators.svg) | B1 target expectations versus B2 influence and acceptance decisions. | Information requirements and compatible composition rules. |
| 10 · [Evidence comparability](../figures/evidence.svg) | TRACE and TRIAGE have different learner paths, rollout targets, and baseline sets. | Edges indicate direct within-study comparisons; no cross-study performance ordering. |
| 11 · [Complete-loop efficiency](../figures/timing.svg) | Faster rollout and added work alter total iteration cost. | Illustrative serialized execution; rollout share 0.6 and speedup 2. |
| 12 · [Conditional and response probabilities](../figures/prefixes.svg) | Equal local conditionals can coexist with unequal prefix and response probabilities. | Constructed two-step illustration in Appendix C. |
| 13 · [Signed clipping](../figures/clipping.svg) | Positive and negative advantages have opposite active clipping boundaries. | Constructed surrogate with epsilon 0.2 and advantages ±1; Appendix F. |
| 14 · [Score centering](../figures/centering.svg) | A behavior-weighted scalar score mean becomes zero. | Exact two-action example; Appendix F. |

Blue and teal identify numerical interventions; muted plum and bronze identify estimation and update control. Slate denotes context or complementary mechanisms. Labels and line styles carry meaning independently of color. White panel bodies, subtle header accents, sentence-case headings, and fine rules establish a common visual hierarchy. Shaded regions in analytical plots retain their mathematical meaning. The timeline uses pale yellow method labels and blue calendar nodes. All scientific figures use Charter text, with consistent heading, body, and annotation styles; mathematical notation follows the manuscript. Smaller affiliation marks remain secondary to method names. Chronological proximity does not assert technical inheritance.

Named studies carry citations matching the manuscript bibliography. The [catalog](CATALOG.md) gives complete titles and reviewed versions; the [timeline records](../data/timeline.json) give dates, affiliations, and source locations.

## Timeline affiliations and organization marks

Affiliations follow the author block of each cited paper. All institution names are retained, using compact labels in the figure. Up to three marks follow the institution order on the first page; this order does not encode contribution rank. QeRL lists NVIDIA, MIT, HKU, and Tsinghua University (THU), while showing the first three marks. Jet-RL also includes an independent researcher. QUADS and TRACE use the Qwen team mark, while their affiliation labels retain the paper’s institutional names.

The marks identify author affiliations and retain their respective owners’ rights. They are excluded from the repository’s CC BY-SA grant. Sources are institutional websites and official media resources, with the indicated university images obtained from Wikimedia.

| Institution | Mark source |
|---|---|
| Microsoft Research | [Institutional asset](https://uhf.microsoft.com/images/microsoft/RE1Mu3b.png) |
| University of California San Diego | [Institutional asset](https://ucsd.edu/favicon.ico) |
| Mila | [Institutional asset](https://mila.quebec/sites/default/themes/mila_v1/favicon.ico) |
| NVIDIA | [Institutional asset](https://www.nvidia.com/content/nvidiaGDC/us/en_US/about-nvidia/legal-info/logo-brand-usage/_jcr_content/root/responsivegrid/nv_container_392921705/nv_container/nv_image.coreimg.svg/1776076920288/nvidia-logo-vert.svg) |
| Massachusetts Institute of Technology | [Institutional asset](https://www.mit.edu/themes/mit/assets/favicon/favicon.ico) |
| The University of Hong Kong | [Institutional asset](https://www.hku.hk/etc.clientlibs/hkucms/clientlibs/clientlib-site/resources/icon-192x192.png) |
| University of California, Berkeley | [Wikimedia image](https://thumb.wikimedia.org/wikipedia/commons/thumb/a/a1/Seal_of_University_of_California%2C_Berkeley.svg/960px-Seal_of_University_of_California%2C_Berkeley.svg.png?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail) |
| Yale University | [Institutional asset](https://www.yale.edu/sites/all/themes/yale_blue/images/favicons/apple-touch-icon-57x57.png) |
| University of Southern California | [Institutional asset](https://www.usc.edu/wp-content/themes/usc-communications-2023/favicon/apple-touch-icon.png) |
| The Hong Kong University of Science and Technology | [Institutional asset](https://hkust.edu.hk/sites/default/files/2024-03/HKUST_logo_1.svg) |
| City University of Hong Kong | [Wikimedia image](https://thumb.wikimedia.org/wikipedia/en/thumb/4/4a/CityU_logo.svg/960px-CityU_logo.svg.png?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail) |
| Zhejiang University | [Wikimedia image](https://thumb.wikimedia.org/wikipedia/en/thumb/1/16/Zhejiang_University_Logo.svg/330px-Zhejiang_University_Logo.svg.png?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail) |
| Huawei | [Institutional asset](https://www.huawei.com/-/media/hcomponent-header/1.0.1.20260908162100/component/img/huawei_logo.png) |
| Qwen Team / Alibaba Group | [Official team mark](https://avatars.githubusercontent.com/u/141221163?s=400&v=4) |
| Together AI | [Institutional asset](https://cdn.prod.website-files.com/69654e88dce9154b5f1206dd/69a6dad66e8b98c718262888_together-ai-logo-suite.zip) |
| University of Wisconsin–Madison | [Institutional asset](https://www.wisc.edu/favicon.ico) |
| ByteDance Seed | [Institutional asset](https://lf-flow-web-cdn.doubao.com/obj/flow-doubao/deploy/flow/ai_official_website/88329/static/image/footer_brand_logo.a2d9c12f.png) |
| InfiX.ai | [Institutional asset](https://avatars.githubusercontent.com/u/182507003?v=4&s=400) |
| The Ohio State University | [Wikimedia image](https://thumb.wikimedia.org/wikipedia/en/thumb/e/e1/Ohio_State_University_seal.svg/250px-Ohio_State_University_seal.svg.png?utm_source=en.wikipedia.org&utm_campaign=api&utm_content=thumbnail) |
| KAIST | [Institutional asset](https://www.kaist.ac.kr/kr/img/content/sub01/sym_new_01.gif) |
| NAVER Cloud | [Institutional asset](https://www.navercloudcorp.com/img/navercloud_favicon.ico) |
| AITRICS | [Institutional asset](https://aitrics.com/img/common/favicon.ico) |
