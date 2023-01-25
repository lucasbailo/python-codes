import os

os.system('cls') or None

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

med = (n1 + n2) / 2
print('')

if 7 > med >= 5:
    print('A média é {:.2f}, o aluno está de RECUPERAÇÃO'.format(med))
elif 5 > med:
    print('A média é {:.2f}, o aluno está REPROVADO'.format(med))
else:
    print('A média é {:.2f}, o aluno está APROVADO'.format(med))
    
print('')