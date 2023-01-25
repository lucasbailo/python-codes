import os

os.system('cls') or None

Celsius = float(input('Digite o valor em graus Celsius: '))

Frt =  ((Celsius) * (9/5)) + 32 # Fómula que eu peguei do google (0 °C × 9/5) + 32 = 32F

print('') # Apenas para dar espaço
print('A temperatura {}°C equivale a {} Fahrenheit'.format(Celsius,Frt))