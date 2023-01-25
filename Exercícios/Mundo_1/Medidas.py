import os

os.system('cls') or None

medida = float(input('Digite uma distância em metros: '))
cm = medida*100
mm = medida*1000

print('A medida {} metros corresponde a {} centímetros e {} milimetros'.format(medida, cm, mm))