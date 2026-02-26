import openai

def ai_math_cleanup(text):
    prompt = f"""
Convert the following OCR math text into clean LaTeX format.
Fix brackets, subscripts, math symbols, and set notation.

{text}
"""
    # call API