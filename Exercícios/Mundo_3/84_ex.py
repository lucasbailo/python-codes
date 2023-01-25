import os
os.system('cls') or None

temp = []
principal = []

menor = maior = 0

while True:
    temp.append(str(input('Digite o nome: ')).strip().title())
    temp.append(float(input('Digite o peso: ')))
    

    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if maior < temp[1]:
            maior = temp[1]
        if menor > temp[1]:
            menor = temp[1]

    principal.append(temp[:])
    temp.clear()

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().title()[0]
        print('')
    if continuar == 'N':
        break


print(f'Dados cadastrados! Lista: {principal}')
print(f'Você cadastrou {len(principal)} pessoas')

print(f'O maior peso é {maior} Kg. Que é o peso de',end='')
for x in principal:
    if x[1] == maior:
        print(f' [{x[0]}]',end='')

print()    
print(f'O menor peso é {menor} Kg. Que é o peso de',end='')
for x in principal:
    if x[1] == menor:
        print(f' [{x[0]}]',end='')



