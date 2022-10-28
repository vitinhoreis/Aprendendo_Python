''' Crie um programa que faça o
    computador jogar Jokenpô com você. '''

import random
import time

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))

tu = ('PEDRA', 'PAPEL', 'TESOURA')
pc = random.randint(0, 2)

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ')

print('-=' * 15)

print(f'Computador jogou {tu[pc]}')
print(f'Jogador jogou {tu[jogador]}')

print('-=' * 15)

if jogador == pc:
    print(f'EMPATE')

elif jogador == 0 and pc == 2 or jogador == 1 and pc == 0 or jogador == 2 and pc == 1:
    print('Jogador VENCEU!')

elif jogador == 0 and pc == 1 or jogador == 1 and pc == 2 or jogador == 2 and pc == 0:
    print('Computador VENCEU!')




