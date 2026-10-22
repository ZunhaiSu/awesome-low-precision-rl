# Connecting mechanisms, measurements, and interventions

The survey follows a chain: **numerical execution → sampled experience → gradient estimation → policy update → the next numerical sampler**. Measurements identify a discrepancy or its consequence at a point in this chain; method classes identify which component is changed. These are complementary views, not interchangeable classifications.

## Mechanism, granularity, and required information

Intervention class identifies what changes. Granularity identifies where it acts; information requirements determine what the implementation must observe or retain. These examples describe components, including the specified UAQ component of QuRL.

| Component / class | Targeted mechanism | Application unit | Required information or execution |
|---|---|---|---|
| **Jet-RL · A1**<br>[Jet-RL: Enabling On-Policy FP8 Reinforcement Learning with Unified Training and Rollout Precision Flow](https://arxiv.org/abs/2601.14243v2) | Share operator precision and numerical configuration. | Corresponding operators. | Coordinated precision flow and quantizer semantics. |
| **QuRL · A2 · UAQ component**<br>[QuRL: Low-Precision Reinforcement Learning for Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6b4880ced785077159b340710ceb7681-Abstract-Conference.html) | Preserve the expression of parameter updates after quantization. | Parameters and layer parameterization. | A rescaling chosen relative to update and quantization scales. |
| **TRACE · A1**<br>[TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models](https://arxiv.org/abs/2610.07767v2) | Couple realized rounding outcomes. | Paired layer, token, and quantization site. | Retained rollout code information and scales, matched to learner states. |
| **KV4-RL · A2**<br>[KV4-RL: Unlocking Faster Asynchronous Rollouts for RLVR with INT4 KV Cache Quantization](https://arxiv.org/abs/2610.14448v1) | Protect sensitive cache information. | Selected cache positions. | Position-aware low-bit cache execution with higher-precision protection. |
| **FlashRL / TIS · B1**<br>[On the Rollout-Training Mismatch in Modern RL Systems](https://www.opt-ml.org/papers/2025/paper116.pdf) | Reweight observed actions toward a specified target. | Sampled tokens and the declared reduction. | Actual behavior and proximal/learner probabilities, with support assumptions. |
| **Score Centering · B1**<br>[Score Centering Stabilizes Off-policy Reinforcement Learning](https://arxiv.org/abs/2609.20807v1) | Remove the corresponding conditional score mean. | Action expectation at a prefix. | Behavior distribution information; the implementation reconstructs it from top-k records and a modeled tail. |
| **P3O / ESS · B2**<br>[Let the Batch Decide, On- or Off-Policy: Effective Sample Size for RL Post-Training](https://arxiv.org/abs/2605.12380v2) | Adapt cap and regularization to reliability. | Batch-level signal, applied through the objective. | Raw ratio moments and valid-token counts. |
| **TRIAGE · B2**<br>[TRIAGE: Direction-Aware Mismatch Stabilization of Native NVFP4 Reinforcement Learning](https://arxiv.org/abs/2610.07043v2) | Select directional contributions and apply bounded repair. | Tokens and segments with response normalization. | Advantages, signed learner–behavior gaps, and segment statistics. |
| **MIPU · B2**<br>[The Mirage of Optimizing Training Policies: Monotonic Inference Policies as the Real Objective for LLM Reinforcement Learning](https://arxiv.org/abs/2606.29526v1) | Accept or reject a synchronized inference-policy candidate. | Whole candidate policy. | Post-conversion assessment and a candidate/rollback mechanism. |

Shared granularity does not imply shared estimators, and complementary targets do not guarantee a compatible implementation. The policy pair, weighting and reduction must remain consistent when components are combined.

## Studied combinations

The following bundles are discussed in the reviewed primary sources. They illustrate mechanistic complementarity without establishing that any component can be swapped into another system unchanged.

| Study and complete title | Components used together | Why the combination matters |
|---|---|---|
| **QuRL** · [QuRL: Low-Precision Reinforcement Learning for Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6b4880ced785077159b340710ceb7681-Abstract-Conference.html) | UAQ (A2) + ACR (B2) | Update visibility and the clipping constraint address different stages. |
| **QaRL** · [QaRL: Rollout-Aligned Quantization-Aware RL for Fast and Stable Training under Training--Inference Mismatch](https://aclanthology.org/2026.findings-acl.841/) | Aligned QAT (A1) + TBPO (B2) | Representation matching and response-level update control. |
| **QUADS** · [QUADS: Stabilizing NVFP4 Reinforcement Learning for MoE via QUantization-error Alignment across Dual Sides](https://arxiv.org/abs/2607.15810v1) | Weight QAT (A1) + residual activation compensation (A2) | Weight alignment leaves an activation approximation to improve. |
| **KV4-RL** · [KV4-RL: Unlocking Faster Asynchronous Rollouts for RLVR with INT4 KV Cache Quantization](https://arxiv.org/abs/2610.14448v1) | Selective cache protection (A2) + retained TIS | Sampler fidelity and bounded conditional correction remain separate components. |
| **TRACE** · [TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models](https://arxiv.org/abs/2610.07767v2) | Guided QAT (A1) + routing replay + token-ratio correction | Rounding guidance does not remove route differences or policy lag by itself. |
| **Score Centering** · [Score Centering Stabilizes Off-policy Reinforcement Learning](https://arxiv.org/abs/2609.20807v1) | Score centering with TIS or MIS (B1) | The correction centers the corresponding weighted score; reconstruction and regularization still matter. |

## What measurements contribute

A controlled shared-prefix probe can locate conditional numerical disagreement. An online learner–behavior curve measures the discrepancy encountered during learning, potentially including parameter lag. An update audit asks which clipping branches, signed contributions, or candidate decisions change. Held-out quality and total cost establish whether that mechanism matters for useful learning.

These roles explain why a smaller average gap, higher empirical ESS, or lower clipping fraction is not a sufficient endpoint. A control signal can be reduced by selection; a capped-weight ESS can rise because the cap removed its tail; a stable run can still learn slowly. Report the policy pair, reduction population, selected subset, update stage, and the measured consequence.

## Three connections across the collection

**Numerical fidelity has several targets.** Cross-path agreement, approximation to a higher-precision computation, and preservation of parameter-update resolution can differ. TRACE, QUADS and QuRL address different parts of this distinction. Forward agreement also leaves the learner's backward arithmetic to be specified.

**Correction and control preserve different information.** A bounded action weight, a reconstructed conditional score mean, and an advantage-conditioned gate change different aspects of the gradient. Their composition requires consistent behavior probabilities, the intended weighted expectation, and compatible reduction rules. Tested bundles provide evidence for their own implementation and regime.

**Execution savings must survive the learning loop.** Native kernels, simulated quantization, BF16 backward passes, guidance transfer, reference calibration and candidate rejection have different costs. The relevant outcome combines quality with the budget of the complete system, not an isolated kernel speedup.

Joint cache/weight/activation quantization and untested mixtures of rounding guidance, score centering and directional control remain empirical questions. Controlled comparisons under matched resources would establish their learning benefits and costs.

See [measurement practice](MEASUREMENTS.md), [component definitions](TAXONOMY.md), [source-specific comparisons](COMPARISONS.md), and [the survey PDF](../Survey.pdf).
