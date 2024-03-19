# Importar a biblioteca qrcode
import qrcode

# Definir o link de site que queremos armazenar no QRCode
link = "[5](https://linktr.ee/felipecard0so)"

# Criar o QRCode a partir do link
img = qrcode.make(link)

# Salvar o QRCode em um arquivo de imagem
img.save("qrcode.png")
