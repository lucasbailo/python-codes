import os
os.system('cls') or None

lista = []
listaPar = []
listaImpar = []

while True:
    n = int(input('Digite um número: '))

    lista.append(n)

    if n % 2 == 0:
        listaPar.append(n)
    else:
        listaImpar.append(n)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        print('')
    if continuar == 'N':
        break

print(f'A lista completa é {lista}')
print(f'A lista de números pares é {listaPar}')
print(f'A lista de números ímpares é {listaImpar}')
print('')