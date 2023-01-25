import os

os.system('cls') or None

idade = ''
sexo = ''

soma = qtd = homens = mulheres = 0

idadeM = idadeF = 0
mediaM = mediaF = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]

    # Para não digitar nada além de M e F:

    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
        

    # Quer continuar?
    continuar = ' '
    while continuar not in 'SN':
        print('')
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        print('')
    
    soma += idade
    qtd += 1  

    # Quantidade de pessoas de cada sexo

    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        mulheres += 1

    # Média de idade de cada sexo
    
    if sexo == 'M':
        idadeM += idade
        mediaM = idadeM / homens
    if sexo == 'F':
        idadeF += idade
        mediaF = idadeF / mulheres
    # Médias

    mediageral = soma / qtd
    
    # Break

    if continuar == 'N':
        break    

print('')

print(f'O número de homens é {homens}, o número de mulheres é {mulheres}')

print('')

print(f'A média de idade das mulheres é {mediaF} e a média de idade dos homens é {mediaM}')
print('')
print(f'A média geral é {mediageral}')


