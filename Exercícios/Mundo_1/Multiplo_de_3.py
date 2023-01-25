import os

os.system('cls') or None

soma = 0
cont = 0

for x in range(1,501,2):
    if x % 3 == 0:
        soma += x
        cont += 1

print('')

print('A soma de todos os valores solicitados é {}'.format(soma))

print('')

print('A quantidade de valores na soma é {}'.format(cont))

print('')