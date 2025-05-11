import qrcode as qr
from PIL import Image  # Python Imaging Library
qr = qr.QRCode(version=1, error_correction=qr.constants.ERROR_CORRECT_H,
               box_size=10,border=20)
qr.add_data("https://www.google.com")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("Google.png")


# import PIL
# # print(dir(Image))
# print(PIL.__name__)
