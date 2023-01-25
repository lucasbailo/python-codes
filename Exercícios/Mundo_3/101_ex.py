import os
from random import randint
from time import sleep

os.system('cls') or None

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        print(f'Não é necessário votar com {idade} anos!')
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos, o voto é opcional!'
    if idade >= 18:
        return f'Com {idade} anos, o voto é obrigatório!!!' 


print(voto(int(input('Em que ano você nasceu? Digite o ano: '))))
