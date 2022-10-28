''' Faça um programa que leia um ângulo qualquer e
    mostre na tela o valor do seno, cosseno e
    tangente desse ângulo. '''

from math import sin, cos, tan, radians
ag = float(input('Digite o ângulo que você deseja: '))
se = sin(radians(ag))
co = cos(radians(ag))
ta = tan(radians(ag))
print(f'O ângulo de {ag}° tem o SENO de {se:.2f}. ')
print(f'O ângulo de {ag}° tem o COSSENO de {co:.2f}.')
print(f'O ângulo de {ag}° tem a TANGENTE de {ta:.2f}.')
