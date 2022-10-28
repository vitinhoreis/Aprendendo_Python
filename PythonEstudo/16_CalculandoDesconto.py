"""Calculando desconto"""

n = float(input('Preço do produto: '))
nd = n-((n/100)*5)
print(f'Com o desconto de 5% o produto de R${n} sai por R${nd}')
