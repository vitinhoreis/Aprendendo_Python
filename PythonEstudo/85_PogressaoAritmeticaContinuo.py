''' Melhore o DESAFIO 061, perguntando se ele quer mostrar mais alguns termos.
    O programa encerra quando ele disser que quer mostrar 0 termos. '''

pt = int(input('Digite o primeiro termo de uma PA: '))
ra = int(input('Digite a razão dessa PA: '))

c = 0
add = 10

while c < add:
    c += 1
    pt = pt + ra
    pa = pt - ra
    print(pa)
    apa = str(input('Deseja continuar? [S/N]')).upper()
    if apa == 'S':
        nte = int(input('Digite quantos termos quer adicionar: '))
        add = add + nte