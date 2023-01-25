import os

os.system('cls') or None

n = 0
soma = 0
contador = 0

while n != 999:
    n = int(input('Digite um númemo (ou 999 para parar): '))
    if n != 999:
        contador += 1
        soma += n
    else:
        contador += 0
        soma += 0
    
print('')
print('Você digitou {} números e a soma deles é {}'.format(contador,soma))
print('')