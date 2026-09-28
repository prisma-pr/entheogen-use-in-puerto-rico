"""Reproducible word count check for v7_draft.tex against JPD's 4,000-word
Introduction-Methods-Results-Discussion cap and 200-word unstructured-abstract cap.
Run: PYTHONIOENCODING=utf-8 python manuscript/wordcount.py
"""
import re

text = open('drafts/v7_draft.tex', encoding='utf-8').read()


def strip_latex(s):
    s = re.sub(r'(?<!\\)%.*', '', s)  # comments
    s = re.sub(r'\\citep\{[^}]*\}', 'CITE', s)
    s = re.sub(r'\\cite[a-zA-Z]*\{[^}]*\}', 'CITE', s)
    s = re.sub(r'\\label\{[^}]*\}', '', s)
    s = re.sub(r'\\ref\{[^}]*\}', 'REF', s)
    s = re.sub(r'\\emph\{([^}]*)\}', r'\1', s)
    s = re.sub(r'\\textbf\{([^}]*)\}', r'\1', s)
    s = re.sub(r"\\'\{?([a-zA-Z])\}?", r'\1', s)
    s = re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?(\{[^}]*\})?', ' ', s)
    s = re.sub(r'[{}]', ' ', s)
    return s


abs_start = text.index(r'\begin{abstract}')
abs_end = text.index(r'\end{abstract}')
abstract_raw = text[abs_start + len(r'\begin{abstract}'):abs_end]
abstract_words = len(strip_latex(abstract_raw).split())
print("Abstract word count:", abstract_words, "(cap: 200, unstructured required)")

intro_start = text.index(r'\section{Introduction}')
disc_end = text.index(r'\section*{Author contributions}')
body_words = len(strip_latex(text[intro_start:disc_end]).split())
print("Introduction-through-Discussion word count:", body_words, "(cap: 4,000)")

sections = [r'\section{Introduction}', r'\section{Methods}', r'\section{Results}', r'\section{Discussion}']
idxs = [text.index(s) for s in sections] + [disc_end]
names = ['Introduction', 'Methods', 'Results', 'Discussion']
for i in range(4):
    seg = text[idxs[i]:idxs[i + 1]]
    w = len(strip_latex(seg).split())
    print(f"  {names[i]}: {w} words")
