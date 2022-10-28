''' Escreva um programa que leia dois números inteiros e compare-os
    mostrando na tela uma mensagem:
    - O primeiro valor é maior.
    - O segundo valor é maior.
    - Não existe valor maior, os dois são iguais. '''

fn = float(input('Primeiro número: '))
sn = float(input('Segundo número: '))
if fn > sn:
    print('O PRIMEIRO número é maior.')
elif sn > fn:
    print('O SEGUNDO número é maior.')
elif fn == sn:
    print('Os dois números são IGUAiS.')