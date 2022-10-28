"""Colorindo as impressões"""

print('\033[7;33;44mOlá Mundo!\033[m')

cores = {'limpa':'\033[m', 'azul':'\033[34m'}#Dicionário

print('Hello {} World'.format(cores['azul']))

print(f'{cores["azul"]} Olá Mundo {cores["limpa"]}')

