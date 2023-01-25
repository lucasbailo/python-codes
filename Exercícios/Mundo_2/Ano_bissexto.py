from calendar import isleap
import os

os.system('cls') or None

ano = int(input('Digite um ano: '))

if isleap(ano):
    print('O ano {} é bissexto!'.format(ano))
else:
        print('O ano {} NÃO é bissexto!'.format(ano))