import os

os.system('cls') or None

print('Vamos analisar os valores que você digitar e informar se podem formar um triângulo!')

print('')

l1 = int(input('Digite o primeiro lado do triângulo: '))
l2 = int(input('Digite o segundo lado do triângulo: '))
l3 = int(input('Digite o terceiro lado do triângulo: '))

print('')

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Os lados informados PODEM formar um triângulo ',end='')
    
    if l1 == l2 and l1 == l3:
        print('equilátero, ou seja, todos os lados são iguais!')
    elif l1 == l3 or l1 == l2 or l2 == l3:
        print('isóceles, ou seja, pelo menos 2 lados são iguais!')
    else:
        print('escaleno, ou seja, todos os lados são diferentes!')

else:
     print('Os lados informados NÃO podem formar um triângulo')

print('')
