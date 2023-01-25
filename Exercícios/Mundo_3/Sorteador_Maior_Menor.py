import os
from random import randint

os.system('cls') or None


# Jeito 1

números = randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10)

print(f'A lista de números é: ',end='')

for x in números:
    print(f'{x}',end=' ')

print(f'\nO maior valor é: {max(números)}')
print(f'Já o menor valor é: {min(números)}')

# Jeito 2 (modo que eu fiz kkk)

# qtd = 0

# maior = menor = ' '

# print('A lista de números é: ',end='')

# while True:
#     qtd += 1
#     u = randint(0,10)
#     print(u,end=' ')

#     if qtd == 1:
#         menor = maior = u
#     else:
#         if u < menor:
#             menor = u
#         if u > maior:
#             maior = u

#     if qtd > 4:
#         print(f'\nO maior número é {maior}')
#         print(f'O menor número é {menor}')
#         break
