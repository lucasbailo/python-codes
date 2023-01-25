import os
os.system('cls') or None
from random import randint

vitórias = 0

while True:
    
    numPc = randint(0,10)
    num = int(input('Digite um número: '))
    escolha = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    resultado = num + numPc
    
    print('')
    
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]

    if escolha == 'P' and resultado % 2 == 0 or escolha == 'I' and resultado % 2 != 0:
        print(f'Parabéns! Eu coloquei {numPc} e você {num}! O resultado foi', 'Par' if resultado % 2 == 0 else 'Ímpar','.')
        print('')
        vitórias += 1
    else:
        print('')
        print('Você escolheu','Par' if escolha == 'P' else 'Ímpar',f'mas o resultado foi','Par.' if resultado % 2 == 0 else 'Ímpar.',)
        print(f'Eu coloquei {numPc} e você colocou {num}. O total é {resultado}')
        print('')
        break

print(f'Você ganhou {vitórias} vezes')
print('')
