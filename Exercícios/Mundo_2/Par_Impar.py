from distutils.command.install_scripts import install_scripts
import os
from random import randrange

os.system('cls') or None

num = int(input('Digite um número: '))

if num % 2 == 0: # Se o resto da divisão do número digitado for zero, ele é par, senão, é ímpar
    print('O número {} é par'.format(num))
else:
    print('O número {} é ímpar'.format(num))