from openpyxl import Workbook


def obter_nota(mensagem):
    while True:
        nota = input(mensagem)
        nota = nota.replace(',', '.')  # substituir vírgula por ponto
        try:
            valor = float(nota)
            if 0 <= valor <= 10:  # verifica se a nota está no intervalo valido
                return valor
            else:
                print("por favor, digite uma nota entre 0 e 10. ")
        except ValueError:
            print("Entrada invalida. Por favor, use ponto ( . ) ao invés de vírgula.")


# Cria um novo Workbook (arquivo do Excel)

wb = Workbook()
ws = wb.active

# Adiciona cabeçalhos
ws.append(['Nome', 'Nota B1', 'Nota B2', 'Nota B3', 'Média', 'Resultado'])

# OBITENDO NOME DOS ALUNOS E SUAS NOTAS

alunos = []

while True:
    nome = input("Digite o nome do aluno (ou 'Sair' para Terminar): ")
    if nome.lower() == "sair":
        break
    nota_b1 = obter_nota(f"Digite a nota da B1 do aluno {nome.title()}: ")
    nota_b2 = obter_nota(f"Digite a nota da B2 do aluno {nome.title()}: ")
    nota_b3 = obter_nota(f"Digite a nota da B3 do aluno {nome.title()}: ")
    alunos.append([nome.title(), nota_b1, nota_b2, nota_b3])

    # Aqui vamos armazenar o nome e a notas na lista 'alunos'

print('------------------------------------------------------------')
print("DADOS DOS ALUNOS ARMAZENADOS COM SUCESSO!")
print(alunos)
print('------------------------------------------------------------')
# CALCULANDO A MEDIA DOS ALUNOS e DETERMINAR A APROVAÇÃO
# Supondo que 'alunos' é a lista que contém os nomes e notas dos alunos

print("lista de APROVAÇÃO ")
medias = []

for aluno in alunos:
    nome = aluno[0]
    notas = aluno[1:]
    media = sum(notas) / len(notas)
    medias.append(media)
    resultado = "Aprovado" if media >= 6 else "Reprovado"
    ws.append([nome, *notas, round(media, 2), resultado])
    print(f"Aluno: {nome.title()} - Média: {round(media, 2): .2f} - {resultado}")

print('------------------------------------------------------------')
# Calculando a média da turma

media_turma = sum(medias) / len(medias)
print(f"Media Geral da turma: {round(media_turma, 2): .2f}")

# Salva o arquivo do Excel
wb.save("notas_alunos.xlsx")
