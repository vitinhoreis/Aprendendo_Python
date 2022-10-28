''' Desenvolva um programa que pergunte a distância de uma viagem
    em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
    viagens de até 200Km e R$0,45 para viagens mais longas. '''

d = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {d}Km.')
if d <= 200:
    p1 = d * 0.50
    print(f'E o preço da sua passagem será de R${p1:.2f}.')
else:
    p2 = d * 0.45
    print(f'E o preço da sua passagem será de R${p2:.2f}.')