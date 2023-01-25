import os
os.system('cls') or None

t1 = 0
t2 = 1

n = int(input('Digite a quantidade de termos que você quer ver: '))

print('{} → {}'.format(t1,t2),end='')

contador = 3

while contador <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    contador += 1
print(' Fim',end='')