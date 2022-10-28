''' Escreva um programa que leia um valor em metros e o exiba
    convertido em centímetro e milímetros. '''

n = float(input('Uma distância em metros: '))
km = n/1000
hm = n/100
dam = n/10
dm = n*10
cm = n*100
mm = n*1000
print(f'A medida de {n}m corresponde a: ')
print(f'{km}km')
print(f'{hm}hm')
print(f'{dam}dam')
print(f'{dm:.0f}dm')
print(f'{cm:.0f}cm')
print(f'{mm:.0f}mm')