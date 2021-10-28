# pip install pyzbar

from pyzbar.pyzbar import decode
from PIL import Image

print("Welcome to QR Code Reader")

# Opening the image
img = Image.open("QRCode.png")

# Decoding the image
d = decode(img)

# Printing the result
print(d[0].data.decode())