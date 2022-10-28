''' Escreva um programa que leia um número inteiro qualquer
    e peça para o usuário escolher qual será a base de conversão:
    - 1 para binário
    - 2 para octal
    - 3 para hexadecimal '''

ni = int(input('Digite um número inteiro: '))
co = int(input('Qual será a base de conversão? Digite (1) para binário, (2) para octal e (3) para hexadecimal: '))
if co == 1:
    print(f'{ni} Convertido para BINÁRIO é igual a {bin(ni)[2:]}')
elif co == 2:
    print(f'{ni} Convertido para OCTAL é igual a {oct(ni)[2:]}')
elif co == 3:
    print(f'{ni} Convertido para HEXADECIMAL é igual a {hex(ni)[2:]}')
else:
    print('Opção inválida. Tente novamente.')