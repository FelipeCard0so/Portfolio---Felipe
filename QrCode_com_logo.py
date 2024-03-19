import qrcode
from PIL import Image
"""
# ---------- outro modelo mais simples de QrCode-----------

imagem_qr = qrcode.make(r"https://linktr.ee/felipecard0so")
imagem_qr.save("QRfurini.png")

# ----------------------------------------------------------

"""
logo = Image.open('TT.png')  # este arquivo tem que estar na mesma pasta de criação deste cod.
# esta imagem fiacara centralizada como um logo no QrCode

# Redimensionando a imagem do logo
basewidth = 120
wpercent = (basewidth / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.LANCZOS)  # Usando LANCZOS para redimensionar
qr_big = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr_big.add_data(r'https://linktr.ee/TTrincas')  # mensagem do Qrcode.
qr_big.make()
img_qr_big = qr_big.make_image(fill_color='#333333', back_color="white").convert('RGB')

# Calculando a posição para colar o logo no centro do QR code
pos = ((img_qr_big.size[0] - logo.size[0]) // 2, (img_qr_big.size[1] - logo.size[1]) // 2)
img_qr_big.paste(logo, pos)
img_qr_big.save("QrTT.png")  # formato que o arquivo sera salvo, aqui usei png, mas tu escolhe o formato.
