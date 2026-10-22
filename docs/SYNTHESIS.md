# Connecting mechanisms, measurements, and interventions

The survey follows a chain: **numerical execution → sampled experience → gradient estimation → policy update → the next numerical sampler**. Measurements identify a discrepancy or its consequence at a point in this chain; method classes identify which component is changed. These are complementary views, not interchangeable classifications.

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
