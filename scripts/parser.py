import re

def is_math(line):
    return bool(re.search(r"[=^+\-*/]", line))


def parse_text(text):
    lines = text.split("\n")
    output = []

    for line in lines:
        line = line.strip()

        # Chapter
        if line.lower().startswith("chapter"):
            output.append(f"\\chapter{{{line}}}")

        # Section
        elif line.lower().startswith("section"):
            title = line.replace("Section", "").strip()
            output.append(f"\\section{{{title}}}")

        # Subsection
        elif line.lower().startswith("subsection"):
            title = line.replace("Subsection", "").strip()
            output.append(f"\\subsection{{{title}}}")

        # Math detection
        elif is_math(line):
            output.append(f"${line}$")

        # Bold text
        else:
            line = line.replace("**", "\\textbf{", 1).replace("**", "}", 1)
            output.append(line)

    return "\n".join(output)


def convert_file(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    latex = parse_text(text)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(latex)


