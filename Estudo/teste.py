import os

os.system('cls') or None

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    def myFunc(self):
        print('Olá meu nome é '+ self.nome +' e tenho '+self.idade+' anos!')

p1 = Pessoa(input('Digite o nome: '),input('Digite a idade: '))
p1.myFunc()