''' Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada. '''

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print(f'O dobro de {n} é igual a {d}.')
print(f'O triplo de {n} é igual a {t}.')
print(f'A raíz quadrada de {n} é igual a {r:.2f}.')


#ou
#import math
#n = int(input('Digite um número: '))
#d = n*2
#t = n*3
#r = math.sqrt(n)
#print(f'O dobro de {n} é igual a {d}.')
#print(f'O triplo de {n} é igual a {t}.')
#print(f'A raíz quadrada de {n} é igual a {r:.2f}.')
