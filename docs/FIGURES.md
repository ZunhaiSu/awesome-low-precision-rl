# Original figures

The manuscript contains four original vector figures. The overview, taxonomy, and clipping diagrams are also exported as SVGs for the README. All four remain embedded in the standalone LaTeX source.

1. **Survey overview (Figure 1).** The first-page graphical overview connects quantized rollout, collected experience, learner updates, and synchronization. Blue and teal panels locate numerical and learning interventions; the lower band connects fidelity, stability, quality, and training cost. This is a conceptual diagram, with no experimental performance curves.
2. **Component taxonomy (Figure 2).** Numerical and learning interventions appear in separate columns, with configuration axes in a dashed box. Paper names identify components; one study can contribute to both columns.
3. **Feedback loop (Figure 3).** Sampler, responses and learning signals, learner, and parameter synchronization locate interventions in the technical formulation.
4. **Sign-dependent clipping (Figure 4).** Analytical curves follow the standard clipped surrogate with epsilon 0.2 and advantage +1 or -1. Red regions are flat clipping branches; the negative-advantage marker at ratio 0.7 illustrates Section 3.2.

The opening sequence is title/abstract and overview on page one, complete contents on page two, and the introduction from page three. The body taxonomy retains the paper-level detail omitted from the compact overview.

To regenerate the three SVG assets with Tectonic and Poppler, run:

```sh
python3 scripts/export_figures.py
```

The exporter accepts `--tectonic` and `--pdftocairo` when those programs are not on PATH. It uses temporary standalone builds and retains only the SVG outputs. The full paper does not load the exported files.
