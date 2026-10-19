# LaTeX template provenance

The paper uses the actual `mystyle.cls` supplied with [arXiv:2601.14004v4](https://arxiv.org/abs/2601.14004v4), not that paper's scientific outline.

The supplied class identifies its lineage as an edited Berkeley RAIL / Google DeepMind report template and declares **CC BY-SA 4.0**. Its provenance and license notice are preserved in `survey/mystyle.cls` and in the embedded copy inside `survey/survey.tex`.

Preserved features: 11-point letterpaper, the source's font stack, blue section headings, pale-blue title/abstract panel, running title, numbered references, and right-aligned page numbers. The source main file's one-inch margin override is also applied.

Changes: one dormant, unrelated hard-coded author-contribution sentence was removed; small-cap microtype tracking was disabled for XeTeX compatibility and the same XCharter family was forced to Type 1 for consistent font encoding; manuscript-specific macros and original diagrams were added. The reference paper's prose, figures, author list, contact information, and repository identity are not reused.

`survey.tex` embeds the class using `filecontents*`, so the full manuscript is available as one LaTeX file. A matching separate class is supplied for conventional project editing. Both copies must remain synchronized.

The eight-section scientific framework remains the framework developed for this low-precision RL survey.

Front-matter adaptation: the title/abstract panel is compacted at manuscript level, the introduction begins on the first page, and a complete one-page contents listing follows the introduction. PDF section bookmarks provide additional navigation. The original class and its embedded copy remain synchronized. Three original TikZ figures now explain the intervention taxonomy, the learning feedback loop, and sign-dependent clipping; the two new diagrams are also supplied as standalone vector assets.
