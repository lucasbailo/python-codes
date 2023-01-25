from ntpath import join
import os
os.system('cls') or None

frase = str(input('Digite uma palavra: ')).strip().upper()
separada = frase.split()
junto = ''.join(separada)
inverso = ''

print('')
print('Você digitou a frase {}'.format(frase))

for x in range(len(junto) - 1,-1,-1):
    inverso += junto[x]

print('')

print('{} ao contrário fica {}'.format(junto,inverso))
print('')
if junto == inverso:
    print ('{} É palíndromo de {}'.format(inverso,junto))
else:
    print ('{} NÃO é palíndromo de {}'.format(inverso,junto))
print('')