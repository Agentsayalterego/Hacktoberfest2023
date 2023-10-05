import qrcode

img = qrcode.make("https://github.com/sayantancodex")
#run this code to generate a qr
img.save("h.png")
