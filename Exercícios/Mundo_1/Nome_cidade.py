import os

os.system('cls') or None

cid = str(input('Digite o nome da sua cidade: ')).strip().title()

check = cid[:5]
var = str('Santo')

if check == var:
    print('Começa com "Santo"')
else:
    print('Não começa com "Santo"')