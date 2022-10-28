''' Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. '''

import math
n1 = float(input('Digite um valor: '))
n2 = math.trunc(n1)
print(f'O valor digitado foi {n1} e a sua porção inteira é {n2}.')

#ou
#n = float(input('Digite um valor: '))
#print(f'O valor digitado foi {n1} e a sua porção inteira é {int(n1)}')
