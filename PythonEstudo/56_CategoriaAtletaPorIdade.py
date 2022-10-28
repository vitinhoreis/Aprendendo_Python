''' A Confederação Nacional de Natação precisa de um programa
    que leia o ano de nascimento de um atleta
    e mostre sua categoria, de acordo com a idade:
    - Até 9 anos : MIRIM             - Até 25 anos: SÊNIOR
    - Até 14 anos: INFANTIL          - Acima: MASTER
    - Até 19 anos: JUNIOR                         '''

import datetime
an = int(input('Digite o ano de nascimento do atleta: '))  # Ano de nacimento

at = datetime.date.today().year  # Ano Atual
id = at - an  # Idade do atleta

if id <= 9:
    print(f'Com {id} anos, atleta na categoria: MIRIM.')

elif id > 9 and id <= 14:
    print(f'Com {id} anos, atleta na categoria: INFANTIL.')

elif id > 14 and id <= 19:
    print(f'Com {id} anos, atleta na categoria: JUNIOR.')

elif id > 19 and id <= 25:
    print(f'Com {id} anos, atleta na categoria: SÊNIOR.')

else:
    print(f'Com {id} anos, atleta na categoria: MASTER.')


