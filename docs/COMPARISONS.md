# Comparing mechanisms, configurations and evidence

A method class describes what an intervention changes. Its experimental configuration describes where the source tested it. These selected records keep the two separate.

The comparisons retain the numerical configurations, baselines, and evaluation rules reported in each primary study.

## Execution configurations

| Study | Learner | Rollout | Collection and scope |
|---|---|---|---|
| **Jet-RL**<br>[Jet-RL: Enabling On-Policy FP8 Reinforcement Learning with Unified Training and Rollout Precision Flow](https://arxiv.org/abs/2601.14243v2) | FP8 GEMMs with unified precision flow | FP8 execution coordinated with the learner path | Updated actor weights transfer to the inference engine after each step; vLLM and verl implementation. Operator-level FP8 does not imply that every module and training state is FP8. [Source](https://arxiv.org/abs/2601.14243v2), Sections 2.1 and 4.1-4.3. |
| **FP8-RL**<br>[FP8-RL: A Practical and Stable Low-Precision Stack for LLM Reinforcement Learning](https://arxiv.org/abs/2601.18150v2) | Higher-precision learner with repeated calibration and weight synchronization | Native W8A8 linear layers; FP8 attention and KV extensions | Step-wise rollout/training workflow with dynamic QKV-scale recalibration. Each extension has its own precision exceptions and calibration cost. [Source](https://arxiv.org/abs/2601.18150v2), Sections 2.1-2.3; Figures 1 and 4. |
| **QaRL**<br>[QaRL: Rollout-Aligned Quantization-Aware RL for Fast and Stable Training under Training--Inference Mismatch](https://aclanthology.org/2026.findings-acl.841/) | Rollout-aligned fake quantization in the learner forward | W8A8 and W4A16 configurations; W4A8 in quantization ablations | Quantized rollout and aligned learner under TBPO; numerical targets are tested across model regimes. KV quantization is excluded; QAT should not be read as a measured native low-bit trainer speedup. [Source](https://aclanthology.org/2026.findings-acl.841/), Sections 3-4; Figure 9; Appendix A. |
| **HiFloat4 / Rollout-ResQ**<br>[HiFloat4 Format for End-To-End Reinforcement Learning Post-Training of Large Language Models](https://arxiv.org/abs/2607.26515v1) | QAT under simulated FP4 execution | HiFloat4 and MXFP4 with Rollout-ResQ activation compensation | Simulated low-precision RL experiments. Simulation overhead prevents direct measurement of native-FP4 speedup. [Source](https://arxiv.org/abs/2607.26515v1), Sections 4-6; Limitations and Future Directions. |
| **TRACE**<br>[TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models](https://arxiv.org/abs/2610.07767v2) | Guided fake-quantized forward; BF16 backward | NVFP4 W4A4 routed experts + NVFP4 KV in softmax attention; other modules BF16 | Asynchronous; routing replay and importance correction retained. No native-FP4 trainer acceleration is established. [Source](https://arxiv.org/abs/2610.07767v2), Sections 3.1 and 4; Table 1. |
| **TRIAGE**<br>[TRIAGE: Direction-Aware Mismatch Stabilization of Native NVFP4 Reinforcement Learning](https://arxiv.org/abs/2610.07043v2) | Native NVFP4 W4A4 forward; higher-precision training state remains | Native W4A4; KV is BF16 in documented characterization | Synchronous math RL on Qwen3-4B and Qwen3-30B-A3B. No KV4 experiment or direct SC/TIS+SC comparison is reported. [Source](https://arxiv.org/abs/2610.07043v2), Section 5; Appendix B.1; Table 1. |
| **Score Centering**<br>[Score Centering Stabilizes Off-policy Reinforcement Learning](https://arxiv.org/abs/2609.20807v1) | BF16 learner; top-k behavior reconstruction | Quantization stress includes FP4 KV and INT8 sampler with INT4 KV | Quantization and policy-lag tests are separate settings. Shared-objective controls and training-accuracy curves are not full-recipe replications or a universal held-out ranking. [Source](https://arxiv.org/abs/2609.20807v1), Sections 5.1-5.4; Appendix D. |
| **KV4-RL**<br>[KV4-RL: Unlocking Faster Asynchronous Rollouts for RLVR with INT4 KV Cache Quantization](https://arxiv.org/abs/2610.14448v1) | BF16 | INT4 KV with bounded INT8 protection; cache-focused execution | Quota-based partial collection; generation and learning alternate. Common BF16 evaluation isolates learned-policy quality; no joint W4A4/KV4 training result is established. [Source](https://arxiv.org/abs/2610.14448v1), Sections 5.2 and 6; Appendix A.1. |

## Direct comparison cases

### TRACE versus TIS+SC

**Setting.** Qwen3.5-35B-A3B; joint NVFP4 expert W/A and KV rollout; four reasoning/code benchmarks

**Compared.** TRACE; TIS+SC (cap 2, top-128 reconstruction); BF16 reference

**Reported outcome.** Reported task mean: TRACE 75.3; TIS+SC 74.1; BF16 74.9.

**Checkpoint and repetition rule.** SC is selected by its highest four-task mean through 400 training steps.

**Interpretation.** TRACE and TIS+SC each lead on two of the four tasks; Table 6 provides no uncertainty interval. This is not a TRIAGE comparison.

[Primary source](https://arxiv.org/abs/2610.07767v2) · Section 4.4; Table 6

### TRIAGE versus TIS under native W4A4

**Setting.** Qwen3-30B-A3B; synchronous math RL; native NVFP4 W4A4 forward

**Compared.** BF16; native NVFP4; NVFP4+TIS; full TRIAGE

**Reported outcome.** At step 1700, five-task mean: TRIAGE 70.96; TIS 63.18; BF16 72.41.

**Checkpoint and repetition rule.** Stable arms use their final step 1700. Collapsed naive NVFP4 uses the saved step-700 checkpoint.

**Interpretation.** No direct SC/TIS+SC, TRACE or KV4 comparison is reported. Stability is observed only within the evaluated horizon.

[Primary source](https://arxiv.org/abs/2610.07043v2) · Section 5.1-5.2; Table 1; Section 8

### KV4-RL versus cache-precision controls

**Setting.** Qwen3-8B-Base; 400 updates; TIS retained; common BF16 evaluation

**Compared.** BF16, KV8, unprotected KV4 and selectively protected KV4-RL

**Reported outcome.** Final six-task mean: KV4-RL 52.8, BF16 52.4. Cumulative rollout/full-iteration speedups: 1.80x/1.27x.

**Checkpoint and repetition rule.** Final step 400; one training run per precision in the documented 8B learning-curve study, with three evaluation seeds.

**Interpretation.** Evaluation-seed standard deviations do not measure variability across independent training runs. Timing is specific to this collection workload.

[Primary source](https://arxiv.org/abs/2610.14448v1) · Sections 6.1-6.3; Table 1; Appendix D.5

## Read the measurements together

| Measurement | Interpretation |
|---|---|
| Policy entropy | Uncertainty of a specified next-token distribution; neither a quality score nor evidence that entropy regularization is active. |
| Mean training reward | Scores of collected responses under a stated reward rule; distinct from group advantages and held-out quality. |
| Mean absolute log-probability gap | Agreement on sampled tokens; averaging removes direction and local concentration. |
| Held-out quality | Requires the evaluation precision, decoding and checkpoint rule. A common BF16 evaluator and a deployed low-precision evaluator answer different questions. |
| Rollout and iteration time | Different timing scopes. Generation length, concurrency, synchronization and guidance can affect total cost. |

Interpret outcomes under their stated execution and evaluation conditions. Checkpoint selection and timing scope can change the comparison.

[Survey PDF](../Survey.pdf) · [Full catalog](CATALOG.md) · [Source observations](EVIDENCE.md) · [Classification](TAXONOMY.md)
