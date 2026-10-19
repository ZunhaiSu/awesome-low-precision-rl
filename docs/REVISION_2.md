# Second review cycle: three substantive passes

Date: 2026-10-19. This cycle revises the complete manuscript delivered after the first three editorial rounds. It consists of three additional self-review passes, with a saved source snapshot after each pass. It is editorial self-review, not external peer review or experimental replication.

## Overall assessment before revision

The eight-section framework is coherent and the component-level classification is a useful contribution. However, the draft was stronger as a conceptual guide than as an evidence-rich survey. Three shortcomings required substantive changes:

1. Conditional importance correction was carefully qualified, but the missing full-response formula made the distinction harder to verify. Behavior-probability and execution-state semantics also needed tightening.
2. The synthesis contained too many general cautions and too few source-specific observations. The discussion of approximation and implementation remained abstract in places.
3. Some secondary discussion locations in the catalog did not match the manuscript. The taxonomy summary appeared too late, and a new evidence table needed pagination work.

**Editorial decision:** substantive revision. More polishing alone would not resolve these issues.

## Pass 1 — technical precision

**Evaluation.** The basic notation is sound, but readers need to see which change-of-measure statement is exact and which practical loss is only a surrogate. Cache state and post-decoding probabilities matter when describing the actual behavior law.

**Implemented changes.** Added full-response likelihood factorization and the response-level policy-gradient identity, including support, stopping, and fixed-behavior assumptions. Distinguished raw returned model log-probabilities from transformed sampling probabilities. Clarified deterministic execution schedules, cache provenance, and unobserved execution randomness. Derived the sign-dependent clipping branches and added a clearly labeled illustrative example. Made the top-k reconstruction and detached coefficients in Score Centering explicit.

**Verification.** Compiled the revised source; checked the changed equation pages visually. No undefined references or citations appeared. The conditional and response-level expressions are not presented as equivalent estimators for arbitrary group-normalized advantages.

**Residual limitation.** These are explanatory identities under stated assumptions. They do not turn surrogate gradients through quantizers or reconstructed behavior distributions into exact gradients.

## Pass 2 — evidence and cross-paper synthesis

**Evaluation.** A survey needs to say what the papers actually establish. Generic warnings about heterogeneous experiments were overrepresented.

**Implemented changes.** Rewrote the stability/quality synthesis around three source-backed findings: correction over the learning trajectory, numerical coupling at a named interface, and preservation of signed update contributions. Added six selected within-paper comparisons with regimes, observations, and interpretive limits. Added source-section locators in `data/evidence.json`. Distinguished best-checkpoint selection from final-checkpoint comparison. Used one within-study timing example to distinguish cumulative rollout speedup from cumulative full-iteration speedup. Explicitly separated AIS's autoregressive and diffusion evidence from the autoregressive equations used in this survey.

**Primary checks.** QuRL Sections 4–5; QUADS Section 4.3; Score Centering Section 5 and Appendix A; Full Pipeline FP8 Sections 3–5; TRIAGE Sections 3–5 and Appendix B; KV4-RL Sections 5–6. Public links and precise locators are stored with the evidence records.

**Verification.** Compiled and inspected both pages of the initial evidence-table layout. The first split left only one row on the preceding page; this was queued for the third pass.

**Residual limitation.** The six evidence records are selected illustrations, not a complete experimental extraction for all twenty focal works. Absolute results across papers remain incomparable without matching conditions; no new benchmark was conducted.

## Pass 3 — scholarly presentation and consistency

**Evaluation.** The argument was stronger after the second pass, but navigation and metadata consistency still weakened the presentation.

**Implemented changes.** Moved the five-class summary beside its initial definition. Sharpened the contribution paragraph. Replaced remaining editorial instructions with direct scientific statements. Explained both stages of Calibrated Clipping. Made the open questions specify what remains unresolved and what would distinguish useful progress. Kept the evidence table together. Audited and corrected every secondary section location against actual in-text citations; added explicit discussion of adopted TIS/MIS where needed. Synchronized the appendix, catalog, README, and source notes. Removed the local-release label from the paper's abstract panel.

**Verification.** The final source is compiled in the project and in a clean directory containing only `survey.tex`; all pages are rendered for inspection. The checker verifies citations, references, bibliography consistency, the embedded class, all eight main sections, primary/secondary locations, evidence keys, and local links. Final compiler and page-count details are recorded in [BUILD.md](BUILD.md).

**Residual limitation.** Source coverage remains a curated narrative snapshot. The author names and affiliations were supplied after this review cycle and have now been added to the manuscript. Three additional self-review passes improve the manuscript but do not provide independent subject-matter validation.

## Editorial assessment after revision

| Dimension | Before this cycle | After this cycle |
|---|---|---|
| Scientific organization | Coherent eight-section framework | Preserved; taxonomy is introduced where first needed |
| Technical precision | Clear conditional caveats, incomplete sequence-level bridge | Explicit response-level bridge, signed clipping logic, and behavior semantics |
| Synthesis | Mostly general comparison principles | Source-linked observations support three concrete findings |
| Method comparison | Component classifications and interface costs | Adds implementation details, evaluation rules, and evidence boundaries |
| Navigation and consistency | Some inaccurate secondary section locations | Catalog and appendix locations checked against the text |
| Readiness | Complete scholarly draft needing substantive revision | Stronger scholarly draft ready for author and subject-matter review |

The most valuable remaining work is a targeted author review of source coverage and claims. A new benchmark is not required for the survey's stated narrative purpose. There is no basis for assigning an acceptance probability or claiming that self-review has made the manuscript submission-ready.
