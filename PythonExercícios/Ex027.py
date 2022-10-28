''' Faça um programa que leia o nome completo de uma pessoa,
    mostrando em seguida o primeiro e o último nome separadamente.
    Ex: Ana Maria de Souza
    primeiro = Ana
    último = Souza '''

nome = str(input('Digite seu nome completo: ')).strip()
print('Muito prazer em te conhercer!')
ns = nome.split()
print(f'Seu primeiro nome é {ns[0]}')
nu = ns[len(ns)-1]
print(f'Seu último nome é {nu}')