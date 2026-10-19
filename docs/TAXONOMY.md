# Taxonomy and section responsibilities

1. Introduction and Scope: motivation, inclusion boundary, questions.
2. Problem Formulation and Taxonomy: learner, behavior, proximal, reference; execution mismatch versus parameter change.
3. Mechanisms: conditional effects, cross-step feedback, diagnosis. QeRL is a separate exploration boundary box.
4. Numerical Design and Execution Alignment: A1 matching computation; A2 controlling quantization error and preserving parameter updates; limits of alignment.
5. Learning under Residual Mismatch: B1 estimator corrections; B2 update controls; B3 schedule adaptation; composition and failure modes.
6. Synthesis of Findings and Practical Trade-offs: published coverage, stability/quality findings, costs, and evidence limits. No new benchmark.
7. Open Problems: predictive diagnosis, composition, staleness/long-horizon interaction, evidence standards.
8. Conclusion: conditional synthesis.

A1/A2 and B1/B2 are not mathematically disjoint sets. Assign a component by its operative rule and design objective; document secondary effects through cross-references. A whole paper can contain several components. B3 remains a short section because direct low-bit evidence is limited in the current corpus.

Paper roles (core/support/boundary) and evidence types are distinct. MiniRL is principally a formulation reference here but includes direct FP8 rollout experiments. QeRL has direct quantized-RL evidence without being a mismatch-elimination method. VeXact is a diagnostic reference rather than a quantized accelerator.

Figure 2 maps every focal work onto the taxonomy, including cross-category components and supporting connections. Appendix A provides the corresponding Surveyed Papers table with numerical regimes and discussion locations.
