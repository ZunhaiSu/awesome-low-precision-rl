# Editorial review history

The first cycle below records the original delivered draft. The additional cycle at the end links to the current revision assessment.

This is self-review of a working manuscript, not independent peer review or experimental replication. The scientific outline remains the agreed eight-section framework. The reference paper supplies the actual LaTeX template only.

## Round 1 — technical semantics and source attribution

**Assessment.** The draft separated numerical and optimization interventions, but the decoupled surrogate needed explicit frozen-advantage semantics. Its same-snapshot policy could be mistaken for a mandatory stored proximal model. Derivative identities also needed a qualification for surrogate gradients through quantizers.

**Changes.** Stated fixed sampled advantages and detached correction weights; clarified the conceptual snapshot versus implementation proximal policy; added the surrogate-gradient qualification. Checked the focal count (13 core, 6 supporting, 1 boundary) and prevented conference/preprint double counting. Removed any suggestion that the reference survey supplied our content framework.

**Template correction.** Used the actual supplied class, preserved its attribution, removed unrelated dormant author text, and corrected two XeTeX/font compatibility settings without replacing the template's visual identity.

**Remaining concern.** The qualitative synthesis still needed a more concrete contrast between information requirements and failure modes, rather than repeated general cautions.

## Round 2 — argument, synthesis, and readability

**Assessment.** The first complete draft was technically organized, but its evidence section relied too heavily on generic cautions about incomparable settings. It needed a concrete comparison that changes how a reader selects and combines methods.

**Changes.** Added a source-linked contrast between numerical-path treatment, native low-precision update control, KV-focused partial rollout, and full-pipeline FP8. Added an information/implementation requirements table that compares behavior probabilities, score expectations, matched numerical paths, rollout guidance, reference ratios, and protected cache state. Clarified that the progression of A1 methods is not a superiority ranking. Compressed repeated framing in the synthesis section.

**Scope retained.** All eight main sections remain; no numerical leaderboard, invented experiment, or claim of an exhaustive search was added. Original figures and tables serve this survey's framework rather than importing the reference paper's framework.

**Remaining concern.** Final typography, page breaks, links, and portable single-file compilation still required a separate verification pass.

## Round 3 — publication-style prose, typography, and release consistency

**Assessment.** The rendered draft was readable and had no visible overlap, but the table of contents spilled onto a mostly empty second page. Some top floats could precede the section text that introduced them. A few sentences described writing choices rather than the scientific subject.

**Changes.** Compacted the contents typography within the original template; prevented floats from appearing before their source location or escaping their main section, and allowed in-place placement to remove an unnecessarily sparse page; replaced draft-process phrasing in the scientific discussion. Verified the 20-entry catalog against all manuscript citations and the 26-entry bibliography. The class embedded in the single-file source is checked against the supplied separate class.

**Validation.** The final 22-page manuscript compiled successfully and every page was rendered and visually inspected. A separate clean-directory build containing only `survey.tex` also succeeded and generated its own template class. See [build validation](BUILD.md) for tested compilers and nonfatal warnings. The dependency-free checker verifies citation keys, cross-references, eight main sections, local README links, and absence of private paths in portable metadata.

## Editorial conclusion

The result is a complete narrative-survey draft, not only an outline. Its strengths are explicit policy semantics, a component-level taxonomy, and synthesis organized around information requirements and evidence conditions. The main limitations remain the curated rather than exhaustive corpus, heterogeneous primary evidence, limited direct low-bit support for schedule adaptation, and lack of independent reproduction. Three self-review rounds do not substitute for subject-matter peer review or author approval.

At the end of this review cycle, author details were pending. Author details were subsequently supplied and later revised; the current manuscript records Zunhai Su, The University of Hong Kong. Any intended venue requirements remain to be applied; no DOI, arXiv identifier, repository URL, or peer-review status has been invented.

## Additional revision cycle

A subsequent user-requested cycle completed three more substantive passes. See [second-cycle assessment and changes](REVISION_2.md). The original review above records the first delivered draft; [BUILD.md](BUILD.md) records validation of the current manuscript.

## Five-pass prose and synthesis revision

The next revision strengthens the connected scientific argument, expands qualitative evidence records to all thirteen core studies, and restores a complete printed contents page. See [the five-pass assessment and before/after examples](REVISION_3.md). The earlier entries remain a history of previous drafts; [BUILD.md](BUILD.md) describes the current manuscript.
