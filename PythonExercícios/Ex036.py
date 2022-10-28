''' Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
    O programa vai perguntar o valor da casa, o salário do comprador e em quantos
    anos ele vai pagar.
    Calcule o valor da prestação mensal. Sabendo que ela não pode exceder 30% do
    salário ou então o empréstimo será negado. '''

print('-=' * 20)
casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
print('-=' * 20)

prestação = casa / (anos * 12)
mínimo = salário * 30 / 100

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos,', end = ' ')
print(f'a prestação será de R${prestação:.2f}.')

if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
