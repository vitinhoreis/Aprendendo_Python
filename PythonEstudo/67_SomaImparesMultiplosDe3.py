''' Faça um programa que calcule a soma entre todos os números impares
    que são múltiplos de três e que se encontram no intervalo de 1 até 500 '''

soma = 0
for c in range(1, 500 + 1):
    if c % 3 == 0 and c % 2 != 0:
        soma = soma + c
print(soma)
