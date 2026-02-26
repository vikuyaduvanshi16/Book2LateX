import re


def escape_text(text: str) -> str:
    replacements = {
        "&": r"\&",
        "%": r"\%",
        "#": r"\#",
        "_": r"\_",
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text


def clean_ocr(line: str) -> str:
    # line = line.replace(" E ", r" \in ")
    # line = line.replace(" U ", r" \cup ")
    # line = line.replace(" n ", r" \cap ")
    return line


def parse_text(text: str) -> str:
    lines = text.split("\n")
    output = []

    for line in lines:
        line = line.strip()

        if not line:
            output.append("")
            continue

        line = clean_ocr(line)

        # Chapter detection
        if line.lower().startswith("chapter"):
            output.append(f"\\chapter{{{escape_text(line)}}}")
            continue

        # Section detection (1.1 Title)
        section_match = re.match(r"^(\d+\.\d+)\s+(.*)", line)
        if section_match:
            number, title = section_match.groups()
            output.append(f"\\section{{{escape_text(title)}}}")
            continue

        # Example detection
        if line.lower().startswith("example"):
            output.append(f"\\begin{{example}}\n{escape_text(line)}\n\\end{{example}}")
            continue

        # Normal text only (NO AUTO MATH)
        output.append(escape_text(line))

    return "\n".join(output)