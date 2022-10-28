"""Separando Unidade, Dezena, Centena e Milhar de um número"""

n1 = int(input('Digite um número de 0 a 9999: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print(f'O número digitado foi: {n1}')
print(f'Unidade : {u}')
print(f'Dezena  : {d}')
print(f'Centena : {c}')
print(f'Milhar  : {m}')