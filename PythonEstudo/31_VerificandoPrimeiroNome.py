"""Verifica o primeiro nome de uma cidade"""

nc = str(input('Digite o nome de uma cidade: '))
ns = nc.split()
ni = ns[0].upper()
nf = 'SANTO' in ni
print(f'O nome da cidade começa com "Santo": {nf}')
