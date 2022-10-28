"""O laço será executado enquanto o usuário inserir 'S', para continuar """

r = 'S'

while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')