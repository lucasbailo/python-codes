import os

os.system('cls') or None

from math import trunc

num = float(input('Digite um número quebrado: '))

print('A parte inteira de {} é {}'.format(num,trunc(num)))
print('A parte inteira de {} é {:.1f}'.format(num,int(num)))
