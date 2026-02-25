def wrap_latex(content: str, title="Book", author="Author"):
    return rf"""
\documentclass[12pt]{{book}}

\usepackage{{amsmath, amssymb}}
\usepackage{{graphicx}}
\usepackage{{hyperref}}

\title{{{title}}}
\author{{{author}}}

\begin{{document}}

\maketitle
\tableofcontents

{content}

\end{{document}}
"""