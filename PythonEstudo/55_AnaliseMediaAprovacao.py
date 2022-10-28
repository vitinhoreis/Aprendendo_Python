''' Crie um programa que leia duas notas de um aluno e calcule sua média,
    mostrando uma mensagem no final, de acordo com a média atingida:
    - Média abaixo de 5.0: REPROVADO
    - Média entre 5.0 e 6.9: RECUPERAÇÃO
    - Média 7.0 ou superior: APROVADO '''

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

m = (n1 + n2) / 2

if m < 5.0:
    print(f'Sua média foi {m}, você foi reprovado!')

elif m >= 5.0 and m < 7:
    print(f'Sua média foi {m}, você está de recuperação!')

elif m >= 7 and m <= 10:
    print(f'Sua média foi {m}, Você foi aprovado!')