import os
os.system('cls') or None

lista = []

for x in range(0,5):
    n = int(input('Digite um valor: '))
    if x == 0 or n > lista[len(lista)-1]:
        lista.append(n)
print(lista)