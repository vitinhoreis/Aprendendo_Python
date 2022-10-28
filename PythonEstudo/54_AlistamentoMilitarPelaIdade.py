''' Faça um programa que leia o ano de nascimento de um jovem e informe,
    de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
    se é a hora de se alistar ou se já passou do tempo de alistamento.
    Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. '''

import datetime

an = int(input('Digite o ano de seu nascimento: '))  # Ano de nascimento

at = datetime.date.today().year  # Ano atual
id = at - an  # Idade do jovem

if id < 18:
    ida = 18 - id  # Idade atual
    print(f'Você está com {id - 1}-{id} anos, você deverá se alistar daqui a aproximadamente {ida} ano(s).')

elif id > 18:
    ida = id - 18
    print(f'Você está com {id - 1}-{id} anos, você ja passou da hora de se alistar em aproximadamente {ida} ano(s).')

elif id == 18:
    print(f'Você está com {id - 1}-{id} anos, já está na hora de se alistar.')