import os
from random import randint
from time import sleep
os.system('cls') or None




def sorteia(lista):
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ',end='',flush=True)
        sleep(0.4)

def somapar(lista):
    par = 0
    for x in lista:
        if x % 2 == 0:
            par += x
        else:
            par += 0
    print()
    print(f'Somando os valores pares de {lista}, temos {par}')

números = list()
sorteia(números)
somapar(números)
