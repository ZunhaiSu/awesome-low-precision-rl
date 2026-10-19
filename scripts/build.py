#!/usr/bin/env python3
"""Build the standalone paper, refresh the public PDF, and validate the project."""
import argparse,re,shutil,subprocess,sys
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--tectonic',default='tectonic')
parser.add_argument('--pdftocairo',default='pdftocairo')
parser.add_argument('--figures',action='store_true')
a=parser.parse_args();root=Path(__file__).resolve().parents[1]
paths=[root/'survey/survey.pdf',root/'Survey.pdf']
previous={p:p.read_bytes() if p.exists() else None for p in paths}
try:
 subprocess.run([a.tectonic,'--keep-logs','survey.tex'],cwd=root/'survey',check=True)
 log=(root/'survey/survey.log').read_text(errors='replace')
 if re.search(r'Overfull|Undefined control sequence|LaTeX Error|undefined citations|undefined references',log,re.I):
  raise RuntimeError('Compilation diagnostics require review; see survey/survey.log')
 shutil.copy2(paths[0],paths[1])
 if a.figures:
  subprocess.run([sys.executable,str(root/'scripts/export_figures.py'),'--tectonic',a.tectonic,'--pdftocairo',a.pdftocairo],check=True)
 subprocess.run([sys.executable,str(root/'scripts/validate.py')],check=True)
except Exception:
 for path,data in previous.items():
  if data is not None:path.write_bytes(data)
 raise
print('Built and validated Survey.pdf')
