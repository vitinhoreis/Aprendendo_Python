''' Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. '''

n1 = float(input('Qual é o salário do Funcionário? R$'))
n2 = n1 + (n1 * 15 / 100)
n3 = (n1 / 100) * 15
print(f'15% de {n1} é igual {n3}')
print(f'Um funcionário que ganhava R${n1:.2f}, com 15% de aumento, passa a receber R%{n2:.2f}.')