from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-' * 20)
    print(f'contagem de {i} até {f}, de: ({p} em {p}).')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end="")
            sleep(0.5)
            cont += p
        print('Fim...')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end="")
            sleep(0.5)
            cont -= p
        print('Fim...')


contador(10, 0, 1)
contador(0, 10, 2)
print('-' * 20)
print("Determine como sera a proxima contagem: ")
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
