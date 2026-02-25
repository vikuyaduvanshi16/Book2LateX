import argparse
import logging
import os
import sys
from scripts.parser import parse_text
from scripts.template import wrap_latex


def setup_logger(verbose: bool):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(levelname)s: %(message)s"
    )


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Convert plain text book into LaTeX format"
    )

    parser.add_argument(
        "input_file",
        help="Path to input text file"
    )

    parser.add_argument(
        "-o", "--output",
        help="Output LaTeX file path"
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


def determine_output_path(input_path, output_arg):
    if output_arg:
        return output_arg

    filename = os.path.splitext(os.path.basename(input_path))[0]
    return f"output/{filename}.tex"


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


def main():
    args = parse_arguments()
    setup_logger(args.verbose)

    logging.debug("Arguments parsed successfully")

    text = read_input(args.input_file)

    logging.info("Converting text → LaTeX")

    parsed = parse_text(text)
    latex_output = wrap_latex(parsed)

    output_path = determine_output_path(args.input_file, args.output)
    logging.debug(f"Output path resolved → {output_path}")

    write_output(output_path, latex_output, args.overwrite)

    logging.info(f"✔ Conversion successful → {output_path}")


if __name__ == "__main__":
    main()