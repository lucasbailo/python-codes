from math import factorial
import os
os.system('cls') or None



num = int(input('Digite o número que você quer saber o fatorial: '))
c = num
fat = 1

print('Calculando {}! = '.format(num),end='')

while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ',end='')
    fat *= c
    c -= 1

print('{}'.format(fat))

