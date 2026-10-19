# Current manuscript validation

Validated on 2026-10-20 after twenty editorial and visual rounds. The literature snapshot remains 2026-10-19.

- Manuscript: **29 pages**, 20 focal works, 26 references, 13 source-located core evidence records, and **10 original vector figures**.
- Author: **Zunhai Su, The University of Hong Kong**; PDF author metadata agrees.
- Navigation: title/abstract and graphical overview on page one, original contents typography on pages two and three, introduction from page four. The complete taxonomy and two-page Surveyed Papers table remain present.
- Public copy: root `Survey.pdf` and `survey/survey.pdf` match byte for byte.
- Built-in LaTeX compiler: success on the final source.
- Tectonic 0.17.0: project build and clean build from only `survey.tex` both produced 29-page PDFs. The embedded class and bibliography supply the standalone source; external SVGs are not build inputs.
- Public build command: `scripts/build.py --figures` successfully built the paper, refreshed the root copy, exported all ten SVGs, and ran the consistency checker.
- Integrity: bibliography/citation keys, labels, eight sections, primary and secondary discussion locations, all thirteen core evidence records, matching class copies, figure markers/exports, Markdown and HTML image paths, author metadata, and PDF copies passed.
- Visual review: all 29 final pages rendered and inspected. The policy, probability-tree, mechanisms, clipping, quantizer, learning-operator, evidence, and timing pages were also inspected at a readable scale during revision. The conclusion no longer spills a few lines onto a separate page.
- README: browser preview checked the hero, image scaling, catalog, and navigation; GitHub-compatible details keep supporting material expandable. The preview is a local approximation of GitHub styling.
- Numerical illustrations: checked the probability-tree reweighting, fixed-step quantizer cases, signed clipping derivatives away from boundaries, and normalized timing arithmetic.
- Revision record: twenty saved source/README snapshots; sixteen source-changing rounds compiled, while four README-only rounds retained the preceding PDF. See [REVISION_4.md](REVISION_4.md).

Nonfatal legacy package encoding warnings and one underfull bibliography paragraph remain. No overfull boxes, undefined citations, unresolved references, or compilation errors were observed. No independent experiments or external peer review are implied by these checks.
