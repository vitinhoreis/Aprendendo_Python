''' Refaça o desafio 009, mostrando a tabuada de um número
    que o usuário escolher, só que agora utilizando um laço for. '''

num = int(input('Digite um número para ver sua tabuada: '))

for c in range(0, 10+1):
    print(f'{num} x {c} = {num * c}')