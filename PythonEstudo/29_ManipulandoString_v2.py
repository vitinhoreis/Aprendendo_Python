"""Manipulando String com a frase digitada pelo usuário"""

n0 = input('Digite o seu nome completo: ')
n1 = n0.strip()
n2 = n1.upper()
print(f'O nome totalmente em maiúsculo: {n2}')
n3 = n1.lower()
print(f'O nome totalmente em minúsculo: {n3}')
n4 = len(n1)-n1.count(' ')
print(f'Seu nome tem ao todo {n4} letras.')
n5 = n1.split()[0]
n6 = len(n5)
print(f'Seu primeiro nome tem {n6} letras')