from qrcode import QRCode
from qrcode.constants import ERROR_CORRECT_L
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from datetime import datetime
import cv2



def hex2rgb(code):
    code = code.lstrip("#")
    return tuple(int(code[i:i+2], 16) for i in (0, 2, 4))

dt = datetime.now().strftime("%Y%m%d %H-%M-%S")

qr = QRCode(
    version=1,
    error_correction=ERROR_CORRECT_L,
    box_size=10,
    border=4
)

input_data = input("Input the url...\n> ")
backgrd_code = hex2rgb(input("Input the backgrd RGB...\n> "))
code_code = hex2rgb(input("Input the code RGB...\n> "))

# print(f"backgrd_code:{backgrd_code}, code_code:{code_code}")

qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(image_factory=StyledPilImage, color_mask = SolidFillColorMask(backgrd_code, code_code), module_drawer = RoundedModuleDrawer())
img.save(f"{dt}_output.png")
print("img saved.")
img = cv2.imread(f"{dt}_output.png")
cv2.imshow(f"{dt}_output", img)
