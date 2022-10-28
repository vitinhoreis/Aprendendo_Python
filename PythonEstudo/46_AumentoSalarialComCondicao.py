"""Aumento salarial de acordo com o salário atual"""

sa = float(input('Digite o valor do salário do funcionário: R$'))
if sa <= 1250:
    as1 = sa + (sa / 100 * 15)
    print(f'O aumento será de 15%, o salário será de R${as1:.2f}')
else:
    as2 = sa + (sa / 100 * 10)
    print(f'O aumento será de 10%, o salário será de R${as2:.2f}')