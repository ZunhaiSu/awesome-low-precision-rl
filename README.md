<h1 align="center">Awesome Low-Precision RL</h1>

<p align="center">
  <strong>Training–Rollout Mismatch in Low-Precision LLM Reinforcement Learning: A Survey</strong><br>
  Quantized rollouts · Numerical alignment · Learning under mismatch
</p>

<p align="center">
  <strong>Zunhai Su<sup>1</sup> · Wei Wu<sup>2</sup> · Jianchao Tan<sup>2</sup> · Ngai Wong<sup>1</sup></strong><br>
  <sup>1</sup>The University of Hong Kong &nbsp;·&nbsp; <sup>2</sup>Meituan<br>
  Literature snapshot: <strong>20 October 2026</strong> · Editorial update: 22 October 2026
</p>

<p align="center">
  <img src="figures/status.svg" alt="Working survey · 29 focal studies · CC BY-SA 4.0" width="570">
</p>

<p align="center">
  <a href="Survey.pdf"><strong>Read the survey PDF</strong></a> &nbsp;·&nbsp;
  <a href="papers/README.md"><strong>Reading library</strong></a> &nbsp;·&nbsp;
  <a href="#paper-catalog">All papers</a> &nbsp;·&nbsp;
  <a href="docs/EVIDENCE.md">Evidence</a> &nbsp;·&nbsp;
  <a href="#citation">Cite</a>
</p>

Quantized rollout changes the policy that generates training experience. This survey traces the resulting discrepancy through gradient estimation and policy updates, connecting numerical mechanisms, measurement practice, learned quality, and total training cost.

## Explore the survey

