import os

os.system('cls') or None

def ficha():
    n = str(input('Digite o nome do jogador: ')).strip().title()
    if n == '':
        n = '<desconhecido>'
    g = str(input(f'Digite a quantide de gols do {n}: '))
    
    while True:
        if g.isnumeric():
            int(g)
            break
        else:
            g = str(input(f'APENAS NÚMEROS → Digite a quantide de gols do {n}: '))

    
    print()
    print(f'O jogador {n} fez {g} gols')
    print()

ficha()