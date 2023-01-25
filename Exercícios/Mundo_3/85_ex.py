import os
from random import vonmisesvariate
os.system('cls') or None

lista = [[],[]]
temp = []

valor = 0

qtd = 1

for x in range(1,8):
    valor = int(input(f'Digite o {x}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

lista[0].sort()
lista[1].sort()
print(f'Os pares são: {lista}')
print(f'Os pares são: {lista[0]}')
print(f'Os ímpares são: {lista[1]}')

    