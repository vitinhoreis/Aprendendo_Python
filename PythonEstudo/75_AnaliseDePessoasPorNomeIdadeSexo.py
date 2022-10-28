''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
    No final do programa, mostre:
    - A média de idade do grupo.
    - Qual é o nome do homem mais velho.
    - Quantas mulheres têm menos de 20 anos '''

somaidades = 0
hmm = 0
hmn = 0
mulheres = 0

for c in range(1, 5):
    nome = str(input(f'Digite o nome da {c}° pessoa: '))
    idade = int(input(f'Digite a idade da {c}° pessoa: '))
    sexo = str(input(f'Digite o sexo da {c}° pessoa: ')).upper().strip()
    print('-=' * 20)
    somaidades += idade
    media = somaidades / 4
    if sexo == 'MASCULINO':
        if c == 1:
            hmm = idade
            hmn = idade
            nomave = nome
        else:
            if idade > hmm:
                hmm = idade
                nomave = nome
            if idade < hmn:
                hmn = idade
    elif sexo == 'FEMININO':
        if idade < 20:
            mulheres = mulheres + 1
    else:
        print(f'{sexo} não é uma opção válida.')

print(f'A média de idade do grupo é de {media}.')
print(f'O homem mais velho é {nomave}.')
print(f'{mulheres} mulher(es)tem menos de 20 anos.')

