# Mostra quanto tu ganha por hora...

salario = float(input('Quanto tu ganha por mês? '))
hSemanais = float(input('Quantas horass semanais? '))

sHora = float(salario / (hSemanais * 4))
print('-------------------------------------------------------------------------')
print('--------->', end=' '), print(f'Seu salário é: R$ {salario} ')
print('-------------->', end=' '),print(f'Tu trabalha {hSemanais * 4}h por mês.')
print('------------------>', end=' '),print (f'tu ganha por hora trabalhada: R$ {sHora}')
print('-------------------------------------------------------------------------')
