import os
from random import randrange

os.system('cls') or None

n = int(input('''Olá raça inferior! Vou escolher um número e vc tentará adivinhar...
Se você acertar, sua aposta será multiplicada por 2, senão tua grana será minha
Quer jogar? Então digite um o número que você acha que eu estou pensando entre 0 e 5: '''))

print(' ')

ap = int(input('Digite o valor de sua aposta em Reais: '))
print(' ')

rand = randrange(0,6)

print('O número que eu pensei foi {}'.format(rand))
print('O número que você disse foi: {}'.format(n))
print(' ')

if n == rand:
    print('Teve muita sorte humano, seu prêmio é R$ {}'.format(ap*2))
else:
    print('Patético! Como era de se esperar da sua raça... Você perdeu R$ {}'.format(ap))

print('')

