''' Faça um prgrama que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
    Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

s = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]

while s != 'F' and s != 'M':
    s = str(input('Dados inválidos. Pro favor, informe seu sexo: ')).upper()

print(f'Sexo {s} registrado com sucesso!')
