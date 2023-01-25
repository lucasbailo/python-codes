import os
from random import randint
from time import sleep
os.system('cls') or None

def maior(* núm):
    cont = maior = 0
    print('-'*35)
    print('Analisando os números: ')
    for x in núm:
        print(f'{x} ',end='',flush=True)
        sleep(0.4)
        cont += 1
        if cont == 0:
            maior = x
        else:
            if x > maior:
                maior = x
    
    print()
    print('')
    print(f'Foram informados {cont} ao todo')
    print(f'O maior valor é {maior}')
    print('_'*35)
# principal

maior(randint(1,20),randint(1,20),randint(1,20),randint(1,20),randint(1,20))
maior(randint(1,20),randint(1,20),randint(1,20),randint(1,20),randint(1,20))
maior(randint(1,20),randint(1,20),randint(1,20),randint(1,20),randint(1,20))
maior(randint(1,20),randint(1,20),randint(1,20),randint(1,20),randint(1,20))
