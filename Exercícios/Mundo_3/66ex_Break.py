import os
os.system('cls') or None

contador = soma = 0

while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    contador += 1
    soma += num
    media = soma / contador

print('')
print(f'Você digitou {contador} números e a soma deles foi {soma}. E a média é {media}')