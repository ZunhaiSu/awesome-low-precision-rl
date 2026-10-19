# Current manuscript validation

Validated on 2026-10-19 after the five-pass prose and synthesis revision.

- Manuscript: **25 pages**, 20 focal works, 26 references, and 13 source-located core evidence records.
- Author and affiliation: **Zunhai Su, The University of Hong Kong**; PDF author metadata agrees.
- Navigation: the introduction begins on page one. A complete one-page contents listing follows Section 1, covering all eight sections and three appendices; PDF bookmarks remain available.
- Figures: three embedded TikZ figures. The two existing README SVG assets remain consistent with their unchanged TikZ definitions.
- Built-in LaTeX compiler: success on the final source.
- Tectonic 0.17.0: successful project build and a separate clean build whose only supplied project file was `survey.tex`; both produced 25-page PDFs. No external figure or bibliography file is required for this standalone build.
- Consistency checker: all focal and bibliography keys, citations, labels, primary/secondary discussion locations, matching embedded class, eight sections, thirteen core evidence records, local links, author metadata, and printed-contents placement passed.
- Visual inspection: all 25 pages rendered and reviewed. The first page, complete contents, and evidence-table page were also inspected at a readable scale. The corpus table starts on a fresh page and is kept together.
- Each of the five editorial passes compiled successfully. Source/PDF snapshots were compared during revision; representative prose comparisons appear in [REVISION_3.md](REVISION_3.md).

Nonfatal legacy package encoding warnings and one underfull bibliography paragraph remain. No overfull boxes, undefined citations, unresolved cross-references, or compilation errors were observed. The README's conventional `latexmk` command is an alternative build option and was not independently tested in this environment.

These checks establish document integrity and portability. They do not establish experimental reproduction or independent peer review.
