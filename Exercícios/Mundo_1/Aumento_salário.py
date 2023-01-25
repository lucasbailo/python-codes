import os

os.system('cls') or None

#Aqui eu montei como se até o desconto fosse uma variável que o usuário pode inserir

Atual = float(input('Digite o valor do salário atual sem desconto: ')) #Digitar o valor autal
Aumt = float(input('Digite a % de aumento no salário: ')) # Digitar a % de aumento

Porc = Aumt/100 # Aqui apenas deixa o valor em % (divide o valor inserido pelo usuário por 100)

Novo = Atual + (Atual*Porc) # Aqui calcula o valor final do salário com aumento!

print('') # Só para dar um espaçamento no código
print('O salário que era de {} reais, com {}% de aumento, fica {:.2f} reais'.format(Atual,Aumt,Novo))
