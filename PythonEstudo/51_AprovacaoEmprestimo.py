''' Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
    O programa vai perguntar o valor da casa, o salário do comprador e em quantos
    anos ele vai pagar.
    Calcule o valor da prestação mensal. Sabendo que ela não pode exceder 30% do
    salário ou então o empréstimo será negado. '''

print('-=' * 20)
vc = float(input('Digite o valor da casa: R$'))
sa = float(input('Digite o seu salário: R$'))
ap = float(input('Digite em quantos anos será pago: '))
print('-=' * 20)

me = ap * 12         # anos vezes 12 = meses
pm = vc / me         # valor da casa dividido pelos meses, resultando nas parcelas mensais
print(f'As parcelas serão de R${pm:.2f}.')
ps = sa / 100 * 30   # 30% do salário do comprador

if pm < ps:
    print('A compra está aprovada!')
else:
    print('A compra foi negada!')