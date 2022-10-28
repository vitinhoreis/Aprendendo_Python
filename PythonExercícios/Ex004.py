''' Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informaççoes possíveis sobre ele '''

a = input('Digite algo: ')
b = type(a)
c = a.isspace()
d = a.isnumeric()
e = a.isalpha()
f = a.isalnum()
g = a.isupper()
h = a.islower()
print(f'O tipo primitivo desse valor é: {b}')
print(f'Só tem espaços? {c}')
print(f'É um número? {d}')
print(f'É alfabético? {e}')
print(f'É alfanumérico? {f}')
print(f'Está em maiúsculo? {g}')
print(f'Está em minúsculo? {h}')
