import os
from re import I
from time import sleep
os.system('cls') or None

def contador(i,f,p):
    
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print(f'Contagem de {i} até {f} pulando de {p} em {p}')
    
    

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont:.2f} / ',end='',flush=True)
            sleep(0.4)
            cont += p
        print('→ Fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont:.2f} / ',end='',flush=True)
            sleep(0.4)
            cont -= p
        print('→ Fim')



contador(0, -100, 15)
contador(0, 3.14, 0.4)

print('')
print('Agora é sua vez!!!')
print('')
i = float(input('Digite o início: '))
f = float(input('Digite o fim: '))
p = float(input('Digite o passo: '))

contador(i,f,p)