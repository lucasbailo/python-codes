import os

os.system('cls') or None

dist = int(input('Digite a distância da viagem em Km/h (apenas números): '))

aduz = dist * (0.5) # Cálculo do preço até duzentos Km
mduz = dist * (0.45) # Cálculo do preço para viagens maiores que duzentos Km

if dist <= 200:
    print('O valor da passagem é de R$ {:.2f}'.format(aduz))
else:
    print('O valor da passagem é de R$ {:.2f}'.format(mduz))