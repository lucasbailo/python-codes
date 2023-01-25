import os

os.system('cls') or None


while True:

        num = int(input('Digite o número que você quer saber a tabuada: '))
        

        if num > 0: 
            print('')
            print('='*12,'> TABUADA DO {} <'.format(num),'='*12)
            print('')

            for x in range(0,11):
                print('{} x {} = {}'.format(x,num,x*num))

            print('')
            print('='*12,'> Fim! <','='*12)
            print('')
        else:
            print('')
            print('Você informou um número negativo')
            print('')
            break
