#!/usr/bin/env python3
"""Generate reader views and the repository status badge from canonical records."""
import argparse
import json
import re
from pathlib import Path
from build_comparisons import comparison_markdown

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- BEGIN GENERATED CATALOG -->'
END = '<!-- END GENERATED CATALOG -->'

def cell(value):
    return str(value).replace('|', '&#124;').replace('\n', ' ')

def source(row):
    return row.get('reviewed_source_url') or row['publication_url']

def title_link(row):
    title = cell(row['title']).replace('--', '–')
    return f"[{title}]({source(row)})"

def author_name(value):
    if ', ' in value:
        family, given = value.split(', ', 1)
        return given + ' ' + family
    return value

def generate():
    rows = json.loads((ROOT / 'data/papers.json').read_text())
    evidence = json.loads((ROOT / 'data/evidence.json').read_text())
    by_key = {r['key']: r for r in rows}
    catalog = []
    for role, title in [('core', 'Core methods and systems'),
                        ('support', 'Supporting formulation, theory, and general TIM studies'),
                        ('boundary', 'Exploration boundary')]:
        group = sorted((r for r in rows if r['role'] == role), key=lambda r: r['first_publication'])
        catalog += [f'### {title}', '', '| First public | Paper | Focus | Class / discussion |',
                    '|---|---|---|---|']
        for r in group:
            catalog.append(f"| {r['first_publication']} | **{cell(r['name'])}**<br>{title_link(r)} | "
                           f"{cell(r['catalog_summary'])} | {cell(r['categories'])} · {r['primary_section']} |")
        catalog += ['']
    catalog += ['Roles describe relevance to the survey, rather than evidence quality. '
                'Primary and secondary discussion locations are navigation fields; a work can introduce several coequal components.', '']
    readme = (ROOT / 'README.md').read_text()
    assert readme.count(START) == readme.count(END) == 1
    before, rest = readme.split(START)
    _, after = rest.split(END)
    readme = before + START + '\n\n' + '\n'.join(catalog) + '\n' + END + after

    full = ['# Reviewed paper catalog', '',
            'Full titles, source versions, numerical regimes, and discussion locations for the surveyed contributions.', '',
            'Entries distinguish contribution roles, numerical regimes, and tested settings.', '']
    full += ['## Browse by intervention', '',
             '[Chronological records](#chronological-records) · [Evidence synthesis](EVIDENCE.md) · [Classification rules](TAXONOMY.md)', '',
             'A work can appear in several component classes. Supporting studies are labeled explicitly; diagnostics and the exploration boundary remain in the chronological records.', '']
    for code, heading, description in [
            ('A1', 'Alignment (A1)', 'Shared learner–sampler computation.'),
            ('A2', 'Fidelity (A2)', 'Quantization error and visible parameter updates.'),
            ('B1', 'Estimation (B1)', 'Target expectations and gradient correction.'),
            ('B2', 'Update control (B2)', 'The influence of samples on policy updates.'),
            ('S', 'Scheduling (S)', 'Cross-family optimization scheduling; direct low-bit validation remains limited.')]:
        selected = [r for r in rows if re.search(r'\b' + code + r'\b', r['categories'])]
        links = [f"[{r['name']}](#paper-{r['key']})" + (' (support)' if r['role'] == 'support' else '')
                 for r in sorted(selected, key=lambda r: r['first_publication'])]
        full += [f'### {heading}', '', description, '', ' · '.join(links), '']
    full += ['## Chronological records', '']
    for r in sorted(rows, key=lambda r: r['first_publication']):
        full += [f'<a id="paper-{r["key"]}"></a>', '', f"### {r['name']}", '', f"**{title_link(r)}**", '',
                 'Authors: ' + '; '.join(author_name(x) for x in r['authors']) + '.', '',
                 f"First public: {r['first_publication']} · Source version: [{r['reviewed_version']}]({source(r)})", '',
                 f"- Numerical regime: {r['regime']}",
                 f"- Contribution role: {r['role']}; evidence domain: {r['evidence_domain']}",
                 f"- Components: {r['categories']}",
                 f"- Main discussion: {r['primary_section']}; additional locations: {r['secondary_sections'] or 'none listed'}",
                 f"- Scope: {r['note']}", '']
        if r['arxiv_url']:
            full += [f"[arXiv record]({r['arxiv_url']}) · [Publication/source]({r['publication_url']})", '']

    detail = ['# Source-linked qualitative evidence', '',
              'Published findings from the nineteen core studies, with their numerical regimes and primary-source locations.', '',
              'Read each outcome under the stated configuration and evaluation rule. Findings from different settings are not pooled.', '',
              '| Study / reviewed regime | Source observation | Interpretive limit | Primary source / location |',
              '|---|---|---|---|']
    for e in evidence['observations']:
        r = by_key[e['key']]
        detail.append(f"| **{cell(r['name'])}**<br>{title_link(r)}<br>{cell(r['regime'])} | {cell(e['observation'])} | "
                      f"{cell(e['limit'])} | [Source]({e['url']})<br>{cell(e['locator'])} |")
    status = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 570 30" role="img" aria-labelledby="title desc">
<title id="title">Survey · Curated reading · CC BY-SA 4.0</title>
<desc id="desc">Survey, curated reading resources, and repository license.</desc>
<g font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Arial, sans-serif" font-size="11.5" font-weight="600" text-anchor="middle">
<rect x="1" y="1" width="182" height="28" rx="6" fill="#EDF3F9" stroke="#CCD8E2"/><text x="92" y="19" fill="#2B608F">RESEARCH SURVEY</text>
<rect x="194" y="1" width="182" height="28" rx="6" fill="#EDF6F2" stroke="#CCD8E2"/><text x="285" y="19" fill="#1A7B70">CURATED READING</text>
<rect x="387" y="1" width="182" height="28" rx="6" fill="#F2F4F7" stroke="#CCD8E2"/><text x="478" y="19" fill="#526477">CC BY-SA 4.0</text>
</g></svg>
'''
    return {ROOT / 'README.md': readme,
            ROOT / 'docs/CATALOG.md': '\n'.join(full),
            ROOT / 'docs/EVIDENCE.md': '\n'.join(detail),
            ROOT / 'figures/status.svg': status,
            ROOT / 'docs/COMPARISONS.md': comparison_markdown(ROOT)}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if generated views differ from the records.')
    args = parser.parse_args()
    outputs = generate()
    stale = [str(p.relative_to(ROOT)) for p, text in outputs.items()
             if not p.exists() or p.read_text() != text]
    if args.check:
        if stale:
            raise SystemExit('Stale generated views: ' + ', '.join(stale))
        print('PASS: README catalog and review tables match canonical JSON.')
    else:
        for p, text in outputs.items():
            p.parent.mkdir(exist_ok=True)
            p.write_text(text)
        print('Generated README catalog, docs/CATALOG.md and docs/EVIDENCE.md.')

if __name__ == '__main__':
    main()
