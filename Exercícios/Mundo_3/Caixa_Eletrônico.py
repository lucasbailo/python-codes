import os
from wsgiref.validate import validator
os.system('cls') or None

print('='*30)
print('{:^30}'.format('BANCO PY'))
print('='*30)

saque = int(input('Qual valor você quer sacar? R$ '))
print('')
total = saque
cédula = 50
totalCédulas = 0

while True:
    if total >= cédula:
        total -= cédula
        totalCédulas += 1
    else:
        if totalCédulas > 0:
            print(f'O total de cédulas é {totalCédulas} de R$ {cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        totalCédulas = 0
        if total == 0:
            break
    
print('')