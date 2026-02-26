def wrap_latex(content: str, title="Discrete Mathematics", author="Vikash Yadav"):
    return rf"""
\documentclass[11pt]{{amsbook}}

% ---------- Encoding ----------
\usepackage[utf8]{{inputenc}}
\usepackage[T1]{{fontenc}}

% ---------- Math Packages ----------
\usepackage{{amsmath, amssymb, amsthm}}
\usepackage{{mathtools}}
\usepackage{{bm}}

% ---------- Layout ----------
\usepackage{{geometry}}
\geometry{{margin=1in}}

\usepackage{{setspace}}
\onehalfspacing

\usepackage{{graphicx}}
\usepackage{{float}}

% ---------- Hyperref (load last) ----------
\usepackage[colorlinks=true,
            linkcolor=blue,
            citecolor=blue,
            urlcolor=blue]{{hyperref}}

% ---------- Theorem Environments ----------

\theoremstyle{{definition}}
\newtheorem{{definition}}{{Definition}}[chapter]
\newtheorem{{example}}{{Example}}[chapter]

\theoremstyle{{plain}}
\newtheorem{{theorem}}{{Theorem}}[chapter]
\newtheorem{{lemma}}{{Lemma}}[chapter]
\newtheorem{{corollary}}{{Corollary}}[chapter]

\theoremstyle{{remark}}
\newtheorem*{{remark}}{{Remark}}

% ---------- Custom Commands (Optional Helpers) ----------
\newcommand{{\N}}{{\mathbb{{N}}}}
\newcommand{{\Z}}{{\mathbb{{Z}}}}
\newcommand{{\Q}}{{\mathbb{{Q}}}}
\newcommand{{\R}}{{\mathbb{{R}}}}

% ------------------------------------------

\title{{{title}}}
\author{{{author}}}

\begin{{document}}

\frontmatter
\maketitle
\tableofcontents

\mainmatter

{content}

\end{{document}}
"""