# Awesome Low-Precision RL

### Quantized rollouts and training–rollout mismatch

A survey and curated research collection on how low-precision execution changes reinforcement learning for language models.

**[Survey PDF](Survey.pdf)** · [LaTeX](survey/survey.tex) · [BibTeX](references.bib) · [Paper catalog](data/papers.json) · [Source-linked evidence](data/evidence.json)

**Zunhai Su · The University of Hong Kong**<br>
Living survey · Literature snapshot: **19 October 2026** · **20 focal studies**

The companion manuscript, *Training–Rollout Mismatch in Low-Precision LLM Reinforcement Learning: A Survey*, connects numerical execution, gradient estimation, and policy optimization. It examines which numerical differences affect learning and how numerical design and learning correction determine the updates retained during training.

<img src="figures/overview.svg" alt="Survey overview: generation, collected experience, and learner updates form a feedback loop" width="100%">

> **An evolving research resource.** Missing papers, technical corrections, reproducibility observations, and collaboration ideas are welcome through [GitHub Issues](https://github.com/ZunhaiSu/awesome-low-precision-rl/issues).

## Contents

[Start here](#start-here) · [Scope](#scope) · [Taxonomy](#taxonomy) · [Reading routes](#reading-routes) · [Papers](#paper-catalog) · [Findings](#research-findings) · [Build](#build-and-validate) · [Contribute](#contribute) · [Citation](#citation)

## Start here

1. Read the [survey](Survey.pdf), especially §§2–3, to distinguish actual behavior probabilities, learner computation, and policy lag.
2. Use the taxonomy below to choose a numerical route (§4) or a learning route (§5). A study may contribute to both.
3. Read §6 alongside Appendix A for the evidence synthesis and the complete **Surveyed Papers** table.

## Scope

The collection focuses on the interface between the numerical policy that generates a rollout and the computation used to learn from it. It covers weight, activation, and KV-cache quantization; low precision on one or both endpoints; and closely related work on training–inference mismatch (TIM).

The focal corpus contains **13 method/system studies, 6 formulation or general TIM studies, and 1 exploration boundary case**. These roles describe how a study enters the survey. Foundational RL papers and neighboring surveys appear in the bibliography but are not counted as focal works.

This is a focused narrative survey. General PTQ, low-precision pretraining, and unrelated rollout acceleration fall outside its focal scope. The collection synthesizes published evidence and introduces no new benchmark.

<details>
<summary><strong>Survey organization: eight sections</strong></summary>

| Section | Purpose |
|---|---|
| 1. Introduction and Scope | Motivate the learner–sampler interface and define the review boundary. |
| 2. Problem Formulation and Taxonomy | Separate policy roles, execution mismatch, decoding, and staleness. |
| 3. Mechanisms | Trace probability differences through estimation, clipping, and feedback. |
| 4. Numerical Design and Execution Alignment | Compare computation alignment, fidelity control, and update visibility. |
| 5. Learning under Residual Mismatch | Compare estimator correction, update control, scheduling, and composition. |
| 6. Synthesis of Findings and Practical Trade-offs | Connect published learning outcomes to evidence and system cost. |
| 7. Open Problems | Develop priorities in diagnosis, composition, stateful execution, and transfer. |
| 8. Conclusion | Bring numerical fidelity and learning correction into one perspective. |

Appendix A summarizes all twenty focal works; Appendices B–C describe source selection, assumptions, and transfer.

</details>

## Taxonomy

<img src="figures/taxonomy.svg" alt="Component taxonomy of low-precision RL" width="100%">


The unit of classification is a **component**, so a paper may occupy multiple cells.

| Code | Intervention | Main discussion | Representative components |
|---|---|---|---|
| A1 | Align computation between learner and rollout | §4.1 | Jet-RL; QaRL QAT; QUADS asymmetric QAT; TRACE; R3 as background |
| A2 | Control quantization error and preserve parameter updates | §4.2 | QuRL UAQ; QUADS RAC; FP8-RL calibration; KV4-RL protection |
| B1 | Correct gradient estimation | §5.1 | FlashRL/TIS; AIS; CIS; Score Centering |
| B2 | Control policy-update influence | §5.2 | QuRL ACR; QaRL TBPO; Calibrated Clipping; ACRL; TRIAGE |
| B3 | Adapt the optimization schedule | §5.3 | Beyond Precision, as general TIM support |

Precision format, W/A/KV target, architecture, adaptation regime, and collection schedule are **separate configuration labels**. CIS calibrates importance sampling; Calibrated Clipping calibrates update boundaries. QeRL is discussed in a boundary box; VeXact is a diagnostic reference.

## Reading routes

The catalog follows first public appearance. The routes below follow conceptual dependencies and keep closely related questions together.

| Question | Suggested route | Survey |
|---|---|---|
| What is the mismatch being corrected? | [FlashRL / TIS](https://www.opt-ml.org/papers/2025/paper116.pdf) → [MiniRL](https://arxiv.org/abs/2512.01374) → [VeXact / Diagnosing TIM](https://arxiv.org/abs/2605.14220) | §§2–3 |
| How can the two numerical paths be coupled? | [Jet-RL](https://arxiv.org/abs/2601.14243) → [QaRL](https://aclanthology.org/2026.findings-acl.841/) → [QUADS](https://arxiv.org/abs/2607.15810) → [TRACE](https://arxiv.org/abs/2610.07767) | §4.1 |
| Which information should low precision preserve? | [QuRL](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6b4880ced785077159b340710ceb7681-Abstract-Conference.html) (UAQ) → [FP8-RL](https://arxiv.org/abs/2601.18150) → [KV4-RL](https://arxiv.org/abs/2610.14448) | §4.2 |
| How do correction and control differ? | TIS → [AIS](https://arxiv.org/abs/2605.13907) → [Score Centering](https://arxiv.org/abs/2609.20807) / [CIS](https://arxiv.org/abs/2609.32444); then ACR, TBPO, [Full Pipeline FP8 RL](https://arxiv.org/abs/2609.22870), [ACRL](https://arxiv.org/abs/2607.24062), and [TRIAGE](https://arxiv.org/abs/2610.07043) | §5 |

Keep [QeRL](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a15a2ece7f0663d1ba7db91103ac61c9-Abstract-Conference.html) visible as an exploration boundary case and [Beyond Precision](https://arxiv.org/abs/2602.01826) as general TIM evidence for scheduling. A route expresses reading dependencies, without implying a performance ranking or historical influence.

## Paper catalog

Each row represents one contribution. Dates refer to first public appearance; links may point to a later formal publication. Full titles, authors, reviewed versions, and secondary locations are available in the [catalog](data/papers.json), [bibliography](references.bib), and Surveyed Papers appendix.

### Core methods and systems

| First public | Study | Focus | Class / discussion |
|---|---|---|---|
| 2025 | **[FlashRL / TIS](https://www.opt-ml.org/papers/2025/paper116.pdf)** | Recorded behavior probabilities and truncated correction | B1 · §5.1 |
| 2026-01-20 | **[Jet-RL](https://arxiv.org/abs/2601.14243)** | Unified FP8 precision flow | A1; A2 · §4.1 |
| 2026-01-26 | **[FP8-RL](https://arxiv.org/abs/2601.18150)** | W8A8 rollout, FP8 attention/KV, and stack integration | A2; system integration · §4.2 |
| 2026-02-15 | **[QuRL](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6b4880ced785077159b340710ceb7681-Abstract-Conference.html)** | Adaptive clipping and update-aware quantization | B2; A2 · §5.2 |
| 2026-04-09 | **[QaRL](https://aclanthology.org/2026.findings-acl.841/)** | Rollout-aligned QAT and trust-band updates | A1; B2 · §4.1 |
| 2026-05-13 | **[AIS](https://arxiv.org/abs/2605.13907)** | Adaptive importance-weighted estimator mixture | B1 · §5.1 |
| 2026-07-17 | **[QUADS](https://arxiv.org/abs/2607.15810)** | NVFP4 MoE weight alignment and activation compensation | A1; A2 · §4.1 |
| 2026-07-27 | **[ACRL](https://arxiv.org/abs/2607.24062)** | Discrepancy-dependent update control | B2 · §5.2 |
| 2026-09-17 | **[Score Centering](https://arxiv.org/abs/2609.20807)** | Additive behavior-weighted score correction | B1 · §5.1 |
| 2026-09-19 | **[Full Pipeline FP8 RL](https://arxiv.org/abs/2609.22870)** | FP8 learner/rollout and calibrated clipping | B2; system integration · §5.2 |
| 2026-10-05 | **[TRIAGE](https://arxiv.org/abs/2610.07043)** | Direction-aware control for native NVFP4 | B2 · §5.2 |
| 2026-10-06 | **[TRACE](https://arxiv.org/abs/2610.07767)** | Rollout-guided FP4 rounding for MoE | A1 · §4.1 |
| 2026-10-10 | **[KV4-RL](https://arxiv.org/abs/2610.14448)** | INT4 KV with selective INT8 protection | A2; system integration · §4.2 |

<details>
<summary><strong>Supporting formulation and general TIM studies</strong></summary>

| First public | Study | Focus | Class / discussion |
|---|---|---|---|
| 2025-10-13 | **[R3](https://arxiv.org/abs/2510.11370)** | MoE routing alignment | A1 · §3.1 |
| 2025-10-30 | **[FP16-Mismatch](https://arxiv.org/abs/2510.26788)** | BF16/FP16 precision-selection evidence | A2 · §3.1 |
| 2025-12-01 | **[MiniRL](https://arxiv.org/abs/2512.01374)** | Policy roles and mismatch-aware formulation; FP8 experiments | B1/B2 · §2.1 |
| 2026-02-02 | **[Beyond Precision](https://arxiv.org/abs/2602.01826)** | Optimization schedule under general TIM | B3 · §5.3 |
| 2026-05-14 | **[VeXact / Diagnosing TIM](https://arxiv.org/abs/2605.14220)** | Zero-mismatch diagnostic reference | Diagnostic · §3.4 |
| 2026-09-26 | **[CIS](https://arxiv.org/abs/2609.32444)** | Confidence-dependent correction under BF16 cross-engine mismatch | B1 · §5.1 |

A supporting role does not exclude direct low-precision experiments. The role records how the work supports this survey's argument.

</details>

### Exploration boundary

**[QeRL](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a15a2ece7f0663d1ba7db91103ac61c9-Abstract-Conference.html)** (2025) combines NVFP4, LoRA, and adaptive quantization noise. It is discussed in Box 1 because exploration and agreement answer different questions in this setting.

## Research findings

The [evidence records](data/evidence.json) cover all thirteen core studies and locate their observations in the primary papers. The survey develops three recurring findings:

**Correction evolves with learning.** [QuRL](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6b4880ced785077159b340710ceb7681-Abstract-Conference.html), [AIS](https://arxiv.org/abs/2605.13907), and [Score Centering](https://arxiv.org/abs/2609.20807) address complementary effects on the evolving learner: clipping and update visibility, adaptive importance weighting, and conditional score drift.

**Alignment depends on the shared computation.** [Jet-RL](https://arxiv.org/abs/2601.14243), [QUADS](https://arxiv.org/abs/2607.15810), and [TRACE](https://arxiv.org/abs/2610.07767) share different information: a precision-flow design, a representation, or realized rounding decisions. Their remaining execution differences determine the scope of agreement.

**Signed update selection reveals hidden effects.** [Full Pipeline FP8 RL](https://arxiv.org/abs/2609.22870) and [TRIAGE](https://arxiv.org/abs/2610.07043) connect stability to signed clipping or direction-dependent control. Mean disagreement alone can hide which learning contributions survive.

Numerical fidelity, optimization stability, policy quality, and runtime remain distinct outcomes. Section 6 connects them through within-study evidence, information requirements, and timing scope.

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
| [Mechanism map](figures/mechanisms.svg) | Relative influence, score drift, update selection, and feedback. |
| [Quantized-update visibility](figures/quantization.svg) | Why a smaller update can cross a boundary while a larger one remains invisible. |
| [Learning operators](figures/operators.svg) | The different target objects of estimator correction, update control, and scheduling. |
| [Evidence lenses](figures/evidence.svg) | Numerical, update, trajectory, and quality/cost measurements. |
| [Timing decomposition](figures/timing.svg) | A constructed example separating rollout acceleration from iteration speedup. |

All figures are editable vector drawings embedded in the standalone LaTeX source. Numerical illustrations are explicitly labeled; no cross-paper leaderboard is inferred.

</details>

## Build and validate

The manuscript embeds its class, bibliography, and vector figures. `survey/survey.tex` can be shared as one LaTeX source file; the matching separate class supports conventional project editing.

With [Tectonic](https://tectonic-typesetting.github.io/) installed, run from the repository root:

```sh
python3 scripts/build.py
```

This builds the manuscript, refreshes the root `Survey.pdf`, and checks catalog, bibliography, figure, and link consistency. To also regenerate every SVG, install Poppler and run:

```sh
python3 scripts/build.py --figures
```

The scripts accept explicit tool paths through `--tectonic` and `--pdftocairo`. See [build notes](docs/BUILD.md) and [figure notes](docs/FIGURES.md) for tested behavior and figure assumptions. The root PDF and `survey/survey.pdf` are kept identical.

## Citation

The survey is a working manuscript. Until a public preprint identifier is available, the following metadata can be used to cite the manuscript; please cite the original papers for their individual results.

```bibtex
@misc{su2026trainingrollout,
  title  = {Training--Rollout Mismatch in Low-Precision LLM Reinforcement Learning: A Survey},
  author = {Su, Zunhai},
  year   = {2026},
  note   = {Working manuscript},
  url    = {https://github.com/ZunhaiSu/awesome-low-precision-rl}
}
```

## Contribute

Propose a missing paper, correct a technical claim, or discuss a research collaboration through [GitHub Issues](https://github.com/ZunhaiSu/awesome-low-precision-rl/issues). Primary sources and precise section/equation references make corrections especially useful. See [contribution guidance](CONTRIBUTING.md) for catalog fields, evidence records, and version handling.

## Template, status, and license

The paper adapts the **typesetting template** from [arXiv:2601.14004v4](https://arxiv.org/abs/2601.14004v4); its scientific framework is specific to this survey. Attribution and modifications are documented in [TEMPLATE.md](docs/TEMPLATE.md).

The survey is under active development. Its scientific scope and source versions are documented alongside the manuscript; editorial assessments are available in the [review history](docs/REVIEW.md).

Repository content and template adaptations use [CC BY-SA 4.0](LICENSE). Linked papers retain their own licenses; their PDFs are not redistributed here.
