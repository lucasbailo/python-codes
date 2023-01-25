import os
from random import randint
from time import sleep
from operator import itemgetter
os.system('cls') or None


x = ' '

ranking = {}
dicio = {'Jogador 1': randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1,6),
        'Jogador 4': randint(1,6)}

print('='*10,' VALORES SOTEADOS ','='*10)

for i, v in dicio.items():
    print(f'O {i} tirou {v}')
    sleep(0.65)

ranking = sorted(dicio.items(), key=itemgetter(1),reverse=True)
print('')

for i,v in enumerate(ranking):
    print(f'{i+1}º lugar foi o {v[0]} e tirou: {v[1]}')

print('')
    
