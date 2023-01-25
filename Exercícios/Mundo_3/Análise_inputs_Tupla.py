import os
os.system('cls') or None

par = 0

num = (int(input('Digite o primeiro número: ')), 
        int(input('Digite o segundo número: ')),
        int(input('Digite o terceiro número: ')),
        int(input('Digite o quarto número: ')))

print(f'Os valores digitados são: {num}')
print(f'O menor valor é {min(num)}')
print(f'O número 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 aparece na {num.index(3)+1}ª posição')

for x in num:
    if x % 2 == 0:
        par += 1

print(f'A quantidade de números pares é {par}')

# tupla = (' ')
# num = 1

# while num < 4:
    
#     primeiro = str(input(f'Digite o {num}º número: '))
#     num +=1

#     segundo = str(input(f'Digite o {num}º número: '))
#     num +=1

#     terceiro = str(input(f'Digite o {num}º número: '))
#     num +=1

#     quarto = str(input(f'Digite o {num}º número: '))
#     num +=1

# tupla = primeiro + segundo + terceiro + quarto
# print(tupla)