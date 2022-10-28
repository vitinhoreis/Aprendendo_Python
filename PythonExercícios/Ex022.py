''' Crie um programa que leia o nome completo de uma pessoa e mostre:
    - O nome com todas as letras maiúsculas e minúsculas.
    - Quantas letras ao todo(sem considerar espaços)
    - Quantas letras tem o primeiro nome. '''

n = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {n.upper()}.')
print(f'Seu nome em minúsculas é {n.lower()}.')
c = len(n) - n.count(' ')
print(f'Seu nome tem ao todo {c}.')
p = n.split()[0]
l = len(p)
print(f'Seu primeiro nome é {p} e ele tem {l} letras.')