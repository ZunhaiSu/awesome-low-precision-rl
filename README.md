# Awesome Low-Precision RL

### Quantized Rollouts and Training–Rollout Mismatch

**A curated reading list on quantized rollouts and training–rollout mismatch in LLM reinforcement learning.**

This repository accompanies **Training–Rollout Mismatch in Low-Precision LLM Reinforcement Learning: A Survey**. It brings together the papers, technical taxonomy, and source-linked evidence needed to understand how low-precision rollout generation changes policy optimization. The collection covers numerical execution, gradient estimation, update control, and the trade-offs between learning quality and system efficiency.

**Author:** Zunhai Su

**Affiliation:** The University of Hong Kong

**Snapshot:** 2026-10-19 · **Focal corpus:** 20 unique contributions · **Status:** living survey · under active development.

[GitHub repository](https://github.com/ZunhaiSu/awesome-low-precision-rl) · [Read the survey](survey/survey.pdf) · [LaTeX source](survey/survey.tex) · [Bibliography](references.bib) · [Machine-readable catalog](data/papers.json) · [Evidence records](data/evidence.json)

> **Updates and collaboration.** This survey and its companion collection are under active development. Suggestions for missing papers, technical corrections, reproducibility insights, and research collaborations are welcome through [GitHub Issues](https://github.com/ZunhaiSu/awesome-low-precision-rl/issues).

![Survey overview: numerical execution and learning in a shared feedback loop](figures/overview.svg)

## Contents

- [Scope](#scope)
- [Survey organization](#survey-organization)
- [Taxonomy](#taxonomy)
- [Reading paths](#reading-paths)
- [Paper catalog](#paper-catalog)
- [How to interpret results](#how-to-interpret-results)
- [Build and validate](#build-and-validate)
- [Citation](#citation)
- [Contribute](#contribute)
- [Template and attribution](#template-and-attribution)
- [License](#license)

## Scope

The collection focuses on the interface between the policy that generates a rollout and the numerical policy used to compute its learning update. It includes weight, activation, and KV-cache quantization; low-precision execution on one or both endpoints; and general training–inference mismatch work needed to explain those settings.

The twenty focal entries have three editorial roles: **13 method/system studies, 6 formulation or general TIM supporting studies, and 1 exploration boundary case**. These are writing roles, not quality rankings or claims about whether a paper contains direct quantization experiments. Foundational RL and neighboring surveys appear in the bibliography but are not counted as focal contributions.

This is a curated narrative collection, not an exhaustive systematic review. Pure low-precision pretraining, generic PTQ, and unrelated acceleration methods are not included merely because they use FP8 or FP4. No new benchmark results are claimed.

## Survey organization

The survey follows a progression from **policy semantics**, through **failure mechanisms** and **interventions**, to **published evidence and open problems**. Its central distinction is between changing the numerical computation that produces a policy and changing the learning rule applied to samples from that policy.

| Section | Focus | Question addressed |
|---|---|---|
| 1. Introduction and Scope | Motivation, inclusion boundaries, and research questions | What makes quantized rollout a distinct RL problem? |
| 2. Problem Formulation and Taxonomy | Learner, behavior, proximal, and reference policies; execution mismatch and staleness | Which distributions differ, and what is being corrected? |
| 3. Mechanisms | Numerical propagation, estimator drift, clipping decisions, feedback, and diagnosis | How can local numerical differences change learning? |
| 4. Numerical Design and Execution Alignment | Computation alignment, error control, and preservation of parameter updates | Which execution interface should be aligned or protected? |
| 5. Learning under Residual Mismatch | Estimator correction, policy-update control, schedule adaptation, and composition | How should the learner use data from a different numerical policy? |
| 6. Synthesis of Findings and Practical Trade-offs | Source-linked observations, learning outcomes, information requirements, and cost | What do the published studies establish under their actual conditions? |
| 7. Open Problems | Predictive diagnosis, method composition, stateful execution, and generalization | Which unresolved questions would make the results more transferable? |
| 8. Conclusion | Integrated perspective on numerical fidelity and learning correction | What principles emerge across the literature? |

Three contributions connect these sections: **explicit policy and probability semantics**, **classification of operative method components**, and **evidence synthesis with stated conditions and limits**. Appendix A contains a **Surveyed Papers** table covering all twenty focal works, their numerical regimes, method components, and discussion locations. The other appendices document source/version handling and evidence interpretation. Section 6 synthesizes existing results; the survey does not introduce a new experimental benchmark.

## Taxonomy

![Component taxonomy of low-precision RL](figures/taxonomy.svg)


The unit of classification is a **component**, so a paper may occupy multiple cells.

| Code | Intervention | Main discussion | Representative components |
|---|---|---|---|
| A1 | Align computation between learner and rollout | §4.1 | Jet-RL; QaRL QAT; QUADS asymmetric QAT; TRACE; R3 as background |
| A2 | Control quantization error and preserve parameter updates | §4.2 | QuRL UAQ; QUADS RAC; FP8-RL calibration; KV4-RL protection |
| B1 | Correct gradient estimation | §5.1 | FlashRL/TIS; AIS; CIS; Score Centering |
| B2 | Control policy-update influence | §5.2 | QuRL ACR; QaRL TBPO; Calibrated Clipping; ACRL; TRIAGE |
| B3 | Adapt the optimization schedule | §5.3 | Beyond Precision, as general TIM support |

Precision format, W/A/KV target, architecture, adaptation regime, and collection schedule are **separate configuration labels**. CIS calibrates importance sampling; Calibrated Clipping calibrates update boundaries. QeRL is discussed in a boundary box; VeXact is a diagnostic reference.

## Reading paths

**Start with the problem:** FlashRL/TIS → MiniRL → VeXact. Read survey §§2–3 alongside these papers to separate actual behavior probabilities, proximal policies, execution mismatch, and staleness.

**Numerical interventions:** Jet-RL → QaRL → QUADS → TRACE. Then compare QuRL's UAQ, FP8-RL, and KV4-RL to understand numerical fidelity and selective precision.

**Learning interventions:** TIS → AIS → Score Centering and CIS. Continue with ACR/TBPO, Calibrated Clipping, ACRL, and TRIAGE to compare estimator correction with update control.

**Keep the boundary cases visible:** QeRL for quantization and exploration; Beyond Precision for optimization schedules; R3 and FP16-Mismatch for numerical and execution context. Reading order expresses conceptual dependencies, not a ranking or a claim of historical influence.

## Paper catalog

Dates below refer to first public appearance where recorded; the bibliography may cite a later formal publication. Each row is one contribution even when several components are discussed.

| First public date | Work and primary source | Role / components | Primary survey location |
|---|---|---|---|
| 2025 | **FlashRL / TIS** — [On the Rollout-Training Mismatch in Modern RL Systems](https://www.opt-ml.org/papers/2025/paper116.pdf) | core; B1 | 5.1 |
| 2025-10-13 | **QeRL** — [QeRL: Quantization-enhanced Low-Rank Reinforcement Learning for LLMs](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a15a2ece7f0663d1ba7db91103ac61c9-Abstract-Conference.html) | boundary; Boundary | Box 1 |
| 2025-10-13 | **R3** — [Stabilizing MoE Reinforcement Learning by Aligning Training and Inference Routers](https://arxiv.org/abs/2510.11370) | support; Support; A1 | 3.1 |
| 2025-10-30 | **FP16-Mismatch** — [Defeating the Training-Inference Mismatch via FP16](https://arxiv.org/abs/2510.26788) | support; Support; A2 | 3.1 |
| 2025-12-01 | **MiniRL** — [Stabilizing Reinforcement Learning with LLMs: Formulation and Practices](https://arxiv.org/abs/2512.01374) | support; Support; B1/B2 | 2.1 |
| 2026-01-20 | **Jet-RL** — [Jet-RL: Enabling On-Policy FP8 Reinforcement Learning with Unified Training and Rollout Precision Flow](https://arxiv.org/abs/2601.14243) | core; A1; A2 | 4.1 |
| 2026-01-26 | **FP8-RL** — [FP8-RL: A Practical and Stable Low-Precision Stack for LLM Reinforcement Learning](https://arxiv.org/abs/2601.18150) | core; A2; system | 4.2 |
| 2026-02-02 | **Beyond Precision** — [Beyond Precision: Training-Inference Mismatch is an Optimization Problem and Simple LR Scheduling Fixes It](https://arxiv.org/abs/2602.01826) | support; Support; B3 | 5.3 |
| 2026-02-15 | **QuRL** — [QuRL: Efficient Reinforcement Learning with Quantized Rollout](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6b4880ced785077159b340710ceb7681-Abstract-Conference.html) | core; B2; A2 | 5.2 |
| 2026-04-09 | **QaRL** — [QaRL: Rollout-Aligned Quantization-Aware RL for Fast and Stable Training under Training--Inference Mismatch](https://aclanthology.org/2026.findings-acl.841/) | core; A1; B2 | 4.1 |
| 2026-05-13 | **AIS** — [AIS: Adaptive Importance Sampling for Quantized RL](https://arxiv.org/abs/2605.13907) | core; B1 | 5.1 |
| 2026-05-14 | **VeXact / Diagnosing TIM** — [Diagnosing Training Inference Mismatch in LLM Reinforcement Learning via a Zero-Mismatch Reference](https://arxiv.org/abs/2605.14220) | support; Diagnostic | 3.4 |
| 2026-07-17 | **QUADS** — [QUADS: Stabilizing NVFP4 Reinforcement Learning for MoE via QUantization-error Alignment across Dual Sides](https://arxiv.org/abs/2607.15810) | core; A1; A2 | 4.1 |
| 2026-07-27 | **ACRL** — [ACRL: Adaptive Control of Training-Inference Discrepancy for Stable Reinforcement Learning](https://arxiv.org/abs/2607.24062) | core; B2 | 5.2 |
| 2026-09-17 | **Score Centering** — [Score Centering Stabilizes Off-policy Reinforcement Learning](https://arxiv.org/abs/2609.20807) | core; B1 | 5.1 |
| 2026-09-19 | **Full Pipeline FP8 RL** — [Towards Full Pipeline FP8 Reinforcement Learning for LLMs](https://arxiv.org/abs/2609.22870) | core; B2; system | 5.2 |
| 2026-09-26 | **CIS** — [Rethinking Training-Inference Mismatch in LLM Reinforcement Learning: Where It Arises and How to Correct It](https://arxiv.org/abs/2609.32444) | support; Support; B1 | 5.1 |
| 2026-10-05 | **TRIAGE** — [TRIAGE: Direction-Aware Mismatch Stabilization of Native NVFP4 Reinforcement Learning](https://arxiv.org/abs/2610.07043) | core; B2 | 5.2 |
| 2026-10-06 | **TRACE** — [TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models](https://arxiv.org/abs/2610.07767) | core; A1 | 4.1 |
| 2026-10-10 | **KV4-RL** — [KV4-RL: Unlocking Faster Asynchronous Rollouts for RLVR with INT4 KV Cache Quantization](https://arxiv.org/abs/2610.14448) | core; A2; system | 4.2 |

Full version notes, secondary locations, and scope caveats are in [`data/papers.json`](data/papers.json) and the survey's corpus appendix. The catalog deliberately does not invent unverified code-repository links.

## How to interpret results

![Sign-dependent clipping of the policy surrogate](figures/clipping.svg)

The clipping diagram is an analytical illustration of the standard surrogate with positive and negative advantages; it is not a cross-paper performance plot. The flat branch switches sides with the sign of the learning signal. See §3.2 of the survey for the ratio semantics.


The [evidence records](data/evidence.json) cover all thirteen core method/system studies, linking their main observations to primary-source sections and interpretive limits. Six representative comparisons appear in the manuscript's evidence table. They support three recurring conclusions: assess correction over the learning trajectory; identify the numerical interface that is coupled; and examine which signed updates survive clipping or gating. The records are qualitative synthesis aids, not a complete result database.

Keep four outcomes separate: **numerical agreement, optimization stability, learned-policy quality, and runtime cost**. A smaller average gap is not a stability guarantee; completing training is not equivalent to reaching comparable quality; rollout throughput is not end-to-end speedup.

When adding a result, record the learner/sampler precision paths, model, task, training horizon, baseline, evaluation precision, and timing scope. Mark unavailable details as unreported. Avoid cross-paper performance rankings when these conditions differ.

## Build and validate

The manuscript includes its bibliography and an embedded copy of the supplied template class. `survey.tex` can therefore be shared as a single LaTeX source file. The separate `.cls` is provided for conventional editing and must match the embedded copy.

```sh
python3 scripts/validate.py
cd survey
latexmk -pdf -interaction=nonstopmode -halt-on-error survey.tex
```

Alternatively, with [Tectonic](https://tectonic-typesetting.github.io/):

```sh
cd survey
tectonic survey.tex
```

The three README diagrams are exported from the TikZ definitions embedded in the manuscript. With Tectonic and Poppler available, regenerate them with `python3 scripts/export_figures.py`. See [figure notes](docs/FIGURES.md) for their scope.

The PDF is supplied as a reading copy. `references.bib` is available for reuse, but the standalone source does not require a separate BibTeX run. A reasonably complete TeX installation is needed for the original template's fonts and packages; Tectonic may download its TeX bundle on first use.

Repository layout:

```text
README.md
references.bib
survey/       manuscript, matching template class, rendered PDF
figures/      vector diagrams for the manuscript and README
data/         20-entry focal catalog and selected source-linked evidence
docs/         taxonomy, source notes, template provenance, review cycles, build notes
scripts/      dependency-free consistency checker
CONTRIBUTING.md
LICENSE
```

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

See [CONTRIBUTING.md](CONTRIBUTING.md). A useful addition identifies the primary source, its direct connection to low-precision rollout or TIM, the component it contributes, its numerical configuration, and its evidence boundary. Corrections to versions, terminology, or attribution are especially valuable.

Keep publication and preprint versions in one record. Label new combinations as hypotheses unless the cited source evaluates them. Do not upload third-party PDFs to this repository.

## Template and attribution

The manuscript uses `mystyle.cls` from [arXiv:2601.14004v4](https://arxiv.org/abs/2601.14004v4). This is a **typesetting template adaptation only**. The eight-section scientific framework is the framework developed for this survey. See [template provenance](docs/TEMPLATE.md) for the source's RAIL/DeepMind lineage, retained license notice, and modifications.

The manuscript is under active development. Missing papers, technical corrections, and research collaboration proposals are welcome through [GitHub Issues](https://github.com/ZunhaiSu/awesome-low-precision-rl/issues). It has no assigned DOI or arXiv identifier and is not presented as peer reviewed. The [editorial history](docs/REVIEW.md) and [latest review cycle](docs/REVISION_3.md) document the draft's internal revisions.

## License

Repository content and template adaptations are distributed under [CC BY-SA 4.0](LICENSE), consistent with the supplied class's license. Linked papers remain under their respective licenses. Template attribution is preserved in the class and [TEMPLATE.md](docs/TEMPLATE.md).
