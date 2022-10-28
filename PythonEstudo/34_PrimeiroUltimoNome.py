"""Descobrindo o primeiro e último nome"""

n = str(input('Digite um nome: '))
s1 = n.strip()
s2 = n.split()
s3 = s2[0]
print(f'Primeiro nome: {s3}')
u = s2[len(s2)-1]
print(f'Último nome: {u}')