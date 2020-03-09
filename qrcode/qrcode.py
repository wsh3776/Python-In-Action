# https://github.com/sylnsfar/qrcode#common-qr-code
from MyQR import myqr
import os

version, level, qr_name = myqr.run(
    # Just input a URL or a sentence, then get your QR-Code named 'qrcode.png' in the current directory.
    words="https://blog.csdn.net/qq_43827595",
    version=10,  # length:1-40
    level='H',
    picture="jienigui.gif",  # background jpg png bpm gif(less than 2MB)
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name=None,  # output name
    save_dir=os.getcwd()
)

# Output “line 16: mode: byte" means successful
