"""Somando dois números e fazendo a impressão do resultado usando o 'format'"""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1+n2
#print('A soma entre', n1, 'e', n2, 'vale', s)
print('A soma entre {} e {} vale {}'.format(n1, n2, s))