"""Verifica a velocidade do carro e caso esteja acima da velocidade permitida calcula a multa"""

vc = float(input('Digite a velocidade do carro em Km/h: '))
if vc <=80:
    print('Você está dentro do limite de velocidade (80Km/h). Contiue assim!')
else:
    m1 = vc - 80
    m2 = m1 * 7
    print('Você está acima do limite de velocidade!')
    print('Terá que pagar R$7.00 por cada Km acima do limite.')
    print(f'Total de multa a pagar R${m2}')