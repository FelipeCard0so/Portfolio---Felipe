"""
Calculadora de juros compostos...
"""
print("---------------------------------------------------------------------------------------------------------------")
nome = input("Qual o seu nome? ")
print(f"olá {nome.title()}, Seja muito bem vindo aos juros compostos! Aqui nós cuidamos da sua aposentadoria ;)\n")
print("---------------------------------------------------------------------------------------------------------------")
din_inicial = int(input("digite quanto pretende investir hoje? "))
tempo_desejado = int(input(f"Por quantos meses pretende deixar esse valor de:R$ {din_inicial} investido? "))
taxa = float(input("digite em (decimal ex: 0.00) qual o valor da taxa mensal de retorno do seu investimento: "))
sal_desejado = int(input("Digite o salario que você quer receber ao se aposentar: "))
aporte = int(input("De quanto será o aporte mensal? "))

print("---------------------------------------------------------------------------------------------------------------")
tempo_decorrido = 0

while tempo_decorrido < tempo_desejado:
    if tempo_decorrido == 0:

        montante = din_inicial * (1 + taxa) ** 1
        montante = round(montante, 2)
        tempo_decorrido = tempo_decorrido + 1

    else:
        # noinspection PyUnboundLocalVariable
        montante = (montante + aporte) * (1 + taxa) ** 1
        montante = round(montante, 2)
        tempo_decorrido = tempo_decorrido + 1


# noinspection PyUnboundLocalVariable
print(f"Parabens {nome.title()}!\n "
      f"Ao final de {tempo_desejado//12} anos. Você terá o valor acumulado de: R$ {montante} Reais\n")

# adicionando funcionalidade de liberdade financeira

salario_mensal = (montante * taxa)
salario_mensal = round(salario_mensal, 2)

if salario_mensal >= sal_desejado:
    print(f" Parabens, você pode se aposentar!\n"
          f" Seu salario mensal com esse montante é de R$ {salario_mensal}\n")

elif salario_mensal < sal_desejado:
    print(f" infelizmente ainda nao pode se aposentar!\n"
          f" Seu salario mensal com esse montante é de R$ {salario_mensal}")
print("---------------------------------------------------------------------------------------------------------------")
fechar = input("aperte enter para fechar: ")
print("---------------------------------------------------------------------------------------------------------------")
