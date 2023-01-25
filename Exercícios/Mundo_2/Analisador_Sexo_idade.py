import os
os.system('cls') or None

somaidade = 0 # Acumulador de idade
contador = 0 # Contador de nomes e idades, assim eu posso deixar móvel sem ficar alterando na fórmula da média
homemmaioridade = 0 # Acumulador do mais velho
nomehomemmaisvelho = '' # Acumulador de nome do mais velho
qtdmulher20 = 0 # Acumulador qtd de mulheres com menos de 20 anos
mulhergeral = 0 # Acumuldor de mulheres todas idades


for x in range(1,6):
    print('='*12,'{}ª PESSOA'.format(x),'='*12)
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    # Cálculo média
    
    somaidade += idade
    contador += 1
    media = somaidade / contador # Fórmula da média

    # Cálculo do nome e da idade do homem mais velho
    if x == 1 and sexo == 'M':
        homemmaioridade = idade
        nomehomemmaisvelho = nome
    else:
        if sexo == 'M' and idade > homemmaioridade:
            homemmaioridade = idade
            nomehomemmaisvelho = nome

    # Cálculo qtd de mulheres com mais de 20 anos

    if sexo == 'F' and idade < 20:
        qtdmulher20 += 1
    else:
        qtdmulher20 += 0
    
    # Cálculo qtd de mulheres de todas as idades
    if sexo == 'F':
        mulhergeral += 1
    else:
        mulhergeral += 0

print('')
print('> A média de idade do grupo é {:.2f}'.format(media))
print('> O homem mais velho do grupo é {} e tem {} anos'.format(nomehomemmaisvelho,homemmaioridade))
print('> A quantidade de mulheres é {} porém apenas {} tem menos de 20 anos'.format(mulhergeral,qtdmulher20))
print('')
    




