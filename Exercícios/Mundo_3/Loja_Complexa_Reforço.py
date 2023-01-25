import os

os.system('cls') or None

soma = qtd = maisBarato = maisCaro = 0

nomeBarato = nomeCaro = ' '

while True:
    produto = str(input('Digite o nome do produto: ')).strip().title()
    preço = int(input('Digite o preço do produto: R$ '))

    soma += preço
    qtd += 1

    if qtd == 1:
        nomeBarato = nomeCaro = produto
        maisBarato = maisCaro = preço
    
    else:
        if maisBarato > preço:
            maisBarato = preço
            nomeBarato = produto
        
        if maisCaro < preço:
            maisCaro = preço
            nomeCaro = produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print('')
print(f'O total de {qtd} produtos custou R$ {soma} ao todo!')
print('')

if qtd == 1:
    print(f'Você comprou apenas um produto que é o(a) {produto} e custou R$ {preço:.2f}.')
else:
    print(f'O Produto mais caro é {nomeCaro} e custou R$ {maisCaro:.2f}')
    print(f'O Produto mais barato é {nomeBarato} e custou R$ {maisBarato:.2f}')