import win32com.client as win32
from datetime import datetime

# Criar objeto para interagir com o Outlook
outlook = win32.Dispatch('Outlook.Application')

# Criar um novo e-mail
mail = outlook.CreateItem(0)

# Ler os endereços de e-mail do arquivo
with open(r'LOCAL ONDE ESTA A \lista_de_email.txt', 'r') as file:
    bcc_emails = file.read().splitlines()

# Configurar destinatários (para, cópia e cópia oculta)
mail.BCC = ';'.join(bcc_emails)

# Obter a data atual
data_atual = datetime.now().strftime('%d/%m/%Y')

# Configurar assunto e corpo do e-mail
mail.Subject = f"Felipe Cardoso - {data_atual}"
mail.Body = f"""Prezados/as, tudo bem.\n

Meu nome é Felipe, moro em Curitiba e estou a procura de um trabalho onde eu possa mostrar todo meu potencial e energia, 
em um mundo tão competitivo.
Anexo meu curriculo, e me coloco a diposição para uma possivel entrevista. 
\n
Atentamente:\n
Felipe Cardoso"""

# Anexar arquivo (currículo)
attachment = r"LOCAL ONDE ESTA O ARQUIVO EM.pdf"
mail.Attachments.Add(attachment)

# Enviar e-mail
mail.Send()
