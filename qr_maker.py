#  QR code generator
import pyqrcode
from PIL import Image
import png


def qr_code(link="https://engineering.catholic.edu/eecs/index.html", logo = False, size = 8):
    """
    paras:
        hyper_link: string type. your url for qr code. default is the CUA EECS index page
        logo_name: user's logo image name (uploaded). It can be png or jpg format. Default is the None.
        size: the QR size: int.

    return:
        image file name (saved in the local disk, .png format.): String type
    """
    # if no logo uploaded
    if logo == False:
        # (1) QR CODE generation for a given link
        qr_code = pyqrcode.QRCode(link, error = 'H')
        f_name = './images/QR.png'
        with open(f_name, 'wb') as f:
            qr_code.png(f, scale=size)
        return f_name

    # if logo file is given
    else:
        # (2.1) QR code first
        qr = Image.open('./images/QR.png')
        width, height = qr.size
        qr = qr.convert("RGBA")   # keep the logo's colors


        # (2.2) Open the logo image
        logo = Image.open("./images/logo.png")

        #how big the logo we want to put in the qr code (20% by 20%)
        logo_w, logo_h =  width/5, height/5

        # Calculate xmin, ymin, xmax, ymax to put the logo
        xmin = int((width / 2) - (logo_w / 2))
        xmax = int((width / 2) + (logo_w / 2))
        ymin = int((height/ 2) - (logo_h / 2))
        ymax = int((height/ 2) + (logo_h / 2))

        # resize the logo as calculated
        logo = logo.resize((xmax - xmin, ymax - ymin))

        # (2.3) put the logo in the qr code
        qr.paste(logo, (xmin, ymin, xmax, ymax))

        # (2.4) save to disk
        f_name = './images/QR-logo.png'
        qr.save(f_name)
        return f_name