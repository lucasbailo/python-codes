import os

os.system('cls') or None

Real = float(input('Digite o valor em reais: '))
Dol = Real / 5.17

print('Convertendo R$ {:.2f} reais é igual a US$ {:.2f} dólares!'.format(Real,Dol))