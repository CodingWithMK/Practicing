import segno
import qrcode
from urllib.request import urlopen

def make_qrcode(url_data):
    qr_code = qrcode.make("https://www.tiktok.com/@codenology")
    qr_code.save("YouTubeQR.png")


make_qrcode()

