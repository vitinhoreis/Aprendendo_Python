"""Embaralhando uma lista de nomes usando o método 'shuffle' da biblioteca 'random' """

import random
a1 = input('Nome do(a) aluno(a): ')
a2 = input('Nome do(a) aluno(a): ')
a3 = input('Nome do(a) aluno(a): ')
a4 = input('Nome do(a) aluno(a): ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print(f'{lista}')
