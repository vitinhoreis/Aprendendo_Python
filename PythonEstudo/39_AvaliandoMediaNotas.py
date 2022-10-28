"""Avaliando a média de notas"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m:.1f}')
if m >=6.0:
    print('Parabéns, sua média foi boa!')
else:
    print('Que pena, sua média foi ruim. Estude mais!')
