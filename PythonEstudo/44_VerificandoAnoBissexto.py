"""Verificando se é um ano bissexto"""

ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    #ano % 100>0
    #ano % 400 == 0
    print('É um ano Bissexto!')
else:
    print('Não é um ano Bissexto!')