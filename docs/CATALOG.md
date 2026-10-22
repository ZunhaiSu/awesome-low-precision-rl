# Reviewed paper catalog

Full titles, source versions, numerical regimes, and discussion locations for the surveyed contributions.

Entries distinguish contribution roles, numerical regimes, and tested settings.

## Browse by intervention

[Chronological records](#chronological-records) · [Evidence synthesis](EVIDENCE.md) · [Classification rules](TAXONOMY.md)

A work can appear in several component classes. Supporting studies are labeled explicitly; diagnostics and the exploration boundary remain in the chronological records.

### Alignment (A1)

Shared learner–sampler computation.

[R3](#paper-r3) (support) · [TBIK / Deterministic Inference](#paper-tbik) (support) · [Jet-RL](#paper-jet) · [QaRL](#paper-qarl) · [QUADS](#paper-quads) · [Miles v0.1](#paper-miles) · [QATFactory / QARL](#paper-qatfactory) · [TRACE](#paper-trace)

### Fidelity (A2)

Quantization error and visible parameter updates.

[FP16-Mismatch](#paper-fp16) (support) · [Jet-RL](#paper-jet) · [FP8-RL](#paper-fp8rl) · [QuRL](#paper-qurl) · [QUADS](#paper-quads) · [HiFloat4 / Rollout-ResQ](#paper-hif4) · [Miles v0.1](#paper-miles) · [KV4-RL](#paper-kv4)

### Estimation (B1)

Target expectations and gradient correction.

[FlashRL / TIS](#paper-flashrl) · [MiniRL](#paper-minirl) (support) · [AIS](#paper-ais) · [Score Centering](#paper-score) · [CIS](#paper-cis) (support) · [Baselines and Score Centering](#paper-scorebaseline) (support)

### Update control (B2)

The influence of samples on policy updates.

[MiniRL](#paper-minirl) (support) · [DPPO](#paper-dppo) (support) · [QuRL](#paper-qurl) · [QaRL](#paper-qarl) · [P3O / ESS](#paper-p3o) · [DRPO](#paper-drpo) · [MIPU](#paper-mipu) · [ACRL](#paper-acrl) · [Full Pipeline FP8 RL](#paper-fullfp8) · [TRIAGE](#paper-triage)

### Scheduling (B3)

Complementary scheduling, retained as a navigation topic rather than a fifth primary class; direct low-bit evidence remains limited.

[Beyond Precision](#paper-beyond) (support)

## Chronological records

<a id="paper-flashrl"></a>

### FlashRL / TIS

**[On the Rollout-Training Mismatch in Modern RL Systems](https://www.opt-ml.org/papers/2025/paper116.pdf)**

Authors: Feng Yao; Liyuan Liu; Dinghuai Zhang; Chengyu Dong; Jingbo Shang; Jianfeng Gao.

First public: 2025 · Source version: [OPT2025](https://www.opt-ml.org/papers/2025/paper116.pdf)

- Numerical regime: Higher-precision learner; quantized rollout
- Contribution role: core; evidence domain: direct_low_precision
- Components: B1
- Main discussion: 5.1; additional locations: 1.1; 2.1
- Scope: Quantized rollout; recorded behavior probabilities.

<a id="paper-qerl"></a>

### QeRL

**[QeRL: Beyond Efficiency - Quantization-enhanced Reinforcement Learning for LLMs](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a15a2ece7f0663d1ba7db91103ac61c9-Abstract-Conference.html)**

Authors: Wei Huang; Yi Ge; Shuai Yang; Yicheng Xiao; Huizi Mao; Yujun Lin; Hanrong Ye; Sifei Liu; Ka Chun Cheung; Hongxu Yin; Yao Lu; Xiaojuan Qi; Song Han; Yukang Chen.

First public: 2025-10-13 · Source version: [ICLR2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a15a2ece7f0663d1ba7db91103ac61c9-Abstract-Conference.html)

- Numerical regime: NVFP4 with LoRA and adaptive noise
- Contribution role: boundary; evidence domain: exploration_boundary
- Components: Boundary
- Main discussion: Box 1; additional locations: none listed
- Scope: NVFP4 with LoRA and adaptive noise; exploration setting.

[arXiv record](https://arxiv.org/abs/2510.11696) · [Publication/source](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a15a2ece7f0663d1ba7db91103ac61c9-Abstract-Conference.html)

<a id="paper-r3"></a>

### R3

**[Stabilizing MoE Reinforcement Learning by Aligning Training and Inference Routers](https://arxiv.org/abs/2510.11370v2)**

Authors: Wenhan Ma; Hailin Zhang; Liang Zhao; Yifan Song; Yudong Wang; Zhifang Sui; Fuli Luo.

First public: 2025-10-13 · Source version: [v2](https://arxiv.org/abs/2510.11370v2)

- Numerical regime: MoE routing; general execution mismatch
- Contribution role: support; evidence domain: general_TIM
- Components: Support; A1
- Main discussion: 3.1; additional locations: 4.1
- Scope: MoE routing replay; routing mismatch is not uniquely quantization-induced.

[arXiv record](https://arxiv.org/abs/2510.11370) · [Publication/source](https://arxiv.org/abs/2510.11370)

<a id="paper-fp16"></a>

### FP16-Mismatch

**[Defeating the Training-Inference Mismatch via FP16](https://arxiv.org/abs/2510.26788v1)**

Authors: Penghui Qi; Zichen Liu; Xiangxin Zhou; Tianyu Pang; Chao Du; Wee Sun Lee; Min Lin.

First public: 2025-10-30 · Source version: [v1](https://arxiv.org/abs/2510.26788v1)

- Numerical regime: BF16 / FP16 numerical comparison
- Contribution role: support; evidence domain: higher_precision_comparison
- Components: Support; A2
- Main discussion: 3.1; additional locations: none listed
- Scope: BF16/FP16 numerical evidence; not a low-bit acceleration method.

[arXiv record](https://arxiv.org/abs/2510.26788) · [Publication/source](https://arxiv.org/abs/2510.26788)

<a id="paper-tbik"></a>

### TBIK / Deterministic Inference

**[Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch](https://arxiv.org/abs/2511.17826v2)**

Authors: Ziyang Zhang; Xinheng Ding; Jiayi Yuan; Rixin Liu; Huizi Mao; Jiarong Xing; Zirui Liu.

First public: 2025-11-21 · Source version: [v2](https://arxiv.org/abs/2511.17826v2)

- Numerical regime: BF16 / FP32; matched reduction order across TP sizes
- Contribution role: support; evidence domain: general_TIM
- Components: Support; A1
- Main discussion: 3.1; additional locations: 4.1; 6.3
- Scope: Deterministic cross-TP execution reference; not a low-bit rollout acceleration method.

[arXiv record](https://arxiv.org/abs/2511.17826) · [Publication/source](https://arxiv.org/abs/2511.17826)

<a id="paper-minirl"></a>

### MiniRL

**[Stabilizing Reinforcement Learning with LLMs: Formulation and Practices](https://arxiv.org/abs/2512.01374v3)**

Authors: Chujie Zheng; Kai Dang; Bowen Yu; Mingze Li; Huiqiang Jiang; Junrong Lin; Yuqiong Liu; Hao Lin; Chencan Wu; Feng Hu; An Yang; Jingren Zhou; Junyang Lin.

First public: 2025-12-01 · Source version: [v3](https://arxiv.org/abs/2512.01374v3)

- Numerical regime: Hybrid-engine RL; includes FP8-rollout experiments
- Contribution role: support; evidence domain: direct_low_precision
- Components: Support; B1/B2
- Main discussion: 2.1; additional locations: 1.2; 5.1
- Scope: Formulation role; also contains direct FP8 rollout experiments.

[arXiv record](https://arxiv.org/abs/2512.01374) · [Publication/source](https://arxiv.org/abs/2512.01374)

<a id="paper-jet"></a>

### Jet-RL

**[Jet-RL: Enabling On-Policy FP8 Reinforcement Learning with Unified Training and Rollout Precision Flow](https://arxiv.org/abs/2601.14243v2)**

Authors: Haocheng Xi; Charlie Ruan; Peiyuan Liao; Yujun Lin; Han Cai; Yilong Zhao; Shuo Yang; Kurt Keutzer; Song Han; Ligeng Zhu.

First public: 2026-01-20 · Source version: [v2](https://arxiv.org/abs/2601.14243v2)

- Numerical regime: Unified FP8 learner and rollout paths
- Contribution role: core; evidence domain: direct_low_precision
- Components: A1; A2
- Main discussion: 4.1; additional locations: 6.2
- Scope: Unified FP8 flow; granularity is an associated numerical design choice.

[arXiv record](https://arxiv.org/abs/2601.14243) · [Publication/source](https://arxiv.org/abs/2601.14243)

<a id="paper-fp8rl"></a>

### FP8-RL

**[FP8-RL: A Practical and Stable Low-Precision Stack for LLM Reinforcement Learning](https://arxiv.org/abs/2601.18150v2)**

Authors: Zhaopeng Qiu; Shuang Yu; Jingqi Zhang; Shuai Zhang; Xue Huang; Jingyi Yang; Junjie Lai.

First public: 2026-01-26 · Source version: [v2](https://arxiv.org/abs/2601.18150v2)

- Numerical regime: W8A8 rollout; FP8 attention / KV; FP8 learner explored in v2
- Contribution role: core; evidence domain: direct_low_precision
- Components: A2; system
- Main discussion: 4.2; additional locations: 5.1; 6.2; 6.3
- Scope: FP8 stack; adopted TIS/MIS is not a new correction family.

[arXiv record](https://arxiv.org/abs/2601.18150) · [Publication/source](https://arxiv.org/abs/2601.18150)

<a id="paper-beyond"></a>

### Beyond Precision

**[Beyond Precision: Training-Inference Mismatch is an Optimization Problem and Simple LR Scheduling Fixes It](https://arxiv.org/abs/2602.01826v1)**

Authors: Yaxiang Zhang; Yingru Li; Jiacai Liu; Jiawei Xu; Ziniu Li; Qian Liu; Haoyuan Li.

First public: 2026-02-02 · Source version: [v1](https://arxiv.org/abs/2602.01826v1)

- Numerical regime: General TIM; optimization scheduling
- Contribution role: support; evidence domain: general_TIM
- Components: Support; B3
- Main discussion: 5.3; additional locations: 3.3
- Scope: General TIM scheduling evidence; do not infer FP4 validation.

[arXiv record](https://arxiv.org/abs/2602.01826) · [Publication/source](https://arxiv.org/abs/2602.01826)

<a id="paper-dppo"></a>

### DPPO

**[Rethinking the Trust Region in LLM Reinforcement Learning](https://arxiv.org/abs/2602.04879v3)**

Authors: Penghui Qi; Xiangxin Zhou; Zichen Liu; Tianyu Pang; Chao Du; Min Lin; Wee Sun Lee.

First public: 2026-02-04 · Source version: [v3](https://arxiv.org/abs/2602.04879v3)

- Numerical regime: General LLM trust-region and cross-engine mismatch evidence
- Contribution role: support; evidence domain: general_TIM
- Components: Support; B2
- Main discussion: 5.2; additional locations: 3.2
- Scope: Divergence-based trust-region geometry; do not infer native FP4 or FP8 validation.

[arXiv record](https://arxiv.org/abs/2602.04879) · [Publication/source](https://arxiv.org/abs/2602.04879)

<a id="paper-qurl"></a>

### QuRL

**[QuRL: Low-Precision Reinforcement Learning for Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6b4880ced785077159b340710ceb7681-Abstract-Conference.html)**

Authors: Yuhang Li; Reena Elangovan; Xin Dong; Priyadarshini Panda; Brucek Khailany.

First public: 2026-02-15 · Source version: [ICLR2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6b4880ced785077159b340710ceb7681-Abstract-Conference.html)

- Numerical regime: INT8 / FP8 rollout
- Contribution role: core; evidence domain: direct_low_precision
- Components: B2; A2
- Main discussion: 5.2; additional locations: 3.1; 4.2; 5.4; 6.2
- Scope: ACR and UAQ are distinct components.

[arXiv record](https://arxiv.org/abs/2602.13953) · [Publication/source](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6b4880ced785077159b340710ceb7681-Abstract-Conference.html)

<a id="paper-qarl"></a>

### QaRL

**[QaRL: Rollout-Aligned Quantization-Aware RL for Fast and Stable Training under Training–Inference Mismatch](https://aclanthology.org/2026.findings-acl.841/)**

Authors: Hao Gu; Hao Wang; Jiacheng Liu; Lujun Li; Qiyuan Zhu; Bei Liu; Binxing Xu; Lei Wang; Xintong Yang; Sida Lin; Sirui Han; Yike Guo.

First public: 2026-04-09 · Source version: [ACL2026-Findings](https://aclanthology.org/2026.findings-acl.841/)

- Numerical regime: Quantized MoE rollout; aligned learner QAT
- Contribution role: core; evidence domain: direct_low_precision
- Components: A1; B2
- Main discussion: 4.1; additional locations: 5.2; 5.4; 6.2
- Scope: Aligned QAT and TBPO are distinct components.

[arXiv record](https://arxiv.org/abs/2604.07853) · [Publication/source](https://aclanthology.org/2026.findings-acl.841/)

<a id="paper-p3o"></a>

### P3O / ESS

**[Let the Batch Decide, On- or Off-Policy: Effective Sample Size for RL Post-Training](https://arxiv.org/abs/2605.12380v2)**

Authors: Rasool Fakoor; Murdock Aubry; Nicholas Stranges; Alexander J. Smola.

First public: 2026-05-12 · Source version: [v2](https://arxiv.org/abs/2605.12380v2)

- Numerical regime: BF16 learner / FP8 rollout; dense reasoning models
- Contribution role: core; evidence domain: direct_low_precision
- Components: B2
- Main discussion: 5.2; additional locations: 6.2; 6.3
- Scope: Normalized ESS controls update influence and off-policy regularization.

[arXiv record](https://arxiv.org/abs/2605.12380) · [Publication/source](https://arxiv.org/abs/2605.12380)

<a id="paper-ais"></a>

### AIS

**[AIS: Adaptive Importance Sampling for Quantized RL](https://arxiv.org/abs/2605.13907v1)**

Authors: Jiajun Zhou; Wei Shao; Lingchao Zheng; Yuwei Fan; Ngai Wong.

First public: 2026-05-13 · Source version: [v1](https://arxiv.org/abs/2605.13907v1)

- Numerical regime: BF16 learner / FP8 rollout; autoregressive and diffusion models
- Contribution role: core; evidence domain: direct_low_precision
- Components: B1
- Main discussion: 5.1; additional locations: 6.1; 6.2
- Scope: Adaptive estimator mixture; autoregressive and diffusion evidence distinguished.

[arXiv record](https://arxiv.org/abs/2605.13907) · [Publication/source](https://arxiv.org/abs/2605.13907)

<a id="paper-vexact"></a>

### VeXact / Diagnosing TIM

**[Diagnosing Training Inference Mismatch in LLM Reinforcement Learning via a Zero-Mismatch Reference](https://arxiv.org/abs/2605.14220v2)**

Authors: Tianle Zhong; Neiwen Ling; Yifan Pi; Zijun Wei; Tianshu Yu; Geoffrey Fox; Peng Wu; Xiao Yu.

First public: 2026-05-14 · Source version: [v2](https://arxiv.org/abs/2605.14220v2)

- Numerical regime: Matched-execution diagnostic reference
- Contribution role: support; evidence domain: diagnostic_reference
- Components: Diagnostic
- Main discussion: 3.4; additional locations: none listed
- Scope: Zero-mismatch reference for attribution; not a quantized accelerator.

[arXiv record](https://arxiv.org/abs/2605.14220) · [Publication/source](https://arxiv.org/abs/2605.14220)

<a id="paper-drpo"></a>

### DRPO

**[Rethinking the Divergence Regularization in LLM RL](https://arxiv.org/abs/2606.09821v1)**

Authors: Jiarui Yao; Xiangxin Zhou; Penghui Qi; Wee Sun Lee; Liefeng Bo; Tianyu Pang.

First public: 2026-06-08 · Source version: [v1](https://arxiv.org/abs/2606.09821v1)

- Numerical regime: BF16, FP8 rollout-only, and FP8 end-to-end MoE settings
- Contribution role: core; evidence domain: direct_low_precision
- Components: B2
- Main discussion: 5.2; additional locations: 6.2
- Scope: Smooth divergence-based update control; distinguish the Binary-TV geometry from importance-ratio clipping.

[arXiv record](https://arxiv.org/abs/2606.09821) · [Publication/source](https://arxiv.org/abs/2606.09821)

<a id="paper-mipu"></a>

### MIPU

**[The Mirage of Optimizing Training Policies: Monotonic Inference Policies as the Real Objective for LLM Reinforcement Learning](https://arxiv.org/abs/2606.29526v1)**

Authors: Jing Liang; Hongyao Tang; Yi Ma; Yancheng He; Weixun Wang; Xiaoyang Li; Ju Huang; Wenbo Su; Jinyi Liu; Yan Zheng; Jianye Hao; Bo Zheng.

First public: 2026-06-28 · Source version: [v1](https://arxiv.org/abs/2606.29526v1)

- Numerical regime: BF16 learner / FP8 rollout; Qwen3-1.7B and 4B
- Contribution role: core; evidence domain: direct_low_precision
- Components: B2; formulation
- Main discussion: 5.2; additional locations: 2.1; 6.2; 6.3
- Scope: Sampler-referenced candidates and inference-gap-aware acceptance; practical proxy guarantees are limited.

[arXiv record](https://arxiv.org/abs/2606.29526) · [Publication/source](https://arxiv.org/abs/2606.29526)

<a id="paper-quads"></a>

### QUADS

**[QUADS: Stabilizing NVFP4 Reinforcement Learning for MoE via QUantization-error Alignment across Dual Sides](https://arxiv.org/abs/2607.15810v1)**

Authors: Zhengyang Zhuge; Hao Yu; Xin Wang; Zheng Li; Yizhong Cao; Dayiheng Liu; Jianwei Zhang.

First public: 2026-07-17 · Source version: [v1](https://arxiv.org/abs/2607.15810v1)

- Numerical regime: NVFP4 MoE rollout; learner weight QAT
- Contribution role: core; evidence domain: direct_low_precision
- Components: A1; A2
- Main discussion: 4.1; additional locations: 4.2; 5.4; 6.2
- Scope: Asymmetric QAT plus rollout activation compensation.

[arXiv record](https://arxiv.org/abs/2607.15810) · [Publication/source](https://arxiv.org/abs/2607.15810)

<a id="paper-acrl"></a>

### ACRL

**[ACRL: Adaptive Control of Training-Inference Discrepancy for Stable Reinforcement Learning](https://arxiv.org/abs/2607.24062v1)**

Authors: Wenwu Fan; Qihong Lin; Zhijie Xia; Zhuo Zheng; Sihao Wang; Qiang Chen; Liangsheng Zhu.

First public: 2026-07-27 · Source version: [v1](https://arxiv.org/abs/2607.24062v1)

- Numerical regime: FP8 rollout; discrepancy-dependent updates
- Contribution role: core; evidence domain: direct_low_precision
- Components: B2
- Main discussion: 5.2; additional locations: 3.3; 6.2
- Scope: Advantage-guided, discrepancy-dependent update control.

[arXiv record](https://arxiv.org/abs/2607.24062) · [Publication/source](https://arxiv.org/abs/2607.24062)

<a id="paper-hif4"></a>

### HiFloat4 / Rollout-ResQ

**[HiFloat4 Format for End-To-End Reinforcement Learning Post-Training of Large Language Models](https://arxiv.org/abs/2607.26515v1)**

Authors: Hei Yi Mak; Shadan Golestan; Hoang Le; Mehran Taghian Jazi; Yunke Peng; Yaoyuan Wang; Yao Wang; Junsong Wang; Tianchi Hu; Fengchen He; Guipeng Hu; Tanzila Rahman; Anandharaju Durai Raju.

First public: 2026-07-29 · Source version: [v1](https://arxiv.org/abs/2607.26515v1)

- Numerical regime: Simulated end-to-end HiF4 / MXFP4; rollout residual correction
- Contribution role: core; evidence domain: direct_low_precision
- Components: A2
- Main discussion: 4.2; additional locations: 3.1; 6.2; 6.3
- Scope: Direct rollout activation compensation; all FP4 experiments are simulated, so native speedup is unmeasured.

[arXiv record](https://arxiv.org/abs/2607.26515) · [Publication/source](https://arxiv.org/abs/2607.26515)

<a id="paper-miles"></a>

### Miles v0.1

**[Miles v0.1: Production-Level Post-Training](https://arxiv.org/abs/2609.08368v1)**

Authors: RadixArk; Tom Chen; Mao Cheng; Shi Dong; Kangrui Du; Yanbin Jiang; Jiajun Li; Yiming Li; Tao Lin; Yusheng Su; Andy Ye; Yueming Yuan; Zhichen Zeng.

First public: 2026-09-08 · Source version: [v1](https://arxiv.org/abs/2609.08368v1)

- Numerical regime: FP8 / MXFP8 / NVFP4 RL recipes; precision exceptions
- Contribution role: core; evidence domain: direct_low_precision
- Components: A1; A2; system
- Main discussion: 4.1; additional locations: 4.2; 6.1; 6.3
- Scope: Shared quantization/export contracts and integration evidence; MXFP8/NVFP4 recipes remain Beta.

[arXiv record](https://arxiv.org/abs/2609.08368) · [Publication/source](https://arxiv.org/abs/2609.08368)

<a id="paper-score"></a>

### Score Centering

**[Score Centering Stabilizes Off-policy Reinforcement Learning](https://arxiv.org/abs/2609.20807v1)**

Authors: Martin Marek; Max Ryabinin.

First public: 2026-09-17 · Source version: [v1](https://arxiv.org/abs/2609.20807v1)

- Numerical regime: BF16 learner; quantized sampler including FP4/INT4 KV variants; separate policy-lag tests
- Contribution role: core; evidence domain: direct_low_precision
- Components: B1
- Main discussion: 5.1; additional locations: 2.2; 3.2; 5.4; 6.2
- Scope: Additive score correction; not full on-policy recovery.

[arXiv record](https://arxiv.org/abs/2609.20807) · [Publication/source](https://arxiv.org/abs/2609.20807)

<a id="paper-fullfp8"></a>

### Full Pipeline FP8 RL

**[Towards Full Pipeline FP8 Reinforcement Learning for LLMs](https://arxiv.org/abs/2609.22870v1)**

Authors: Fanchao Chen; Ziheng Jiang; Ziyun Wei; Zheng Zhong; Du Li; Chi Zhang; Haibin Lin; Shivaram Venkataraman.

First public: 2026-09-19 · Source version: [v1](https://arxiv.org/abs/2609.22870v1)

- Numerical regime: FP8 learner and rollout; calibration against BF16
- Contribution role: core; evidence domain: direct_low_precision
- Components: B2; system
- Main discussion: 5.2; additional locations: 3.2; 6.2; 6.3
- Scope: Clipping calibration; distinguish from quantizer calibration.

[arXiv record](https://arxiv.org/abs/2609.22870) · [Publication/source](https://arxiv.org/abs/2609.22870)

<a id="paper-cis"></a>

### CIS

**[Rethinking Training-Inference Mismatch in LLM Reinforcement Learning: Where It Arises and How to Correct It](https://arxiv.org/abs/2609.32444v1)**

Authors: Tianrun Yu; Kaixiang Zhao; Shangzhe Li; Yuxiao Yang; Porter Jenkins; Weitong Zhang; Taylor W. Killian.

First public: 2026-09-26 · Source version: [v1](https://arxiv.org/abs/2609.32444v1)

- Numerical regime: BF16 cross-engine mismatch
- Contribution role: support; evidence domain: general_TIM
- Components: Support; B1
- Main discussion: 5.1; additional locations: 3.2
- Scope: Calibrated importance sampling; BF16 cross-engine evidence.

[arXiv record](https://arxiv.org/abs/2609.32444) · [Publication/source](https://arxiv.org/abs/2609.32444)

<a id="paper-qatfactory"></a>

### QATFactory / QARL

**[QATFactory: A Versatile, Deployment-Aligned Framework for Quantization-aware Training and Distillation of LLMs](https://arxiv.org/abs/2609.39223v2)**

Authors: Weili Xu; Jisen Li; Yuqing Jian; Chenxi Li; Zhizhou Sha; Yifan Yu; Qingyang Wu; Chenfeng Xu; Zhongzhu Zhou; Tianyi Zhang; Ben Athiwaratkun.

First public: 2026-09-30 · Source version: [v2](https://arxiv.org/abs/2609.39223v2)

- Numerical regime: Native NVFP4 rollout; simulated-quantization BF16 training
- Contribution role: core; evidence domain: direct_low_precision
- Components: A1; system
- Main discussion: 4.1; additional locations: 6.2; 6.3
- Scope: The QARL component is focal; the framework also includes separate QAD/PTQ studies.

[arXiv record](https://arxiv.org/abs/2609.39223) · [Publication/source](https://arxiv.org/abs/2609.39223)

<a id="paper-triage"></a>

### TRIAGE

**[TRIAGE: Direction-Aware Mismatch Stabilization of Native NVFP4 Reinforcement Learning](https://arxiv.org/abs/2610.07043v2)**

Authors: Zhen Li; Shuai Zhang; Yanggan Gu; Yiming Zhang; Yang Yu; Mingfa Feng; Congkai Xie; Shuang Yu; Junjie Lai; Hongxia Yang.

First public: 2026-10-05 · Source version: [v2](https://arxiv.org/abs/2610.07043v2)

- Numerical regime: Native NVFP4 W4A4 forward on both endpoints; documented BF16 KV; synchronous math RL
- Contribution role: core; evidence domain: direct_low_precision
- Components: B2
- Main discussion: 5.2; additional locations: 3.3; 6.2
- Scope: Direction-aware control under native W4A4 execution.

[arXiv record](https://arxiv.org/abs/2610.07043) · [Publication/source](https://arxiv.org/abs/2610.07043)

<a id="paper-trace"></a>

### TRACE

**[TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models](https://arxiv.org/abs/2610.07767v2)**

Authors: Xin Wang; Hao Yu; Zhengyang Zhuge; Bochao Mao; Zheng Li; Junda Feng; Yuyan Luo; Yi Zhang; Yizhong Cao; Mi Zhang; Dayiheng Liu; Jianwei Zhang.

First public: 2026-10-06 · Source version: [v2](https://arxiv.org/abs/2610.07767v2)

- Numerical regime: NVFP4 expert W4A4 + softmax KV4 rollout; guided fake-quantized learner forward, BF16 backward; asynchronous
- Contribution role: core; evidence domain: direct_low_precision
- Components: A1
- Main discussion: 4.1; additional locations: 3.1; 6.2
- Scope: Rollout-guided rounding; local guarantees have limited scope.

[arXiv record](https://arxiv.org/abs/2610.07767) · [Publication/source](https://arxiv.org/abs/2610.07767)

<a id="paper-kv4"></a>

### KV4-RL

**[KV4-RL: Unlocking Faster Asynchronous Rollouts for RLVR with INT4 KV Cache Quantization](https://arxiv.org/abs/2610.14448v1)**

Authors: Sihwan Park; Sung-Yub Kim; Doohyuk Jang; Eunho Yang.

First public: 2026-10-10 · Source version: [v1](https://arxiv.org/abs/2610.14448v1)

- Numerical regime: BF16 learner; INT4 KV with bounded INT8 protection; quota-based partial collection
- Contribution role: core; evidence domain: direct_low_precision
- Components: A2; system
- Main discussion: 4.2; additional locations: 5.1; 6.2; 6.3
- Scope: INT4 KV with selective protection; colocated partial rollout.

[arXiv record](https://arxiv.org/abs/2610.14448) · [Publication/source](https://arxiv.org/abs/2610.14448)

<a id="paper-scorebaseline"></a>

### Baselines and Score Centering

**[Baselines and Score Centering in Policy Gradient Estimation](https://arxiv.org/abs/2610.22263v1)**

Authors: Shuo Han; Ziqing Hu.

First public: 2026-10-15 · Source version: [v1](https://arxiv.org/abs/2610.22263v1)

- Numerical regime: Sequence- and token-level regularized importance sampling
- Contribution role: support; evidence domain: general_TIM
- Components: Support; B1
- Main discussion: 5.1; additional locations: 5.4
- Scope: Covariance analysis of group baselines and score centering; theoretical support, not a quantized accelerator.

[arXiv record](https://arxiv.org/abs/2610.22263) · [Publication/source](https://arxiv.org/abs/2610.22263)
