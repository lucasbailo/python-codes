import os
os.system('cls') or None

print('='*12,' Gerador de PA ','='*12)

num = int(input('Digite o número que você quer saber a PA: '))
raz = int(input('Digite a razão: '))
qtd = int(input('Digite a quantidade de vezes que você quer que mostre: '))
contador = 1
termo = num


while contador <= qtd:
    print('{}'.format(termo),end='')
    print(' → ' if contador < qtd else '',end="")
    contador += 1
    termo += raz