[Mechanisms and background](#reading-routes) · [Interventions](#taxonomy) · [Measurement practice](docs/MEASUREMENTS.md) · [Source-linked evidence](docs/EVIDENCE.md)

Use the [core reading route](papers/README.md#core-reading) across both topic folders. Folder placement describes the paper's topic; core and supporting roles describe its contribution to the survey.

**New to the topic?** Start with the GRPO example in §2.1: rewards → group advantages → policy ratios and clipping → update → quantized synchronization. Section 2.4 explains W/A/KV targets, QAT, and native arithmetic.

<p align="center">
  <img src="figures/overview.svg" alt="Survey overview: generation, collected experience, and learner updates form a feedback loop" width="680">
</p>

> **Living survey.** Technical corrections, missing papers, and research collaborations are welcome through [GitHub Issues](https://github.com/ZunhaiSu/awesome-low-precision-rl/issues).

## Contents

[Explore](#explore-the-survey) · [Scope](#scope) · [Taxonomy](#taxonomy) · [Measurements](#measuring-mismatch) · [Compare](#comparing-methods) · [Reading routes](#reading-routes) · [Papers](#paper-catalog) · [Findings](#research-findings) · [Contribute](#contribute) · [Citation](#citation)

## Scope

The collection focuses on the interface between the numerical policy that generates a rollout and the computation used to learn from it. It covers weight, activation, and KV-cache quantization; low precision on one or both endpoints; and closely related work on training–inference mismatch (TIM).

The corpus contains **19 core method/system studies, 9 supporting studies, and 1 exploration boundary case**. Roles describe contributions to this synthesis; foundational RL papers and neighboring surveys are additional bibliography entries.

This narrative survey synthesizes published evidence. General PTQ, low-precision pretraining, and unrelated rollout acceleration enter only where they explain this interface.

<details>
<summary><strong>Survey organization: eight sections</strong></summary>

| Section | Purpose |
|---|---|
| 1. Introduction and Scope | Motivate the learner–sampler interface and define the review boundary. |
| 2. Background and Problem Formulation | Separate policy roles, execution mismatch, decoding, and staleness. |
| 3. How Execution Mismatch Affects Learning | Trace probability differences through estimation, clipping, and feedback. |
| 4. Numerical Design and Execution Alignment | Compare computation alignment, fidelity control, and update visibility. |
| 5. Learning under Residual Mismatch | Explain estimator correction and update control, with complementary scheduling and composition. |
| 6. Evidence Synthesis and System Trade-offs | Connect published learning outcomes to evidence and system cost. |
| 7. Open Problems | Develop priorities in diagnosis, composition, stateful execution, and transfer. |
| 8. Conclusion | Bring numerical fidelity and learning correction into one perspective. |

Appendix A summarizes all twenty-nine focal works; Appendices B–C describe source selection, assumptions, and transfer; Appendix D defines the terminology; Appendix E maps mismatch measurements across all nineteen core studies.

</details>

## Taxonomy

<img src="figures/taxonomy.svg" alt="Component taxonomy of low-precision RL" width="100%">


Read each work through three complementary views: **mismatch source → intervention target → tested setting**. The source explains why probabilities differ; the target determines the method class; the setting conditions its evidence.

**A · Numerical design** addresses mismatch at its computational source: align the two paths (A1), or preserve numerical fidelity and update resolution (A2). **B · Learning under residual mismatch** manages its effect on learning: correct gradient estimation (B1), or control update influence and acceptance (B2). B can preserve useful learning without shrinking the policy gap. The families can be combined within one system.

| Code | Intervention | Main discussion | Representative components |
|---|---|---|---|
| A1 | Align computation between learner and rollout | §4.1 | Jet-RL; QaRL QAT; QUADS weight QAT; TRACE; Miles; QATFactory QARL; R3/TBIK as background |
| A2 | Control quantization error and preserve parameter updates | §4.2 | QuRL UAQ; QUADS RAC; FP8-RL calibration; KV4-RL protection; Rollout-ResQ; Miles precision exceptions |
| B1 | Correct gradient estimation | §5.1 | FlashRL/TIS; AIS; CIS; Score Centering; baseline/centering theory |
| B2 | Control policy-update influence | §5.2 | QuRL ACR; QaRL TBPO; Calibrated Clipping; P3O; DRPO; MIPU; ACRL; TRIAGE; DPPO as background |

Format, W/A/KV target, architecture, adaptation, and collection schedule are **configuration labels**. Scheduling (§5.3, navigation tag B3) complements the four classes. QeRL marks the exploration boundary; VeXact supplies a diagnostic reference.

B2 includes boundary placement (QuRL/QaRL/Calibrated Clipping), batch reliability (P3O), divergence geometry (DPPO/DRPO), directional influence (ACRL/TRIAGE), and candidate acceptance (MIPU). Their different decision units are summarized in the [classification guide](docs/TAXONOMY.md#control-decisions-inside-b2).

The [related-work perspectives](docs/RELATED_WORK.md) connect this framework to how the primary papers organize neighboring work. Their terminology is interpreted alongside each paper's actual mechanism.

## Measuring mismatch

The papers do **not** use one common mismatch metric. TRIAGE's average absolute log gap, TRACE's gap extrema, QuRL's behavior-to-proximal KL, and KV4-RL's full-distribution shared-prefix KL describe different quantities. ESS measures weight concentration; reward and entropy describe learning outcomes.

The [measurement guide](docs/MEASUREMENTS.md) maps all **19 core studies** with complete titles, source locations, policy comparisons, and interpretation limits. In the paper, **§3.4 defines the measurements, §6.2 interprets the learning evidence, and Appendix E collects study-specific practices**. The chain is numerical disagreement → estimator or update effects → learned quality and total cost.

## Comparing methods

The taxonomy identifies the intervention; the configuration identifies its tested scope. Read the learner path, rollout W/A/KV precision, and comparison rule together.

| Work | Mechanism | Reviewed execution setting |
|---|---|---|
| **TRACE**<br>[TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models](https://arxiv.org/abs/2610.07767v2) | Guide learner rounding using rollout quantization information. | Joint NVFP4 expert W4A4 and softmax KV4 rollout; guided fake-quantized learner forward, BF16 backward. |
| **TRIAGE**<br>[TRIAGE: Direction-Aware Mismatch Stabilization of Native NVFP4 Reinforcement Learning](https://arxiv.org/abs/2610.07043v2) | Gate and rebalance selected updates; add bounded repair. | Native NVFP4 W4A4 forward on both endpoints; documented BF16 KV; no reported KV4 experiment. |
| **Score Centering**<br>[Score Centering Stabilizes Off-policy Reinforcement Learning](https://arxiv.org/abs/2609.20807v1) | Center the behavior-weighted score to remove conditional drift. | BF16 learner; quantization stress includes FP4/INT4 KV; policy-lag experiments are separate. |
| **KV4-RL**<br>[KV4-RL: Unlocking Faster Asynchronous Rollouts for RLVR with INT4 KV Cache Quantization](https://arxiv.org/abs/2610.14448v1) | Protect sensitive cache positions at higher precision. | INT4 KV with bounded INT8 protection; BF16 learner; quota-based partial collection. |

The [studied combinations](docs/SYNTHESIS.md) connect numerical alignment, fidelity, correction and update control while distinguishing tested bundles from open combinations. TRACE directly compares TIS+SC under joint NVFP4 W/A/KV rollout. TRIAGE's reported comparisons do not include SC/TIS+SC or TRACE. Their results therefore answer different questions.

[Execution and direct-comparison records](docs/COMPARISONS.md) retain the models, source locations, checkpoint rules, outcomes and limits. The [comparison map](figures/evidence.svg) shows selected within-study connections.

## Reading routes

The catalog is chronological; these routes connect mechanisms. The [numbered reading library](papers/README.md) preserves the local topic groups and provides direct paper access.

| Question | Suggested route | Survey |
|---|---|---|
| What is the mismatch being corrected? | [FlashRL / TIS](https://www.opt-ml.org/papers/2025/paper116.pdf) → [MiniRL](https://arxiv.org/abs/2512.01374) → [VeXact / Diagnosing TIM](https://arxiv.org/abs/2605.14220) | §§2–3 |
| How can the two numerical paths be coupled? | [Jet-RL](https://arxiv.org/abs/2601.14243) → [QaRL](https://aclanthology.org/2026.findings-acl.841/) → [QUADS](https://arxiv.org/abs/2607.15810) → [TRACE](https://arxiv.org/abs/2610.07767) | §4.1 |
| Which information should low precision preserve? | [QuRL](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6b4880ced785077159b340710ceb7681-Abstract-Conference.html) (UAQ) → [FP8-RL](https://arxiv.org/abs/2601.18150) → [HiFloat4 / Rollout-ResQ](https://arxiv.org/abs/2607.26515v1) → [KV4-RL](https://arxiv.org/abs/2610.14448) | §4.2 |
| How should behavior samples estimate a target gradient? | [TIS](https://www.opt-ml.org/papers/2025/paper116.pdf) → [AIS](https://arxiv.org/abs/2605.13907) → [Score Centering](https://arxiv.org/abs/2609.20807), alongside [baseline theory](https://arxiv.org/abs/2610.22263v1); compare [CIS](https://arxiv.org/abs/2609.32444). | §5.1 |
| Which local learning contributions should be retained? | [QuRL](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6b4880ced785077159b340710ceb7681-Abstract-Conference.html) (ACR) → [QaRL](https://aclanthology.org/2026.findings-acl.841/) (TBPO) → [Full Pipeline FP8 RL](https://arxiv.org/abs/2609.22870); then compare [ACRL](https://arxiv.org/abs/2607.24062) and [TRIAGE](https://arxiv.org/abs/2610.07043). | §5.2 |
| How can control extend beyond local clipping? | [DPPO](https://arxiv.org/abs/2602.04879v3) → [DRPO](https://arxiv.org/abs/2606.09821v1) for trust-region geometry; [P3O / ESS](https://arxiv.org/abs/2605.12380v2) for batch reliability; [MIPU](https://arxiv.org/abs/2606.29526v1) for candidate acceptance. | §5.2 |
| What must a deployable low-precision stack coordinate? | [FP8-RL](https://arxiv.org/abs/2601.18150) → [Miles](https://arxiv.org/abs/2609.08368v1) → [QATFactory QARL](https://arxiv.org/abs/2609.39223v2): calibration, conversion, precision exceptions, and weight transfer. | §§4, 6.3 |

Keep [QeRL](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a15a2ece7f0663d1ba7db91103ac61c9-Abstract-Conference.html) visible as an exploration boundary case and [Beyond Precision](https://arxiv.org/abs/2602.01826) as general TIM evidence for scheduling. A route expresses reading dependencies, without implying a performance ranking or historical influence.

## Paper catalog

Each entry pairs a short name with the full paper title, linked directly to the reviewed source. The tables follow first public appearance and count each contribution once. Authors, reviewed versions, and additional discussion locations are in the [reviewed catalog](docs/CATALOG.md) and Surveyed Papers appendix. Dates can precede the formal publication linked here. [Classification rules](docs/TAXONOMY.md) distinguish contribution roles from evidence domains. [JSON records](data/papers.json) support reuse.

Browse by intervention: [A1 · Alignment](docs/CATALOG.md#alignment-a1) · [A2 · Fidelity](docs/CATALOG.md#fidelity-a2) · [B1 · Estimation](docs/CATALOG.md#estimation-b1) · [B2 · Update control](docs/CATALOG.md#update-control-b2). Complement: [scheduling](docs/CATALOG.md#scheduling-b3).

<!-- BEGIN GENERATED CATALOG -->

### Core methods and systems

| First public | Paper | Focus | Class / discussion |
|---|---|---|---|
| 2025 | **FlashRL / TIS**<br>[On the Rollout-Training Mismatch in Modern RL Systems](https://www.opt-ml.org/papers/2025/paper116.pdf) | Recorded behavior probabilities and truncated correction | B1 · 5.1 |
| 2026-01-20 | **Jet-RL**<br>[Jet-RL: Enabling On-Policy FP8 Reinforcement Learning with Unified Training and Rollout Precision Flow](https://arxiv.org/abs/2601.14243v2) | Unified FP8 precision flow | A1; A2 · 4.1 |
| 2026-01-26 | **FP8-RL**<br>[FP8-RL: A Practical and Stable Low-Precision Stack for LLM Reinforcement Learning](https://arxiv.org/abs/2601.18150v2) | W8A8 rollout, FP8 attention/KV, and stack integration | A2; system · 4.2 |
| 2026-02-15 | **QuRL**<br>[QuRL: Low-Precision Reinforcement Learning for Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6b4880ced785077159b340710ceb7681-Abstract-Conference.html) | Adaptive clipping and update-aware quantization | B2; A2 · 5.2 |
| 2026-04-09 | **QaRL**<br>[QaRL: Rollout-Aligned Quantization-Aware RL for Fast and Stable Training under Training–Inference Mismatch](https://aclanthology.org/2026.findings-acl.841/) | Rollout-aligned QAT and trust-band updates | A1; B2 · 4.1 |
| 2026-05-12 | **P3O / ESS**<br>[Let the Batch Decide, On- or Off-Policy: Effective Sample Size for RL Post-Training](https://arxiv.org/abs/2605.12380v2) | Batch-adaptive ESS cap and regularization | B2 · 5.2 |
| 2026-05-13 | **AIS**<br>[AIS: Adaptive Importance Sampling for Quantized RL](https://arxiv.org/abs/2605.13907v1) | Adaptive importance-weighted estimator mixture | B1 · 5.1 |
| 2026-06-08 | **DRPO**<br>[Rethinking the Divergence Regularization in LLM RL](https://arxiv.org/abs/2606.09821v1) | Smooth corrective divergence regularization | B2 · 5.2 |
| 2026-06-28 | **MIPU**<br>[The Mirage of Optimizing Training Policies: Monotonic Inference Policies as the Real Objective for LLM Reinforcement Learning](https://arxiv.org/abs/2606.29526v1) | Inference-policy candidate construction and acceptance | B2; formulation · 5.2 |
| 2026-07-17 | **QUADS**<br>[QUADS: Stabilizing NVFP4 Reinforcement Learning for MoE via QUantization-error Alignment across Dual Sides](https://arxiv.org/abs/2607.15810v1) | NVFP4 MoE weight alignment and activation compensation | A1; A2 · 4.1 |
| 2026-07-27 | **ACRL**<br>[ACRL: Adaptive Control of Training-Inference Discrepancy for Stable Reinforcement Learning](https://arxiv.org/abs/2607.24062v1) | Discrepancy-dependent update control | B2 · 5.2 |
| 2026-07-29 | **HiFloat4 / Rollout-ResQ**<br>[HiFloat4 Format for End-To-End Reinforcement Learning Post-Training of Large Language Models](https://arxiv.org/abs/2607.26515v1) | Sparse residual correction for FP4 rollout activations | A2 · 4.2 |
| 2026-09-08 | **Miles v0.1**<br>[Miles v0.1: Production-Level Post-Training](https://arxiv.org/abs/2609.08368v1) | Shared quantization, synchronization, and precision contracts | A1; A2; system · 4.1 |
| 2026-09-17 | **Score Centering**<br>[Score Centering Stabilizes Off-policy Reinforcement Learning](https://arxiv.org/abs/2609.20807v1) | Additive behavior-weighted score correction | B1 · 5.1 |
| 2026-09-19 | **Full Pipeline FP8 RL**<br>[Towards Full Pipeline FP8 Reinforcement Learning for LLMs](https://arxiv.org/abs/2609.22870v1) | FP8 learner/rollout and calibrated clipping | B2; system · 5.2 |
| 2026-09-30 | **QATFactory / QARL**<br>[QATFactory: A Versatile, Deployment-Aligned Framework for Quantization-aware Training and Distillation of LLMs](https://arxiv.org/abs/2609.39223v2) | Deployment-aligned QARL and inference-ready weight synchronization | A1; system · 4.1 |
| 2026-10-05 | **TRIAGE**<br>[TRIAGE: Direction-Aware Mismatch Stabilization of Native NVFP4 Reinforcement Learning](https://arxiv.org/abs/2610.07043v2) | Direction-aware control for native NVFP4 | B2 · 5.2 |
| 2026-10-06 | **TRACE**<br>[TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models](https://arxiv.org/abs/2610.07767v2) | Rollout-guided FP4 rounding for MoE | A1 · 4.1 |
| 2026-10-10 | **KV4-RL**<br>[KV4-RL: Unlocking Faster Asynchronous Rollouts for RLVR with INT4 KV Cache Quantization](https://arxiv.org/abs/2610.14448v1) | INT4 KV with selective INT8 protection | A2; system · 4.2 |

### Supporting formulation, theory, and general TIM studies

| First public | Paper | Focus | Class / discussion |
|---|---|---|---|
| 2025-10-13 | **R3**<br>[Stabilizing MoE Reinforcement Learning by Aligning Training and Inference Routers](https://arxiv.org/abs/2510.11370v2) | MoE routing alignment | Support; A1 · 3.1 |
| 2025-10-30 | **FP16-Mismatch**<br>[Defeating the Training-Inference Mismatch via FP16](https://arxiv.org/abs/2510.26788v1) | BF16/FP16 precision-selection evidence | Support; A2 · 3.1 |
| 2025-11-21 | **TBIK / Deterministic Inference**<br>[Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch](https://arxiv.org/abs/2511.17826v2) | Cross-TP deterministic kernels as an alignment reference | Support; A1 · 3.1 |
| 2025-12-01 | **MiniRL**<br>[Stabilizing Reinforcement Learning with LLMs: Formulation and Practices](https://arxiv.org/abs/2512.01374v3) | Policy roles and mismatch-aware formulation; FP8 experiments | Support; B1/B2 · 2.1 |
| 2026-02-02 | **Beyond Precision**<br>[Beyond Precision: Training-Inference Mismatch is an Optimization Problem and Simple LR Scheduling Fixes It](https://arxiv.org/abs/2602.01826v1) | Optimization schedule under general TIM | Support; B3 · 5.3 |
| 2026-02-04 | **DPPO**<br>[Rethinking the Trust Region in LLM Reinforcement Learning](https://arxiv.org/abs/2602.04879v3) | Divergence-based trust regions under general TIM | Support; B2 · 5.2 |
| 2026-05-14 | **VeXact / Diagnosing TIM**<br>[Diagnosing Training Inference Mismatch in LLM Reinforcement Learning via a Zero-Mismatch Reference](https://arxiv.org/abs/2605.14220v2) | Zero-mismatch diagnostic reference | Diagnostic · 3.4 |
| 2026-09-26 | **CIS**<br>[Rethinking Training-Inference Mismatch in LLM Reinforcement Learning: Where It Arises and How to Correct It](https://arxiv.org/abs/2609.32444v1) | Confidence-dependent correction under BF16 cross-engine mismatch | Support; B1 · 5.1 |
| 2026-10-15 | **Baselines and Score Centering**<br>[Baselines and Score Centering in Policy Gradient Estimation](https://arxiv.org/abs/2610.22263v1) | Granularity-dependent roles of baselines and score centering | Support; B1 · 5.1 |

### Exploration boundary

| First public | Paper | Focus | Class / discussion |
|---|---|---|---|
| 2025-10-13 | **QeRL**<br>[QeRL: Beyond Efficiency - Quantization-enhanced Reinforcement Learning for LLMs](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a15a2ece7f0663d1ba7db91103ac61c9-Abstract-Conference.html) | NVFP4 with LoRA and adaptive noise; exploration setting. | Boundary · Box 1 |

Roles describe relevance to the survey, rather than evidence quality. Primary and secondary discussion locations are navigation fields; a work can introduce several coequal components.

<!-- END GENERATED CATALOG -->

## Research findings

The [evidence records](data/evidence.json) cover all nineteen core studies and locate their observations in the primary papers. The survey develops three recurring findings:

**Shared computation matters more than nominal symmetry.** [Jet-RL](https://arxiv.org/abs/2601.14243), [QaRL](https://aclanthology.org/2026.findings-acl.841/), [QUADS](https://arxiv.org/abs/2607.15810), and [TRACE](https://arxiv.org/abs/2610.07767) coordinate different objects: precision flow, quantized representations, or realized rounding. Matching format labels alone does not identify what remains inconsistent.

**Controlling disagreement must preserve useful learning.** [QuRL](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6b4880ced785077159b340710ceb7681-Abstract-Conference.html), [Score Centering](https://arxiv.org/abs/2609.20807), [Full Pipeline FP8 RL](https://arxiv.org/abs/2609.22870), and [TRIAGE](https://arxiv.org/abs/2610.07043) address update visibility, gradient drift, clipping, and direction-dependent control. Their mechanisms explain why stable curves or small mean gaps alone do not establish effective learning.

**Generation speed and learning efficiency have different costs.** [KV4-RL](https://arxiv.org/abs/2610.14448) reports distinct rollout and full-iteration gains. Calibration, behavior reconstruction, rounding guidance, and weight conversion add dependencies elsewhere in the loop. Section 6 relates these costs to learned-policy quality; the [comparison records](docs/COMPARISONS.md) retain the tested configurations.

The collection distinguishes simulated FP4, native low-bit kernels, and BF16 computation on quantized values. It synthesizes source-reported results and does not introduce a common leaderboard or an independently reproduced benchmark.

<details>
<summary><strong>Analytical example: clipping depends on advantage sign</strong></summary>

<img src="figures/clipping.svg" alt="Analytical clipped surrogate: the flat branch lies on opposite sides for positive and negative advantages" width="100%">

The curves illustrate the standard surrogate with epsilon 0.2 and advantage ±1. They are analytical constructions, not performance measurements. A negative-advantage token with ratio 0.7 lies on the flat branch; the interpretation depends on which policy ratio is clipped.

</details>

<details>
<summary><strong>Explore the technical figures</strong></summary>

| Figure | What it explains |
|---|---|
| [Policy identities](figures/policies.svg) | Learner, sampling snapshot, actual behavior, proximal anchor, and KL reference. |
| [Probability trees](figures/prefixes.svg) | Equal local conditionals with different prefix and response probabilities. |
| [Measurement regimes](figures/measurement_practice.svg) | Fixed-checkpoint numerical probes and online update diagnostics, with distinct policy comparisons. |
| [Mechanism map](figures/mechanisms.svg) | Relative influence, score drift, update selection, and feedback. |
| [Quantized-update visibility](figures/quantization.svg) | Why a smaller update can cross a boundary while a larger one remains invisible. |
| [Score centering](figures/centering.svg) | A calculated two-action example separating gradient centering from reward centering. |
| [Rollout-guided rounding](figures/rounding.svg) | Why better cross-path agreement can differ from lower per-path quantization error. |
| [Learning operators](figures/operators.svg) | Estimator correction, direction-selective control, and effective gate normalization. |
| [Direct-comparison map](figures/evidence.svg) | Available comparison sets and their distinct numerical settings. |
| [Timing decomposition](figures/timing.svg) | A constructed example separating rollout acceleration from iteration speedup. |

All figures are available as scalable vector drawings. Numerical illustrations are explicitly labeled; no cross-paper leaderboard is inferred. See the [figure notes](docs/FIGURES.md) for their purposes and assumptions.

</details>

## Citation

The survey is a working manuscript. Use the citation below or GitHub's **Cite this repository** control, which uses [CITATION.cff](CITATION.cff). Please cite the original papers for their individual results.

```bibtex
@misc{su2026trainingrollout,
  title  = {Training--Rollout Mismatch in Low-Precision LLM Reinforcement Learning: A Survey},
  author = {Su, Zunhai and Wu, Wei and Tan, Jianchao and Wong, Ngai},
  year   = {2026},
  note   = {Working manuscript},
  url    = {https://github.com/ZunhaiSu/awesome-low-precision-rl}
}
```

## Contribute

Propose a missing paper, correct a technical claim, or discuss a research collaboration through [GitHub Issues](https://github.com/ZunhaiSu/awesome-low-precision-rl/issues). Primary sources and precise section/equation references make corrections especially useful. See [contribution guidance](CONTRIBUTING.md) for catalog fields, evidence records, and version handling.

## Template, status, and license

The paper adapts the **typesetting template** from [arXiv:2601.14004v4](https://arxiv.org/abs/2601.14004v4); its scientific framework is specific to this survey. Attribution and modifications are documented in [TEMPLATE.md](docs/TEMPLATE.md).

This working manuscript welcomes corrections and collaboration. [Scope and source versions](docs/CATALOG.md), [editorial assessment](docs/ASSESSMENT.md), and [document validation](docs/BUILD.md) accompany the PDF.

The survey PDF, repository content, and template adaptations use [CC BY-SA 4.0](LICENSE). Third-party papers retain their own licenses. The [reading library](papers/README.md) provides 11 explicitly licensed PDF mirrors and 18 official-source links, with attribution and version records in [NOTICES](papers/NOTICES.md) and the [manifest](papers/manifest.json).
