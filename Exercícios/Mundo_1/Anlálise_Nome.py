import os

os.system('cls') or None

nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')
print('Seu nome é: {} '.format(nome.title()))
print('Seu nome em letras maiúsculas é: {} '.format(nome.upper()))
print('Seu nome em letras minúsculas é: {} '.format(nome.lower()))
print('A quantidade de caracteres do seu nome é: {}'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras!'.format(nome.find(' ')))
split = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(split[0],len(split[0])))