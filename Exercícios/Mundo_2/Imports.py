import os

os.system('cls') or None

import math

num = int(input('Digite um número: '))

raiz = math.sqrt(num)
pot = math.pow(num,2)

print('A raiz quadrada de {} é {} e a número ao quadrado é {}'.format(num,raiz,pot))