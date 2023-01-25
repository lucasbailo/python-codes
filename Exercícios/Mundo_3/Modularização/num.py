import os
os.system('cls') or None

import uteis

num = int(input('Digite um número: '))

fat = uteis.fatorial(num)

print(f'O Fatorial de {num} é {fat}. O dobro é {uteis.dobro(num)} e o triplo é {uteis.triplo(num)}')
