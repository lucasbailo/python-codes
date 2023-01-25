import os

os.system('cls') or None

import math

num = int(input('Digite o número que você quer saber a tabuada: '))
print('')
print('='*12,'> TABUADA DO {} <'.format(num),'='*12)
print('')

for x in range(0,11):
    print('{} x {} = {}'.format(x,num,x*num))

print('')
print('='*12,'> Fim! <','='*12)
print('')
