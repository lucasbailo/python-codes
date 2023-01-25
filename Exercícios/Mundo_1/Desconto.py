import os

os.system('cls') or None

# Aqui eu criei até um input para o usuário preencher qual é o valor do desconto, assim o desconto não fica fixo.

re = float(input('Digite o valor do produto sem desconto: ')) #Digitar o valor real
desc = float(input('Digite a % de desconto: ')) # Digitar a % de desconto

porc = desc/100 # Aqui apenas deixa o valor em % (divide o valor inserido pelo usuário por 100)

atual = re - (re*porc) # Aqui calcula o valor final do produto com o desconto!

print('')
print('O valor do produto que era de {} reais, com {}% de desconto, fica {:.2f} reais'.format(re,desc,atual))
