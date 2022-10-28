''' Faça um programa que leia o ano de nascimento de um jovem e informe,
    de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
    se é a hora de se alistar ou se já passou do tempo de alistamento.
    Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. '''

from datetime import date

atual = date.today().year

nasc = int(input('Ano de nascimento: '))

idade = atual - nasc

print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')

elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} ans para o alistamento.')
    alistamento = atual + saldo
    print(f'Seu alistamento será em {alistamento}.')

elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    alistamento = atual - saldo
    print(f'Seu alistamento foi em {alistamento}.')