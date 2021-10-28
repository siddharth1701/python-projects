# pip install pyqrcode
# pip install pypng

import pyqrcode
import png

print("Welcome to QR Code Generator")

msg = input("Type your secret message: ")

code = pyqrcode.create(msg)

code.png("QRCode.png", scale=5)

print("QR Code Generated Sucessfully!")