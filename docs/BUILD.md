# Current manuscript validation

Validated on 20 October 2026 for the [integrated edition](REVISION_5.md). The literature snapshot remains 19 October 2026.

- **Manuscript:** 28 pages, eight main sections, twenty focal studies, twenty-six references, thirteen source-located core evidence records, and ten original vector figures.
- **Author:** Zunhai Su, The University of Hong Kong; PDF author metadata agrees.
- **Navigation:** title, abstract, and graphical overview on page one; original contents typography on pages two and three; introduction from page four; conclusion on page twenty-three; Surveyed Papers appendix from page twenty-four.
- **Integrity:** all eleven displayed equations, all twenty appendix paper entries, and bibliography content match the preceding technical edition. The classification and primary/secondary discussion locations pass the consistency checker.
- **Compilation:** the built-in editor compiler and Tectonic 0.17.0 both succeed on the final source. A clean directory containing only `survey.tex` also builds a 28-page PDF. The embedded class and bibliography provide the standalone distribution.
- **Diagnostics:** no overfull or underfull boxes, undefined citations, unresolved references, or LaTeX errors in the final Tectonic build. Nonfatal encoding warnings from legacy packages remain.
- **Visual review:** all 28 pages rendered and inspected. Final bibliography changes were re-rendered and inspected at a readable scale. The conclusion fits on the final main-text page, and bibliography entries remain together across page breaks.
- **Figures:** all ten SVG exports are valid XML. The build/export command regenerates them from the manuscript's TikZ definitions and shared palette. Analytical constructions remain identified separately from empirical observations.
- **Public PDF:** root `Survey.pdf` and `survey/survey.pdf` match byte for byte.
- **Repository:** citations, bibliography keys, figure markers, local links, image paths, author fields, matching class copies, and the eight-section framework pass `scripts/validate.py`. README navigation reflects the revised research-findings heading.

The current cycle compared the main historical versions and completed four focused manuscript revisions, with a successful build saved after each. This is editorial and technical self-review, without new experiments or external peer review. The source-selection and evidence limitations remain explicit in the manuscript.
