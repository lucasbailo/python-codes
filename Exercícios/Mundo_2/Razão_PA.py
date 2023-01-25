import os

os.system('cls') or None

print('='*12,'> 10 termos de uma PA <',12*'=')
print('')

pri = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))

soma = 0
decimo = pri + (10-1) * raz

for x in range(pri,decimo+raz,raz):
      print('{}'.format(x),end=' → ')
print('Fim')