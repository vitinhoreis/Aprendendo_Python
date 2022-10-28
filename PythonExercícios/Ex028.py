''' Escreva um programa que faça o computador 'pensar' em um
    número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
    qual foi número escolhido pelo computador. O programa deverá
    escrever na tela se o usuário venceu ou perdeu. '''

from random import randint
import time
pc = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente advinhar...')
print('-=-' * 20)
player = int(input('Em que número eu pensei? ')) #Jogador tenta advinhar
print('PROCESSANDO...')
time.sleep(2)
if player == pc:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {pc} e não no {player}!')
