#!/usr/bin/env python3
"""Render selected, source-bound execution and comparison records."""
import json


def comparison_markdown(root):
    records = json.loads((root / 'data/comparisons.json').read_text())
    papers = {p['key']: p for p in json.loads((root / 'data/papers.json').read_text())}
    def cell(value):
        return str(value).replace('|', '&#124;').replace('\n', ' ')
    def paper(key):
        p = papers[key]
        return f"**{p['name']}**<br>[{p['title']}]({p['reviewed_source_url']})"
    lines = [
        '# Comparing mechanisms, configurations and evidence', '',
        'A method class describes what an intervention changes. Its experimental configuration describes where the source tested it. These selected records keep the two separate.', '',
        'Literature snapshot: **20 October 2026**. The cases below are source-reported observations, not independent reproductions or a cross-paper leaderboard.', '',
        '## Execution configurations', '',
        '| Study | Learner | Rollout | Collection and scope |',
        '|---|---|---|---|']
    for r in records['regimes']:
        lines.append(f"| {paper(r['key'])} | {cell(r['learner'])} | {cell(r['rollout'])} | {cell(r['collection'])}. {cell(r['boundary'])} [Source]({r['url']}), {cell(r['locator'])}. |")
    lines += ['', '## Direct comparison cases', '']
    for r in records['comparisons']:
        lines += [
            f"### {r['title']}", '',
            f"**Setting.** {r['setting']}", '',
            f"**Compared.** {r['compared']}", '',
            f"**Reported outcome.** {r['outcome']}", '',
            f"**Checkpoint and repetition rule.** {r['checkpoint_rule']}", '',
            f"**Interpretation.** {r['limit']}", '',
            f"[Primary source]({r['url']}) · {r['locator']}", '']
    lines += [
        '## Read the measurements together', '',
        '| Measurement | Interpretation |',
        '|---|---|',
        '| Policy entropy | Uncertainty of a specified next-token distribution; neither a quality score nor evidence that entropy regularization is active. |',
        '| Mean training reward | Scores of collected responses under a stated reward rule; distinct from group advantages and held-out quality. |',
        '| Mean absolute log-probability gap | Agreement on sampled tokens; averaging removes direction and local concentration. |',
        '| Held-out quality | Requires the evaluation precision, decoding and checkpoint rule. A common BF16 evaluator and a deployed low-precision evaluator answer different questions. |',
        '| Rollout and iteration time | Different timing scopes. Generation length, concurrency, synchronization and guidance can affect total cost. |',
        '', 'The mechanism and evidence tables support a focused narrative survey. A controlled benchmark and any proposed predictive metric require additional experiments; neither is claimed by these records.', '',
        '[Survey PDF](../Survey.pdf) · [Full catalog](CATALOG.md) · [Source observations](EVIDENCE.md) · [Classification](TAXONOMY.md)', '']
    return '\n'.join(lines)
