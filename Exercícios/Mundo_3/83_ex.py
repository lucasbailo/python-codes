import os
os.system('cls') or None

pilha = []

exp = str(input('Digite uma expressão: '))

for x in exp:
    if x == '(':
        pilha.append('(')

    elif x == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão não está válida!')
print('')