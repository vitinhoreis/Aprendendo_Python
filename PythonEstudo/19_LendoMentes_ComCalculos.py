"""Descobrindo o número escolhido pelo usuário através de cálculos"""

import random
n1 = random.randint(1, 10)
n2 = random.randint(1, 10)
n3 = random.randint(1, 5)
n4 = random.randint(1, 10)
s1 = n1+n2
s2 = s1-n3
s3 = s2*2
s4 = s3+n4

print('Pense e escolha um número de 1 a 10. Apenas mentalize-o, não o digite.')
r1 = str(input('Pronto? Caso afirmativo, digite "s" = '))
print(f'Some com o número que você pensou {n1}.')
r2 = str(input('Pronto? Caso afirmativo, digite "s" = '))
print(f'Some agora mais {n2}.')
r3 = str(input('Pronto? Caso afirmativo, digite "s" = '))
print(f'Subtraia {n3}.')
r4 = str(input('Pronto? Caso afirmativo, digite "s" = '))
print('Agora retire o número que você pensou primeiro.')
r5 = str(input('Pronto? Caso afirmativo, digite "s" = '))
print('Multiplique o resto por 2.')
r6 = str(input('Pronto? Caso afirmativo, digite "s" = '))
print(f'Some mais {n4}.')
r7 = str(input('Pronto? Caso afirmativo, digite "s" = '))
print(f'O resultado é: {s4}')
