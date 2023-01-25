import os

os.system('cls') or None

soma = 0
cont = 0

for x in range(0,6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        soma += n
        cont += 1

print('')

print('Você informou {} números pares e a soma dos valores pares digitados é {}'.format(cont,soma))
print('')
