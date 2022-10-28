'''' Crie um pograma que leia dois valores e mostre um menu na tela:
    [1] somar
    [2] multiplicar
    [3] qual é maior
    [4] novos números (trocar os números)
    [5] sair do programa
    Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segunto valor: '))

opção = 0

while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')

    opção = int(input('>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
    elif opção == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é {produto}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)

print('Fim do programa! Volte sempre!')