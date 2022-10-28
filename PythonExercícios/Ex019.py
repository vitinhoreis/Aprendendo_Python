''' um professor quer sortear um dos seus quatro alunos para apagar
    o quadro. Faça um programa que ajude ele, lendo o nome deles e
    escrevendo o nome do escolhido. '''

import random
pa = input('Primeiro aluno: ')
sa = input('Segundo aluno: ')
ta = input('Terceiro aluno: ')
qa = input('Quarto aluno: ')
li = [pa, sa, ta, qa]
es = random.choice(li)
print(f'O(a) aluno(a) escolhido foi {es}')