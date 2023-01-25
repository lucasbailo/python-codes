import os

os.system('cls') or None

peso = float(input('Digite seu peso em kilogramas: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / (pow(altura,2)) # IMC = peso / (altura²)

ab = 18.5 # abaixo do peso
pi = 25 # peso ideal
sp = 30 # sobrepeso
om = 40 # obesidade até 40, se maior = obesidade mórbida

print('')
print('Seu IMC é: {:.2f}'.format(imc))
print('')

if imc <= ab:
    print('Você está abaixo do peso')
elif imc <= pi:
    print('Você está no peso ideal!')
elif imc <= sp:
    print('Você está com sobrepeso!')
elif imc <= om:
    print('Você está com obesidade')
elif imc > om:
    print('Você está com obesidade mórbida')





