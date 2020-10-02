# 生成最普通的二维码
import qrcode

image = qrcode.make("https://blog.csdn.net/qq_43827595")
image.save("qr.png")