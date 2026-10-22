# Measuring training–rollout mismatch

There is no shared measurement protocol across the surveyed studies. Probability differences, weight concentration, update distortion, and learning outcomes answer different questions. The source-linked records below cover all **19 core studies**, distinguishing an explicit definition from a figure label, a control signal, and an outcome comparison. They are a survey of reported evidence, not a benchmark or an exhaustive audit of logging code.

## Four complementary levels

| Level | Representative observables | What the measurement can establish |
|---|---|---|
| Numerical and distributional agreement | Paired activation error; sampled-action probability/log gaps; conditional full-vocabulary KL | Where specified computations or probability distributions disagree. |
| Estimator reliability | Weight tails, raw/capped ESS, score-mean drift, advantage-weight variance amplification | How sampled experience enters a gradient estimator. |
| Update distortion | Sign-separated clipping, directional masses, segment concentration, candidate rejection | Which learning contributions or candidate steps are changed. |
| Learning and system outcomes | Reward, held-out quality, entropy, failure time, total cost | Whether the evaluated learning process remains useful and efficient. These are not direct policy distances. |

The levels are connected, but a reduction at one level does not guarantee improvement at the next. A high empirical ESS can coexist with uniformly miscalibrated weights; a small mean gap can conceal a harmful local tail; exact scores on sampled tokens do not prove equality over the vocabulary.

## Definitions that must travel with a curve

1. **Policy pair and time:** current learner or sampling-snapshot learner; actual behavior, re-scored rollout, proximal anchor, or fixed reference. Current/behavior differences may include policy lag.
2. **Probability convention:** raw softmax or post-temperature/truncation behavior; support, normalization, and stored precision. A reference-policy KL penalty is not a TIM diagnostic.
3. **Conditioning:** identical prefixes and checkpoint, route replay, retained-cache state, or independently generated trajectories. State which source of discrepancy the comparison holds fixed.
4. **Reduction:** sampled action or full vocabulary; signed, absolute, extreme, or quantile; token, response, group, segment, layer, and rank aggregation; masks and zero-advantage treatment.
5. **Measurement stage and population:** before/after update or synchronization; training stage; batch/token count; raw or truncated weights; uncertainty unit. A changing maximum can reflect a larger measurement population.

With d = log p − log q on actions sampled from q, the mean of |d| is a sampled-action discrepancy. The mean of −d estimates KL(q || p) for normalized conditional laws with common support and finite expectations. The mean of exp(d) − d − 1 has the same expectation when p is covered by q. Neither is KL(p || q), and finite sampled estimates differ from a full-vocabulary sum. The sampled mean of −d can even be negative without a population KL becoming negative. A response geometric mean and a complete-response likelihood product are also different quantities.

Normalized empirical ESS = (Σw)² / (N Σw²) measures concentration among N weights. Report whether w is raw or capped. It is not, by itself, a calibrated numerical distance or a guarantee of gradient accuracy.

## Training duration and delayed instability

Longer optimization and longer generated trajectories test different properties. Stability over the reported training window does not establish stability over larger budgets, and a persistent numerical gap does not by itself imply failed correction. The question is whether useful learning persists as the policy and sampled states evolve.

Report optimizer steps, rollout and learner tokens, and elapsed training cost; retain late-stage quality alongside the best checkpoint. Periodic paired execution probes help separate numerical error from policy staleness, while online estimator and update diagnostics show how the data continue to influence learning. Track retained contributions or rejected updates to detect stability obtained by progressively suppressing learning.

