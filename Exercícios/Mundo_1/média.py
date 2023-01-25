import os

os.system('cls') or None

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

med = (n1 + n2) / 2

print('A média arredondada das notas {} e {} é {:.1f}!'.format(n1,n2,med))
print('A média das notas {} e {} é {}!'.format(n1,n2,med))