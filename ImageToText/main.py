from PIL import Image
from pytesseract import pytesseract
# Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define path to image
photo = 'test.png'
path_to_image = f"C:/VisualStudioCode/python_folder/picToText/images/{photo}"

# Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

# Open image with PIL
img = Image.open(path_to_image)

text = pytesseract.image_to_string(img)
print(text)
