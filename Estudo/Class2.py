import os

os.system('cls') or None

class Teste:
    def __init__(self,nome,idade) -> None:
        self.nome = input('Digite seu nome: ')
        self.idade = input('Digite sua idade: ')
    def myTest(self):
        print('Olá, meu nome é ' + self.nome + ' e tenho ' + self.idade + ' anos!')

nomeidade =  Teste(self.nome,self.idade)
nomeidade.myTest()