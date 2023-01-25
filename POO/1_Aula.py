import os
os.system('cls') or None

from pessoa import Pessoa
p1 = Pessoa()
p2 = Pessoa()

print(p1)
print(p2)

p1.nome = 'Luiz'
print(p1.nome)