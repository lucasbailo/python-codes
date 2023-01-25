import os

os.system('cls') or None

class Sequencia:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myClass = Sequencia()
myIter = iter(myClass)

for x in myIter:
    if x <= 20:
        print(x)
    else:
        raise StopIteration

