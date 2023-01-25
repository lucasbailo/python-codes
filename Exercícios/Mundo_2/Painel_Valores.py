import os
from time import sleep
os.system('cls') or None


primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
print('')
print('Escolha uma das opções abaixo digitando o número!')
print('')


opção = 0

while opção != 5:

    somar = primeiro + segundo
    multiplicar = primeiro * segundo

    sleep(1.6)

    print('=-=-'*12)
    print('')
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')

    sleep(0.6)

    print('')

    opção = int(input('Digite o número correspondente à sua opção: '))

    print('')

    if opção == 1:
        sleep(0.6)
        print('A soma dos números {} e {} é igual a {}'.format(primeiro,segundo,somar))
        print('')

    elif opção == 2:
        sleep(0.6)
        print('O produto da multiplicação de {} e {} é igual a {}'.format(primeiro,segundo,multiplicar))
        print('')

    elif opção == 3:
        sleep(0.6)
        if primeiro == segundo:
            sleep(0.6)
            print('Os números informados são iguais!')
            print('')
        elif primeiro > segundo:
            sleep(0.6)
            print('O número {} é maior que o segundo {}'.format(primeiro,segundo))
            print('')
        else:
            sleep(0.6)
            print('O número {} é maior que o número {}'.format(segundo,primeiro))
            print('')
    
    elif opção == 4:
        sleep(0.6)
        primeiro = int(input('Digite o novo primeiro valor: '))
        segundo = int(input('Digite o novo segundo valor: '))
        print('')
    
    elif opção == 5:
        sleep(0.6)
        print('Finalizando...')
        print('')
    
    else:
        sleep(0.6)
        print('Opção invalida. Tente novamente!')
        print('')





 


print('')
print('Fim do programa. Volte sempre!')
print('')

