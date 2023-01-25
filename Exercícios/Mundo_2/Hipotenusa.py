import os

os.system('cls') or None

import math

b = float(input('Digite a base do triângulo retângulo: '))
a = float(input('Digite a altura do triângulo retângulo: '))

h = math.sqrt(math.pow(b,2) + math.pow(a,2))

print('A hipotenusa do triângulo de base {} e altura {} é {}'.format(b,a,h))

h2 = math.hypot(a,b)

print(h2)