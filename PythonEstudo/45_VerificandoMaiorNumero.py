"""Verificando qual é o maior número"""

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))
if n1 > n2 > n3:
    print(f'Dentre os números digitados o Maior é {n1}')
elif n1 < n2 and n1 > n3:
    print(f'Dentre os números digitados o Maior é {n2}')
elif n1 < n3 and n1 > n2:
    print(f'Dentre os números digitados o Maior é {n3}')