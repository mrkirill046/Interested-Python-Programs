import pytesseract
from PIL import Image
from mtranslate import translate

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def recognize_text(image_path):
    extracted_text = pytesseract.image_to_string(Image.open(image_path), lang='eng')
    return extracted_text


def translate_text(text, target_language='ru'):
    translated_text = translate(text, target_language)
    return translated_text


if __name__ == "__main__":
    input_image_path = "image.jpg"
    e_text = recognize_text(input_image_path)
    t_text = translate_text(e_text)
    print(f"Переведенный текст:\n{t_text}")
