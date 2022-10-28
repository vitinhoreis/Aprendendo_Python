''' Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. '''

n = float(input('Qual o preço do produto? R$'))
d = n - ((n / 100) * 5)
print(f'O produto que custava R${n:.2f}, na promoção com desconto de 5% vai custar R${d:.2f}.')

#ou

#n = float(input('Qual o preço do produto? R$'))
#d = n - (n * 5 / 100)
#print(f'O produto que custava R${n:.2f}, na promoção com desconto de 5% vai custar R${d:.2f}.')