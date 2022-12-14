import qrcode

data = "Salman"

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)

qr.add_data(data)

qr.make(fit = True)

img = qr.make_image(fill_color = 'red', back_color = 'white')

img.save("...\qrcode.png") # idk if this works tbh my vscode stopped working

from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("...\qrcode.png")

result = decode(img)

print(result)
