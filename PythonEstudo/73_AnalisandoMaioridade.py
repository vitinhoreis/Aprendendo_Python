''' Crie um programa que leia o ano de nascimento de sete pessoas.
    No final, mostre quantas pessoas ainda não atingiram a maioridade
    e quantas já são maiores. '''

from datetime import date

print('Digite o ano de nascimento de 7 pessoas.')

maiores = 0
menores = 0

for c in range(1, 8):
    nascimento = int(input(f'{c}° pessoa: '))
    atual = date.today().year
    idade = atual - nascimento
    print(f'Quem nasceu em {nascimento} tem {idade} anos.')
    if idade >= 21:  # considerado 21 anos como maior idade
        maiores = maiores + 1
    else:
        menores = menores + 1

print(f'{maiores} são maiores de idade e {menores} são menores de idade.')
