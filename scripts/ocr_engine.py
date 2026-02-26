import os
import pytesseract
from PIL import Image

# Set path if PATH not working
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_folder(folder):
    text = ""
    images = sorted(os.listdir(folder))

    for img_name in images:
        if img_name.lower().endswith((".png", ".jpg", ".jpeg")):
            img_path = os.path.join(folder, img_name)
            print(f"OCR: {img_name}")
            img = Image.open(img_path)
            page_text = pytesseract.image_to_string(img, config="--psm 6")
            text += page_text + "\n\n"

    return text