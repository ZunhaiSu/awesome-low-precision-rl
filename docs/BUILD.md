# Current release validation

Validated on 2026-10-19 after the author, layout, and figure update.

- Current manuscript: **24 pages**, 20 focal works and 26 references.
- Author and affiliation: **Zunhai Su, The University of Hong Kong**. The PDF author metadata agrees.
- First-page layout: compact title/abstract panel followed directly by the introduction; no separate cover or printed contents page. PDF section bookmarks remain.
- Figures: three embedded TikZ figures, including two newly exported SVG diagrams for the README. The exported SVG files parse successfully.
- Built-in LaTeX compiler: success on the final source.
- Tectonic 0.17.0: successful PDF export in the project and from a new directory containing only `survey.tex`; both have 24 pages. The external SVG files are not needed to build the paper.
- Consistency checker: citations, labels, bibliography keys, embedded class, eight main sections, discussion locations, evidence keys, local links, the single author and affiliation, and the three figure environments passed.
- Visual inspection: all 24 pages rendered and inspected; the title page, taxonomy diagram, and clipping plot were additionally checked at a readable scale.

Nonfatal legacy package encoding warnings and one underfull bibliography box remain. No overfull boxes, undefined citations, or compilation errors were observed. The conventional `latexmk` command in the README is an alternative build option and has not been independently tested in this environment.

These checks establish document integrity and portability, not experimental reproduction or independent peer review. The six-pass editorial history describes earlier drafts; this note records the current layout.
