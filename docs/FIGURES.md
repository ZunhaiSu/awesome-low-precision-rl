# Original figures

The manuscript contains three original vector figures. None is a cross-paper numerical leaderboard.

1. **Component taxonomy (Figure 1).** Numerical and learning interventions are placed in separate columns, with configuration axes shown in a dashed box. Paper names identify operative components; the same study may contribute to both columns.
2. **Feedback loop (Figure 2).** The existing diagram connects sampler, responses and learning signals, learner, and parameter synchronization. It locates interventions in the training loop.
3. **Sign-dependent clipping (Figure 3).** Curves follow the standard clipped surrogate with epsilon 0.2 and advantage +1 or -1. Red regions are the flat clipping branches. The negative-advantage marker at ratio 0.7 illustrates the zero-gradient example in Section 3.2. These are analytical curves, not measured outcomes.

The taxonomy and clipping diagrams are embedded in `survey/survey.tex` and exported to `figures/taxonomy.svg` and `figures/clipping.svg` for the README. They remain vectors when enlarged. The full paper builds without loading these external assets.

To regenerate the assets, install Tectonic and Poppler, then run:

```sh
python3 scripts/export_figures.py
```

The exporter accepts `--tectonic` and `--pdftocairo` when those programs are not on PATH. It uses temporary standalone builds and retains only the SVG outputs.
