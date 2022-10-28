''' Escreva um programa que leia a velocidade de um carro.
    Se ele ultrapassar 80Km/h, mostre uma mensagem
    dizendo que ele foi multado.
    A multa vai custar R$7,00 por cada Km acima do limite. '''

vc = float(input('Qual a velocidade atual do carro? '))
if vc > 80:
    m = (vc - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h.')
    print(f'Você deve pagar uma multa de R${m:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')