''' Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um
    número de 0 a 10. Só que agora o jogador vai tentar advinhar até acertar,
    mostrando no final quantos palpites foram necessários para vencer. '''

import random

jo = int(input('Digite um valor de 0 a 5: '))
pc = random.randint(0, 5)
con = 0

while jo != pc:
    pc = random.randint(0, 5)
    jo = int(input('O valor digitado está errado,tente novamente: '))
    con = con + 1

if jo == pc:
    print(f'Você venceu, foram necessárias {con + 1} tentativas.')