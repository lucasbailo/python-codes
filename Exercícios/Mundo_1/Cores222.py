import os
os.system('cls') or None

from colorama import Fore, Back, Style, init, deinit
 
frente = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
fundo = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]
init()
for cor_frente in frente:
    for cor_fundo in fundo:
        print(cor_frente + cor_fundo + "AMADOR PROGRAMA", end = "")
print(Style.RESET_ALL) 
deinit()