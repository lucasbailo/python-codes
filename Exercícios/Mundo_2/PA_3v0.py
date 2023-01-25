import os
os.system('cls') or None

print('')
print('='*12,' Gerador de PA ','='*12)
print('')

num = int(input('Digite o número que você quer saber a PA: '))
raz = int(input('Digite a razão: '))
print('')

contador = 1
termo = num

total = 0
mais = 10

while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} → '.format(termo),end='')
       
        contador += 1
        termo += raz
    print('PAUSA')
    print('')
    mais = int(input('Quantos vezes você ainda quer ver? '))
    print('')
print('Progressão terminada com {} termos mostrados!'.format(total))
print('')