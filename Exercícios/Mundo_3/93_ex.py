import os
from random import randint
from time import sleep
from datetime import datetime
from operator import itemgetter
os.system('cls') or None

dicio = {}
gols = []

dicio['Nome'] = str(input('Digite o nome do Jogador: ')).strip().title()
qtd = int(input(f'Quantas partidas {dicio["Nome"]} jogou? → Digite o número de partidas: '))

for x in range(0,qtd):
    gols.append(int(input(f'  Digite quantos gols {dicio["Nome"]} marcou na {x+1}ª partida: ')))

dicio['Gols'] = gols[:]
dicio['Total'] = sum(gols)

print('')
print('='*50)
print(dicio)
print('='*50)
print('')

for i,v in dicio.items():
    print(f'O campo {i} tem o valor de {v}')

print(f"O jogador {dicio['Nome']} jogou {len(gols)} partidas")
print('='*50)
print('')

for i, v in enumerate(gols):
    print(f'Na partida {i+1} o jogador {dicio["Nome"]} marcou {v} gols')
print(f'Foi um total de {dicio["Total"]} gols')
print('')