# Current manuscript validation

Current checks cover the restored contents typography, expanded work-to-class taxonomy, and Surveyed Papers appendix. The literature snapshot remains October 19, 2026.

- Manuscript: **27 pages**, 20 focal works, 26 references, and 13 source-located core evidence records.
- Public PDF: repository-root `Survey.pdf` is an exact copy of `survey/survey.pdf`; the checker enforces this match.
- Author and affiliation: **Zunhai Su, The University of Hong Kong**; PDF author metadata agrees.
- Navigation: the first page contains the title/abstract panel and a vector survey overview. Pages two and three contain the complete contents in the original template typography, covering all eight sections and three appendices. The introduction begins on page four; PDF bookmarks remain available.
- Figures: four embedded TikZ figures. Figure 2 is a work-to-class taxonomy covering all twenty focal studies. Three README SVG assets are exported from the overview, taxonomy, and clipping definitions.
- Built-in LaTeX compiler: success on the final source.
- Tectonic 0.17.0: successful project build and a separate clean build whose only supplied project file was `survey.tex`; both produced 27-page PDFs. No external figure or bibliography file is required for this standalone build.
- Consistency checker: all focal and bibliography keys, citations, labels, primary/secondary discussion locations, matching embedded class, eight sections, thirteen core evidence records, local links, author metadata, and printed-contents placement passed.
- Visual inspection: the four opening pages, taxonomy page, and both surveyed-paper table pages were rendered and inspected. The unchanged body figures and tables retain the earlier full-document visual review. The Surveyed Papers table begins on a fresh page and repeats its header across two pages. The first-page overview remains in place above the contents break.
- Each of the five editorial passes compiled successfully. Source/PDF snapshots were compared during revision; representative prose comparisons appear in [REVISION_3.md](REVISION_3.md).

Nonfatal legacy package encoding warnings and one underfull bibliography paragraph remain. No overfull boxes, undefined citations, unresolved cross-references, or compilation errors were observed. The README's conventional `latexmk` command is an alternative build option and was not independently tested in this environment.

These checks establish document integrity and portability. They do not establish experimental reproduction or independent peer review.
