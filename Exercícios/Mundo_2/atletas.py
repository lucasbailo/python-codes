from datetime import date
import os

os.system('cls') or None

nasc = int(input('Digite o ano de nascimento do atleta: '))

anoatual = date.today().year

idade = anoatual - nasc
print('')
print('A idade do atleta é {}'.format(idade))
print('')


if idade > 25:
    print('Classificação: MASTER')
elif idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
   print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')

