import pytesseract as pyt
from PIL import Image


def ocr(file):
    text = pyt.image_to_string(Image.open(file))
    return text
