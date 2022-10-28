''' Estrutura condicional aninhada. '''

n = str(input('Qual é o seu nome? ')).capitalize()
nome = n.upper()
if nome == 'VITOR':
    print('Que nome bonito você tem!')
elif nome == 'PEDRO' or nome == 'MARIA' or nome == 'LUIZA' or nome == 'JOÃO':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'ANA CLÁUDIA JÉSSICA JULIANA':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal')
print(f'Tenha um bom dia, {n}.')