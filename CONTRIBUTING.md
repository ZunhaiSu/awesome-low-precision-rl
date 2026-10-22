# Contributing

This living survey grows through discussions as well as paper suggestions. Use [GitHub Issues](https://github.com/ZunhaiSu/awesome-low-precision-rl/issues) for missing work, technical corrections, or a research collaboration proposal. A short description of the idea and its connection to the survey is enough to start a conversation.

## Propose a paper

Include a primary-source URL and explain the connection to low-precision rollout or training–rollout mismatch. State whether the contribution is a method, a system, diagnostic evidence, or a boundary case. Identify components rather than assigning a whole paper to one exclusive category.

Add or update a record in `data/papers.json`. Preserve the existing schema, record the reviewed version, and keep conference and preprint versions together. Supply authors, title, first-publication date, primary discussion location, and scope note. Distinguish direct low-precision experiments from general TIM evidence.

For core studies, add a source-located observation and its interpretive limit to `data/evidence.json`. Supply a numerical regime, evidence domain, replication status, concise catalog summary, and reviewed source URL in `data/papers.json`. A pinned version must come from an identified source record. Do not infer code availability, seed counts, or replication elsewhere from an unfilled field.

Run `python3 scripts/build_tables.py` to refresh the README catalog and the complete catalog/evidence views, then run `python3 scripts/validate.py`. Preserve manual README content outside the generated markers. Update the literature snapshot only after the stated source checks have actually been performed. [Classification guidance](docs/TAXONOMY.md) distinguishes relevance, method components, and evidence domains; none is an experimental-quality grade.

## Report a correction

Identify the exact claim, the source section or equation supporting the correction, and the affected records. Useful corrections include confused probability ratios, mismatched numerical configurations, over-generalized stability claims, and incorrect attribution of adopted methods.

## Suggest a collaboration

We welcome ideas on predictive mismatch diagnostics, numerical and learning method composition, stateful rollout semantics, and clearer synthesis of existing evidence. Describe the question you would like to explore and link any relevant public work.

## Keep evidence comparable

Do not infer a global ranking from different model/hardware/budget settings. Record a reported speedup with its baseline and timing scope. Treat an untested method combination as a hypothesis. Do not claim an exhaustive search unless a corresponding search protocol and log are provided.

## Rights and attribution

Contribute original material you may share under the repository license. Third-party papers retain their own licenses. Mirror a paper only when its exact source version explicitly permits redistribution: preserve its original bytes and notices, provide full attribution and the license URL in `papers/NOTICES.md`, and record source and hash evidence in `papers/manifest.json`. Otherwise add a numbered entry linking to the official PDF. Preserve the supplied template's CC BY-SA attribution. Do not add an author's name, affiliation, endorsement, or publication status without verified authorization or a primary source.

## Keep the public PDF current

The repository-root `Survey.pdf` is the only published survey manuscript file. Licensed third-party reading copies belong under `papers/` and are checked against its manifest. Manuscript sources are maintained separately in Overleaf and must not be uploaded to this repository. Do not add LaTeX sources, class/style files, manuscript build scripts, or a second PDF copy in a source directory.

After a requested manuscript update, compile and check the source in the authoring project, inspect the affected PDF pages, then publish the successful PDF as `Survey.pdf`. Refresh changed catalog records and SVG figures as needed. Preserve unrelated GitHub edits. A failed compilation must not replace the last successful public PDF.
