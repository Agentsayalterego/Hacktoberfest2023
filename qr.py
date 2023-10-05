import qrcode

img = qrcode.make("https://github.com/sayantancodex")
img.save("h.png")
