''' Elabore um programa que calcule o valor a ser pago por um produto,
    considerando o seu preço normal e condição de pagamento:
    - à vista dinheiro/cheque  : 10% de desconto
    - à vista no cartão       : 5% de desconto
    - em até 2x no cartão: preço normal
    - 3x ou mais no cartão: 20% de juros  '''

print('====== LOJAS REIS ======')

pc = float(input('Preço das compras: R$'))  # Preço das compras

print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão''')

op = int(input('Qual é a opção? '))  # Opção de pagamento

if op == 1:
    tp = pc - (pc * 10 / 100) # Total à pagar, diminuindo 10% do valor das compras
    print('Desconto de 10% no total, para pagamentos à vista dinheiro/cheque. ')
    print(f'Total à pagar: R${tp:.2f}')

elif op == 2:
    tp = pc - (pc * 5 / 100)  # Total à pagar, diminuindo 5% o valor das compras
    print('Desconto de 5% no total, para pagamentos à vista no cartão.')
    print(f'Total à pagar: R${tp:.2f}')

elif op == 3:
    print(f'Total à pagar: R${pc:.2f}')

elif op == 4:
    tp = pc + (pc * 20 / 100)
    print('Juros de 20% no total, para pagamentos em 3x ou mais no cartão.')
    print(f'Total à pagar: R${tp:.2f}')