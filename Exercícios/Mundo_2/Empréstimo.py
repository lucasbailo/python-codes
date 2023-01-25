import os
os.system('cls') or None


valor = int(input('Digite o valor da casa: '))
salario = int(input('Digite o seu salário líquido: '))
anos = int(input('Em quantos anos você deseja pagar a casa? '))

part = salario * 0.3
valorano = valor / anos
valormes = valorano / 12

porc = ((valormes / salario))*100

print('')

print('''Seu salário é {}. Já o valor da casa é {}. Pagando em {} anos, seu valor por ano será {}.
Já o valor por mês será {:.2f}. O valor mensal não pode ultrapassar 30% do seu salário líquido!'''.format(salario,valor,anos,valorano,valormes))

print('')

if valormes >= part:
    print('''Infelizmente não podemos liberar o financiamento.  
    Pois o valor mensal corresponde a {:.2f} % do seu salário'''.format(porc))

else:
    print('Valor liberado!Pois o valor mensal corresponde a {:.2f} % do seu salário'.format(porc))
