import os

os.system('cls') or None

n1 = int(input('Digite um número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))

menor = min(n1,n2,n3)

print('O menor número é ',menor,'!')
