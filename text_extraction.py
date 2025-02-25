```python
import pdfplumber
from PIL import Image
import pytesseract

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_text_from_image(image_path):
    """Extract text from an image file."""
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text
