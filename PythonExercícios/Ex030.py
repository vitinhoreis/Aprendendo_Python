''' Crie um programa que leia um número inteiro
    e mostre na tela se ele é PAR ou ÍMPAR. '''

n1 = int(input('Me diga um número qualquer: '))
if n1 % 2 == 0:
    print(f'O número {n1} é PAR.')
else:
    print(f'O número {n1} é ÍMPAR.')