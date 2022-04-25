import qrcode
from PIL import Image
# ----------------------------------------------------------

# ---------- outro modelo mais simples de QrCode-----------

# imagem_qr = qrcode.make(r"https://wa.me/+17472144567?text=Hello!%20Woulda%20you%20like%20to%20order.")
# imagem_qr.save("qrDay.png")

# ----------------------------------------------------------

logo = Image.open('nome da imagem')
# este arquivo tem que estar na mesma pasta de criação deste cod.
# esta imagem fiacara centralizada como um logo no QrCode

basewidth = 75
wprcent = (basewidth / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wprcent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
qr_big = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr_big.add_data(r'https://wa.me/+telefone?text=Hello!%20Woulda%20you%20like%20to%20order.')  # mensagem do Qrcode.
qr_big.make()
img_qr_big = qr_big.make_image(fill_color='#0b4e39', back_color="white").convert('RGB')
pos = ((img_qr_big.size[0] - logo.size[0]) // 2, (img_qr_big.size[1] - logo.size[1]) // 2)
img_qr_big.paste(logo, pos)
img_qr_big.save("day.png")  # formato que o arquivo sera salvo, aqui usei png, mas tu escolhe o formato.
