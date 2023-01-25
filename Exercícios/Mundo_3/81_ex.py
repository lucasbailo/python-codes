import os
os.system('cls') or None

lista = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

lista.sort(reverse=True)

print('')
print(f'Você digitou {len(lista)} números')
print(f'Os números digitados em ordem decrescente são: {lista}')
if 5 in lista:
    print('O número 5 está presente na sua lista!')
else:
    print('O número 5 não está presente na sua lista!')
print('')