''' Crie um pograma que leia dois valores e mostre um menu na tela:
    [1] somar
    [2] multiplicar
    [3] qual é maior
    [4] novos números (trocar os números)
    [5] sair do programa
    Seu programa deverá realizar a operação solicitada em cada caso.'''

print('Digite dois números e escolha a opção que deseja..')

n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))

print('''Opções:
[1] somar
[2] multiplicar
[3] qual é maior
[4] novos números (trocar os números)
[5] sair do programa''')

escolha = int(input('Digite sua opção: '))

while escolha != 5:
    if escolha == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    elif escolha == 2:
        multi = n1 * n2
        print(f'{n1} x {n2} = {multi}')
    elif escolha == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}.')
        elif n1 == n2:
            print(f'{n1} é igual a {n2}.')
        else:
            print(f'{n2} é maior que {n1}.')
    elif escolha == 4:
        print('Escolha novos números:')
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))

    #print('''Opções:
    #[1] somar
    #[2] multiplicar
    #[3] qual é maior
    #[4] novos números (trocar os números)
    #[5] sair do programa''')

    escolha = int(input('Digite sua opção: '))

print('Fim')