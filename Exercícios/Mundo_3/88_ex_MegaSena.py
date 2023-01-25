import os
from random import randint
from time import sleep
os.system('cls') or None

lista = []
jogos = []


print('-'*30)
print('       Joga na Mega Sena      ')
print('-'*30)
quant = int(input('Digite qts listas você quer gerar: '))
tot = 1

while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break      
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('='*15,f' Sorteando {quant} jogos! ','='*15)
print(' ')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.8)

print('')
print('Boa Sorte!')