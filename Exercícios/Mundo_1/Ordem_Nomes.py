import os

os.system('cls') or None

n = str(input('Digite seu nome completo: ')).title().strip()

n2 = n.split()

print('')

print('Seu primeiro nome é {}'.format(n2[0]))
print('Seu último nome é {}'.format(n2[len(n2)-1]))