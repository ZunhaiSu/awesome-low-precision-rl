# Current manuscript validation

Current checks cover the graphical opening added after the five-pass prose and synthesis revision. The literature snapshot remains October 19, 2026.

- Manuscript: **25 pages**, 20 focal works, 26 references, and 13 source-located core evidence records.
- Author and affiliation: **Zunhai Su, The University of Hong Kong**; PDF author metadata agrees.
- Navigation: the first page contains the title/abstract panel and a vector survey overview. Page two contains the complete contents, covering all eight sections and three appendices. The introduction begins on page three; PDF bookmarks remain available.
- Figures: four embedded TikZ figures. Three README SVG assets are exported from the overview, taxonomy, and clipping definitions.
- Built-in LaTeX compiler: success on the final source.
- Tectonic 0.17.0: successful project build and a separate clean build whose only supplied project file was `survey.tex`; both produced 25-page PDFs. No external figure or bibliography file is required for this standalone build.
- Consistency checker: all focal and bibliography keys, citations, labels, primary/secondary discussion locations, matching embedded class, eight sections, thirteen core evidence records, local links, author metadata, and printed-contents placement passed.
- Visual inspection: all 25 pages rendered and reviewed. The first three pages, complete corpus map, and evidence-table page were also inspected at a readable scale. The corpus table starts on a fresh page and is kept together. The first-page overview remains in place above the contents break.
- Each of the five editorial passes compiled successfully. Source/PDF snapshots were compared during revision; representative prose comparisons appear in [REVISION_3.md](REVISION_3.md).

Nonfatal legacy package encoding warnings and one underfull bibliography paragraph remain. No overfull boxes, undefined citations, unresolved cross-references, or compilation errors were observed. The README's conventional `latexmk` command is an alternative build option and was not independently tested in this environment.

These checks establish document integrity and portability. They do not establish experimental reproduction or independent peer review.
