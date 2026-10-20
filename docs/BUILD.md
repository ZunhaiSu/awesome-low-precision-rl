# Current manuscript validation

The public manuscript was validated on 20 October 2026. Its literature snapshot remains 19 October 2026.

- **Manuscript:** 30 pages, eight main sections, twenty focal studies, twenty-six references, thirteen source-located core evidence records, and ten original vector figures.
- **Author:** Zunhai Su, The University of Hong Kong; PDF metadata agrees.
- **Navigation:** title, abstract, and graphical overview on page one; contents on pages two and three; main text from page four; Surveyed Papers appendix from page twenty-five; terminology table on page twenty-eight.
- **Document checks:** compilation and citation checks passed in the separate authoring project. All thirty pages were rendered and visually inspected; the evidence comparison and paper appendix were checked at a readable scale.
- **Public files:** the manuscript is distributed only as the root [Survey.pdf](../Survey.pdf). LaTeX sources and manuscript compilation tools remain in the Overleaf authoring project.
- **Catalog checks:** `python3 scripts/validate.py` checks canonical metadata, generated views, complete linked titles, evidence coverage, local links, and the PDF-only publication layout.
- **Publication:** updates are manual. A failed build must not replace the last successful PDF. The literature snapshot changes only after the corresponding source checks.

These checks establish document consistency, not independent experimental reproduction or external peer review.
