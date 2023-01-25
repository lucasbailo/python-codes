import os
os.system('cls') or None

num = int(input('Digite um número: '))
print('')

tot = 0

for x in range(1,num+1):
    if num % x == 0:
        print('\033[32m',end='')
        tot += 1
    else:
        print('\033[31m',end='')
    print('{}'.format(x), end=' ')


print('')

print('\n\033[mO número {}, foi divisível {} vezes'.format(num,tot))

print('')

if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO é primo!')
print('')
