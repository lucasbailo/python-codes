from ast import While
import os
os.system('cls') or None

soma = qtd = 0

preçoMaisBarato = 0
nomeMaisBarato = ' '


while True:
    produto = str(input('Digite o nome do produto: ')).strip().title()
    preço = float(input('Digite o preço do produto: R$ '))

    soma += preço
    qtd += 1

    if qtd == 1:
        preçoMaisBarato = preço
        nomeMaisBarato = produto
    else:
        if preçoMaisBarato > preço:
            preçoMaisBarato = preço
            nomeMaisBarato = produto


    continuar = ' '
    while continuar not in 'SN':
        print('')
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        print('')
    if continuar == 'N':
        break

print('')
print(f'A soma de todos os produtos é R$ {soma:.2f}')
print(f'A quantidade de itens que você comprou é {qtd}')
print('')

print(f'O produto mais barato que você comprou é {nomeMaisBarato} e custou R$ {preçoMaisBarato:.2f}')
print('')