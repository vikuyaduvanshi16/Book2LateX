import argparse
import logging
import os
import sys

from scripts.parser import parse_text
from scripts.template import wrap_latex
from scripts.preprocess import preprocess_ocr
from scripts.ocr_engine import extract_text_from_folder
from scripts.ai_cleanup import ai_math_cleanup


# ----------------------------------------
# Logging
# ----------------------------------------

def setup_logger(verbose: bool):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(levelname)s: %(message)s"
    )


# ----------------------------------------
# Argument Parsing
# ----------------------------------------

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Convert OCR text into structured LaTeX book format"
    )

    parser.add_argument(
        "input_file",
        help="Path to input OCR text file"
    )

    parser.add_argument(
        "-o", "--output",
        help="Output LaTeX file path"
    )

    parser.add_argument(
        "--title",
        default="Discrete Mathematics",
        help="Book title"
    )

    parser.add_argument(
        "--author",
        default="Vikash Yadav",
        help="Author name"
    )

    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite output file if it exists"
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )

    return parser.parse_args()


# ----------------------------------------
# Path Handling
# ----------------------------------------

def determine_output_path(input_path, output_arg):
    if output_arg:
        return output_arg

    filename = os.path.splitext(os.path.basename(input_path))[0]
    return os.path.join("output", f"{filename}.tex")


# ----------------------------------------
# File IO
# ----------------------------------------

def read_input(path):
    if not os.path.exists(path):
        logging.error(f"Input file not found: {path}")
        sys.exit(1)

    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        logging.error(f"Failed to read file: {e}")
        sys.exit(1)


def write_output(path, content, overwrite):
    if os.path.exists(path) and not overwrite:
        logging.error(f"File exists: {path} (use --overwrite to replace)")
        sys.exit(1)

    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)

    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        logging.error(f"Failed to write file: {e}")
        sys.exit(1)


# ----------------------------------------
# Main Pipeline
# ----------------------------------------

def main():
    args = parse_arguments()
    setup_logger(args.verbose)

    logging.debug("Arguments parsed successfully")

    # If input is folder → run OCR
    if os.path.isdir(args.input_file):
        logging.info("Running OCR on image folder...")
        text = extract_text_from_folder(args.input_file)
    else:
        logging.info("Reading OCR text...")
        text = read_input(args.input_file)

    logging.info("Preprocessing OCR text...")
    text = preprocess_ocr(text)

    logging.info("Running AI math cleanup...")
    text = ai_math_cleanup(text)

    logging.info("Parsing structure...")
    parsed_content = parse_text(text)

    logging.info("Applying LaTeX template...")
    latex_output = wrap_latex(
        parsed_content,
        title=args.title,
        author=args.author
    )

    output_path = determine_output_path(args.input_file, args.output)
    logging.debug(f"Output path resolved → {output_path}")

    write_output(output_path, latex_output, args.overwrite)

    logging.info(f"✔ Conversion successful → {output_path}")

if __name__ == "__main__":
    main()