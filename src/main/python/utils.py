from PIL import Image
import pytesseract

def image_to_string(image_path):
    text=pytesseract.image_to_string(Image.open(image_path), lang='chi_sim')
    return text