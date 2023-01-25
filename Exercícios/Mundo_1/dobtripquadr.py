import os

os.system('cls') or None

n = int(input('Digite um número: '))

print('Seu número é {}! O dobro do seu número é {} e a raiz quadrada do seu número é {}!'.format(n, n*2, n**(1/2)))