import os

os.system('cls') or None

Dias = int(input('Digite a quantidade de dias que o carro foi alugado: ')) # Qtd de dias
Km = float(input('Digite a quantidade de Kilômetros rodados: ')) # Qtd de Km

Vd = Dias * 60 # Valor por dias
VKm = Km * 0.15 # Valor por Km rodado

VT = Vd + VKm # Valor total

print('') # Apenas para dar espaçamento no código
print('O valor por {} dias é {} reais. O valor por {} kilômetros é de {} reias. Sendo assim, o total a pagar é {} reais'.format(Dias,Vd,Km,VKm,VT))