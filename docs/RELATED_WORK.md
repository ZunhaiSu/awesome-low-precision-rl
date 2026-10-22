# Perspectives from the primary literature

The primary papers organize neighboring work from different viewpoints. This guide relates those viewpoints to the survey’s component framework. Interpretations refer to the reviewed versions linked below; method-level descriptions are checked against the source methods, rather than inferred only from a related-work label.

## Scope among surveys

| Survey | Organizing scope | Connection to this review |
|---|---|---|
| [Generate, Filter, Control, Replay: A Comprehensive Survey of Rollout Strategies for LLM Reinforcement Learning](https://arxiv.org/abs/2605.02913v1) | Lifecycle functions of rollout pipelines. | Provides the broader data-collection context. |
| [Rollout Efficiency in Reinforcement Learning for Reasoning Large Language Models: A Taxonomy and Future Directions](https://arxiv.org/abs/2609.25463v1) | Mechanisms and bottlenecks of rollout efficiency, composition, and reporting. | Provides the broader efficiency context. |
| [Training–Rollout Mismatch in Low-Precision LLM Reinforcement Learning: A Survey](../Survey.pdf) | Numerical discrepancies, estimation, update decisions, and learning consequences. | Connects intervention targets to the information and evidence needed to assess their effects. |

## Three complementary views

| View | Question | Role in the survey |
|---|---|---|
| Mismatch source | Why do probabilities differ: numerical execution, routing, or parameter lag? | Problem formulation and mechanism analysis. |
| Intervention target | What does the component change: computation, numerical information, estimation, or update control? | Four primary method classes. |
| Execution setting | Where was it tested: W/A/KV, adaptation, arithmetic, architecture, and collection? | Scope and interpretation of evidence. |

These are complementary descriptions, not mutually exclusive paper buckets. A component can address several sources, and several classes can appear within one system.

## Organizing perspectives in the reviewed papers

| Paper and source location | Organizing perspective | Implication for this survey |
|---|---|---|
| **Jet-RL**<br>[Jet-RL: Enabling On-Policy FP8 Reinforcement Learning with Unified Training and Rollout Precision Flow](https://arxiv.org/abs/2601.14243v2)<br>Section 6 | Separates low-precision training/inference, LLM RL, and efficient reasoning. | Keep arithmetic scope, learning procedure and systems efficiency distinct. |
| **FP8-RL**<br>[FP8-RL: A Practical and Stable Low-Precision Stack for LLM Reinforcement Learning](https://arxiv.org/abs/2601.18150v2)<br>Section 3 | Separates FP8 quantization, RL systems, and training–inference mismatch. | Treat correction and stack integration as different contributions. |
| **QuRL**<br>[QuRL: Low-Precision Reinforcement Learning for Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6b4880ced785077159b340710ceb7681-Abstract-Conference.html)<br>Section 2; mechanism check in Section 4 | Uses PTQ/QAT as quantization context, then explains its repeated-quantization RL setting. | Avoid forcing every quantized RL method into static PTQ or explicit learner-side QAT. |
| **QaRL**<br>[QaRL: Rollout-Aligned Quantization-Aware RL for Fast and Stable Training under Training--Inference Mismatch](https://aclanthology.org/2026.findings-acl.841/)<br>Section 5 | Discusses quantization procedures alongside LLM policy-optimization variants. | Keep QAT adaptation separate from the TBPO update component. |
| **P3O / ESS**<br>[Let the Batch Decide, On- or Off-Policy: Effective Sample Size for RL Post-Training](https://arxiv.org/abs/2605.12380v2)<br>Appendix E | Distinguishes quantized-weight remedies, objective adaptation and in-flight policy updates. | Treat proposed component combinations as hypotheses until evaluated; distinguish token behavior records from a single response checkpoint. |
| **AIS**<br>[AIS: Adaptive Importance Sampling for Quantized RL](https://arxiv.org/abs/2605.13907v1)<br>Appendix B; mechanism check in Section 3.1 | Separates numerical compression from infrastructure and asynchronous RL. | AIS adapts the strength of a truncated importance correction through an estimator mixture; this is not simply an adaptive clipping boundary. |
| **DRPO**<br>[Rethinking the Divergence Regularization in LLM RL](https://arxiv.org/abs/2606.09821v1)<br>Appendix A | Separates ratio-based or divergence-based trust-region geometry from hard or smooth enforcement. | Use constraint geometry as a B2 decision; the presence of an importance ratio does not alone define an estimator-correction contribution. |
| **MIPU**<br>[The Mirage of Optimizing Training Policies: Monotonic Inference Policies as the Real Objective for LLM Reinforcement Learning](https://arxiv.org/abs/2606.29526v1)<br>Section 3 | Contrasts system-side mismatch reduction, sampler-aware update remedies, and inference-policy acceptance. | Separate constructing a learner update from accepting its synchronized inference-policy realization. |
| **QUADS**<br>[QUADS: Stabilizing NVFP4 Reinforcement Learning for MoE via QUantization-error Alignment across Dual Sides](https://arxiv.org/abs/2607.15810v1)<br>Section 5 | Distinguishes RL context, low-precision rollout, and TIM remedies; emphasizes weight/activation asymmetry. | Retain separate components for learner weight alignment and rollout activation compensation. |
| **HiFloat4 / Rollout-ResQ**<br>[HiFloat4 Format for End-To-End Reinforcement Learning Post-Training of Large Language Models](https://arxiv.org/abs/2607.26515v1)<br>Section 2 | Groups neighboring quantization techniques by scaling, rotation and residual correction. | Track when a transformation or correction is selected and whether it adapts to a changing RL policy; general quantization techniques do not become focal RL methods automatically. |
| **Score Centering**<br>[Score Centering Stabilizes Off-policy Reinforcement Learning](https://arxiv.org/abs/2609.20807v1)<br>Section 2; correction comparison in Appendix B.2 | Separates numerical and temporal sources of TIM and organizes bounded corrections by clipping or masking regions. | Distinguish mismatch sources from remedies; retain the estimation target as the basis for B1 rather than classifying every ratio-bearing loss alike. |
| **Full Pipeline FP8 RL**<br>[Towards Full Pipeline FP8 Reinforcement Learning for LLMs](https://arxiv.org/abs/2609.22870v1)<br>Section 6 | Contrasts clipping mechanisms, token/sequence aggregation, batch control and full-pipeline numerical design. | Record the unit of control and separate reference-calibrated objective boundaries from quantizer calibration. |
| **CIS**<br>[Rethinking Training-Inference Mismatch in LLM Reinforcement Learning: Where It Arises and How to Correct It](https://arxiv.org/abs/2609.32444v1)<br>Section 5 | Separates numerical, routing and staleness remedies; distinguishes correction confidence and aggregation. | Read the correction target, threshold signal and aggregation level separately. Its general-TIM evidence does not become native-FP4 evidence. |
| **QATFactory / QARL**<br>[QATFactory: A Versatile, Deployment-Aligned Framework for Quantization-aware Training and Distillation of LLMs](https://arxiv.org/abs/2609.39223v2)<br>Section 2 | Distinguishes PTQ, QAT/distillation, efficient adaptation, native training, and low-precision RL. | Keep adaptation procedure, trainable parameters, arithmetic and synchronization as separate execution descriptors. |
| **TRIAGE**<br>[TRIAGE: Direction-Aware Mismatch Stabilization of Native NVFP4 Reinforcement Learning](https://arxiv.org/abs/2610.07043v2)<br>Section 6 | Distinguishes low-precision training, training–inference alignment, and directional control. | Explain control of residual update dynamics separately from numerical alignment. |
| **TRACE**<br>[TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models](https://arxiv.org/abs/2610.07767v2)<br>Section 2 | Connects MoE routing and low-precision RL, then separates per-path error compensation from rounding-outcome alignment. | Distinguish agreement across paths from approximation accuracy within a path. |
| **KV4-RL**<br>[KV4-RL: Unlocking Faster Asynchronous Rollouts for RLVR with INT4 KV Cache Quantization](https://arxiv.org/abs/2610.14448v1)<br>Section 2 | Separates asynchronous/partial collection, quantized RL, and KV compression/selective precision. | Treat the numerical target and collection workload as separate setting axes; inference compression evidence alone does not establish an RL learning benefit. |

## Distinctions retained in the framework

**Adaptation is separate from correction.** QAT describes how the learner is exposed to quantization, while TIS-like methods describe how behavior samples enter an update. Low-rank/full-parameter adaptation and native/simulated arithmetic provide further descriptors. QuRL’s repeated quantization during RL also differs from quantizing a fixed final checkpoint.

**A ratio is not a classification rule.** A loss may contain an importance ratio while its proposed contribution changes update geometry or acceptance. The framework classifies DPPO/DRPO by their trust-region intervention and Score Centering by its conditional score correction.

**B2 contains different decisions.** Boundary placement, batch adaptation, divergence geometry, directional influence, and candidate acceptance use different signals and units. The [classification guide](TAXONOMY.md#control-decisions-inside-b2) makes these distinctions explicit.

**Workload affects the useful quantization target.** Expert W4A4 and low-bit KV address different costs. Collection protocol, context length, concurrency and kernels must accompany a timing claim.

**A paper’s positioning is not a cross-paper conclusion.** Broad context headings, novelty statements and claims of complementarity do not establish exhaustive coverage, a tested combination or a performance ranking. The survey adopts useful distinctions while retaining its own scope and experiment-specific evidence.

[Survey PDF](../Survey.pdf) · [Classification](TAXONOMY.md) · [Catalog](CATALOG.md) · [Comparison records](COMPARISONS.md)
