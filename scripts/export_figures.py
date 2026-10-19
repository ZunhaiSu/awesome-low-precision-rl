#!/usr/bin/env python3
"""Export embedded TikZ diagrams using the manuscript palette as portable SVG assets.

Requires Tectonic and Poppler's pdftocairo. The manuscript stays self-contained;
these assets are for the companion README, not inputs to the paper.
"""
import argparse,re,subprocess,tempfile
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--tectonic',default='tectonic')
parser.add_argument('--pdftocairo',default='pdftocairo')
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
source=(root/'survey/survey.tex').read_text()
output=root/'figures';output.mkdir(exist_ok=True)
preamble=r'''\documentclass[11pt,tikz,border=6pt]{standalone}
\usepackage[T1]{fontenc}
\usepackage[type1]{XCharter}
\usepackage{amsmath,amssymb}
\usepackage{xcolor}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning,fit}
''' + re.search(r'% BEGIN SURVEY PALETTE\n(.*?)\n% END SURVEY PALETTE',source,re.S).group(1) + r'''
\begin{document}
'''
for name in re.findall(r'% BEGIN FIGURE ([a-z_]+)',source):
 match=re.search(r'% BEGIN FIGURE '+name+r'\n(.*?)\n% END FIGURE '+name,source,re.S)
 if not match:raise ValueError('Missing embedded diagram: '+name)
 with tempfile.TemporaryDirectory(prefix='survey-figure-') as directory:
  work=Path(directory);tex=work/(name+'.tex')
  tex.write_text(preamble+match.group(1)+'\n\\end{document}\n')
  result=subprocess.run([args.tectonic,str(tex)],cwd=work,text=True,capture_output=True)
  if result.returncode:raise RuntimeError(result.stdout+result.stderr)
  subprocess.run([args.pdftocairo,'-svg',str(work/(name+'.pdf')),str(output/(name+'.svg'))],check=True)
 print('Exported',name+'.svg')
