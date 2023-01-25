import os
os.system('cls') or None

maior = 0 
menor = 0 

for x in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(x)))
    if x == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('')
print('O maior peso é {} Kg'.format(maior))
print('O menor peso é {} Kg'.format(menor))
print('')