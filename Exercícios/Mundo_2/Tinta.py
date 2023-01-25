import os

os.system('cls') or None

a2 = float(input('Informe a altura da parede em metros: '))
c2 = float(input('Informe a largura da parede em metros: '))

m2 = a2 * c2 #aqui é o cálculo da metragem cúbica da parede (base x altura)

tt = m2 / 2 #aqui é o cálculo para informar quanto de tinta será usado
print('')
print('Uma parede de {} metros de altura e {} metros de largura, tem {} metros quadrados, e precisará de {} litros de tinta'.format(a2,c2,m2,tt))


