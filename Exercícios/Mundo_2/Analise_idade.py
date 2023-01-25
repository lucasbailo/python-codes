import os
from datetime import date

os.system('cls') or None

atual = date.today().year

Qmenor = 0
Qmaior = 0

for x in range(1,8):
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(x)))
    idade = atual - nasc
    if idade >= 21:
        Qmaior += 1
    else:
        Qmenor += 1

print('')
print('A quantidade de pessoas com mais de 21 anos é de {}'.format(Qmaior))
print('A quantidade de pessoas com menos de 21 anos é de {}'.format(Qmenor))
print('')
