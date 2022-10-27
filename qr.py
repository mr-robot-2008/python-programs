import pyqrcode
import png
link = "https://www.instagram.com/the.clever.programmer/"
qr_code = pyqrcode.create(link)
qr_code.png("instagram.png", scale=5)
