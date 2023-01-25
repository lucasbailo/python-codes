import os
os.system('cls') or None

dicio = []
temp = {'Nome': '' , 'Média': '' , 'Resultado':''}

temp['Nome'] = str(input('Digite seu nome: ')).strip().title()
temp['Média'] = float(input('Digite a média: '))
if temp['Média'] < 7:
    temp['Resultado'] = 'Reprovado'
else:
    temp['Resultado'] = 'Aprovado'

print('')

for i, v in temp.items():
    print(f'{i} é igual a {v}')
print('')
