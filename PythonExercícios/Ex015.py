''' Escreva um programa que pergunte a quantidade de Km
    percorridos por um carro alugado e a quantidade de dias pelos
    quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
    custa R$60 por dia e R$0,15 por Km rodado. '''

d = int(input('Quantos dias alugados? '))
k = float(input('Quantos Km rodados? '))
p = (d * 60) + (k * 0.15)
print(f'O total a pagar é de R${p:.2f} ')


#qd = int(input('Quantos dias o carro foi alugado? '))
#qk = float(input('Quantos Km percorridos? '))
#pd = qd * 60
#pk = qk * 0.15
#tp = pd + pk
#print(f'O total a pagar é de R${tp:.2f}.')