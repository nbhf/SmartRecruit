import fitz  # PyMuPDF
from pdf2image import convert_from_path
import pytesseract

def extract_text(file_path):
    text = ""
    try:
        # Essai avec PyMuPDF (PDF texte)
        doc = fitz.open(file_path)
        for page in doc:
            text += page.get_text()
        if text.strip():  # Si du texte a été trouvé
            return text
    except:
        pass
    
    # Si PDF contient une image, OCR avec pytesseract
    images = convert_from_path(file_path)
    for image in images:
        text += pytesseract.image_to_string(image)
    
    return text
