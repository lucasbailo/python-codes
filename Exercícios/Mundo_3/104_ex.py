import os

os.system('cls') or None

def leiaNum():
    n = str(input('Digite um número: '))
    while True:
        
        if n.isnumeric():
            print()
            print(f'Você digitou o número [" {n} "]!')
            print()
            break
        else:
            print()
            print(f'\033[0;31m[" {n} "] → Isso não é um número\033[m')
            n = str(input('TENTE NOVAMENTE → Digite um número: '))

leiaNum()
 
