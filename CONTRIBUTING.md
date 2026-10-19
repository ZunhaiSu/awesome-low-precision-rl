# Contributing

## Propose a paper

Include a primary-source URL and explain the connection to low-precision rollout or training–rollout mismatch. State whether the contribution is a method, a system, diagnostic evidence, or a boundary case. Identify components rather than assigning a whole paper to one exclusive category.

Add or update a record in `data/papers.json`. Preserve the existing schema, record the reviewed version, and keep conference and preprint versions together. Supply authors, title, first-publication date, primary discussion location, and scope note. Distinguish direct low-precision experiments from general TIM evidence.

Update `README.md`, `references.bib`, and the inline bibliography/corpus table in `survey/survey.tex` when needed. Run `python3 scripts/validate.py`, compile the manuscript, and inspect the rendered pages. Update the snapshot date only after the stated source checks have actually been performed.

## Report a correction

Identify the exact claim, the source section or equation supporting the correction, and the affected records. Useful corrections include confused probability ratios, mismatched numerical configurations, over-generalized stability claims, and incorrect attribution of adopted methods.

## Keep evidence comparable

Do not infer a global ranking from different model/hardware/budget settings. Record a reported speedup with its baseline and timing scope. Treat an untested method combination as a hypothesis. Do not claim an exhaustive search unless a corresponding search protocol and log are provided.

## Rights and attribution

Contribute material you may share under the repository license. Link to third-party papers instead of copying their PDFs. Preserve the supplied template's CC BY-SA attribution. Do not add an author's name, affiliation, endorsement, or publication status without verified authorization or a primary source.
