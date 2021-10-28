# !sudo apt install tesseract-ocr
# !pip install pytesseract

import pytesseract
import shutil
import os
import random
try:
 from PIL import Image
except ImportError:
 import Image


######## Method : 1 ########
image_path_in_colab="10.jpeg"
extractedInformation = pytesseract.image_to_string(Image.open(image_path_in_colab))
print(extractedInformation)


######## Method : 2 ########
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

text = ocr_core('6.png')
t = text.strip()
t = t.replace("\n", " ")
print(t)

######## Method : 3 ########
print(pytesseract.image_to_string(Image.open('1.jpeg')))

######## Method : 4 Using input directory########
# !sudo apt install tesseract-ocr
# !pip install pytesseract

import pytesseract
import os
try:
    from PIL import Image
except ImportError:
    import Image

indir = r'input/'
for root, dirs, filenames in os.walk(indir):
    for filename in filenames:
        print("")
        print('################################## ' + filename + ' ##################################')
        print("")
        im = Image.open(indir + filename)
        text = pytesseract.image_to_string(im, lang='eng')
        print(text)

######## Method : 5 with input directory using try except ########

from PIL import Image
import pytesseract
import os
import pandas as pd

# Path is given for for 64 bit installer
# pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

f = []
t = []
input_dir = r'input/'

for root, dirs, filenames in os.walk(input_dir):
    for filename in filenames:
        try:
            print(filename)
            f.append(filename)
            img = Image.open(input_dir+ filename)
            text = pytesseract.image_to_string(img, lang = 'eng')
            t.append(text)
            print(text)
            print('-='*20)
        except:
            continue


#df = pd.DataFrame(list(zip(f, t)),columns=['file_Name','Text'])