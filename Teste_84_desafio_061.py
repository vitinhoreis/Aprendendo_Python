''' Refaça o DESAFIO 051, lendo o primeiro termo de uma razão de uma PA,
    mostrando os 10 primeiros termos da progressão usando a estrutura while. '''

pt = int(input('Digite o primeiro termo de uma PA: '))
ra = int(input('Digite a razão dessa PA: '))

rb = ra
c = 0

while c < 10:
    c += 1
    pt = pt + ra
    pa = pt - ra
    print(pa)
