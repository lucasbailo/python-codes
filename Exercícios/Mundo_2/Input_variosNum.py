import os

os.system('cls') or None

num = 0
pergunta = 'S'

soma = 0
contador = 0
maior = 0
menor = 0
quantidade = 0

txt = 1

while pergunta == 'S':
    num = int(input('Digite o {}º número: '.format(txt)))
    txt += 1
    
    contador += 1
    quantidade += 1
    soma += num
    media = soma / contador

    if quantidade == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    pergunta = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    
    print('')

print('')
print('Você digitou {} números, a soma deles é {} e a média é {:.2f}.'.format(contador,soma,media))
print('O menor número é {} e o maior número é {}'.format(menor,maior))
print('Fim!')