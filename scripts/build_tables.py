#!/usr/bin/env python3
"""Generate the README catalog and review tables from the canonical JSON records."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- BEGIN GENERATED CATALOG -->'
END = '<!-- END GENERATED CATALOG -->'

def cell(value):
    return str(value).replace('|', '&#124;').replace('\n', ' ')

def source(row):
    return row.get('reviewed_source_url') or row['publication_url']

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
                        ('support', 'Supporting formulation and general TIM studies'),
                        ('boundary', 'Exploration boundary')]:
        group = sorted((r for r in rows if r['role'] == role), key=lambda r: r['first_publication'])
        catalog += [f'### {title}', '', '| First public | Study | Focus | Class / discussion |',
                    '|---|---|---|---|']
        for r in group:
            catalog.append(f"| {r['first_publication']} | **[{cell(r['name'])}]({source(r)})** | "
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
            'Generated from `data/papers.json`. Dates and versions identify the reviewed snapshot, not a claim that a source has never changed.', '',
            'The catalog separates contribution role, evidence domain, and numerical regime. No independent reproduction was performed for this survey; this status makes no claim about reproductions elsewhere. Code availability, seed counts, and experiment-level model/task coverage are not systematically audited here.', '']
    for r in sorted(rows, key=lambda r: r['first_publication']):
        full += [f"## {r['name']}", '', f"**{r['title']}**", '',
                 'Authors: ' + '; '.join(author_name(x) for x in r['authors']) + '.', '',
                 f"First public: {r['first_publication']} · Reviewed record: [{r['reviewed_version']}]({source(r)}) · Source snapshot checked: {r['checked_date']}", '',
                 f"- Numerical regime: {r['regime']}",
                 f"- Contribution role: {r['role']}; evidence domain: {r['evidence_domain']}",
                 f"- Components: {r['categories']}",
                 f"- Main discussion: {r['primary_section']}; additional locations: {r['secondary_sections'] or 'none listed'}",
                 f"- Scope: {r['note']}", '']
        if r['arxiv_url']:
            full += [f"[arXiv record]({r['arxiv_url']}) · [Publication/source]({r['publication_url']})", '']

    detail = ['# Source-linked qualitative evidence', '',
              'Generated from `data/evidence.json` and `data/papers.json`. These records cover all thirteen core studies. Supporting and boundary studies remain in the [complete catalog](CATALOG.md); their role does not imply an absence of low-precision experiments.', '',
              'Observations retain their source setting and interpretive limit. They are not quality grades, pooled estimates, or independent replications. A source section is a locator within the linked reviewed source; a survey discussion number is a different field.', '',
              '| Study / reviewed regime | Source observation | Interpretive limit | Primary source / location |',
              '|---|---|---|---|']
    for e in evidence['observations']:
        r = by_key[e['key']]
        detail.append(f"| **{cell(r['name'])}**<br>{cell(r['regime'])} | {cell(e['observation'])} | "
                      f"{cell(e['limit'])} | [Source]({e['url']})<br>{cell(e['locator'])} |")
    detail += ['', 'Statistical reporting and external replication have not been exhaustively extracted. Missing metadata is unassessed, rather than a negative experimental finding.', '']
    return {ROOT / 'README.md': readme,
            ROOT / 'docs/CATALOG.md': '\n'.join(full),
            ROOT / 'docs/EVIDENCE.md': '\n'.join(detail)}

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
