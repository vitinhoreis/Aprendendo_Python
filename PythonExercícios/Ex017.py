''' Faça um programa que leia o comprimento do
    cateto oposto e do cateto adjacente de um
    triângulo retângulo, calcule e mostre o
    comprimento da hipotenusa. '''

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f} ')

#ou

#import math
#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#h1 = (co * co) + (ca * ca)
#h2 = math.sqrt(h1)
#print(f'A hipotenusa vai medir {h2:.2f}')

#ou

#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print(f'A hipotenusa vai medir {hi:.2f}')



