''' Escreva um programa que leia um número inteiro qualquer
    e peça para o usuário escolher qual será a base de conversão:
    - 1 para binário
    - 2 para octal
    - 3 para hexadecimal '''

num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL ''')

opção = int(input('Sua opção: '))

if opção == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')

elif opção == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')

elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')

else:
    print('Opção inválida. Tente novamente.')