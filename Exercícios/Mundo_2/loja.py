import os

os.system('cls') or None

val = int(input('Digite o valor da compra: '))

print('')

print('''Escolha como você irá pagar:

[1] A vista débito / cheque
[2] Crédito 1x
[3] Crédito 2x
[4] Crédito 3x ou mais''')

print('')

tipo = int(input('Escolha a forma de pagamento citada acima: '))

print('')

juros = 0.03
juros3 = 0.045

if tipo == 1 or tipo == 2:
    print('O valor da compra é {:.2f} reais'.format(val))
elif tipo == 3:    
    print('O valor da compra que era de {} será de {} reais, pois os juros são de {}%'.format(val,((juros+1)*val),(juros*100)))
else:
    pc = int(input('Quantas parcelas? '))
    print('O valor da compra que era de {} reais, será de {:.2f} reais, pois os juros são de {}%'.format(val,(((juros3*pc)+1)*val),(juros3*100)))

print('')