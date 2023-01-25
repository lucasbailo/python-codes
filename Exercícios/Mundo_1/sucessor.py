import os

os.system('cls') or None

n = int(input('Digite seu número: '))
ant = n - 1
suc = n + 1

print('Seu número é ', n,'!' + ' O antecessor é o número ', ant, ' e o sucessor é o número ', suc,'!')

# Apenas com uma variável

print('Seu número é {}! O o dobro é o número {} e a metade é o número {}!'.format(n,n*2,n/2))