Time to failure requires a declared event and persistence window, such as sustained quality loss assessed alongside estimator or update diagnostics. Independent RL runs reveal variation in onset. A run ending without the event establishes survival only to its observation limit. Extended-budget comparisons should distinguish sustained useful learning, delayed deterioration, and learning stagnation. Stress tests require separate validation: [Score Centering](https://arxiv.org/abs/2609.20807v1) describes severe mismatch on short sequences as a proxy for longer training under milder mismatch, while [ACRL](https://arxiv.org/abs/2607.24062v1) identifies possible reference-baseline drift over exceptionally long runs.

## Source-by-source measurement map

The table identifies the selected evidence. Each following entry states its comparison and interpretation boundary. A missing detail is marked locally; it is not inferred from another paper using the same metric name.

| Study and complete title | Selected measurements | Source location |
|---|---|---|
| **FlashRL / TIS** · [On the Rollout-Training Mismatch in Modern RL Systems](https://www.opt-ml.org/papers/2025/paper116.pdf) | Cross-engine KL is plotted alongside accuracy; TIS uses the learner-to-behavior sampled-action ratio. | Figure 3 and Sections 3–4 |
| **Jet-RL** · [Jet-RL: Enabling On-Policy FP8 Reinforcement Learning with Unified Training and Rollout Precision Flow](https://arxiv.org/abs/2601.14243v2) | Learning curves compare BF16 training with FP8 rollout across context lengths and task difficulty. | Section 3.2, Figures 3–4 |
| **FP8-RL** · [FP8-RL: A Practical and Stable Low-Precision Stack for LLM Reinforcement Learning](https://arxiv.org/abs/2601.18150v2) | Mismatch KL is defined as D_KL(pi_FP8 || pi_train). Scaling and KV/attention ablations track it with learning curves. | Section 2.2.1, Metrics; Figure 12 |
| **QuRL** · [QuRL: Low-Precision Reinforcement Learning for Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6b4880ced785077159b340710ceb7681-Abstract-Conference.html) | Behavior-to-proximal KL, E_behav[log(pi_behav/pi_prox)], and the maximum proximal-to-behavior ratio. | Section 4.2, Figure 3 |
| **QaRL** · [QaRL: Rollout-Aligned Quantization-Aware RL for Fast and Stable Training under Training--Inference Mismatch](https://aclanthology.org/2026.findings-acl.841/) | Token-level distributions of the proximal ratio and mismatch weight; response-level geometric-mean ratios drive TBPO. | Section 3.2, Figure 4; Appendix Figure 13 |
| **P3O / ESS** · [Let the Batch Decide, On- or Off-Policy: Effective Sample Size for RL Post-Training](https://arxiv.org/abs/2605.12380v2) | Normalized ESS = mean(rho)^2 / mean(rho^2), formed from all-reduced ratio sums, squared sums, and valid-token counts. | Equation 11 and Algorithm 2 |
| **AIS** · [AIS: Adaptive Importance Sampling for Quantized RL](https://arxiv.org/abs/2605.13907v1) | Mean absolute sampled-token log gap; ESS of truncated weights; standard-deviation amplification std(A*w_bar)/(std(A)+epsilon). | Section 3.1, Equations 12–17 |
| **DRPO** · [Rethinking the Divergence Regularization in LLM RL](https://arxiv.org/abs/2606.09821v1) | Binary-TV probability shift defines the constraint geometry; accuracy, entropy, and response length characterize update outcomes. | Sections 3.1–3.2; Appendix D.4, Figures 9–10 |
| **MIPU** · [The Mirage of Optimizing Training Policies: Monotonic Inference Policies as the Real Objective for LLM Reinforcement Learning](https://arxiv.org/abs/2606.29526v1) | Mismatch-K3 = mean(exp(d)-d-1), d=log(pi_train)-log(mu), on rollout tokens; post-synchronization inference-gap proxy and rollback rate. | Section 5.1; Sections 4.2 and 5.4 |
| **QUADS** · [QUADS: Stabilizing NVFP4 Reinforcement Learning for MoE via QUantization-error Alignment across Dual Sides](https://arxiv.org/abs/2607.15810v1) | Per-step maximum norm of train–inference log-probability differences; layer-wise MoE activation/output L2 discrepancies. | Figures 2, 6–7; Section 3.1 |
| **ACRL** · [ACRL: Adaptive Control of Training-Inference Discrepancy for Stable Reinforcement Learning](https://arxiv.org/abs/2607.24062v1) | Absolute sampled-action probability difference |pi-mu|; within-response means are averaged over a response group and compared with an initial/baseline reference X. | Section 4.1, Equations 8–12 |
| **HiFloat4 / Rollout-ResQ** · [HiFloat4 Format for End-To-End Reinforcement Learning Post-Training of Large Language Models](https://arxiv.org/abs/2607.26515v1) | Activation/residual MSE and RMSE under 2:4 sparsification, together with precision ablations and learned performance. | Sections 4.2–4.3, Figure 4; Section 5 ablations |
| **Miles v0.1** · [Miles v0.1: Production-Level Post-Training](https://arxiv.org/abs/2609.08368v1) | Same-token cross-engine log-probability comparisons verify low-precision recipes. A separate agentic reference run reports a train–inference KL curve; true-on-policy mode reports zero sampled-token absolute difference. | Section 3.1; Section 5.3; Figure 5 |
| **Score Centering** · [Score Centering Stabilizes Off-policy Reinforcement Learning](https://arxiv.org/abs/2609.20807v1) | Conditional mean score and baseline drift motivate the method analytically; shared-objective learning curves test injected weight noise, quantization, and lag separately. | Sections 3–5, especially Section 5.1 |
| **Full Pipeline FP8 RL** · [Towards Full Pipeline FP8 Reinforcement Learning for LLMs](https://arxiv.org/abs/2609.22870v1) | Normalized MAE of FP8 probabilities and ratios versus BF16 shadow passes; lower/upper over-clipping classified by advantage sign and a BF16 branch counterfactual. | Section 3, Figures 1 and 3–4 |
| **QATFactory / QARL** · [QATFactory: A Versatile, Deployment-Aligned Framework for Quantization-aware Training and Distillation of LLMs](https://arxiv.org/abs/2609.39223v2) | QARL reports loss, reward, completion length, post-export accuracy, and speed. The paper also reports teacher KL/top-1 agreement in its separate QAD experiments. | Section 4.6, Figure 8 and Table 8; Sections 4.1–4.4 for QAD |
| **TRIAGE** · [TRIAGE: Direction-Aware Mismatch Stabilization of Native NVFP4 Reinforcement Learning](https://arxiv.org/abs/2610.07043v2) | Mean absolute sampled-token log gap, signed quantiles, advantage-conditioned amplifying/contracting masses, and segment-localization statistics; before/after replay audits directional motion. | Section 3, Figure 4; Appendices B.2–B.6 |
| **TRACE** · [TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models](https://arxiv.org/abs/2610.07767v2) | Maximum/minimum log-probability differences; relative excess activation MSE (D_FP4-D_BF16)/D_BF16 across layers. | Section 3.1, Figure 4; Section 4.4, Figure 11; Appendix A |
| **KV4-RL** · [KV4-RL: Unlocking Faster Asynchronous Rollouts for RLVR with INT4 KV Cache Quantization](https://arxiv.org/abs/2610.14448v1) | Mean full-vocabulary conditional D_KL(p_BF16 || q_quant) over identical BF16-generated prefixes, before temperature scaling or sampling truncation. | Section 5.2, Equation 5.2; Appendix B.5 |

## Interpretation boundaries

**FlashRL / TIS.** The formulation compares FSDP and vLLM at the old parameter snapshot. The figure caption does not specify KL direction, vocabulary coverage, or the numerical reduction. Do not reconstruct these from the TIS formula.

**Jet-RL.** BF16 and mixed-precision training runs; rollout length and initial model capability are varied. These experiments establish a learning discrepancy, not a common scalar TIM distance. The reference-policy KL loss is a different quantity.

**FP8-RL.** Rollout versus training policies in the stated precision configuration. The direction is explicit; the metrics paragraph does not fully specify the estimator, vocabulary coverage, or reduction. Do not equate it with full-vocabulary KL by default.

**QuRL.** Quantized behavior policy against the proximal training policy used for correction. KL and the maximum ratio describe different aspects of mismatch. The maximum depends on token population and batch size; this KL is not reference regularization.

**QaRL.** Current/old learner probabilities are separated from old learner/sampler probabilities. The proximal and mismatch ratios have different denominators. Geometric-mean response ratios are not complete-response likelihood ratios.

**P3O / ESS.** Current learner/recorded behavior ratios across valid response tokens in the batch. This includes parameter lag as well as execution differences. Uniform weights yield high empirical ESS even when their common value is not one.

**AIS.** Current training and rollout probabilities on the mini-batch; reliability uses capped weights. The gap controls correction necessity; capped-weight ESS controls reliability. Its value is not directly comparable with raw-ratio ESS in P3O.

**DRPO.** Sampled-action probabilities of the current policy and the behavior anchor in the objective. A constraint variable is not necessarily a separately logged TIM metric. Binary-TV on one sampled action is not full-vocabulary total variation.

**MIPU.** Rollout-token learner/sampler comparison; candidate policy additionally examined after synchronization. K3 estimates D_KL(mu || pi) under normalization/support assumptions. The inference-gap proxy and rollback rate measure update acceptance, not a policy distance.

**QUADS.** Paired training/inference execution under weight and activation ablations. A maximum gap depends on the measured population. Layer-wise L2 also depends on tensor shape, scale, and measurement location.

**ACRL.** Training and inference probabilities at the old parameter snapshot; Y/X controls reweighting. Absolute probability distance is not absolute log distance. Response/group weighting differs from one global token mean; the baseline normalizes a controller, not a universal tolerance.

**HiFloat4 / Rollout-ResQ.** A quantized tensor and its sparsified counterpart in the residual design; rollout/training precision arms in learning ablations. The Figure 4 tensor errors are not paired learner–sampler probability distances. Precision ablations locate an error source but do not yield a common TIM scalar.

**Miles v0.1.** Comparisons depend on the execution mode. True-on-policy re-scores completed sequences by prefill rather than retaining decode-kernel probabilities. The different observations are not one universal metric or one low-precision experiment. Exact sampled-token scores do not imply equality over the entire vocabulary or remove parameter lag.

**Score Centering.** Correction rules share objective, advantages, sampler, and trainer; severe mismatch is used to separate methods within short runs. The score expectation is a theoretical estimand, not automatically an empirically logged norm. Stress-test severity and failure time are not a calibrated distance scale.

**Full Pipeline FP8 RL.** FP8 and BF16 shadow probabilities/ratios for the examined updates; negative-advantage lower-bound over-clipping requires r_BF16>1-epsilon but r_FP8<=1-epsilon. Over-clipping is a counterfactual decision disagreement, not the ordinary clipping fraction. Ratio NMAE concerns update distortion and is not solely a fixed-snapshot learner–sampler distance.

**QATFactory / QARL.** QARL versus BF16 RL and post-hoc quantization; QAD compares teacher/student fidelity on held-out corpora. Teacher-student KL from QAD must not be presented as an online QARL learner–sampler mismatch measurement.

**TRIAGE.** Recorded generation log probabilities are fixed. The 30B characterization replays sampled MoE routes; 4B measures the ordinary gap. Marginal statistics include all valid completion tokens; gradient-bearing occupancy excludes zero advantage. The paper explicitly does not compare raw 4B and routing-conditioned 30B magnitudes. Directional indicators are audited rather than assumed to predict every token update.

**TRACE.** Paired train–rollout activation discrepancies under FP4 and BF16; online extrema accompany reward/entropy/test curves. The excess MSE is a relative increase over BF16 train–rollout discrepancy, not quantized-versus-exact tensor reconstruction error. Extrema are not TRIAGE-style mean absolute gaps; exact reduction must be retained.

**KV4-RL.** Same policy checkpoint, paired KV execution, fixed prefix set; response-cluster bootstrap intervals. This isolates a raw conditional numerical discrepancy, not actual post-decoding behavior probabilities, visited-prefix shift, or the online current-learner/old-behavior gap.

## Reading the evidence together

TRIAGE's average absolute gap, TRACE's extrema, QuRL's behavior-to-proximal KL, MIPU's sampled K3, and KV4-RL's paired full-distribution KL should not be ranked on a shared numerical axis. A useful synthesis follows a chain: **specified numerical disagreement → estimator or update effect → learned quality and total cost**. Each arrow requires its own evidence.

This measurement map complements the [component taxonomy](TAXONOMY.md), [controlled comparison records](COMPARISONS.md), and [survey PDF](../Survey.pdf). Definitions and reported observations are taken from the reviewed versions in [the catalog](CATALOG.md); structured records are in [measurements.json](../data/measurements.json).

## Measurement practice: a reproducible report

These recommendations synthesize the reviewed practices; they are not a shared standard already used by all papers.

| Regime | What to hold fixed or record | Read the result as |
|---|---|---|
| Controlled execution probe | Same checkpoint and exact prefixes; stated kernel, routing, cache, and decoding controls | A conditional discrepancy between the specified execution paths |
| Online operational diagnostic | Original generation score/version; named current learner replay; pre/post update or synchronization stage | The gap actually encountered by training, potentially including lag |
| Update audit | Same sampled batch, prefixes, advantages, masks and behavior scores before/after an update | Realized motion under that update; not a guarantee for unobserved histories |

For two constructed responses of lengths 2 and 8 with constant absolute gaps 1 and 0.1, the token-weighted mean is **0.28**, while the response-weighted mean is **0.55**. Both calculations are correct; the reduction changes the question. Across ranks, combine sums and valid counts before division for a global token mean. Compute global maxima from maxima, not an average of rank maxima.

Report full valid-token diagnostics alongside intervention-eligible subsets. A lower retained-token gap after gating can be a selection effect. Include subset occupancy and the relevant retained contribution; token count and advantage-weighted mass are not interchangeable.

Practical source examples include [TRIAGE's fixed-batch update audit](https://arxiv.org/abs/2610.07043v2) (Appendix B.3), [KV4-RL's fixed-checkpoint shared-prefix KL](https://arxiv.org/abs/2610.14448v1) (Section 5.2 and Appendix B.5), [P3O's distributed moments](https://arxiv.org/abs/2605.12380v2) (Equation 11), and [CIS's measurement and numerical controls](https://arxiv.org/abs/2609.32444v1) (Appendices C.4 and D.5). CIS is supporting general-TIM evidence, not an additional direct FP4 experiment.

A stored log-probability can have limited resolution. Near-one probabilities can saturate, and a clamp representable in one dtype may not be representable in another. State numeric precision, clamps, invalid-value handling, and the reduction population. Raw-logit errors additionally need an offset convention because a constant shift leaves softmax probabilities unchanged.

Keep **learner–sampler KL**, **current–proximal KL**, **learner–reference KL**, and **teacher–student distillation KL** distinct. Also name K1/K3 or the full-vocabulary calculation, direction, probability convention, and sample law.

Use quantiles and extrema with measured token counts. Define the time axis, report whether curves are smoothed, and identify the uncertainty unit. Tokens within one response and repeated evaluations of one trained model are not independent training replications. A compact set should follow the mechanism: direct discrepancy → estimator/update consequence → quality and total cost.
