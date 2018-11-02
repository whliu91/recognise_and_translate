from PIL import Image
import pytesseract
from translate import Translator


def image_to_string(image_path):
    text=pytesseract.image_to_string(Image.open(image_path), lang='chi_sim')
    return text

def eng_to_zhcn(eng_str):
    translator = Translator(to_lang="en", from_lang="zh")
    zhcn_str = translator.translate(eng_str)
    return zhcn_str