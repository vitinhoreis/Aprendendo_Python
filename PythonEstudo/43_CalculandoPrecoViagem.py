"""Calculando o preço de uma viagem usando como parâmetro a distância em Km"""

d = float(input('Qual a distância em (Km) da viagem? '))
if d <=200:
    print('Para viagens de até 200Km, o preço é de R$0,50 por Km.')
    print(f'O total a pagar é R${d * 0.50}')
else:
    print('Para viagens de mais de 200Km, o preço é de R$0,45 por Km.')
    print(f'O total a pagar é R${d * 0.45}')