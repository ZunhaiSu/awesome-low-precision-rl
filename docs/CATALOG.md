# Reviewed paper catalog

Generated from `data/papers.json`. Dates and versions identify the reviewed snapshot, not a claim that a source has never changed.

The catalog separates contribution role, evidence domain, and numerical regime. No independent reproduction was performed for this survey; this status makes no claim about reproductions elsewhere. Code availability, seed counts, and experiment-level model/task coverage are not systematically audited here.

## FlashRL / TIS

**On the Rollout-Training Mismatch in Modern RL Systems**

Authors: Feng Yao; Liyuan Liu; Dinghuai Zhang; Chengyu Dong; Jingbo Shang; Jianfeng Gao.

First public: 2025 · Reviewed record: [OPT2025](https://www.opt-ml.org/papers/2025/paper116.pdf) · Source snapshot checked: 2026-10-19

- Numerical regime: Higher-precision learner; quantized rollout
- Contribution role: core; evidence domain: direct_low_precision
- Components: B1
- Main discussion: 5.1; additional locations: 1.1; 2.1
- Scope: Quantized rollout; recorded behavior probabilities.

## QeRL

**QeRL: Quantization-enhanced Low-Rank Reinforcement Learning for LLMs**

Authors: Wei Huang; Yi Ge; Shuai Yang; Yicheng Xiao; Huizi Mao; Yujun Lin; Hanrong Ye; Sifei Liu; Ka Chun Cheung; Hongxu Yin; Yao Lu; Xiaojuan Qi; Song Han; Yukang Chen.

First public: 2025-10-13 · Reviewed record: [ICLR2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a15a2ece7f0663d1ba7db91103ac61c9-Abstract-Conference.html) · Source snapshot checked: 2026-10-19

- Numerical regime: NVFP4 with LoRA and adaptive noise
- Contribution role: boundary; evidence domain: exploration_boundary
- Components: Boundary
- Main discussion: Box 1; additional locations: none listed
- Scope: NVFP4 with LoRA and adaptive noise; exploration setting.

[arXiv record](https://arxiv.org/abs/2510.11696) · [Publication/source](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a15a2ece7f0663d1ba7db91103ac61c9-Abstract-Conference.html)

## R3

**Stabilizing MoE Reinforcement Learning by Aligning Training and Inference Routers**

Authors: Wenhan Ma; Hailin Zhang; Liang Zhao; Yifan Song; Yudong Wang; Zhifang Sui; Fuli Luo.

First public: 2025-10-13 · Reviewed record: [v2](https://arxiv.org/abs/2510.11370v2) · Source snapshot checked: 2026-10-19

- Numerical regime: MoE routing; general execution mismatch
- Contribution role: support; evidence domain: general_TIM
- Components: Support; A1
- Main discussion: 3.1; additional locations: 4.1
- Scope: MoE routing replay; routing mismatch is not uniquely quantization-induced.

[arXiv record](https://arxiv.org/abs/2510.11370) · [Publication/source](https://arxiv.org/abs/2510.11370)

## FP16-Mismatch

**Defeating the Training-Inference Mismatch via FP16**

Authors: Penghui Qi; Zichen Liu; Xiangxin Zhou; Tianyu Pang; Chao Du; Wee Sun Lee; Min Lin.

First public: 2025-10-30 · Reviewed record: [v1](https://arxiv.org/abs/2510.26788v1) · Source snapshot checked: 2026-10-19

- Numerical regime: BF16 / FP16 numerical comparison
- Contribution role: support; evidence domain: higher_precision_comparison
- Components: Support; A2
- Main discussion: 3.1; additional locations: none listed
- Scope: BF16/FP16 numerical evidence; not a low-bit acceleration method.

[arXiv record](https://arxiv.org/abs/2510.26788) · [Publication/source](https://arxiv.org/abs/2510.26788)

## MiniRL

**Stabilizing Reinforcement Learning with LLMs: Formulation and Practices**

Authors: Chujie Zheng; Kai Dang; Bowen Yu; Mingze Li; Huiqiang Jiang; Junrong Lin; Yuqiong Liu; Hao Lin; Chencan Wu; Feng Hu; An Yang; Jingren Zhou; Junyang Lin.

First public: 2025-12-01 · Reviewed record: [v3](https://arxiv.org/abs/2512.01374v3) · Source snapshot checked: 2026-10-19

- Numerical regime: Hybrid-engine RL; includes FP8-rollout experiments
- Contribution role: support; evidence domain: direct_low_precision
- Components: Support; B1/B2
- Main discussion: 2.1; additional locations: 1.2; 5.1
- Scope: Formulation role; also contains direct FP8 rollout experiments.

[arXiv record](https://arxiv.org/abs/2512.01374) · [Publication/source](https://arxiv.org/abs/2512.01374)

## Jet-RL

**Jet-RL: Enabling On-Policy FP8 Reinforcement Learning with Unified Training and Rollout Precision Flow**

Authors: Haocheng Xi; Charlie Ruan; Peiyuan Liao; Yujun Lin; Han Cai; Yilong Zhao; Shuo Yang; Kurt Keutzer; Song Han; Ligeng Zhu.

First public: 2026-01-20 · Reviewed record: [v2](https://arxiv.org/abs/2601.14243v2) · Source snapshot checked: 2026-10-19

- Numerical regime: Unified FP8 learner and rollout paths
- Contribution role: core; evidence domain: direct_low_precision
- Components: A1; A2
- Main discussion: 4.1; additional locations: 6.2
- Scope: Unified FP8 flow; granularity is an associated numerical design choice.

[arXiv record](https://arxiv.org/abs/2601.14243) · [Publication/source](https://arxiv.org/abs/2601.14243)

## FP8-RL

**FP8-RL: A Practical and Stable Low-Precision Stack for LLM Reinforcement Learning**

Authors: Zhaopeng Qiu; Shuang Yu; Jingqi Zhang; Shuai Zhang; Xue Huang; Jingyi Yang; Junjie Lai.

First public: 2026-01-26 · Reviewed record: [v2](https://arxiv.org/abs/2601.18150v2) · Source snapshot checked: 2026-10-19

- Numerical regime: W8A8 rollout; FP8 attention / KV; FP8 learner explored in v2
- Contribution role: core; evidence domain: direct_low_precision
- Components: A2; system
- Main discussion: 4.2; additional locations: 5.1; 6.2; 6.3
- Scope: FP8 stack; adopted TIS/MIS is not a new correction family.

[arXiv record](https://arxiv.org/abs/2601.18150) · [Publication/source](https://arxiv.org/abs/2601.18150)

## Beyond Precision

**Beyond Precision: Training-Inference Mismatch is an Optimization Problem and Simple LR Scheduling Fixes It**

Authors: Yaxiang Zhang; Yingru Li; Jiacai Liu; Jiawei Xu; Ziniu Li; Qian Liu; Haoyuan Li.

First public: 2026-02-02 · Reviewed record: [arXiv record](https://arxiv.org/abs/2602.01826) · Source snapshot checked: 2026-10-19

- Numerical regime: General TIM; optimization scheduling
- Contribution role: support; evidence domain: general_TIM
- Components: Support; B3
- Main discussion: 5.3; additional locations: 3.3
- Scope: General TIM scheduling evidence; do not infer FP4 validation.

[arXiv record](https://arxiv.org/abs/2602.01826) · [Publication/source](https://arxiv.org/abs/2602.01826)

## QuRL

**QuRL: Efficient Reinforcement Learning with Quantized Rollout**

Authors: Yuhang Li; Reena Elangovan; Xin Dong; Priyadarshini Panda; Brucek Khailany.

First public: 2026-02-15 · Reviewed record: [ICLR2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6b4880ced785077159b340710ceb7681-Abstract-Conference.html) · Source snapshot checked: 2026-10-19

- Numerical regime: INT8 / FP8 rollout
- Contribution role: core; evidence domain: direct_low_precision
- Components: B2; A2
- Main discussion: 5.2; additional locations: 3.1; 4.2; 5.4; 6.2
- Scope: ACR and UAQ are distinct components.

[arXiv record](https://arxiv.org/abs/2602.13953) · [Publication/source](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6b4880ced785077159b340710ceb7681-Abstract-Conference.html)

## QaRL

**QaRL: Rollout-Aligned Quantization-Aware RL for Fast and Stable Training under Training--Inference Mismatch**

Authors: Hao Gu; Hao Wang; Jiacheng Liu; Lujun Li; Qiyuan Zhu; Bei Liu; Binxing Xu; Lei Wang; Xintong Yang; Sida Lin; Sirui Han; Yike Guo.

First public: 2026-04-09 · Reviewed record: [ACL2026-Findings](https://aclanthology.org/2026.findings-acl.841/) · Source snapshot checked: 2026-10-19

- Numerical regime: Quantized MoE rollout; aligned learner QAT
- Contribution role: core; evidence domain: direct_low_precision
- Components: A1; B2
- Main discussion: 4.1; additional locations: 5.2; 5.4; 6.2
- Scope: Aligned QAT and TBPO are distinct components.

[arXiv record](https://arxiv.org/abs/2604.07853) · [Publication/source](https://aclanthology.org/2026.findings-acl.841/)

## AIS

**AIS: Adaptive Importance Sampling for Quantized RL**

Authors: Jiajun Zhou; Wei Shao; Lingchao Zheng; Yuwei Fan; Ngai Wong.

First public: 2026-05-13 · Reviewed record: [v1](https://arxiv.org/abs/2605.13907v1) · Source snapshot checked: 2026-10-19

- Numerical regime: BF16 learner / FP8 rollout; autoregressive and diffusion models
- Contribution role: core; evidence domain: direct_low_precision
- Components: B1
- Main discussion: 5.1; additional locations: 6.1; 6.2
- Scope: Adaptive estimator mixture; autoregressive and diffusion evidence distinguished.

[arXiv record](https://arxiv.org/abs/2605.13907) · [Publication/source](https://arxiv.org/abs/2605.13907)

## VeXact / Diagnosing TIM

**Diagnosing Training Inference Mismatch in LLM Reinforcement Learning via a Zero-Mismatch Reference**

Authors: Tianle Zhong; Neiwen Ling; Yifan Pi; Zijun Wei; Tianshu Yu; Geoffrey Fox; Peng Wu; Xiao Yu.

First public: 2026-05-14 · Reviewed record: [arXiv record](https://arxiv.org/abs/2605.14220) · Source snapshot checked: 2026-10-19

- Numerical regime: Matched-execution diagnostic reference
- Contribution role: support; evidence domain: diagnostic_reference
- Components: Diagnostic
- Main discussion: 3.4; additional locations: none listed
- Scope: Zero-mismatch reference for attribution; not a quantized accelerator.

[arXiv record](https://arxiv.org/abs/2605.14220) · [Publication/source](https://arxiv.org/abs/2605.14220)

## QUADS

**QUADS: Stabilizing NVFP4 Reinforcement Learning for MoE via QUantization-error Alignment across Dual Sides**

Authors: Zhengyang Zhuge; Hao Yu; Xin Wang; Zheng Li; Yizhong Cao; Dayiheng Liu; Jianwei Zhang.

First public: 2026-07-17 · Reviewed record: [v1](https://arxiv.org/abs/2607.15810v1) · Source snapshot checked: 2026-10-19

- Numerical regime: NVFP4 MoE rollout; learner weight QAT
- Contribution role: core; evidence domain: direct_low_precision
- Components: A1; A2
- Main discussion: 4.1; additional locations: 4.2; 5.4; 6.2
- Scope: Asymmetric QAT plus rollout activation compensation.

[arXiv record](https://arxiv.org/abs/2607.15810) · [Publication/source](https://arxiv.org/abs/2607.15810)

## ACRL

**ACRL: Adaptive Control of Training-Inference Discrepancy for Stable Reinforcement Learning**

Authors: Wenwu Fan; Qihong Lin; Zhijie Xia; Zhuo Zheng; Sihao Wang; Qiang Chen; Liangsheng Zhu.

First public: 2026-07-27 · Reviewed record: [v1](https://arxiv.org/abs/2607.24062v1) · Source snapshot checked: 2026-10-19

- Numerical regime: FP8 rollout; discrepancy-dependent updates
- Contribution role: core; evidence domain: direct_low_precision
- Components: B2
- Main discussion: 5.2; additional locations: 3.3; 6.2
- Scope: Advantage-guided, discrepancy-dependent update control.

[arXiv record](https://arxiv.org/abs/2607.24062) · [Publication/source](https://arxiv.org/abs/2607.24062)

## Score Centering

**Score Centering Stabilizes Off-policy Reinforcement Learning**

Authors: Martin Marek; Max Ryabinin.

First public: 2026-09-17 · Reviewed record: [v1](https://arxiv.org/abs/2609.20807v1) · Source snapshot checked: 2026-10-19

- Numerical regime: BF16 learner; quantized rollout or policy lag
- Contribution role: core; evidence domain: direct_low_precision
- Components: B1
- Main discussion: 5.1; additional locations: 2.2; 3.2; 5.4; 6.2
- Scope: Additive score correction; not full on-policy recovery.

[arXiv record](https://arxiv.org/abs/2609.20807) · [Publication/source](https://arxiv.org/abs/2609.20807)

## Full Pipeline FP8 RL

**Towards Full Pipeline FP8 Reinforcement Learning for LLMs**

Authors: Fanchao Chen; Ziheng Jiang; Ziyun Wei; Zheng Zhong; Du Li; Chi Zhang; Haibin Lin; Shivaram Venkataraman.

First public: 2026-09-19 · Reviewed record: [v1](https://arxiv.org/abs/2609.22870v1) · Source snapshot checked: 2026-10-19

- Numerical regime: FP8 learner and rollout; calibration against BF16
- Contribution role: core; evidence domain: direct_low_precision
- Components: B2; system
- Main discussion: 5.2; additional locations: 3.2; 6.2; 6.3
- Scope: Clipping calibration; distinguish from quantizer calibration.

[arXiv record](https://arxiv.org/abs/2609.22870) · [Publication/source](https://arxiv.org/abs/2609.22870)

## CIS

**Rethinking Training-Inference Mismatch in LLM Reinforcement Learning: Where It Arises and How to Correct It**

Authors: Tianrun Yu; Kaixiang Zhao; Shangzhe Li; Yuxiao Yang; Porter Jenkins; Weitong Zhang; Taylor W. Killian.

First public: 2026-09-26 · Reviewed record: [arXiv record](https://arxiv.org/abs/2609.32444) · Source snapshot checked: 2026-10-19

- Numerical regime: BF16 cross-engine mismatch
- Contribution role: support; evidence domain: general_TIM
- Components: Support; B1
- Main discussion: 5.1; additional locations: 3.2
- Scope: Calibrated importance sampling; BF16 cross-engine evidence.

[arXiv record](https://arxiv.org/abs/2609.32444) · [Publication/source](https://arxiv.org/abs/2609.32444)

## TRIAGE

**TRIAGE: Direction-Aware Mismatch Stabilization of Native NVFP4 Reinforcement Learning**

Authors: Zhen Li; Shuai Zhang; Yanggan Gu; Yiming Zhang; Yang Yu; Mingfa Feng; Congkai Xie; Shuang Yu; Junjie Lai; Hongxia Yang.

First public: 2026-10-05 · Reviewed record: [v2](https://arxiv.org/abs/2610.07043v2) · Source snapshot checked: 2026-10-19

- Numerical regime: Native NVFP4 W4A4; MoE analysis
- Contribution role: core; evidence domain: direct_low_precision
- Components: B2
- Main discussion: 5.2; additional locations: 3.3; 6.2
- Scope: Direction-aware control under native W4A4 execution.

[arXiv record](https://arxiv.org/abs/2610.07043) · [Publication/source](https://arxiv.org/abs/2610.07043)

## TRACE

**TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models**

Authors: Xin Wang; Hao Yu; Zhengyang Zhuge; Bochao Mao; Zheng Li; Junda Feng; Yuyan Luo; Yi Zhang; Yizhong Cao; Mi Zhang; Dayiheng Liu; Jianwei Zhang.

First public: 2026-10-06 · Reviewed record: [v2](https://arxiv.org/abs/2610.07767v2) · Source snapshot checked: 2026-10-19

- Numerical regime: FP4 MoE rollout; guided learner QAT
- Contribution role: core; evidence domain: direct_low_precision
- Components: A1
- Main discussion: 4.1; additional locations: 3.1; 6.2
- Scope: Rollout-guided rounding; local guarantees have limited scope.

[arXiv record](https://arxiv.org/abs/2610.07767) · [Publication/source](https://arxiv.org/abs/2610.07767)

## KV4-RL

**KV4-RL: Unlocking Faster Asynchronous Rollouts for RLVR with INT4 KV Cache Quantization**

Authors: Sihwan Park; Sung-Yub Kim; Doohyuk Jang; Eunho Yang.

First public: 2026-10-10 · Reviewed record: [v1](https://arxiv.org/abs/2610.14448v1) · Source snapshot checked: 2026-10-19

- Numerical regime: INT4 KV with bounded INT8 protection
- Contribution role: core; evidence domain: direct_low_precision
- Components: A2; system
- Main discussion: 4.2; additional locations: 5.1; 6.2; 6.3
- Scope: INT4 KV with selective protection; colocated partial rollout.

[arXiv record](https://arxiv.org/abs/2610.14448) · [Publication/source](https://arxiv.org/abs/2610.14448)
