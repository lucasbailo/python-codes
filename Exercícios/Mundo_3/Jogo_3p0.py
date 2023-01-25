import os
from random import randrange
os.system('cls') or None

adv = randrange(0,11)
tent = 1

guess = int(input('Pensei em um número de 0 a 10 aqui, tente adivinhar! Digite um número: '))

print('')

while guess != adv:
    if guess > adv:
        print('Errou, o número que eu pensei é menor!')
        print('')
    else:
        print('Errou, o número que eu pensei é maior!')
        print('')
    tent += 1
    guess = int(input('{}ª Chance! Tente outra vez: '.format(tent)))
    
    

print('')
print('Parabéns, você acertou! O número que eu tinha pensado foi {}'.format(adv))
print('Você acertou em {} tentativas'.format(tent))
print('')