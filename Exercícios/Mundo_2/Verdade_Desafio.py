import os
from timeit import repeat

os.system('cls') or None

import random

v1 = 'Já fez algo de que se arrependa? Se sim o que?'
v2 = 'Ja perdeu o celular?'
v3 = 'Você tem um dia inesquecível?, se sim como foi?'
v4 = 'Você ja desistiu de algo muito importante? Se sim o que foi?'
v5 = 'Já sofreu ou praticou bullying na escola?'
v6 = 'Tem algum grande desejo? Qual?'
v7 = 'Ja entrou em uma briga? Como foi?'
v8 = 'Você quer ter filhos? Se sim, quantos?'

d1 = 'Imite um macaco'
d2 = 'Deixe a pessoa do seu lado direito te dar um tapa'
d3 = 'Teve sorte, pule a sua vez'
d4 = 'Fale uma raça de cachorro que começa com y, se não conseguir imite um '
d5 = 'Não fale nada pelos proximos 5 minutos'
d6 = 'Fale para uma pessoa que não está na brincadeira que a ama (não vale parente)'
d7 = 'Você so poderá escolher desafio nas proximas 5 rodadas'
d8 = 'Agora você tem poder, mande um dos jogadores fazer o que você quiser'

lista_v = [v1, v2, v3, v4, v5, v6, v7, v8]
lista_d = [d1, d2, d3, d4, d5, d6, d7, d8]

escolha=(input('Caso queira Verdade escreva (V),se quiser Desafio escreva (D): '))

random.shuffle(lista_v)
random.shuffle(lista_d)

print('')

if escolha != 'V' and 'D':
    print('Digite apenas V ou D')
else:

    if 'V' == escolha :
        print(lista_v[0])

    elif 'D' == escolha :
        print(lista_d[0])

