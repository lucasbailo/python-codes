import os

os.system('cls') or None

num = int(input('Digite um número inteiro: '))

print('')

print('''Escolha um dos 3 números abaixo para converter o númer que você digitou: 
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')

print('')

opcao = int(input('Sua opção: '))

print('')

if opcao == 1:
    print('O numeral {} convertido para BINÁRIO é igual a {:b}'.format(num,num))
elif opcao == 2:
    print('O numeral {} convertido para OCTAL é igual a {:o}'.format(num,num))
elif opcao == 3:
    print('O numeral {} convertido para HEXADECIMAL é igual a {:X}'.format(num,num))
else:
    print('A opção digitada não está entre as opções')

print('')
print('Fim!')