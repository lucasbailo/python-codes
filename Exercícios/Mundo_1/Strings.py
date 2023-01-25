import os

os.system('cls') or None

n = 'Curso em vídeo'
z = '           Removendo os espaços   ' 


print(n[::3])
n2 = n.capitalize()
print(n2)
n3 = n.title()
print(n.title())

print(z.strip())

# print('''Segurou segurou segurou

# Vou pedir a atenção de voces pra falar como cheguei até aqui
# bom foi entrar ruim vai ser pra sair
# eu vou mostrar para voces o que eu tive que ouvir

# Existe dois tipo de muié 
# aquela que é brava e aquela que nao te quer
# uma fala batido e a outra fala vai pra onde voce quiser

# um dia ela falou pra eu ir pra barretos
# eu respondi como é que é?
# mal sabia ela que eu ja iria sem ela souber

# A nativa falou que uns 10 ingressos iria arrumar
# assim eu e meus amigos vai pode falar que vai pescar

# Se eu for ela falou que vai esperar acordada
# hoje ja completa 3 dias que ela nao prega o zói por nada''')

print(n.split())
print(len(n))
print(n.replace('em','EM'))
print('Curso' in n)
print(n.find('em'))
print(n.lower())