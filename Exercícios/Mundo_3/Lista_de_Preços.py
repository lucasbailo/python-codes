import os

os.system('cls') or None

produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
        
print('='*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('='*40)


print('-'*40)
for x in range(0,len(produtos)):
    if x % 2 == 0:
        print(f'{produtos[x]:.<30}',end='')
    else:
        print(f'R$ {produtos[x]:>6.2f}')

print('-'*40)
print('')