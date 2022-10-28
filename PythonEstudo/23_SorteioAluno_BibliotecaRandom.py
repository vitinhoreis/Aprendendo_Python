"""Escolhendo um aluno aleatório com o método 'choice' da biblioteca 'random' """

import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quinto aluno: ')
lista = [a1, a2, a3, a4]
s = random.choice(lista)
print(f'O aluno escolhido foi {s}')
