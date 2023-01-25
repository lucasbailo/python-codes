from itertools import count
import os
os.system('cls') or None

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

# A variável "x" serve para listar as palavras
# A variável "y" serve para listar cada letra da variável "x" em palavras

vogais = 0

for x in palavras:
    print(f'\nNa palavra "{x.title()}" temos as vogais: ',end='')
    for y in x:
        if y.lower() in 'aâãáàäeëéèêiíìîïoóòôöõuùüûú':
            print(f'{y}',end=' ')

