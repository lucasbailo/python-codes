from operator import ge
import os
os.system('cls') or None

geral = []
temp = {}

soma = media = 0
qtd = 0

while True:
    temp['Nome'] = str(input('Digite o nome: ')).strip().title()
    temp['Sexo'] = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    while temp['Sexo'] not in 'MF':
        temp['Sexo'] = str(input('ERRO! Digite apenas "M" ou "F": ')).strip().upper()[0]
    
    temp['Idade'] = int(input('Digite a idade: '))
    soma += temp['Idade']
    geral.append(temp.copy())

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        print('')
    if continuar == 'N':
        break

print('')
print('-'*50)
print(f'Ao todo tivemos {len(geral)} pessoas cadastradas!')

media = soma / len(geral)

print(f'A média de idade é {media:.2f} anos')
print(f'As mulheres cadastradas foram: ', end='')

for x in geral:
    if x['Sexo'] == 'F':
        print(f'[{x["Nome"]}] ', end='')

print()
print('')
print('_Lista das pessoas com idade acimda da média_')

print('As pessoas com idade acima da média são: ',end='')

for x in geral:
    if x['Idade'] > media:
        print('   ',end='')
        for i, v in x.items():
            print(f'{i} = {v}; ',end='')
print('')