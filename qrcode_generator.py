import pyqrcode as qr
import png
from pyqrcode import QRCode

def qrcode_generator():
    # enter your link
    link = input('Enter your link : ')
    # creating qr 
    url = qr.create(link)
    # saving the image
    url.png('myqr.png', scale=6)
    print('QR code is created!')

if __name__ == '__main__':
    qrcode_generator()