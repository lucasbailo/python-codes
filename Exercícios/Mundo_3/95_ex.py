import enum
import os
from random import randint
from time import sleep
from datetime import datetime
from operator import itemgetter
os.system('cls') or None

dicio = {}
gols = []
time = list()

while True:
    dicio.clear()
    dicio['Nome'] = str(input('Digite o nome do Jogador: ')).strip().title()
    qtd = int(input(f'Quantas partidas {dicio["Nome"]} jogou? → Digite o número de partidas: '))
    gols.clear()
    for x in range(0,qtd):
        gols.append(int(input(f'  Digite quantos gols {dicio["Nome"]} marcou na {x+1}ª partida: ')))

    dicio['Gols'] = gols[:]
    dicio['Total'] = sum(gols)
    time.append(dicio.copy())

    while True:
        resp = str(input('Quer continuar? [S/N]: '))
        if resp in 'SN':
            break
        print('Erro! Responda "S" ou "N".')
    if resp == 'N':
        break

print('=_='*15)
for i, v in enumerate(time):
    print(f'{i+1:>3}: ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
