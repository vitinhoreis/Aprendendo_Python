''' Escreve um programa que pergunte o salário de um funcionário e
    calcule o valor do seu aumento.
    Para salários superiores a R$1.250,00, calcule um aumento de 10%.
    Para os inferiores ou iguais, o aumento é de 15%. '''

s = float(input('Qual é o salário atual do funcionário? R$'))
if s > 1250:
    ns = s + (s / 100) * 10
    print(f'Quem ganhava R${s:.2f} passa a ganhar R${ns:.2f} agora.')
else:
    ns = s + (s / 100) * 15
    print(f'Quem ganhava R${s:.2f} passa a ganhar R${ns:.2f} agora.')