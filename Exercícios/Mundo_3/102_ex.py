import os

os.system('cls') or None

def fatorial(n, show=False):
    """
    → Calcula o fatorial de um número
    :param. n: O número a ser calculado.
    :param. show: (opicional) Mostrar ou não a conta.
    :return: O valor de Fatorial de um número n.
    """
    f = 1
    for x in range(n, 0,-1):
        if show:
            print(f'{x}',end='')
            if x > 1:
                print(' x ',end='')
            else:
                print(' = ',end='')     
        f *= x


    print(f)

p = int(input('Digite o número que vc quer fatorar: '))
fatorial(p,show=True)