''' Refaça o desafio 035 dos triângulos, acrescentando o recurso de
    mostrar que tipo de triângulo será formado:
    - Equilátero: todos os lados iguais
    - Isósceles: dois lados iguais
    - Escaleno: todos os lados diferentes '''

r1 = int(input('Primeira reta: '))
r2 = int(input('Segunda reta: '))
r3 = int(input('Terceira reta: '))

#if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
   # print('Podem formar um triângulo.')

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1 and r1 == r2 == r3:
    print('Podem formar um Triângulo Equilátero.')

elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1 and (r1 == r2 or r1 == r3 or r2 == r3):
    print('Podem formar um Triângulo Isóceles.')

elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1 and (r1 != r2 or r1 != r3 or r2 != r3):
    print('Podem formar um Triângulo Escaleno.')

else:
    print('Não podem formar um triângulo.')

