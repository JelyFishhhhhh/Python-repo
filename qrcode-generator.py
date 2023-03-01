from qrcode import QRCode
from qrcode.constants import ERROR_CORRECT_L
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from datetime import datetime

dt = datetime.now().strftime("%Y%m%d %H-%M-%S")

qr = QRCode(
    version=1,
    error_correction=ERROR_CORRECT_L,
    box_size=10,
    border=4
)

input_data = input("Input the url...\n> ")
# backgrd_code = input("Input the RGB...\n> ")
# code_code = input("Input the RGB...\n> ")

qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(image_factory=StyledPilImage, color_mask = SolidFillColorMask((22, 25, 27), (149, 165, 166)), module_drawer = RoundedModuleDrawer())
img.save(f"{dt}_output.png")
