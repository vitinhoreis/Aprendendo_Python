"""Usando a biblioteca 'math' para realizar operações de raiz quadrada"""

from math import sqrt, ceil, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raíz de {num} é igual a {raiz}')
print(f'A raíz de {num} é igual a {raiz:.2f}')
print(f'A raíz de {num} (arredondada para cima) é igual a {ceil(raiz)}')
print(f'A raíz de {num} (arredondada para baixo) é igual a {floor(raiz)}')

#ou
#import math
#num = int(input('Digite um número: '))
#raiz = math.sqrt(num)
#print(f'A raíz de {num} é igual a {raiz}')
#print(f'A raíz de {num} é igual a {raiz:.2f}')
#print(f'A raíz de {num} (arredondada para cima) é igual a {math.ceil(raiz)}')
#print(f'A raíz de {num} (arredondada para baixo) é igual a {mathfloor(raiz)}')