import os
os.system('cls') or None

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

qtd = 0

while True:
    
    num = int(input('Digite um número de 0 a 20: '))
    
    while num < 0 or num > 20:
        num = int(input('Apenas entre 0 e 20!! Digite um número: '))
    
    print('')
    print(f'Você digitou o número {cont[num].title()}')
    print('')

    qtd += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        print('')
    if continuar == 'N':
        print('')
        print(f'Fim do programa! Você digitou {qtd} números')
        print('')
        break

        

        



