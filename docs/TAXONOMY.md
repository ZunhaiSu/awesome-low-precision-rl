# Classification and evidence roles

Three views describe a contribution: **mismatch source** (why probabilities differ), **intervention target** (what the component changes), and **execution setting** (where the source tested it). Numerical execution, routing and lag are source descriptions; W/A/KV precision, adaptation and collection are setting axes. They are not peer method classes.

**A addresses the numerical source; B manages the learning consequences.** A changes how a policy is numerically evaluated or how parameter changes survive quantization. B changes how collected experience forms, constrains, or passes acceptance for an update while mismatch remains. B can correct gradient drift or preserve useful updates without forcing learner and sampler probabilities to agree.

These are intervention targets, so numerical design can act on the learner, sampler, or both. A and B components can operate together; the distinction is not a division between training and inference. Four primary classes refine these targets:

| Class | Direct target | Assignment rule |
|---|---|---|
| A1 | Shared computation | Match learner and rollout operators, representations, or realized execution choices. |
| A2 | Numerical fidelity | Preserve update resolution or sensitive information through scaling, compensation, calibration, or selective precision. |
| B1 | Estimation | Change action weights or score expectations to address a distributional estimation problem. |
| B2 | Update influence | Change the constraints, magnitude, or direction of sampled contributions, or accept/reject a whole candidate update. |

**Complementary scheduling.** Beyond Precision remains under §5.3 with navigation tag B3. Its general-TIM scheduling evidence is useful context, but it does not form a fifth primary route with equal direct low-bit coverage.

The classes answer four questions: can the two computations agree more closely (A1); is useful information preserved at low precision (A2); how should behavior samples estimate a target gradient (B1); and which updates should influence the next policy (B2)? The distinction follows the component's direct target, not its software primitive. Both B1 and B2 can multiply a loss by weights. B1 starts from an estimation target; B2 starts from a constraint, selection rule, or acceptance criterion. Truncation can bias an estimator, and update control can also change estimation.

A loss can contain an importance ratio while contributing a new update constraint. DPPO and DRPO are classified by trust-region geometry (B2), whereas Score Centering changes a conditional gradient expectation (B1). The presence of a ratio or mask alone does not fix the assignment.

These purposes can overlap. QaRL introduces A1 and B2 components, QuRL introduces A2 and B2 components, and QUADS combines A1 with A2. Rollout-ResQ is A2 activation compensation. P3O, DRPO, and MIPU are B2 controls over batch reliability, divergence geometry, and whole-update acceptance. Miles contributes A1 contracts and A2 precision choices; QATFactory's QARL component aligns quantized representations while retaining BF16 training matmuls. A system's adoption of TIS is distinguished from its numerical or integration contribution.

`primary_section` and `secondary_sections` locate the survey discussion. They do not rank a paper's components, novelty, or evidence strength. Ordering in `categories` does not make other components less important.

Three other fields answer different questions:

- `role`: core method/system study, supporting formulation/theory/general mismatch study, or exploration boundary case.
- `evidence_domain`: direct low-precision RL, general TIM, higher-precision comparison, diagnostic reference, or exploration boundary. MiniRL has a supporting role and direct FP8 experiments; QeRL contributes low-precision exploration evidence at a different research boundary.
- `replication_status`: whether this survey independently reproduced the source. The current records state that it did not; they do not characterize replication elsewhere.

Contribution roles describe relevance independently of experimental strength. Assessing evidence quality requires experiment-level controls, training seeds, uncertainty, baselines, and reproduction records.

Reviewed arXiv versions are pinned where the source record identifies one. Formal publication records remain distinct from arXiv versions; version-unspecified records are left explicit. The [catalog](CATALOG.md) and [source observations](EVIDENCE.md) are generated from the JSON records with `python3 scripts/build_tables.py`.

The [configuration and comparison records](COMPARISONS.md) additionally distinguish learner arithmetic, rollout W/A/KV scope, direct baselines, checkpoint selection and evaluation randomness. Method classes do not imply experimental validation in every precision regime.

The eight-section paper develops definitions and mechanisms before comparing numerical and learning interventions, then connects published findings to costs and open questions. Figure 2 maps all focal works, including contextual connections and the QeRL exploration boundary; Appendix A provides numerical regimes and discussion locations. The complete section outline is retained in the README and printed contents.

## Control decisions inside B2

| Decision | Representative components | Unit or signal level |
|---|---|---|
| Place update boundaries | QuRL ACR, QaRL TBPO, Calibrated Clipping | Token or response |
| Adapt to batch reliability | P3O | Batch ESS and objective weights |
| Choose constraint geometry | DPPO, DRPO | Token-level probability shifts |
| Select directional influence | ACRL, TRIAGE | Tokens/segments within responses |
| Accept a synchronized candidate | MIPU | Whole inference-policy candidate |

These are descriptions within B2, not five additional primary classes. QAT and PTQ describe adaptation procedures; low-rank/full-parameter updates and native/simulated arithmetic remain separate axes. QuRL also illustrates repeated quantization during RL without an explicit learner-side QAT path.

[Perspectives from the primary papers' related work](RELATED_WORK.md) explains the source distinctions used to refine this framework.

## Measurement is a separate view

A method class identifies the intervention target. A diagnostic identifies what is observed: numerical agreement, estimator reliability, update distortion, or learning outcomes. These views should not be conflated. See the [measurement map of all nineteen core studies](MEASUREMENTS.md) and §3.4 / Appendix E of the survey.
