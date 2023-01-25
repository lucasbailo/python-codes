import os

os.system('cls') or None

class Teste:
    def __init__(self,nome,idade) -> None:
        self.nome = nome
        self.idade = idade
    def myTest(self):
        print('Olá, meu nome é ' + self.nome + ' e tenho ' + self.idade + ' anos!')

nomeidade =  Teste(input('Digite seu nome: '),input('Digite sua idade: '))
nomeidade.myTest()

class Teste2(Teste):
    def __init__(self, nome, idade, anoGrad) -> None:
        super().__init__(nome, idade)
        self.anoGrad = anoGrad
    
    def myTest2(self):
        print('Olá, meu nome é ' + self.nome + ' e tenho ' + self.idade + ' anos!'+' Me formei em ' + self.anoGrad)

nomeidade =  Teste2(input('Digite seu nome: '),input('Digite sua idade: '),input('Digite o ano de sua graduação: '))
nomeidade.myTest2()