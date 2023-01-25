import os
from xml.dom import InuseAttributeErr
os.system('cls') or None

lista = []

while True:
    n = int(input('Digite um valor: '))

    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('O valor informado já foi adicionado anteriormente, digite outro valor!')
    print('')

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        print('')
    if continuar == 'N':
        print(f'A sua lista é: {sorted(lista)}')
        print('Fim do programa')
        break
