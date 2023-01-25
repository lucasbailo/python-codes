import os
os.system('cls') or None

lista = []

menor = 0
maior = 0

for x in range(0,5):
    lista.append(int(input(f'Digite um valor para posição {x}: ')))

    if x == 0:
        menor = maior = lista[x]
    else:
        if menor > lista[x]:
            menor = lista[x]
        if maior < lista[x]:
            maior = lista[x]

print('-'*40)
print(f'Você digitou os valores: {lista}')
print(f'O maior valor é {maior} e aparece nas posições: ',end='')

for i, v in enumerate(lista): # i = índice e v = variável
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'O menor valor é {menor} e aparece nas posições: ',end='')

for i, v in enumerate(lista): # i = índice e v = variável
    if v == menor:
        print(f'{i}... ',end='')