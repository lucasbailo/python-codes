import os
os.system('cls') or None

matriz = [[0,0,0] , [0,0,0] , [0,0,0]]

par = 0

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um número para a posição [{linha}, {coluna}]: '))

print('-='*40)

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end='')
    print()

print('')
print(f'A quantidade de números pares é {par}')