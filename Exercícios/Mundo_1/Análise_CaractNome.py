import os

os.system('cls') or None

nome = str(input('Digite seu nome completo: ')).title().strip()

if 'Silva' in nome:
    print('Tem Silva no nome!')
else:
    print('Não tem Silva no nome!')
