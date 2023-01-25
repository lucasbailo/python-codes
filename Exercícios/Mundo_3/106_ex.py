from ast import fix_missing_locations
import os

os.system('cls') or None

c = ('\033[m',           #0 - sem cor
     '\033[0;30;41m',    #1 - vermelho
     '\033[0;30;42m',    #2 - verde
     '\033[0;30;43m',    #3 - amarelo
     '\033[0;30;44m',    #4 - azul
     '\033[0;30;45m',    #5 - roxo
     '\033[0;30'         #6 - branco
    );

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',4)
    print(c[6],end='')
    help(com) 

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f' {msg} ')
    print('~' * tam)
    print(c[0], end='')

# PROGRAMA PRINCIPAL

comando = ' '
while True:
    titulo('SISTEMA DE AJUDA PY HELP',2)
    comando = str(input('Funcão ou Biblioteca? ["FIM" = break]:  ')).strip()
    if comando.upper() == 'FIM':
        print()
        print('Fim do programa!')
        print()
        break
    else:
        ajuda(comando)

print()
titulo('ATÉ LOGO', 1)