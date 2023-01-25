import os
from typing import List

os.system('cls') or None
print('')
print('Manipulação de Listas')
print('')


lista = ['carro' , 'lanchas' , 'moto' , 'jetski' , 'pedestres' , 'banhistas']

print(f'→ Lista Normal: {lista}')
print('')

lista.append('golf')
print(f'1) → lista.append("golf"): {lista}')
print('   • Serve para ADICIONAR algum item no final')
print('')

lista.insert(2,'Adicionei aqui')
print(f'2) → lista.insert(2,"Adicionei aqui"): {lista}')
print('   • Serve para ADICIONAR algum item na posição desejada, ele não vai substituir mas vai tomar o lugar do que ja estava sem remover.')
print('')

lista.pop(2)
print(f'3) → lista.pop(2): {lista}')
print('   • Serve para REMOVER algum item na posição desejada. Caso estiver sem referência dentro "lista.pop()", removerá o último.')
print('')

lista.remove('moto')
print(f'4) → lista.remove("moto"): {lista}')
print('   • Serve para REMOVER algum item pelo texto ou número EXATO como está na lista.')
print('')

lista.remove('jetski')
print(f'5) → lista.remove("moto"): {lista}')
print('   • Serve para REMOVER algum item pelo texto ou número EXATO como está na lista.')
print('')

intervalo = list(range(4,11))
print(f'6) → list(range(4,11)): {intervalo}')
print('   • Serve para CRIAR uma lista com o intervalo desejado.')
print('')

valores = [8,2,5,4,9,3,0]
valores.sort()
print(f'7) → valores = [8,2,5,4,9,3,0] → valores.sort(): {valores}')
print('   • Serve para ORDENAR os valores de uma lista do menor para o maior.')
print('')

valores = [8,2,5,4,9,3,0]
valores.sort(reverse=True)
print(f'8) → valores = [8,2,5,4,9,3,0] → valores.sort(reverse=True): {valores}')
print('   • Serve para INVERTER a ordenação dos valores de uma lista, do maior para o menor.')
print('')

contagem = len(valores)
print(f'9) → contagem = len(valores): {contagem}')
print('   • Serve para CONTAR a quantidade de valores de uma lista.')
print('')


