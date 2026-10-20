# Classification and evidence roles

The unit of classification is a component. Its operative purpose identifies the class:

| Class | Direct target | Assignment rule |
|---|---|---|
| A1 | Shared computation | Match learner and rollout operators, representations, or realized execution choices. |
| A2 | Numerical fidelity | Preserve update resolution or sensitive information through scaling, compensation, calibration, or selective precision. |
| B1 | Estimation | Change action weights or score expectations to address a distributional estimation problem. |
| B2 | Update influence | Change acceptance, constraints, magnitude, or direction of sampled contributions. |
| B3 | Optimization schedule | Change the scale or schedule of learning over time. |

These purposes can overlap. QaRL introduces A1 and B2 components, QuRL introduces B2 and A2 components, and QUADS combines A1 with A2. A multiplicative weight can belong to B1 or B2 depending on its target. A system's adoption of TIS is distinguished from its numerical or integration contribution.

`primary_section` and `secondary_sections` locate the survey discussion. They do not rank a paper's components, novelty, or evidence strength. Ordering in `categories` does not make other components less important.

Three other fields answer different questions:

- `role`: core method/system study, supporting formulation/general mismatch study, or exploration boundary case.
- `evidence_domain`: direct low-precision RL, general TIM, higher-precision comparison, diagnostic reference, or exploration boundary. MiniRL has a supporting role and direct FP8 experiments; QeRL contributes low-precision exploration evidence at a different research boundary.
- `replication_status`: whether this survey independently reproduced the source. The current records state that it did not; they do not characterize replication elsewhere.

No E1–E4 or numerical quality grade is inferred from these fields. A quality assessment would need experiment-level extraction of controls, seeds, uncertainty, baselines, and reproduction. A formulation or diagnostic role is not evidence of weak experimental quality.

Reviewed arXiv versions are pinned where the source record identifies one. Formal publication records remain distinct from arXiv versions; version-unspecified records are left explicit. The [catalog](CATALOG.md) and [source observations](EVIDENCE.md) are generated from the JSON records with `python3 scripts/build_tables.py`.

The eight-section paper develops definitions and mechanisms before comparing numerical and learning interventions, then connects published findings to costs and open questions. Figure 2 maps all focal works, including contextual connections and the QeRL exploration boundary; Appendix A provides numerical regimes and discussion locations. The complete section outline is retained in the README and printed contents.
