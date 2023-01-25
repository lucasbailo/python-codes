import os
os.system('cls') or None

sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
print(sexo)

while sexo not in 'FfMm':
    sexo = str(input('Dados inválidos! Digite seu sexo [M/F]: ')).strip().upper()[0]