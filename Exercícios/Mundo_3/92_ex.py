import os
from random import randint
from time import sleep
from datetime import datetime
from operator import itemgetter
os.system('cls') or None

dados = dict()

print('='*30)
print(f'{"Digite os Dados Trabalhistas":^30}')
print('='*30)

dados['Nome'] = str(input('Nome: ')).strip().title()
nasc = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Digite a carteira de trabalho ("0" se não tem): '))
if dados['CTPS'] != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário R$'] = float(input('Salário R$: '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Ano de contratação'] + 35) - datetime.now().year)

print('='*30)
print(f'{"DADOS":^30}')
print('='*30)

print('')

for i, v in dados.items():
    print(f'→ {i}: {v}')

print('')