import os
from turtle import st
os.system('cls') or None

brasileirão = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Patético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')


while True:

    print('='*122)
    print(f'→ A lista de times do Brasileirão é: {brasileirão}')
    print('='*122)
    print('')
    print('='*122)
    print(f'→ Os 5 primeiros são: {brasileirão[0:5]}')
    print('='*122)
    print('')
    print('='*122)
    print(f'→ A zona de rebaixamento é formada por (4 últimos): {brasileirão[-4:]}')
    print('='*122)
    print('')
    print('='*122)
    print(f'→ Os times em ordem alfabética são: {sorted(brasileirão)}')
    print('='*122)
    print('')

    tipo = ' '
    while tipo not in 'PN':
        tipo = str(input('Você quer ver o time pela posição ou a posição pelo nome do time? [Posição / Nome] - [P/N]: ')).strip().upper()[0]

    if tipo == 'P':

        time = int(input('Digite a posição que você quer verficar: '))

        print(f'A {time}ª posicação está ocupada pela {brasileirão[time-1]}')
    else: 
        nome = str(input('Digite o nome de um time: ')).strip().title()

        print(f'A posição do {nome} no brasileirão é {brasileirão.index(nome)+1}º')
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [Sim/Não] - [S/N]: ')).strip().upper()[0]
    
    if continuar == 'N':
        print('')
        print('Fim do programa!')
        print('')
        break
    else:
        continue