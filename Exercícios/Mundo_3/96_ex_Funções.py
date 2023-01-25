import os
os.system('cls') or None

def area(b,h):
    a = b * h
    print(f'A área de um quadrado com base {b:.2f} m e altura {h:.2f} m é de {a:.2f} m²')



print('__Calculador de área em m²__')

dicio = {}
lista = []

while True:
    b = float(input('Digite a base em metros: '))
    h = float(input('Digite a altura em metros: '))

    area(b,h)

    continuar =' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        print('')
        print('Fim do Programa!')
        print('')
        break