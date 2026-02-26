import re


def remove_page_markers(text: str) -> str:
    text = re.sub(r"<PARSED TEXT FOR PAGE:.*?>", "", text)
    return text


def remove_page_numbers(text: str) -> str:
    # Remove isolated page numbers
    text = re.sub(r"\n\d+\s*\n", "\n", text)
    return text


def fix_ligatures(text: str) -> str:
    replacements = {
        "": "fi",
        "": "ff",
        "": "fl",
        "": "ffi",
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text


def fix_hyphenation(text: str) -> str:
    # Remove hyphen + newline (word break)
    text = re.sub(r"-\n", "", text)
    return text


def remove_running_headers(text: str) -> str:
    # Remove patterns like "CI Discrete Mathematics CI"
    text = re.sub(r"CI Discrete Mathematics CI", "", text)
    return text


def normalize_whitespace(text: str) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text


def preprocess_ocr(text: str) -> str:
    text = remove_page_markers(text)
    text = fix_ligatures(text)
    text = fix_hyphenation(text)
    text = remove_running_headers(text)
    text = remove_page_numbers(text)
    text = normalize_whitespace(text)
    return text