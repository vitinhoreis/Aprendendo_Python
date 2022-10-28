''' Faça um programa que leia uma frase pelo teclado e mostre:
    - Quantas vezes aparece a letra 'A'.
    - Em que posição ela aparece pela primeira vez.
    - Em que posição ela aparece a última vez. '''

frase = str(input('Digite uma frase: ')).strip().upper()
q1 = frase.count('A')
print(f'A letra A aparece {q1} vezes na frase.')
q2 = frase.find('A')+1
print(f'A primeira letra A apareceu na posição {q2}')
q3 = frase.rfind('A')+1
print(f'A última letra A apareceu na posição {q3}')
