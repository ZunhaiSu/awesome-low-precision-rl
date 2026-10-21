# Figures and visual conventions

Thirteen original vector figures connect the learning loop, method mechanisms and source-bound comparisons. Numerical examples are constructed illustrations; comparison sets retain their source configurations.

| Figure | Purpose | Interpretation |
|---|---|---|
| 1 · [Survey at a glance](../figures/overview.svg) | The rollout–learning loop, four intervention classes, and complementary source/target/setting views. | Conceptual synthesis. |
| 2 · [Component taxonomy](../figures/taxonomy.svg) | All 29 focal works, with scheduling and supporting roles shown separately. | Component assignments; no ranking. |
| 3 · [Policy identities](../figures/policies.svg) | Learner, sampling snapshot, actual behavior, proximal and KL-reference roles. | Probability semantics. |
| 4 · [Mechanism map](../figures/mechanisms.svg) | Weighting, conditional drift, clipping and feedback. | Conceptual synthesis. |
| 5 · [Signed clipping](../figures/clipping.svg) | Opposite active clipping boundaries for positive and negative advantages. | Analytical surrogate; epsilon 0.2 and advantages ±1. |
| 6 · [Measurement regimes](../figures/measurement_practice.svg) | Controlled shared-prefix numerical probes and online training diagnostics. | Distinct policy comparisons and estimands; no pooled measurement scale. |
| 7 · [Rollout-guided rounding](../figures/rounding.svg) | Learner 0.74 and rollout 0.76 on a fixed E2M1 interval. | Constructed example separating agreement from per-path error. |
| 8 · [Update visibility](../figures/quantization.svg) | Quantization-boundary crossings can differ from update magnitude. | Fixed-step scalar quantizer, avoiding ties. |
| 9 · [Score centering](../figures/centering.svg) | A behavior-weighted score mean of 0.3 becomes zero. | Exact two-action scalar-logit example. |
| 10 · [Learning operators](../figures/operators.svg) | Estimator correction, TRIAGE eligibility and normalized gate influence. | Local rules and illustrative raw weights. |
| 11 · [Comparison graphs](../figures/evidence.svg) | Separate TRACE and TRIAGE comparison graphs. | Edges mark direct comparisons; no cross-study ordering. |
| 12 · [Serialized timing](../figures/timing.svg) | Faster generation and added work affect total iteration time. | Constructed example with rollout share 0.6 and speedup 2. |
| 13 · [Conditional and response probabilities](../figures/prefixes.svg) | Local conditionals and visited prefix mass, in Appendix C. | Exact two-step illustration. |

Blue and teal identify numerical interventions; violet and amber identify estimation and update control. Slate identifies context and complementary scheduling. Labels, equations and line styles carry meaning independently of color.

The original Charter-based paper template and contents typography are retained. The first-page overview is followed by the contents and main text. Figures are exported from the same embedded TikZ source as the manuscript.

Figure labels and notes use a consistent sans-serif hierarchy with larger minimum text. The restrained blue, teal, violet and amber palette keeps the semantic classes readable on pale backgrounds; numerical examples and source comparisons retain distinct captions.
