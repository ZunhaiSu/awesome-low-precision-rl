# Contributing

This living survey grows through discussions as well as paper suggestions. Use [GitHub Issues](https://github.com/ZunhaiSu/awesome-low-precision-rl/issues) for missing work, technical corrections, or a research collaboration proposal. A short description of the idea and its connection to the survey is enough to start a conversation.

## Propose a paper

Include a primary-source URL and explain the connection to low-precision rollout or training–rollout mismatch. State whether the contribution is a method, a system, diagnostic evidence, or a boundary case. Identify components rather than assigning a whole paper to one exclusive category.

Add or update a record in `data/papers.json`. Preserve the existing schema, record the reviewed version, and keep conference and preprint versions together. Supply authors, title, first-publication date, primary discussion location, and scope note. Distinguish direct low-precision experiments from general TIM evidence.

For core studies, add a source-located observation and its interpretive limit to `data/evidence.json`. Update `README.md`, `references.bib`, and the inline bibliography/corpus table in `survey/survey.tex` when needed. Run `python3 scripts/validate.py`, compile the manuscript, and inspect the rendered pages. Update the snapshot date only after the stated source checks have actually been performed.

## Report a correction

Identify the exact claim, the source section or equation supporting the correction, and the affected records. Useful corrections include confused probability ratios, mismatched numerical configurations, over-generalized stability claims, and incorrect attribution of adopted methods.

## Suggest a collaboration

We welcome ideas on predictive mismatch diagnostics, numerical and learning method composition, stateful rollout semantics, and clearer synthesis of existing evidence. Describe the question you would like to explore and link any relevant public work. Opening a discussion does not add authorship or endorsement; those are agreed with the people involved.

## Keep evidence comparable

Do not infer a global ranking from different model/hardware/budget settings. Record a reported speedup with its baseline and timing scope. Treat an untested method combination as a hypothesis. Do not claim an exhaustive search unless a corresponding search protocol and log are provided.

## Rights and attribution

Contribute material you may share under the repository license. Link to third-party papers instead of copying their PDFs. Preserve the supplied template's CC BY-SA attribution. Do not add an author's name, affiliation, endorsement, or publication status without verified authorization or a primary source.
