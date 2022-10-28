''' Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
    e mostre quantos Doláres ela pode comprar.
    Considere US$1,00 = R$3,27 '''

r = float(input('Quanto dinheiro você tem na carteira? R$'))
d = r/3.27
print(f'Com R${r:.2f} você pode comprar U${d:.2f}.')
