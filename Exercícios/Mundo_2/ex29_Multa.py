import os
from random import randrange

os.system('cls') or None

v = int(input('Informe a velocidade (em Km/h) que você passou no radar: '))

lim = 80 # Limite de velocidade estabelecido em 80km/k
u = (v-lim)  # Cálculo da qtd de Km/h que ele estava acima
m = u*7 # Cálculo do valor da multa

if v <= lim:
    print('Você estava dentro do limite de velocidade! Não será multado.')
else:
    print('Você estava {} Km/h acima do limite de velocidade. Sua multa será de R$ {:.2f}'.format(u,m))